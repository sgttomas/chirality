#!/usr/bin/env python3
"""Read-only, independent postimage checks for provisional D-PEC-101 part K4.

Usage: python3 verify_d101_k4.py <pre_root> <post_root> [--covers] [--allow-k1]

Compares a pre-state tree (a `git archive` export of aca930622) with a post-state
tree. It does not import or read the generator: every expectation is derived from
the pre-state bytes and the post-state registers. Prints one PASS/FAIL line per
check; exit 0 when every check holds, 1 otherwise.

  --covers    expect add-on C (DEL-04-03 / DEL-08-03 covers lists follow
              Deliverables.csv); without it those two bullets must be unchanged.
  --allow-k1  tolerate files present in post but not in pre when they lie in a
              deliverable folder `projects/pec/execution/PKG-*/1_Working/DEL-*/`
              that does not exist in pre (the separately rulable K1 part creates
              DEL-08-06 and DEL-10-13 born at revision 1.6 / PRD v2.4). Those new
              contexts and references must still pass the post-state currency
              checks. Nothing else is tolerated: no deletions, no other additions,
              no other changed file under projects/.
"""
import argparse
import csv
import difflib
import io
import os
import re
import sys
from pathlib import Path

EX = "projects/pec/execution"
REV_CLAUSE = re.compile(r"revision (\d+\.\d+) \(`current_basis`,\s+(SCA-\d{3}) successor")
STD_TAIL = "then by revision 1.5 (`current_basis`, SCA-005 successor).\n"
D93_LINE = re.compile(r"^SCA-005 successor; deliverable added by (A-\d+)\)\. Fields templated\n$")
REF_DECOMP_15 = "- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5, accepted `current_basis`; SCA-005 successor)\n"
REF_PRD_23 = "- `docs/PRD.md` v2.3 (accepted source corpus; see SourceRef column of the ledger)\n"
COVERS = re.compile(r"^- `execution/_Decomposition/ScopeLedger\.csv` \(SOW→PKG→DEL→OBJ ledger; covers (.*)\)\n?$")
NEW_DEL = re.compile(r"^projects/pec/execution/PKG-[^/]+/1_Working/(DEL-[^/]+)/")


def walk(root: Path) -> dict:
    out = {}
    base = root / "projects"
    for d, dirs, files in os.walk(base):
        dirs.sort()
        for name in files + [x for x in dirs if os.path.islink(os.path.join(d, x))]:
            p = os.path.join(d, name)
            out[os.path.relpath(p, root)] = p
    return out


def same(a: str, b: str) -> bool:
    if os.path.islink(a) or os.path.islink(b):
        return os.path.islink(a) and os.path.islink(b) and os.readlink(a) == os.readlink(b)
    if os.path.getsize(a) != os.path.getsize(b):
        return False
    with open(a, "rb") as fa, open(b, "rb") as fb:
        return fa.read() == fb.read()


def provenance(t: str) -> str:
    block = t.split("\n## Provenance\n", 1)[1] if "\n## Provenance\n" in t else ""
    nxt = block.find("\n## ")
    return block if nxt < 0 else block[: nxt + 1]


def did(rel: str) -> str:
    return Path(rel).parent.name.split("_")[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pre", type=Path)
    ap.add_argument("post", type=Path)
    ap.add_argument("--covers", action="store_true")
    ap.add_argument("--allow-k1", action="store_true")
    a = ap.parse_args()
    pre, post = a.pre.resolve(), a.post.resolve()
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print(f"{'PASS' if cond else 'FAIL'}\t{name}\t{detail}")

    # 1. whole-tree comparison under projects/
    A, B = walk(pre), walk(post)
    only_pre = sorted(set(A) - set(B))
    only_post = sorted(set(B) - set(A))
    pre_dels = {m.group(1) for r in A if (m := NEW_DEL.match(r))}
    k1_new = [r for r in only_post if a.allow_k1 and (m := NEW_DEL.match(r)) and m.group(1) not in pre_dels]
    other_new = sorted(set(only_post) - set(k1_new))
    changed = sorted(r for r in set(A) & set(B) if not same(A[r], B[r]))
    check("no file removed under projects/", not only_pre, f"{len(only_pre)} removed {only_pre[:3]}")
    check("no file added under projects/ (beyond --allow-k1 new deliverable folders)", not other_new,
          f"{len(other_new)} added {other_new[:3]}; tolerated K1 files {len(k1_new)}")

    # 2. expected write set, derived from the pre-state
    pre_ctx = sorted(str(p.relative_to(pre)) for p in (pre / EX).glob("PKG-*/1_Working/DEL-*/_CONTEXT.md"))
    pre_ref = sorted(str(p.relative_to(pre)) for p in (pre / EX).glob("PKG-*/1_Working/DEL-*/_REFERENCES.md"))
    ptext = {p: (pre / p).read_text(encoding="utf-8") for p in pre_ctx + pre_ref}
    std = [p for p in pre_ctx if STD_TAIL in ptext[p]]
    d93 = [p for p in pre_ctx if any(D93_LINE.match(ln) for ln in ptext[p].splitlines(keepends=True))]
    refs = [p for p in pre_ref if REF_DECOMP_15 in ptext[p] and REF_PRD_23 in ptext[p]]
    check("pre-state census", (len(pre_ctx), len(pre_ref), len(std), len(d93), len(refs)) == (66, 66, 61, 2, 66),
          f"{len(pre_ctx)} contexts / {len(pre_ref)} references; std {len(std)}, d93 {len(d93)}, refs {len(refs)}")
    expected = set(std) | set(d93) | set(refs)
    check("changed files under projects/ equal the write set", set(changed) == expected,
          f"changed {len(changed)} (expected {len(expected)}); extra {sorted(set(changed) - expected)[:3]}; "
          f"missing {sorted(expected - set(changed))[:3]}")
    n_ctx = len([p for p in changed if p.endswith("_CONTEXT.md")])
    n_ref = len([p for p in changed if p.endswith("_REFERENCES.md")])
    check("counts 63 contexts + 66 references", (n_ctx, n_ref) == (63, 66), f"{n_ctx} + {n_ref}")

    # 3. edits confined to the anchor lines
    with open(post / EX / "_Decomposition/Deliverables.csv", newline="", encoding="utf-8") as f:
        cells = {r["DeliverableID"]: r["CoversScopeItems"] for r in csv.DictReader(f)}
    bad = []
    covers_changed = []
    for p in sorted(expected & set(changed)):
        a_l = ptext[p].splitlines(keepends=True)
        b_l = (post / p).read_text(encoding="utf-8").splitlines(keepends=True)
        d = [ln for ln in difflib.unified_diff(a_l, b_l, n=0) if ln[:1] in "+-" and ln[:3] not in ("+++", "---")]
        minus = [ln[1:] for ln in d if ln[0] == "-"]
        plus = [ln[1:] for ln in d if ln[0] == "+"]
        if p in std:
            good = (len(minus) == 1 and minus[0].endswith(STD_TAIL)
                    and plus == [minus[0][:-2] + ",\n", "then by revision 1.6 (`current_basis`, SCA-006 successor).\n"])
        elif p in d93:
            m = D93_LINE.match(minus[0]) if len(minus) == 1 else None
            good = bool(m) and plus == [f"SCA-005 successor; deliverable added by {m.group(1)}),\n",
                                        "then by revision 1.6 (`current_basis`, SCA-006 successor). Fields templated\n"]
        else:
            exp = []
            for mline in minus:
                cm = COVERS.match(mline)
                if cm:
                    covers_changed.append(did(p))
                    exp.append(mline.replace(f"covers {cm.group(1)})", f"covers {cells.get(did(p))})"))
                else:
                    exp.append(mline.replace("revision 1.5", "revision 1.6").replace("SCA-005", "SCA-006")
                               .replace("v2.3", "v2.4"))
            n_exp = 3 if (a.covers and did(p) in ("DEL-04-03", "DEL-08-03")) else 2
            good = (len(minus) == n_exp and exp == plus and REF_DECOMP_15 in minus and REF_PRD_23 in minus)
        if not good:
            bad.append(p)
    check("edits confined to the anchor lines", not bad, f"off-anchor {len(bad)} {bad[:3]}")
    exp_cov = ["DEL-04-03", "DEL-08-03"] if a.covers else []
    check("covers bullets changed exactly as the flags require", sorted(covers_changed) == exp_cov,
          f"changed covers: {sorted(covers_changed) or 'none'}")

    # 4. post-state currency over the whole corpus (including any tolerated K1 folders)
    post_ctx = sorted(str(p.relative_to(post)) for p in (post / EX).glob("PKG-*/1_Working/DEL-*/_CONTEXT.md"))
    post_ref = sorted(str(p.relative_to(post)) for p in (post / EX).glob("PKG-*/1_Working/DEL-*/_REFERENCES.md"))
    qtext = {p: (post / p).read_text(encoding="utf-8") for p in post_ctx + post_ref}
    c16 = [p for p in post_ctx if (REV_CLAUSE.findall(provenance(qtext[p])) or [None])[-1] == ("1.6", "SCA-006")]
    check("every context ends its provenance at revision 1.6 (SCA-006)", len(c16) == len(post_ctx),
          f"{len(c16)}/{len(post_ctx)}")
    r16 = [p for p in post_ref
           if REF_DECOMP_15.replace("1.5", "1.6").replace("SCA-005", "SCA-006") in qtext[p]
           and REF_PRD_23.replace("v2.3", "v2.4") in qtext[p]
           and not re.search(r"revision 1\.5, accepted|`docs/PRD\.md` v2\.3", qtext[p])]
    check("every reference names revision 1.6 and PRD v2.4 (and not 1.5 / v2.3)", len(r16) == len(post_ref),
          f"{len(r16)}/{len(post_ref)}")
    scaffolded = [p for p in post_ctx if p in pre_ctx and p not in d93]
    blocks = {provenance(qtext[p]) for p in scaffolded}
    check("the 64 D-PEC-62-scaffolded contexts share one provenance block",
          len(scaffolded) == 64 and len(blocks) == 1, f"{len(scaffolded)} contexts, {len(blocks)} distinct")

    # 5. covers list versus register cell (blank cell agrees with the retired form)
    agree, differ = 0, []
    for p in post_ref:
        m = [COVERS.match(ln) for ln in qtext[p].splitlines(keepends=True)]
        m = [x.group(1) for x in m if x]
        cell = cells.get(did(p))
        if len(m) == 1 and cell is not None and (
                m[0] == cell or (cell == "" and re.fullmatch(r"none — retired under SCA-005, formerly SOW-\d{3}", m[0]))):
            agree += 1
        else:
            differ.append(did(p))
    want = [] if a.covers else ["DEL-04-03", "DEL-08-03"]
    check("covers lists equal Deliverables.csv", sorted(differ) == want,
          f"{agree}/{len(post_ref)} agree; differ: {';'.join(sorted(differ)) or 'none'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
