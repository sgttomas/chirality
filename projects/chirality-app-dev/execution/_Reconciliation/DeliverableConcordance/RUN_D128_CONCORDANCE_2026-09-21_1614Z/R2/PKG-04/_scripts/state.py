#!/usr/bin/env python3
"""Append one line to R2/PKG-04/STATE.jsonl (the PKG-04 manager is the only writer).
Usage: state.py UNIT EVENT AGENT_ID [OUTPUT_FILE|-] [VALIDATOR] [NOTE]"""
import sys, json, hashlib, datetime, os
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
a = sys.argv[1:] + [""] * 6
unit, event, agent, out, val, note = a[:6]
rec = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "unit": unit, "event": event, "agent_id": agent or None, "model": "opus",
       "mechanism": "claude-code-harness-native-descendant (D-GOV-35)", "parent": "PKG-04 WORKING_ITEMS manager"}
if out and out != "-":
    rec["output"] = os.path.relpath(out, P)
    rec["output_sha256"] = hashlib.sha256(open(out, "rb").read()).hexdigest() if os.path.exists(out) else None
if val: rec["validator"] = val
if note: rec["note"] = note
open(os.path.join(P, "STATE.jsonl"), "a").write(json.dumps(rec) + "\n")
print(json.dumps(rec))
