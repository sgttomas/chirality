#!/usr/bin/env python3
"""PKG-07 Batch-01 binding of the accepted package-verifier harness."""
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
    "DEL-07-01": ("c796e8f88538fb579c7812a303fc2a2d1bc48a60dc041b31b097ef38f7d3f7f6", "09a473cad3af6b06ae6e1ba1d5157d8ea8ccef82b3a9a301ac8adc2bc5557dd8", "316fb60d9d7bd5840e1167ac86d9d99dfcf11d92c96078f9a3d02193fe5d5f9b", 32, 326),
    "DEL-07-02": ("8de613f147c49f3f1def86655ddc3130787e0687f02fcfc2fb12feb9c0c08e75", "112fee6a944b72a6450994fbea3aa6b2561705cf2430303dd900d10238378c5d", "dfcc9656be9e02980d03d3e8fd5fb817e454bc337a6d3a79637edb7c9e74d291", 37, 279),
    "DEL-07-03": ("6bd11d226a7dc6a5b19dd589624dcca7191099b7589c4b75c6befa3b7f451e10", "3dff5e819cad1b64162ca50d2d676ade5812d50ded13043c5d1bb5b9d6879b7c", "df60267ab09e31656257486aca9ad2fc98a6e32a3106057d6285e67b802875eb", 41, 408),
    "DEL-07-04": ("9cc66b44ab0417997fe54acfcc191a292dde6bc3a1cc14ca72176a357ac331cb", "f9a693fad005c503c30cece6298353e7f273c0e39dd14677b589ca9424631f10", "69e94f98643853957c5e62871144bab16f40cc7f61e1c469ab9b8353b373ff46", 32, 250),
    "DEL-07-05": ("d323d271f18d68b53a206848e0153ebab6b16c8ee7f9049542c166dc6a0263ab", "5144c44383fb01ae19ae0d9180d604ef171e8bb94b57bf53d37ef9fb9f7d5cdd", "5f42f4d39adf70023ec80673735f8805f89a2d5dfde86e8a1d86cf7cb84b92fc", 33, 272),
}
SEEDS = {
    "DEL-07-01": ("A 3D viewport and centerline-editor contract covering unit-aware nodes, pipe runs, bends, simple component symbols, stable selection identity, command-routed edits, explicit diagnostics, and bounded interaction evidence is produced for the declared scope and objective.", "The contract preserves the current implemented viewport slice and named residuals, separates durable model state from transient interaction state, keeps missing or protected engineering data explicit, and invents no component dimensions, code values, defaults, compliance status, or professional approval.", "Validate the contract and review source parity, centerline and symbol boundaries, command/service mutation routing, stable identity, units, diagnostics, current implementation declarations and residuals, protected-data controls, and every retained governed TBD."),
    "DEL-07-02": ("A model-tree and property-inspector contract covering stable entity hierarchy and selection, unit-aware editable properties, provenance and validation feedback, command-routed mutations, and viewport coordination is produced for the declared scope and objective.", "The contract preserves the current implemented inspection/editing boundary, explicit read-only and missing-data states, durable-versus-transient state separation, and protected/private data constraints without inventing engineering defaults, component data, authority, or hidden mutations.", "Validate the contract and review source parity, tree/selection identity, property categories and edit routing, unit and provenance handling, viewport synchronization, diagnostics and blocked states, current residuals, and professional-boundary language."),
    "DEL-07-03": ("A material, component, and rule-pack editor contract covering schema-governed records, units, provenance and redistribution state, checksum/version identity, validated application-service commands, diagnostics, and explicit private/protected-content boundaries is produced for the declared scope and objective.", "The contract preserves the current editor slice and unresolved implementation decisions, keeps public and private data distinct, prevents silent defaults and direct persistence bypass, and invents no proprietary tables, formulas, allowables, component dimensions, code content, or professional acceptance.", "Validate the contract and review source parity, material/component/rule-pack field boundaries, units and provenance, checksum/version handling, command and persistence boundaries, private/protected data, diagnostics, current residuals, and every retained TBD or conflict."),
    "DEL-07-04": ("A missing-data warning and blocking-UX contract covering typed findings, solve-blocking and rule-check-blocking separation, affected-object navigation, provenance and unit diagnostics, remediation guidance, and visible professional-boundary status is produced for the declared scope and objectives.", "The contract preserves explicit fail-closed behavior, the distinction between mechanics input completeness and user-rule input completeness, and current warning UX evidence without inventing values, suppressing findings, treating absence as success, or implying code compliance or approval.", "Validate the contract and review source parity, diagnostic classes and severity, blocking-state separation, navigation and remediation surfaces, missing/incompatible/unprovenanced data handling, current implementation declarations and residuals, and no-silent-default behavior."),
    "DEL-07-05": ("A results-viewer contract covering unit-aware mechanics and user-rule result categories, tabular and graphical review, warnings and assumptions, result-envelope traceability, ratio availability, and report/export handoff signals is produced for the declared scope and objectives.", "The contract preserves the implemented result surface and translational overlay, retains rotational visualization as an explicit residual, separates mechanics, user-rule checks, and human review, and invents no thresholds, formulas, allowables, code categories, compliance status, or professional approval.", "Validate the contract and review source parity, result categories and unit labels, diagnostics and provenance, status separation, ratio blocked/unavailable behavior, translational versus rotational visualization boundary, report/export traceability, and every retained governed residual."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG07/children/VERIFY-B1"')
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
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
