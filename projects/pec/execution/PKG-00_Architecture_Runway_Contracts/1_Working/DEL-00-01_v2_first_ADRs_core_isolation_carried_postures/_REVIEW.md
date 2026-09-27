# Review — DEL-00-01 v2 first ADRs

**Review stage:** REVIEW COMPLETE FOR THE D-PEC-105 BYTES — ONE MAJOR FINDING OPEN (HumanDisposition TBD) — OWNER EXACT-BYTE ACCEPTANCE PENDING — GATE 5 NOT ENTERED

**Review Type:** SELF_CHECK

**Reviewer(s):** `REVIEW-SELF-DEL-00-01-20260927-RV1` — a fresh Type 2 TASK instance (`pec-task`) on the PEC loop's producer side, dispatched by the RV1 WORKING_ITEMS manager of `HELP-HUMAN-PEC-20260927-RV1-INTAKE`. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`); the role and the high reasoning effort are instruction-asserted.

**Independence:** SELF_CHECK is not independent review. In the bundled method it is "producer reviews own work"; here, as in the 2026-08-01 record, it is a producer-side mechanical `AGENT_CHECK` with no human reviewer. This reviewer authored none of the `D-PEC-105` bytes, none of the D-PEC-72 production bytes and none of the prior review records; this instance's own context began with this assignment. No human reviewer is inferred, and every finding below is `Origin=AGENT_CHECK`.

**Date:** 2026-09-27

**Lifecycle:** `CHECKING`, unchanged. No lifecycle transition is proposed, prompted or evaluated. Gate 5 is not entered.

**Target transition:** none. This review is the `D-PEC-105` RR1 REVIEW of the postimage bytes; it attempts no transition.

### Authority

The owner's direction of 2026-09-27, recorded in `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md` (SHA-256 `403a0497ae65c413f844b656daf6b3f5a58f99ffd65012dfd42b078430def346`), verbatim:

> Intake: CAND-01 b (each deliverable's production packet will absorb its own); CAND-02 promote; CAND-03 promote to Root; keep D-PEC-96 row.
> Proceed with RV-1.
> Take the approach you recommend for K3.
> Production itself will be done in a different session and production packets will be determined at that time, unless they become a dependency of something necessary.

The owner's freeze-point direction of the same day, verbatim (`D-PEC-107` §"Freeze point"):

> I don't want to proceed with the scope change right now.  I'm re-writing the App PRD and along with it the entire governance framework of Chirality.  I want to have this as a freeze point where important decision have been made and a large undertaking is complete.  This work you're proposing now is meant just to be put in the record so that it can be considered when everything undergoes a reassessment from the ground up.

Asked whether RV1 should be held as part of the freeze, the owner replied, verbatim: "Yes I still want you to complete the task management work and the RV1."

`D-PEC-107` §"RV1 authorization" implements `D-PEC-105` RR1 (`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-105_RULING_2026-09-27.md`, `401c2419ba26c8a43610d8416663e745a80d8061363d5abb73459dea931bd0ef`; owner direction verbatim: "D-PEC-105: A; P; RR1; confirm 4a 4b; M; defaults"; proposal `D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md`, `077610057791063e2308d932cf08a7ac44cd02793fe60925c744d969fd6ba89f`). The review type (`SELF_CHECK`) and the method basis are HELP_HUMAN's interpretation and choice, disclosed in that section; the owner's words are "Proceed with RV-1." The review type is the one the owner selected for this deliverable on 2026-08-01, verbatim: "I agree with your recommendation for the replacement ruling. Proceed accordingly." (the referenced recommendation was `SELF_CHECK`; see the history section below).

### Method basis and substitutions

The bundled `review` workflow as of commit `2f825f180`, read only with `git show 2f825f180:<path>`: `workflows/review/WORKFLOW.md` `f8a8f240a034395dd1d069799449215eca29ce14887a20653f1cec9a674906bc`; `workflows/review/execution.json` `d1c668ae85f9f5a0edf2ecb312a449e21aa9101f99da9997fc4a7805677074df`; `workflows/review/resources/contract.md` `d3d7eb27993068fbdf4ea3b06c78a19106ff4d145f149d5cf50040756144b328`; `workflows/review/resources/method.md` `63c8a3959cd6286f95acf30ae87e42a5dd99d951b2ae2ab3ec6212a81f930daa`. The working-tree `workflows/review/**` (the revised edition, `77dbfcb72` onward) was not read or applied; PEC has not adopted it.

Gate mapping (recorded as the brief requires):

| Old-method gate | This review |
|---|---|
| Gate 1 human input | `D-PEC-107` RV1 authorization (deliverable and review type) |
| Gate 2 checklist confirmation | The deterministic derivation; every `AC-*` copied verbatim in emitted order. No new owner confirmation of this checklist was given. The owner's 2026-08-01 confirmation ("The checklists are adequate and can be used but should remain open to revision.") concerned the prior derivation `bb815439…3b84`, whose criteria are byte-identical to this one apart from the source hash |
| Gate 3 findings | `Origin=AGENT_CHECK` agent checks only; no human reviewer exists or is inferred |
| Gate 4 dispositions | `HumanDisposition=TBD` for every new finding; each `ProposedDisposition` is a labelled PROPOSAL |
| Gate 5 | Not entered |

Substitutions and departures:

1. **Gate 1 step 4 (`audit-decomp` TASK).** This TASK cannot delegate. Substitute: the strict register validator plus a direct identity check of `_CONTEXT.md`, `ScopeOfWork.md`, `Deliverables.csv`, `ScopeLedger.csv` and `SOFTWARE_DECOMP.md` (`evidence/04_strict_registers.out`; `evidence/05_selfcheck_checks.out` §C1).
2. **Deliverable-local writes and snapshot.** The method has WORKING_ITEMS write `_REVIEW.md`, `Review_Findings.csv` and the snapshot. This TASK drafts them outside the repository; the manager wrote them and named the snapshot `REV_DEL-00-01_2026-09-27_1554`.
3. **Review-type rows.** The method defines no ID prefix for `SELF_CHECK` focus rows. They are recorded as review-local `SC-*` rows. They are not `CU-*` custom items; no `CU-*` item was supplied and none is active.
4. **Premise-ledger check.** An independent re-rendering of the `D-PEC-105` premise ledgers against the pre-act preimages was added (`evidence/05_selfcheck_checks.out`, first command). It is an extra mechanical check, not a method step.
5. **Deferral rule.** No CRITICAL or MAJOR finding is proposed or recorded as `DEFER`/`DEFERRED` (root `docs/SPEC.md` §3.4), although the `2f825f180` edition would allow it.
6. **Gate 4 step 5 / Gate 5 / pointer.** No snapshot-creation or pointer script is run by this TASK; Gate 5 is not entered.

## Review Basis

| Input | Identity (SHA-256) |
|---|---|
| `artifacts/v2/ADRs.md` (bytes under review; `D-PEC-105` postimage) | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` |
| `ScopeOfWork.md` (production contract; `D-PEC-105` add-on P postimage; `SOW_V1`) | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` |
| Derived checklist (`chirality-review-checklist/v1`, tool version 1, 7 criteria; re-derived twice, byte-identical to the manager's copy) | `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9` |
| Prior checklist, derived from the prior SOW `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` | `bb815439562b97e81c00bfdc3f07746af22e2fe1be958694f20c6696c7c13b84` (differs only in the source SHA-256, eight occurrences) |
| Prior ADR bytes (owner-accepted 2026-08-01; acceptance lapsed) | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |
| Prior `_REVIEW.md` / `Review_Findings.csv` (header only) | `c417418e96bfb8e230634049c7ee359fb84ad688a7946b5f819e21b2bc5d6968` / `3f1cec3bf34776b3cc7e9d0fdacd3dd268e6ddf9dfb4e51855d0d1efa40e25e0` |
| Prior snapshots `REV_DEL-00-01_2026-08-01_1935`, `…_2029`, `…_2109` | per-file hashes in `evidence/00_hash_checks.out` |
| 2026-08-01 ruling `_Coordination/D-PEC-72_P1_ENTRY_FOUNDATION_2026-08-01/ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md` | `9a53d09bb6754aed375acebe985ab924a3eeda6ed9f18f4261f00bd02ecd4bf8` |
| `_STATUS.md` / `_CONTEXT.md` / `Dependencies.csv` / `_DEPENDENCIES.md` / `_REFERENCES.md` / `MEMORY.md` | `41c871a5…ceea` / `f9647800…5701` / `a8573c64…4467` / `31ee4bc0…14f4` / `f38d9257…87eb` / `0596e9c6…fa76` |
| `D-PEC-105` act run root `_Coordination/D1_PREMISE_AMEND_2026-09-27/`: `HANDOFF_STATE.md` / `VALIDATION.md` / `premise/DEL-00-01_ADR.json` / `premise/DEL-00-01_SOW.json` | `a893885a…8c20` / `91ec7ea3…418c` / `f1b68b2e…8afa` / `238d8eaf…06fe` |
| Intake `_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md` | `e2ccf3e33b6636c46afe3fe68eff586f22141b405364bcb6b6eeefd63077818a` |
| Current basis: decomposition revision 1.6 at `189f205ff` — `SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` / `_LATEST.md` | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` / `768ae4c4…a771` (unchanged between `189f205ff` and the review HEAD) |
| `projects/pec/docs/PRD.md` v2.4 | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| Archived ADRs `projects/pec/docs/.archive/adr/ADR.md`; Root `docs/CONTRACT.md` | `14e0bdc4…88eb`; `510f6a84…3f71` |
| Reliance-hold preflight (run by the manager; cited, not rerun) `_Coordination/RV1_D1_REVIEW_2026-09-27/evidence/reliance_hold_preflight.out` | `bd27f9d2373e7d7108b343ce6a031739e375edd8543ebc24c0d999631277d0e2` — `ALLOW` ×8, `candidate-validation` being the matching review operation; register `f877d931…741cbc`, script `b1712e4b…d0e` |
| Instruction sources: Root `AGENTS.md` / `projects/pec/AGENTS.md` / `agents/AGENT_TASK.md` | `c8ce87ef…1dffd` / `df9196d1…5eb8` / `1a13a5b0…c8fb7` |
| Briefs `RV1_D1_REVIEW_2026-09-27/briefs/COMMON_REVIEW_TASK.md` / `RV1_SELF_CHECK_DEL-00-01.md` | `3b48557d…3cd6` / `4e41ac4c…9ea83` |

`evidence/…` names a file in this review's evidence set (commands, cwd, interpreter, exit codes and outputs), filed by the RV1 manager at `projects/pec/execution/_Coordination/RV1_D1_REVIEW_2026-09-27/evidence/DEL-00-01_SELF_CHECK/`. The immutable snapshot of this review is `projects/pec/execution/_Evaluation/Reviews/REV_DEL-00-01_2026-09-27_1554/`.

Review HEAD: `a1735cc3b` (branch `claude/pec-rv1-d1-review`), clean. Every hash was recomputed before assessment; none differed (`evidence/00_hash_checks.out`). The current bytes equal an independent rendering of the `D-PEC-105` ledgers over the pre-act preimages (ADR: 6 hunks; SOW: 3 hunks; `evidence/05_selfcheck_checks.out`).

## Gate 1 Precondition Summary

| Precondition | Result | Evidence |
|---|---|---|
| Deliverable folder | PASS | Folder, `_STATUS.md`, `_CONTEXT.md`, `ScopeOfWork.md` and `artifacts/v2/ADRs.md` present |
| Lifecycle state | `CHECKING` | Entered 2026-08-01 under the D-PEC-72 review-from-`INITIALIZED` override (`_STATUS.md` history); no transition is attempted here |
| Production format | PASS | `validate_scope_of_work.py`: `PASS format=SOW_V1` (`evidence/03_validate_scope_of_work.out`) |
| Context validity (substitute for `audit-decomp`) | PASS | Strict registers: 68 registers, 285 rows, 0 errors, 26 `XRG-013` warnings (D-GOV-48 OUT/TBD ledger rows without `PackageID`; none names DEL-00-01), exit 1, matching the recorded pre-act baseline; identity check 12/12 PASS |
| Anticipated artifact | PRESENT | `artifacts/v2/ADRs.md`, path set by the D-PEC-72 packet |
| Reliance-hold preflight | ALLOW | Manager's run, cited above |
| Review type | SELECTED | `SELF_CHECK`, per the 2026-08-01 owner replacement ruling carried by `D-PEC-107` |
| Gate 1 human confirmation | `D-PEC-107` | RV1 authorization; no separate prompt |

## Checklist

All results are mechanical `AGENT_CHECK` results against the current bytes.

### Artifact Presence

| ID | Artifact | Present | Notes |
|---|---|---|---|
| AP-001 | `artifacts/v2/ADRs.md` | Y | SHA-256 `ad6bab7e…c49e`, the `D-PEC-105` postimage |
| AP-002 | `ScopeOfWork.md` | Y | SHA-256 `3757632b…a647`, valid `SOW_V1` |

### Acceptance Criteria

Copied verbatim from checklist `6e99f93c…8cf9`, in emitted order. Source binding: qualified ID; `ScopeOfWork.md` SHA-256 `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647`; line.

| ID | Criterion | Verification | Source binding | Addressed |
|---|---|---|---|---|
| AC-001 | The published ADR set contains exactly one decision record that names a single selected v2 core isolation style and states in its own text that it resolves OI-012. | VER-001 | `DEL-00-01-AC-001`; `3757632b…a647`; L107 | Y — ADR-PEC-V2-001 (ADRs.md L22–26, L54–55) selects ports and adapters (hexagonal isolation) and states "Resolves: OI-012"; ADR-PEC-V2-002 records carried postures, not a core-isolation decision; functional-core/imperative-shell is kept only as an internal technique (L78–82) and is not selected as the isolation posture (L110–113) |
| AC-002 | That decision record's context section reproduces the recorded Gate 4 basis elements of CLM-006 and adds no invariant or service rule absent from the accepted PRD and decomposition. | VER-001 | `DEL-00-01-AC-002`; `3757632b…a647`; L108 | PARTIAL — the Context section (L30–50) reproduces the forced-properties element, the package grain and the PKG-01 seam, and adds no invariant or service rule absent from PRD v2.4 and revision 1.6; it does not reproduce the element "nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply" (absent from the whole ADR), and the lighter functional-core element appears only under "Alternatives considered" (L110–113). RF-001 |
| AC-003 | The ADR set re-cites ADR-002 as the sole live carried posture, cites ADR-014 as historical lineage only, carries the accepted v2 runtime/client and human-only-act boundary without the retired PEC-project-adapter allocation, and asserts no other archived ADR as live authority. | VER-002 | `DEL-00-01-AC-003`; `3757632b…a647`; L109 | Y — carried postures 1–3 (L144–163) and "Consequences and boundary" (L169–174); ADR-002 and ADR-014 resolve to archived headings (`ADR.md` L16, L201); posture 3 now carries the `D-GOV-43` A2 boundary matching CLM-005/REQ-004 (XD-002). REQ-005's literal path is noted at RF-005 |
| AC-004 | The ADR set names itself in its own text as the resolution of OI-012, and that self-identification is consistent with the disposition the open-issue register already carries for OI-012 — "Decided in DEL-00-01's ADR; owner review at that ADR" — requiring no change to it. The set decides none of OI-001 through OI-009 or OI-013 and claims no register-side effect; any register-side update is an out-of-scope downstream act (SCOPE_CHANGE or coordination upkeep), not a completion condition of this deliverable. | VER-001; VER-003 | `DEL-00-01-AC-004`; `3757632b…a647`; L110 | Y — "Resolves: OI-012" (L26); the disposition is unchanged at `SOFTWARE_DECOMP.md` L673 (revision 1.6); "Non-decisions" (L118–124) and Decision 3 (L73–74) decide none of OI-001..009 or OI-013; no register-side effect is claimed |
| AC-005 | The ADR set states the entity-schema versus store-persistence seam inside PKG-01 explicitly enough that a reader can classify a candidate PKG-01 change as core or adapter. | VER-001 | `DEL-00-01-AC-005`; `3757632b…a647`; L111 | Y — Decision 6 (L83–88) gives the classification rule (domain meaning is core; storage or retrieval of the same meaning is adapter) |
| AC-006 | The v2 docs-tree path is recorded in the deliverable packet, the ADR markdown entries exist at that path, and the run produced no write outside `PKG-00`. | VER-004 | `DEL-00-01-AC-006`; `3757632b…a647`; L112 | Y — the path is recorded in `D-PEC-72_p1_entry_foundation_slice.md` L111 and `_run_records/D-PEC-72_PKG-00_ACTIVATION.md` L33; the file exists; production commit `5942c5033` wrote only PKG-00 files; the `D-PEC-105` act commit `7c250e370` wrote four PKG-00 product files plus two evidence files in its run root under `_Coordination/**` (coordination records, not a write into another package) |
| AC-007 | An accountable owner confirms the selected core isolation style at the ADR, consistent with the OI-012 disposition "owner review at that ADR", and confirms that nothing in the set makes a governed act depend on PEC-held state. | HUMAN_REVIEW: accountable owner review at the DEL-00-01 ADR, per the OI-012 disposition recorded in SOFTWARE_DECOMP.md | `DEL-00-01-AC-007`; `3757632b…a647`; L113 | UNSATISFIED for these bytes — READY FOR OWNER DECISION (see "Acceptance status") |

### Objective Coverage

| ID | Objective | Addressed | Document §Section |
|---|---|---|---|
| OC-001 | `OBJ-005`: Everything PEC holds can be deleted at any moment without blocking any governed act | Y | ADRs.md Context (L32–38: graceful absence, rebuildable record tier, `PEC-K-01`/`PEC-K-02`); Decision 6 (persistence behind a core-owned port); carried posture 1 (zero third-party dependencies); posture 3 (PEC an optional client, no second execution loop, human-only acts unavailable to agents); posture 4 (runtime ownership never transfers into PEC). No text in the amended set makes a governed act depend on PEC-held state; the six hunks only re-name the runtime owner outside PEC and the remaining bridge |

### Production-Contract Consistency

| ID | Check | Result | Notes |
|---|---|---|---|
| XD-001 | Every `OUT-*`, `AC-*` and `VER-*` closes through the output/evaluation matrix | PASS | 5 rows; OUT-001..002, REQ-001..010 and VER-001..004 all appear; each of AC-001..007 exactly once; AC-007 bound to `HUMAN_REVIEW` (`evidence/05_selfcheck_checks.out` §C2) |
| XD-002 | CLM-005 and REQ-004 (add-on P hunks) against ADR carried posture 3 (ADR hunk P05) | PASS | Same elements in all three: application-owned Runtime service owns sessions, delegation, tools, turn locks and interruption per App instance; credentials custodied by Codex; local-model residency retired; `D-GOV-43` A2; optional client; no second loop; human-only acts. REQ-004 reaches K-RUNTIME-1 through CLM-005 (act verifier note 2). Matches Root `docs/CONTRACT.md` K-RUNTIME-1 and K-RESIDENCY-1 (retired) and PRD v2.4 §4.2/§15. No "Root owns" premise remains outside AX-008's provenance account (SOW L142) and posture 2's history of ADR-014 (ADR L150–151, true of the archived text) |
| XD-003 | The six ADR hunks and three SOW hunks left the ADR and its contract consistent; nothing outside the hunks changed | PASS | Independent ledger rendering equals the current bytes; the ADR decision, consequences' substance, non-decisions and the D-PEC-72 selection are unchanged; P02/P03/P06 agree with PRD v2.4 §8, PEC-STR-003 and §13 (T-RT deferral); the retained PRD v2.2 Sources line and "PEC is an optional client" follow owner-confirmed reading 4(b) |
| XD-004 | ADR citations resolve at the current basis | PASS | `PEC-K-01/02/03/07/08/10/11`, `PEC-SVC-001`, `PEC-STR-002`, `PEC-API-003` exist in PRD v2.4; `SOW-001/002/034/042/052/055/056/087` exist in the revision-1.6 ledger with the cited meaning (SOW-087 OUT, deferred) |
| XD-005 | CLM-007 against the dependency registers | PASS | `Dependencies.csv` holds only DEP-00-01-001/002 (ANCHOR); DEP-00-02-003 (`E-N18`, `LOW_CONFIDENCE`) and DEP-01-01-003 (`E-P01`) are ACTIVE EXECUTION rows in the consumers' registers, `Origin=EXTRACTED`, marked PROPOSAL, not DECLARED |
| XD-006 | SOW state and currency statements against current governed state | FAIL | Authoring-time lifecycle wording (RF-002) and SCA-004-era currency wording (RF-003) are false at the current bytes; AX-002's present-tense basis wording is owner-confirmed as the birth basis (RF-004). AX-008 discloses all three as left unchanged |
| XD-007 | REQ-005 against the ADR's citation form | PARTIAL | The ADR does not cite the literal path `projects/pec/docs/.archive/adr/ADR.md` (RF-005); AC-003 and VER-002 are unaffected |

### Dependency Satisfaction

| ID | Dependency | Target | Satisfaction | Notes |
|---|---|---|---|---|
| DS-001 | No ACTIVE upstream `EXECUTION` row in `Dependencies.csv` | N/A | SATISFIED | Root node. DEP-00-01-001 (PKG-00 tree anchor) and DEP-00-01-002 (SOW-088 trace) are ACTIVE `ANCHOR` rows, `SATISFIED`. The two downstream EXECUTION edges into DEL-00-01 (DEP-00-02-003, DEP-01-01-003; `PENDING`) sit in the consumers' registers and do not gate this deliverable |

### TBD Inventory

| ID | Check | Result | Notes |
|---|---|---|---|
| TB-001 | Remaining TBDs assessed | 2 registered TBDs remaining; 0 unregistered TBD items | TBD-001 (docs-tree path) is set in fact by the D-PEC-72 packet (`artifacts/v2/ADRs.md`); the contract keeps it as deferred to the packet, consistent with REQ-008. TBD-002 (`ResponsibleParty`) remains TBD and is not inferred. The other TBD tokens (CLM-001's `ResponsibleParty` value; REQ-008, AX-005 and the matrix citing registered IDs) are not separate items. ADRs.md has none. Unchanged from the prior record; acceptable for this review stage |

### Review-Type-Specific (SELF_CHECK focus)

| ID | Check | Result | Notes |
|---|---|---|---|
| SC-001 | Completeness: every checklist row assessed against the current bytes | PASS | AP 2, AC 7, OC 1, XD 7, DS 1, TB 1 |
| SC-002 | Internal consistency of ADR and contract | FINDINGS | RF-001 (AC-002), RF-002, RF-003, RF-005; RF-004 observation |
| SC-003 | TBD reduction | NO CHANGE | 2 registered TBDs before and after the `D-PEC-105` act |

## Findings (Gate 3/4)

Recorded in `Review_Findings.csv` as RF-001..RF-005, each `Origin=AGENT_CHECK`, `HumanDisposition=TBD`, `Status=OPEN`, `ReviewerID=REVIEW-SELF-DEL-00-01-20260927-RV1`. Each `ProposedDisposition` is a PROPOSAL. Corrections are recorded only, not prepared (freeze point).

| ID | Severity | Finding | Correction it calls for (recorded only) |
|---|---|---|---|
| RF-001 | MAJOR | AC-002 is only partly met. CLM-006 (SOW L82) records five Gate 4 basis elements. The ADR-PEC-V2-001 Context section (L30–50) reproduces three. The element "nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply" appears nowhere in the ADR (no "§16", "adapter-level" or "open cheaply" text). The element "the lighter functional-core/imperative-shell variant fits a deterministic-derivation service with less ceremony" appears only under "Alternatives considered" (L110–113), outside the context section the criterion names. The gap dates from the first production bytes (`5942c5033`) and is untouched by the `D-PEC-105` hunks. The D-PEC-72 candidate validation (`_run_records/D-PEC-72_CANDIDATE_VALIDATION.md` L33) states that the Context "carries … adapter-level open-decision posture, functional-core alternative", which the bytes do not bear out, and the 2026-08-01 SELF_CHECK recorded AC-002 as Y. Severity follows the brief's scale (a criterion the bytes fail is MAJOR); a reading that treats the context's summary and its citation of CLM-006 as reproduction would make this MINOR, and that call is the owner's | The Context section of ADR-PEC-V2-001 would have to state the two missing CLM-006 elements. That is an artifact byte change, which needs an owner-ruled correction packet, then a fresh checklist derivation and REVIEW, before re-acceptance. PROPOSAL: `REVISE` |
| RF-002 | MINOR | Proposal "Other findings" 1 (intake CAND-01 item 8). Contract text describes the pre-D-PEC-72 state as current: the Epistemology opening (L92–94, "No ADR exists for this deliverable at the time of writing; `_STATUS.md` records state `INITIALIZED`"), AX-006 (L140, "the deliverable is at `INITIALIZED` and no ADR has been authored") and CON-001 (L83, OI-012 "**undecided** at the time of this contract"; no selection may be inferred). The Praxeology opening (L117, "the future authoring run") is authoring-time wording of the same kind. `_STATUS.md` reads `CHECKING`, the ADR exists, and D-PEC-72 O-B decided OI-012. AX-008 (L142) discloses the wording as left unchanged. No AC result depends on it | The Epistemology opening, AX-006 and CON-001 (and the Praxeology opening) would have to be brought to the current state. That is a `ScopeOfWork.md` change needing an owner-ruled correction packet before re-acceptance. PROPOSAL: `REVISE` |
| RF-003 | MINOR | Proposal "Other findings" 8 (intake item 8). The objective warrant (L31–32, "it remains unchanged in revision 1.3, the current successor basis") and the basis provenance note (L58–63: `_REFERENCES.md` "now names … revision 1.3 as the accepted `current_basis`"; `_CONTEXT.md` "retains the revision-1.1 to revision-1.2 supersession trace, while SCA-003 establishes revision 1.3 as the current successor") have been false since SCA-004. `_REFERENCES.md` L3 now names revision 1.6, and `_CONTEXT.md` provenance runs to revision 1.6. AX-008 discloses this | Both passages would have to be restated as history or brought current, keeping the owner-confirmed revision-1.3 birth basis. That is a `ScopeOfWork.md` change needing an owner-ruled correction packet. PROPOSAL: `REVISE` |
| RF-004 | OBSERVATION | Proposal "Other findings" 7 (intake item 8). AX-002 (L136) says in the present tense "The accepted basis is `SOFTWARE_DECOMP.md` revision 1.3 at merge `11a494e9a`", while the current basis is revision 1.6. The owner confirmed reading 4(b) under `D-PEC-105` ("confirm 4a 4b"). The ruling's resolution table (HELP_HUMAN's interpretation) records that reading as including "The DEL-00-01 contract keeps its revision-1.3 birth basis", and AX-008 labels AX-002 as the birth basis. The content is therefore ruled; only the wording is ambiguous. The DEL-01-05 AX-006 and DEL-10-01 AX-005 parts of that item belong to other deliverables and are out of scope here | None required. Any rewording of "is" as the birth basis could travel with RF-003's correction. PROPOSAL: `ACCEPT_AS_IS` |
| RF-005 | MINOR | Proposal "Other findings" 10. REQ-005 (L100) says the ADR set "shall cite `projects/pec/docs/.archive/adr/ADR.md` as historical baseline only". The ADR cites "archived ADR-002 and ADR-014 (historical corpus)" (L131) and "the archived ADR set" (L144) but never the path (no `docs/.archive` or `ADR.md` text). AC-003 and VER-002 still pass, because both citations resolve to locatable headings in the only archived ADR file (`ADR.md` L16, L201). Pre-existing; the `D-PEC-105` hunks did not touch it | The ADR's Sources line would have to cite the archive path (an artifact change needing an owner-ruled correction packet before re-acceptance), or the owner accepts the ID citation as meeting REQ-005. PROPOSAL: `REVISE` |

Items judged out of scope for findings against these bytes:

- **Proposal "Other findings" 9** (`projects/pec/AGENTS.md` L175, "The client seam carries as a concept"). This is an instruction surface, not a DEL-00-01 byte. The ADR's posture 4 already states the T-RT deferral that PRD v2.4 §13 records. Correcting AGENTS.md needs its own instruction tranche.
- **Proposal "Other findings" 11** (PRD v2.4 §13, L496, "live postures (ADR-002, ADR-014) re-cited in v2's first ADRs"). This is PRD wording. The ADR follows its contract and the accepted decomposition (SOW-088; `D-PEC-67` L-A2; SCA-003), which govern downstream, and the SOW's objective warrant records the supersession (L53–56). Its home is the promoted CAND-02 row, a consideration for the reassessment.
- **Intake CAND-01 item 8's DEL-00-03 entries** ("Other findings" 4, 5 and 6) belong to the DEL-00-03 review. **Item 6's DEL-01-05 and DEL-01-01 entries** belong to those deliverables' own packets. Noted for the owner's act: DEL-01-05 TBD-005 (L90) rests on "accepted `ADR-PEC-V2-001`", which describes these bytes only after the owner's re-acceptance, and DEL-01-01 CLM-009 (L103) anchors the prior ADR and SOW hashes.
- **Act verifier note 4** (the ADR's premise-amendment note names SCA-005 and SCA-006, although every ADR hunk has an SCA-005 cause). Not a finding: the note is a true statement about the class of premises, to which SCA-006 contributed none.

## Findings Summary

| Severity | Total | Resolved | Open | Deferred |
|---|---|---|---|---|
| CRITICAL | 0 | 0 | 0 | 0 |
| MAJOR | 1 | 0 | 1 | 0 |
| MINOR | 3 | 0 | 3 | 0 |
| OBSERVATION | 1 | 0 | 1 | 0 |

There is no CRITICAL finding. There is one MAJOR finding, RF-001, open with `HumanDisposition=TBD`; it is not deferred and may not be deferred. The prior 2026-08-01 register was header-only; RF-001..RF-005 are new at this review.

## Acceptance status and next step

The owner's `ACCEPT_EXACT_BYTES` of the new hashes (ADR `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e`, SOW `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647`) has **not** been given. The prior acceptance lapsed when the `D-PEC-105` act landed: the AC-007 acceptance was bound to ADR `f63ecc27…5db5` (proposal "Acceptance-lapse account"), and with add-on P this record's prior SOW basis `43346150…1740` also describes superseded bytes. **AC-007 is unsatisfied for these bytes until the owner's act, which is the next step.**

AC-007: **READY FOR OWNER DECISION.** The owner would confirm, at the ADR:
1. that ports and adapters (hexagonal isolation) is PEC v2's selected core-isolation style. It is still stated at ADR-PEC-V2-001 Decision (L54–55); the `D-PEC-105` hunks left the decision, its alternatives and its non-decisions unchanged.
2. that nothing in the set makes a governed act depend on PEC-held state. The amended bytes still support this: the hunks move runtime ownership to the application-owned Runtime service (outside PEC), name the hooks CLI as the one remaining bridge and defer the runtime-client seam. PEC stays an optional client with no second loop (OC-001).

The owner decides with RF-001 (MAJOR) open and `TBD`. If the owner rules RF-001 `REVISE`, the correction changes the ADR bytes. Acceptance is hash-bound, so the corrected bytes would need their own owner-ruled packet, fresh derivation and REVIEW before an exact-byte acceptance. This review claims no acceptance, readiness, release or reliance.

## Freeze-point limit

Under `D-PEC-107` §"Freeze point", every correction a finding calls for is recorded above and not prepared. No replacement text is drafted. Any `ScopeOfWork.md` or artifact change needs an owner-ruled correction packet before re-acceptance. This review writes no `ScopeOfWork.md`, artifact, `_STATUS.md`, register, context or reference file.

## Revised-edition consequence (recorded once; no prompt)

The revised `review` edition, which PEC has not adopted, would surface a deliverable that entered `CHECKING` under an earlier override without a recorded frozen SHA or checking basis. It would ask for a human ruling that records them, or for reversal. DEL-00-01 entered `CHECKING` on 2026-08-01 under the D-PEC-72 override. This is recorded as a consequence for the owner's reserved decision under that edition, if PEC ever adopts it. Nothing here prompts about `CHECKING`.

## Transition Readiness

**Transition readiness:** no transition attempted; Gate 5 not entered. `DEL-00-01` remains `CHECKING`.

## History — prior review record (describes superseded bytes)

The prior `_REVIEW.md` (SHA-256 `c417418e96bfb8e230634049c7ee359fb84ad688a7946b5f819e21b2bc5d6968`) follows; its AC-007 acceptance of ADR `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` lapsed under `D-PEC-105` when the act landed, and its review basis describes the superseded ADR and SOW bytes.

Disclosure: the body below is the prior file verbatim except that each of its 13 heading lines is demoted by one `#`; no other byte, and no quoted owner ruling, is altered.

## Review — DEL-00-01 v2 first ADRs

**Review stage:** ARTIFACT FITNESS OWNER ACCEPTED — CHECKING

**Review Type:** SELF_CHECK

**Reviewer(s):** AGENT_CHECK (producer-side mechanical self-check; no human reviewer identity inferred)

**Target transition:** INITIALIZED → CHECKING (owner-approved review-from-INITIALIZED override; applied)

**Owner authorization (verbatim, 2026-08-01):**

> First merge your work through PR. Then I approve D-PEC-72 review: PEER_REVIEW for DEL-00-01 and DEL-00-03; authorize review from INITIALIZED.

**Owner amendment (verbatim, 2026-08-01):**

> I'm sorry I don't have a peer reviewer I made that judgment in error.
>
> The checklists are adequate and can be used but should remain open to revision.

The amendment withdraws `PEER_REVIEW` before any practitioner was named or any
finding was captured. It confirms this common checklist as adequate. Revision
remains open through additive `CU-*` items; the deterministically compiled
`AC-*` sequence and text remain contract-bound and are not edited or removed.

**Owner replacement ruling (verbatim, 2026-08-01):**

> I agree with your recommendation for the replacement ruling. Proceed accordingly.

The referenced recommendation was `SELF_CHECK`. This opens mechanical
producer-side assessment only; it does not convert agent checks into human
engineering judgment, artifact acceptance, finding disposition, or lifecycle
authority.

**Owner Gate 5 ruling (verbatim, 2026-08-01):**

> Approve both recommendations as stated.

The approved recommendation for this deliverable was: `DEL-00-01 Gate 5:
advance to CHECKING.` The guarded transition was applied with the committed
ruling record. This approval advances lifecycle state only; it does not accept
the ADR artifact bytes or satisfy AC-007's owner-only fitness confirmation.

**Owner finalization authorization (verbatim, 2026-08-01):**

> D-PEC-72 artifact-status normalization — authorize WORKING_ITEMS
> to revise only present-tense candidate/pending-acceptance status
> prose in DEL-00-01 artifacts/v2/ADRs.md and DEL-00-03
> artifacts/v2/SPEC.md into acceptance-neutral authority prose.
> Do not change architecture, requirements, identifiers, citations,
> objective attribution, scope, open decisions, or lifecycle state.
> Rerun REVIEW against the resulting hashes. No artifact acceptance
> is inferred.

The authorized normalization is present at producer commit
`87272dde8a82dbef034968b14af4461fe4b056d4`. This SELF_CHECK rerun binds the
final ADR hash below. The normalized prose is acceptance-neutral and changes
no architecture or contract criterion.

**Owner artifact-fitness ruling (verbatim, 2026-08-01):**

> DEL-00-01 AC-007 — ACCEPT.
>
> I accept artifacts/v2/ADRs.md at SHA-256
> f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5
> as fit for DEL-00-01. I confirm ports-and-adapters / hexagonal
> isolation as PEC v2’s selected core-isolation style and confirm
> that no governed act depends on PEC-held state.
>
> This accepts these artifact bytes only. It does not advance
> DEL-00-01 to ISSUED, close C-05, authorize P1, or impose this
> architecture on another loop.

This ruling is recorded at committed authority
`ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md` at
`7f5acbf5`. It accepts only the exact review-basis artifact hash and changes no
lifecycle state.

### Review Basis

- D-PEC-72 production merged through PR #450 at `0f7f7ef108e65b953d188bd01fb116858959830f`.
- Selected artifact: `artifacts/v2/ADRs.md` (`sha256:f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`).
- Production contract: `ScopeOfWork.md`, valid `SOW_V1` (`sha256:4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740`).
- Checklist compiler: `tools/scope_of_work/derive_review_checklist.py`, schema `chirality-review-checklist/v1`, tool version 1, 7 criteria.
- Decomposition coverage: strict deterministic register validation PASS (64 registers, 254 rows, zero errors/warnings). No managed AUDIT_DECOMP child session was available in this runtime; no structural discrepancy was detected by the registered validator.
- Lifecycle state: `CHECKING`; the owner explicitly authorized review and Gate 5 advancement from `INITIALIZED`, and the guarded override is recorded in `_STATUS.md`.
- Context validity: PASS — `DEL-00-01`, `PKG-00`, `SOW-088`, and `OBJ-005` agree across `_CONTEXT.md`, `ScopeOfWork.md`, and accepted decomposition registers.

### Gate 1 Precondition Summary

| Precondition | Result | Evidence |
|---|---|---|
| Deliverable folder | PASS | Folder and governed context/status files exist |
| Lifecycle entry | PASS BY OWNER OVERRIDE | `INITIALIZED`; verbatim authorization above |
| Production format | PASS | `SOW_V1`, zero validation issues |
| Anticipated artifact | PRESENT | Final normalized `artifacts/v2/ADRs.md` at the review-basis hash |
| Dependency posture | PASS | No active `EXECUTION` upstream rows; two satisfied `ANCHOR` rows |
| Review type | SELECTED | `SELF_CHECK`, by owner replacement ruling |
| Reviewer identity | AGENT_CHECK | Mechanical producer-side assessment only; no human reviewer is inferred |

### Checklist

The owner confirmed this checklist as adequate and selected `SELF_CHECK`.
Assessment results below are mechanical `AGENT_CHECK` results. Additive `CU-*`
revisions remain allowed; the compiled `AC-*` rows remain unchanged.

#### Artifact Presence

| ID | Artifact | Present | Notes |
|---|---|---|---|
| AP-001 | `artifacts/v2/ADRs.md` | Y | Packet-recorded ADR candidate; final normalized artifact hash matches the review basis |

#### Acceptance Criteria

| ID | Criterion | Verification | Source binding | Addressed |
|---|---|---|---|---|
| AC-001 | The published ADR set contains exactly one decision record that names a single selected v2 core isolation style and states in its own text that it resolves OI-012. | VER-001 | `DEL-00-01-AC-001`; ScopeOfWork line 107; SHA above | Y — ADR-PEC-V2-001 selects hexagonal isolation and names OI-012 |
| AC-002 | That decision record's context section reproduces the recorded Gate 4 basis elements of CLM-006 and adds no invariant or service rule absent from the accepted PRD and decomposition. | VER-001 | `DEL-00-01-AC-002`; ScopeOfWork line 108; SHA above | Y — AGENT_CHECK corroborates the producer mapping |
| AC-003 | The ADR set re-cites ADR-002 as the sole live carried posture, cites ADR-014 as historical lineage only, carries the accepted v2 runtime/client and human-only-act boundary without the retired PEC-project-adapter allocation, and asserts no other archived ADR as live authority. | VER-002 | `DEL-00-01-AC-003`; ScopeOfWork line 109; SHA above | Y — explicit in ADR-PEC-V2-002 |
| AC-004 | The ADR set names itself in its own text as the resolution of OI-012, and that self-identification is consistent with the disposition the open-issue register already carries for OI-012 — "Decided in DEL-00-01's ADR; owner review at that ADR" — requiring no change to it. The set decides none of OI-001 through OI-009 or OI-013 and claims no register-side effect; any register-side update is an out-of-scope downstream act (SCOPE_CHANGE or coordination upkeep), not a completion condition of this deliverable. | VER-001; VER-003 | `DEL-00-01-AC-004`; ScopeOfWork line 110; SHA above | Y — Non-decisions section preserves every named issue and register boundary |
| AC-005 | The ADR set states the entity-schema versus store-persistence seam inside PKG-01 explicitly enough that a reader can classify a candidate PKG-01 change as core or adapter. | VER-001 | `DEL-00-01-AC-005`; ScopeOfWork line 111; SHA above | Y — Decision item 6 supplies the classification rule |
| AC-006 | The v2 docs-tree path is recorded in the deliverable packet, the ADR markdown entries exist at that path, and the run produced no write outside `PKG-00`. | VER-004 | `DEL-00-01-AC-006`; ScopeOfWork line 112; SHA above | Y — path exists; production commit `5942c5033` is PKG-00-contained |
| AC-007 | An accountable owner confirms the selected core isolation style at the ADR, consistent with the OI-012 disposition "owner review at that ADR", and confirms that nothing in the set makes a governed act depend on PEC-held state. | HUMAN_REVIEW | `DEL-00-01-AC-007`; ScopeOfWork line 113; SHA above | Y — owner ACCEPTS final hash `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`, confirms hexagonal isolation, and confirms graceful absence |

#### Objective Coverage

| ID | Objective | Addressed | Document section |
|---|---|---|---|
| OC-001 | `OBJ-005`: everything PEC holds can be deleted without blocking a governed act | Y | ADR context, carried posture, non-decisions, and acceptance boundary |

#### Production-Contract Consistency

| ID | Check | Result | Notes |
|---|---|---|---|
| XD-001 | `OUT-001` and `OUT-002` close through their registered `AC-*` and `VER-*` mappings without adding scope | PASS | Seven compiled criteria present in order; candidate-validation mapping corroborated |

#### Dependency Satisfaction

| ID | Dependency | Target | Satisfaction | Notes |
|---|---|---|---|---|
| DS-001 | No active `EXECUTION` upstream dependency | N/A | SATISFIED | Root-node posture; two declared anchors are satisfied |

#### TBD Inventory

| ID | Check | Result | Notes |
|---|---|---|---|
| TB-001 | Remaining TBDs assessed | PASS FOR CHECKING | Packet resolves the artifact path; assignment remains explicitly TBD and is not inferred |

#### SELF_CHECK Focus

Completeness, internal consistency, the carried TBDs, and the authorized
status-prose delta were checked against the final artifact hash. No custom
`CU-*` row is active.

### Findings Summary

`Review_Findings.csv` remains header-only. The final-hash mechanical
SELF_CHECK found zero CRITICAL, MAJOR, MINOR, or OBSERVATION findings. The
status-prose normalization is acceptance-neutral and introduced no checklist
regression. AC-007 is satisfied by the exact owner artifact-fitness ruling; it
is not an agent disposition.

### Transition Readiness

**Recommendation:** NO FURTHER LIFECYCLE ACT AUTHORIZED

All common checklist items remain populated against the final artifact hash,
there are zero findings, and the authorized normalization introduced no
substantive change. The owner separately accepted the exact final ADR hash and
satisfied AC-007. `DEL-00-01` remains `CHECKING`; no `ISSUED` transition,
C-05 closure, or P1 authority is created.
