#!/usr/bin/env python3
"""VERIFICATION_INDEX.csv: every *.test.ts(x) under frontend/src/__tests__/** and runtime tests/**.

LOC = number of lines; TestCount = regex count of call sites
`(?<![\\w.$])(it|test)(\\.(only|skip|todo|each|concurrent|fails|sequential))*\\s*\\(`.
"""
import argparse, re
import r1_common as C

CALL = re.compile(r"(?<![\w.$])(?:it|test)(?:\.(?:only|skip|todo|each|concurrent|fails|sequential))*\s*\(")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows = []
    for label, p in C.test_files(a.frozen_root):
        t = C.read_text(p)
        rows.append([label, C.rel(a.frozen_root, p), len(t.splitlines()), len(CALL.findall(t))])
    C.write_csv(a.out, ["Root", "TestFile", "LOC", "TestCount"], rows)
    print(len(rows), "test files;", sum(r[3] for r in rows), "call sites")


if __name__ == "__main__":
    main()
