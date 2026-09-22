#!/usr/bin/env python3
"""Append one line to R4/STATE.jsonl (the R4 manager is the only writer). Usage: state.py key=value ..."""
import json, sys, os, datetime
R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
for a in sys.argv[1:]:
    k, v = a.split("=", 1)
    d[k] = v
with open(os.path.join(R4, "STATE.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps(d) + "\n")
