import io
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
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

    def test_cli_outputs_are_private_and_symlinks_are_rejected(self):
        script = Path(__file__).resolve().parents[1] / "enrich.py"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.jsonl"
            target = root / "enriched.jsonl"
            review = root / "review.jsonl"
            source.write_text("invalid\n", encoding="utf-8")
            target.write_text("old data", encoding="utf-8")
            target.chmod(0o644)
            command = [sys.executable, str(script), str(source), str(target), str(review)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o600)
            self.assertEqual(stat.S_IMODE(review.stat().st_mode), 0o600)
            self.assertEqual(target.read_text(encoding="utf-8"), "")
            self.assertIn('"raw": "invalid"', review.read_text(encoding="utf-8"))

            victim = root / "victim.jsonl"
            victim.write_text("keep", encoding="utf-8")
            review.unlink()
            review.symlink_to(victim)
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(victim.read_text(encoding="utf-8"), "keep")
