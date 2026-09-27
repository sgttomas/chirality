# D-PEC-105 — D1 derivative premise amendment: DEL-00-01 ADRs and DEL-00-03 SPEC (with the DEL-00-03 Scope of Work) — proposal

Status: **DRAFT PROPOSAL / AWAITING_RULING**. **The number D-PEC-105 is provisional.** At `origin/main` `6c6cc1b00` the decision register's last row is `D-PEC-103`; `D-PEC-102` is reserved for the S4 packet and the work graph names `D-PEC-104` as the S1 packet's provisional number. No row reserves `D-PEC-105`. Rechecked at `origin/main` `78e74f590` (after `git fetch`): `D-PEC-102` has since been ruled (A + M) and published, and still no row reserves `D-PEC-104` or `D-PEC-105`; between the two commits `projects/pec` changed only in `docs/STATUS.md`, the work graph, `_REGISTER.md`, the `D-PEC-102` ruling and published proposal, and two review transcriptions, so no pinned file or target preimage moved. Rechecked again at `origin/main` `f0a6159c9` (PR #998, the `D-PEC-102` act, which replaced the eight S4 contracts outside PKG-00): all 18 pinned files and all four preimages hash as tabled. The number becomes final when HELP_HUMAN publishes this packet in `_DECISIONS/` with its register row.

Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1) for the PEC loop, 2026-09-26 (session date). Brief: `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/D1P_PREMISE_PROPOSAL.md` (SHA-256 `d1cdf4e3104d38a08e8bef8c3641070d942ec9ad2744bddeb9cadfb482cbc1f1`), with the shared `COMMON.md` supplied beside it in the session scratchpad (`51b70e46f1049696c456be1d4ab7b4b236e3cbfc6fa3a667ed0426035510b311`; not a repository file). No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every check ran on `git archive` exports. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md`.

The act it asks for is bounded: **replace three accepted files with the exact bytes tabled below** — DEL-00-03 `artifacts/v2/SPEC.md`, DEL-00-03 `ScopeOfWork.md` and DEL-00-01 `artifacts/v2/ADRs.md` — in one run of a bound act script, as **premise-only amendments**: every byte outside the listed hunks is the owner-accepted preimage, and each hunk is a premise correction, its minimal consequence, the uniform amendment note or a provenance `AX` (one consequence also corrects text stale since SCA-004; it is labelled where it occurs and put to the owner in question 4(a)). **One reading goes beyond premise-only scope and is put to the owner as such (question 4(a)):** rebinding the DEL-00-03 contract to revision 1.6 and PRD v2.4 changes OUT-002, REQ-001, REQ-002, REQ-003, AC-003 and the production sequence, re-resolves AC-002, AC-004, VER-002 and VER-004 against the rebound basis, and so changes the basis and requirement source they resolve against, which is more than SCA-006 §B4's "CLM-004 L70, CLM-006 L77 … premise only" for that contract. No lifecycle change. Add-on P (a fourth file, the DEL-00-01 `ScopeOfWork.md`) and add-on M are separate questions.

## Provenance

- **Owner acts relied on.**
  - **Steering.** The owner's 2026-09-25 direction, recorded in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md`: "You can continue with all the open work you identified." The work graph (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`, `1ec5719fe36541346584f116894a07548a35e18c78568765f1b6f949e0151ad8` at `6c6cc1b00`) makes it node D1 (row text, composed here from two table cells: "D1 Derivative premise review" | "DEL-00-01 ADRs, DEL-00-03 SPEC (WORKING_ITEMS with owning workflows)"; gate cell: "Packet binding exact bytes (outside default surfaces); after R3 for K-03 text"); READY, R3 met.
  - **SCA-005 checkpoint 2** (`D-PEC-92`) accepted `_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md` (`50cd0b1d…1350`). Its §B5 table: DEL-00-01 `ADRs.md` — "runtime-ownership premise (D-GOV-20 → D-GOV-43 A2, ADR carried posture 3); daemon (2) and cmux (1, L54/L84) mentions"; DEL-00-03 `SPEC.md` — "§4 information model, §6 PKG-07 row, §8 open decisions; daemon (1) and cmux (1, L128)"; action for both: "amend stale premises only; accepted bytes remain history". Its §B4 classes both contracts `STALE_REVIEW_REQUIRED` (DEL-00-01: "C13/D-GOV-43 runtime-ownership premise (ADR carried posture 3)"; DEL-00-03: "quotations of §1.4/§4 charter; SPEC §4/§6/§8"). SCA-005 amendment 1 deferred cmux out of scope (owner 2026-09-24, "no plans for cmux compatibility").
  - **SCA-006 checkpoint 2** (`D-PEC-97`) accepted `_ScopeChange/SCA-006_2026-09-25_1912/Propagation_Plan.md` (`f95d00d1…d7d8`). Its §B5 adds, for `SPEC.md` (`cc9f4754…1bae`), "the K-03 row L46 …, the requirement counts L23 and L62 (46 → 49), the API row L73 (response budgets and the tool-call surface) and the release-proof list L78 (the reliance-advertisement gate)"; "Accepted bytes remain history"; `ADRs.md` stays `CURRENT` for SCA-006's own causes. Its §B4 row for DEL-00-03: "CLM-004 L70, CLM-006 L77: the '46 requirements' premise (49 after SCA-006); review level, premise only"; "DEL-00-03 is CHECKING: its SOW and SPEC change only through its owning workflow and exact-byte gate (B5); nothing here moves its lifecycle."
  - **SCA-006 checkpoint 3** (accepted 2026-09-26; `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`) made decomposition revision 1.6 `current_basis` with PRD v2.4.
  - **`D-PEC-90`** (R-A, 2026-09-25): operational reliance on PEC data; its proposal pinned the SPEC at `cc9f4754…1bae` and listed the L46 K-03 row for re-quotation. Grant item 1 (no rebuild around verify-before-rely) is followed.
  - **`D-PEC-95`** and **`D-PEC-101`** (ruled; acts `fdc7a2071` and `62230fa46`): re-pinned every `_CONTEXT.md` and `_REFERENCES.md`, including both deliverables', to revisions 1.5 and 1.6.
  - **`D-PEC-99`** (ruled A): no `## Remaining` surface. Its exhibit (`EXHIBIT_MOVED_ITEMS.md`, `69b646f8…f45e`) names **no Part B item for node D1** (Part B nodes: S1, S2, S4 only).
  - **Owner acceptances of the current bytes** (they lapse under ruling A; see "Acceptance-lapse account"): the DEL-00-01 AC-007 artifact-fitness ruling of 2026-08-01 (ADR `f63ecc27…5db5`) and the DEL-00-03 `ACCEPT_EXACT_BYTES` of 2026-08-09 (SOW `3e4f0efc…5741`, SPEC `cc9f4754…1bae`).
  - **Precedents.** `D-PEC-90` (pinned the SPEC); the 2026-08-09 SPEC currency repair and re-acceptance (TM-PEC-014: handoff `_TaskManagement/HANDOFF_TM-PEC-014_DEL-00-03_SPEC_CURRENCY.md`, return `TM-PEC-014_SPEC_CURRENCY_2026-08-09/REVISION_01_RF-002_RF-003_2026-08-09/RETURN.md`, closeout `PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`, commit `e92a82ca9`); `D-PEC-100` and `D-PEC-98` for act-script rigour; the S4 draft (`PEC_SOW_CURRENCY_S4_PREP_2026-09-26/DRAFT_D-PEC-102_s4_sow_currency_proposal.md`) for the acceptance-lapse disclosure form. The brief also names commit `8f02609b5` as part of the 2026-08-09 SPEC re-acceptance; that commit is the 2026-08-04 DEL-01-06 RF-002 acceptance and touches no DEL-00-03 file, so it is not relied on here (SCA-005 `Propagation_Plan.md` L964 makes the same citation).
- **Fence.** `projects/pec/AGENTS.md` (`df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`) §"Write Scopes And Fences": every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the STATUS pointer needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. No earlier ruling opens these targets.
- **Source state.**
  - **Observation commit `6c6cc1b00`** (`6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240`, the PR #992 merge), `origin/main` after `git fetch` when preparation began. Every unanchored state claim in the candidates is an observation there, apart from the authoring-time wording that the add-on P candidate's AX-008 names as left unchanged.
  - **Pin `189f205ff`** (`189f205ff02df4111b33c20be441ce06e65ada7a`, SCA-006 checkpoint-3 acceptance, PR #954), an ancestor of `6c6cc1b00`. `SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `docs/PRD.md` and all four target preimages are byte-identical at the pin and at `6c6cc1b00`; between them no PKG-00 file changed except DEL-00-02's `_STATUS.md` (the `D-PEC-99` act) and the PKG-00 contexts and references (the `D-PEC-101` act).
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…d0e`) run from `projects/pec` of a `6c6cc1b00` export with `--operation exact-correction-preparation` on the four targets, both `_STATUS.md`, both `_REVIEW.md` and both (absent) `MEMORY.md`: `ALLOW`, exit 0, ×10 (`evidence/reliance_hold_preflight.out`).

## Method and owning workflow

- **Owning workflow, from the deliverables' records.**
  - **Artifact production.** Both artifacts were produced by WORKING_ITEMS under the PKG-00 package activation `D-PEC-72-PKG-00-WI-01` (run ID `D-PEC-72-PRE-P1-FOUNDATION`; `DEL-00-01/_run_records/D-PEC-72_PKG-00_ACTIVATION.md`, the authoritative copy, and the DEL-00-03 record copy), each bound by its deliverable's `SOW_V1` production contract, with candidate validation (`_run_records/D-PEC-72_CANDIDATE_VALIDATION.md`), then REVIEW and a separate owner act.
  - **Verification and acceptance.** REVIEW under the bundled `review` workflow (DEL-00-01: `SELF_CHECK`, snapshots `REV_DEL-00-01_2026-08-01_*`; DEL-00-03: `PEER_REVIEW` rerun `REV_DEL-00-03_2026-08-09_2136`, acceptance snapshot `REV_DEL-00-03_2026-08-09_2156`), then the owner's exact-byte act.
  - **Amendment practice.** The only accepted amendment of these bytes is the 2026-08-09 route that the owner named "the DEL-00-03 owning workflow": a bounded WORKING_ITEMS candidate edit of named loci → deterministic checks → REVIEW rerun bound to the new SHA → owner `ACCEPT_EXACT_BYTES`; historical bytes preserved; lifecycle, dependencies and source preserved. This packet follows that discipline for the candidate edit and its checks, with one difference stated plainly: on 2026-08-09 the candidate was REVIEWed before it became current, whereas under ruling A the new bytes replace the accepted ones before any REVIEW, and any re-review follows the act (question 3; a REVIEW-before-merge variant is named under "Options").
  - **Scope of Work contracts.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3`); no project or user workflow of that name exists. The contract edits are authored under `MODE=INIT` discipline (`DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`; source-grounded; every still-true sentence kept byte-for-byte), bound as an owner-ruled exact-bytes replacement, and checked by the method's `MODE=VERIFY` (the `D-PEC-100`/`D-PEC-98` practice). **Disclosure (one line):** Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` added `scope-of-work` `MODE=REVISE`; the owner has deferred adopting it in PEC, and this packet does not use it.
  - **No `MEMORY.md`** exists in either deliverable folder at `6c6cc1b00`.
- **Identities and hashes relied on** (at `6c6cc1b00`): `workflows/review/WORKFLOW.md` `99eae11d69671c283828818d4cb10c865d1f0a7af568ba267c54cee303e907ab`, `execution.json` `d1c668ae…074df`, `resources/contract.md` `fdf25136…cb18`, `resources/method.md` `669f5585…52e`; `workflows/scope-of-work/WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`, `resources/checks.md` `44ab41ac…f188`, `resources/tools.md` `fbd07771…5cc7` (`representation-migration.md` not loaded); standard `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254a…433c`. The `review` edition at `6c6cc1b00` is the one `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` (`30aab470…4168`) describes; the 2026-08-09 rerun predates it.
- **How "premise-only" is made mechanical.** Each target has a premise ledger (`premise/<KEY>.json`): an ordered list of hunks, each with its locus, cause (scope-change row), exact `pre` text (unique when applied), exact `post` text and reason. `render_candidates.py` reads the preimage at `6c6cc1b00`, checks its hash, applies the hunks and writes the candidate; its check mode requires the committed candidate to equal that rendering. **Every byte outside the listed hunks is the preimage** — the owner-accepted bytes for the three group-A targets, and for add-on P the DEL-00-01 contract bytes written by the `D-PEC-69` R4 owner-approved exact whole-contract repair (`ea6b4b5d0`, 2026-07-28; ratified by `D-PEC-71`), which were never separately accepted as exact bytes — so the ledger is the complete account of what changes.
- **The premise rule the drafters applied** (`DRAFTER_BRIEF.md`, `fbcc5e9f…cdca41`): a premise is a statement true when the bytes were accepted and false at the current basis because of SCA-005 or SCA-006 (including their propagation acts `D-PEC-93`, `D-PEC-95`, `D-PEC-101` and the PRD successors they adopted), including a count or completeness claim they made false; change only premises plus the smallest coherent consequence in the same sentence or row; keep history ("born from PRD v2.2 and revision 1.3 at `11a494e9a`", "seeded before P1"); report other findings unchanged; one uniform premise-amendment note per artifact; in contracts, keep every ID and meaning and add one provenance `AX-*`; name no D-PEC number in any candidate.
- **Actors.** Two Type 2 TASK drafters (DEL-00-03 pair; DEL-00-01 pair) and one Type 2 TASK tool builder, in one round; WORKING_ITEMS set the rules and the two readings in question 4, reconciled the returns, bound the act and ran the checks; fresh read-only `pec-reviewer` TASKs ran `MODE=VERIFY` and the packet review (`VERIFIER_VERDICT_*.md`, each with the manager's dispositions): verdicts 01–03 (all FAIL; blocking findings: a false ground in question 4(a), a misstated inventory row, and hunks correcting text stale since SCA-004 presented as premises), repaired — the add-on P candidate lost its two SCA-004-era currency hunks and was re-rendered; the DEL-00-03 basis-note correction is now labelled and put to the owner — then re-verified: verdict 04 (PASS WITH NOTES; its notes applied, including a scoped AX-008 in the add-on P candidate, re-rendered) and verdict 05 on that delta (PASS WITH NOTES; notes applied as draft text only). HELP_HUMAN's independent review of PR #997 (at `26c38d6ce`, PASS WITH NOTES) then asked for four repairs and several notes: posture 3 narrowed to the premise's own elements and add-on P aligned to it, AX-009 tempered, the REVIEW-before-merge variant restated, reading 4(a) stated as beyond premise-only scope, whitespace-clean stored diffs, and the counts refreshed at `f0a6159c9`; the three changed candidates and the script were re-rendered, the checks and controls rerun, and verdict 06 (PASS WITH NOTES) verified that delta; its notes were applied as text only (draft, one ledger `why` field, the return), with no candidate, claim, script or check-aid change. Models: Opus 5.5 (`claude-opus-5-5`) at `high` for every actor. Role identity is instruction-asserted.
- **Tools** (`tools/scope_of_work/`, unchanged at `6c6cc1b00`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`.

## What preparation found

### Lifecycle

- **Both deliverables are `CHECKING`** at `6c6cc1b00` (`DEL-00-01/_STATUS.md` `41c871a5…ceea`; `DEL-00-03/_STATUS.md` `629ca0dd…6cfb`), each entered on 2026-08-01 by the owner-approved D-PEC-72 review-from-`INITIALIZED` override. None of the targets is `ISSUED`.
- Per the brief, `CHECKING` does not stop this packet: the graph routes these amendments through an owner-ruled exact-byte packet, as SCA-005 §B5 and SCA-006 §B4/§B5 direct. **No lifecycle change is proposed or implied.** The act script refuses if either `_STATUS.md` or `_REVIEW.md` differs from its pinned bytes, and never writes them.
- **Root review-edition consequence (disclosed, not raised).** `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` revises the bundled `review` workflow: while `CHECKING`, a deliverable's claim surfaces are treated as frozen at a recorded candidate SHA, a `CHECKING → ISSUED` review checks that they are unchanged since it, and a deliverable that entered `CHECKING` under an earlier override without a recorded frozen SHA or checking basis is surfaced for a human ruling that records them, or for the reversal. The notice leaves adoption to this loop, and the work graph holds it as a consequence with no owner prompt, for D1 to account for. The account: both deliverables entered `CHECKING` under the D-PEC-72 override; their `_REVIEW.md` records carry exact-byte artifact acceptances and review bases, not a frozen candidate SHA in the notice's sense. This packet follows PEC's accepted amendment practice (the 2026-08-09 route, which amended the `CHECKING` DEL-00-03 in place under an owner exact-byte gate), not the revised edition, and it makes no claim under it. Whatever a later review under that edition would surface for these deliverables stays with that later review.

### Premise inventory

Line numbers are preimage lines. "Named" means the scope-binding source names the locus; "review" means the owning-workflow review found it (a premise the brief asks to be reported with evidence). Current sources are read at `189f205ff` unless noted.

**DEL-00-03 `artifacts/v2/SPEC.md` — 22 hunks** (`premise/DEL-00-03_SPEC.json`)

| Hunk | Locus | Was | Cause | Now |
|---|---|---|---|---|
| P01 | after L7–9 | — | brief (uniform note) | premise-amendment note naming PRD v2.4, revision 1.6 at `189f205ff` and the accepted hash |
| P02 | L17 | "PRD v2.2 requirement identifiers" | named (SCA-006 §B5 counts) | "PRD v2.4 …" |
| P03 | L23 | "PRD v2.2: 46 `PEC-*-NNN` requirements" | named (SCA-006 §B5, L23) | "PRD v2.4: 49" (PRD §§9–10 carry 49 rows: ORI 7, RCN 6, GAT 4, PRS 7, STR 5, API 7, DSH 7, SVC 6) |
| P04 | L46 K-03 row | "an enabled consumer owns use and verify-before-rely" | named (SCA-006 §B5, L46; `D-PEC-90`) | consumer-owned use; operational reliance only within the declared pin, coverage and trust tier (PEC-ORI-007) and only from a release past the §12 gate; never authority (PEC-K-02); file fallback when PEC is absent, degraded, failing its checks or stating a limitation |
| P05 | L62 | "full 46-requirement catalogue" | named (SCA-006 §B5, L62) | "49-requirement" |
| P06 | L68 Orientation | `PEC-ORI-001..006`; `SOW-004..009` | review (SCA-006: PEC-ORI-007, SOW-097; the row is part of the "full catalogue" claim) | `PEC-ORI-001..007`, "and the reliance envelope"; `SOW-097` added |
| P07 | L69 Reconciliation scope | `SOW-010..021` | review (SCA-005: SOW-095, SOW-096 cite PEC-RCN-002) | adds `SOW-095`, `SOW-096` |
| P08 | L71 Presence | "correlation/hierarchy"; `SOW-026..032` | review (SCA-005: PEC-PRS-004 deferred behind T-RT; SOW-029 OUT) | "correlation (live hierarchy deferred behind trigger T-RT)"; "(SOW-029 OUT, deferred)" |
| P09 | L72 Streams | "declared bridges" | review (SCA-005: PEC-STR-003, hooks CLI the only remaining bridge; SOW-035, SOW-037 OUT) | the hooks CLI bridge, Runtime SSE bridge deferred (T-RT), cmux deferred; "(SOW-035, SOW-037 OUT, deferred)" |
| P10 | L73 API | `PEC-API-001..005` | named (SCA-006 §B5, L73) | `PEC-API-001..007`; response-size budgets and a read-only agent tool-call query surface; `SOW-098`, `SOW-099` |
| P11 | L77–81 release proof | list ends at directed bootstrap | named (SCA-006 §B5, L78) | adds "the §12 standing reliance-advertisement gate" and `SOW-100` |
| P12 | §4 L85–87 | record-tier list | named (SCA-005 §B5 §4; INV-182, inventory NOTE-ONLY) | "Workplan/Step/Gate (a declared historical-grammar entity)"; adds WorkGraph/WorkNode (PRD v2.4 §7.1; SOW-001) |
| P13 | §6 L114 | "all 64 deliverables" | review (SCA-005/006 register changes) | "all 68 deliverable rows (64 active; four retired under SCA-005)" (reflow only in the rest of the sentence) |
| P14 | §6 PKG-02 | `DEL-02-01..07` | review (SCA-005 added DEL-02-08/09) | `DEL-02-01..09` |
| P15 | §6 PKG-04 | role | review (SCA-006: SOW-097 in PKG-04) | adds "and the reliance envelope" |
| P16 | §6 PKG-06 | "hierarchy" | review (SCA-005: DEL-06-04 retired) | live hierarchy deferred (T-RT); "(DEL-06-04 retired)" |
| P17 | §6 PKG-07 L128 | "declared daemon/hook/cmux/runtime-client bridges" | named (SCA-005 §B5 PKG-07 row, daemon and cmux; INV-183) | the hooks CLI bridge, the only remaining bridge; Runtime SSE bridge and runtime-client seam deferred (T-RT); cmux deferred; "(DEL-07-02, DEL-07-04, DEL-07-05 retired)" |
| P18 | §6 PKG-08 | role; `DEL-08-01..05` | review (SCA-006: DEL-08-06, SOW-098/099) | adds response-size budgets, agent tool-call query surface; `DEL-08-01..06` |
| P19 | §6 PKG-10 | `DEL-10-01..12` | review (SCA-006: DEL-10-13) | `DEL-10-01..13` |
| P20 | L133 | "94 items: 72 IN, 14 OUT, and 8 TBD" | review (revision 1.6 §7) | "100 items: 74 IN, 18 OUT, and 8 TBD" |
| P21 | §7 L146–147 | "P3 … interfaces/presence/Git observation, and P4 streams/live hierarchy" | review (PRD v2.4 §12 P3/P4) | P3 adds the agent tool-call query surface; P4 streams, with live hierarchy tier and Runtime SSE bridge deferred (T-RT) and cmux deferred |
| P22 | §8 L156 | labels only | named (SCA-005 §B5 §8; INV-184, inventory NOTE-ONLY) | appends the SCA-005 re-expressed premises of OI-002, OI-006 (and its SCA-006 `agent`-credential scope) and OI-008 (revision 1.6 §10); the OI-003 sentence and the rest are unchanged |

**DEL-00-03 `ScopeOfWork.md` — 15 hunks** (`premise/DEL-00-03_SOW.json`)

| Hunk | Locus | Was | Cause | Now |
|---|---|---|---|---|
| P01 | frontmatter L5 | `…@11a494e9a` | reading (a), question 4 | `…@189f205ff02df4111b33c20be441ce06e65ada7a` (revision 1.6) |
| P02 | basis provenance note L52–57 | "`_REFERENCES.md` names … revision 1.3 …; … 1.1 → 1.2 → 1.3" | consequence of P01 (the paragraph states the bound basis); its first sentence was already stale since the SCA-004 re-pin `1c6ecc6d9` and, left beside the rebound basis, would contradict it — corrected for that reason, not as a premise (question 4(a)) | names revision 1.6 and the 1.1 → … → 1.6 chain (observed at `6c6cc1b00`); bound basis 1.6 at `189f205ff`; 1.3 at `11a494e9a` is the SPEC's birth basis |
| P03 | OUT-002 L60 | "`PRD.md` v2.2" | reading (a) (SCA-006 §B4) | "v2.4" |
| P04 | CLM-004 L70 | quotation only | named (SCA-006 §B4, CLM-004 L70) | quotation kept verbatim (the register note is unchanged at revision 1.6); own-voice sentence: "46 requirements" is the PRD v2.2 count, PRD v2.4 carries 49 |
| P05 | CLM-005 L76 | revision 1.3 counts | consequence of P01 | revision 1.6: 11 packages, 68 deliverable rows (64 active; four named retired), 6 objectives, 100 items (74 / 18 / 8) |
| P06, P07 | CLM-006 L77 | "The requirement source of record is `PRD.md` v2.2 alone:" | named (SCA-006 §B4, CLM-006 L77; INV-131, inventory NOTE-ONLY) | source of record is PRD v2.4 (the revision 1.6 `source_corpus`; 49 and 11); intake posture 1 is quoted verbatim, in its revision 1.3 wording, "verbatim at revision 1.6" |
| P08 | CLM-009 L80 | "…event-contract types shared by daemon, hooks CLI, and adapters" | review (SCA-005 §B4 "quotations of §1.4/§4 charter"; INV-132, inventory NOTE-ONLY: "refresh only if the charter changes", and it did) | re-quoted from revision 1.6 §4: "consumed by the hooks CLI bridge, the only remaining bridge" |
| P09 | REQ-001 L96 | "…at the basis revision and commit bound…" | consequence of P01 | "…as brought current to the revision and commit bound…" (the seed was born from revision 1.3; its premises are current to the rebound basis) |
| P10–P12 | REQ-002, REQ-003, AC-003 | "`PRD.md` v2.2" | reading (a) | "v2.4" |
| P13 | production sequence L125 | "`PRD.md` v2.2's" | reading (a) | "v2.4's" |
| P14 | AX-003 L148 | "The accepted basis is … revision 1.3 …" | consequence of P01 | revision 1.6 at `189f205ff` via SCA-006; 1.3 at `11a494e9a` is the SPEC's birth basis; 1.5, 1.4, 1.2, 1.1 prior provenance |
| P15 | new AX-009 | — | brief (provenance) | prior hash, causes, rebind rationale, IDs whose rule changed, observation at `6c6cc1b00`, pin `189f205ff` |

No ID is added (other than AX-009), retired or reused. Validator `PASS format=SOW_V1`. The derived checklist changes only in `AC-003`'s text (v2.2 → v2.4) and in line numbers and the source hash: prior `1c4d492728e3e7a5c031bdb2a6f915e855916effa7cc1644f8bd7031b73ffbdb` (the hash `_REVIEW.md` binds) → `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1`.

**DEL-00-01 `artifacts/v2/ADRs.md` — 6 hunks** (`premise/DEL-00-01_ADR.json`)

| Hunk | Locus | Was | Cause | Now |
|---|---|---|---|---|
| P01 | after L8–10 | — | brief (uniform note) | premise-amendment note |
| P02 | Decision 2, L53–57 (daemon token L54; reflow only) | "CLI, daemon, socket, …" | named (SCA-005 §B5, daemon; INV-179, inventory NOTE-ONLY) | "CLI, application-owned Runtime service, socket, …" (PRD v2.4 §8; `D-GOV-43` A2) |
| P03 | Consequences, L84–85 | "daemon/hook/cmux bridges" | named (SCA-005 §B5, daemon and cmux at L84; INV-180, inventory NOTE-ONLY) | "the hooks CLI bridge" (PEC-STR-003) |
| P04 | ADR-002 context, L128 | "Root-runtime / optional-client / human-only-act boundary" | named (runtime-ownership premise) | "runtime-ownership / optional-client / human-only-act boundary" |
| P05 | carried posture 3, L144–149 | "Root owns generic runtime semantics including sessions, delegation, turn locks, credentials, interruption, and model residency; … PRD v2.2 §4.2 and §15" | named (SCA-005 §B5 posture 3; INV-178) | for each App instance the application-owned Runtime service owns sessions, delegation, tools, turn locks and interruption; credentials custodied by Codex; local-model residency retired (only the premise's own elements are corrected — "tools" is carried from K-RUNTIME-1's enumeration of the same runtime semantics; the `codex app-server` child is not added) (`D-GOV-43` A2, superseding `D-GOV-20` items 2–4 on that path; Root `docs/CONTRACT.md` K-RUNTIME-1); "PEC is an optional client and starts no second execution loop", the human-only acts and "`D-PEC-56` behaviors 2, 4, and 7 as limited by `D-PEC-58` behavior 8" kept; "PRD v2.4 §4.2 and §15" |
| P06 | carried posture 4, L150–152 | "runtime-client seam is an adapter … does not transfer Root runtime ownership … (`SOW-087`)" | review (SCA-005: SOW-087 OUT behind T-RT, DEL-07-05 retired; INV-181, inventory NOTE-ONLY) | "seam, deferred behind trigger T-RT, is an adapter … if taken up. It does not transfer runtime ownership into PEC …" "(`SOW-087`, deferred OUT; PRD v2.4 §13)" |

The ADR-PEC-V2-001 decision (ports and adapters), its consequences' substance, the D-PEC-72 selection and every non-decision are unchanged. The owner's AC-007 confirmations — hexagonal isolation, and that nothing makes a governed act depend on PEC-held state — remain true of the amended bytes: the amendment only restates who owns the runtime (outside PEC) and which bridges remain. **SCA-006 made no ADR premise false:** its plan leaves `ADRs.md` untouched and `CURRENT` for its own causes (SCA-006 `Propagation_Plan.md` §B5; IA §7.2), and the drafter and verdict 06 checked that no SCA-006-changed text is stated in them: the ADR cites PEC-K-03 only for "not a new consumer duty", which PRD v2.4's amended PEC-K-03 still supports, and states no §12 gate or operational-reliance text. Every ADR hunk is an SCA-005 cause.

**Add-on P — DEL-00-01 `ScopeOfWork.md` — 3 hunks** (`premise/DEL-00-01_SOW.json`; see "Add-on P")

| Hunk | Locus | Was | Cause | Now |
|---|---|---|---|---|
| P01 | CLM-005 L81 | "limited to Root ownership of generic runtime semantics" | named (SCA-005 §B4 row DEL-00-01; IA row 308; INV-130, locator CLM-005 L81) | "limited to the application-owned Runtime service's ownership of sessions, delegation, tools, turn locks, and interruption for each App instance, with credentials custodied by Codex and local-model residency retired (`D-GOV-43` A2, …; Root `docs/CONTRACT.md` K-RUNTIME-1)" — the same elements as the amended ADR posture 3 |
| P02 | REQ-004 L99 | "Root owns generic runtime semantics;" | review (REQ-004 restates CLM-005's premise verbatim; INV-130 does not name it) | "the application-owned Runtime service owns sessions, delegation, tools, turn locks, and interruption for each App instance, credentials are custodied by Codex and local-model residency is retired (`D-GOV-43` A2);" |
| P03 | new AX-008 | — | brief (provenance) | prior hash; the SCA-005 cause; IDs whose rule changed (CLM-005, REQ-004: the named runtime owner and the scope it owns, with credential custody and model-residency retirement, per Root `docs/CONTRACT.md` K-RUNTIME-1 and `docs/DIRECTIVE.md`, matching the amended posture 3); birth basis kept (frontmatter and AX-002, revision 1.3 at `11a494e9a`); the SCA-004-era currency wording and the authoring-time lifecycle wording (Epistemology opening paragraph, AX-006, CON-001) left and reported, with the observation sentence scoped around them; observation at `6c6cc1b00`; pin `189f205ff` |

Validator `PASS format=SOW_V1`; **no `AC-*` text changes** (checklist `bb815439…3b84` → `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9`, the source hash only; AX-008 follows every criterion, so no line number moves). `DEL-00-01/REQ-006` and `/AC-005`, which DEL-01-01's contract cites, are byte-identical.

### Loci examined and left unchanged on purpose (summary)

- **SPEC:** the "Born from" paragraph and §10's "seeded before P1 from accepted decomposition revision 1.3" (history); §2 boundary and non-goals, the other K-rows, the GAT, DSH and SVC rows; the presence-tier entity list (HierarchyEdge is still in PRD v2.4 §7.2 and SOW-002); §5 objectives; PKG-00, 01, 03, 05, 09 roles; the PKG-10 role ("release proof" covers the gate); §7 modes paragraph; §8's OI-003, OI-013 and "eight `TBD`" (still eight) sentences; §9. The preimage's daemon/cmux premise at L128 is replaced; the new text names them only as deferred or absent.
- **DEL-00-03 SOW:** objective-warrant history; CLM-011 ("At the accepted revision 1.4 basis …", dated and still true); CLM-014, AX-007; every other quotation, verified verbatim at its named commit (30 quote entries); TBD-002 (`docs/` still holds only `PRD.md` and `STATUS.md` besides `.archive`); AC-002/VER-002's "64 deliverables" (the active count); REQ-004, AC-004, VER-004 (the SPEC states its birth basis and names revision 1.6 at `189f205ff`, equal to the rebound frontmatter).
- **ADRs:** the authority-status and accepted-basis paragraphs; ADR-001 context (it cites no SCA-006-changed text); Decision 1's "runtime-client" adapter class (a still-true conditional rule); Decisions 3–7; ADR-002's "Sources" line (kept as provenance of the accepted record; the amended postures carry their own current citations — see question 4 (b)); posture 2's history of ADR-014; "PEC is an optional client" (SOW-088 and the DEL-00-01 register row still read "runtime/client" at `189f205ff`).
- **DEL-00-01 SOW (add-on P):** frontmatter and AX-002 (the birth basis; no premise requires moving it, because no DEL-00-01 criterion resolves identifiers "at the bound basis"). **INV-130's note** names REQ-005, AC-003 and AX-004 ("accepted v2 runtime/client ... boundary") as carrying the same premise; they, and OUT-002, are left unchanged on purpose: they echo register wording still verbatim at `189f205ff` (`ScopeLedger.csv` SOW-088 and the `Deliverables.csv` DEL-00-01 row read "accepted v2 runtime/client and human-only-act boundary"), they name no runtime owner, and changing AC-003 would change the checklist. The objective warrant ("revision 1.3, the current successor basis") and the basis provenance note ("`_REFERENCES.md` now names … revision 1.3") are stale since SCA-004 (revision 1.4 applied at `65955cceb`; reference re-pin `1c6ecc6d9`), not by SCA-005/006; they are left and reported (Other findings), and AX-008 says so, as it does for the authoring-time lifecycle wording (Other findings 1).

### Other findings (not premises; not changed; for later)

1. DEL-00-01 SOW L92–94 (the Epistemology opening paragraph), AX-006 and CON-001 still describe the pre-D-PEC-72 state ("No ADR exists … `INITIALIZED`"; OI-012 "undecided at the time of this contract"). Stale since 2026-08-01, not by SCA-005/006, and lifecycle-adjacent; add-on P's AX-008 names them as left unchanged and scopes its observation sentence around them. The Praxeology opening ("Production sequence expected of the future authoring run") is authoring-time wording of the same kind; it states an expectation rather than a present state, and AX-008 does not list it. (Ordering: the SOW's AX-006 wording and its L94 date from `ea6b4b5d0`, 2026-07-28, and L92–93 from `01199c851`, 2026-07-25; the ADR file was added at `5942c5033`, 2026-08-01.)
2. `ScopeLedger.csv` and `SOFTWARE_DECOMP.md` §2.2 SOW-067 Notes still read "Permanent. Daemon owns execution (C13)", while C13 was re-expressed under SCA-005 — a decomposition surface for a later scope change.
3. `SOFTWARE_DECOMP.md` §1.4 intake posture 1 ("PRD v2.2 alone … 46") and the `Deliverables.csv` DEL-00-03 envelope note ("46 requirements / 64 deliverables") are unedited at revision 1.6; the DEL-00-03 contract now quotes them verbatim and corrects the premise in its own voice. (SCA-005 Q-CP2-3 (a) left such residual register text.)
4. `3623b958b`, cited as revision 1.2's commit in the DEL-00-03 note and AX-003, does not resolve in this repository (the known housekeeping pin, SCA-005 §B4); kept verbatim.
5. DEL-00-03 SOW L46 presents "thin but non-arbitrary" where the SCA-002 source reads "Thin but non-arbitrary." (case only); CLM-013's `'seeded before P1'` renders the exhibit's doubled double quotes as single quotes. Both predate SCA-005.
6. The SPEC's §2 non-goal list omits "not a Git actor" (PRD §4.2); predates SCA-005.
7. DEL-00-01 AX-002, DEL-01-05 AX-006 and DEL-10-01 AX-005 still say "The accepted basis is `SOFTWARE_DECOMP.md` revision 1.3" (DEL-01-05 and DEL-10-01 are outside this packet).
8. DEL-00-01 SOW objective warrant ("it remains unchanged in revision 1.3, the current successor basis") and basis provenance note ("`_REFERENCES.md` now names `SOFTWARE_DECOMP.md` revision 1.3 as the accepted `current_basis` …; … SCA-003 establishes revision 1.3 as the current successor") have been false since SCA-004 (revision 1.4 applied at `65955cceb` and the reference re-pin `1c6ecc6d9`, both 2026-08-03); not SCA-005/006 premises, so left (add-on P's AX-008 records this).
9. `projects/pec/AGENTS.md` §"Shared Runtime Boundary" still says "The client seam carries as a concept, reimplemented against v2 entities (PRD v2 §13)", while PRD v2.4 §13 defers a per-application Runtime client behind trigger T-RT and SOW-087 is OUT (an instruction surface; outside this packet).
10. DEL-00-01 REQ-005 asks the ADR set to cite `projects/pec/docs/.archive/adr/ADR.md`; the ADRs cite the archived ADRs without that literal path (pre-existing; an RR1 review would meet it).
11. PRD v2.4 §13 still reads "live postures (ADR-002, ADR-014) re-cited in v2's first ADRs" (SCA-003's reading; not an SCA-005/006 premise).

### Acceptance-lapse account

| Record | What the owner accepted | What happens under ruling A (and P) |
|---|---|---|
| DEL-00-03 `_REVIEW.md` ("Exact-byte acceptance and remaining gates"; `REV_DEL-00-03_2026-08-09_2156`; `_Evaluation/Reviews/_LATEST.md`) | `ACCEPT_EXACT_BYTES` of SOW `3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741` and SPEC `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae`; AC-011 (the owner's confirmation that the seed is the v2 SPEC of record and that the LOW-confidence OBJ-001 attribution stands) satisfied for those bytes | **Both acceptances lapse on the record's own terms**: "Any SOW or SPEC byte change invalidates this acceptance and requires a new checklist derivation and REVIEW rerun." AC-011 is unsatisfied for the new bytes until a later owner act. The record keeps describing the prior bytes, bound to checklist `1c4d4927…`; this packet does not write it. |
| DEL-00-01 `_REVIEW.md` ("Owner artifact-fitness ruling"; `ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md`) | AC-007 "ACCEPT" of `artifacts/v2/ADRs.md` at `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` ("This accepts these artifact bytes only"); the SELF_CHECK review basis binds that ADR hash and the SOW `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` | **The ADR acceptance lapses**: it is bound to the prior hash, and AC-007 is unsatisfied for the new bytes until a later owner act. The record states no general invalidation clause, but acceptance and review basis are hash-bound. With add-on P the SELF_CHECK's SOW basis also describes superseded bytes. No owner exact-byte acceptance of the DEL-00-01 SOW was found. |

Neither `_REVIEW.md`, `Review_Findings.csv` nor any `REV_*` snapshot is written. Lifecycle stays `CHECKING` for both. No REVIEW is opened, and nothing here is a CHECKING question.

**Re-review, as an owner option (question 3; not assumed):**

- **RR1 — REVIEW rerun, then owner exact-byte acceptance (recommended; the record's own terms and the 2026-08-09 precedent).** A later, separately authorized REVIEW of the new bytes for each deliverable (a fresh checklist derivation — DEL-00-03 `a3bc80a0db9a…21b1`; DEL-00-01 `6e99f93c37c7…8cf9` with P, or the unchanged `bb815439…3b84` without P — against the new artifact hashes, recorded in `_REVIEW.md`, `Review_Findings.csv` and a new `REV_*` snapshot), followed by the owner's `ACCEPT_EXACT_BYTES` of the tabled postimage hashes, with the owner confirmations the prior acts carried (DEL-00-01 AC-007; DEL-00-03 AC-011). Selecting RR1 records the intent: HELP_HUMAN adds a graph node for that later REVIEW packet; this packet grants none of it, and the later authorization names its review type and method basis. Disclosed: the bundled `review` edition at `6c6cc1b00` carries the frozen-candidate rules described under "Lifecycle"; the 2026-08-09 rerun predates them.
- **RR2 — owner exact re-acceptance of the new bytes in this ruling.** The owner states `ACCEPT_EXACT_BYTES` for the tabled postimage hashes, relying on this packet's `MODE=VERIFY` and independent verifier evidence; HELP_HUMAN records it in the ruling record. To stand where the prior acts stood, the owner's words would also cover DEL-00-01 AC-007's two confirmations (ports-and-adapters isolation; nothing makes a governed act depend on PEC-held state) and DEL-00-03 AC-011's (the seed is the v2 SPEC of record; the LOW-confidence OBJ-001 attribution stands). Disclosed: for DEL-00-03 this departs from the record's stated requirement of "a new checklist derivation and REVIEW rerun"; the preparation verdicts are packet verification, not a REVIEW; no `_REVIEW.md` would record the acceptance unless a later act writes it.
- **RR3 — neither now.** The acceptances lapse; the new bytes stand un-accepted, lifecycle unchanged, until a later steer. (For context only: the owner ruled `D-PEC-102` A on 2026-09-26 with DEL-04-01's prior exact-byte acceptance lapsing and no review opened.)

Without an answer, RR3 holds (nothing is opened).

### External anchors and downstream consequences

- **Dependency evidence quotes.** No ACTIVE `Dependencies.csv` row, in any register, has any of the four targets as its `EvidenceFile` (`check_quote_currency.py`: `TARGET-cited active rows: 0`); corpus-wide quote currency is 127/127 verbatim before and after the act. **No dependency row goes stale**, and none is written. The two ACTIVE EXECUTION edges into DEL-00-01 — DEP-00-02-003 (DEL-00-02 → DEL-00-01) and DEP-01-01-003 (DEL-01-01 → DEL-00-01) — take their `EvidenceFile` and `EvidenceQuote` from `SOFTWARE_DECOMP.md` OI-012 text, not from the targets, and are unaffected.
- **Other contracts citing or quoting the targets** (verified by the drafters and the heuristic scan; nothing here changes them):
  - DEL-01-01 `ScopeOfWork.md` CLM-009 (L103) anchors the ADR hash `f63ecc2725b2…5db5` and the DEL-00-01 contract hash `433461504444…1740` at `aca930622`: it stays a true anchored observation, but after the act it describes superseded bytes (and, with P, a superseded "reliable input" contract). Its quotation of the ADR ("Inside PKG-01, record- and presence-tier entity schemas are core-facing") is unchanged. REQ-009 cites `DEL-00-01/REQ-006` and `/AC-005` — byte-identical. CON-001 and AX-008 unaffected.
  - DEL-01-05 `ScopeOfWork.md` (`IN_PROGRESS`) AX-005 cites the ADR-002 re-citation (unchanged). Its TBD-005 (L72) rests on "D-PEC-72 O-B and accepted `ADR-PEC-V2-001`" (the S1 candidate keeps that text): ADR-PEC-V2-001's decision is unchanged, but once the ADR acceptance lapses (under RR3, or until RR1 completes; not under RR2) the word "accepted" describes the prior bytes. Listed for DEL-01-05's own packet; nothing here changes it.
  - No contract quotes SPEC text or DEL-00-03 SOW text; other contracts cite only the ID DEL-00-03.
- **Records that quote changed text** (history; not edited; the scan at `origin/main` `f0a6159c9` lists 82 heuristic STALE lines: 69 in the records below, and 13 scanner artefacts): the `D-PEC-90` proposal L65 and SCA-006 `Propagation_Plan.md` L319 (old K-03 row); the TM-PEC-014 handoff L78 (old §8 paragraph); SCA-005 `IMPACT_INVENTORY_PEC_BASIS.csv` (the scan flags INV-065, INV-130, INV-132 and INV-178..183; INV-131 and INV-184 also quote changed loci); the 2026-09-05 concordance CSVs under `_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/` (old REQ-001/002/003, AC-003, CLM-005, REQ-004 text); `TM-PEC-014_SPEC_CURRENCY_2026-08-09/REVISION_01_RF-002_RF-003_2026-08-09/DEL-00-03_REVIEW_CHECKLIST.json` L75 (old AC-003 text). DEL-00-03 `_REVIEW.md` also quotes the old AC-003 text and binds checklist `1c4d4927…`; the heuristic scan does not flag it. The other 13 are scanner artefacts matching other contracts' `@11a494e9a` frontmatter text: six in the S4 prep folder, six in the S4 act run root `SOW_CURRENCY_S4_2026-09-26/`, and one in the live DEL-08-01 contract written by the `D-PEC-102` act, which cites its own prior pin. (At the observation commit `6c6cc1b00` the scan listed 75: the same 69 and six artefacts.) Hash anchors (2,198 live, 30 history) are almost all in the concordance manifests; the rest are `_REVIEW.md`/`Review_Findings.csv`/run records of the two deliverables, the D-PEC-72/74/75/77/78 packets, DEL-08-02's D-PEC-74 activation record and the closed `loop/LOOP_RECEIPTS.md` — all history.
- **Line-number references.** SCA-005/006 plans and IA cite preimage lines (L23, L46, L54, L62, L73, L78, L84, L128); after the act they refer to the accepted preimage.
- **Relation to S1, S4, K2.** S1 (`D-PEC-104`, PR #986) excludes DEL-00-01 and DEL-00-03; S4 (`D-PEC-102`, ruled A + M after the observation commit) excludes DEL-00-03; K2 (`D-PEC-103`) writes only DEL-08-06/10-13. None cites a local ID of these targets, and this act pins none of their targets, so any ruling order works.

### Add-on P — why it is offered

The brief names, for DEL-00-01, only the ADR. The DEL-00-01 contract carries the same stale premise: SCA-005 §B4 classes it `STALE_REVIEW_REQUIRED` for "C13/D-GOV-43 runtime-ownership premise" — the SCA-005 plan's §B4 row at L828 covers the DEL-00-01 contract itself, so add-on P follows the brief's own scope-binding sources even though the brief does not name the file (inventory INV-130: CLM-005 L81; its note names REQ-005/AC-003/AX-004, and review finds the same premise stated verbatim in REQ-004), and **it has no packet home** — the S1 packet excludes DEL-00-01 because it is `CHECKING`. Its REQ-004 obliges the ADR set to "carry forward only the accepted v2 boundary recorded in CLM-005: Root owns generic runtime semantics", so **ruling A without P leaves the amended ADR contradicting its own contract**, and a later REVIEW of the ADR against that contract would meet the conflict. Add-on P is the premise-only correction of that contract (CLM-005, REQ-004 and the provenance AX-008), prepared under the same rules and checks. **It goes beyond the brief's touch limit** ("only the named artifacts and, if needed, DEL-00-03's `ScopeOfWork.md`"): it enters the act only if the owner selects it (question 2), and HELP_HUMAN decides whether to present it or withhold it.

## Options

- **A — the three premise-only replacements in one act, no lifecycle change (recommended).** 3 product paths, all modified; nothing created or removed; no `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, register, context, reference, dependency or `MEMORY.md` file touched. The owner acceptances of the three prior files lapse (see the account); the re-review is question 3.
- **A + P (recommended together)** — as A, plus the DEL-00-01 contract (4 paths).
- **A (+ P) + M** — plus add-on M at the undertaking's closeout.
- **Amend** — for example: drop a hunk (the ledger makes each separable, but P01 of the DEL-00-03 contract carries P02, P05, P09 and P14 with it, and dropping it makes the amended SPEC fail AC-002/AC-005 against a revision-1.3 binding); keep the SPEC's §8 unchanged; change a reading in question 4; or a REVIEW-before-merge variant — the owner rules the bytes **and** separately authorizes a REVIEW; the act runs once on its branch exactly as granted (its script pins `_REVIEW.md` and `Review_Findings.csv`, so no REVIEW may be written before it, and no re-pin is pre-authorized); checks 1–12 run on that act commit; the REVIEW and the owner's exact-byte acceptance are then recorded on the same branch, in their own commits under that separate authorization, whose files the review checks cover instead of rows 8 and 11; and the branch merges only after acceptance. This keeps the new bytes off `main` until they are reviewed and accepted, as on 2026-08-09. A REVIEW before the act would instead need a re-rendered script, which this packet does not grant.
- **Defer** — nothing opens; the artifacts keep premises that SCA-005 and SCA-006 made false, and the SCA-005 §B5 / SCA-006 §B5 obligations stay open.

A split that amends the SPEC without the DEL-00-03 contract is not offered: the SPEC's corrected premises cite revision-1.6 identifiers and PRD v2.4 requirements that the unamended contract's AC-002, AC-003 and AC-005 would reject.

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once**, with `--with-addon-p` only if add-on P is selected. Paths are relative to `projects/pec/execution/`.

| Group | Target | Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|---|
| A | DEL-00-03 SPEC | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` |
| A | DEL-00-03 SOW | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/ScopeOfWork.md` | `3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741` | `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` |
| A | DEL-00-01 ADRs | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` |
| P | DEL-00-01 SOW | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md` | `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` |

The postimages are the exact candidate files (207, 172, 182 and 152 lines), copied byte for byte into the run root as `candidates/…`. They have no date slot and name no D-PEC number.

Read-only files the act re-verifies before and after writing and never writes (SHA-256 at `6c6cc1b00`; the first five also at `189f205ff`):

- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`
- `projects/pec/execution/_Decomposition/Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`
- `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`
- `projects/pec/docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- DEL-00-01 (`…/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/`): `_STATUS.md` `41c871a5e4c07655a1f526aeb20f74603099f0b5997bbba4d7a8fcc2897ceeea`; `_REVIEW.md` `c417418e96bfb8e230634049c7ee359fb84ad688a7946b5f819e21b2bc5d6968`; `Review_Findings.csv` `3f1cec3bf34776b3cc7e9d0fdacd3dd268e6ddf9dfb4e51855d0d1efa40e25e0`; `Dependencies.csv` `a8573c64bf2828add66cba70e00b91115e8d885060b905a689e5ee1d60654467`; `_CONTEXT.md` `f9647800b5bba9cb13ebedc666ca680d6b41ee00344afffcd4a9817a0ac25701`; `_REFERENCES.md` `f38d9257b5fff875a7e9d11c9832ed2e08a814a24eac2b3390a95f76e61387eb`
- DEL-00-03 (`…/DEL-00-03_v2_SPEC_seed/`): `_STATUS.md` `629ca0dda894954943b694680ebbaf8688615e0ca3fefa1a18ef84c2cd606cfb`; `_REVIEW.md` `200125240bbed6cd7e3dd2cc64d0cc8619348cf2cbdfaae3e5ee9d169f8c8b97`; `Review_Findings.csv` `fd28bac592572edcdff196fb40fc8d6ebeaf1bab97f8cb207f67196cddc9301e`; `Dependencies.csv` `5b42f2de2a098fb8f833736ebaf15445bd50734a9341b7fb19e7fa1d0112cde2`; `_CONTEXT.md` `d4742ccaf65aeb05620e88413b14c56f416a23920d1b044538ee3a174b05be14`; `_REFERENCES.md` `fb18afbb27fe54493f6dac0df890d86359db43ad0b4b8fefbd84075bf68a1146`

### Add-on M — MEMORY files (only if question 5 selects it)

Neither folder has a `MEMORY.md` at `6c6cc1b00`. The deliverables' records support one: each already indexes prior runs in `_run_records/` (D-PEC-72 activation and validation, the D-PEC-63/66 contract runs), and `projects/pec/AGENTS.md` asks for a MEMORY run row, or an owner decision to complete without it, when a packet opens a deliverable. At the undertaking's closeout (graph node M1), WORKING_ITEMS creates, under each `PKG-00_Architecture_Runway_Contracts/1_Working/<DEL folder>/`, `MEMORY.md` from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` row:

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | Premise-only amendment under D-PEC-105 (graph node D1). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-105 ruling record> |
```

| Deliverable | Path | Preimage | Act |
|---|---|---|---|
| DEL-00-03 | `…/DEL-00-03_v2_SPEC_seed/MEMORY.md` | absent | created from the template |
| DEL-00-01 | `…/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/MEMORY.md` | absent | created from the template |

The slots `{D}`, `{PR}` and the two link targets are fixed at closeout ("D-PEC-105" follows the final number). The verifier checks that no other byte departs from the template.

## Generation method (binding)

The postimages come from one run of `apply_d1p.py`, **SHA-256 `952a7512fd74e1b77f2f6b948d3cf46c876448ee1dee5370759f627236399d4d`** (stdlib-only Python, prepared with CPython 3.13.7), rendered by `build_apply_d1p.py` from `apply_d1p.template.py` at basis `f0a6159c9` (the `origin/main` of the PR #997 review; a second rendering is byte-identical, the runner re-checks it, and a rendering at the observation commit `6c6cc1b00` differs only in its one comment line naming the basis, because every pin and preimage is the same at both). It is copied byte for byte into the run root with the candidate files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/D1_PREMISE_AMEND_{D}/apply_d1p.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/D1_PREMISE_AMEND_{D}/candidates [--with-addon-p] [--check-only]
```

**Failure semantics.**

- **Preflight** (exit 1 before any byte is written): every selected candidate hashes to its postimage; every target (all four, in either mode) holds its preimage; no temporary sibling (`.d1ptmp`) of any target exists; every pinned file hashes as tabled; the run-root guard (a script directory under `projects/pec/` must begin with `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_`).
- **Write.** Each selected postimage goes to a temporary sibling, is hash-checked and renamed over its target. If anything fails after the first write (I/O, hash mismatch, post-write inventory mismatch, pinned-file drift), every replaced target is restored from the preimage bytes read at preflight and re-hashed, every temporary file is removed, and the script exits 1; exit 2 reports an incomplete rollback.
- **Write set.** The script inventories every file under `projects/pec` (path and SHA-256), except its own directory, before and after writing, and requires the difference to be exactly the selected targets, each preimage → postimage, nothing created or removed. In A-only mode the P target must stay at its preimage.
- **Second run** fails preflight. The script never touches `_STATUS.md`, `_REVIEW.md` or `MEMORY.md`.

Check aids (not bound):

| Aid | SHA-256 | Role |
|---|---|---|
| `render_candidates.py` | `a02b468480e41f0bd36d3a74d37543812e8d98ce06caf0dec68be7a8d1026701` | renders each candidate from its premise ledger; check mode proves nothing outside the hunks changed |
| `verify_d1p_quotes.py` | `728832dc73ba9abf02b7b840d191f6ce162c3fa3177bc9fa9bb629033bd4e765` | two-sided quotes at named commits; raw dependency quotes; FORBID "at the basis"; PIN; OBS; MULT |
| `verify_d1p_state_claims.py` | `e6bd6c5a41ac67e597a8e2839802ae71500a13d846ea5ad163634a93f47b2038` | commit-anchored state claims, each also matched in the candidate |
| `check_quote_currency.py` | `c654431455e866bb03b71f3b74e69ef8a47ea621c76c1d31c7f0b9ad02d9d319` | corpus-wide `D-PEC-95` quote currency; target-cited rows |
| `scan_external_quotes.py` | `ab6c914330a6c8a365068e4637b0360d1477cbc5ba92316f96646c95ff25551b` | informational downstream quote and hash-anchor scan |
| `test_apply_d1p.py` | `330087edaebfe73df663fdb3beeb72302e441093c82f7f6b6f34114de1d91094` | fault injection, 24 cases |
| `run_d1p_checks.sh` | `80714ae4a69a8178d7726f095657e8c4297b8babbe9ed86933c2deacd8b0ed8e` | runs rows 2–11 on pre/post exports in both modes, and checks its own stored outputs for trailing whitespace and blank lines at EOF |
| `negative_controls.sh` | `7f2a2195328ee57c6686034da28888ebd936ef599a7c0631d51c76c365010411` | six negative controls |
| `build_apply_d1p.py` / `apply_d1p.template.py` | `27abb5e3ece4ecc9fdb9e33757143b17f7705fd131352e57c248fce57a3ab9da` / `79a532837eca6177f01780be2b2bdf52a7aaa5973d39782e5ca1469edb48e692` | renders the bound script |
| `targets.json` | `1efbc5af6f01736c9b7657b554404560404782aa3f8dab671deae62c11d48aa9` | targets, groups, preimages, commits |

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`, on the act branch; record each command, exit code and output in the run root. `run_d1p_checks.sh` runs rows 2–11 on `git archive` exports and is the rerun method.

| Check | Command | Required result |
|---|---|---|
| 1. Preconditions | ruling and register row on fetched `origin/main`; `apply_d1p.py --check-only` (with `--with-addon-p` if P); `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `CHECK preflight passed`; `ALLOW` everywhere; on any pin mismatch stop and route to the owner (no re-pin is pre-authorized) |
| 2. Ledger rendering | `render_candidates.py --gitdir . --prep <run root>` | `RESULT PASS fails=0` (every candidate equals its ledger rendering) |
| 3. Contract validity | `validate_scope_of_work.py <DEL folder>` for DEL-00-03 (and DEL-00-01 if P) | `PASS format=SOW_V1` |
| 4. Checklist | `derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, twice | exit 0; byte-identical; DEL-00-03 `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1`, DEL-00-01 `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9` |
| 5. Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json … --show-not-checkable <DEL folder>/ScopeOfWork.md` | exit 0; no `UNRESOLVED_OWNER`/`UNDEFINED_CLAIM` (0 `NOT_CHECKABLE`) |
| 6. Quote fidelity | `verify_d1p_quotes.py --tree . --gitdir . --prep <run root> --observation 6c6cc1b00` | `RESULT PASS 74/74` |
| 7. State claims | `verify_d1p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 126/126` |
| 8. Lifecycle and review records preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv'` (on the act commit; under the REVIEW-before-merge variant the later REVIEW commits are checked under their own authorization) | empty |
| 9. Registers and quote currency | `validate_decomposition_registers.py --strict projects/pec/execution` and `check_quote_currency.py`, before and after | outputs identical to the pre-act run (at `6c6cc1b00`: exit 1, 0 errors, 26 `XRG-013` warnings under D-GOV-48; 127/127; target-cited rows 0) |
| 10. Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | exit 0 each; identical before and after |
| 11. Containment | `git diff --name-status origin/main...HEAD` | the three (or four) targets; M's files if selected; the run root and HELP_HUMAN's records under `execution/_Coordination/**` (and `docs/STATUS.md` under `D-PEC-88`); nothing else |
| 12. Whitespace | `git diff --check origin/main...HEAD` (the runner's row 12 pre-checks its own outputs for trailing whitespace and EOF blank lines; this row is the check for the whole run root) | clean, including every file in the run root |

Re-audit: not recommended. The act changes no decomposition truth, register or topology.

### Independent verifier

A separate `MODE=VERIFY` run, read-only on production content, by a TASK that authored nothing; preparation verdicts are in the prep folder (`VERIFIER_VERDICT_*.md`, with the manager's dispositions), and a fresh one runs at the act. It returns a verdict file; defects return to the author. It checks:

1. **Basis.** Ruling and register row on `origin/main`; script hash as bound; pins match.
2. **Byte identity.** Written files equal the tabled postimages, and each equals its ledger rendering from the accepted preimage.
3. **`MODE=VERIFY`** on each Scope of Work target: the mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21).
4. **Premise-only semantics.** Each hunk corrects a premise made false by SCA-005 or SCA-006 (or is its minimal consequence, the uniform note, or the provenance `AX`), cites its cause, and is true at the named commit; nothing outside the hunks changed; history is kept; no ID is retired, reused or added other than the provenance `AX`; nothing is built around verify-before-rely; operational reliance appears only as PRD v2.4 states it; no lifecycle, acceptance or readiness claim; the ADR decision and the owner's AC-007 confirmations stay true.
5. **Coherence.** The amended SPEC satisfies the amended DEL-00-03 contract's `AC-*` criteria that are checkable by inspection; the amended ADR is consistent with DEL-00-01's contract if P is selected (and the conflict is as disclosed if not).
6. **Containment and lifecycle.** As in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act, the checks and, if selected, add-on M at closeout, and runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/D1_PREMISE_AMEND_{D}/`, in the default-writable fence: `apply_d1p.py` (exact bytes), `candidates/`, `premise/`, `quotes/`, `claims/`, `targets.json`, the check aids and all outputs (the runner stores its target diffs as `diff_<KEY>.diff.txt` and its checklist diffs as `checklist_diff_<KEY>.patch`, both with trailing whitespace and trailing blank lines stripped — review aids, not applicable patches — and its row 12 fails if any output it writes carries trailing whitespace or a blank line at EOF; files the runner does not write (`MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, verdicts) are written to pass the same rule, and check 12 is what confirms it); `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`; `VERIFIER_VERDICT_NN.md`. No `_run_records/` entry is written in either deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under `D-PEC-88`. `_Evaluation/**`, registers, dependency files, contexts, references and each deliverable's `_REVIEW.md`/`Review_Findings.csv` stay closed.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high`, unless the owner states otherwise. Role identity is instruction-asserted.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the script leaves every target at its preimage and no temporary file. If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR restores the tabled preimages (and removes M's two files if M ran). No lifecycle state changed. The lapsed acceptances do not revive by themselves: restoring the exact accepted bytes makes the prior acceptance records describe the current bytes again, which the owner may confirm. Under RR2, a rollback also lapses the owner's exact re-acceptance of the new bytes, which then describes superseded bytes. The ruling record and register row are never reverted; a rollback is its own register row and record. The run root stays as non-current evidence with a rollback note. No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + P, A (+ P) + M or an amendment, grants none of the following:

- any lifecycle change or `_STATUS.md` write; `CHECKING` or `ISSUED` acts; any REVIEW gate act, `_REVIEW.md`, `Review_Findings.csv` or `REV_*` write, or pointer move; any artifact acceptance (except an owner `ACCEPT_EXACT_BYTES` the owner states under RR2, recorded by HELP_HUMAN in the ruling); under the REVIEW-before-merge variant, the REVIEW files and acceptance record are written only under the owner's separate REVIEW authorization, never under this grant;
- any `v2/**`, `software-workflow.json`, `docs/PRD.md` or source, fixture or test write;
- any `_Decomposition/**` or `_ScopeChange/**` write or any register write (no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `Dependencies.csv` or `_DEPENDENCIES.md` change), and no action on the D-GOV-48 warnings or on the residual register text in "Other findings";
- any `_CONTEXT.md`, `_REFERENCES.md` or `_SEMANTIC.md` write, or any file of a deliverable other than the tabled targets (the DEL-01-01, DEL-01-05 and other consequences are for their own packets);
- a `## Remaining` entry, a Task Management disposition, an audit run, or an edit of the `D-PEC-99` exhibit;
- a registry, profile or tier-0 act, any tool declaration or invocation, or a resolution of any `CON` item;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- adoption of `scope-of-work` `MODE=REVISE`, of the revised `review` edition, or of any other Root mode;
- a readiness, release, reliance or professional-reliance claim.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A** — the three premise-only replacements in one act, as tabled. Ruling A lets the owner's exact-byte acceptances of the three prior files lapse on their terms (see the account). No review is opened, and no lifecycle transition is asked.
2. **Add-on P — the DEL-00-01 contract.** Include its premise-only amendment (CLM-005, REQ-004, AX-008), so the amended ADR and its contract agree (recommended); or leave it out, accepting the disclosed ADR/contract conflict until a later packet. Add-on P goes beyond the brief's named touch set; it is prepared so the choice can be made in one ruling.
3. **Re-review.** RR1 (recommended), RR2 or RR3, as described under "Acceptance-lapse account". Without an answer, RR3 holds.
4. **Readings the candidates take, for confirmation.**
   - (a) **This reading goes beyond premise-only scope.** SCA-006 §B4 names only CLM-004 L70 and CLM-006 L77 ("the '46 requirements' premise … premise only") for this contract; the reading also changes OUT-002, REQ-001, REQ-002, REQ-003 and AC-003, and the basis and requirement source they resolve against, and AX-009 says so. The DEL-00-03 contract is rebound from revision 1.3 at `11a494e9a` to revision 1.6 at `189f205ff`, with `PRD.md` v2.4 as its requirement source (OUT-002, REQ-002, REQ-003, AC-003, the production sequence) and REQ-001 reading the seed "as brought current to" the bound basis. Grounds: the amended SPEC must name revision-1.6 identifiers and PRD v2.4 requirements, which AC-002, AC-003 and AC-005 would otherwise reject. For comparison: every contract created or rebuilt since SCA-005 (11 of the 36 at `6c6cc1b00`: the `D-PEC-98`, `D-PEC-100` and `D-PEC-103` contracts) pins `189f205ff`, as do the eight `D-PEC-102` candidates; 12 contracts, including both targets, still pin `11a494e9a`. The accepted pair already mixed bases: the 2026-08-09 rerun reviewed against revision 1.4 while the frontmatter bound 1.3, and the accepted SPEC's §6 counts (94: 72/14/8) were revision 1.4 counts while the accepted contract's CLM-005 (71/14/9) gave revision 1.3's. Consequences disclosed: REQ-001 is reworded because of the rebind (it would otherwise read the seed as authored from revision 1.6; the check aid's "at the basis" rule also flagged its old wording, which is not why it changed); REQ-004 still asks for the basis the seed "was born from" (revision 1.3 at `11a494e9a`, stated in the SPEC's "Born from" paragraph), while AC-004/VER-004 compare the stated basis with the rebound frontmatter, which the SPEC's premise-amendment note satisfies by naming revision 1.6 at `189f205ff`; and the basis provenance note's first sentence, stale since the SCA-004 re-pin, is corrected because the rebind restates that paragraph. The SPEC's own "born from revision 1.3" history is kept.
   - (b) The ADRs keep "PEC is an optional client" (no current source says PEC is a Runtime client; it stays accurate as "optional" because the per-application Runtime client seam is deferred behind trigger T-RT, PRD v2.4 §13 and SOW-087, which the amended posture 4 now states), `D-PEC-56` behaviors 2, 4 and 7 (behavior 2 removes credential, session, delegation, interruption and model-residency ownership from PEC's path, consistent with `D-GOV-43` A2; 4 and 7 survive per `D-PEC-58` behavior 8 and PRD §15), and ADR-002's "Sources" line (PRD v2.2 §§4, 10, 13, 15) as the accepted record's provenance, with the amended postures carrying their own current citations; and the DEL-00-01 contract (if P) keeps its revision-1.3 birth basis.

   Recommendation: **confirm both**. Otherwise say which to amend; the affected candidates would be re-rendered from their ledgers.
5. **Add-on M — MEMORY files.** Create the two `MEMORY.md` files at closeout, as tabled (recommended); or record the run only in the graph and central receipt.
6. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran on `git archive` exports in the session scratchpad, never on a checkout. Interpreter: Python 3.13.7 (CPython); local dates 2026-09-26 (preparation) and 2026-09-27 (the final run, after `f0a6159c9`). Final run (`evidence/run_main/SUMMARY.out`, `run_d1p_checks.sh` on exports of `origin/main` `f0a6159c9` with observation commit `6c6cc1b00`; every raw output beside it, except that `scan_external_quotes.out` is the `--no-kept` rendering — its `KEPT` listing, about 43,000 lines, is omitted; the counts and every STALE and ANCHOR line are kept, and the runner reproduces the full file):

```text
PASS apply_d1p.py equals a fresh rendering at its basis f0a6159c9
PASS render_candidates check (RESULT PASS fails=0)
PASS act mode A: check-only 0, apply 0, rerun refuses 1; containment exactly 3 files
PASS act mode AP: check-only 0, apply 0, rerun refuses 1; containment exactly 4 files
PASS validate / checklist (rerun byte-identical) / boundary — DEL-00-03 SOW (modes A, AP), DEL-00-01 SOW (AP)
PASS quotes: RESULT PASS 74/74
PASS state claims: RESULT PASS 126/126
PASS strict / harness / receipts identical before/after, both modes (strict: 0 errors, 26 warnings, exit=1)
PASS dependency quote currency identical, both modes (127/127; TARGET-cited active rows: 0)
INFO external-quote scan: stale=82 anchor=2198 kept=43231 history-anchor=30 (files_scanned=6380)
PASS whitespace (4 candidates)
PASS fault injection: RESULT PASS 24/24
PASS evidence whitespace: 0 file(s) with trailing whitespace or a blank line at EOF
OVERALL PASS
```

Negative controls (`evidence/negative_controls/NEGATIVE_CONTROLS.out`), each of which tripped its check after passing on an undamaged copy: (1) one character changed in the SPEC candidate fails the ledger rendering; (2) a changed quote text fails the quote verifier; (3) a wrong hash fails its state claim; (4) a removed matrix row fails validation; (5) a candidate without the pin fails PIN; (6) a stale postimage hash in `apply_d1p.py` fails `--check-only`. `RESULT PASS negative controls 6/6`.

Preparation artifacts (this prep folder; hashes in `SHA256SUMS`): `candidates/…` ×4; `premise/`, `quotes/`, `claims/` ×4 each; `targets.json`; the bound `apply_d1p.py` and its template and builder; the check aids; `DRAFTER_BRIEF.md`; `evidence/`; `VERIFIER_VERDICT_*.md`.

Basis at `6c6cc1b00` (and at `189f205ff` where noted):

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `9ae4bea2…9665` / `df9196d1…5eb8` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` / `_LATEST.md` (also at `189f205ff`) | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` / `768ae4c4…a771` |
| `docs/PRD.md` (v2.4; also at `189f205ff`) | `ae49b806…3fbe` |
| SCA-005 `Propagation_Plan.md` / `Impact_Assessment.md` / `IMPACT_INVENTORY_PEC_BASIS.csv` | `50cd0b1d…1350` / `0bcbe9bd…39bf` / `f0bba13a…e3bc` |
| SCA-006 `Propagation_Plan.md` / `Impact_Assessment.md` | `f95d00d1…d7d8` / `93253b7d…b691` |
| Work graph | `1ec5719f…1ad8` |
| `D-PEC-99` exhibit | `69b646f8…f45e` |
| Root `docs/DIRECTIVE.md` / `docs/CONTRACT.md` | `b191750c…7fbf` / `510f6a84…3f71` |
| `NOTICE_2026-09-26_REVIEW_SPEC34_REVERSAL.md` (PEC copy) | `30aab470…4168` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `pec_reliance_hold.py` | `f877d931…741cbc` / `b1712e4b…d0e` |
| `MEMORY_TEMPLATE.md` | `5a9564f4…6a5a` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, node D1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with two TASK drafters, one TASK tool builder and fresh read-only reviewers (one per verdict). The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The roles and the `high` reasoning effort are instruction-asserted.
