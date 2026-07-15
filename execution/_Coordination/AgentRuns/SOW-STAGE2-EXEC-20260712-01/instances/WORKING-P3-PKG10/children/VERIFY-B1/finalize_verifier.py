#!/usr/bin/env python3
"""Produce PKG-10-B1 verifier replacement, simulation, and closure evidence."""
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
HERE = RUN / "instances/WORKING-P3-PKG10/children/VERIFY-B1"
CAND = RUN / "candidates/W_P3/PIP-PKG10"
HEAD = "4d153302c3c4cd42578936db160c2bac1270225a"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-10-01": ("42e3069a9f8d0401126b8f62cc03bb5def8065ae1fa06f7c9bde95bf2dcac8ea", 36, 379),
    "DEL-10-02": ("f4610a3931b00d76000e6b80c4132a57756982744afbe116545abdd9226f6e54", 29, 270),
    "DEL-10-03": ("f46752c77887d13bad6d50b29b6bbd65bcb4c669ac474b44bc20203a23b0d5f3", 36, 384),
    "DEL-10-04": ("1b7eb7b1a11810a6d88da3c1c105263bcf991cc19c47b0cb59ee21868292e474", 32, 291),
    "DEL-10-05": ("f22605f1b2d67ea4f22624bd108b3fe701ce67f03516d17e8c92dc7e3ba183ea", 30, 270),
}
'''
code = prefix + "\ndef sha(path: Path) -> str:" + remainder
code = code.replace('RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv"', 'RUN / "snapshots/W_P3/preflight/P3_MANIFEST.tsv"')
code = code.replace('"mappings": 151, "source_lines": 1343', '"mappings": 163, "source_lines": 1594')
code = code.replace('"mapping_rows": 151, "source_lines": 1343', '"mapping_rows": 163, "source_lines": 1594')
code = code.replace('`DEL-06-01..05`', '`DEL-10-01..05`')
code = code.replace('151/151 mappings and 1,343/1,343 physical source lines', '163/163 mappings and 1,594/1,594 physical source lines')
code = code.replace('WORKING-P2-PKG06/children/VERIFY-B1/', 'WORKING-P3-PKG10/children/VERIFY-B1/')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
