#!/usr/bin/python3
from pathlib import Path
import sys

EXPECTED = {
    "OWNER_RUNBOOK.md": "<<UNFILLED:OWNER_RUNBOOK>>",
    "scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh": "<<UNFILLED:OWNER_ENVIRONMENT_PREFLIGHT>>",
    "scripts/CAPTURE_TRACE_EVIDENCE.zsh": "<<UNFILLED:CAPTURE_TRACE_EVIDENCE>>",
    "EVIDENCE_CAPTURE.md": "<<UNFILLED:EVIDENCE_CAPTURE>>",
    "LEDGER_CITATION.md": "<<UNFILLED:LEDGER_CITATION>>",
    "APPROVAL_REQUEST.md": "<<UNFILLED:APPROVAL_REQUEST>>",
}

root = Path(sys.argv[1])
census = Path(sys.argv[2])
mode = sys.argv[3] if len(sys.argv) > 3 else "pre"
filled = 0
for rel, sentinel in EXPECTED.items():
    data = (root / rel).read_text(encoding="utf-8")
    if mode == "pre":
        ok = data == sentinel + "\n"
        state = "STUB" if ok else "INVALID"
    else:
        ok = sentinel not in data and bool(data.strip())
        state = "FILLED" if ok else "UNFILLED"
        filled += int(ok)
    print(f"{state}|{rel}|{len(data.encode('utf-8'))}")
    if not ok:
        sys.exit(1)
if mode == "pre":
    expected_census = "<<UNFILLED:N1_SELF_CENSUS>>\n"
    if census.read_text(encoding="utf-8") != expected_census:
        print("INVALID|census")
        sys.exit(1)
else:
    census_text = census.read_text(encoding="utf-8")
    for rel in EXPECTED:
        if f"| `{rel}` | FILLED |" not in census_text:
            print(f"CENSUS_MISMATCH|{rel}")
            sys.exit(1)
print(f"PASS|mode={mode}|filled={filled}|total={len(EXPECTED)}")
