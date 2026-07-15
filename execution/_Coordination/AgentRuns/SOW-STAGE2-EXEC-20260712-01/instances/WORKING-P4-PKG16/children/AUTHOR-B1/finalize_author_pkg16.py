#!/usr/bin/env python3
"""Adapt the accepted PKG-15 terminal binder to frozen PKG-16."""
from pathlib import Path

root = Path(__file__).resolve().parents[8]
template = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P4-PKG15/children/AUTHOR-B1/finalize_author_pkg15.py"
source = template.read_text(encoding="utf-8")
replacements = {
    "WORKING-P4-PKG15": "WORKING-P4-PKG16",
    "candidates/W_P4/PIP-PKG15": "candidates/W_P4/PIP-PKG16",
    "W_P4/PIP-PKG15": "W_P4/PIP-PKG16",
    "DEL-15-": "DEL-16-",
    "PKG-15": "PKG-16",
    "1087": "1097",
    "1,087": "1,097",
    "119": "106",
}
for old, new in replacements.items():
    source = source.replace(old, new)
for forbidden in ("WORKING-P4-PKG15", "PIP-PKG15", "DEL-15-", "PKG-15", "1087", "1,087", "119 mappings"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
