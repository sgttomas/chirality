#!/usr/bin/env python3
"""PKG-03 Batch-01 binding of the accepted PKG-02 verifier harness."""
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
HEAD = "5f124ad80fe84357f6dc33072dc4fbdbeb05d545"
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
ALL_INPUTS = SOURCE_FILES + CONTROL_FILES
EXPECTED = {
    "DEL-03-01": ("10f15873479e154964ba3aa1dc95d6899fa827ce4b1b3a822bc32ce2818d526c", "d49ba65e086c0b7bfb0444a4e262ada196c22d72d7de98303a35e82efbdb4225", "b1218116afd7d3db563ba0db2ee5d5399dac9582c9d3db362f7ad3690522398a", 29, 220),
    "DEL-03-02": ("4500e92649d1887e3d2517b18854005e2f65e7619160929394e903aaa9060b08", "11a125a780b54a3979f10789a13cfcfadfed946b2fb7d16ed0ca25a66355fdfd", "60a6a050dd539531086885f0ead2f19eb975926e20c6379033fb3bab218c632a", 29, 272),
    "DEL-03-03": ("b6099aeb468fc98d96a9eea5c5529058ac2efb8ca8b5a9e1fb18b81074f3d12a", "79ddb650b5616641fb9129cc98cec19f0fc70198cbf930bc989147b69c609f2a", "27ce2297ea53aa9428f3507bd411db74feba398a4a024b9092d638fe2e72fdb7", 25, 191),
    "DEL-03-04": ("eb32ee8f838c4861bbe31d4eeb9f54408e5ea38546f9dd15432ec8c6871457c6", "420a2462880e6033a873475711c37a015e616d66876416a3e64128155de7bde7", "411245ba0d7954dcac22b9a875f0002b325c6675228530ae76390e6d2e58c9a9", 32, 349),
    "DEL-03-05": ("3355aa71ca62900ec1d77e00e45fb9cd630d41ec370ffdd217cdb5542575541b", "97493f89fb25c411c7eb611acbe41e51086631f149ad25e9c8db8a7fc4fc8653", "7fe7a2ef86684b4b6bc55dc0cc0b43b287d5420132f26676a9cb13d43e281a5e", 31, 235),
}
SEEDS = {
    "DEL-03-01": ("A material-library schema contract covering temperature-dependent properties, allowable slots, provenance, redistribution status, privacy, completeness, and explicit diagnostics is produced for the declared scope and objective.", "The contract preserves accepted material-data requirements and boundaries, including unit awareness, protected-content and redistribution controls, explicit missing-value findings, and unresolved policy decisions without supplying engineering values or professional approval.", "Validate the contract and review source parity, schema and fixture coverage, unit and provenance boundaries, missing-value diagnostics, protected-content controls, deterministic persistence compatibility, and unresolved human-review items."),
    "DEL-03-02": ("A pipe-section and component-library schema contract covering section geometry and properties, component identity, units, provenance, library governance, and explicit completeness diagnostics is produced for the declared scope and objective.", "The contract preserves accepted source requirements for unit-aware, provenance-bearing pipe and component records, rights-safe public fixtures, private data boundaries, explicit unknowns, and no silent engineering defaults.", "Validate the contract and review source parity, pipe-section and component record coverage, units and provenance, public/private data controls, missing-value diagnostics, deterministic persistence compatibility, and unresolved policy decisions."),
    "DEL-03-03": ("A bend-and-elbow component-model contract defining geometry, section, flexibility, stiffness, mass, unit, provenance, and completeness fields is produced for the declared scope and objective.", "The contract preserves accepted bend and elbow modeling requirements, explicit units and provenance, protected-data boundaries, diagnostic treatment of missing inputs, and unresolved engineering-policy choices without inventing defaults.", "Validate the contract and review source parity, bend and elbow field coverage, dimensional consistency, provenance and protected-content boundaries, missing-input diagnostics, mechanics handoff limits, and unresolved decisions."),
    "DEL-03-04": ("A branch-connection component-model contract defining geometry, run and branch identities, section and stiffness inputs, units, provenance, completeness, and diagnostics is produced for the declared scope and objective.", "The contract preserves accepted branch-connection requirements and limits, including explicit dimensional and provenance data, rights-safe fixtures, missing-value findings, and unresolved engineering choices without inferred values or compliance claims.", "Validate the contract and review source parity, branch geometry and identity coverage, dimensional consistency, provenance and protected-content controls, missing-input diagnostics, mechanics handoff limits, and unresolved decisions."),
    "DEL-03-05": ("A rigid and semi-rigid component-model contract covering valves, flanges, reducers, rigid placeholders, and specialty items, including geometry, mass, center-of-gravity, stiffness, units, provenance, and completeness fields, is produced for the declared scope and objective.", "The contract preserves accepted rigid-component requirements, public/private and protected-data boundaries, explicit missing-value diagnostics, provenance and unit discipline, resolved historical findings, and unresolved coordinate and solver-treatment decisions without inventing component values.", "Validate the contract and review source parity, component-family and field coverage, split stiffness dimensions, provenance and protected-content controls, explicit missing values, coordinate-convention gaps, mechanics handoff limits, and unresolved decisions."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P1-PKG03/children/BATCH-01-VERIFY"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P1/PIP-PKG03"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-03"')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
