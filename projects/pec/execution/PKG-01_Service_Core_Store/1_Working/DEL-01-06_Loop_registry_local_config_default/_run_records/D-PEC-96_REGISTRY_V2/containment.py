#!/usr/bin/env python3
"""D-PEC-96 containment check (read-only).

Usage: containment.py <name-status file>
The input is the output of `git diff --name-status origin/main...HEAD`
(repository-relative paths). Every changed path must be one of the 11 granted
product paths (with the granted act), a run-root file, DEL-01-06 MEMORY.md
(added), or the brief-authorized return file. All 11 product paths must be
present. Exit 0 when contained, 1 otherwise.
"""

from __future__ import annotations

import sys

PEC = "projects/pec/"
DEL = PEC + "execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/"
RUN_ROOT = DEL + "_run_records/D-PEC-96_REGISTRY_V2/"
MEMORY = DEL + "MEMORY.md"
RETURN = PEC + "execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/G2_D96_REGISTRY_ACT.md"
PRODUCT = {
    "v2/config/loops.json": "M",
    "v2/config/loops.schema.json": "M",
    "v2/src/pec_v2/core/ports/loop_registry.py": "M",
    "v2/src/pec_v2/core/ports/__init__.py": "M",
    "v2/src/pec_v2/core/__init__.py": "M",
    "v2/src/pec_v2/adapters/config/loop_registry.py": "M",
    "v2/tests/config/test_json_loop_registry.py": "M",
    "v2/tests/config/test_loop_registry_contract.py": "M",
    "v2/tests/config/fixtures/duplicate_loop_id.json": "M",
    "v2/tests/config/fixtures/missing_loop_id.json": "M",
    "v2/tests/config/fixtures/schema_version_1.json": "A",
}


def main() -> int:
    lines = [ln.rstrip("\n") for ln in open(sys.argv[1], encoding="utf-8") if ln.strip()]
    counts = {"PRODUCT": 0, "RUN_ROOT": 0, "MEMORY": 0, "RETURN": 0}
    bad: list[str] = []
    seen: set[str] = set()
    for ln in lines:
        status, path = ln.split("\t", 1)
        if "\t" in path:
            bad.append(f"RENAME/COPY {ln}")
            continue
        rel = path[len(PEC):] if path.startswith(PEC) else None
        if rel in PRODUCT:
            if status != PRODUCT[rel]:
                bad.append(f"WRONG_ACT {status} {path} (granted {PRODUCT[rel]})")
            counts["PRODUCT"] += 1
            seen.add(rel)
        elif path.startswith(RUN_ROOT) and status in ("A", "M"):
            counts["RUN_ROOT"] += 1
        elif path == MEMORY and status == "A":
            counts["MEMORY"] += 1
        elif path == RETURN and status in ("A", "M"):
            counts["RETURN"] += 1
        else:
            bad.append(f"OUTSIDE {status} {path}")
    missing = sorted(set(PRODUCT) - seen)
    for m in missing:
        bad.append(f"GRANTED_PATH_UNCHANGED {m}")
    print("changed paths:", len(lines))
    for k, v in counts.items():
        print(f"{k}: {v}")
    for b in bad:
        print(b)
    print("RESULT", "CONTAINED" if not bad else "NOT_CONTAINED")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
