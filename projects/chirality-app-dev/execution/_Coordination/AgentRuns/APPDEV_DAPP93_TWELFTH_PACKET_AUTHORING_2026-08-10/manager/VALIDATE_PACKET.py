#!/usr/bin/python3
from hashlib import sha256
from pathlib import Path
import re
import subprocess
import sys

RG = "/opt/homebrew/Cellar/ripgrep/15.2.0/bin/rg"
PATTERNS = [
    r"C[0-9]{3,}",
    r"A3-OP-[0-9]{3}",
    r"R[0-9]+-C[0-9]{3,}",
    r"ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+",
]
PACKET_FILES = [
    "OWNER_RUNBOOK.md",
    "scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh",
    "scripts/CAPTURE_TRACE_EVIDENCE.zsh",
    "EVIDENCE_CAPTURE.md",
    "LEDGER_CITATION.md",
    "APPROVAL_REQUEST.md",
]

if len(sys.argv) != 5 or sys.argv[1] != "--mode":
    raise SystemExit("usage: VALIDATE_PACKET.py --mode fixture|packet ROOT SPECS")
mode, root, specs = sys.argv[2], Path(sys.argv[3]).resolve(), Path(sys.argv[4]).resolve()
if mode not in {"fixture", "packet", "reject-fixture"}:
    raise SystemExit("invalid mode")

manifest = specs / "SPEC_IDENTITIES.sha256"
for row in manifest.read_text(encoding="utf-8").splitlines():
    expected, name = row.split("  ", 1)
    observed = sha256((specs / name).read_bytes()).hexdigest()
    if observed != expected:
        print(f"SPEC_CHANGED|{name}|{observed}|{expected}")
        raise SystemExit(1)

hits = []
for rel in PACKET_FILES:
    path = root / rel
    if not path.is_file():
        print(f"MISSING|{rel}")
        raise SystemExit(1)
    data = path.read_text(encoding="utf-8")
    if not data.strip() or "<<UNFILLED:" in data:
        print(f"UNFILLED|{rel}")
        raise SystemExit(1)
    for pattern in PATTERNS:
        proc = subprocess.run(
            [RG, "--line-number", "--no-heading", "--color", "never", "-e", pattern, str(path)],
            text=True,
            capture_output=True,
            check=False,
            env={"PATH": "/opt/homebrew/Cellar/ripgrep/15.2.0/bin:/usr/bin:/bin"},
            cwd=root,
        )
        if proc.returncode not in {0, 1}:
            print(f"RG_ERROR|{rel}|pattern={pattern}|exit={proc.returncode}|{proc.stderr.strip()}")
            raise SystemExit(1)
        if proc.returncode == 0:
            for line in proc.stdout.splitlines():
                hits.append((rel, pattern, line))
                print(f"HIT|file={rel}|pattern={pattern}|location={line}")

if mode == "reject-fixture":
    if not hits:
        print("REJECT_FIXTURE_FAILED|no classified hit")
        raise SystemExit(1)
    print(f"PASS_EXPECTED_REJECTION|classified_hits={len(hits)}")
    raise SystemExit(2)
if hits:
    print(f"REJECT|classified_hits={len(hits)}")
    raise SystemExit(2)
print(f"PASS|mode={mode}|files={len(PACKET_FILES)}|historical_hits=0|embedded_rg={RG}")
