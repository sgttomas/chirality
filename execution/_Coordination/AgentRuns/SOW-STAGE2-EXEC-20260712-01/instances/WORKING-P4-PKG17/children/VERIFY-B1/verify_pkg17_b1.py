#!/usr/bin/env python3
"""Execute the accepted verifier mechanics independently over frozen PKG-17 B1."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG14/children/VERIFY-B1/verify_pkg14.py"
source = template.read_text(encoding="utf-8")
source = source.replace("WORKING-P4-PKG14", "WORKING-P4-PKG17")
source = source.replace("candidates/W_P4/PIP-PKG14", "candidates/W_P4/PIP-PKG17")
source = source.replace('"PKG-14"', '"PKG-17"')
source = source.replace("'PKG-14'", "'PKG-17'")
members = '''MEMBERS = {
    "DEL-17-01": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-01_CAEPIPE and export-format source basis",
    "DEL-17-02": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-02_Export package, profile, and stable ID map contracts",
    "DEL-17-03": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-03_Native open JSON export package",
    "DEL-17-04": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-04_CAEPIPE MBF export profile and deterministic writer",
    "DEL-17-05": "projects/chirality-piping/execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-05_CAEPIPE external run harness and CSV parser",
}'''
source, count = re.subn(r"MEMBERS = \{.*?\n\}", members, source, count=1, flags=re.S)
assert count == 1
replacements = {
    'len(author_manifest) == 923': 'len(author_manifest) == 991',
    'author_status.get("mappings_passed") == 158': 'author_status.get("mappings_passed") == 166',
    'author_status.get("source_lines_covered") == 1454': 'author_status.get("source_lines_covered") == 1528',
    'len((AUTHOR/"RUNTIME_EVENTS.jsonl").read_text().splitlines()) == 13': 'len((AUTHOR/"RUNTIME_EVENTS.jsonl").read_text().splitlines()) == 10',
    '"ZSH_SPECIAL_PATH_VARIABLE_IN_READ_ONLY_LOOP" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text()': '"DEL-17-05" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text() and "finish" in (AUTHOR/"RUNTIME_EVENTS.jsonl").read_text()',
    '"variable-name-only repair" in (AUTHOR/"RETURN.md").read_text()': '"Mechanical wrapper attempts" in (AUTHOR/"RETURN.md").read_text() and "inherited single-batch PKG-16 assumptions" in (AUTHOR/"FAILURE_ATTEMPTS.md").read_text()',
    'total_mappings==158': 'total_mappings==166',
    'total_lines==1454': 'total_lines==1528',
}
for old, new in replacements.items():
    assert old in source, old
    source = source.replace(old, new)
for forbidden in ("DEL-14-", "PKG-14", "PIP-PKG14", "WORKING-P4-PKG14", "== 923", "== 158", "== 1454"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__", "__file__": str(Path(__file__).resolve())})
