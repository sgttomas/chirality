#!/usr/bin/env python3
"""Append one line to R2/SURFACES/STATE.jsonl (R1b manager is the only writer).
Usage: state_log.py <unit> <event> <agent_id> [output_file] [validator_result]"""
import datetime, hashlib, json, os, sys
run = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
unit, event, agent = sys.argv[1:4]
out = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
val = sys.argv[5] if len(sys.argv) > 5 else None
sha = hashlib.sha256(open(out, "rb").read()).hexdigest() if out and os.path.exists(out) else None
rec = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "unit": unit,
       "event": event, "agent_id": agent, "model": "opus (Claude Opus 5)",
       "mechanism": "Claude Code Agent tool, harness-native descendant of the R1b manager (D-GOV-35)",
       "output_sha256": sha, "validator": val}
with open(os.path.join(run, "R2", "SURFACES", "STATE.jsonl"), "a") as fh:
    fh.write(json.dumps(rec) + "\n")
print(json.dumps(rec))
