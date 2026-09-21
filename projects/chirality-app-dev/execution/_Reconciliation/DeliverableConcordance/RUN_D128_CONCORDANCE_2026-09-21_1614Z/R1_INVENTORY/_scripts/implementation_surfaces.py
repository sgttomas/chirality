#!/usr/bin/env python3
"""IMPLEMENTATION_SURFACES.csv (+ AREA_SUMMARY.csv beside it, or --summary-out).

Files: `.ts,.tsx,.mjs,.js,.cjs,.json,.css` under frontend/{src,electron,packages,scripts,build}
(test dirs `__tests__`/`test`/`tests` and `*.test.*`/`*.spec.*` excluded), frontend top-level
package.json, next.config.mjs, tsconfig*.json, every file under instructions/**, and the same
extensions under chirality-runtime/packages/** (excluding dist, node_modules, test dirs/files).
Area = first matching rule in r1_common.AREA_RULES; else UNASSIGNED.
"""
import argparse, os
import r1_common as C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--summary-out", default=None)
    a = ap.parse_args()
    files, excluded = C.implementation_files(a.frozen_root)
    rows, summ = [], {}
    for label, p in files:
        r = C.rel(a.frozen_root, p)
        area = C.area_for(r)
        n = C.loc(p)
        rows.append([label, r, n, area])
        f, l = summ.get(area, (0, 0))
        summ[area] = (f + 1, l + n)
    C.write_csv(a.out, ["Root", "Path", "LOC", "Area"], rows)
    order = [x[0] for x in C.AREA_RULES] + ["UNASSIGNED"]
    srows = [[ar, summ.get(ar, (0, 0))[0], summ.get(ar, (0, 0))[1]] for ar in order]
    srows.append(["TOTAL", sum(x[1] for x in srows), sum(x[2] for x in srows)])
    so = a.summary_out or os.path.join(os.path.dirname(os.path.abspath(a.out)), "AREA_SUMMARY.csv")
    C.write_csv(so, ["Area", "Files", "LOC"], srows)
    print(len(rows), "files;", summ.get("UNASSIGNED", (0, 0))[0], "UNASSIGNED;", len(excluded), "test-path files excluded")
    for e in excluded:
        print("  excluded:", e)


if __name__ == "__main__":
    main()
