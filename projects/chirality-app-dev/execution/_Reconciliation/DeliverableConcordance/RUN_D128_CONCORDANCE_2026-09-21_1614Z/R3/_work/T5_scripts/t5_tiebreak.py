"""T5: apply the Addendum 5 tie-break to CAND_TIEBREAK.csv rows (decisions recorded below by hand)."""
import collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "_scripts"))
import r3lib  # noqa: E402

SS = "STALE_SPECIFICATION"
RSM = "REMAINING_STATE_MISMATCH"

# ClaimKey -> (Verdict, AlsoNote, Basis)
D = {
    # PKG-01
    "DEL-01-02#CLM-022.2": ("KEEP", "", "Rule 2b: SoW open item OI-RBR-002 is a TBD placeholder ('fill exact implementation paths after modules exist') behind filled paths; it says nothing false about the product."),
    "DEL-01-02#REM-1": ("KEEP", "", "Rule 1: the Remaining item's open status is not contradicted (2a fails); its text says D-GOV-20 owns the one-daemon boundary, which D-GOV-43 contradicts on the App path."),
    "DEL-01-02#CLM-059.3": ("KEEP", "", "Rule 2b: TBD-RBR-002 is a TBD placeholder lagging a decision recorded in amended K-EVENT-4 and D-GOV-43 item 5."),
    "DEL-01-02#CLM-059.5": ("KEEP", "", "Rule 2b: TBD-RBR-004 is a TBD placeholder behind existing validator automation (contract-pins manifest)."),
    "DEL-01-04#REGISTER-3": ("KEEP", "", "Rule 1: DEP-01-04-010 is marked SATISFIED on evidence that is now a LEGACY_ONLY module while the live composer ships full access."),
    # PKG-02
    "DEL-02-01#REM-1": ("KEEP", "ALSO:" + RSM, "Rule 4: the Remaining note's 'no code owed' status is contradicted (2a) and it says src/app/icon.svg satisfies the convention though the file is absent (1); the repair is rewriting the note."),
    "DEL-02-02#REMTXT-1": ("KEEP", "ALSO:" + RSM, "Rule 4: the Remaining prose says Work/Workbench/Pipeline presentations 'are implemented' (false on the live path, 1) and 'no presentation residual' beside open V3 items (2a); the repair is rewriting the prose."),
    "DEL-02-02#REM-2": ("KEEP", "", "Rule 1: the item's open status is correct (2a fails); its gate names Root DEL-02-10 schema-v2 acceptance, which D-GOV-43 item 2 replaced."),
    "DEL-02-02#REGISTER-4": ("KEEP", "", "Rule 2b: the _DEPENDENCIES.md summary counts (8 PENDING) lag Dependencies.csv (7 PENDING); register bookkeeping only."),
    "DEL-02-04#REGISTER-6": ("KEEP", "", "Rule 2b: summary counts lag the CSV and DEP-02-04-017..019 stay PENDING after their fields landed; lagging status fields."),
    # PKG-03
    "DEL-03-01#REGISTER-4": ("KEEP", "", "Rule 2b: DEP-03-01-008 stays PENDING while the section9 ID exists; a lagging status field."),
    "DEL-03-04#STATE-2": ("KEEP", "", "Rule 2a: '## Remaining: None' is contradicted by the unapplied D-APP-127 SoW revision and the open redaction gap."),
    "DEL-03-04#REGISTER-3": ("KEEP", "", "Rule 1: DEP-03-04-006/-007/-009 say DEL-05-02 provides the HarnessEvent JSONL writer; the live writer is in chirality-runtime session-store.ts."),
    # PKG-04 DEL-04-01
    "DEL-04-01#CLM-001": ("MOVE", "", "Rule 3: the 'current-state note (2026-07-12)' says REF-006 'is MATCH' and 'describes current source state' with no named snapshot; recomputed PRD hash differs. SEE:DEL-04-01#REGISTER-1."),
    "DEL-04-01#CLM-008": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note restating REF-006 'is MATCH' as current. SEE:DEL-04-01#REGISTER-1."),
    "DEL-04-01#CLM-015": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note restating REF-006 'is MATCH' as current. SEE:DEL-04-01#REGISTER-1."),
    "DEL-04-01#CLM-022": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note restating REF-006 'is MATCH' as current. SEE:DEL-04-01#REGISTER-1."),
    "DEL-04-01#CLM-004.2": ("UNDECIDED", "", "Rule 3 vs neither: the row says '_REFERENCES.md records MATCH' (still literally true) and asks for snapshot confirmation before closure. Reading A: STALE_SPECIFICATION, since 'reconciled under D-APP-38' presents the MATCH as the current source state (SEE:DEL-04-01#REGISTER-1). Reading B: the warning itself defers to snapshot confirmation and is not false, so neither verdict fits."),
    "DEL-04-01#CLM-013.10": ("MOVE", "", "Rule 3: VER-010 states 'REF-006 hash status: MATCH ... reconciled under D-APP-38' as current, with no named snapshot. SEE:DEL-04-01#REGISTER-1."),
    "DEL-04-01#CLM-025": ("MOVE", "", "Rule 3: bullet 1 says 'REF-006 is MATCH under D-APP-38' as current; the other bullets match the records. SEE:DEL-04-01#REGISTER-1."),
    "DEL-04-01#REGISTER-1": ("MOVE", "", "Rule 1: _REFERENCES.md records ActualSHA256 = Expected with Status MATCH for REF-002/003/006 and names no snapshot date; the recomputed hashes differ."),
    "DEL-04-01#STATE-1": ("KEEP", "", "Rule 2a: the empty ## Remaining is contradicted by SOW-079, which SCA-APP-009 maps to DEL-04-01."),
    "DEL-04-01#STATE-3": ("KEEP", "", "Rule 2b: MEMORY.md Open Items keeps BLOCKED_TBD and probe-needed markers discharged on 2026-07-18/19; lagging status fields about evidence, not product facts."),
    # PKG-04 DEL-04-02
    "DEL-04-02#CLM-001": ("MOVE", "", "Rule 3: the current-state note says REF-006 'is MATCH' as current with no named snapshot. SEE:DEL-04-02#REGISTER-1."),
    "DEL-04-02#CLM-008": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note. SEE:DEL-04-02#REGISTER-1."),
    "DEL-04-02#CLM-022": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note. SEE:DEL-04-02#REGISTER-1."),
    "DEL-04-02#REGISTER-1": ("MOVE", "", "Rule 1: _REFERENCES.md records REF-002/003/006 as MATCH with ActualSHA256 values and no snapshot date; the recomputed hashes differ."),
    "DEL-04-03#REGISTER-4": ("KEEP", "", "Rule 2b: 'Declared Upstream/Downstream: TBD - no accepted dependency edges extracted yet' is a scaffold TBD placeholder behind the extracted register; the REF-006 warning is a dated run note."),
    # PKG-04 DEL-04-04
    "DEL-04-04#CLM-001": ("MOVE", "", "Rule 3: the current-state note says REF-006 'is MATCH' as current with no named snapshot. SEE:DEL-04-04#REGISTER-1."),
    "DEL-04-04#CLM-008": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note. SEE:DEL-04-04#REGISTER-1."),
    "DEL-04-04#CLM-015": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note. SEE:DEL-04-04#REGISTER-1."),
    "DEL-04-04#CLM-022": ("MOVE", "", "Rule 3: verbatim repeat of the current-state note. SEE:DEL-04-04#REGISTER-1."),
    "DEL-04-04#CLM-029": ("MOVE", "", "Rule 3: 'REF-006 is MATCH under D-APP-38; earlier warning is history' restates MATCH as current. SEE:DEL-04-04#REGISTER-1."),
    "DEL-04-05#REGISTER-5": ("MOVE", "", "Rule 1: DEP-04-05-007 Notes say the RQ-011 four-class assertion gap 'remains its own gated Remaining item'; D-APP-65 added the assertions and no such item exists."),
    # PKG-05
    "DEL-05-01#REM-1": ("KEEP", "", "Rule 1: the item's open status is correct (2a fails); its gate names Root DEL-02-11, recorded retired under D-GOV-43."),
    "DEL-05-02#CLM-007": ("KEEP", "", "Rule 2b: the dated P45 reconciliation (2026-07-12) counts '11 ACTIVE / 1 RETIRED' against a register now at 15 ACTIVE; count bookkeeping only."),
    "DEL-05-02#CLM-027": ("KEEP", "", "Rule 2b: repeat of the dated P45 register count. SEE:DEL-05-02#CLM-007."),
    "DEL-05-02#REM-2": ("KEEP", "", "Rule 1: the item's open status is correct (2a fails); Return and Removed-when bind to an 'accepted schema identity' and the write locus names LEGACY_ONLY modules."),
    "DEL-05-03#REM-1": ("KEEP", "", "Rule 1: the work is open (2a fails); the gate on Root schema v2 and the APP-HOLD-1 check were retired by D-APP-127 and amended K-EVENT-6."),
    "DEL-05-03#REGISTER-3": ("MOVE", "", "Rule 2b: the _DEPENDENCIES.md mirror lags Dependencies.csv (DEP-009 PENDING vs SATISFIED, DEP-011 ACTIVE vs RETIRED, TBD placeholder, old counts); the CSV itself is right."),
    # PKG-06
    "DEL-06-01#REGISTER-4": ("KEEP", "", "Rule 2b: _STATUS header 'Last Updated 2026-07-12' and D-APP-19 approval fields are lagging status fields; lifecycle state is consistent."),
    "DEL-06-02#REGISTER-2": ("MOVE", "ALSO:" + RSM, "Rule 4: the Declared TBD sections are bookkeeping (2b), but EvidenceFile names Guidance/Procedure/Datasheet.md, which are absent, and DEP-06-02-011 is SATISFIED on the non-reproducing REF-006 MATCH (1)."),
    "DEL-06-03#REGISTER-2": ("MOVE", "", "Rule 2b: 'TBD - no accepted dependency edges have been extracted yet' is a scaffold TBD placeholder behind the 18-row register; nothing false about the product."),
    "DEL-06-03#REGISTER-3": ("KEEP", "", "Rule 2b: the P45 'current structured-register mirror' counts were never relabelled as history; count bookkeeping only."),
    "DEL-06-04#REGISTER-2": ("MOVE", "", "Rule 2b: the Declared sections are the scaffold TBD placeholder behind extracted ACTIVE edges; nothing false about the product."),
    "DEL-06-05#REGISTER-3": ("KEEP", "ALSO:" + RSM, "Rule 4: the Declared TBD prose is bookkeeping (2b), but Dependencies.csv EvidenceFile names Specification.md/Procedure.md, which are absent (1)."),
    "DEL-06-06#STATE-2": ("UNDECIDED", "", "Reading A (2a): _STATUS ## Remaining is empty while live-path residuals are open, so REMAINING_STATE_MISMATCH. Reading B (1, via rule 4): MEMORY.md:7 names the LEGACY_ONLY sdk-message-mapper as the canonical surface, a present fact now false, so STALE_SPECIFICATION. The row combines both claims."),
    # PKG-07
    "DEL-07-01#REM-1": ("KEEP", "", "Rule 1: open status matches the evidence (2a fails); the write locus names frontend/electron/daemon-instruction-root.ts, which is absent."),
    "DEL-07-01#REGISTER-3": ("MOVE", "", "Rule 2b: 'no accepted edges' and 'report-only preview not written to the carrier' are register labels not flipped after D-APP-109 applied the preview; nothing false about the product."),
    "DEL-07-02#REGISTER-2": ("MOVE", "", "Rule 2b: the RequiredMaturity summary count (TBD 7 vs 3 in the CSV) is register count bookkeeping; nothing false about the product."),
    "DEL-07-02#REGISTER-3": ("KEEP", "", "Rule 1: Dependencies.csv EvidenceFile cites Datasheet.md, Procedure.md and Specification.md in this folder; the files are absent."),
    "DEL-07-02#STATE-1": ("KEEP", "", "Rule 2a: the empty ## Remaining is contradicted by the live scaffold 501 gap and ADQ-06 residuals; header fields lag (2b)."),
    "DEL-07-04#REGISTER-3": ("KEEP", "", "Rule 2b: TBD placeholders, the IMPLEMENTATION_LOCATION_TBD warning and summary counts lag the register; dated run notes are history."),
    "DEL-07-04#REGISTER-4": ("KEEP", "", "Rule 2b: _STATUS header 'Last Updated', Authorization Basis and Checking Approval SHA are lagging status fields."),
    "DEL-07-04#STATE-1": ("KEEP", "", "Rule 2a: the empty ## Remaining is contradicted by open residuals on CLM-011 and CLM-013.10."),
    # PKG-08
    "DEL-08-02#REMTXT-1": ("KEEP", "ALSO:" + RSM, "Rule 4: the Remaining preamble says alias/persona resolution, read-only replay routing and matrix compatibility are 'implemented and validated' (false on the live path, 1) and closes them as done (2a); the repair is rewriting the preamble."),
    "DEL-08-03#SEC-3": ("KEEP", "", "Rule 2b: the dated D-APP-108 seating paragraph says DEP-023/DEP-024 'await the registered dependency-extract pass'; this is dependency bookkeeping behind the 2026-09-05 write, not a product fact."),
    "DEL-08-04#REGISTER-1": ("MOVE", "", "Rule 1: _REFERENCES.md records CONTRACT Actual = Expected, Status MATCH, with no snapshot date; the recomputed hash differs."),
    "DEL-08-04#REGISTER-2": ("MOVE", "", "Rule 1: _REFERENCES.md records SPEC Actual = Expected, Status MATCH, with no snapshot date; the recomputed hash differs."),
    "DEL-08-04#REGISTER-3": ("MOVE", "", "Rule 1: _REFERENCES.md records PRD Actual = Expected, Status MATCH, with no snapshot date; the recomputed hash differs."),
    "DEL-08-05#REGISTER-5": ("KEEP", "", "Rule 2b: the P45 'current structured-register mirror' counts predate DEP-08-05-011; count bookkeeping only."),
    # PKG-09
    "DEL-09-01#REGISTER-2": ("KEEP", "", "Rule 2b: the Declared TBD sections and 'TBD 10' summary lag the register's own rows."),
    "DEL-09-02#REGISTER-3": ("MOVE", "", "Rule 2b: the TBD_SURFACES warning and 'no dependency edges extracted yet' are TBD placeholders behind known surfaces and 25 extracted rows; they mark values as undecided, not absent."),
    "DEL-09-03#REGISTER-2": ("KEEP", "", "Rule 1: every TargetLocation points at the wrong decomposition line and DEP-013 EvidenceFile cites Guidance.md, which is absent; SATISFIED rests on rewritten SOW/OBJ text."),
    "DEL-09-03#REGISTER-3": ("MOVE", "", "Rule 2b: the Declared sections are the scaffold TBD placeholder beside 13 extracted rows in the same file; nothing false about the product."),
    "DEL-09-04#REGISTER-52": ("KEEP", "", "Rule 1: _CONTEXT.md says the Claude Agent SDK remains the current path and cites four retired files, while Codex is the packaged live engine."),
    "DEL-09-05#CLM-019": ("KEEP", "", "Rule 2b: CI workflow path, upload name and runbook filename are TBD placeholders behind recorded values; the remaining TBDs stand."),
    "DEL-09-05#CLM-028": ("KEEP", "", "Rule 2b: upload name, runbook filename and evidence location are TBD placeholders behind recorded values."),
    "DEL-09-05#CLM-032": ("KEEP", "", "Rule 2b: the SoW Open Items TBD set lags recorded values. SEE:DEL-09-05#CLM-019."),
    "DEL-09-05#REGISTER-52": ("KEEP", "", "Rule 1: DEP-09-05-015 presents the G6a owner ruling as an ACTIVE constraint gating WP-11 'as a current factual row'; _STATUS records G6a retired under D-APP-127."),
    "DEL-09-06#REM-2": ("KEEP", "", "Rule 1: the item's open status is correct (2a fails); its NOT_SELECTABLE gate says effective home and login have not landed, but both are LIVE."),
    "DEL-09-06#REGISTER-2": ("MOVE", "", "Rule 2b: the Declared TBD sections and 'currently TBD' test framework, command names and paths are TBD placeholders behind known values."),
    "DEL-09-06#STATE-3": ("KEEP", "", "Rule 2b: MEMORY.md lacks the D-APP-127 application entry; bookkeeping lag only."),
    "DEL-09-07#REGISTER-1": ("KEEP", "", "Rule 2b: _REFERENCES.md records 'Accepted SHA-256' pins with no MATCH verdict; pins lagging later doc edits are bookkeeping."),
    # PKG-10
    "DEL-10-02#REGISTER-2": ("KEEP", "", "Rule 1: the MEMORY entry says IN_PROGRESS 'because active code implementation is underway', a product statement D-APP-37 ruled false."),
    "DEL-10-02#REGISTER-4": ("KEEP", "", "Rule 1: the dependency note says frontend/packages/harness-contract/src/domain-profile.ts declares the fields at lines 120-121; that file is now a re-export."),
    "DEL-10-04#REGISTER-2": ("KEEP", "", "Rule 2b: Declared TBD lists, summary counts and closure text lag Dependencies.csv; register bookkeeping only."),
    "DEL-10-04#REGISTER-3": ("KEEP", "", "Rule 2b: SATISFIED rows keep TBD target fields; the -005 PRD MATCH note is dated 2026-07-10 (rule 3 snapshot)."),
    "DEL-10-05#REGISTER-2": ("KEEP", "", "Rule 3: the basis notes are tied to LastSeen 2026-07-10 and D-APP-53 reverify; anchors and SHAs lag, and SATISFIED is not shown false."),
    "DEL-10-05#REGISTER-3": ("MOVE", "", "Rule 2b: the Declared TBD lines, 'satisfaction lifecycle remains TBD' and '_STATUS.md stays CHECKING' are placeholders and a lagging status field in the register."),
    "DEL-10-05#STATE-3": ("KEEP", "", "Rule 2a: the empty ## Remaining ('no open scope') is contradicted by open items at CLM-036 and missing closure evidence (CLM-019)."),
    # EXT
    "DEC:REGISTER-3": ("KEEP", "", "Rule 1: the D-APP-124 ruling-record cell says PR #739 is '(open; not merged)'; git log shows it merged (2c75eb4bf)."),
}

EXCLUDED = {"DEL-06-02#CLM-005", "DEL-06-02#CLM-032"}


def main():
    h, rows = r3lib.read_csv(os.path.join(r3lib.WORK, "CAND_TIEBREAK.csv"))
    out, seen = [], set()
    for r in rows:
        k = r["ClaimKey"]
        if k in EXCLUDED:
            continue
        cur = r["Disposition"]
        assert cur in (SS, RSM), k
        v, also, basis = D[k]
        new = (RSM if cur == SS else SS) if v == "MOVE" else cur
        if also:
            assert also.split(":", 1)[1] != new, k
        out.append({"ClaimKey": k, "CurrentDisposition": cur, "Verdict": v,
                    "NewDisposition": new, "AlsoNote": also, "Basis": basis})
        seen.add(k)
    missing = set(D) - seen
    assert not missing, missing
    hdr = ["ClaimKey", "CurrentDisposition", "Verdict", "NewDisposition", "AlsoNote", "Basis"]
    r3lib.write_csv(os.path.join(r3lib.WORK, "T5_TIEBREAK_VERDICTS.csv"), hdr, out)
    pkg = {r["ClaimKey"]: r["PackageID"] for r in rows}
    c = collections.Counter((o["Verdict"]) for o in out)
    print("verdicts", dict(c), "total", len(out))
    print("moves", collections.Counter((o["CurrentDisposition"], o["NewDisposition"]) for o in out if o["Verdict"] == "MOVE"))
    byp = collections.defaultdict(collections.Counter)
    for o in out:
        byp[pkg[o["ClaimKey"]]][o["Verdict"]] += 1
    for p in sorted(byp):
        print(p, dict(byp[p]))


if __name__ == "__main__":
    main()
