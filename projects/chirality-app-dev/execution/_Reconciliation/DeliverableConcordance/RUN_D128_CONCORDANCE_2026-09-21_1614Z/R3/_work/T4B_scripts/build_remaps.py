"""T4B: build T4B_REMAPS.csv for run-wide calls (c), (d), (f). Emits only real changes
against the current cells of R3/CLAIM_CONCORDANCE.csv and R3/EXTENSION_CONCORDANCE.csv."""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r3lib import read_csv, write_csv, R3, WORK

cur = {}
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    _, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        cur[r["ClaimKey"]] = r

OUT = []
def add(key, field, new, call, ev):
    r = cur[key]  # KeyError = wrong key; fail loudly
    if field != "Notes+" and r[field] == new:
        return
    OUT.append({"ClaimKey": key, "Field": field, "NewValue": new, "Call": call, "Evidence": ev})

# ---------------- (c) SoW-conversion parity ----------------
OWNER_Q = ("OWNER_CHECK: Did the July 2026 D-GOV-16 Stage-2 conversion record validator, claim-map, parity, "
           "checklist and render results and an independent verifier return for this deliverable's ScopeOfWork.md?")
C2_EV = ("D-GOV-16 items 7-8 (docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md:128-168) "
         "place map/parity/checklist results in per-deliverable receipts and verifier returns of the Stage-2 wave run, "
         "outside the evidence roots; App AgentRuns SOW-STAGE2-EXEC-20260712-01-C2A* hold only the frontend runtime "
         "activation; CONVENTIONS 2.6 Addendum 10")

# C1: AC-001 content rows, parity recomputed by T4B from frozen git (R3/_work/T4B_scripts/parity.py)
add("DEL-00-02#CLM-014.2", "Disposition", "ALIGNED", "c",
    "parity.py: 209/209 non-empty legacy lines at fae8e5117^ present in ScopeOfWork.md at fae8e5117 and 670a71ed0; "
    "1 line changed by 7fd0466f9 (D-APP-65), 10 by 03f4e10d8 (D-APP-68 disposition 1 names the PKG-00/01 rows); MR-11")
add("DEL-00-02#CLM-014.2", "Notes+",
    "R3_RUNWIDE(c): class C1 (AC-001 legacy content). T4B recomputed line parity from frozen git: 209/209 legacy "
    "lines kept at 670a71ed0; the 11 later changes come from D-APP-65 (7fd0466f9) and D-APP-68 (03f4e10d8), which "
    "stand under MR-11. Sealed UNKNOWN rested on no parity artifact in the App tree. ALSO:UNKNOWN.", "c",
    "R3/_work/T4B_scripts/parity.py over git show fae8e5117^ vs 670a71ed0/7fd0466f9/03f4e10d8")
add("DEL-05-03#CLM-014.1", "Disposition", "ALIGNED", "c",
    "parity.py: 248/248 non-empty legacy lines at e9b9e302c^ present in ScopeOfWork.md at e9b9e302c and 571e729d1; "
    "one line (DEL-05-03-R14) changed by 03f4e10d8 under D-APP-68 disposition 7, which names DEL-05-03; MR-11")
add("DEL-05-03#CLM-014.1", "CauseTag", "NONE", "c", "ALIGNED row; no divergence mechanism")
add("DEL-05-03#CLM-014.1", "Notes+",
    "R3_RUNWIDE(c): class C1 (AC-001 legacy content). T4B recomputed line parity from frozen git: 248/248 legacy "
    "lines kept at e9b9e302c and 571e729d1; the one later change (DEL-05-03-R14, 03f4e10d8) is D-APP-68 "
    "disposition 7 (MR-11). RemainingWork UNKNOWN on this row is now NONE_OBSERVED (manager applies). ALSO:UNKNOWN.",
    "c", "R3/_work/T4B_scripts/parity.py over git show e9b9e302c^ vs e9b9e302c/571e729d1/03f4e10d8")

# C2: VER-001 conversion checks with no conversion record in the evidence roots -> UNKNOWN + OWNER_CHECK
C2 = {
    # key: (alt reading kept, extra note)
    "DEL-00-01#CLM-018.2": ("DOCUMENTED_UNIMPLEMENTED", ""),
    "DEL-00-02#CLM-021.2": ("PARTIALLY_IMPLEMENTED", " Positive part: validate_scope_of_work PASS in _run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md."),
    "DEL-01-01#CLM-018": ("ALIGNED", " The Records half holds (run records exist); only the VER-001 check record is missing from the App tree."),
    "DEL-01-02#CLM-038.4": ("PARTIALLY_IMPLEMENTED", " The sealed search looked in frontend/scripts; the conversion tools are Root-owned."),
    "DEL-01-03#CLM-022": ("PARTIALLY_IMPLEMENTED", " Positive part: validator PASS 2026-07-19. The human-review half is an open lifecycle gate (IN_PROGRESS)."),
    "DEL-01-04#CLM-020.2": ("PARTIALLY_IMPLEMENTED", " Positive part: validator PASS 2026-07-19. The human-review half is an open lifecycle gate (IN_PROGRESS)."),
    "DEL-02-01#CLM-023.2": ("DOCUMENTED_UNIMPLEMENTED", ""),
    "DEL-02-02#CLM-021.2": ("", ""),
    "DEL-02-03#CLM-023.2": ("", ""),
    "DEL-02-04#CLM-021.2": ("", ""),
    "DEL-02-05#CLM-020.1": ("DOCUMENTED_UNIMPLEMENTED", ""),
    "DEL-05-03#CLM-020.1": ("", ""),
    "DEL-05-04#CLM-019.2": ("", ""),
    "DEL-10-01#CLM-022.2": ("ALIGNED", " The sealed ALIGNED rested on a Root AgentRuns CHECKS.md (30/30) outside the evidence roots."),
    "DEL-10-04#CLM-023.2": ("", ""),
    "DEL-10-05#CLM-020.1": ("PARTIALLY_IMPLEMENTED", " Positive part: sow-source-begin PRESERVED markers in 9ccbbea99, removed at finalization b5c9a1760 as the SoW standard prescribes."),
}
for k, (alt, extra) in C2.items():
    add(k, "Disposition", "UNKNOWN", "c", C2_EV)
    add(k, "CauseTag", "DOC_HYGIENE", "c", "class C2 shape: the operative issue is a conversion record not carried in the App tree")
    sealed_alt = f" ALSO:{cur[k]['Disposition']} (sealed)." if cur[k]["Disposition"] != "UNKNOWN" else ""
    add(k, "Notes+",
        f"R3_RUNWIDE(c): class C2 (VER-001 conversion checks, no conversion record in the evidence roots). {OWNER_Q}"
        f"{extra}{sealed_alt}", "c", C2_EV)

# C2 notes on mixed rows whose parity part rests on absence (Disposition stands on other evidence)
for k in ["DEL-03-02#CLM-018", "DEL-05-05#CLM-020.2"]:
    add(k, "Notes+",
        f"R3_RUNWIDE(c): the VER-001 parity part of this row is class C2 (no conversion record in the evidence roots); "
        f"the Disposition stands on other evidence. {OWNER_Q}", "c", C2_EV)
add("DEL-10-02#CLM-019.2", "Notes+",
    "R3_RUNWIDE(c): class C2-R (parity reproduced; sealed STALE_VERIFICATION rests on the 0410a15df frontmatter pin "
    "edit after finalization). The same pin edit touched other converted SoWs judged ALIGNED or UNKNOWN (RUN_BASIS 5 "
    f"known basis defect). ALSO:UNKNOWN. {OWNER_Q}", "c", C2_EV)

# ---------------- (d) D-GOV-43 policy rows under R4-Q6 ----------------
D_EV = ("App DIRECTIVE 2.8/2.10/4.1/4.2 and CONTRACT K-PERM-1/K-PERM-6 unamended at 00115c719 "
        "(projects/chirality-app-dev/docs/DIRECTIVE.md:115-150,225-270; CONTRACT.md:90,95); D-GOV-43 items 3-4 "
        "(Root AGENTS.md; CONTRACT.md:17) do not name them; CONVENTIONS 1 and 2.4 R4-Q6; Addendum 9 context only")
SUB = {
    "SC": "shared Codex configuration and resources (~/.codex link, settings isolation, plugins/MCP; DIRECTIVE 4.2 vs D-GOV-43 item 3)",
    "AP": "approval policy and permission ownership (DIRECTIVE 2.8, 4.1-4.2, K-PERM-1 hard-deny precedence vs D-GOV-43 item 4)",
    "FA": "live Full access option (K-PERM-6, DIRECTIVE 4.2 vs D-GOV-43 item 4)",
    "EV": "event pass-through (DIRECTIVE 2.10 with K-ENGINE-4; R4-Q5 carries the K-EVENT side)",
    "ED": "Claude/Anthropic default and API-key UI (DIRECTIVE 2.8, 4.1)",
}
D = [  # key, sub, new HDN (None = unchanged), to_AC
    ("DEL-01-02#CLM-006.7", "SC", "R4-Q1; R4-Q6", False),
    ("DEL-01-02#CLM-018.8", "SC", "R4-Q1; R4-Q6", False),
    ("DOC:RELIANCE#3.8", "SC", "R4-Q1; R4-Q6", True),
    ("DOC:RELIANCE#4.8", "SC", "R4-Q1; R4-Q6", True),
    ("SOW:SOW-045.2", "SC", "R4-Q1; R4-Q6", True),
    ("SOW:SOW-076", "SC", "R4-Q6", False),
    ("SOW:SOW-075.2", "SC", "R4-Q6", False),
    ("DEL-01-04#CLM-003.1", "SC", "R4-Q6", False),
    ("DEL-01-04#CLM-003.4", "SC", "R4-Q6", False),
    ("DEL-01-04#CLM-006.1", "SC", "R4-Q6", False),
    ("DEL-01-04#CLM-010.2", "SC", "R4-Q6", False),
    ("DEL-01-04#CLM-023", "SC", "R4-Q6", False),
    ("DEL-01-04#CLM-004.5", "SC", "R4-Q6", False),
    ("DEL-01-04#REGISTER-3", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-01-02#CLM-006.3", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-01-02#CLM-007.4", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-01-02#CLM-018.10", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-01-02#CLM-044", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-01-03#CLM-024", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-01#CLM-003", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-06-01#CLM-009.3", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-06-01#CLM-024", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-06-01#CLM-025", "AP", "R4-Q1; R4-Q6", True),
    ("DEL-06-04#CLM-003", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-04#CLM-009.7", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-04#CLM-018", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-04#CLM-022", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-05#CLM-022", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-05#CLM-004.2", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-06-03#CLM-004", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-09-02#CLM-010.6", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-09-03#CLM-005.8", "AP", None, True),
    ("DEL-09-03#CLM-009.9", "AP", None, True),
    ("DOC:RELIANCE#3.4", "AP", "R4-Q1; R4-Q6", True),
    ("DOC:RELIANCE#4.4", "AP", "R4-Q1; R4-Q6", True),
    ("SOW:SOW-050.2", "AP", "R4-Q1; R4-Q6", False),
    ("DEL-01-04#CLM-003.5", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-01-04#CLM-006.2", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-01-04#CLM-010.4", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-01-04#CLM-024", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-01-04#CLM-025", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-06-01#CLM-009.9", "FA", "R4-Q1; R4-Q6", False),
    ("DEL-06-01#CLM-004", "FA", "R4; R4-Q1; R4-Q6", False),
    ("DEL-06-01#CLM-027", "FA", "R4; R4-Q1; R4-Q6", False),
    ("DEL-06-01#CLM-031", "FA", "R4; R4-Q1; R4-Q6", False),
    ("DEL-06-01#CLM-032", "FA", "R4-Q6", False),
    ("DEL-01-01#CLM-009.7", "EV", "R4-Q1; R4-Q5; R4-Q6", False),
    ("DEL-01-01#CLM-021.5", "EV", "R4-Q1; R4-Q5; R4-Q6", False),
    ("DEL-01-01#CLM-023", "EV", "R4-Q1; R4-Q5; R4-Q6", False),
    ("DEL-03-01#CLM-004.1", "EV", "R4-Q5; R4-Q6", False),
    ("DEL-03-01#CLM-004.6", "EV", "R4-Q5; R4-Q6", False),
    ("DEL-03-01#CLM-009.2", "EV", "R4-Q5; R4-Q6", False),
    ("DEL-03-01#CLM-009.7", "EV", "R4-Q5; R4-Q6", False),
    ("DEL-04-05#CLM-026", "EV", "R4-Q5; R4-Q6", False),
]
EXTRA = {
    "DEL-06-01#CLM-004": " R4 kept for the K-PERM-4/K-PERM-5 half, which R4-Q6 does not name.",
    "DEL-06-01#CLM-027": " R4 kept for the K-PERM-4/K-PERM-5 half, which R4-Q6 does not name.",
    "DEL-06-01#CLM-031": " R4 kept for the K-PERM-4/K-PERM-5 half, which R4-Q6 does not name.",
    "SOW:SOW-075.2": " The clause at stake is DIRECTIVE 2.6 (no hidden memory); it enters R4-Q6 through the unfiltered ~/.codex link (memories, sessions).",
    "DEL-01-04#CLM-004.5": " The row turns on whether the CLM-003.4/003.5/STATE-2 conflicts stand.",
    "DEL-01-04#REGISTER-3": " Disposition unchanged (tie-break rule 1); whether the constraint still binds is the CLM-003.5 question.",
    "DEL-06-01#CLM-032": " Disposition unchanged; the text 'no direct source conflict' turns on this conflict.",
    "DOC:RELIANCE#3.8": " The row's literal wording names Claude Code settings only (ALSO:ALIGNED on that reading, as DEL-01-04#CLM-010.3 holds for the named files).",
    "DOC:RELIANCE#4.8": " The row's literal wording names Claude Code settings only (ALSO:ALIGNED on that reading).",
}
for key, sub, hdn, to_ac in D:
    r = cur[key]
    if to_ac:
        add(key, "Disposition", "AUTHORITY_CONFLICT", "d", D_EV)
    if hdn is not None:
        add(key, "HumanDecisionNeeded", hdn, "d", D_EV)
    also = f" ALSO:{r['Disposition']} (sealed)." if to_ac else ""
    add(key, "Notes+",
        f"R3_RUNWIDE(d): R4-Q6 cluster {sub}: {SUB[sub]}. Rules conflict pending the owner's R4 confirmation; the "
        f"owner's recorded answer (Addendum 9) is context only and not applied.{also}{EXTRA.get(key, '')}", "d", D_EV)

# ED: engine-default statement rows, two readings kept (UNDECIDED at R3)
ED_AC = {"DEL-01-01#STATE-1": "R4-Q1; R4-Q6", "DEL-01-02#STATE-1": "R4-Q1; R4-Q6", "DEL-01-02#CLM-040": "R4-Q1; R4-Q6",
         "DEL-01-03#STATE-1": "R4-Q1; R4-Q6", "DEL-01-03#STATE-3": "R4-Q1; R4-Q6", "DEL-01-04#STATE-2": "R4-Q1; R4-Q6",
         "DEL-01-04#STATE-4": "R4-Q1; R4-Q6", "DEL-04-01#CLM-003": "R4-Q1; R4-Q6",
         "DEL-02-05#CLM-003.1": "R4-Q6", "DEL-02-05#CLM-004.2": "R4-Q6", "DEL-02-05#CLM-005.2": "R4-Q6"}
ED_SS = ["DEL-03-01#CLM-021", "DEL-04-01#STATE-2", "DEL-04-02#CLM-004", "DEL-04-02#CLM-023", "DEL-04-02#STATE-1",
         "DEL-04-04#STATE-1", "DEL-04-05#STATE-2", "DEL-06-01#STATE-1", "DEL-06-02#REGISTER-4", "DEL-06-03#STATE-1",
         "DEL-06-04#STATE-1", "DEL-06-05#REGISTER-5", "DEL-09-01#STATE-1", "DEL-09-02#STATE-1", "DEL-09-03#STATE-1",
         "DEL-09-04#REGISTER-52", "DEL-09-05#REGISTER-55", "DEL-09-06#STATE-1", "DEL-10-01#STATE-1",
         "DEL-10-02#REGISTER-3", "DEL-10-03#STATE-1", "DEL-10-04#STATE-1", "DEL-10-05#STATE-1"]
ED_EV = ("DIRECTIVE.md:115-136 (2.8: Claude key-aware default; 'Every other provider or harness path requires a fresh "
         "governed tranche'); CONTRACT K-ENGINE-3 and Codex-only preambles amended under D-GOV-43; D-GOV-43 names Root "
         "DIRECTIVE 5/7 only")
for k, hdn in ED_AC.items():
    add(k, "HumanDecisionNeeded", hdn, "d", ED_EV)
    add(k, "Notes+",
        f"R3_RUNWIDE(d): R4-Q6 cluster ED: {SUB['ED']}. Two readings kept, UNDECIDED at R3: AUTHORITY_CONFLICT "
        "(sealed; D-GOV-43 does not name App DIRECTIVE 2.8) and ALSO:STALE_SPECIFICATION (2.8 itself admits other paths "
        "through a fresh governed tranche, which D-GOV-43 and amended K-ENGINE-3 supply; the reading of DEL-04-02#CLM-004). "
        "Owner answer (Addendum 9) context only.", "d", ED_EV)
for k in ED_SS:
    add(k, "Notes+",
        f"R3_RUNWIDE(d): R4-Q6 cluster ED: {SUB['ED']}. Two readings kept, UNDECIDED at R3: STALE_SPECIFICATION (sealed; "
        "authority order resolved by the fresh-tranche clause of DIRECTIVE 2.8) and ALSO:AUTHORITY_CONFLICT (unamended "
        "2.8 'Claude remains the default', not named by D-GOV-43; the reading of DEL-01-0x STATE rows, R4-Q6).",
        "d", ED_EV)

# ---------------- (f) release-signing cluster ----------------
F_EV = ("R2/PKG-09/VERIFICATION.md 5.1; R2/PKG-09/PACKAGE_SUMMARY.md 9 item 2; CONTRACT.md:17 vs :138; PRD.md:339-346; "
        "D-APP-97_RULING_RELEASE_PREPARATION_2026-08-17.md:20; decomposition v3_2 DEL-09-05 row (G6a)")
F_ROWS = ["DEL-09-04#CLM-003.1", "DEL-09-04#CLM-004.3", "DEL-09-04#CLM-008", "DEL-09-04#CLM-009.1",
          "DEL-09-04#CLM-011.6", "DEL-09-04#CLM-012.2", "DEL-09-04#CLM-016", "DEL-09-04#CLM-017",
          "DEL-09-04#CLM-022", "DEL-09-04#CLM-023.3",
          "DEL-09-05#STATE-1", "DEL-09-05#CLM-003", "DEL-09-05#CLM-009", "DEL-09-05#CLM-010.6", "DEL-09-05#CLM-010.7",
          "DEL-09-05#CLM-012", "DEL-09-05#CLM-013", "DEL-09-05#CLM-016.3", "DEL-09-05#CLM-016.6",
          "DEL-09-05#CLM-020", "DEL-09-05#CLM-023.2", "DEL-09-05#CLM-026", "DEL-09-05#REM-2",
          "DEL-09-05#REGISTER-52", "DEL-09-05#STATE-52",
          "SOW:SOW-072", "DOC:BUILDREL#4.14", "DOC:BUILDREL#11"]
for k in F_ROWS:
    add(k, "Notes+",
        "R3_CLUSTER:RELEASE_SIGNING. One question for the owner: does the amended CONTRACT preamble (K-RELEASE-1 read "
        "with D-GOV-43 items 1 and 4; SPEC 19.4; PRD 7.12/12.8) supersede the unsigned/unnotarized target (K-RELEASE-1 "
        "row text, PRD 6.2), the D-APP-97 F-APP-2 signing fence and the G6a exact-candidate gate? Disposition unchanged "
        "pending that answer.", "f", F_EV)
for k in ["DEL-09-04#CLM-022", "DEL-09-04#CLM-023.3"]:
    add(k, "HumanDecisionNeeded", "R4", "f",
        "MR-11 (CONVENTIONS 1): an AUTHORITY_CONFLICT row carries R4 or R4-Qn; PKG-09 CORRECTIONS set NO while the "
        "Disposition stayed AUTHORITY_CONFLICT. No named question fits (not R4-Q6: K-RELEASE-1 is not a DIRECTIVE/K-PERM text).")

write_csv(os.path.join(WORK, "T4B_REMAPS.csv"), ["ClaimKey", "Field", "NewValue", "Call", "Evidence"], OUT)
from collections import Counter
print(len(OUT), Counter((o["Call"], o["Field"]) for o in OUT))
# stats for the md
json.dump({k: {f: cur[k][f] for f in ("Disposition", "SealedDisposition", "HumanDecisionNeeded", "CauseTag")}
           for k in {o["ClaimKey"] for o in OUT}},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "current_cells.json"), "w"), indent=1, sort_keys=True)
