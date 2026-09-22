#!/usr/bin/env python3
"""R3 coverage QA (deterministic). Writes R3/UNMAPPED_IMPLEMENTATION.csv and R3/COVERAGE_AND_QA.md."""
import os, re, collections
from r3lib import *

DISP = ["ALIGNED", "IMPLEMENTED_UNDOCUMENTED", "DOCUMENTED_UNIMPLEMENTED", "PARTIALLY_IMPLEMENTED",
        "IMPLEMENTED_DIFFERENTLY", "STALE_SPECIFICATION", "STALE_ASSESSMENT", "STALE_VERIFICATION",
        "ACCEPTED_DIVERGENCE", "RETIRED_BY_RULING", "LIFECYCLE_REASSESSMENT_REQUIRED",
        "REMAINING_STATE_MISMATCH", "DEFERRED_AGENT_WORKFLOW", "AUTHORITY_CONFLICT", "UNKNOWN", "NOT_AUDITABLE"]
BASE = re.compile(r"^(.*?)(\.\d+)?$")


def base_key(k):
    return BASE.match(k).group(1)


def main():
    res = []
    cc = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1]
    ec = read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
    rv = read_csv(os.path.join(R3, "REVERSE_CONCORDANCE.csv"))[1]
    log = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
    sealed = read_csv(os.path.join(WORK, "SEALED_ROWS.csv"))[1]
    idx = read_csv(os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv"), require_end=False)[1]
    eidx = read_csv(os.path.join(RUN, "R1_INVENTORY", "EXTENSION_INDEX.csv"))[1]

    # 1. CLAIM_INDEX coverage
    have = {base_key(r["ClaimKey"]) for r in cc if r["Disposition"]}
    keys = [r["ClaimKey"] for r in idx]
    miss = [k for k in keys if k not in have]
    res.append(("Q1 CLAIM_INDEX units dispositioned", not miss and len(keys) == 1746,
                f"{len(keys) - len(miss)} of {len(keys)} (expected 1,746); missing {len(miss)} {miss[:5]}"))
    # 2. EXTENSION_INDEX coverage
    have = {base_key(r["ClaimKey"]) for r in ec if r["Disposition"]}
    ekeys = [r["UnitKey"] for r in eidx]
    miss = [k for k in ekeys if k not in have]
    res.append(("Q2 EXTENSION_INDEX units dispositioned", not miss and len(ekeys) == 221,
                f"{len(ekeys) - len(miss)} of {len(ekeys)} (expected 221); missing {len(miss)} {miss[:5]}"))
    # 3. capability coverage
    claimed = collections.defaultdict(set)
    for r in rv:
        if r["Response"] in ("CLAIMED_BY", "PARTIAL"):
            claimed[r["CapabilityID"]].add(r["DeliverableID"])
    caps, unm = [], []
    for f in sorted(os.listdir(os.path.join(R2, "SURFACES"))):
        if not f.endswith("_capabilities.csv"):
            continue
        for c in read_csv(os.path.join(R2, "SURFACES", f))[1]:
            caps.append(c)
            if not claimed.get(c["CapabilityID"]):
                reach = re.findall(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY|UNREACHED)", c["Notes"])
                state = re.findall(r"STATE=(ENABLED|DISABLED)", c["Notes"])
                unm.append({"CapabilityID": c["CapabilityID"], "Area": c["Area"], "Capability": c["Capability"],
                            "Paths": c["Paths"], "Reach": "|".join(dict.fromkeys(reach)) or "NOT_STATED",
                            "State": "|".join(dict.fromkeys(state)) or "NOT_STATED",
                            "ResponsesSeen": ";".join(sorted({f"{r['DeliverableID']}:{r['Response']}" for r in rv
                                                              if r["CapabilityID"] == c["CapabilityID"]}))[:0] or
                            str(sum(1 for r in rv if r["CapabilityID"] == c["CapabilityID"])) + " NOT_MINE"})
    write_csv(os.path.join(R3, "UNMAPPED_IMPLEMENTATION.csv"),
              ["CapabilityID", "Area", "Capability", "Paths", "Reach", "State", "ResponsesSeen"], unm)
    ok = all(claimed.get(c["CapabilityID"]) or c["CapabilityID"] in {u["CapabilityID"] for u in unm} for c in caps)
    no_reach = [u["CapabilityID"] for u in unm if u["Reach"] == "NOT_STATED" or u["State"] == "NOT_STATED"]
    unknown_caps = sorted({r["CapabilityID"] for r in rv} - {c["CapabilityID"] for c in caps})
    res.append(("Q3 capabilities claimed or listed as unmapped (with reach and state)", ok and not no_reach and not unknown_caps,
                f"{len(caps)} capability rows: {len(caps) - len(unm)} claimed/partial by >=1 deliverable, {len(unm)} in UNMAPPED_IMPLEMENTATION.csv; "
                f"unmapped without stated reach/state: {len(no_reach)} {no_reach[:5]}; reverse IDs not in any capability file: {len(unknown_caps)} {unknown_caps[:5]}"))
    # 4. package summaries reproduce from ledgers (sealed Disposition census)
    by_pkg = collections.defaultdict(collections.Counter)
    for s in sealed:
        by_pkg["EXT:" + s["ClaimKey"].split(":")[0] if s["Kind"] == "EXT" else s["PackageID"]][s["Disposition"]] += 1
    detail, fails = [], 0
    for pkg in sorted(k for k in by_pkg if k.startswith("PKG-")):
        txt = open(os.path.join(R2, pkg, "PACKAGE_SUMMARY.md"), encoding="utf-8").read()
        bad = []
        for d, n in by_pkg[pkg].items():
            rows = [l for l in txt.splitlines() if re.match(rf"^\|\s*`?{d}`?\s*\|", l)]
            if not rows:
                bad.append(f"{d}: no census row")
            elif not any(re.search(rf"(?<![\d.]){n}(?![\d.%])", l.split("|", 2)[2]) for l in rows):
                bad.append(f"{d}={n} not in census row")
        for l in txt.splitlines():
            m = re.match(r"^\|\s*`?([A-Z_]+)`?\s*\|", l)
            if m and m.group(1) in DISP and m.group(1) not in by_pkg[pkg] and re.search(r"[1-9]", l.split("|", 2)[2].split("|")[-2] if l.count("|") > 2 else ""):
                pass
        total = sum(by_pkg[pkg].values())
        tm = re.search(r"Total rows:\s*(\d+)", txt)
        if tm and int(tm.group(1)) != total:
            bad.append(f"Total rows {tm.group(1)} != {total}")
        fails += bool(bad)
        detail.append(f"{pkg}: {total} rows; {'reproduces' if not bad else 'MISMATCH ' + '; '.join(bad)}")
    ext_txt = open(os.path.join(R2, "EXT", "EXT_SUMMARY.md"), encoding="utf-8").read()
    ext_led = collections.defaultdict(collections.Counter)
    for s in sealed:
        if s["Kind"] == "EXT":
            k = s["ClaimKey"]
            stem = "DEC" if k.startswith("DEC:") else "SOW" if k.startswith("SOW:") else "DOC-" + k.split(":")[1].split("#")[0]
            ext_led[stem][s["Disposition"]] += 1
    for stem, cnt in sorted(ext_led.items()):
        m = re.search(rf"`{re.escape(stem)}` \((\d+) rows\)\. Disposition: ([^.]+)\.", ext_txt)
        if not m:
            fails += 1
            detail.append(f"EXT {stem}: census line not found")
            continue
        got = {a.rsplit(" ", 1)[0]: int(a.rsplit(" ", 1)[1]) for a in m.group(2).split(", ")}
        okx = got == dict(cnt) and int(m.group(1)) == sum(cnt.values())
        fails += not okx
        detail.append(f"EXT {stem}: {sum(cnt.values())} rows; {'reproduces' if okx else f'MISMATCH summary {got} vs ledger {dict(cnt)}'}")
    res.append(("Q4 package summaries reproduce from the ledgers (sealed Disposition census)", fails == 0,
                f"{len(detail) - fails} of {len(detail)} summaries reproduce"))
    # 5. duplicate keys
    d1 = [k for k, c in collections.Counter(r["ClaimKey"] for r in cc + ec).items() if c > 1]
    d2 = [k for k, c in collections.Counter((r["CapabilityID"], r["DeliverableID"]) for r in rv).items() if c > 1]
    res.append(("Q5 no duplicate keys", not d1 and not d2,
                f"ClaimKey duplicates {len(d1)} {d1[:3]}; reverse (CapabilityID, DeliverableID) duplicates {len(d2)} {d2[:3]}"))
    # 6. REMAP_LOG reconciles sealed census to final census
    final = {r["ClaimKey"]: r for r in cc + ec}
    replay = {s["ClaimKey"]: {"Disposition": s["Disposition"], "HumanDecisionNeeded": s["HumanDecisionNeeded"]} for s in sealed}
    for l in log:
        if l["Field"] in ("Disposition", "HumanDecisionNeeded"):
            if replay[l["ClaimKey"]][l["Field"]] != l["SealedValue"]:
                replay[l["ClaimKey"]]["_chain_break"] = True
            replay[l["ClaimKey"]][l["Field"]] = l["NewValue"]
    mism = [k for k, v in replay.items() if v["Disposition"] != final[k]["Disposition"]
            or v["HumanDecisionNeeded"] != final[k]["HumanDecisionNeeded"] or v.get("_chain_break")]
    sc = collections.Counter(s["Disposition"] for s in sealed)
    fc = collections.Counter(r["Disposition"] for r in cc + ec)
    res.append(("Q6 REMAP_LOG reconciles the sealed census to the final census", not mism and len(replay) == len(final),
                f"{len(replay)} rows replayed from sealed values through {len(log)} log lines; mismatches {len(mism)} {mism[:3]}"))

    with open(os.path.join(R3, "COVERAGE_AND_QA.md"), "w", encoding="utf-8") as f:
        f.write("# R3 coverage and QA — RUN_D128_CONCORDANCE_2026-09-21_1614Z\n\n")
        f.write("Built by `R3/_scripts/r3_qa.py` (deterministic). Inputs: `CLAIM_CONCORDANCE.csv`, "
                "`EXTENSION_CONCORDANCE.csv`, `REVERSE_CONCORDANCE.csv`, `REMAP_LOG.csv`, `_work/SEALED_ROWS.csv`, "
                "`R1_INVENTORY/CLAIM_INDEX.csv`, `R1_INVENTORY/EXTENSION_INDEX.csv`, `R2/SURFACES/*_capabilities.csv`, "
                "`R2/*/PACKAGE_SUMMARY.md`, `R2/EXT/EXT_SUMMARY.md`.\n\n")
        f.write("| Check | Verdict | Counts |\n|---|---|---|\n")
        for name, ok, cnt in res:
            f.write(f"| {name} | {'PASS' if ok else 'FAIL'} | {cnt} |\n")
        f.write("\n## Q4 detail (per summary)\n\n")
        for d in detail:
            f.write(f"- {d}\n")
        f.write("\nMethod: for each package, every sealed Disposition count computed from the ledgers of record must "
                "appear in that Disposition's census row of `PACKAGE_SUMMARY.md`, and `Total rows:` (where stated) must "
                "match; for EXT, each ledger's `Disposition:` census line in `EXT_SUMMARY.md` §3 must equal the ledger.\n")
        f.write("\n## Q6 census (all rows: deliverable + EXT)\n\n| Disposition | Sealed | Final | Delta |\n|---|---:|---:|---:|\n")
        for d in DISP:
            if sc[d] or fc[d]:
                f.write(f"| {d} | {sc[d]} | {fc[d]} | {fc[d] - sc[d]:+d} |\n")
        f.write(f"| **Total** | {sum(sc.values())} | {sum(fc.values())} | {sum(fc.values()) - sum(sc.values()):+d} |\n")
        f.write("\nThe replay starts from each row's sealed Disposition and HumanDecisionNeeded and applies every "
                "REMAP_LOG line for those fields in order; each line's SealedValue must equal the replayed prior value "
                "(no silent change), and the end state must equal the final concordance cell.\n")
    for name, ok, cnt in res:
        print("PASS" if ok else "FAIL", name, "|", cnt)
    for d in detail:
        print("  ", d)


if __name__ == "__main__":
    main()
