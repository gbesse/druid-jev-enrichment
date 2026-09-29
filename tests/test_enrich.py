import io
import json
import unittest
from enrich import enrich_record,convert
class DruidTests(unittest.TestCase):
    def test_dimensions_and_review(self):
        decision={"outcome":"incident","choice":"incident","probability":0.95,"policyVersion":"0.1.0","inputSha256":"abc"}
        evaluate=lambda text,policy,key:decision
        result=enrich_record({"text":"server down","ts":"2026-01-01T00:00:00Z"},evaluate=evaluate,key="test")
        self.assertEqual(result["jev_outcome"],"incident")
        self.assertEqual(result["ts"],"2026-01-01T00:00:00Z")
        target=io.StringIO();review=io.StringIO()
        self.assertEqual(convert(io.StringIO('{"text":"server down"}\ninvalid\n'),target,review,evaluate=evaluate,key="test"),(1,1))
        self.assertEqual(len(review.getvalue().splitlines()),1)

    def test_existing_dimensions_are_sent_to_review(self):
        target=io.StringIO();review=io.StringIO()
        evaluate=lambda *_: self.fail("Jev must not run")
        self.assertEqual(convert(io.StringIO('{"text":"x","jev_outcome":"user value"}\n'),target,review,evaluate=evaluate,key="test"),(0,1))
        self.assertEqual(target.getvalue(),"")
        self.assertIn("jev_outcome",review.getvalue())
