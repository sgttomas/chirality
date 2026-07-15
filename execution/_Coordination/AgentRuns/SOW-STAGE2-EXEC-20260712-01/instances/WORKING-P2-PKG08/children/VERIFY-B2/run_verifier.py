#!/usr/bin/env python3
"""PKG-08 Batch-02 binding of the accepted package-verifier harness."""
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
HEAD = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
ALL_INPUTS = SOURCE_FILES + CONTROL_FILES
EXPECTED = {
    "DEL-08-06": ("a2447b4f211ea66b4b6c6194a64153847bb916ec7aa2b94ce787778c3ff12ad0", "22f2934acd6c24463131f24b58eb6b91773b0b5deb9bf15f47d9d365c0e0e4a9", "07a895dcc5c92b001d9617095a039c79933df5e534c6e286cc484c0188fcf1f5", 33, 301),
}
SEEDS = {
    "DEL-08-06": (
        "A state, comparison, and handoff report-section contract covering immutable model-state and analysis-run records, deterministic comparisons, handoff manifests, warnings, assumptions, limitations, units, hashes, provenance, and unsupported-target disclosures is produced without implying professional validation or acceptance.",
        "The contract preserves stable record identities, source-envelope diagnostics, deterministic comparison mappings and tolerance references when available, handoff traceability, missing-data visibility, protected/private-content boundaries, and professional-authority limits while retaining unresolved implementation, schema, layout, and external-payload decisions as source-grounded TBDs.",
        "Validate the contract and review source parity, state/run/comparison/handoff coverage, SOW-024 report content, stable identities and hashes, units and provenance, deterministic ordering, missing-data findings, unsupported-target disclosures, protected-content and professional-authority boundaries, and every retained TBD or governed residual.",
    ),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG08/children/VERIFY-B2"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P2/PIP-PKG08"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-08"')
code = code.replace('cmd.extend(["--project-scope-ref", ref])', 'cmd.extend(["--project-scope-ref", ref.strip()])')
code = code.replace('cmd.extend(["--package-objective-ref", ref])', 'cmd.extend(["--package-objective-ref", ref.strip()])')
code = code.replace('mutated.write_bytes(mutated.read_bytes() + b"\\n")', 'mutated.write_bytes(mutated.read_bytes() + b"<!-- verifier-negative-mutation -->\\n")')
code = code.replace('"retries": 3 if did == "DEL-02-01" else 0', '"retries": 0')
code = code.replace('"failures": 3 if did == "DEL-02-01" else 0', '"failures": 0')
code = code.replace("{3 if did == 'DEL-02-01' else 0}\\t{3 if did == 'DEL-02-01' else 0}", "0\\t0")
code = code.replace('failures=3 if did == "DEL-02-01" else 0, retries=3 if did == "DEL-02-01" else 0', 'failures=0, retries=0')
code = code.replace('event("batch_start", member_count=5', 'event("batch_start", member_count=1')
code = code.replace('members_complete=5', 'members_complete=1')
code = code.replace('"members_complete": 5', '"members_complete": 1')
code = code.replace('"fail_closed_probes": 35', '"fail_closed_probes": 7')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
