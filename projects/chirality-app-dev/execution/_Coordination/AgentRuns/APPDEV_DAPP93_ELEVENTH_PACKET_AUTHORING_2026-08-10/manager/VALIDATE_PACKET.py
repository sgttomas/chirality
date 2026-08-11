#!/usr/bin/python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import subprocess

RUN_REL = pathlib.Path("projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10")
PACKET = [
    "packet/OWNER_RUNBOOK.md",
    "packet/scripts/OWNER_PREFLIGHT.zsh",
    "packet/scripts/lldb-signal-trace.txt",
    "packet/EVIDENCE_CAPTURE.md",
    "packet/LEDGER_CITATION.md",
    "packet/APPROVAL_REQUEST.md",
]
PATTERN = r"C[0-9]{3,}|A3-OP-[0-9]{3}|R[0-9]+-C[0-9]{3,}|ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+"


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--phase", choices=["fanin", "freeze", "closeout"], required=True)
args = parser.parse_args()
root = pathlib.Path.cwd() / RUN_REL
errors: list[str] = []
for rel in PACKET:
    path = root / rel
    if not path.is_file() or path.read_text(encoding="utf-8").startswith("STUB — UNFILLED"):
        errors.append(f"UNFILLED {rel}")

with (root / "returns/N1_OUTPUT_CENSUS.csv").open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh))
if len(rows) != 6 or any(r.get("status") != "FILLED" for r in rows):
    errors.append("census not 6/6 FILLED")
if [r.get("path") for r in rows] != PACKET:
    errors.append("census path order mismatch")

combined = "\n".join((root / rel).read_text(encoding="utf-8") for rel in PACKET if (root / rel).is_file())
cp = subprocess.run(["/opt/homebrew/bin/rg", "-n", "-e", PATTERN, *[str(root / p) for p in PACKET]], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if cp.returncode != 1 or cp.stdout:
    errors.append("historical command identity scan not clean")
if "dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809" not in combined:
    errors.append("ledger citation missing")
for required in ["OWNER_PREFLIGHT", "AGENT_PROVEN", "150", "process detach", "quit", "NO EXECUTION AUTHORITY", "credential"]:
    if required not in combined:
        errors.append(f"required concept missing: {required}")

probe_script = root / "packet/scripts/OWNER_PREFLIGHT.zsh"
syntax = subprocess.run(["/bin/zsh", "-n", str(probe_script)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if syntax.returncode != 0:
    errors.append("OWNER_PREFLIGHT.zsh syntax probe failed")
lldb_text = (root / "packet/scripts/lldb-signal-trace.txt").read_text(encoding="utf-8")
for token in ["process handle SIGTERM", "__sigtramp", "uv__signal_handler", "SignalWrap", "Browser::Quit", "NSApplication terminate", "process continue"]:
    if token not in lldb_text:
        errors.append(f"LLDB script token missing: {token}")

report = ["# Manager packet validation", "", f"Phase: `{args.phase}`", "", f"Verdict: `{'BLOCK' if errors else 'PASS'}`", "", f"- Packet files: {len(PACKET)} (five components).", f"- Census: {len(rows)}/6 rows; filled={sum(r.get('status') == 'FILLED' for r in rows)}.", f"- Full-pattern historical-ID scan exit: {cp.returncode}; stdout bytes: {len(cp.stdout.encode())}.", f"- OWNER_PREFLIGHT script syntax exit: {syntax.returncode}.", "- LLDB operative attach/signal/detach commands: REVIEWED_NOT_EXECUTED.", "- Product/runtime/system effects: none.", "- Native context telemetry: unavailable."]
if errors:
    report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
report.append("")
(root / f"validation/MANAGER_{args.phase.upper()}_VALIDATION.md").write_text("\n".join(report), encoding="utf-8")
if errors:
    raise SystemExit("BLOCK: " + "; ".join(errors))

if args.phase in {"freeze", "closeout"}:
    lines = [f"{sha(root / rel)}  {rel}" for rel in PACKET]
    (root / "freeze/FROZEN_PACKET.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(hashlib.sha256((root / "freeze/FROZEN_PACKET.sha256").read_bytes()).hexdigest())
else:
    print("FANIN PASS")
