#!/usr/bin/env python3
"""Evidence tables for provisional D-PEC-101 part K4 (preparation aid; read-only on its inputs).

Usage: python3 tables_k4.py <base_root> <optionA_root> <optionAC_root> <genA.tsv> <out_dir>

Writes <out_dir>/grant_table.md, <out_dir>/aggregates.txt and <out_dir>/census.md.
The write set is taken from the WRITE rows of genA.tsv and cross-checked against
the files that differ between base and the two prototypes.
"""
import collections
import hashlib
import re
import sys
from pathlib import Path

base, pa, pac, gen, out = (Path(x) for x in sys.argv[1:6])
EX = "projects/pec/execution/"
H = lambda b: hashlib.sha256(b).hexdigest()
paths = sorted((ln.split("\t")[1] for ln in gen.read_text(encoding="utf-8").splitlines() if ln.startswith("WRITE\t")),
               key=lambda s: s.encode("utf-8"))
assert len(paths) == 129 and all(p.startswith(EX) for p in paths)
ctx = [p for p in paths if p.endswith("/_CONTEXT.md")]
ref = [p for p in paths if p.endswith("/_REFERENCES.md")]
assert (len(ctx), len(ref)) == (63, 66)
pre = {p: (base / p).read_bytes() for p in paths}
A = {p: (pa / p).read_bytes() for p in paths}
AC = {p: (pac / p).read_bytes() for p in paths}
assert all(pre[p] != A[p] for p in paths)
ac_diff = [p for p in paths if A[p] != AC[p]]

# grant table
rows = ["# K4 grant table (provisional D-PEC-101, part K4)", "",
        "Preimages from the `git archive` export of `aca930622`; postimages from the prototypes built by",
        "`run_k4_prototypes.sh` (option A = the re-pin; A+C = with `--covers`). Paths are relative to",
        "`projects/pec/execution/`, bytewise-sorted. The A+C column is filled only where it differs from A.", "",
        f"Targets: {len(paths)} ({len(ctx)} `_CONTEXT.md`, {len(ref)} `_REFERENCES.md`); A+C differs from A in "
        f"{len(ac_diff)}.", "",
        "| # | Path | Preimage SHA-256 | Postimage SHA-256 (A) | Postimage SHA-256 (A+C, where different) |",
        "|---:|---|---|---|---|"]
for i, p in enumerate(paths, 1):
    rows.append(f"| {i} | `{p[len(EX):]}` | `{H(pre[p])}` | `{H(A[p])}` | "
                f"{'`' + H(AC[p]) + '`' if p in ac_diff else ''} |")
(out / "grant_table.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

# aggregates
def agg(ps, src):
    return H(b"".join(src[p] for p in ps))


def plist(ps):
    return H("".join(p + "\n" for p in ps).encode("utf-8"))


lines = ["K4 aggregate hashes (provisional D-PEC-101, part K4)",
         "Order: bytewise-sorted full paths (projects/pec/...). Aggregate = SHA-256 of the concatenated file bytes",
         "in that order. Path list = SHA-256 of the paths, each followed by one LF, in that order.",
         "set\tfiles\tpathlist_sha256\tpre_sha256\tpost_sha256"]
for name, ps, src in (("all_A", paths, A), ("contexts_A", ctx, A), ("references_A", ref, A),
                      ("all_A+C", paths, AC), ("references_A+C", ref, AC), ("addonC_two_files_A+C", ac_diff, AC)):
    lines.append(f"{name}\t{len(ps)}\t{plist(ps)}\t{agg(ps, pre)}\t{agg(ps, src)}")
(out / "aggregates.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

# census with lifecycle states
STATE = re.compile(r"^\*\*Current State:\*\*\s*(\S+)", re.M)


def state(folder):
    m = STATE.findall((base / folder / "_STATUS.md").read_text(encoding="utf-8"))
    assert len(m) == 1, folder
    return m[0]


def count(ps):
    c = collections.Counter(state(str(Path(p).parent)) for p in ps)
    return ", ".join(f"{k} {c[k]}" for k in sorted(c)), sum(c.values())


folders = sorted({str(Path(p).parent) for p in paths}, key=lambda s: s.encode("utf-8"))
all_folders = sorted((str(p.relative_to(base)) for p in (base / EX).glob("PKG-*/1_Working/DEL-*") if p.is_dir()),
                     key=lambda s: s.encode("utf-8"))
std = [p for p in ctx if b"deliverable added by" not in pre[p]]
d93 = [p for p in ctx if b"deliverable added by" in pre[p]]
mirrors = [f + "/_CONTEXT.md" for f in all_folders if f + "/_CONTEXT.md" not in ctx]
c_str, c_n = count(ctx)
r_str, r_n = count(ref)
u_str, u_n = count([f + "/x" for f in folders])
m_str, _ = count(mirrors)
md = ["# K4 census (provisional D-PEC-101, part K4)", "",
      "Observed on the `git archive` export of `origin/main` `aca930622ba167689881416044ba0feaee3ef003`.",
      "Lifecycle state is the `**Current State:**` line of each folder's `_STATUS.md` (unchanged by K4).", "",
      "| Population | Count | Lifecycle states |", "|---|---:|---|",
      f"| Deliverable folders `PKG-*/1_Working/DEL-*` | {len(all_folders)} | {count([f + '/x' for f in all_folders])[0]} |",
      f"| Contexts re-pinned (CTX_STD, final clause revision 1.5) | {len(std)} | {count(std)[0]} |",
      f"| Contexts re-pinned (CTX_D93: DEL-02-08, DEL-02-09) | {len(d93)} | {count(d93)[0]} |",
      f"| Contexts re-pinned, total | {c_n} | {c_str} |",
      f"| Contexts read-only: SCA-006 A2 mirrors (DEL-04-03, DEL-08-01, DEL-08-03) | {len(mirrors)} | {m_str} |",
      f"| References re-pinned | {r_n} | {r_str} |",
      f"| Union of folders touched (contexts ∪ references) | {u_n} | {u_str} |",
      f"| Add-on C references (DEL-04-03, DEL-08-03) | {len(ac_diff)} | {count(ac_diff)[0]} |", "",
      "No `_STATUS.md`, `_SEMANTIC.md`, `_DEPENDENCIES.md`, `Dependencies.csv` or register file is a target."]
(out / "census.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print("tables written:", len(paths), "targets;", len(ac_diff), "differ under A+C")
