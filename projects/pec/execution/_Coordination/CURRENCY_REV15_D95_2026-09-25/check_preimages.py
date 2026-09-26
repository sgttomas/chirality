#!/usr/bin/env python3
"""D-PEC-95 preimage check against a pre-act tree (read-only).

Every READ line of the preparation report genP.tsv (119 targets, the 3 basis
files and the 2 SCA-005 snapshot files) must hash to its pinned preimage in the
given tree, and the two Task Management registers must equal the proposal's T1
preimages.
Usage: python3 check_preimages.py <tree root> <prep evidence dir>
"""
import hashlib
import sys
from pathlib import Path

TM = {
    "projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv":
        "d350d007362641323dba7dac44309b27b3f8a091432abdf9bed825c4b5d5799d",
    "projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv":
        "ea730ae06f0805c720bbb29aed6d681c323e6d3b0c4a38d53db27e1075fafd94",
}


def main():
    root, ev = Path(sys.argv[1]), Path(sys.argv[2])
    pins = {}
    for line in (ev / "genP.tsv").read_text(encoding="utf-8").splitlines():
        f = line.split("\t")
        if f[0] == "READ":
            pins[f[1]] = f[2]
    pins.update(TM)
    bad = 0
    for path, want in sorted(pins.items()):
        got = hashlib.sha256((root / path).read_bytes()).hexdigest()
        if got != want:
            bad += 1
            print(f"FAIL\t{path}\tgot={got}\tpinned={want}")
    print(f"{'PASS' if not bad else 'FAIL'}\tpreimages equal to pins\t{len(pins) - bad}/{len(pins)}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
