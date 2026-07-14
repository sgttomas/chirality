#!/usr/bin/env python3
"""Run the frozen PKG-03 full-reproduction harness for exact PKG-04 constants."""

from __future__ import annotations

import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "RECON-P1-PKG03" / "reconcile_full_package.py"
EXPECTED_SOURCE_SHA256 = "787114fc44eecd3953d23cda8605963932657ca7e461c2e5e99c861191df5e05"


def main() -> None:
    source_bytes = SOURCE.read_bytes()
    actual = hashlib.sha256(source_bytes).hexdigest()
    if actual != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(f"frozen harness drift: {actual}")
    source = source_bytes.decode("utf-8")
    replacements = {
        "PKG-03 reconciliation": "PKG-04 reconciliation",
        '"instances/WORKING-P1-PKG03"': '"instances/WORKING-P1-PKG04"',
        '"instances/RECON-P1-PKG03"': '"instances/RECON-P1-PKG04"',
        '"snapshots/W_P1/PKG03-preintegration"': '"snapshots/W_P1/PKG04-preintegration-r1"',
        '"candidates/W_P1/PIP-PKG03"': '"candidates/W_P1/PIP-PKG04"',
        'if r["package"] == "PKG-03"': 'if r["package"] == "PKG-04"',
        'r["terminal_verdict"]': 'r["terminal_status"]',
        '[f"DEL-03-{i:02d}" for i in range(1, 9)]': '[f"DEL-04-{i:02d}" for i in range(1, 7)]',
        'prefix=f"recon-pkg03-{did}-"': 'prefix=f"recon-pkg04-{did}-"',
        "assert total_maps == 234 and total_lines == 1966":
            "assert total_maps == 178 and total_lines == 1368",
        '"status": "PASS_PENDING_AGENT2_FANIN", "members": 8, "terminal_children": 4,':
            '"status": "PASS", "members": 6, "terminal_children": 4,',
        '"mappings": total_maps, "source_lines": total_lines, "replacement_rows": 40,':
            '"mappings": total_maps, "source_lines": total_lines, "replacement_rows": 30,',
        '"rollback_rows": 40, "simulations_pass": 8, "negative_probes_pass": 16,':
            '"rollback_rows": 30, "simulations_pass": 6, "negative_probes_pass": 12,',
        "assert len(replacements) == len(rollbacks) == 40":
            "assert len(replacements) == len(rollbacks) == 30",
    }
    for old, new in replacements.items():
        if source.count(old) != 1:
            raise RuntimeError(f"template replacement cardinality != 1: {old!r}")
        source = source.replace(old, new)
    namespace = {"__name__": "recon_pkg04_runtime", "__file__": str(SOURCE)}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
