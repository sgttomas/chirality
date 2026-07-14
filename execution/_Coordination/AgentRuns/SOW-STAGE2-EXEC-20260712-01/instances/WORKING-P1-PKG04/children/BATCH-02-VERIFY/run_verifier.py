#!/usr/bin/env python3
"""PKG-04 Batch-02 binding of the accepted same-package verifier harness."""
from pathlib import Path

repo = Path(__file__).resolve().parents[8]
template = repo / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02/verifier.py"
source = template.read_text(encoding="utf-8")
remainder = source.split("def now() -> str:", 1)[1]

prefix = '''#!/usr/bin/env python3
from __future__ import annotations
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
HEAD = "2a5e3825d8d2fc4943742a53ccad3b89c4c81902"
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
ALL_INPUTS = SOURCE_FILES + CONTROL_FILES
EXPECTED = {
    "DEL-04-06": ("66b02314562b8aa65e09e7cd3d450bc84d9c1d5964aa2dbb5c18342a6b70da07", "4d314c20a833c0c7a9addafd6d8d63f588d39859e8cf692cf8180b907dbc10f7", "23dd49a6a4cec604a5ae563af542572f080ea9c58fcb1cc391eea9bcfae937ad", 33, 276),
}
SEEDS = {
    "DEL-04-06": ("A solver-diagnostics and singularity-detection contract covering deterministic machine-readable diagnostic envelopes, mechanics-only solver status, singularity and conditioning evidence, nonconvergence, invalid model and numeric inputs, provenance, remediation, unit metadata, and reviewable result-envelope interfaces is produced for the declared scope and objectives.", "The contract preserves the accepted diagnostic codes and mappings, caller-supplied threshold and tolerance behavior, explicit sparse-solver and tolerance-policy TBD diagnostics, stable affected and canonical references, unit-aware provenance, rights-cleared verification evidence, and mechanics-only authority without inventing numerical policy, release readiness, professional approval, or code-compliance meaning.", "Validate the contract and review source parity, diagnostic-envelope fields and mappings, solver-status authority boundaries, singularity, restraint, topology, numeric, conditioning and nonconvergence coverage, caller-supplied policy inputs, sparse and tolerance deferrals, units and provenance, deterministic evidence, protected-content controls, and every surviving governed residual."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P1-PKG04/children/BATCH-02-VERIFY"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P1/PIP-PKG04"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-04"')
code = code.replace('cmd.extend(["--project-scope-ref", ref])', 'cmd.extend(["--project-scope-ref", ref.strip()])')
code = code.replace('cmd.extend(["--package-objective-ref", ref])', 'cmd.extend(["--package-objective-ref", ref.strip()])')
code = code.replace('mutated.write_bytes(mutated.read_bytes() + b"\\n")', 'mutated.write_bytes(mutated.read_bytes() + b"<!-- verifier-negative-mutation -->\\n")')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
code = code.replace('members_complete=5', 'members_complete=len(EXPECTED)')
code = code.replace('"members_complete": 5', '"members_complete": len(EXPECTED)')
code = code.replace('"fail_closed_probes": 35', '"fail_closed_probes": 7 * len(EXPECTED)')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
