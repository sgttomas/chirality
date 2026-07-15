#!/usr/bin/env python3
"""PKG-06 Batch-01 binding of the accepted package-verifier harness."""
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
    "DEL-06-01": ("e79285e4080512f58a8cc8d808a431e9b27fc18838c149479aae3926897a0667", "2dabc6c8337678fd2cb829fa73e2b5550a692db0045de3d5779fae6208872bb3", "3178e5ea6faab84c9ac1092d939cf7b00491ce48072a9faadbae13247cddef68", 29, 260),
    "DEL-06-02": ("70708249bd899bfdf38ab98a2e16713d4d3c3ec27c006aab96af4b2b46ab46fd", "b439df6dab8cadf7c3784589becb85bf75d32d26e3f7f71446b6cc7417d8adc9", "54448721280354cfb79f91b0e355c1143c1a5381c597ef6a9e9af85eb91b6b4f", 35, 301),
    "DEL-06-03": ("f8c758b78a1d576cf7de2da9ccc09059d4a6975acf03e6213349b503978c9a2a", "9404636c5eb9becf8fa2c5c3df12aa7d32e276783664b9dfa4970f3f5f651e1f", "8badd94e19ddcfd17534850eca25b12914cdfcadfbfb706ef0c09c4a0536c3ae", 30, 231),
    "DEL-06-04": ("1c6755846908ffde2c2e07ee103ad6a141e3e6f6c732652c30481601314b110f", "58ab8ae2e0a65bfc816c9f3d5ba775381eac2ca86fa74635b0609cfbf2d865a5", "9e162ce9e4549846cdc3d9aeee5f741f53ca0f101a0595c57e760fcb05b3ed32", 28, 266),
    "DEL-06-05": ("5721725b89007da54ac58dc0d944dbc5f248d0a32ec581d40d9962bb4734eabc", "3b05da1fc58d3bb2023ca707ff7325ca390f8c6106765bec8e22c9f17a14aad8", "a15d3c97cf01040d25c0201fdf0d79f8baaa9472ffe54f4fa501b92bf1f6daaa", 29, 285),
}
SEEDS = {
    "DEL-06-01": ("A rule-pack-schema contract covering identity and versioning, provenance and redistribution status, canonical payload checksums, required inputs, declarative formula and allowable slots, check criteria, diagnostics, units, and professional-boundary metadata is produced for the declared scope and objective.", "The contract preserves the accepted public/private and protected-content boundaries, declarative sandbox-compatible posture, explicit missing-data behavior, canonical JSON/JCS-compatible hash basis, and retained grammar, storage, encryption, and packaging TBDs without inventing protected formulas, allowables, code content, defaults, or professional approval.", "Validate the contract and review source parity, schema record groups, identity/version/checksum/provenance fields, required-input and unit handling, evaluator and redistribution boundaries, diagnostics, invented-example constraints, and every retained governed residual."),
    "DEL-06-02": ("A sandboxed unit-aware expression-evaluator contract covering a declarative allowlisted grammar, typed variables and functions, dimensional checks, bounded evaluation, deterministic diagnostics, canonical rule-pack version binding, and schema-first result envelopes is produced for the declared scope and objective.", "The contract preserves the accepted no-arbitrary-code, no-side-effect, unit/provenance, protected-content, private-data, and professional-authority boundaries together with retained grammar/library and integration TBDs, without embedding proprietary rules, formulas, allowables, silent conversions, or compliance meaning.", "Validate the contract and review source parity, grammar and sandbox boundaries, dimensional compatibility, persistence/version binding, deterministic evaluation and diagnostics, resource constraints, protected-content controls, and every unresolved governed item."),
    "DEL-06-03": ("A required-input-completeness contract connecting declarative rule-pack requirements to project, model, and user-supplied data, with explicit missing, unit-incompatible, unprovenanced, and rule-check-blocking findings, is produced for the declared scope and objectives.", "The contract preserves the accepted separation between solve-blocking physical inputs and rule-check-required data, explicit no-default behavior, private user-data and protected-content boundaries, and professional responsibility, while retaining the expression grammar/library decision as TBD and inventing no engineering values.", "Validate the contract and review source parity, declarative input binding, completeness and provenance classes, unit compatibility, RULE_INPUTS_INCOMPLETE and RULE_CHECK_BLOCKING behavior, schema/status dependencies, protected-content escalation, and surviving governed conflicts."),
    "DEL-06-04": ("A private rule-pack lifecycle and checksum contract covering stable identity and version, source/provenance notice, redistribution and quarantine status, canonical JSON/JCS-compatible payload hashing, non-JSON manifest hashes, diagnostics, and report/audit references is produced for the declared scope and objectives.", "The contract preserves the accepted local-first privacy, explicit payload-bound checksum, stale-hash, protected-content, unit, and professional-authority boundaries while deferring storage, encryption, access policy, permission persistence, and final redistribution enums to their governed owners.", "Validate the contract and review source parity, lifecycle metadata, checksum payload boundaries, private/public and quarantine handling, diagnostics, audit hooks, no-bypass constraints, deferred security ownership, and all surviving source conflicts."),
    "DEL-06-05": ("An invented non-code example-rule-pack contract covering demonstration-only schema shape, original artificial values, provenance and redistribution fields, required-input and check placeholders, explicit notices, and safe verification expectations is produced for the declared scope and objectives.", "The contract preserves the accepted invented-only public posture, declarative non-executable boundary, no-silent-default behavior, protected-content exclusions, and professional non-reliance notice while retaining schema, grammar, evaluator, and checksum details as TBD until their owning deliverables resolve them.", "Validate the contract and review source parity, invented-value and notice requirements, provenance and redistribution fields, protected-content exclusions, professional boundaries, schema/evaluator ownership, example-path limits, and every surviving governed residual."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG06/children/VERIFY-B1"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P2/PIP-PKG06"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-06"')
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
