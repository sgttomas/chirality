#!/usr/bin/env python3
"""D-PEC-98 question-4 re-pin: move exactly three places in each candidate copy."""
import sys
from pathlib import Path
base = Path(sys.argv[1])  # run-root candidates/<repo-rel> base
P = "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/"
NEW = "189f205ff02df4111b33c20be441ce06e65ada7a"
FM_OLD = "decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@c9e5cd87d\n"
FM_NEW = f"decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@{NEW}\n"
PUR_OLD = """The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.5** (`current_basis`, SCA-005 successor), accepted by the owner at
SCA-005 checkpoint group 3 on 2026-09-25. The frontmatter pin `c9e5cd87d` is the
checkpoint-3 acceptance commit, an ancestor of `origin/main`. At that commit
`SOFTWARE_DECOMP.md` has SHA-256 `dc2b84791454…9660`, `Deliverables.csv`
`b8628fc4c7b3…3d65a` and `ScopeLedger.csv` `83152a94d91c…9df`, the values
`_Decomposition/_LATEST.md` records, and `docs/PRD.md` v2.3 has SHA-256
`fff27a66cd23…dc32`.
"""
PUR_NEW = f"""The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`{NEW}` is the
checkpoint-3 acceptance commit, an ancestor of `origin/main`. At that commit
`SOFTWARE_DECOMP.md` has SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv`
`94ee5d182ae9…9805` and `ScopeLedger.csv` `1d24a4b86f05…916e`, the values
`_Decomposition/_LATEST.md` records, and `docs/PRD.md` v2.4 has SHA-256
`ae49b8065698…3fbe`.
"""
OBS_OLD = """`origin/main` `53145aaeb`, where the three registers and the PRD named above
are byte-identical to the pin. At `53145aaeb` the deliverable-local
"""
LOCI = {
 "DEL-02-08_Work_graph_parser": """the `SOW-095` row and the `SOW-015` Notes cell of `ScopeLedger.csv`; the
`DEL-02-08` Description and context-envelope notes and the `DEL-01-01` and
`DEL-02-05` Descriptions in `Deliverables.csv`; the `OBJ-001` and `OBJ-002`
statements, the §3 mapping note, decision-log entry `DL-20`, the `PKG-02`
charter, the §5 row and the §8 text of `SOFTWARE_DECOMP.md`; and, in the PRD,
`PEC-RCN-002`, the §7.1 WorkGraph/WorkNode row, the §7.1 DependencyEdge source,
the §7.1 remaining-items field and `PEC-K-10`.""",
 "DEL-02-09_MEMORY_run_index_parser": """the `SOW-096` row of `ScopeLedger.csv`; the `DEL-02-09` and `DEL-01-01`
Descriptions in `Deliverables.csv`; the `OBJ-001` and `OBJ-002` statements,
the §3 mapping note, decision-log entry `DL-20`, the `PKG-02` charter, the §5
row and the §8 text of `SOFTWARE_DECOMP.md`; and, in the PRD, `PEC-RCN-002`,
the §7.1 RunRecord row and the §7.1 remaining-items field.""",
}
def obs_new(d): return f"""`origin/main` `53145aaeb`. There the three registers and the PRD are the
revision-1.5 and PRD v2.3 bytes (`dc2b84791454…9660`, `b8628fc4c7b3…3d65a`,
`83152a94d91c…9df` and `fff27a66cd23…dc32`), which differ from the pin. The
loci this contract quotes from them were re-verified verbatim at the pin:
{LOCI[d]} At `53145aaeb` the deliverable-local
"""
for d in LOCI:
    f = base / (P + d + "/ScopeOfWork.md")
    t = f.read_text(encoding="utf-8")
    for old, new in ((FM_OLD, FM_NEW), (PUR_OLD, PUR_NEW), (OBS_OLD, obs_new(d))):
        assert t.count(old) == 1, (d, old[:50], t.count(old))
        t = t.replace(old, new)
    f.write_bytes(t.encode("utf-8"))
    print("REPINNED", f)
