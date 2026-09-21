#!/usr/bin/env python3
"""R1_NOTES.md: method table, counts, UNASSIGNED list, parser caveats and SHA-256 of every R1a output.

Reads only the R1a outputs beside --out (and CLAIM_INDEX.csv as an input hash). --frozen-root is
accepted for interface uniformity and is not written into the notes.
"""
import argparse, csv, glob, hashlib, os
import r1_common as C

OUTPUTS = [
    ("DELIVERABLE_INVENTORY.csv", "deliverable_inventory.py",
     "one row per `execution/PKG-*/1_Working/DEL-*` folder; state/date from `_STATUS.md` bold fields; ClaimUnits/RemainingItems from CLAIM_INDEX; gated = >=1 parsed gate fragment; assessment date from `| Date |` header cell; basis from SoW front matter"),
    ("REMAINING_INVENTORY.csv", "remaining_inventory.py",
     "every CLAIM_INDEX REM/REMTXT unit; full item text re-read from frozen `_STATUS.md` at SourceLine; gate fragments verbatim; `Depends:` field line"),
    ("DECISION_INDEX.csv", "decision_index.py",
     "every `| D-... |` row of the frozen App `_REGISTER.md`; paths = backticked path tokens; EffectFlag keyword match on state+ruling cells; DEL/PKG IDs by regex over the whole row"),
    ("VERIFICATION_INDEX.csv", "verification_index.py",
     "every `*.test.ts(x)` under `frontend/src/__tests__/**` and runtime `tests/**`; TestCount = `it(`/`test(` call-site regex (incl. `.only/.skip/.todo/.each/.concurrent/.fails/.sequential`)"),
    ("IMPLEMENTATION_SURFACES.csv", "implementation_surfaces.py",
     "brief §5 file set; Area = first matching path rule (r1_common.AREA_RULES)"),
    ("AREA_SUMMARY.csv", "implementation_surfaces.py", "Files/LOC per Area plus TOTAL"),
    ("DIRECTION_RECORD_INDEX.csv", "direction_record_index.py",
     "plans + steers `chirality_app_v3_*`; SCA-APP-008/009 `.md` at depth <= 2; HANDOFF*/OWNER*/*RULING* files (recursive) in APP_V3_*, APPDEV_V3_NODE_*, CHIRALITY_V3_* AgentRuns; Kind by ordered filename rule"),
    ("HINTS/<DEL-ID>.csv", "hints.py",
     "mechanical tokens from each unit's block text, fixed-string grep over implementation + test roots; <=5 hits/token, <=40/unit"),
]

CAVEATS = [
    "CLAIM_INDEX.csv (HELP_HUMAN-owned) has no trailing `#END` line; the R1a loader reads it as plain CSV and also tolerates a `#END` line if one is added later.",
    "REM item text = bullet line plus indented continuation lines; a non-indented line ends the item (consistent with claim_index.py, which would count such a line as REMTXT).",
    "Gate parsing: `(gated: ...)`/`(stage-gated: ...)` use balanced-parenthesis matching; `NOT_SELECTABLE_UNTIL:` runs to the next backtick, else end of line. A `NOT_SELECTABLE_UNTIL` nested inside a `(gated: ...)` fragment is emitted as a second fragment (DEL-03-01#REM-1).",
    "ParsedDepends is the single `Depends:` field line only; items without that field (older prose items) have an empty value even when the prose names a dependency.",
    "DECISION_INDEX: the register rows split cleanly into six cells (no escaped pipes observed; the script aborts otherwise). PacketPath/RulingPath are empty when the cell names no backticked path (e.g. `-` or prose). EffectFlag is a keyword flag only and does not interpret supersession.",
    "DELIVERABLE_INVENTORY: DEL-09-07 has no Assessment file (AssessmentFile/AssessmentDate empty); DEL-00-01/DEL-00-02 have no Dependencies.csv.",
    "IMPLEMENTATION_SURFACES: `frontend/build/**` holds only .plist/.svg/.icns (outside the extension list), so BUILD there contributes no rows; `instructions/**` is taken whole (its only file is AGENTS.md); `frontend/next-env.d.ts` is not in the listed top-level config set and is omitted; runtime package test files (`packages/*/test/*.test.ts`, 2 files) are excluded as tests and are not in VERIFICATION_INDEX because the brief names only `<RT>/tests/**`.",
    "VERIFICATION_INDEX: TestCount is a regex count of call sites; `it.each(...)` counts once regardless of table rows, and call-like text inside strings/comments would be counted.",
    "DIRECTION_RECORD_INDEX: AgentRuns handoff/owner matches are recursive (subfolders included) and include one .json (`HANDOFF_STATE.json`, empty Title). Date falls back to the nearest dated ancestor folder.",
    "HINTS: pointers, not evidence. Generic tokens (e.g. `docs/PRD.md`, `MATCH`, `TBD`, `HarnessEvent`) are kept as extracted and can consume the 40-hit unit cap; tokens are taken in sorted order. Units with no hits carry one row with empty Token/HitPath/HitLine so every unit appears.",
]


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def count_rows(p):
    with open(p, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    assert rows[-1] == ["#END"], p
    return len(rows) - 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    base = os.path.dirname(os.path.abspath(a.out))
    L = ["# R1a Inventory Notes — RUN_D128_CONCORDANCE_2026-09-21_1614Z", "",
         "Generated by `_scripts/build_notes.py`. All inventories are script outputs over the frozen checkout at the pinned basis `00115c719`; no CSV cell carries model judgment. Each script runs as `python3 _scripts/<script> --frozen-root <FROZEN_TREE> --out <file>` (for `hints.py`, `--out` is the `HINTS/` directory; `implementation_surfaces.py` also writes `AREA_SUMMARY.csv` beside its output). Shared rules live in `_scripts/r1_common.py`. Outputs are sorted/deterministic and use repo-relative paths.", "",
         "## Method", "", "| Output | Script | Rule |", "|---|---|---|"]
    for o, s, r in OUTPUTS:
        L.append(f"| `{o}` | `_scripts/{s}` | {r} |")
    L += ["", "## Counts", "", "| Output | Data rows |", "|---|---|"]
    for o, _, _ in OUTPUTS:
        if o.startswith("HINTS"):
            hs = sorted(glob.glob(os.path.join(base, "HINTS", "*.csv")))
            L.append(f"| `HINTS/` | {len(hs)} files, {sum(count_rows(h) for h in hs)} rows |")
        else:
            L.append(f"| `{o}` | {count_rows(os.path.join(base, o))} |")
    with open(os.path.join(base, "AREA_SUMMARY.csv"), encoding="utf-8") as fh:
        area = [r for r in csv.reader(fh)][1:-1]
    L += ["", "## Area summary", "", "| Area | Files | LOC |", "|---|---|---|"] + [f"| {a_} | {f} | {l} |" for a_, f, l in area]
    with open(os.path.join(base, "IMPLEMENTATION_SURFACES.csv"), encoding="utf-8") as fh:
        un = [r[1] for r in csv.reader(fh) if len(r) == 4 and r[3] == "UNASSIGNED"]
    L += ["", "## UNASSIGNED", "", f"{len(un)} file(s)." + ("" if un else " Target zero met.")] + [f"- `{u}`" for u in un]
    L += ["", "## Parser caveats", ""] + [f"- {c}" for c in CAVEATS]
    L += ["", "## SHA-256 of outputs", "", "| File | SHA-256 |", "|---|---|"]
    files = [os.path.join(base, o) for o, _, _ in OUTPUTS if not o.startswith("HINTS")]
    files += sorted(glob.glob(os.path.join(base, "HINTS", "*.csv")))
    files += sorted(glob.glob(os.path.join(base, "_scripts", "*.py")))
    for f in files:
        L.append(f"| `{os.path.relpath(f, base)}` | `{sha(f)}` |")
    L += ["", "Input consumed (not modified): `CLAIM_INDEX.csv` SHA-256 `" + sha(os.path.join(base, "CLAIM_INDEX.csv")) + "`.",
          "", "`R1_NOTES.md` cannot carry its own hash; compute it from the committed bytes.", ""]
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("notes written;", len(files), "hashed files")


if __name__ == "__main__":
    main()
