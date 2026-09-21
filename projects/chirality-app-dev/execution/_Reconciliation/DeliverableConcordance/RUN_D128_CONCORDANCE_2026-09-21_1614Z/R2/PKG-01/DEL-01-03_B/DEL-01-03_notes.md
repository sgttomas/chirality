# DEL-01-03 — R2 forward-pass notes (worker B, double-blind)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-01 wave 4. Frozen basis `00115c719`. Ledger
`DEL-01-03_claims.csv` (45 rows). No split and no pregather.

## 1. Census

**Rows by Disposition (sealed):** ALIGNED 25 · STALE_SPECIFICATION 11 · NOT_AUDITABLE 6 ·
AUTHORITY_CONFLICT 3. Total 45.

**Rows by ClaimType × Disposition:**

| ClaimType | ALIGNED | STALE_SPECIFICATION | NOT_AUDITABLE | AUTHORITY_CONFLICT | Total |
|---|---:|---:|---:|---:|---:|
| REQUIREMENT | 17 | 0 | 0 | 2 | 19 |
| ACCEPTANCE | 3 | 1 | 0 | 0 | 4 |
| EXCLUSION | 0 | 1 | 0 | 0 | 1 |
| CONTEXT_CLAIM | 0 | 4 | 6 | 0 | 10 |
| STATE_ASSERTION | 5 | 3 | 0 | 1 | 9 |
| REGISTER_DEFECT | 0 | 2 | 0 | 0 | 2 |

- **Indexed units:** 31 (CLM-001..CLM-031), all covered. **Run-local rows:** 5 (STATE-1..3,
  REGISTER-1..2).
- **Split rate:** 1 of 31 units split (3.2%). CLM-009 splits into 10 sub-rows (REQ-01..REQ-10,
  a table of separately numbered REQ items). The index lists no sub-items for CLM-009. CLM-013
  (AC-001) and CLM-022 (VER-001) each list one sub-item (k = 1) and are covered on a single row
  that names the item.
- **SEE rows (counted separately, MR-4):** 6. These are CLM-010, CLM-030 and REGISTER-2
  (→ REGISTER-1), CLM-012 and CLM-016 (→ CLM-008), and CLM-019 (→ CLM-011). Excluding them,
  39 rows carry their own disposition: ALIGNED 25, STALE_SPECIFICATION 5, NOT_AUDITABLE 6,
  AUTHORITY_CONFLICT 3.
- **HumanDecisionNeeded:** NO 40 · R4 2 (CLM-024, STATE-2) · R4-Q1 2 (CLM-009.8, .9) · R4-Q5 1
  (CLM-009.3).
- **Confidence:** HIGH 20 · MEDIUM 24 · LOW 1.
- PostReleaseBasis is `NO` on every row. None of the cited files appears in `TOUCHED_PATHS.csv`,
  whose touched set covers Runtime daemon, contracts, client and tests plus Root export files.
  No App `frontend/**` path is touched, so no blame was needed.
- No errata file (pass 1).

## 2. Least-confident rows

- **CLM-009.4 (REQ-04, LOW):** sealed as ALIGNED. The words "state or preserve" are met by
  preservation, because no live copy claims that agent output is approved. No live surface
  states the draft posture on agent output. The one explicit non-approval notice is in
  `workflow-detail.tsx:18`, which is TEST_ONLY. *Alternative:* PARTIALLY_IMPLEMENTED, if the
  requirement is read as needing an affirmative notice.
- **CLM-009.3 (REQ-03, MEDIUM, AUTHORITY_CONFLICT / R4-Q5):** *Alternative:* ALIGNED. On that
  reading the copy test is only whether Codex is disclosed as provider detail with Chirality as
  the product, and the live copy passes that test. I chose the conflict because REQ-03's own
  sources (DIRECTIVE §2.10, K-ENGINE-4, both unamended) conflict with the live "Codex" panel.
  That panel shows upstream notification method names as received, as amended K-EVENT-1 and
  D-GOV-43 require.
- **CLM-024 (MEDIUM, AUTHORITY_CONFLICT / R4):** *Alternative:* ALIGNED, reading the posture as
  copy guidance about identity only. I chose the conflict because the row restates the DIRECTIVE
  §2.8 ownership list ("permission policy", "the SDK" as substrate). D-GOV-43 re-expresses that
  list without naming the clause: approval and sandbox policy become the user's Codex choice,
  with no veto of the user's configuration.
- **STATE-2 (MEDIUM, AUTHORITY_CONFLICT / R4):** *Alternative:* STALE_SPECIFICATION with
  CODEX_SOLE_ENGINE, if D-GOV-43 / amended K-ENGINE-3 is taken to govern. I did not take it,
  because the unamended DIRECTIVE §2.8 still states the Claude default and ranks above CONTRACT.
- **CLM-009.8 / CLM-009.9 (REQ-08/09, MEDIUM, ALIGNED + R4-Q1):** *Alternative:*
  DOCUMENTED_UNIMPLEMENTED, if "future domain-engine notices" is read as a present obligation.
  I read it as conditional on domain surfaces that do not yet exist on the live path.
- **CLM-010 / CLM-030 / REGISTER-2 (MEDIUM, STALE_SPECIFICATION):** *Alternative:* a
  snapshot-bound reading. The text says the "current D-APP-38 corpus snapshot" records a
  matching hash, and snapshot v23 does record it (it equals `_REFERENCES.md`). On that reading
  these rows would fold into REGISTER-1 under MR-8(iv). I applied tie-break rule 3 because the
  text names no version and presents the match as current.

**Authority routes taken on governance-invariant rows that turn on authority** (the brief asks
for this):

| Row | Route |
|---|---|
| CLM-009.3 | AUTHORITY_CONFLICT (R4-Q5): a ruling undercuts unamended DIRECTIVE §2.10, and two CONTRACT texts (K-ENGINE-4 vs amended K-EVENT-1) conflict with no §0 ranking between them |
| CLM-024 | AUTHORITY_CONFLICT (R4): D-GOV-43 / D-APP-127 undercut unamended DIRECTIVE §2.8 without naming it |
| STATE-2 | AUTHORITY_CONFLICT (R4): same mechanism as CLM-024 (Claude default in DIRECTIVE §2.8 vs Codex sole engine) |
| CLM-003, CLM-004, CLM-009.1/.2/.4–.10, CLM-017/018, CLM-025–029 | No authority turn; the cited identity, professional and domain clauses are unamended and unconflicted |

DIRECTIVE §0 ranks documents. It does not rank a Root ruling against the DIRECTIVE, so I did not
use it to resolve these three rows. MR-11 was applied only where a ruling explicitly addresses
the item: D-APP-56 R4-P35 for CT-001 and D-APP-53 for DEL-01-03's dependency rows.

## 3. Register-defect summary

- **REGISTER-1 (`_REFERENCES.md`):** REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD are recorded
  as MATCH, but at `00115c719` they recompute to `57411f8d…`, `8b0d805b…` and `17ca3f3c…`
  (`REFERENCE_HASHES.csv`, Match NO). The recorded values equal the corpus v23 snapshot of
  2026-09-12. REF-001, REF-004, REF-005, REF-007, REF-009 and REF-010 reproduce; REF-007/009/010
  were recomputed on Root `workflows/software-decomp/**`. REF-008 is absent from the numbering,
  which is cosmetic.
- **REGISTER-2 (`Dependencies.csv` DEP-01-03-007/008/011 Notes, `_DEPENDENCIES.md` line 31):**
  undated "now/current … MATCH" premises for SATISFIED. The SATISFIED status itself still holds.
- **Hygiene, not ledgered:** `_DEPENDENCIES.md` lines 26–27 carry machine-absolute paths in the
  2026-05-20 run notes. This is the same class as the run-wide REF-007 absolute-path wart from the
  D-APP-55 run.
- **Stale conflict-table / closure text:** CT-001 was ruled under D-APP-56 R4-P35, but it is
  still shown as TBD in CLM-011, CLM-019 and CLM-020. CLM-030 itself records the ruling
  correctly. The CT-002 closure basis in CLM-030 and CLM-011 rests on the PRD hash match, which
  no longer reproduces.
- **Stale dependency text:** SoW CLM-008, CLM-012 and CLM-016 still say the dependency rows are
  TBD. All 12 are SATISFIED under D-APP-53.
- **Status metadata:** `_STATUS.md` has an empty Remaining and IN_PROGRESS state, which is
  consistent with the rulings (STATE-1). Last Updated 2026-09-04 matches the last carrier change.
- **D-APP-127 map:** every carrier is `NO`. `_CONTEXT.md` still describes the pre-D-GOV-43
  Claude/Anthropic engine (STATE-2).

## 4. Direction and cause

- **CauseTags:** DOC_HYGIENE 6 (hash drift ×4, REF-007, CLM-020); PRE_V3_DRIFT 5 (dependency-TBD
  and CT-001-TBD texts; D-APP-53 of 2026-07-10 and D-APP-56 of 2026-07-12 both predate the
  2026-07-14 SoW finalization and 2026-08-22); CODEX_SOLE_ENGINE 2 (CLM-009.3, STATE-2);
  A2_TOPOLOGY 1 (CLM-024).
- **Secondaries:** CAUSE2:CARRIER_PROPAGATION appears on CLM-006, CLM-008, CLM-011, CLM-012,
  CLM-016, CLM-019, CLM-020 and STATE-2. CAUSE2:A2_TOPOLOGY appears on CLM-010, CLM-030,
  REGISTER-1 and REGISTER-2. CAUSE2:CODEX_SOLE_ENGINE appears on CLM-024.
- **GOVERNING records used:** D-GOV-43 (ruling set under Root
  `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/`; grep for
  DIRECTIVE / product identity / §2.8 / §2.11 / K-SDK-4 finds only Root DIRECTIVE §5/§7 in
  IMPACT.md, never App DIRECTIVE §2.8/§2.10), D-APP-127, D-APP-56 (R4-P35, P43, P45), D-APP-53,
  D-APP-38, D-APP-108.
- **CONTEXT records used:**
  - `execution/_Coordination/AgentRuns/CHIRALITY_V3_APP_ADOPTION_20260909/CORPUS_V21_CANDIDATE.md`
    (v3 four-role adoption), for CLM-006.
  - `plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md` line 200 (the DEL-01-03
    copy-table note), for STATE-1.
  - `execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/_run_records/initial-checks/corpus-status.stdout.txt`,
    cited in Notes only. RUN_BASIS §5 does not list it as a CONTEXT source; it corroborates the
    known basis defect.
- **Searches:** I grepped `_DECISIONS/_REGISTER.md` for DEL-01-03, "product identity" and
  "boundary copy". It has no row naming DEL-01-03 other than via D-APP-55, D-APP-56 and D-APP-108;
  D-APP-53 names it in its ruling. I also grepped the D-APP-127 ruling for DIRECTIVE, DEL-01-03 and
  identity, and found no hit on App DIRECTIVE or this deliverable. No row uses `NONE_FOUND` in
  DirectionEvidence.

## 5. Method friction

- **MR-4 versus attribute and condition tables.** CLM-003 (Attributes) and CLM-004 (Conditions)
  are the earliest units, and they restate the postures that REQ-01..REQ-10 (CLM-009) then state
  as requirements. Applied literally, MR-4 would make the ten REQ rows `SEE:` rows of a composite
  table row that has no clean single disposition. I gave each REQ its own full disposition and
  used plain-text `cf.` references. *Proposed revision:* when an earlier unit is a composite
  table and a later unit states the same content as numbered REQ items, the numbered REQ rows
  carry the disposition and the table row gets `cf.`.
- **"Future" requirements (REQ-08/09) versus live-path judgment.** The §2.3 rule
  (DOCUMENTED_UNIMPLEMENTED if the live path lacks it) does not say what happens when the
  requirement is conditional on a surface that is not yet in scope. I used ALIGNED plus R4-Q1,
  per rule 3. *Proposed revision:* add an explicit case for "conditional future-surface"
  requirements.
- **Named-snapshot wording.** Rule 3 of the tie-break fits "MATCH at v23" and "is MATCH", but not
  "the current D-APP-38 corpus snapshot records a match". That text is snapshot-bound, but it does
  not name the version. See §2.
- **Governance gap, outside any row:** K-SDK-4, DIRECTIVE §2.11 and PRD FR-127 name only Claude
  Code and Anthropic. The live engine vendor is Codex/OpenAI. No GOVERNING text or DEL-01-03
  carrier states a Codex/OpenAI identity boundary.

## 6. Effort

About 30 files or file slices read: the deliverable folder (8 carriers plus 4 run records), App
DIRECTIVE/CONTRACT/PLAN/PRD slices, `BOUNDARY_REVIEW_CHECKLISTS.md`, the D-APP-56, D-APP-108 and
D-APP-127 slices, the D-GOV-43 grep, about 15 frontend component or test slices, and the evidence
pack by script. Root `agents/` and `workflows/software-decomp/` were used for listing and hashing
only. The context budget was adequate, not tight.

## Coverage gaps

1. **`docs/BOUNDARY_REVIEW_CHECKLISTS.md` content is stale, and no row owns it.** This is the
   DEL-01-03/DEL-01-04 materialized artifact, and it is not an indexed unit.
   - Lines 9 and 78 say "REF-006 `docs/PRD.md` currently MATCH", which no longer reproduces.
   - Line 25 says "absent that, the Anthropic key-aware loopback default stands". Amended
     K-NET-1 lists the loopback/Anthropic path as compatibility history.
   - SB-02 frames the settings boundary as Claude `settingSources: []` and `~/.claude`, which
     are pre-D-GOV-43 terms.
   - Suggested owner: DEL-01-03 jointly with DEL-01-04.
2. **The shell-redesign copy pass has had no DEL-01-03 review.**
   - The D-APP-108 note offered the `03_TARGET_SPEC.md` §10 plain-language copy table as a
     candidate amendment; it was not adopted.
   - The live woven-shell copy (DEL-02-01-V3-01) and the Codex account and approval copy have no
     DEL-01-03 release-review evidence record. The Review ID and surfaces in the template are
     still TBD.
   - No forward row covers the review of these newer live surfaces.
3. **Codex/OpenAI identity boundary.** The live hosted copy says "other Codex clients keep their
   own sign-in", which frames Chirality as a Codex client. No carrier or GOVERNING clause
   addresses Codex/OpenAI identity (§5).
4. **App metadata description.** `frontend/src/app/layout.tsx:59` reads "PORTAL, PIPELINE, and
   WORKBENCH shell for local agent execution". It describes the pre-SCA-APP-010 shell, and no
   DEL-01-03 unit covers it. DEL-02-01 may own it.
