#!/usr/bin/env python3
"""PKG-08 Batch-01 binding of the accepted package-verifier harness."""
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
    "DEL-08-01": ("8f0da9dc43c7d33057382663a8d843d56b58180dfe55832eb50f7bfc154a8407", "ae40e3b7aa1b3f45c00be3a69abe6f75a16903e12cccf7890b9fd092eed57625", "b16d573e53e0cf6496f73bbaee4bb4a2675eb41a97dc084398b545c0f94e64c4", 33, 290),
    "DEL-08-02": ("eec16eec083954e5801a03d3ff7a2804d36b86472b9f3e096a1860904af15821", "a9787c24286a41a34652e4be9a0a322ed4ee75006160ec0312de39a23b10348a", "80b8b1ec67139b5c0cf803ee0956dd5fa3a5eea47c9b7f702b1511fbdd6623a9", 28, 253),
    "DEL-08-03": ("b948c1f4efba66345cdfe86040d64301340529f860ee0fccd246895096101f2b", "00ece42387a622e14b7435f1f2edb9126daef8c3edff4fdb919e9f54844d4d30", "f52559d3551ac6dd56a72648c7400903ac6cad437fc75b7e3f47c97d93cde413", 31, 341),
    "DEL-08-04": ("91176c52d2a4c5abc406971fcfbfcf1c1b6924605c0f2159c343c2389a897369", "32477279c39d33fee85454ee646f3d337b8e4ab6d0b74851a38c382f97e5a70f", "07da8ba530826853289ffe1fd100a3e647b69da93b67169cfac73592226489f6", 28, 257),
    "DEL-08-05": ("412bc49a6f65683ce33578b58d1b51598919cb77f6aa0fe62b18708c3c099036", "1461a2ad7e2ff15d0422d5a4a9c1c327b23cfe516aac06a15f8f3e261745a987", "0bdaa96532834d69fec2802774f6f60571448b8620a7a648b19d1a59c179fe81", 33, 347),
}
SEEDS = {
    "DEL-08-01": ("A calculation-report generation contract covering auditable input, source, result, warning, assumption, limitation, unit, provenance, rule-pack, and reproducibility content is produced without claiming certification or professional approval.", "The contract preserves report content and status boundaries, explicit missing-data and diagnostic findings, units and provenance, safe rule-pack metadata, protected-content limits, reproducibility requirements, and competent-human-review notices without inventing unresolved renderer or schema choices.", "Validate the contract and review source parity, report-content completeness, mechanics and rule-check state separation, unit/provenance visibility, protected-content and professional-authority boundaries, deterministic-output requirements, and every retained TBD or governed residual."),
    "DEL-08-02": ("An audit-manifest and model-identity contract covering canonical JSON model hashes, separate non-JSON asset hashes, solver and software versions, units, rule-pack checksums, provenance, warnings, and replay references is produced.", "The contract preserves the explicit hash boundary and deterministic canonicalization basis, complete reproducibility metadata, missing-data findings, protected/private payload exclusion, and separation of computation identity from compliance or professional acceptance without selecting an unapproved library or container.", "Validate the contract and review source parity, canonicalization and hash-boundary rules, deterministic-change behavior, asset-manifest handling, version/unit/provenance fields, protected/private data limits, professional-boundary language, and every retained TBD or governed residual."),
    "DEL-08-03": ("A report-section contract covering warnings, assumptions, missing solve and rule inputs, user-supplied values, provenance, units, reproducibility references, and professional-review notices is produced.", "The contract preserves upstream diagnostic class, severity, source, affected object, message, remediation and provenance when supplied; exposes missingness rather than defaulting it; protects private/protected content; and makes no certification, approval, sealing, authentication, or automatic-compliance claim.", "Validate the contract and review source parity, all warning and missing-data classes, trace-field preservation, unit and provenance visibility, manifest references, protected-content controls and fallback review, prohibited-claim language, and every retained TBD or governed residual."),
    "DEL-08-04": ("A schema-first machine-readable JSON result-envelope contract for review, regression comparison, report generation, GUI consumption, automation, and governed downstream adapters is produced while additional concrete export formats remain TBD.", "The contract preserves explicit units and dimensional metadata, structured diagnostics, provenance and reproducibility references, stable identifiers and ordering, mechanics/rule/human status distinctions, public/private content boundaries, and no-bypass or professional-authority constraints.", "Validate the contract and review source parity, schema-first JSON baseline, retained TBD format choices, unit and diagnostic completeness, deterministic comparison identity, provenance and rule-pack references, adapter no-bypass behavior, protected-content limits, and every governed residual."),
    "DEL-08-05": ("A protected-content report-linting contract covering configured public report surfaces, conservative heuristic findings, safe synthetic fixtures, deterministic diagnostics, quarantine and review routing, optional private scanning, and CI integration boundaries is produced.", "The contract preserves the public/private and redistribution boundary, flags suspected protected or prohibited-authority content without asserting legal sufficiency, uses no protected fixtures, keeps severity and review ownership TBD where unresolved, and retains human/legal review as an independent control.", "Validate the contract and review source parity, authorized scan surfaces, synthetic fixture safety, stable finding traceability, private opt-in behavior, fail/warn/quarantine residuals, professional-claim detection, human/legal review boundaries, and every retained TBD or governed residual."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG08/children/VERIFY-B1"')
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
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
