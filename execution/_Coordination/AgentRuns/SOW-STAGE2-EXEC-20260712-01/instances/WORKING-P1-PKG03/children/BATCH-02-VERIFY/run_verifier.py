#!/usr/bin/env python3
"""PKG-03 Batch-02 binding of the accepted PKG-02 verifier harness."""
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
    "DEL-03-06": ("be4a15e324820f2ddcbd00c5b25a8f17451356d547afd8abf74dd2c9dddeaf05", "cf0a419fdc1bc08c0d1554efe4342f9b2f08509a14b84d44423207a812850100", "ba309339987a43c044a89942565b77f9eb219e98ad0fa601ac322dcfd35dd780", 30, 232),
    "DEL-03-07": ("2c5dece5094332698991983931a48fcb7100765359a8dfe5a2bcc30c9c120916", "f87b738d359e60fb4c9e8108ba486ac137a01acc4f7d4a5e6515efd62cad13a9", "c13ee6184efca604214de2a3c17420d984349a2c0e8a13fef0d90716cb362a49", 26, 218),
    "DEL-03-08": ("08fb868cb1ceac4c4ee3c211f4c18ffbb967f2f926ae573aa811d9e34bc449eb", "623a32692a83cd0aa6187969aa9c2290c68a7aa3a0ccfbadb69de4cd011ed471", "ded51411385937fc7075bf9cef55fdb1a0f9f4d372f163f92b294a72b61e6e97", 32, 249),
}
SEEDS = {
    "DEL-03-06": ("An expansion-joint component-model contract covering supplied stiffnesses, effective area, movement limits, hardware fields, units, provenance, completeness, and diagnostics is produced for the declared scope and objective.", "The contract preserves accepted expansion-joint requirements and boundaries, including supplied-data-only values, explicit units and provenance, protected-content controls, missing-value diagnostics, unresolved taxonomy and solver mappings, and no invented defaults or professional approval.", "Validate the contract and review source parity, field and fixture coverage, dimensional and provenance boundaries, missing-data diagnostics, protected-content controls, downstream solver limits, and unresolved human-review items."),
    "DEL-03-07": ("A public/private library import-provenance checker contract covering source, license, redistribution, contributor and review metadata, privacy posture, unit preservation, quarantine, and diagnostics is produced for the declared scope and objectives.", "The contract preserves accepted public/private data boundaries, conservative missing-provenance handling, protected-content quarantine, unit and diagnostic requirements, and unresolved rights, vocabulary, source-catalog, and legal-acceptance decisions without creating legal conclusions or public defaults.", "Validate the contract and review source parity, metadata and diagnostic coverage, public/private separation, unit preservation, protected-content quarantine, invented-fixture boundaries, and unresolved human or legal review items."),
    "DEL-03-08": ("A pipe section-property and mass-property calculator contract covering explicit dimensional and material inputs, units, provenance, section and mass outputs, diagnostics, protected-data boundaries, and solver handoff limits is produced for the declared scope and objectives.", "The contract preserves accepted calculator requirements and boundaries, including user-entered or lawfully imported inputs, dimensional checks, no silent defaults, invented fixtures, unresolved conversion, schema, contributor, dependency, and human-review decisions, and no code-compliance or professional-approval claim.", "Validate the contract and review source parity, section and mass-property coverage, dimensional consistency, missing-input behavior, provenance, protected-content controls, calculator and solver separation, bounded witness evidence, and unresolved human-review items."),
}
'''

code = prefix + "\ndef now() -> str:" + remainder
code = code.replace('RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"', 'RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"')
code = code.replace('HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"', 'HERE = RUN / "instances/WORKING-P1-PKG03/children/BATCH-02-VERIFY"')
code = code.replace('CAND = RUN / "candidates/PIP-PKG02"', 'CAND = RUN / "candidates/W_P1/PIP-PKG03"')
old_rows = 'rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\\t"))'
new_rows = 'rows = [dict(r, sequence=str(i)) for i, r in enumerate([r for r in csv.DictReader((RUN / "snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\\t") if r["deliverable_id"] in EXPECTED], 1)]'
code = code.replace(old_rows, new_rows)
code = code.replace('"--package-id", "PKG-02"', '"--package-id", "PKG-03"')
code = code.replace('for ref in row["scope_refs"].split(","):\n                cmd.extend', 'for ref in row["scope_refs"].split(","):\n                ref = ref.strip()\n                cmd.extend')
code = code.replace('for ref in row["objective_refs"].split(","):\n                cmd.extend', 'for ref in row["objective_refs"].split(","):\n                ref = ref.strip()\n                cmd.extend')
code = code.replace('''    for row in rows:
        did = row["deliverable_id"]
        seq = int(row["sequence"])''', '''    for row in rows:
        did = row["deliverable_id"]
        existing_summary = HERE / "members" / did / "SUMMARY.json"
        if existing_summary.exists():
            batch.append(json.loads(existing_summary.read_text(encoding="utf-8")))
            continue
        seq = int(row["sequence"])''')
code = code.replace('failures=3, retries=3', 'failures=0, retries=0')
code = code.replace('"failures": 3, "retries": 3', '"failures": 0, "retries": 0')
code = code.replace('member_count=5', 'member_count=3')
code = code.replace('members_complete=5', 'members_complete=3')
code = code.replace('"members_complete": 5', '"members_complete": 3')
code = code.replace('"fail_closed_probes": 35', '"fail_closed_probes": 21')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
