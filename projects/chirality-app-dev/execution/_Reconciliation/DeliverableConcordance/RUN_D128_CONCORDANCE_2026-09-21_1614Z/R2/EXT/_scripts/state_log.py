#!/usr/bin/env python3
"""Append one line to R2/EXT/STATE.jsonl (the EXT manager is the only writer).
Usage: state_log.py <unit> <event> <agent_id> [key=value ...]"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "STATE.jsonl")
unit, event, agent = sys.argv[1:4]
rec = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "manager": "EXT", "unit": unit, "event": event, "agent": agent,
       "model": "opus", "mechanism": "Claude Code harness-native descendant (D-GOV-35)"}
for kv in sys.argv[4:]:
    k, _, v = kv.partition("=")
    rec[k] = v
with open(OUT, "a", encoding="utf-8") as fh:
    fh.write(json.dumps(rec, sort_keys=True) + "\n")
print(json.dumps(rec))
