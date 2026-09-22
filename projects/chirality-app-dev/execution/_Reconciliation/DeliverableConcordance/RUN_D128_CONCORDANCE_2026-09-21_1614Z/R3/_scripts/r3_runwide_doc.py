#!/usr/bin/env python3
"""Assemble R3/RUNWIDE_CALLS.md from the TASK call write-ups (T4A: a, b, g; T4B: c, d, f; T6: e;
T2B: the (a)/(b) disposition consequence) plus REMAP_LOG counts per call. Deterministic."""
import os, re, collections
from r3lib import *


def sections(path):
    txt = open(os.path.join(WORK, path), encoding="utf-8").read()
    parts = re.split(r"^## (\([a-g]\)[^\n]*)\n", txt, flags=re.M)
    return {p: (p, b) for p, b in zip(parts[1::2], parts[2::2])}


def main():
    secs = {}
    for f in ("T4A_RUNWIDE.md", "T4B_RUNWIDE.md"):
        for k, v in sections(f).items():
            secs[k] = (v[0], v[1], f)
    t6 = open(os.path.join(WORK, "T6_RUNWIDE_E.md"), encoding="utf-8").read().split("\n", 1)[1]
    t6 = re.sub(r"^## ", "### ", t6, flags=re.M)
    secs["e"] = ("(e) DEL-02-01 half A / half B splits (fresh re-examination)", t6, "T6_RUNWIDE_E.md")
    log = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
    cnt = collections.defaultdict(collections.Counter)
    keys = collections.defaultdict(set)
    for l in log:
        if l["Source"] != "R3_RUNWIDE":
            continue
        m = re.search(r"RUNWIDE_CALLS\.md \(([a-g])\)", l["RuleOrEvidence"])
        c = m.group(1) if m else "?"
        cnt[c][l["Field"]] += 1
        keys[c].add(l["ClaimKey"])
    t2b = open(os.path.join(WORK, "T2B_NOTES.md"), encoding="utf-8").read().split("\n", 1)[1]
    t2b = re.sub(r"^## ", "#### ", t2b, flags=re.M)
    with open(os.path.join(R3, "RUNWIDE_CALLS.md"), "w", encoding="utf-8") as f:
        f.write("# R3 run-wide consistency calls — RUN_D128_CONCORDANCE_2026-09-21_1614Z\n\n")
        f.write("One section per call: the evidence, the call, and the affected rows re-mapped under `R3_RUNWIDE` "
                "(each re-mapping is in `REMAP_LOG.csv` with `RuleOrEvidence` naming `RUNWIDE_CALLS.md (<call>)`). "
                "Calls were decided from code and records in the evidence roots only, by TASK workers T4A (a, b, g), "
                "T4B (c, d, f), T6 (e) and T2B (the disposition consequence of a and b), and integrated by the R3 "
                "manager. They are consistency calls for this run's rows, not rulings. Where two readings stayed "
                "defensible, both are kept in the rows' Notes.\n\n")
        f.write("| Call | Rows re-mapped (keys) | REMAP_LOG lines by field |\n|---|---:|---|\n")
        for c in "abcdefg":
            f.write(f"| ({c}) | {len(keys[c])} | {', '.join(f'{k} {v}' for k, v in sorted(cnt[c].items())) or 'none'} |\n")
        f.write("\nManager integration notes:\n"
                "- HumanDecisionNeeded values from (c), (d), (f) and (e) were applied as token operations (add/remove), "
                "so tokens added by the Addendum 6/8 R4-Q1 re-derivation and the Addenda 4/7/9 mapping are kept.\n"
                "- Two manager consistency re-mappings are logged under (c) and (d)/(f) (`_work/MGR_REMAPS.csv`): "
                "DEL-05-03#CLM-014.1 RemainingWork → NONE_OBSERVED (consequence of C1), and HumanDecisionNeeded `R4` "
                "restored on AUTHORITY_CONFLICT rows DEL-06-04#STATE-2, DEL-09-04#CLM-022 and #CLM-023.3, where "
                "CORRECTIONS had set `NO` (MR-11). All three are marked CONTESTED in Notes: the verifiers read them as "
                "needing no owner decision, a verdict-field view that was not applied.\n"
                "- Run-wide reach re-tags (a)/(b) are applied before the R4-Q1 re-derivation, so rule 3 reads the "
                "re-tagged cells.\n\n")
        for c in "abcdefg":
            if c == "e":
                title, body, src = secs["e"]
            else:
                k = next(k for k in secs if k.startswith(f"({c})"))
                title, body, src = secs[k]
            f.write(f"## {title}\n\n*Source write-up: `R3/_work/{src}`.*\n\n{body.strip()}\n\n")
            if c == "b":
                f.write("### Disposition consequence of (a) and (b) (T2B)\n\n*Source: `R3/_work/T2B_NOTES.md`, "
                        "`T2B_VERDICTS.csv`.* 99 rows whose sealed Disposition says code meets the claim lost every LIVE "
                        "tag under (a)/(b); each was put through the Addendum 6 subject test.\n\n" + t2b.strip() + "\n\n")
    print({c: len(keys[c]) for c in "abcdefg"})


if __name__ == "__main__":
    main()
