#!/usr/bin/env python3
"""Execute accepted verifier mechanics independently over frozen PKG-17 B2."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG14/children/VERIFY-B1/verify_pkg14.py"
source = template.read_text(encoding="utf-8")
source = source.replace("WORKING-P4-PKG14", "WORKING-P4-PKG17")
source = source.replace("candidates/W_P4/PIP-PKG14", "candidates/W_P4/PIP-PKG17")
source = source.replace("children/AUTHOR-B1", "children/AUTHOR-B2")
source = source.replace('"PKG-14"', '"PKG-17"')
source = source.replace("'PKG-14'", "'PKG-17'")
members = '''MEMBERS = {
    "DEL-17-06": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package",
    "DEL-17-07": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-07_Conservative PCF subset exporter",
    "DEL-17-08": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-08_GLB glTF review geometry export",
    "DEL-17-09": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-09_Export adapter SDK and additional targets",
}'''
source, count = re.subn(r"MEMBERS = \{.*?\n\}", members, source, count=1, flags=re.S)
assert count == 1
replacements = {
    'len(author_manifest) == 923': 'len(author_manifest) == 842',
    'len(author_candidate) == 15': 'len(author_candidate) == 12',
    'author_status.get("members_complete") == 5': 'author_status.get("members_complete") == 4',
    'author_status.get("mappings_passed") == 158': 'author_status.get("mappings_passed") == 180',
    'author_status.get("source_lines_covered") == 1454': 'author_status.get("source_lines_covered") == 1593',
    'author_status.get("negative_probes_passed") == 35': 'author_status.get("negative_probes_passed") == 28',
    'len((AUTHOR/"RUNTIME_EVENTS.jsonl").read_text().splitlines()) == 13': 'len((AUTHOR/"RUNTIME_EVENTS.jsonl").read_text().splitlines()) == 8',
    '"ZSH_SPECIAL_PATH_VARIABLE_IN_READ_ONLY_LOOP" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text()': '"DEL-17-09" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text() and "finish" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text()',
    '"variable-name-only repair" in (AUTHOR/"RETURN.md").read_text()': '"Mechanical pre-tool attempts" in (AUTHOR/"RETURN.md").read_text() and "disabled-render cleanup" in (AUTHOR/"FAILURE_ATTEMPTS.md").read_text()',
    'summary["members_passed"]==5': 'summary["members_passed"]==4',
    'total_mappings==158': 'total_mappings==180',
    'total_lines==1454': 'total_lines==1593',
    'len(replacement_rows)==25': 'len(replacement_rows)==20',
    'len(inverse_rows)==25': 'len(inverse_rows)==20',
    'len(simulations)==5': 'len(simulations)==4',
    'len(negative_rows)==35': 'len(negative_rows)==28',
    'summary["negative_probes_passed"]==35': 'summary["negative_probes_passed"]==28',
}
for old, new in replacements.items():
    assert old in source, old
    source = source.replace(old, new)
for forbidden in ("DEL-14-", "PKG-14", "PIP-PKG14", "WORKING-P4-PKG14", "children/AUTHOR-B1", "== 923", "== 158", "== 1454"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__", "__file__": str(Path(__file__).resolve())})
