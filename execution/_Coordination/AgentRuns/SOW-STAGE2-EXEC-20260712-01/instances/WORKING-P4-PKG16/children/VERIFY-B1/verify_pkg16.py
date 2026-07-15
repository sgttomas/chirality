#!/usr/bin/env python3
"""Execute the accepted verifier mechanics independently over frozen PKG-16."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG14/children/VERIFY-B1/verify_pkg14.py"
source = template.read_text(encoding="utf-8")
source = source.replace("WORKING-P4-PKG14", "WORKING-P4-PKG16")
source = source.replace("candidates/W_P4/PIP-PKG14", "candidates/W_P4/PIP-PKG16")
source = source.replace('"PKG-14"', '"PKG-16"')
source = source.replace("'PKG-14'", "'PKG-16'")
members = '''MEMBERS = {
    "DEL-16-01": "projects/chirality-piping/execution/PKG-16_Model Operation and Agent Proposal Framework/1_Working/DEL-16-01_Structured model operation schema",
    "DEL-16-02": "projects/chirality-piping/execution/PKG-16_Model Operation and Agent Proposal Framework/1_Working/DEL-16-02_Operation validation and diff preview",
    "DEL-16-03": "projects/chirality-piping/execution/PKG-16_Model Operation and Agent Proposal Framework/1_Working/DEL-16-03_User acceptance and operation audit trail",
    "DEL-16-04": "projects/chirality-piping/execution/PKG-16_Model Operation and Agent Proposal Framework/1_Working/DEL-16-04_Agent rationale and professional-boundary controls",
}'''
source, count = re.subn(r"MEMBERS = \{.*?\n\}", members, source, count=1, flags=re.S)
assert count == 1
replacements = {
    'len(author_manifest) == 923': 'len(author_manifest) == 973',
    'len(author_candidate) == 15': 'len(author_candidate) == 12',
    'author_status.get("members_complete") == 5': 'author_status.get("members_complete") == 4',
    'author_status.get("mappings_passed") == 158': 'author_status.get("mappings_passed") == 106',
    'author_status.get("source_lines_covered") == 1454': 'author_status.get("source_lines_covered") == 1097',
    'author_status.get("negative_probes_passed") == 35': 'author_status.get("negative_probes_passed") == 28',
    'len((AUTHOR/"RUNTIME_EVENTS.jsonl").read_text().splitlines()) == 13': 'len((AUTHOR/"RUNTIME_EVENTS.jsonl").read_text().splitlines()) == 12',
    '"ZSH_SPECIAL_PATH_VARIABLE_IN_READ_ONLY_LOOP" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text()': '"LOCAL_RENDER_BRANCH_STRING_MATCH_REPAIRED_BEFORE_EXECUTION" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text() and "LOCAL_EXEC_NAMESPACE_FILE_BINDING_REPAIRED_BEFORE_CHECKS" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text() and "STALE_PRECEDENT_PHRASES_CORRECTED" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text()',
    '"variable-name-only repair" in (AUTHOR/"RETURN.md").read_text()': '"terminal adapter\'s missing `__file__` binding" in (AUTHOR/"RETURN.md").read_text() and "stale precedent phrases" in (AUTHOR/"RETURN.md").read_text()',
    'summary["members_passed"]==5': 'summary["members_passed"]==4',
    'total_mappings==158': 'total_mappings==106',
    'total_lines==1454': 'total_lines==1097',
    'len(replacement_rows)==25': 'len(replacement_rows)==20',
    'len(inverse_rows)==25': 'len(inverse_rows)==20',
    'len(simulations)==5': 'len(simulations)==4',
    'len(negative_rows)==35': 'len(negative_rows)==28',
    'summary["negative_probes_passed"]==35': 'summary["negative_probes_passed"]==28',
}
for old, new in replacements.items():
    assert old in source, old
    source = source.replace(old, new)
for forbidden in ("DEL-14-", "PKG-14", "PIP-PKG14", "WORKING-P4-PKG14", "== 923", "== 158", "== 1454"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__", "__file__": str(Path(__file__).resolve())})
