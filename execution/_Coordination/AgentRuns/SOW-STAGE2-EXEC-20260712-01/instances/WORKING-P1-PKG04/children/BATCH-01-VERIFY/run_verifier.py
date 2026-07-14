#!/usr/bin/env python3
"""PKG-04 Batch-01 binding of the accepted PKG-03 verifier harness."""
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
    "DEL-04-01": ("10b828565ec86bd30109f64962ddc2181f7bd7832d747fd52542ceef5bc4eda6", "f5d2906b5f33c235f3df2238fefb8e178f6efe2f4f3c1d4d0ee772588ad90a84", "2e0132408d917eecc136f970235cc0c4f296cda18d65f26e275217b9180333bc", 29, 245),
    "DEL-04-02": ("9ad77b840d70622c5c762f5045b536ef742410c8d4f64a1b687ed2da64616bc4", "ff030c00a1f17cb85e427a4d3e985bf862056a33274a6c2a2671db6ef040b867", "16659d268b94e572d2aba362b6f310db4584f391605b811d164a703cb65d76b6", 28, 199),
    "DEL-04-03": ("99b1f677e68d5f219ff18a42a888e8e64b3f13ee2df84205c6903ed078f99bdc", "c70ca62b6ecd0afae56eb13f17db839cc61b251e604f20a06aed8391dedcbefa", "750e72ffcc5d7be88eb27f74c92fdcaac14f4f24533439dda44ad03ee1efc460", 29, 216),
    "DEL-04-04": ("6fe5c14cf08b00c06ae9c65e4a5aa382db063ba1447f70d0cd512f641d241449", "23488618ae7f3f3b7249501181ff8ff2febac4bdaab9ea5221237cce5c265083", "bfcbcc888efeef6b0262ed9e9a46723a00eafb6d97a541d92c9790e4531c3056", 27, 200),
    "DEL-04-05": ("92290c95666b0505d74e14fe13886d84bc152cd311a077529950be1deac1879a", "afc3a2dad18a504e851e9b425a7e525b6857091e66e5d4b6af4edfd5e9af4970", "0e83177583781150e56798eab71ff95a154a0ab52f888a74a515eb3490611906", 32, 232),
}
SEEDS = {
    "DEL-04-01": ("A 3D frame-stiffness-kernel contract covering six-degree-of-freedom node mapping, global assembly, coordinate transforms, boundary conditions, sparse-solve interfaces, mechanics-only result envelopes, and deterministic verification is produced for the declared scope and objective.", "The contract preserves the accepted frame-kernel requirements and current declarations, including unit and provenance boundaries, explicit missing-input and solver findings, rights-cleared verification data, and unresolved formulation, tolerance, sparse-policy, arc-pressure-thrust, and mechanics-assessment items without inventing engineering values or approval.", "Validate the contract and review source parity, frame/DOF and assembly coverage, coordinate and boundary interfaces, sparse/reproducibility obligations, units and diagnostics, protected-content and professional boundaries, and every unresolved governed item."),
    "DEL-04-02": ("A straight-pipe-element contract covering local stiffness, explicit section-property integration, weight hooks, boundary metadata, spanned loads and axial effects, unit-aware end/station resultant recovery, and deterministic solver verification is produced for the declared scope and objective.", "The contract preserves the accepted straight-pipe mechanics and interface boundaries, including explicit units and lawful input provenance, no hidden load or engineering defaults, rights-cleared fixtures, mechanics-only outputs, and the unresolved governed solver-to-result-envelope integration.", "Validate the contract and review source parity, straight-pipe behavior and frame-kernel boundaries, section and weight interfaces, spanned-load and resultant coverage, dimensional checks, explicit findings, protected-content controls, and result-envelope residuals."),
    "DEL-04-03": ("A linear-support and restraint contract covering anchors, guides, line stops, vertical supports, springs, imposed-displacement boundary data, frame-kernel DOF mapping, boundary preparation/application, explicit findings, and deterministic tests is produced for the declared scope and objective.", "The contract preserves the accepted implemented linear-support boundaries, unit-bearing quantities, no-default behavior, frame-kernel indexing and prescribed-displacement integration, rights-safe fixtures, and unresolved support-coordinate, sparse/result-envelope, release, and constant-effort-hanger work without implying nonlinear behavior or approval.", "Validate the contract and review source parity, all SOW-011 families, FrameDof and boundary surfaces, dimensional metadata, missing/invalid-data findings, deterministic test evidence, protected-content controls, linear/nonlinear separation, and surviving governed residuals."),
    "DEL-04-04": ("A nonlinear-support classifier and state-oracle contract covering one-way restraints, gaps, lift-off, friction, state-switched transitions, convergence and non-convergence reporting, report-facing records, and integration-facing deterministic verification is produced for the declared scope and objective.", "The contract preserves the accepted classifier versus assembled-loop ownership, implemented state-transition and bounded Coulomb-friction basis, unit and diagnostic boundaries, explicit missing inputs, mechanics-only posture, and unresolved path-history, convergence-threshold, sparse-live-path, and validation policies without inventing defaults or engineering acceptance.", "Validate the contract and review source parity, nonlinear behavior categories and state transitions, classifier/integration ownership, convergence diagnostics, units and provenance, protected-content and professional boundaries, deterministic transition witnesses, and every surviving governed residual."),
    "DEL-04-05": ("A sparse-solver performance and regression harness contract covering deterministic practical-model runs, reproducibility, performance and conditioning observations, lawful fixture provenance, solver/version/hash settings, diagnostics, limitations, and reviewable records is produced for the declared scope and objectives.", "The contract preserves the accepted observer-only harness boundary, deterministic regression intent, explicit units and provenance, no invented timing, memory, conditioning, model-size, or release thresholds, mechanics-only reporting, and formal-review, dimensional-validation, hosted-CI, and cross-machine policy residuals.", "Validate the contract and review source parity, harness/solver separation, repeated-run determinism, performance and conditioning records, unit and fixture provenance, protected-content controls, diagnostics and limitations, no compliance claims, and all unresolved governed threshold and release items."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P1-PKG04/children/BATCH-01-VERIFY"')
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
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
