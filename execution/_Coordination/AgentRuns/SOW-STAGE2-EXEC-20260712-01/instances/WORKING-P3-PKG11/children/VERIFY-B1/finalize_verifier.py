#!/usr/bin/env python3
"""Produce PKG-11-B1 verifier replacement, simulation, and closure evidence."""
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
HERE = RUN / "instances/WORKING-P3-PKG11/children/VERIFY-B1"
CAND = RUN / "candidates/W_P3/PIP-PKG11"
HEAD = "4d153302c3c4cd42578936db160c2bac1270225a"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-11-01": ("46cba20a315bffff070c2ece60c87ea36b6c8021afdbba6650f62c30a888b4ee", 28, 273),
    "DEL-11-02": ("c71fa0a2749ae82e13c350980b65af676efc0f208c1fd3939747d472d7255e91", 34, 373),
    "DEL-11-03": ("b5e973588e062a9e85e4e7dc446fae66d654cfa9b778845cbef2b51bf2ea909d", 29, 375),
    "DEL-11-04": ("9fdf56afa1e57bff58c4eb000d45880a8ee495e7ab6a33a6183e642c28f3158a", 32, 267),
    "DEL-11-05": ("94153b259b6a942fa3492e0da9d614028fdcd8297b099c7c54eb9feb9c6e46e2", 36, 300),
}
'''
code = prefix + "\ndef sha(path: Path) -> str:" + remainder
code = code.replace('RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv"', 'RUN / "snapshots/W_P3/preflight/P3_MANIFEST.tsv"')
code = code.replace('"mappings": 151, "source_lines": 1343', '"mappings": 159, "source_lines": 1588')
code = code.replace('"mapping_rows": 151, "source_lines": 1343', '"mapping_rows": 159, "source_lines": 1588')
code = code.replace('`DEL-06-01..05`', '`DEL-11-01..05`')
code = code.replace('151/151 mappings and 1,343/1,343 physical source lines', '159/159 mappings and 1,588/1,588 physical source lines')
code = code.replace('WORKING-P2-PKG06/children/VERIFY-B1/', 'WORKING-P3-PKG11/children/VERIFY-B1/')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
