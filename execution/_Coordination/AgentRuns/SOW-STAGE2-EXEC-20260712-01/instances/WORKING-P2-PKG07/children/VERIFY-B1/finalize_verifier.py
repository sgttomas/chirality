#!/usr/bin/env python3
"""Produce PKG-07-B1 verifier replacement, simulation, and closure evidence."""
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
HERE = RUN / "instances/WORKING-P2-PKG07/children/VERIFY-B1"
CAND = RUN / "candidates/W_P2/PIP-PKG07"
HEAD = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-07-01": ("09a473cad3af6b06ae6e1ba1d5157d8ea8ccef82b3a9a301ac8adc2bc5557dd8", 32, 326),
    "DEL-07-02": ("112fee6a944b72a6450994fbea3aa6b2561705cf2430303dd900d10238378c5d", 37, 279),
    "DEL-07-03": ("3dff5e819cad1b64162ca50d2d676ade5812d50ded13043c5d1bb5b9d6879b7c", 41, 408),
    "DEL-07-04": ("f9a693fad005c503c30cece6298353e7f273c0e39dd14677b589ca9424631f10", 32, 250),
    "DEL-07-05": ("5144c44383fb01ae19ae0d9180d604ef171e8bb94b57bf53d37ef9fb9f7d5cdd", 33, 272),
}
'''
code = prefix + "\ndef sha(path: Path) -> str:" + remainder
code = code.replace('"mappings": 151, "source_lines": 1343', '"mappings": 175, "source_lines": 1535')
code = code.replace('"mapping_rows": 151, "source_lines": 1343', '"mapping_rows": 175, "source_lines": 1535')
code = code.replace('`DEL-06-01..05`', '`DEL-07-01..05`')
code = code.replace('151/151 mappings and 1,343/1,343 physical source lines', '175/175 mappings and 1,535/1,535 physical source lines')
code = code.replace('WORKING-P2-PKG06/children/VERIFY-B1/', 'WORKING-P2-PKG07/children/VERIFY-B1/')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
