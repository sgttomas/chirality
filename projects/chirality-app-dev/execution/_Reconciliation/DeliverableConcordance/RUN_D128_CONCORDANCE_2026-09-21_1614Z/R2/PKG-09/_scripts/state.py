#!/usr/bin/env python3
"""Append one line to R2/PKG-09/STATE.jsonl (PKG-09 manager is the only writer).
Usage: state.py <unit> <event> <agent_id|-> [output_file|-] [validator|-] [note]"""
import datetime, hashlib, json, os, sys
pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a = sys.argv[1:] + [""] * 6
unit, event, agent, out, val, note = a[:6]
sha = hashlib.sha256(open(out, "rb").read()).hexdigest() if out not in ("", "-") and os.path.exists(out) else None
rec = {"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "unit": unit, "event": event,
       "agent_id": None if agent in ("", "-") else agent, "model": "opus (Claude Opus 5)",
       "mechanism": "Claude Code Agent tool, harness-native descendant of the PKG-09 R2 manager (D-GOV-35)",
       "output": os.path.relpath(os.path.abspath(out), pkg) if sha else None, "output_sha256": sha,
       "validator": None if val in ("", "-") else val}
if note: rec["note"] = note
open(os.path.join(pkg, "STATE.jsonl"), "a").write(json.dumps(rec) + "\n")
print(json.dumps(rec))
