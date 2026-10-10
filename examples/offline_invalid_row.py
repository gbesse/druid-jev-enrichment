"""Show that an invalid JSONL row goes to review before any Jev request."""
import io
import json
from enrich import convert

source = io.StringIO('{"event_id":"synthetic-2","text":null}\n')
target, review = io.StringIO(), io.StringIO()
good, bad = convert(source, target, review, key="synthetic-fixture")
assert (good, bad) == (0, 1)
assert target.getvalue() == ""
record = json.loads(review.getvalue())
assert json.loads(record["raw"])["event_id"] == "synthetic-2"
assert record["errorType"] == "DecisionError"
print(json.dumps({"caseId": "invalid_text_row", "enriched": good, "review": bad,
                  "preservedRawRow": True, "networkCalls": 0}, indent=2))
