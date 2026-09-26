#!/usr/bin/env python3
"""D-PEC-93 optional B1 add-on: re-pin 42 _CONTEXT.md and 64 _REFERENCES.md to revision 1.5.

Deterministic exact replacements (each must occur exactly once per file); fails
closed before any write. Semantic fields are not touched. Excludes the two new
DEL-02-08/09 folders (already at revision 1.5) and the 22 A2 contexts (already
carry the revision-1.5 tail).

Usage: python3 gen_d93_b1.py --repo <REPO_ROOT>
"""
import argparse
import glob
import hashlib
import sys
from pathlib import Path

CTX_OLD = "then by revision 1.4 (`current_basis`, SCA-004 successor).\n"
CTX_NEW = ("then by revision 1.4 (`current_basis`, SCA-004 successor),\n"
           "then by revision 1.5 (`current_basis`, SCA-005 successor).\n")
REF_PAIRS = [
    ("- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.4, accepted `current_basis`; SCA-004 successor)\n",
     "- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5, accepted `current_basis`; SCA-005 successor)\n"),
    ("- `docs/PRD.md` v2.2 (accepted source corpus; see SourceRef column of the ledger)\n",
     "- `docs/PRD.md` v2.3 (accepted source corpus; see SourceRef column of the ledger)\n"),
]
NEW_DIRS = ("DEL-02-08_", "DEL-02-09_")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    repo = ap.parse_args().repo.resolve()
    ex = repo / "projects/pec/execution"
    writes = []
    ctx = [Path(p) for p in sorted(glob.glob(str(ex / "PKG-*/1_Working/DEL-*/_CONTEXT.md")))
           if not Path(p).parent.name.startswith(NEW_DIRS)]
    ref = [Path(p) for p in sorted(glob.glob(str(ex / "PKG-*/1_Working/DEL-*/_REFERENCES.md")))
           if not Path(p).parent.name.startswith(NEW_DIRS)]
    for p in ctx:
        t = p.read_text(encoding="utf-8")
        if "then by revision 1.5 (`current_basis`, SCA-005 successor)." in t:
            continue  # the 22 A2 mirrors
        if t.count(CTX_OLD) != 1:
            print(f"FAIL: context anchor in {p}", file=sys.stderr)
            return 1
        writes.append((p, t.replace(CTX_OLD, CTX_NEW)))
    for p in ref:
        t = p.read_text(encoding="utf-8")
        for old, new in REF_PAIRS:
            if t.count(old) != 1:
                print(f"FAIL: reference anchor in {p}", file=sys.stderr)
                return 1
            t = t.replace(old, new)
        writes.append((p, t))
    n_ctx = sum(1 for p, _ in writes if p.name == "_CONTEXT.md")
    n_ref = sum(1 for p, _ in writes if p.name == "_REFERENCES.md")
    if (n_ctx, n_ref) != (42, 64):
        print(f"FAIL: population {n_ctx} contexts / {n_ref} references, expected 42 / 64", file=sys.stderr)
        return 1
    agg_pre, agg_post = hashlib.sha256(), hashlib.sha256()
    for p, data in sorted(writes, key=lambda w: str(w[0])):
        agg_pre.update(p.read_bytes())
        agg_post.update(data.encode("utf-8"))
    for p, data in writes:
        p.write_text(data, encoding="utf-8")
    print(f"OK contexts={n_ctx} references={n_ref} aggregate_pre={agg_pre.hexdigest()} aggregate_post={agg_post.hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
