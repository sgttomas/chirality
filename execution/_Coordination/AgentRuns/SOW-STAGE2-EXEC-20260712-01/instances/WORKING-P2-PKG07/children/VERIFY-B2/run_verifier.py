#!/usr/bin/env python3
"""PKG-07 Batch-02 binding of the accepted package-verifier harness."""
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
    "DEL-07-06": ("321a9c47e59cd544ddb88842bec108ac418a0760023cb012dedfff3bc955d1f3", "d87b39a528422b33c469c14fab5861cc85fa77622ca684add6374bb0f0b78662", "fdebc50d333ef0884e35525c31a9220ae9868430af989c88d66427bec38d69fa", 35, 300),
    "DEL-07-07": ("5f2f32555e9fac92e9ba140a3c1eb93dd216af47cde0d1eb6ea3a910eadcef20", "614be909dd2ee17f5c2f2ba2c1a1608679bb17edaeaf767d1acd266061a16a3a", "e5e6be32217a8a9691702b08b2a47dc9844ed7de87da4d198f79cf3880087a03", 33, 318),
    "DEL-07-08": ("b964c78752ccbd51cc02e956360bdb1a8274aec677152c8b3a4b3dea0ad0615b", "ef74178472dca39a81131f059aca5beaf700b9e1e23f7e8c89da12290aff81d7", "e6fc997fd5649ba4bc962ef290f0c000548b1f527e89fd7bb668f23369a393a6", 29, 269),
}
SEEDS = {
    "DEL-07-06": ("An accessibility and engineering-review usability baseline covering keyboard access, labels, readability, large-model navigation, unit and diagnostic visibility, warning separation, and report-facing review boundaries is produced without asserting an unapproved conformance level.", "The contract preserves the accessibility and engineering-review baseline, keeps the measurable contrast/readability target explicitly human-owned and TBD, separates diagnostic classes, preserves units and provenance, and makes no certification, compliance, or professional-approval claim.", "Validate the contract and review source parity, keyboard and labeling expectations, diagnostic and warning separation, unit/provenance visibility, protected-content boundaries, professional-boundary language, and every retained TBD or governed residual."),
    "DEL-07-07": ("A solve-execution UX contract covering background job launch, service-reported progress, cancellation requests and terminal states, diagnostics, blocked-state separation, reproducibility signals, and professional-review boundaries is produced.", "The contract preserves service-owned progress and cancellation semantics, complete diagnostic fields and warning classes, separate solve and rule-check readiness, reproducibility traceability, and no invented progress, silent defaults, compliance status, or professional approval.", "Validate the contract and review source parity, job-boundary routing, progress and cancellation semantics, diagnostic fields and warning classes, missing-data separation, reproducibility metadata, protected-content limits, and every retained TBD or governed residual."),
    "DEL-07-08": ("A design-authoring and comparison workspace contract covering design knowledge and constraints, operation/diff review, state/run browsing, comparison tables and overlays, upstream-contract use, and application-service mutation boundaries is produced.", "The contract preserves the declared authoring and comparison surfaces, upstream ownership of backend schemas and engines, proposed/validated/accepted/audited state distinctions, diagnostic visibility, no silent defaults, and no external-validation or professional-approval claim.", "Validate the contract and review source parity, declared workspace surfaces, upstream dependency boundaries, command-intent mutation routing, operation and state distinctions, diagnostics and missing-data visibility, comparison reliance boundaries, and every retained TBD or governed residual."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG07/children/VERIFY-B2"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P2/PIP-PKG07"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-07"')
code = code.replace('cmd.extend(["--project-scope-ref", ref])', 'cmd.extend(["--project-scope-ref", ref.strip()])')
code = code.replace('cmd.extend(["--package-objective-ref", ref])', 'cmd.extend(["--package-objective-ref", ref.strip()])')
code = code.replace('mutated.write_bytes(mutated.read_bytes() + b"\\n")', 'mutated.write_bytes(mutated.read_bytes() + b"<!-- verifier-negative-mutation -->\\n")')
code = code.replace('"retries": 3 if did == "DEL-02-01" else 0', '"retries": 0')
code = code.replace('"failures": 3 if did == "DEL-02-01" else 0', '"failures": 0')
code = code.replace("{3 if did == 'DEL-02-01' else 0}\\t{3 if did == 'DEL-02-01' else 0}", "0\\t0")
code = code.replace('failures=3 if did == "DEL-02-01" else 0, retries=3 if did == "DEL-02-01" else 0', 'failures=0, retries=0')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
code = code.replace('members_complete=5', 'members_complete=len(EXPECTED)')
code = code.replace('"members_complete": 5', '"members_complete": len(EXPECTED)')
code = code.replace('"fail_closed_probes": 35', '"fail_closed_probes": 7 * len(EXPECTED)')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
