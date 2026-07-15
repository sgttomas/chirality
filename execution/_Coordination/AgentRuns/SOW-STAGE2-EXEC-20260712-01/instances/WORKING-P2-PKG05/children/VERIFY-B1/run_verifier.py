#!/usr/bin/env python3
"""PKG-05 Batch-01 binding of the accepted package-verifier harness."""
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
    "DEL-05-01": ("84d35dda5f8440d49046cc668af1d828a97f46031b08d99d85ca21a6f98be515", "248beedc9e4dfd0febbae4a8e03ac2507946ee480627251d0ab74a02f3280acf", "9fc28b036fb58499ba817d80c1799cb8ba715aba39b17539974c8e14c6286a0e", 34, 291),
    "DEL-05-02": ("21a0d9e04e6859592f182e54e7966f6939b9e0341ddb373d3375620526552712", "ec94d8e446bf25760405893229bd91a773992c8ece3cb271d539292141fda783", "f542697d2be32eede102f9806b001bc320b88430bf02b5928c8ac7c23ac3918e", 26, 176),
    "DEL-05-03": ("890aeab5d94fadaf99c031cde847b2e238dfbd12703eab58c0002ed2d012473b", "db8d281b46acbb8aa0c529bbf07965a54bcee424ae7c0ec217560eafddba8765", "49e84c94398c21386d009f20826c36a3aec2fe1dd7d375622d24443eb40a18a1", 28, 234),
    "DEL-05-04": ("60c8eddc479b0661ddc68c32b2fe4902e9ea1b60fede40d0788ff353f2d41492", "d844393abd5bdd7b509f0839671339cbe89e600c75db91111567efa4eeb288b7", "eb505ab254e4e1ba827bcf0c0fc104858cab3404dde122021af3bc8e9e4ec40c", 32, 269),
    "DEL-05-05": ("fa73cf8d1001cd4392dcecb2759e1f4e411db31554f0a2c346615b44d3359faf", "3b0003c3fc44f4334d64a766b2afc4f6baf3d594a6fde9196009ff843d4c0c65", "c0409e920ac5b9c4ba03fdb726d1556c52b5f52d2b48077c74ae00c2f7bf89df", 28, 322),
}
SEEDS = {
    "DEL-05-01": ("A primitive-load-case contract covering explicit weight, pressure, thermal, imposed-displacement, hydrotest, wind, seismic, and occasional mechanics categories, unit-aware preparation, load-case records, diagnostics, and deterministic solver-boundary contributions is produced for the declared scope and objective.", "The contract preserves the accepted primitive-load mechanics, unit, provenance, diagnostic, and rule-separation boundaries, including explicit missing-input findings, caller-supplied equivalent-static bases, and unresolved production policies without inventing code factors, combinations, allowables, defaults, or professional approval.", "Validate the contract and review source parity, category and record coverage, unit/provenance metadata, preparation and solver-vector interfaces, deterministic findings, protected-content and professional boundaries, and every surviving governed residual."),
    "DEL-05-02": ("A load-case-algebra contract covering unit-aware user-defined combinations, deterministic expression evaluation, result-state addition, subtraction, scaling, envelopes and ranges, diagnostics, provenance, and mechanics-only outputs is produced for the declared scope and objectives.", "The contract preserves the accepted bounded algebra surface, explicit units and operand compatibility, user-supplied expressions and factors, deterministic ordering and findings, and unresolved grammar and integration policies without embedding proprietary code combinations, allowables, silent conversions, or compliance meaning.", "Validate the contract and review source parity, algebra and result-state operations, dimensional compatibility, expression/provenance boundaries, deterministic diagnostics and tests, rule-pack separation, protected-content controls, and all unresolved governed items."),
    "DEL-05-03": ("A fundamental stress-recovery contract covering mechanics-only recovery from element end and station resultants, axial, bending, torsional and shear components, section-property and modulus inputs, deterministic sweeps, units, findings, and result hooks is produced for the declared scope and objective.", "The contract preserves the accepted code-neutral mechanics boundary, explicit property and unit provenance, sign and station handling, deterministic recovery evidence, and unresolved envelope, tolerance, labeling, and validation policies without creating code stress categories, allowables, compliance conclusions, or professional approval.", "Validate the contract and review source parity, resultant-to-component recovery, stations and sweeps, section/modulus interfaces, units and sign conventions, diagnostics, deterministic witnesses, protected-content boundaries, and surviving integration residuals."),
    "DEL-05-04": ("An analysis-status-semantics contract defining explicit model-incomplete, mechanics-solved, rule-inputs-incomplete, user-rule checked or failed, human-review-required, and externally recorded human-approval states with schema-first result interfaces is produced for the declared scope and objectives.", "The contract preserves the accepted separation of numerical computation, user-rule evaluation, missing data, professional review, and human-owned project acceptance, including hash-bound external acceptance residuals, without automatic certification, sealing, compliance, approval, or stale-record reuse.", "Validate the contract and review source parity, status vocabulary and transitions, automatic-versus-human authority boundaries, result and diagnostic interfaces, missing-input behavior, stale-hash obligations, tests, and professional-reliance controls."),
    "DEL-05-05": ("A user-load-application contract covering concentrated forces and moments, full and partial-span distributed loads, oriented straight-pipe equivalent nodal recovery, unit-aware boundary records, deterministic findings, axial-effect bridges, and downstream result hooks is produced for the declared scope and objectives.", "The contract preserves the accepted general mechanics-load boundary, explicit units and provenance, deterministic ordering and invalid-input findings, and unresolved result-envelope, persistence, tolerance, and release policies without inventing magnitudes, factors, code combinations, allowables, protected content, or professional claims.", "Validate the contract and review source parity, concentrated and distributed application, partial spans and orientation, equivalent nodal recovery, axial-effect bridge ownership, unit/provenance metadata, result hooks, deterministic tests, and surviving governed residuals."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P2-PKG05/children/VERIFY-B1"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P2/PIP-PKG05"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-05"')
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
