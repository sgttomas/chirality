#!/usr/bin/env python3
"""Produce PKG-09-B1 verifier replacement, simulation, and closure evidence."""
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
HERE = RUN / "instances/WORKING-P2-PKG09/children/VERIFY-B1"
CAND = RUN / "candidates/W_P2/PIP-PKG09"
HEAD = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-09-01": ("fe691b3f75fa90c28619ffb61f1d4bdabe15640c54ae355abf5f92327c836908", 36, 270),
    "DEL-09-02": ("d28109b059328ce938bba9a286e6ffbe014b80dcad4a2949dafef313ea3c3c23", 33, 253),
    "DEL-09-03": ("496fdb82e3c7b026d19c828dab0b864ff9bbfaee0953e205b06dd2fc80dcea40", 31, 275),
    "DEL-09-04": ("f8d63d1c20c52a869c75bf0e139922dd1006eaeb70d43108758dcfbb3c9c5135", 28, 267),
    "DEL-09-05": ("e398d741a5c51ff5ab52f525b235fb92c54a34ae0455fe59dbe787ba0a459f6b", 34, 292),
}
'''
code = prefix + "\ndef sha(path: Path) -> str:" + remainder
code = code.replace('"mappings": 151, "source_lines": 1343', '"mappings": 162, "source_lines": 1357')
code = code.replace('"mapping_rows": 151, "source_lines": 1343', '"mapping_rows": 162, "source_lines": 1357')
code = code.replace('`DEL-06-01..05`', '`DEL-09-01..05`')
code = code.replace('151/151 mappings and 1,343/1,343 physical source lines', '162/162 mappings and 1,357/1,357 physical source lines')
code = code.replace('WORKING-P2-PKG06/children/VERIFY-B1/', 'WORKING-P2-PKG09/children/VERIFY-B1/')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
