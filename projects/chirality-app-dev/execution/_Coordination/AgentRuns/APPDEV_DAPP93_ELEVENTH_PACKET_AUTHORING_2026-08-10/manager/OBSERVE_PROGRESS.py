#!/usr/bin/python3
import json
import pathlib

root = pathlib.Path.cwd() / "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ELEVENTH_PACKET_AUTHORING_2026-08-10"
packet = [
    root / "packet/OWNER_RUNBOOK.md",
    root / "packet/scripts/OWNER_PREFLIGHT.zsh",
    root / "packet/scripts/lldb-signal-trace.txt",
    root / "packet/EVIDENCE_CAPTURE.md",
    root / "packet/LEDGER_CITATION.md",
    root / "packet/APPROVAL_REQUEST.md",
]
files = [path for path in root.rglob("*") if path.is_file()]
filled = sum(not path.read_text(encoding="utf-8").startswith("STUB — UNFILLED") for path in packet)
print(json.dumps({"durable_file_count": len(files), "durable_byte_total": sum(path.stat().st_size for path in files), "filled_stubs": filled, "unfilled_stubs": 6 - filled}, sort_keys=True))
