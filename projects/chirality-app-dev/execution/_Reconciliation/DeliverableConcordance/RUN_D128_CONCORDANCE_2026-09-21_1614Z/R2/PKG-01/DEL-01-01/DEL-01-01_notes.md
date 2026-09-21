# DEL-01-01 — R2 forward-pass notes

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-01 wave 4, TASK worker (pass 1). Basis: frozen tree
at `00115c719`. Ledger: `DEL-01-01_claims.csv` (50 rows, validator PASS, 0 errors, 0 warnings).

## 1. Census

Indexed units: 26 (CLM-001..CLM-026; no REM, REMTXT or SEC units). Run-local rows: REGISTER-1..2,
STATE-1..3. Total rows: 50.

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| ALIGNED | 19 | 3 |
| STALE_SPECIFICATION | 13 | 6 |
| NOT_AUDITABLE | 7 | 0 |
| STALE_ASSESSMENT | 4 | 1 |
| AUTHORITY_CONFLICT | 4 | 2 |
| PARTIALLY_IMPLEMENTED | 3 | 2 |
| **Total** | **50** | **14** |

Without SEE rows (36 rows): ALIGNED 16, STALE_SPECIFICATION 7, NOT_AUDITABLE 7, STALE_ASSESSMENT 3,
AUTHORITY_CONFLICT 2, PARTIALLY_IMPLEMENTED 1. Six of the fourteen SEE rows point at `REGISTER-1`
(tie-break rule 3).

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 26 |
| CONTEXT_CLAIM | 10 |
| STATE_ASSERTION | 8 |
| ACCEPTANCE | 4 |
| REGISTER_DEFECT | 2 |

**Split rate:** 3 of 26 units (11.5%): CLM-004 (six-row conditions table → .1-.6), CLM-009 (ten
numbered DEL-01-01-REQ-001..010 → .1-.10) and CLM-021 (six numbered principles → .1-.6). CLM-012
(AC-001) and CLM-018 (VER-001) list one sub-item each and take one row.

**HumanDecisionNeeded:** NO 43; `R4-Q1` 3 (CLM-004.4, CLM-009.6, CLM-021.4); `R4-Q5; R4-Q1` 3
(CLM-009.7, CLM-021.5, CLM-023); `R4-Q1; R4` 1 (STATE-1).

No errata file exists (pass 1).

## 2. Least-confident rows

- **CLM-017 (LOW).** It is STALE_SPECIFICATION with SEE:REGISTER-1. The alternative: the
  reference-integrity cell is a pass condition, not a present-tense fact. On that reading the row is
  ALIGNED as a criterion, and the deliverable now fails it; the failure itself is on REGISTER-1.
- **CLM-009.2 / CLM-004.1 (MEDIUM, ALIGNED).** The live transition API enforces actor `HUMAN` plus an
  approval SHA, but the actor is a caller-supplied string. A stricter reading of "human-only" would
  give PARTIALLY_IMPLEMENTED. R4-Q3 covers only the legacy `status_transition` tool, so it is not cited.
- **CLM-004.4 / CLM-009.6 / CLM-021.4 (MEDIUM, PARTIALLY_IMPLEMENTED, R4-Q1).** The alternative is
  AUTHORITY_CONFLICT, on the view that D-GOV-43 item 4 (user-chosen approval and sandbox) undercuts
  unamended DIRECTIVE §2.9 and K-RELIANCE-2 without naming them. I kept the live-path verdict and cited
  the named question: R4-Q1 frames exactly this (K-PATH/K-ROOT/K-HOOK unamended for D-GOV-43), and the
  SoW agrees with the GOVERNING text.
- **CLM-021 split.** Splitting a numbered principle list stretches the "table of independently
  dispositionable rows" clause. Without the split, one row would have had to carry three different
  verdicts.

## 3. Register-defect summary

- **REGISTER-1** (`_REFERENCES.md`): REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD record MATCH at the
  corpus v23 hashes (2026-09-12). All three docs changed later that day (`7f1e9f387`, `9eaddb596`), so
  the hashes no longer reproduce (`HASH-RECOMPUTE@00115c719`, pack `REFERENCE_HASHES.csv`). I recomputed
  REF-001 DIRECTIVE, REF-004 TYPES, REF-005 PLAN and REF-007/009/010 (Root software-decomp workflow);
  those still match. SoW rows restating MATCH as current (CLM-003, CLM-010, CLM-017, CLM-022) cite
  REGISTER-1.
- **REGISTER-2** (`Dependencies.csv` / `_DEPENDENCIES.md`) has four stale entries:
  - DEP-01-01-011 targets `agents/AGENT_SOFTWARE_DECOMP.md` by a machine-specific absolute path, and
    that file was deleted by `d1166698d` (2026-09-09).
  - Several evidence notes say "source listed as MATCH".
  - `_DEPENDENCIES.md:62` still says REF-006 is no longer blocked by a hash mismatch.
  - The decomposition line anchors are stale.

  Satisfaction and status fields are unaffected.
- **Other stale carrier text:**
  - The SoW conflict table (CLM-025) is inconsistent with CLM-026 R002 and omits the deliverable
    table's OPEN C003.
  - CLM-026 R001 stays "Closed" although its own reopen trigger (an authority document changed) has
    fired.
  - SoW REF-007 (CLM-006) and `_REFERENCES.md` REF-007 name different sources.
  - `_CONTEXT.md:44` still instructs keeping `ResponsibleParty: TBD` (STATE-2).
- **D-APP-127 application map:** no DEL-01-01 carrier cites D-APP-127 or D-GOV-43. For this
  deliverable that matters only through `_CONTEXT.md` (STATE-1).

## 4. Direction and cause

- **CauseTags:** DOC_HYGIENE 12, CODEX_SOLE_ENGINE 7, RUNTIME_EXTRACTION 3, A2_TOPOLOGY 2, NONE 26.
- **`CAUSE2:` tags:**
  - A2_TOPOLOGY on CLM-004.4, CLM-009.6 and CLM-021.4;
  - CODEX_SOLE_ENGINE on CLM-009.1 and CLM-011;
  - CARRIER_PROPAGATION on CLM-005, CLM-009.5 and CLM-016. The SoW was re-pinned to `d6f6cadb2` on
    2026-09-03 (A12 seating). That is the commit that rewrote CONTRACT K-EVENT-4, and the audit-mirror
    text was not revised.
- **Records used:**
  - GOVERNING: D-GOV-43 (proposal packet `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/`,
    items 1, 2, 4 and 5; the surfaces list names Root DIRECTIVE §5/§7 only); D-APP-127 (names no
    PKG-01 carrier and no App DIRECTIVE clause); D-APP-38, 54, 65, 68 and 73 register rows.
  - CONTEXT: `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Contract_Amendments.proposed.md`
    §K-EVENT-4 (source of the userData-store wording that `d6f6cadb2` applied).
- **Searches behind each `NONE_FOUND`** (CLM-003, 006, 010, 017, 022, 025, 026, CLM-009.8, CLM-021.6,
  REGISTER-1/2, STATE-2):
  - `_REGISTER.md`, searched for DEL-01-01, PKG-01, corpus/drift and Codex-only / sole-engine. Hits:
    D-APP-65 and D-APP-114 only; neither explains the drift.
  - RUN_BASIS §5 CONTEXT sources (SCA-APP-008 packet; AgentRuns APP_V3_* / APPDEV_V3_NODE_*).
  - `NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md:27` and `NOTICE_2026-09-19_LOOP_CLARIFICATIONS.md:19` do
    acknowledge the authority-corpus drift. They are execution notices, not listed CONTEXT sources, so
    they are named in Notes and not cited as `CTX:`.
- **Authority routes on governance-invariant rows:**
  - **DIRECTIVE §0 order applied, no conflict** (CLM-005, CLM-009.5, CLM-016). DIRECTIVE §2.3
    ("…or an explicitly configured Chirality-controlled session path") reconciles with CONTRACT
    K-EVENT-4's userData store. The SoW restates only the first disjunct.
  - **AUTHORITY_CONFLICT** on two issues. D-GOV-43 undercuts App DIRECTIVE clauses without naming them,
    so the order cannot settle either one:
    - CLM-009.7, CLM-021.5 and CLM-023: DIRECTIVE §2.10 and CONTRACT K-ENGINE-4 (unamended) versus
      amended K-EVENT-1 and K-EVENT-6 (upstream Codex payloads preserved; live
      `delegated-engine-adapter.ts`). Framed as R4-Q5.
    - STATE-1: DIRECTIVE §2.8 (Claude Agent SDK key-aware default, "Claude remains the default and
      supervisor", unamended) versus CONTRACT K-ENGINE-3 (Codex sole MVP engine). No named question
      covers this, so plain R4; R4-Q1 is cited by evidence.
  - **Named question R4-Q1, no conflict routed** (CLM-004.4, CLM-009.6, CLM-021.4).
  - **MR-11 not applied anywhere:** no ruling explicitly addresses a DEL-01-01 clause.
- **Coverage gaps:**
  1. App DIRECTIVE §8 ("one opt-in per-user daemon owns engines, credentials, sessions…") is also
     unamended against PRD, CONTRACT and SPEC A2. No DEL-01-01 claim restates §8, so no row owns it.
     It falls within DEL-01-01's alignment scope (CLM-008; cf. CLM-009.1). DIRECTIVE §2.3, §2.8 and §8
     are the unamended clauses the corpus now disagrees with.
  2. The seven D-APP-65 production artifacts (Checklists, Notes, Table, dated 2026-07-18) are not
     declared-state carriers and have no index units. Several of their PASS verdicts are now overtaken
     (Document_Diff D-01; Notes N-05, N-06, N-10; Runtime_Audit A-01; Acceptance C-08). Table W-01
     targets SoW text that D-APP-68 already fixed but misses `_CONTEXT.md:44`. These are used as
     AssessmentEvidence on CLM-009.1, 009.5, 009.8, CLM-011 and CLM-021.6 and are otherwise unowned.
  3. `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` (2026-05-20 lenses citing retired four-document files
     and machine-specific absolute paths) are self-labelled non-authority. No row was written.

## 5. Method friction

- **AssessmentEvidence for doc-only deliverables.** MR-1 speaks of the INSP-03 assessment, but the
  operative verdicts for a DOC_UPDATE deliverable are its own dated checklists. I treated those
  checklists as assessment evidence for STALE_ASSESSMENT. Proposal: name deliverable-produced review
  artifacts explicitly as assessment-class evidence in RUN_BASIS §5.
- **Snapshot-tied references.** "The current D-APP-38 snapshot records MATCH" is true of v23, while
  "_REFERENCES.md records MATCH" is literally true of the register but false as a fact. The tie-break
  handled this, but CLM-015 (ALIGNED, snapshot-named) and CLM-022 (STALE, register-named) differ only
  in wording. Proposal: say explicitly that citing a register verdict as current counts as restating it.
- **"Current path" rows.** DIRECTIVE §0 alone would make unamended DIRECTIVE §2.8 control over the
  Codex-only amendments. That shows why the brief's warning was needed. A named R4 question for
  "App DIRECTIVE unamended for D-GOV-43 (§2.3, §2.8, §2.10, §8)" would cluster STATE-1-type rows
  across packages better than plain R4.

## 6. Effort

- **Files:** about 35 read in full or by range.
  - Deliverable carriers: SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES`, `_DEPENDENCIES`,
    `Dependencies.csv`, MEMORY, INSP-03, two checklists in full, the others by grep.
  - App DIRECTIVE §0-§3 and §7-§8; CONTRACT, PRD and SPEC by grep.
  - D-GOV-43 packet (README and the surfaces-touched section); the D-APP-127 record.
  - About ten code and test files, by range.
- **Git:** `git log`, `show` and `blame -L` on `session-store.ts` 1111-1127 and
  `app-owned-composition.ts` 169, both on the touched list. No lines blame to the four post-release
  commits, so PostReleaseBasis is NO throughout.
- **Context budget:** moderate, not tight.
