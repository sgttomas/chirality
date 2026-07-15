#!/usr/bin/env python3
"""Produce PKG-08-B1 verifier replacement, simulation, and closure evidence."""
from pathlib import Path

repo = Path(__file__).resolve().parents[8]
template = repo / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG06/children/VERIFY-B1/finalize_verifier.py"
source = template.read_text(encoding="utf-8")
remainder = source.split("def sha(path: Path) -> str:", 1)[1]
prefix = '''#!/usr/bin/env python3
from __future__ import annotations
import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/WORKING-P2-PKG08/children/VERIFY-B1"
CAND = RUN / "candidates/W_P2/PIP-PKG08"
HEAD = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-08-01": ("ae40e3b7aa1b3f45c00be3a69abe6f75a16903e12cccf7890b9fd092eed57625", 33, 290),
    "DEL-08-02": ("a9787c24286a41a34652e4be9a0a322ed4ee75006160ec0312de39a23b10348a", 28, 253),
    "DEL-08-03": ("00ece42387a622e14b7435f1f2edb9126daef8c3edff4fdb919e9f54844d4d30", 31, 341),
    "DEL-08-04": ("32477279c39d33fee85454ee646f3d337b8e4ab6d0b74851a38c382f97e5a70f", 28, 257),
    "DEL-08-05": ("1461a2ad7e2ff15d0422d5a4a9c1c327b23cfe516aac06a15f8f3e261745a987", 33, 347),
}
'''
code = prefix + "\ndef sha(path: Path) -> str:" + remainder
code = code.replace('"mappings": 151, "source_lines": 1343', '"mappings": 153, "source_lines": 1488')
code = code.replace('"mapping_rows": 151, "source_lines": 1343', '"mapping_rows": 153, "source_lines": 1488')
code = code.replace('`DEL-06-01..05`', '`DEL-08-01..05`')
code = code.replace('151/151 mappings and 1,343/1,343 physical source lines', '153/153 mappings and 1,488/1,488 physical source lines')
code = code.replace('WORKING-P2-PKG06/children/VERIFY-B1/', 'WORKING-P2-PKG08/children/VERIFY-B1/')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
