#!/usr/bin/env python3
"""PKG-11 Batch-01 binding of the accepted PKG-10 verifier harness."""
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
HEAD = "4d153302c3c4cd42578936db160c2bac1270225a"
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
ALL_INPUTS = SOURCE_FILES + CONTROL_FILES
EXPECTED = {
    "DEL-11-01": ("2f5a4ef163399467504c40e6d3ff77b9ffdd5bb6bad3f94048c0b8b5151f1364", "46cba20a315bffff070c2ece60c87ea36b6c8021afdbba6650f62c30a888b4ee", "93f5903cc85df8ffe3d8e12231ade6f014d08a8dc19c3ece01f7c47f1aa6378d", 28, 273),
    "DEL-11-02": ("92cd83773220669a661896d81be40cb78f9c4d2f9a79f0189e38b4400b8e7b8f", "c71fa0a2749ae82e13c350980b65af676efc0f208c1fd3939747d472d7255e91", "584ef2588cd77c90734f8822d7517fc7bd3148313b128c9b922752ec8b6dd078", 34, 373),
    "DEL-11-03": ("5ce0f70a22864ad70145940519984fe24ab4ea3c7074837b7f89d6ef67624e2d", "b5e973588e062a9e85e4e7dc446fae66d654cfa9b778845cbef2b51bf2ea909d", "88069e324bb7d48d915b280720ab9af075dccc3ad3742d6f30ba5a5c32a4f6ec", 29, 375),
    "DEL-11-04": ("b57daaf2ef6b61394c7f92aeb5cfa3ddfc67e7f93efccbc0e7e0670cb8cba1d7", "9fdf56afa1e57bff58c4eb000d45880a8ee495e7ab6a33a6183e642c28f3158a", "72e785af819de072cbfbfc9e34019db89340d9c64d5c5697333ab8d566764456", 32, 267),
    "DEL-11-05": ("3c570b0bbe60a28957f9a7f2bf375551bede34252f1fa1815216889b0404d9b4", "94153b259b6a942fa3492e0da9d614028fdcd8297b099c7c54eb9feb9c6e46e2", "dc4b59055a7831b3bccd2b77d6b34965be714ab7cbe4fd18663a126a66f5e991", 36, 300),
}
SEEDS = {
    "DEL-11-01": ("A user-guide skeleton contract for safe installation, model creation, solve, result review, troubleshooting, and professional-responsibility navigation is produced.", "The contract preserves the source-defined guide structure, current implementation declarations, unit and missing-data visibility, diagnostics and result interpretation boundaries, invented-example posture, protected/private-data controls, accessibility intent, visible unresolved documentation decisions, and the prohibition on treating software output as professional approval or code compliance.", "Validate the contract and review source parity, user-journey and guide-structure coverage, current-versus-planned declarations, units and diagnostics, protected/private-data and accessibility controls, retained conflicts and TBDs, and professional-responsibility limits."),
    "DEL-11-02": ("A developer-guide contract for governed solver and rule-pack extension, testing, diagnostics, provenance, and integration boundaries is produced.", "The contract preserves architecture and extension-point descriptions, schema and unit invariants, deterministic test and benchmark expectations, rule-pack provenance and protected-content boundaries, diagnostics and failure behavior, current implementation evidence, visible unresolved interfaces, and the separation of software contribution evidence from engineering approval.", "Validate the contract and review source parity, solver and rule-pack extension coverage, architecture and schema boundaries, units/provenance/protected-content controls, deterministic tests and diagnostics, retained interface TBDs, and professional-authority limits."),
    "DEL-11-03": ("A theory-notes contract tracing classical through modern centerline-analysis concepts, assumptions, applicability, limitations, and evidence boundaries is produced.", "The contract preserves the source-defined conceptual progression, coordinate and unit conventions, model assumptions and limitations, source-provenance controls, distinctions among explanation, implementation, verification, validation, and professional reliance, visible unresolved technical questions, and the ban on presenting unverified extracted equations or narrative as authoritative design basis.", "Validate the contract and review source parity, classical-to-modern topic coverage, assumptions and limitations, coordinate/unit conventions, source provenance and equation reliability controls, verification-versus-validation boundaries, retained conflicts and TBDs, and non-reliance limits."),
    "DEL-11-04": ("A contract for invented educational example models that demonstrate governed workflows without importing protected project truth or implying design validity is produced.", "The contract preserves the source-defined example families, synthetic-data and provenance requirements, units and assumptions, expected diagnostics and learning outcomes, reproducibility and verification evidence, protected/private-data exclusions, non-reliance notice, visible conflicts and TBDs, and separation from benchmark, code-compliance, certification, or professional-approval claims.", "Validate the contract and review source parity, example-family and learning-outcome coverage, invented-data provenance, unit/assumption/diagnostic visibility, reproducibility evidence, protected/private-data boundaries, retained conflicts and TBDs, and non-reliance limits."),
    "DEL-11-05": ("A contributor tutorial and onboarding contract for safe repository setup, bounded changes, tests, evidence, review, and governance-aware contribution is produced.", "The contract preserves the source-defined contributor path, architecture-basis handling, schema and unit invariants, deterministic checks, protected/private-data and licensing boundaries, documentation and review records, safe-versus-unsafe examples, visible unresolved onboarding decisions, and the distinction between contribution acceptance and professional engineering approval.", "Validate the contract and review source parity, onboarding-step and contributor-path coverage, architecture and invariant handling, test/evidence/review expectations, protected/private-data and licensing controls, retained conflicts and TBDs, and professional-responsibility limits."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P3-PKG11/children/VERIFY-B1"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P3/PIP-PKG11"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P3/preflight/P3_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-11"')
code = code.replace('cmd.extend(["--project-scope-ref", ref])', 'cmd.extend(["--project-scope-ref", ref.strip()])')
code = code.replace('cmd.extend(["--package-objective-ref", ref])', 'cmd.extend(["--package-objective-ref", ref.strip()])')
code = code.replace('mutated.write_bytes(mutated.read_bytes() + b"\\n")', 'mutated.write_bytes(mutated.read_bytes() + b"<!-- verifier-negative-mutation -->\\n")')
code = code.replace('"retries": 3 if did == "DEL-02-01" else 0', '"retries": 0')
code = code.replace('"failures": 3 if did == "DEL-02-01" else 0', '"failures": 0')
code = code.replace("{3 if did == 'DEL-02-01' else 0}\\t{3 if did == 'DEL-02-01' else 0}", "0\\t0")
code = code.replace('failures=3 if did == "DEL-02-01" else 0, retries=3 if did == "DEL-02-01" else 0', 'failures=0, retries=0')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
