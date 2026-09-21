#!/usr/bin/env python3
"""Append one STATE.jsonl line. Usage: state.py UNIT EVENT AGENT_ID MECHANISM [OUTPUT_FILE|-] [VALIDATOR] [NOTE]"""
import sys, json, hashlib, datetime, os
here = os.path.dirname(os.path.abspath(__file__))
state = os.path.join(os.path.dirname(here), "STATE.jsonl")
a = sys.argv[1:] + [""] * 7
unit, event, agent, mech, out, val, note = a[:7]
sha = None
if out and out != "-" and os.path.exists(out):
    sha = hashlib.sha256(open(out, "rb").read()).hexdigest()
rec = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "unit": unit, "event": event, "agent_id": agent or None, "model": "opus",
       "mechanism": mech or None, "output_sha256": sha, "validator": val or None}
if out and out != "-":
    rec["output"] = os.path.relpath(out, os.path.dirname(os.path.dirname(here)))
if note: rec["note"] = note
open(state, "a").write(json.dumps(rec) + "\n")
print(json.dumps(rec))
