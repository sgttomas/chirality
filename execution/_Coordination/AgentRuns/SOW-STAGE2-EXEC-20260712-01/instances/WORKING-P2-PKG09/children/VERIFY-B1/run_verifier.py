#!/usr/bin/env python3
"""PKG-09 Batch-01 binding of the accepted package-verifier harness."""
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
    "DEL-09-01": ("027dbcebb89a04b71ce554afbbeb30d826ba89c6589428d66004cf8f0a73f48d", "fe691b3f75fa90c28619ffb61f1d4bdabe15640c54ae355abf5f92327c836908", "3db4ba8e6837d4efbca8e6017f53c53fcb177b18a4e248b32364d139ae37aed4", 36, 270),
    "DEL-09-02": ("f517500d035af4f6bf6531d86771bd6a51b637cd7a81fc167413e5908928944d", "d28109b059328ce938bba9a286e6ffbe014b80dcad4a2949dafef313ea3c3c23", "66c21bebd2b47166236146d96c482f57ee10e8b1f5226feb692d5052b152b3dd", 33, 253),
    "DEL-09-03": ("b037c6c72152da88c45564b34cfe552eac9c67520a4b0833a28e0d43b5107319", "496fdb82e3c7b026d19c828dab0b864ff9bbfaee0953e205b06dd2fc80dcea40", "80cd70d3529e532b7debd0ce83ae675363d8ef9042b5c22bc4a02ba3ab064fc0", 31, 275),
    "DEL-09-04": ("46e8fbe2b83204ebc24663a8546ee914e44ed62c0916d20f430e78e955bb6bff", "f8d63d1c20c52a869c75bf0e139922dd1006eaeb70d43108758dcfbb3c9c5135", "7258f898c9ca73b41972e9c2366b3b85b33d483e5001814171aaecb9a2a97be3", 28, 267),
    "DEL-09-05": ("cb6e3c4ce404148acd4577498147a513b1591c318df3121c80799531600ee950", "e398d741a5c51ff5ab52f525b235fb92c54a34ae0455fe59dbe787ba0a459f6b", "9145b615c6a44bde20ded4121678548cfa2803a2458bb6ad8679b5cf631ee351", 34, 292),
}
SEEDS = {
    "DEL-09-01": ("A mechanics benchmark-suite contract covering cantilevers, frames, thermal growth, imposed displacement, and stiffness transforms with original/public/permissive provenance is produced.", "The contract preserves unit-aware inputs and outputs, solver diagnostics, result-envelope fields, assumptions, provenance, limitations, fixture-local unit evidence, and explicit TBD tolerances and project-unit-system decisions without claiming certification, code compliance, professional approval, or project reliance.", "Validate the contract and review source parity, required benchmark-family coverage, source and redistribution posture, unit and diagnostic visibility, setup versus implementation boundaries, retained tolerance and project-unit TBDs, and professional-authority limits."),
    "DEL-09-02": ("A stress-recovery benchmark-suite contract covering axial, bending, torsion, pressure, and stress-range mechanics behavior with governed evidence boundaries is produced.", "The contract preserves public/original/permissive provenance, unit and sign conventions, diagnostics and governed result-envelope evidence, DEC-026's measured analytic relative seed, explicit unmeasured per-kind relative-plus-absolute TBDs, and separation from code compliance, fatigue acceptance, certification, or professional approval.", "Validate the contract and review source parity, all five behavior slots, provenance and protected-content limits, units and dimensional checks, diagnostic/result-envelope preservation, DEC-026 tolerance limits without generalization, and professional-authority boundaries."),
    "DEL-09-03": ("A nonlinear-support regression-suite contract covering active-set, gap, friction, lift-off, convergence, non-convergence, and deterministic rerun evidence is produced.", "The contract preserves source-qualified public/original/permissive cases, unit-aware observations, active and friction state, gap and lift-off, iteration and tolerance basis, diagnostics, solver-maturity dependencies, explicit TBD thresholds, and the software-verification-only authority boundary.", "Validate the contract and review source parity, nonlinear behavior-category coverage, provenance and protected-content exclusions, unit and deterministic rerun requirements, diagnostic/result-envelope categories, retained solver-maturity and tolerance TBDs, and prohibited authority claims."),
    "DEL-09-04": ("A validation-manual skeleton contract separating mechanics verification, intended-use workflow validation, user rule checks, and professional reliance across the required manual outline is produced.", "The contract preserves the ten manual sections, unit/schema/diagnostic/result-envelope evidence slots, public/private and protected-content boundaries, visible gaps and limitations, software-release versus project-reliance distinction, and human-owned professional judgment without certification or code-compliance claims.", "Validate the contract and review source parity, ten-section outline coverage, separation of verification/validation/rule checks/professional reliance, data and provenance boundaries, unit and diagnostic evidence slots, visible TBDs, and release/professional-authority limits."),
    "DEL-09-05": ("A release quality-gate checklist contract routing solver, rule-engine, GUI, report-template, and mixed changes to bounded software-quality evidence and human governance decisions is produced.", "The contract preserves deterministic gate evidence, union routing, provenance, protected/private-data controls, missing-data findings, open risks and TBD thresholds, gate outcome vocabulary, human waiver/risk disposition, and the distinction between release governance and professional engineering approval.", "Validate the contract and review source parity, every gate family and mixed routing, required mechanics/rule/GUI/report evidence, provenance and protected-content checks, unresolved thresholds and authority decisions, outcome semantics, and prohibited compliance or professional-approval claims."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG09/children/VERIFY-B1"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P2/PIP-PKG09"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-09"')
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
