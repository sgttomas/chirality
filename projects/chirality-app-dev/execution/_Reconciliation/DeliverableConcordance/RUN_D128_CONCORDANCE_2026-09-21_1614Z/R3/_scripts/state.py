#!/usr/bin/env python3
"""Append one line to R3/STATE.jsonl (manager is the only writer). Usage: state.py key=value ..."""
import json, sys, os, datetime
from r3lib import R3
d = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
for a in sys.argv[1:]:
    k, v = a.split("=", 1)
    d[k] = v
with open(os.path.join(R3, "STATE.jsonl"), "a", encoding="utf-8") as f:
    f.write(json.dumps(d) + "\n")
