#!/usr/bin/env python3
"""R3 merge and precedence build (RUN_D128). Deterministic; re-runnable.

Precedence per BRIEFS/R3_SYNTHESIS_MANAGER.md:
  1 sealed ledger of record;
  2 that deliverable's _errata.csv, unless a CORRECTIONS.csv row for the same (ClaimKey, Field)
    rejects the erratum (keeps the sealed value);
  3 CORRECTIONS.csv;
  4 R3 re-mappings: _work/DEC_*.csv files, applied in DECISION_ORDER.
Every change from the sealed value is logged in REMAP_LOG.csv (one line per step; the
SealedValue column holds the value immediately before that step, which is the sealed value
for the first step on a (ClaimKey, Field)).

Outputs: CLAIM_CONCORDANCE.csv, EXTENSION_CONCORDANCE.csv, REVERSE_CONCORDANCE.csv,
REMAP_LOG.csv, INPUT_MANIFEST.md, _work/SEALED_ROWS.csv (sealed values for census).
"""
import os, re, sys, collections
from r3lib import *

DECISION_ORDER = [
    ("DEC_RUNWIDE_REACH.csv", "R3_RUNWIDE"),  # RUNWIDE_CALLS.md (a), (b): REACH tags first
    ("DEC_R4Q1.csv", "R3_RULE"),        # Addendum 6 rule 3 + Addendum 8
    ("DEC_R4QN.csv", "R3_RULE"),        # Addenda 4, 7, 9
    ("DEC_TIEBREAK.csv", "R3_RULE"),    # Addendum 5
    ("DEC_ADD10.csv", "R3_RULE"),       # Addendum 10
    ("DEC_RUNWIDE.csv", "R3_RUNWIDE"),  # RUNWIDE_CALLS.md
    ("DEC_SPOTREVERT.csv", None),       # spot-check reverts (Source given per row)
    ("DEC_OWNERCHECK.csv", "OWNER_CHECK"),  # Addendum 13 owner-check answers (R4 step 1)
]
EXTRA = ["SealedDisposition", "SealedHumanDecisionNeeded", "RemapSources", "AltReading", "SourceLedger"]
VOCAB_FIELDS = {"AuthorityTier", "LatestDecision", "Disposition", "CauseTag", "Confidence",
                "HumanDecisionNeeded", "PostReleaseBasis", "MechanicallyUnblocked"}
TOKEN_RE = {
    "AuthorityTier": re.compile(r"^(LOCAL_DESIGN|PRD|GOVERNANCE_INVARIANT|NOT_APPLICABLE)\b"),
    "LatestDecision": re.compile(r"^(NONE_FOUND|D-(?:APP|GOV)-\d+(?: \(context\))?)"),
    "PostReleaseBasis": re.compile(r"^(YES|NO)\b"),
    "HumanDecisionNeeded": re.compile(r"^((?:NO|R4(?:-Q[1-6])?|D-(?:APP|GOV)-\d+)(?:; (?:R4(?:-Q[1-6])?|D-(?:APP|GOV)-\d+))*)$"),
    "CauseTag": re.compile(r"^([A-Z0-9_]+(?::[A-Z0-9_]+)?)$"),
    "Disposition": re.compile(r"^([A-Z_]+)$"),
    "Confidence": re.compile(r"^(HIGH|MEDIUM|LOW)$"),
    "MechanicallyUnblocked": re.compile(r"^(YES|NO|UNKNOWN)$"),
}
REJECT_RE = re.compile(r"(sealed .{0,40}(is|are) correct|ProposedValue is wrong|erratum'?s? (ProposedValue|proposal) is wrong|sealed (value|[A-Z_]+ tag) (holds|stands))", re.I)
REPLACE_START = re.compile(r"^(projects/|documentary claim|GATE-TRANSCRIPT|RUN-INSPECTION|DOC-BASIS|RULING-RECORD|HASH-RECOMPUTE|REACHABILITY|GOV:|CTX:|NONE_FOUND|NONE_OBSERVED|NOT_APPLICABLE|OVERTAKEN|STILL CURRENT|NOT APPLICABLE|Missing:|Tag |Facade |scaffold\.ts|domain-proposal|REQUIRED_DOC_FILES)")


def norm_value(field, value):
    """Return (value, note) for a CORRECTIONS CorrectedValue.
    Vocabulary fields: take the leading token when the cell adds prose; else verbatim."""
    if field in TOKEN_RE:
        m = TOKEN_RE[field].match(value)
        if m:
            tok = m.group(1)
            if field == "LatestDecision" and value.startswith(tok + " (governing)"):
                return tok, value
            if tok != value:
                return tok, value
            return tok, ""
        # "D-APP-108 (governing). ..." -> "D-APP-108"
        m = re.match(r"^(D-(?:APP|GOV)-\d+) \(governing\)", value)
        if field == "LatestDecision" and m:
            return m.group(1), value
    return value, ""


UPTO = None


def main():
    global UPTO
    if "--upto" in sys.argv:
        UPTO = sys.argv[sys.argv.index("--upto") + 1]
    if "--no-decisions" in sys.argv:
        UPTO = "NONE"
    manifest = []
    log = []
    sealed_rows = []

    corrections = collections.OrderedDict()
    for pkg in sorted(os.listdir(R2)):
        p = os.path.join(R2, pkg, "CORRECTIONS.csv")
        if os.path.exists(p):
            h, rows = read_csv(p)
            manifest.append(("CORRECTIONS", rel(p), sha256(p), len(rows)))
            for r in rows:
                corrections.setdefault((r["ClaimKey"], r["Field"]), []).append((pkg, r))

    def load_decisions():
        dec = []
        for fname, src in DECISION_ORDER:
            if UPTO == "NONE":
                continue
            if UPTO and DECISION_ORDER.index((fname, src)) > [x[0] for x in DECISION_ORDER].index(UPTO):
                continue
            p = os.path.join(WORK, fname)
            if not os.path.exists(p):
                continue
            h, rows = read_csv(p)
            manifest.append(("R3_DECISIONS", rel(p), sha256(p), len(rows)))
            for r in rows:
                dec.append((fname, src or r.get("Source", "R3_RULE"), r))
        return dec

    decisions = load_decisions()
    dec_by_key = collections.defaultdict(list)
    for fname, src, r in decisions:
        dec_by_key[r["ClaimKey"]].append((fname, src, r))

    b_rows = {}
    bl, _ = ledger_path(DB_B_LEDGER)
    manifest.append(("DOUBLE_BLIND_B_EVIDENCE", rel(bl), sha256(bl), None))
    for r in read_csv(bl)[1]:
        if r["ClaimKey"] in DB_B_KEYS:
            b_rows[r["ClaimKey"]] = r

    used_corr = set()
    used_dec = set()
    out = {"DEL": [], "EXT": []}
    seen = set()

    for stem in DELIVERABLE_LEDGERS + EXT_LEDGERS:
        kind = "EXT" if stem.startswith("EXT/") else "DEL"
        lp, ep = ledger_path(stem)
        h, rows = read_csv(lp)
        s = sha256(lp)
        if stem in EXPECTED_SHA and s != EXPECTED_SHA[stem]:
            sys.exit(f"SHA mismatch for {stem}")
        manifest.append(("LEDGER_" + kind, rel(lp), s, len(rows)))
        errata = {}
        if os.path.exists(ep):
            eh, erows = read_csv(ep)
            manifest.append(("ERRATA", rel(ep), sha256(ep), len(erows)))
            for e in erows:
                errata[(e["ClaimKey"], e["Field"])] = e
        by_key = {r["ClaimKey"]: r for r in rows}
        for (k, f), e in errata.items():
            if k not in by_key:
                sys.exit(f"erratum for unknown key {k} in {stem}")
        for r in rows:
            k = r["ClaimKey"]
            if k in seen:
                sys.exit(f"duplicate key {k}")
            seen.add(k)
            sealed_rows.append({"ClaimKey": k, "Kind": kind, "PackageID": r["PackageID"],
                                "DeliverableID": r["DeliverableID"], "ClaimType": r["ClaimType"],
                                "Disposition": r["Disposition"],
                                "HumanDecisionNeeded": r["HumanDecisionNeeded"]})
            cur = dict(r)
            srcs = []

            def change(field, new, source, why):
                old = cur[field]
                if new == old:
                    return
                log.append({"ClaimKey": k, "Field": field, "SealedValue": old, "NewValue": new,
                            "Source": source, "RuleOrEvidence": why})
                cur[field] = new
                if source not in srcs:
                    srcs.append(source)

            # 2. errata
            for (ek, f), e in errata.items():
                if ek != k:
                    continue
                if e["SealedValue"] != r[f]:
                    sys.exit(f"errata SealedValue mismatch {k} {f}")
                rej = None
                for pkg, c in corrections.get((k, f), []):
                    if REJECT_RE.search(c["CorrectedValue"]) or c["CorrectedValue"] == r[f]:
                        rej = (pkg, c)
                if rej:
                    used_corr.add((k, f, rej[1]["VerifierShard"]))
                    log.append({"ClaimKey": k, "Field": f, "SealedValue": r[f], "NewValue": r[f],
                                "Source": "CORRECTION",
                                "RuleOrEvidence": f"erratum rejected by {rej[0]}/CORRECTIONS.csv ({rej[1]['VerifierShard']}); sealed value kept. Erratum proposed: {e['ProposedValue'][:200]}"})
                    if "CORRECTION" not in srcs:
                        srcs.append("CORRECTION")
                    continue
                change(f, e["ProposedValue"], "ERRATA", f"{rel(ep)}: {e['Evidence'][:300]}")
            # 3. corrections
            for f in HEADER:
                for pkg, c in corrections.get((k, f), []):
                    tag = (k, f, c["VerifierShard"])
                    if tag in used_corr:
                        continue
                    abbrev = ""
                    if c["SealedValue"] != r[f] and c["SealedValue"] != cur[f]:
                        parts = [p.strip() for p in re.split(r"\.\.\.|…", c["SealedValue"]) if p.strip()]
                        if len(parts) >= 2 and r[f].startswith(parts[0]) and r[f].rstrip().endswith(parts[-1]):
                            abbrev = " [CORRECTIONS SealedValue is an abbreviation of the sealed cell]"
                        elif r[f] and (r[f] in c["SealedValue"] or c["SealedValue"] in r[f]):
                            abbrev = " [CORRECTIONS SealedValue quotes the sealed cell with extra or partial text]"
                        else:
                            sys.exit(f"CORRECTION SealedValue mismatch {k} {f}")
                    used_corr.add(tag)
                    if f in ("ImplementationEvidence", "VerificationEvidence") and not REPLACE_START.match(c["CorrectedValue"]) is None and c["CorrectedValue"] != "NONE_FOUND" and not c["CorrectedValue"].startswith(("RUN-INSPECTION", "GATE-TRANSCRIPT", "DOC-BASIS", "RULING-RECORD", "HASH-RECOMPUTE", "REACHABILITY", "documentary claim")):
                        # evidence cells: never drop sealed citations; append the verifier's corrected reading
                        new = cur[f] + f" [CORRECTION({c['VerifierShard']}): " + c["CorrectedValue"] + "]"
                        why = f"{pkg}/CORRECTIONS.csv {c['VerifierShard']} (evidence correction appended; sealed citations kept)"
                    elif f != "Notes" and f not in TOKEN_RE and not REPLACE_START.match(c["CorrectedValue"]):
                        new = cur[f] + f" [CORRECTION({c['VerifierShard']}): " + c["CorrectedValue"] + "]"
                        why = f"{pkg}/CORRECTIONS.csv {c['VerifierShard']} (prose correction appended to the sealed cell)"
                    elif f == "Notes":
                        new = (cur[f] + " | " if cur[f] else "") + f"CORRECTION({c['VerifierShard']}): " + c["CorrectedValue"]
                        why = f"{pkg}/CORRECTIONS.csv {c['VerifierShard']} (appended to Notes)"
                    else:
                        new, prose = norm_value(f, c["CorrectedValue"])
                        why = f"{pkg}/CORRECTIONS.csv {c['VerifierShard']}"
                        if prose:
                            why += f"; leading vocabulary token taken from: {prose[:300]}"
                    change(f, new, "CORRECTION", why + abbrev)
            # 4. R3 decisions
            for fname, src, d in dec_by_key.get(k, []):
                used_dec.add((fname, k, d["Field"]))
                f = d["Field"]
                if d.get("Find"):
                    if cur[f].count(d["Find"]) != 1:
                        sys.exit(f"{fname}: Find not exactly once in {k} {f}: {d['Find'][:80]}")
                    change(f, cur[f].replace(d["Find"], d["Replace"], 1), src, f"{fname}: {d['RuleOrEvidence']}")
                elif f == "HDN_TOKENS":
                    toks = hdn_tokens(cur["HumanDecisionNeeded"])
                    for op in d["NewValue"].split():
                        if op.startswith("-"):
                            toks = [t for t in toks if t != op[1:]]
                        elif op.startswith("+"):
                            toks.append(op[1:])
                    change("HumanDecisionNeeded", hdn_join(toks), src, f"{fname}: [{d['NewValue']}] {d['RuleOrEvidence']}")
                elif f == "Notes+":
                    new = (cur["Notes"] + " | " if cur["Notes"] else "") + d["NewValue"]
                    change("Notes", new, src, f"{fname}: {d['RuleOrEvidence']}")
                else:
                    change(f, d["NewValue"], src, f"{fname}: {d['RuleOrEvidence']}")
            alt = ""
            if k in b_rows:
                b = b_rows[k]
                alt = (f"OWNER_DEFERRED (Addendum 5): worker B ({DB_B_LEDGER}) Disposition={b['Disposition']}; "
                       f"CauseTag={b['CauseTag']}; HumanDecisionNeeded={b['HumanDecisionNeeded']}")
            cur.update({"SealedDisposition": r["Disposition"],
                        "SealedHumanDecisionNeeded": r["HumanDecisionNeeded"],
                        "RemapSources": ";".join(srcs) if srcs else "NONE",
                        "AltReading": alt, "SourceLedger": rel(lp)})
            out[kind].append(cur)

    missing = [(k, f, s) for (k, f), lst in corrections.items() for pkg, c in lst
               for s in [c["VerifierShard"]] if (k, f, s) not in used_corr]
    if missing:
        sys.exit(f"unapplied corrections: {missing[:5]}")
    missing = [(fname, r["ClaimKey"]) for fname, src, r in decisions
               if (fname, r["ClaimKey"], r["Field"]) not in used_dec]
    if missing:
        sys.exit(f"decisions for unknown keys: {missing[:5]}")

    write_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"), HEADER + EXTRA, out["DEL"])
    write_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"), HEADER + EXTRA, out["EXT"])
    # Stable partition: OWNER_CHECK lines last, so the R3 REMAP_LOG stays a byte-identical prefix (R4 step 1).
    log = [l for l in log if l["Source"] != "OWNER_CHECK"] + [l for l in log if l["Source"] == "OWNER_CHECK"]
    write_csv(os.path.join(R3, "REMAP_LOG.csv"),
              ["ClaimKey", "Field", "SealedValue", "NewValue", "Source", "RuleOrEvidence"], log)
    write_csv(os.path.join(WORK, "SEALED_ROWS.csv"),
              ["ClaimKey", "Kind", "PackageID", "DeliverableID", "ClaimType", "Disposition",
               "HumanDecisionNeeded"], sealed_rows)

    # Reverse concordance: every reverse response of the deliverable ledgers of record.
    rev = []
    for stem in DELIVERABLE_LEDGERS:
        rp = reverse_path(stem)
        h, rows = read_csv(rp)
        manifest.append(("REVERSE", rel(rp), sha256(rp), len(rows)))
        del_id = os.path.basename(stem).split("_")[0]
        for r in rows:
            area = r["CapabilityID"].split("-")[1] if r["CapabilityID"].startswith("CAP-") else ""
            rev.append({"CapabilityID": r["CapabilityID"], "Area": area, "DeliverableID": del_id,
                        "PackageID": stem.split("/")[0], "Response": r["Response"],
                        "ClaimKey": r["ClaimKey"], "Rationale": r["Rationale"]})
    rev.sort(key=lambda x: (x["CapabilityID"], x["DeliverableID"]))
    write_csv(os.path.join(R3, "REVERSE_CONCORDANCE.csv"),
              ["CapabilityID", "Area", "DeliverableID", "PackageID", "Response", "ClaimKey", "Rationale"], rev)
    for f in sorted(os.listdir(os.path.join(R2, "SURFACES"))):
        if f.endswith("_capabilities.csv"):
            p = os.path.join(R2, "SURFACES", f)
            manifest.append(("CAPABILITIES", rel(p), sha256(p), len(read_csv(p)[1])))

    with open(os.path.join(R3, "INPUT_MANIFEST.md"), "w", encoding="utf-8") as fh:
        fh.write("# R3 input manifest — RUN_D128_CONCORDANCE_2026-09-21_1614Z\n\n")
        fh.write("Built by `R3/_scripts/r3_build.py`. Paths are relative to the run folder. Ledgers of record were\n"
                 "identified from each package's `STATE.jsonl` (`superseded`, `acceptance_decision`,\n"
                 "`ledger-of-record`, `merge*`, `accepted` events) and `PACKAGE_SUMMARY.md` §1; DEL-04-05 by its\n"
                 "Addendum 11 re-sealed SHA. Superseded attempts, double-blind B ledgers (except the two\n"
                 "owner-deferred DEL-06-02 keys, carried in `AltReading`), split halves and R0 calibration ledgers\n"
                 "are evidence only and are not listed as inputs except where noted.\n\n")
        fh.write("| Class | Path | SHA-256 | Rows |\n|---|---|---|---|\n")
        for cls, p, s, n in manifest:
            fh.write(f"| {cls} | `{p}` | `{s}` | {'' if n is None else n} |\n")
        fh.write(f"\nCounts: deliverable ledgers {sum(1 for m in manifest if m[0]=='LEDGER_DEL')}, "
                 f"extension ledgers {sum(1 for m in manifest if m[0]=='LEDGER_EXT')}; "
                 f"deliverable rows {len(out['DEL'])}; extension rows {len(out['EXT'])}; "
                 f"reverse responses {len(rev)}; REMAP_LOG lines {len(log)}.\n")
    print(f"DEL rows {len(out['DEL'])} EXT rows {len(out['EXT'])} reverse {len(rev)} remap {len(log)}")
    print(collections.Counter(l["Source"] for l in log))


if __name__ == "__main__":
    main()
