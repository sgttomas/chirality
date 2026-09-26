#!/usr/bin/env python3
"""D-PEC-95 P + R byte-identity check (run from the repository root).

Each written path must equal its option-P postimage in the preparation report
genP.tsv, except the four retired-deliverable _REFERENCES.md files, which must
equal their A + R postimage in genAR.tsv (ruling "P + R bytes"). The act report
gen_d95_report.tsv must list the same paths, preimages and postimages. The two
SCA-005 snapshot files must keep their pinned preimages. Valid for act date
2026-09-25 only (no slot substitution applies at that date).
Usage: python3 check_byte_identity.py <prep evidence dir> <act report tsv>
"""
import hashlib
import sys
from pathlib import Path

RETIRED = ("DEL-06-04_", "DEL-07-02_", "DEL-07-04_", "DEL-07-05_")
SCA005 = {
    "projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Handoff_State.md":
        "a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a",
    "projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/RUN_SUMMARY.md":
        "e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518",
}


def load(path):
    out = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        f = line.split("\t")
        if f[0] == "WRITE":
            out[f[1]] = (f[2], f[3])
    return out


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ev, report = Path(sys.argv[1]), sys.argv[2]
    gen_p, gen_ar, act = load(ev / "genP.tsv"), load(ev / "genAR.tsv"), load(report)
    ok = True
    n_p = n_r = 0
    if set(act) != set(gen_p):
        ok = False
        print("FAIL\tact path set differs from genP.tsv")
    else:
        print(f"PASS\tact path set equals genP.tsv\t{len(act)} paths")
    for path in sorted(gen_p):
        retired = path.endswith("/_REFERENCES.md") and any(r in path for r in RETIRED)
        exp = gen_ar[path][1] if retired else gen_p[path][1]
        got = sha(path)
        rep_pre, rep_post = act.get(path, ("", ""))
        good = got == exp == rep_post and rep_pre == gen_p[path][0]
        ok &= good
        if retired:
            n_r += 1
        else:
            n_p += 1
        if not good:
            print(f"FAIL\t{path}\tgot={got}\texpected={exp}\treport={rep_post}")
    print(f"{'PASS' if n_p == 115 else 'FAIL'}\tfiles equal to their P postimage (genP.tsv)\t{n_p}/115")
    print(f"{'PASS' if n_r == 4 else 'FAIL'}\tretired _REFERENCES.md equal to their A + R postimage (genAR.tsv)\t{n_r}/4")
    ok &= n_p == 115 and n_r == 4
    for path, pin in SCA005.items():
        got = sha(path)
        ok &= got == pin
        print(f"{'PASS' if got == pin else 'FAIL'}\tbyte-unchanged {path}\t{got}")
    print("RESULT\t" + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
