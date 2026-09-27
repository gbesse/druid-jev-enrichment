"""Prepare Jev decision dimensions before Druid ingestion; JSONL in/out."""
import argparse
import json
import os
from pathlib import Path
from jev_core import decide
POLICY=json.loads(Path(__file__).with_name("policy.json").read_text())

def enrich_record(record, *, evaluate=decide, key=None, field="text"):
    if not isinstance(record,dict): raise ValueError("JSON object required")
    result=evaluate(record.get(field),POLICY,key or os.environ["TYPESAFE_API_KEY"])
    return {**record,"jev_outcome":result["outcome"],"jev_choice":result["choice"],"jev_probability":result["probability"],"jev_policy_version":result["policyVersion"],"jev_input_sha256":result["inputSha256"]}

def convert(source,target,review,*,evaluate=decide,key=None,field="text"):
    good=bad=0
    for line in source:
        try:
            record=json.loads(line)
            enriched=enrich_record(record,evaluate=evaluate,key=key,field=field)
            print(json.dumps(enriched,separators=(",",":")),file=target)
            good+=1
        except Exception as exc:
            # Preserve the failed row in a separate review file; no silent data loss.
            print(json.dumps({"raw":line.rstrip("\n"),"errorType":type(exc).__name__}),file=review)
            bad+=1
    return good,bad

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("review")
    parser.add_argument("--text-field",default="text")
    args=parser.parse_args()
    if len({str(Path(p).resolve()) for p in (args.input,args.output,args.review)}) != 3: parser.error("input, output and review paths must differ")
    with open(args.input,encoding="utf-8") as source,open(args.output,"w",encoding="utf-8") as target,open(args.review,"w",encoding="utf-8") as review:
        good,bad=convert(source,target,review,field=args.text_field)
    print(f"enriched={good} review={bad}")
    if bad: raise SystemExit(2)
