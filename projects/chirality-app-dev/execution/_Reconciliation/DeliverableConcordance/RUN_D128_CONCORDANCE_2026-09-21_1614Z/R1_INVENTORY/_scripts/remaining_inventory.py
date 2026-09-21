#!/usr/bin/env python3
"""REMAINING_INVENTORY.csv: every REM/REMTXT unit of CLAIM_INDEX with its full item text.

ItemText = the unit's raw lines from the frozen _STATUS.md (REM: bullet + indented
continuation; REMTXT: paragraph), whitespace-collapsed. ParsedGates = verbatim
`(gated: ...)` / `(stage-gated: ...)` (balanced parentheses) and `NOT_SELECTABLE_UNTIL: ...`
(to the closing backtick, else end of line) fragments, ` | `-joined in text order.
ParsedDepends = the text after a `Depends:` field line, if any.
"""
import argparse
import r1_common as C


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--claim-index", default=None)
    a = ap.parse_args()
    units = C.remaining_units(a.frozen_root, C.load_claim_index(a.claim_index))
    rows = sorted([u["ClaimKey"], u["DeliverableID"], u["ItemText"], " | ".join(u["Gates"]), u["Depends"]]
                  for u in units)
    C.write_csv(a.out, ["ClaimKey", "DeliverableID", "ItemText", "ParsedGates", "ParsedDepends"], rows)
    print(len(rows), "remaining units;", sum(1 for u in units if u["Gates"]), "gated")


if __name__ == "__main__":
    main()
