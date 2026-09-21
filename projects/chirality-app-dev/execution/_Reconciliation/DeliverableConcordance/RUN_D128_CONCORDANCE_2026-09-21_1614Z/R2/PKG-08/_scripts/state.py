#!/usr/bin/env python3
"""Append one line to R2/PKG-08/STATE.jsonl (the PKG-08 manager is the only writer).
Usage: state.py <unit> <event> <agent_id> [output_file] [validator_result] [note]"""
import datetime, hashlib, json, os, sys
pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
unit, event, agent = sys.argv[1:4]
out = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] else None
val = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else None
note = sys.argv[6] if len(sys.argv) > 6 else None
p = os.path.join(pkg, out) if out and not os.path.isabs(out) else out
sha = hashlib.sha256(open(p, "rb").read()).hexdigest() if p and os.path.exists(p) else None
rec = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "unit": unit,
       "event": event, "agent_id": agent, "model": "opus (Claude Opus 5)",
       "mechanism": "Claude Code Agent tool, harness-native descendant of the PKG-08 R2 manager (D-GOV-35)",
       "output": out, "output_sha256": sha, "validator": val, "note": note}
with open(os.path.join(pkg, "STATE.jsonl"), "a") as fh:
    fh.write(json.dumps(rec) + "\n")
print(json.dumps(rec))
