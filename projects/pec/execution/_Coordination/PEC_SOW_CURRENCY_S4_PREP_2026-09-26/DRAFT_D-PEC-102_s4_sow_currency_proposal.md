# D-PEC-102 — Scope of Work currency for the S4 set (DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04, DEL-04-03, DEL-03-04, DEL-10-03) — proposal

Status: **DRAFT PROPOSAL / AWAITING_RULING**. **The number D-PEC-102 is provisional.** At `origin/main` `b990b0c90` the decision register has no D-PEC-102 row, and two other next-wave packets are being prepared in parallel. The number becomes final only when HELP_HUMAN publishes this packet in `_DECISIONS/` with its register row and moves that row to `AWAITING_RULING`.

Prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S4) for the PEC loop, 2026-09-26 (session date). Brief: `briefs/S4P_SOW_CURRENCY_PROPOSAL.md` (SHA-256 `d00a739afc1f4bc03bd5bd9862fb104d880c22ccce6859dbe85c7e588802dc67`), plus HELP_HUMAN's relayed resume directions (quoted under Provenance). No earlier direction approves this file. It performs no production act: no tracked production file was edited, and every check ran on `git archive` exports. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-102_s4_sow_currency_proposal_2026-09-26.md`.

The act it asks for is bounded: **replace eight existing `ScopeOfWork.md` files with the exact bytes tabled below**, in one run of a bound act script, with no lifecycle change. Add-on M (question 4) is separate.

## Provenance

- **Owner acts relied on.**
  - **Steering.** The owner's 2026-09-25 steering, recorded in `_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (`b6814e90…5a6b`): "You can continue with all the open work you identified." The work graph (`WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`, `8296ad0c…b148` at `125cfacc1`) turns it into node S4, "SOWs whose quoted PRD text SCA-006 changes": READY, R3 met. The row names the eight members and the four Part B carry-forwards.
  - **SCA-006 checkpoint 2** (accepted 2026-09-25; snapshot `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`, register row `D-PEC-97`) accepted `Propagation_Plan.md` (`f95d00d1…d7d8`).
    - Its §B4 fixes the S4 membership: DEL-04-01, DEL-04-02, DEL-08-01, DEL-08-03, DEL-08-04 and DEL-04-03, plus DEL-03-04 and DEL-10-03, which are held from §7.1's "S1 or D1" into S4 as a recorded deliberate choice. DEL-00-03 goes through D1 and is not touched here.
    - §B4 also sets the pass rules this packet follows: one pass per contract for both its SCA-005 and SCA-006 causes; PRD v2.4 and revision 1.6 quoted, never v2.3 text; no contract rebuilt around verify-before-rely; the `D-PEC-95` quote-currency check as an acceptance check.
    - Impact Assessment §7.1 (`93253b7d…b691`) gives the SOW loci.
  - **SCA-006 checkpoint 3** (accepted 2026-09-26; `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/`) made decomposition revision 1.6 `current_basis` with PRD v2.4.
  - **SCA-005 checkpoint 2** (`D-PEC-92`) accepted `SCA-005_2026-09-23_2139/Propagation_Plan.md` (`50cd0b1d…1350`). Its §B4 gives each member's SCA-005 class:
    - `STALE_REBUILD_REQUIRED`: DEL-04-01;
    - `STALE_REVIEW_REQUIRED`: DEL-04-03, DEL-08-01 and DEL-03-04;
    - `STALE_REVIEW_REQUIRED (quotation)`: DEL-08-03 and DEL-08-04;
    - `current`: DEL-04-02;
    - `housekeeping only`: DEL-10-03.

    It also lists the housekeeping fixes: the unresolvable `@3623b958b` pin and the false "`_REFERENCES.md` still names revision 1.1" claim, which apply to DEL-03-04 and DEL-10-03.
  - **`D-PEC-90`** (ruled R-A, 2026-09-25; `D-PEC-90_RULING_2026-09-25.md`, `43a0c663…efab`). Grant item 1: DEL-04-01 and the §8 refresh are not to be rebuilt around verify-before-rely.
  - **`D-PEC-99`** (ruled A, 2026-09-26; `D-PEC-99_RULING_2026-09-26.md`, `3e34403a…c989`) and its act (PR #957, `22502e059`). The exhibit (`D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md`, `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`) carries DEL-04-01-REM-001, DEL-04-01-REM-002, DEL-04-02-REM-002 and DEL-04-03-REM-002 to node S4.
  - **`D-PEC-100`** (ruled A + confirm B + M, 2026-09-26; `D-PEC-100_RULING_2026-09-26.md`, `13690e20…729b`). Its act merged in PR #979 as `125cfacc1` and replaced the seven S2 contracts. The ruling assigns the downstream quotations of old S2 text to "S1, S4 or a later DEL-02-08/09 revision".
  - **`D-PEC-101`** (ruled K4 with C; K1; V; Notes a; defaults — `D-PEC-101_RULING_2026-09-26.md`, `baa4fc09…ba28`). Its act (PR #976, `ce934ac33`):
    - re-pinned the contexts and references to revision 1.6;
    - created DEL-08-06 and DEL-10-13 (`OPEN`, no Scope of Work);
    - added their dependency rows;
    - refreshed DEP-10-03-003.
  - **`D-PEC-96`** (the ruled registry, schema version 2, three feed profiles; `852057f0…399e`).
  - **Precedents:** `D-PEC-100` for an exact-bytes replacement of existing contracts with a bound script and fresh verifiers; `D-PEC-98` (`039dc7e2…8361`) for exact-bytes Scope of Work acts and add-on questions.
- **Brief and resume directions (HELP_HUMAN, relayed 2026-09-26, recorded here as evidence).** The host forced two interim handbacks. HELP_HUMAN then directed, in substance:
  - finish the brief: collect the eight drafter returns, reconcile, render the act script, run the checks on exports at current `origin/main` and confirm no pinned file changed since `125cfacc1`;
  - list, and not change, any S1-owned anchor that goes stale, naming DEL-04-05's citations and quotations of DEL-04-01 and DEL-04-03;
  - disclose the DEL-04-01 `_REVIEW.md` point;
  - loop fresh reviewers; open the PR; do not merge.

  The brief itself directs that `scope-of-work` `MODE=REVISE` adoption is **not** put to the owner.
- **Fence.** `projects/pec/AGENTS.md` (`df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`) §"Write Scopes And Fences": every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the STATUS pointer needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. No earlier ruling opens the eight targets.
- **Source state.**
  - **Observation commit `125cfacc1`** (`125cfacc10f664685cb91802a9166b1041f42a25`, the PR #979 merge). This was `origin/main` when preparation began. Each candidate says that every unanchored state claim is an observation there, and every quotation and state claim in the verifier inputs is read at a named commit, `125cfacc1` or earlier.
  - **Frontmatter pin `189f205ff02df4111b33c20be441ce06e65ada7a`** (SCA-006 checkpoint-3 acceptance, PR #954), an ancestor of `origin/main`. The decomposition, `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv` and `docs/PRD.md` are byte-identical at the pin, at `125cfacc1` and at `b990b0c90`.
  - **Checked again at `origin/main` `b990b0c909e88176c1afcf82ca24623ba8172a40`** (PR #988 merge) after `git fetch`. Since `125cfacc1`, `projects/pec` changed only in:
    - PR #981: the undertaking `WORK_GRAPH.md` and the review transcriptions `REVIEW_PR981_0{1,2,3}.md`;
    - PR #982: the undertaking `WORK_GRAPH.md` again, the retirement undertaking's `WORK_GRAPH.md`, its central `RECEIPT.md`, `REVIEW_PR982_0{1,2}.md` and `docs/STATUS.md`.

    PRs #973 and #984 changed Piping files only; PR #985 changed Root tools, exports and workflows; PR #988 changed App files, exports and one Root tranche manifest. Every preimage and all 19 pinned files hash the same at `125cfacc1` and `b990b0c90`. The act script rendered at each commit is byte-identical, apart from its one comment line naming the commit.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e`) was run from `projects/pec` of a `125cfacc1` export with `--operation exact-correction-preparation` on all 24 possible targets (eight `ScopeOfWork.md`, eight `_STATUS.md`, eight `MEMORY.md`): `ALLOW`, exit 0, ×24 (`evidence/reliance_hold_preflight.out`).

## Method

- **Workflow.** `chirality-root:bundled:workflow:scope-of-work`, resolved from `workflows/index.json` (`2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3`). Precedence is project → user → bundled; no project or user workflow of that name exists.
  - Files: `WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`, `execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`, `resources/checks.md` `44ab41ac…f188`, `resources/tools.md` `fbd07771…5cc7`. `resources/representation-migration.md` (`698957a5…3e3c3`) was not loaded; it covers conversion only.
  - Standard: `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c`.
  - These are the same files the `D-PEC-100` preparation recorded.
- **How the currency pass is made (the `D-PEC-100` practice).**
  - The eight candidates were **authored under `MODE=INIT` discipline**: whole contracts, source-grounded in the accepted revision-1.6 basis, `DECOMP_VARIANT=SOFTWARE`, `STATUS_POLICY=NO_STATUS_TOUCH`, with no evidence candidate, map, parity or finalizer.
  - Every sentence still true and in scope was kept byte-for-byte, so that other contracts' quotations of these contracts stay valid.
  - The recorded edition's `INIT` precondition is that no production contract exists; here all eight exist and validate `PASS format=SOW_V1`. So the act is **an owner-ruled exact-bytes replacement** of each contract, bound by preimage and postimage hashes.
  - **The method's `MODE=VERIFY` is the independent check** of each postimage.
  - Authority for the bytes is this ruling, as it was for `D-PEC-100` and `D-PEC-98`.
- **Disclosure (one line).** Root's `NOTICE_2026-09-26_PROJECT_SETUP_INCREMENTAL.md` (`8829ac84…64af`) added `scope-of-work` `MODE=REVISE`; the owner has deferred adopting it in PEC, and this packet does not use it.
- **What "keeps its meaning" means here.** A kept ID keeps its subject or role. Its rule is brought current to revision 1.6, PRD v2.4 and the ruled records. **No ID is retired in any of the eight contracts**; new IDs are numbered after the highest. Each contract's rebuild-provenance `AX-*` names the prior hash, the causes carried and the kept IDs whose rule changed. The contracts themselves are the full account; the table under "The candidates" is a summary.
- **Rules the drafters followed** (shared brief `DRAFTER_BRIEF.md`, `d795dbca4d182472e39ad12a54257b3d7c5f3fff940b55f2b4c5b088a32fb70d`, in this folder):
  - keep each local ID whose meaning survives, with that meaning;
  - retire and never reuse an ID whose meaning is dropped;
  - keep every `Dependencies.csv` `EvidenceQuote` that cites the contract as a raw one-line substring;
  - keep externally cited IDs;
  - keep externally quoted text byte-for-byte unless it is now false;
  - cite a sibling S4 obligation by qualified ID against the sibling's **postimage** (all eight land together), never by quoting it;
  - pin every quotation and state claim to a named commit.
- **Actors.**
  - Eight Type 2 TASK drafters, one per deliverable, in one authoring round.
  - WORKING_ITEMS reconciled the eight and made the wording corrections listed under "Cross-candidate coherence". It also bound the act, extended the check aids (a multiplicity rule in the quote verifier, external-citation and heuristic scans) and ran the checks.
  - Fresh read-only `pec-reviewer` TASKs, one per verdict, ran `MODE=VERIFY` and the packet review (`VERIFIER_VERDICT_01.md` onward): verdicts 01–03 on all eight candidates and the packet (two FAIL, one blocking finding each, both repaired; one PASS WITH NOTES), verdicts 04–05 re-verifying the repairs (PASS WITH NOTES, nothing blocking), and verdict 06 on the final bytes.
  - Models: Opus 5.5 (`claude-opus-5-5`) at `high` for every actor, per the brief.
- **Tools** (`tools/scope_of_work/`, unchanged at `b990b0c90`): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py` `61a34722…0389`.

## What preparation found

### Scope and lifecycle

- **Eight deliverables, exactly the checkpoint-2 set.** DEL-00-03 is not touched here; it is `CHECKING` and goes through D1.
- **Lifecycle: all eight are `INITIALIZED`** at `125cfacc1` and at `b990b0c90`; each `_STATUS.md` was read. None is `CHECKING` or `ISSUED`.
- **What the method does to `_STATUS.md`: nothing.** `WORKFLOW.md` says: "Do not modify `_STATUS.md`, lifecycle state, underscore control files, …". `resources/checks.md` item 3 requires "`_STATUS.md` is byte-identical and its lifecycle state is unchanged".
  - The standard (§8) defines `INITIALIZED` as the selected production contract existing and validating. Each postimage validates, so the condition that made each deliverable `INITIALIZED` still holds after the act.
  - **No transition is proposed.** The act script refuses to run if any `_STATUS.md` differs from its pinned bytes.
- **DEL-04-01's review evidence (disclosed).** DEL-04-01's folder holds `_REVIEW.md` and `Review_Findings.csv`: an owner-opened `PEER_REVIEW` of 2026-08-09, gates 1–4 complete, Gate 5 not entered, with RF-001 and RF-002 `RESOLVED` by a bounded repair to the prior contract (`6f4e8c66…30ae`).
  - That review evidence concerns the prior bytes. After this act it describes a superseded contract, and it is not evidence about the postimage. The repaired content of those findings (CLM-008's evidence cells, CLM-009's upstream state) stays true in the postimage (re-checked at `125cfacc1`).
  - This packet claims, changes and prompts no review state. `_REVIEW.md` and `Review_Findings.csv` are not written.
  - Whether a later review of the new contract is wanted is an ordinary later steer; nothing here opens or closes one.

### The candidates

| Deliverable | Classes (SCA-005 / SCA-006) | Prior contract | Postimage | Lines | Defined IDs | Retired | Checklist items | Quotes / claims |
|---|---|---|---|---|---|---|---|---|
| DEL-04-01 | rebuild / AFFECTED (fixed member) | `6f4e8c66a571…30ae` | `98a3a3ec2273…71a0` | 510 | OUT 2, CLM 23, REQ 18, AC 19, VER 18, AX 15, TBD 5, CON 8 | none | 19 | 148 / 202 |
| DEL-04-02 | current / AFFECTED → review | `a2b50f870aa3…e65a` | `bcd69f503acf…6b11` | 446 | OUT 2, CLM 18, REQ 15, AC 16, VER 15, AX 15, TBD 4, CON 8 | none | 16 | 99 / 158 |
| DEL-08-01 | review / AFFECTED → rebuild | `8ac1dc050efb…3d76` | `b8c021f58144…5e01` | 227 | OUT 3, CLM 11, REQ 9, AC 9, VER 7, AX 10, TBD 4, CON 3 | none | 9 | 32 / 161 |
| DEL-08-03 | review (quotation) / AFFECTED → rebuild | `013c615a0c91…3138` | `d4bb8ffa475a…81bf` | 462 | OUT 3, CLM 14, REQ 20, AC 21, VER 20, AX 13, TBD 6, CON 7 | none | 21 | 94 / 135 |
| DEL-08-04 | review (quotation) / AFFECTED (quotation) | `6d1ec1ad9796…222b` | `16d731a51556…404c` | 442 | OUT 2, CLM 17, REQ 13, AC 16, VER 14, AX 14, TBD 4, CON 8 | none | 16 | 73 / 74 |
| DEL-04-03 | review / AFFECTED → rebuild (new obligation) | `6ec7432bf8cf…ec6d` | `10819cb2ea90…7e18` | 443 | OUT 2, CLM 22, REQ 23, AC 23, VER 22, AX 13, TBD 5, CON 6 | none | 23 | 96 / 153 |
| DEL-03-04 | review / AFFECTED (review level) | `e007f5307fce…4e02` | `5f7bd434694c…196f` | 423 | OUT 2, CLM 17, REQ 16, AC 19, VER 16, AX 12, TBD 5, CON 7 | none | 19 | 100 / 133 |
| DEL-10-03 | housekeeping / AFFECTED (review level) | `cbcabbde6882…6ff8` | `e0df75bdcbde…9865` | 463 | OUT 1, CLM 16, REQ 15, AC 12, VER 10, AX 12, TBD 5, CON 4 | none | 12 | 78 / 128 |

What each pass changes, in brief (the contracts and their provenance `AX-*` are the full account):

- **DEL-04-01 Loop orientation return (rebuild).**
  - **SCA-006.** `CLM-016` and `AX-007` drop verify-before-rely and state PRD v2.4 PEC-K-03 and the §8 Agents bullet: a harness, or an agent through the tool-call surface of DEL-08-06 under the `agent` class. Operational reliance is available only from a release past the §12 gate, and is never authority.
    - New `CLM-023` and `REQ-018`: the return is the content the reliance envelope qualifies; it carries the envelope's inputs and declares no envelope (the envelope is DEL-04-03's under SOW-097).
    - `REQ-011` adds the tool-call and size-budget exclusions.
  - **SCA-005.** SOW-004 and PEC-ORI-001 are re-sourced at revision 1.6. **Seven components**: terminal completion from local Git merge reachability is added to `REQ-001`, which now reads "no eighth".
    - New `REQ-016`: terminal completion is advisory, Explain-shaped, with unresolved PRs stated. New `REQ-017`: node state is declared activity, never liveness, with generation labels.
    - Per-component feed availability under the ruled registry (`CLM-019`); no Remaining section read (`CLM-021`).
    - `CON-001`/`CON-002` re-derived; new `CON-005` to `CON-008`.
  - **S2 currency.** DEL-01-01's sixteen types, its changed `REQ-007`/`REQ-008`, and the receipt-contract-v2 marker.
  - **Part B**, below.
- **DEL-04-02 Delta service since SHA (review level).**
  - `CLM-016` drops verify-before-rely and "names possible consumers only at one remove". It quotes the §8 Agents bullet and the `agent` class, whose reads include deltas.
  - `REQ-013` names both request paths. `REQ-007`/`REQ-010`/`REQ-011` add the envelope, budget, tool-call and gate exclusions.
  - New `CON-006`: the envelope over a difference, routed to DEL-04-03's production declaration. New `CON-007`: continuation over a delta, routed to DEL-08-03's declaration and the Phase 1 confirmation. New `CON-008`: no edge from DEL-08-06, routed to K2 or a dependency packet.
  - Part B DEL-04-02-REM-002 is applied, below.
- **DEL-08-01 Unix-socket server + token-scoped access (rebuild).**
  - The class set becomes **owner, harness, agent, admin**. New `REQ-008`: `agent` is read-only query; ingest, presence reports, admin acts and writes are refused, with no partial result.
  - PEC-API-001 is re-quoted with its D-GOV-43 A2 wording (`REQ-005`'s second sentence). OI-006 / §16.6 is re-expressed, including `agent` credentials. SOW-083 is re-quoted.
  - New owners are named: DEL-08-06, DEL-10-13, DEL-04-03 (SOW-097), DEL-08-03 (SOW-098). The §B6 tier-0 profile act is stated as not this deliverable's.
  - New `CON-003`: whether PRD §8's agent read list is exhaustive.
  - `OUT-001` is byte-identical, so the two dependency quotes stay verbatim.
- **DEL-08-03 Compact citation-bearing response format (rebuild).** Scope grows by **SOW-098**, and `project_scope_refs` becomes `[SOW-043, SOW-098]`.
  - The false "no accepted source states a size metric …" is removed.
  - `REQ-014` to `REQ-017`: a declared size budget per response; pagination or continuation pulled only on request; nothing (citations, stamps, limitations, envelope elements) dropped; truncation stated. Numeric budgets wait on a recorded Phase 1 confirmation (`CON-006`).
  - `REQ-018`: the tool-call surface returns the same format. `REQ-019`: boundary. `REQ-020`: carries the reliance envelope without deciding its structure (`CON-007`).
  - New `CON-005`: response set, orientation only or every API response.
  - `REQ-010` is byte-identical. `OUT-002` keeps the DEP-08-04-004 quote, with two qualifying sentences after it.
- **DEL-08-04 Orientation latency budget (quotation pass).**
  - Four access classes. Response-size budgets are DEL-08-03's under SOW-098 and distinct from the latency budget (SOW-098 Notes).
  - The §12 P1 row is confirmed unedited; the standing gate names no latency proof.
  - Fifteen blockquoted sibling records are replaced by qualified citations. The stale PRD §7.1 "D-APP-57 contract" text is removed.
  - The register evidence columns are stated as repaired under `D-PEC-65` and refreshed under `D-PEC-95`.
  - New `CON-007`: whether ≤100 ms applies per page or per continued sequence. New `CON-008`: whether the bound reaches tool-call reads or a given access class.
- **DEL-04-03 Citation and freshness stamping (rebuild, new obligation).** Scope grows by **SOW-097**, and `project_scope_refs` becomes `[SOW-006, SOW-007, SOW-097]`.
  - `REQ-016` to `REQ-023`: the reliance envelope (pin, per-feed coverage and freshness, per-claim trust tier, file-fallback signal) on every response kind, beside the three-field stamp and **not a stamp field** (`CLM-019`, from the SOW-097 Notes "distinct from SOW-006 stamping"). Its pin equals the stamped SHA. Reliance is bounded, never authority, and never advertised without the §12 gate. Each element is declared in the derivation record.
  - `CON-003` is re-derived from PRD v2.4 PEC-RCN-002 (closed feed profiles; `adapter.yaml` is not the feed manifest) and the ruled registry (`CLM-022`).
  - New `CON-005`: when the file-fallback signal fires. New `CON-006`: presence-tier facts against universal citation.
  - `REQ-001`, `REQ-005`, `REQ-008` are byte-identical. Part B DEL-04-03-REM-002 is applied, below.
- **DEL-03-04 Practitioner-harness parity diff (review level).**
  - New `CLM-017` quotes the PRD v2.4 §12 standing reliance-advertisement gate, which now requires "parity with the practitioner harness clean, or each difference explained by a recorded DriftFinding disposition (PEC-RCN-005)".
  - `CON-001` and `CON-002` are restated: what the gate fixes, and what stays open — whether the verdict binds releases that advertise nothing, how DEL-10-13 consumes it, and what a disposition is and who records it.
  - New `CON-007`: DEL-02-07's divergence findings as a third DriftFinding producer, keeping `CON-004` byte-identical for its two external citations.
  - The P1 row, TBD-003 parity set and SCA-005 residue are brought current. Housekeeping: the frontmatter pin replaces `@3623b958b`, and the false revision-1.1 claim is removed. `CLM-016` corrects `OPEN` to the observed `INITIALIZED`.
- **DEL-10-03 No-ruling-write verification (review level).**
  - `CLM-008`'s three-class paraphrase is replaced by the four-class set. New `REQ-013` to `REQ-015`: probes under the `agent` class; once the tool-call surface exists it is evaluated as `agent` requests, and while absent it is reported "not present", never passed.
  - `AX-011`: a passing run is never authority or a reliance advertisement.
  - Housekeeping: pin and revision-1.1 claim.
  - Observed staleness corrected: DEL-08-02 is `CHECKING`, and `v2/contracts/api/v1/schema.json` exists (`0a4e4273…5c67`).
  - New `CON-004`: tool-call enumeration; whether a scratch-fixture exercise counts as invocation under the tier-0 gate.

### SCA-006 pass rules, as applied

- **PRD v2.4 and revision 1.6 only.** Every PRD quotation is read at `125cfacc1`, where `docs/PRD.md` is v2.4 (`ae49b806…3fbe`). No v2.3 text that SCA-006 changed is quoted as current.
- **No verify-before-rely rebuild.** "verify-before-rely" occurs in the postimages only as a quotation of the prior text or of `D-PEC-90`, or in a statement that the contract is not built around it. Operational reliance is stated as available only from a release past the PRD §12 gate. It is never authority, and it is distinct from the reliance-hold control and from professional reliance (`projects/pec/AGENTS.md`).
- **Quote currency (the `D-PEC-95` carry-forward).** The corpus-wide check (`check_quote_currency.py`, the rule of `gen_d95.py` step 3) gives 127/127 ACTIVE EXECUTION quotes verbatim, identical before and after the act. The three rows that quote an S4 contract stay verbatim: DEP-08-04-004 quoting DEL-08-03, and DEP-08-04-006 and DEP-08-05-005 quoting DEL-08-01.

### `D-PEC-99` Part B landing

| Item | Kind | Where it lands in the postimage | Local IDs that implement it |
|---|---|---|---|
| DEL-04-01-REM-001 | production obligation | DEL-04-01 subsection "### Carried production obligations (D-PEC-99 exhibit Part B)" L273. `CLM-020` L275; gates-still-bind statement L277; the "S4 packet clause" paragraph verbatim L281; Gate line verbatim L283; own-voice mapping L285 | OUT-001, REQ-001, REQ-004, REQ-005, REQ-006, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, CLM-002, CLM-015, TBD-004 |
| DEL-04-01-REM-002 | production obligation | clause verbatim L289; Gate line verbatim L291; mapping L293. The three added verification sentences verbatim in the Praxeology opening, L421–425 | OUT-002, REQ-015, AC-015, VER-013, VER-015 |
| (both) | trace required by the clauses | trace table L297–344: every prior `REQ-001..REQ-015`, `AC-001..AC-016` and `VER-001..VER-015` (46 rows) maps to the same kept ID, with what changed. No removal is claimed, so no owner ruling removing one is needed | — |
| DEL-04-02-REM-002 | documentary correction (5 parts) | (1) opening L19, verbatim, followed by own-voice qualifying sentences L20–24; (2) `CLM-008` L172; (3) `CLM-008` L174; (4) `AX-010` L381; (5) `AC-016` L307 and the matrix row L446. The E-P33 exhibit quotation and the `[E-P26]` sentence are unchanged. `AX-014` (L385) names the item absorbed and quotes its Gate line (L389) | opening, CLM-008, AX-010, AC-016, AX-014 |
| DEL-04-03-REM-002 | documentary correction (3 parts) | (1) opening L20 verbatim, with own-voice qualifying sentences L21–25; (2) both `CLM-010` replacements L213; (3) `AX-010` L383. The E-P34 exhibit block (prior L170–178) is unchanged at L215–223. `AX-013` quotes the Gate line (L388) | opening, CLM-010, AX-010, AX-013, AC-015 |

- **Verification of the landing.** The quote verifier checks each carried paragraph, each Gate line and each replacement text against the exhibit at `125cfacc1` (both sides). It requires two occurrences of the two identical DEL-04-01 Gate lines (the `MULT` rule), so one copy cannot satisfy both.
- **Gates.**
  - The two DEL-04-01 gates **still bind** at the destination. Production of any source, test or fixture stays gated on a separate exact owner-ruled DEL-04-01 production packet on `origin/main` opening the named source and test paths, acts, verification and rollback under F-PEC-1, after WORKING_ITEMS activation and a current reliance preflight. Upstream sequencing (DEL-10-01, DEL-01-01, DEL-03-01) stays as the register records it.
  - The two documentary-correction gates ("owner accepts exact bounded documentary wording and authorizes only the named current-source paraphrase loci …") are met, if the owner rules A, **only for the replacement texts tabled here**.
- **Facts re-verified at `125cfacc1` before applying the corrections.**
  - The DEP-04-02-003 and DEP-04-03-004 cells: `docs/PRD.md`; `PEC-RCN-003` / `PEC-ORI-003` with their full quotations; repaired under `D-PEC-65` at `1c50d4da6`.
  - PEC-RCN-003 and PEC-ORI-003 are unchanged in PRD v2.4.
  - Revision 1.6 is `current_basis`. Revision 1.3 was accepted 2026-07-28 at merge `11a494e9a`.
- **One imprecision, disclosed rather than edited.** Correction (1) for DEL-04-02 and for DEL-04-03 says each contract "was authored against revision 1.3". The first bytes of each (`fb6442f47`, 2026-07-25) cited revision 1.2, and the revision-1.3 bytes are the 2026-07-28 reconciliation at `ea6b4b5d0`. Each candidate keeps the exhibit text verbatim and adds qualifying sentences backed by claims.

### Cross-candidate coherence and external anchors

- **Siblings cite postimages.** Every qualified citation of one S4 deliverable's ID in another S4 candidate, and every qualified citation of an S4 ID from a contract outside S4, resolves to an ID defined in the postimage: `check_sibling_ids.py` gives `RESULT PASS 57/57` (sibling and external). No candidate quotes a sibling's text or contains a sibling's postimage hash.
  - External citations checked:
    - `DEL-04-01/REQ-001` and `/REQ-006` (from DEL-04-05);
    - `DEL-04-03/REQ-001`, `/REQ-008` and `/CON-003` (from DEL-04-05);
    - `DEL-03-04/CON-004` (from DEL-01-01 and DEL-02-07).
- **Manager reconciliation and repairs (WORKING_ITEMS wording corrections after the drafters returned and after verdicts 01–05; each is in the round-1 → final diff):**
  - DEL-04-03 `CLM-011` no longer says DEL-04-01 "counts six components at `125cfacc1`". It cites the postimage's `DEL-04-01/REQ-001`, terminal completion included. Claim S125 was withdrawn and S026 re-anchored.
  - Four `CON` items that said they "resolve in the [sibling] contract" now say what the sibling postimage obliges and route the remainder to that sibling's production declaration, except where the sibling reserves a question for the owner:
    - DEL-04-01 `CON-008`: `DEL-04-03/REQ-016`..`/REQ-020`, `/TBD-005`, `/REQ-023`, and `DEL-08-03/CON-007`; whether a stated absence or limitation is a fallback condition is `DEL-04-03/CON-005`, left to the owner;
    - DEL-04-02 `CON-006`: `DEL-04-03/REQ-016`, `/REQ-017`, `/TBD-005`, `/REQ-023`;
    - DEL-04-02 `CON-007`: `DEL-08-03/REQ-015`, `/TBD-005`, `/CON-006`; a declaration that needs a continuation position conflicts with DEL-04-02 `REQ-010`, and the contract is then revised under its own packet;
    - DEL-08-03 `CON-007`: its first two questions, and the signal's vocabulary and declared conditions, to `DEL-04-03/TBD-005` and `/REQ-023`; whether PEC's absence has a response-borne form, and what counts as degraded or failing, is `DEL-04-03/CON-005`, left to the owner.
  - After verdicts 01–05:
    - DEL-04-02 says **seven** `PEC-ORI-001` components in `CLM-015`, `REQ-011`, `AC-011` and `AX-008`;
    - DEL-04-03 adds the revision-1.2 first-bytes sentence;
    - DEL-04-01 `AX-014` says how siblings are cited;
    - DEL-08-03 `REQ-018` (with `AC-019`, `VER-018`, the matrix row, `OUT-003` and `REQ-012`) is one format for the responses it applies to, uniform across consumer paths, with no access-class clause;
    - DEL-08-03 `CLM-011` says the string search is case-sensitive;
    - DEL-08-03 `REQ-011` and DEL-08-04 `REQ-012` cite their owner claims;
    - DEL-08-04 `CLM-007` and `CON-004` add `DEL-04-01/CON-001`;
    - DEL-08-01 `CON-003` says a decided read list binds only through a revision of `REQ-008`/`AC-008`;
    - DEL-10-03's framing sentence no longer says "this run's brief".
- **Interfaces the eight now state consistently:**
  - access classes owner, harness, agent, admin, with `agent` read-only (DEL-08-01 `REQ-003`, `REQ-008`);
  - the reliance envelope declared by DEL-04-03 (SOW-097), carried by DEL-08-03's format, tested by DEL-10-13;
  - response-size budgets DEL-08-03's (SOW-098), numbers at Phase 1, distinct from DEL-08-04's latency budget;
  - the tool-call surface DEL-08-06's (P3), with the tier-0 profile act before any tool is declared;
  - the §12 gate record DEL-10-13's;
  - DEL-04-01's seven-component return.
- **Dependency quotes.** The three ACTIVE rows whose `EvidenceFile` is an S4 contract keep their `EvidenceQuote` as a raw substring of the postimage: DEP-08-04-004 in DEL-08-03 `OUT-002`; DEP-08-04-006 and DEP-08-05-005 in DEL-08-01 `OUT-001`. No register is written.
- **S2 quotation currency.** The heuristic scan (`scan_s2_quotes.py`, prior S2 bytes at `ce934ac33`) finds **no** stale quotation of old S2 text in the postimages (`stale=0`; two kept spans of DEL-01-01 text the postimage still carries). Against the preimages it finds two: DEL-04-01's quotation of the prior DEL-01-01 `REQ-008` (per-loop field availability, now per grammar) and DEL-08-04's PRD §7.1 "D-APP-57 contract" text. DEL-04-01 also quoted DEL-01-01's prior "fourteen record-tier entity types". The drafters also searched their own contracts beyond the scan.
  - Of the fifteen contracts outside S2 that `D-PEC-100` said quote old S2 text (thirteen, plus DEL-02-08/09), **DEL-04-01, DEL-04-02, DEL-08-04 and DEL-10-03 are S4 members and are brought current here**. DEL-10-03's flagged span was a scanner artefact (the deliverable's own `_DEPENDENCIES.md` text), and so were DEL-04-02's two flags (its own CLM-006 text, and its own CLM-008 recital of the pre-`D-PEC-65` `DEP-04-02-003` cells, which Part B correction (2) replaces).
  - The others belong to S1 or a later packet.

### Consequences outside this packet (disclosed; nothing here writes them)

- **Quotations of S4 contract text in other contracts that stop being verbatim.** Verified by the drafters and the manager against the postimages; the heuristic `scan_external_quotes.py` output is in `evidence/run_main/scan_external_quotes.out`. Each is listed and **not** changed.

  | Quoting contract (owner node) | Quotation | Why it goes stale |
  |---|---|---|
  | DEL-04-05 `CLM-013` (S1, prepared in parallel) | DEL-04-01 `REQ-001` and `CON-004` quoted in full; its own consequence text "six components, no seventh added" and its `CON-003` | `REQ-001` now carries seven components (terminal completion, per revision-1.6 SOW-004 and PEC-ORI-001) and "no eighth"; `CON-004` says "seven stated absences". DEL-04-01 `REQ-006` is byte-identical |
  | DEL-04-05 `CLM-012` (S1); DEL-04-05 `CON-003` | DEL-04-03 `CON-003` quoted in full; DEL-04-05's own premise that neither the composing nor the stamping contract states where a response-level limitation statement lives | `CON-003` quoted v2.2-era PEC-RCN-002 text ("`_harness/adapter.yaml` as the feed manifest"), false under PRD v2.4, and is re-derived. The premise may go partly stale: the new DEL-04-03 `REQ-018` has the envelope carry, per feed, whether a limitation is stated. DEL-04-03 `REQ-001`, `REQ-005` and `REQ-008` are byte-identical |
  | DEL-10-11 `CLM-014` (no current node: SCA-005 `current`, SCA-006 NOT_AFFECTED; suggested for the work graph as a later DEL-10-11 currency item) | DEL-03-04 `CON-001` and `CON-005` quoted in full | `CON-001` is an SCA-006 locus restated against the §12 gate. `CON-005` said DEL-01-05 "records the toolchain as undetermined", which is false (`DEL-01-05/TBD-003..005`). DEL-10-11's other quotations of DEL-03-04 (`REQ-003`, `REQ-007`, `REQ-013` in `CLM-013`; `CON-004`, `TBD-005`) stay verbatim |

  - Kept, no consequence: DEL-10-02 `CLM-012`'s quotations of DEL-10-03 `REQ-007` and `OUT-001`, which are byte-identical. (DEL-10-02 already renders `OUT-001`'s double quotes as single quotes, a pre-existing inexactness.)
  - Within S4, DEL-08-04's and DEL-04-03's prior quotations of DEL-08-01, DEL-08-03 and DEL-04-01 are replaced in their own postimages by qualified citations, so they land together.
  - **Recommended ordering:** rule S4 before the S1 packet is finalized, so S1 can absorb the DEL-04-05 anchors at its own basis. If S1 is ruled first on the current S4 preimages, its DEL-04-05 quotations of DEL-04-01 `REQ-001`/`CON-004` and DEL-04-03 `CON-003` go stale when this act lands.
- **Stale text found in passing outside the eight** (reported, not repaired):
  - DEL-01-05 `CLM-009` quotes superseded PEC-API-001 text ("D-GOV-20's no-TCP-control-listener posture"), and its `CON-001` quotes the old SOW-083 statement (S1).
  - DEL-01-03 quotes the old §12 P1 row "for one loop (piping or root)" (S1).
  - DEL-08-02 (`CHECKING`) quotes an abridged revision-1.2 OBJ-001 row; only its owning workflow can change it.
  - DEL-04-02's `_DEPENDENCIES.md` view does not mention the `D-PEC-65` repair; it makes no false claim.
  - The work graph at `125cfacc1` still showed S2 "awaiting merge". PR #981 has since updated it.
- **Open items the owner may want to see** (each carried as a `CON` or `TBD`, none resolved):
  - DEL-08-01 `CON-003`: whether PRD §8's agent read list is exhaustive; to K2 or a later scope change.
  - DEL-04-03 `CON-005`: file-fallback trigger; to DEL-10-13's first Scope of Work (K2) or a scope change.
  - DEL-04-03 `CON-006`: presence-tier facts against universal citation; to a scope change.
  - DEL-03-04 `CON-001`/`CON-002`/`CON-007`: parity gating beyond the §12 gate, "explained", the third DriftFinding producer.
  - DEL-08-03 `CON-005`/`CON-006`: response set; who confirms numeric budgets at Phase 1.
  - DEL-08-04 `CON-007`/`CON-008`.
  - DEL-04-02 `CON-008` and DEL-10-03 `CON-004`: no dependency edge from DEL-08-06; to K2 or a dependency packet.
- **Relation to K2 and the tier-0 act.** Several `CON` items name DEL-08-06's or DEL-10-13's first Scope of Work (graph node K2) as a place they may resolve. This packet writes nothing for K2 and cites those deliverables only by register row. No tool is declared or invoked, and the SCA-006 §B6 tier-0 profile act stays a precondition before any agent tool-call tool is declared.
- **Other records.** The eight `_CONTEXT.md`/`_REFERENCES.md` already name revision 1.6 (`D-PEC-101` K4). The `D-PEC-99` exhibit's Part A currency notes cite prior-contract line numbers; the exhibit is not edited, by rule. No ID is retired, so every Part A linked-ID list still resolves.

## Options

- **A — replace the eight contracts with the tabled bytes in one act, no lifecycle change (recommended).** **8 product paths, all modified**; nothing created or removed; no `_STATUS.md`, `_REVIEW.md`, register, context, reference, dependency or `MEMORY.md` file touched. Add-on M (question 4) is independent.
- **A + M** — as A, plus the add-on M `MEMORY.md` files at the undertaking's closeout (8 created files).
- **Amend** — for example:
  - drop a deliverable (the candidates cite one another's postimages, so dropping DEL-04-01, DEL-04-03, DEL-08-01 or DEL-08-03 requires re-drafting siblings that cite them);
  - rule the seventh component out of DEL-04-01 `REQ-001`;
  - change a requirement;
  - resolve a `CON` now.
- **Defer** — nothing opens. P1 orientation, API and gate work waits on these contracts, and DEL-04-05's S1 currency meets moving anchors.

A per-deliverable split with the current bytes is not offered: the candidates are reconciled to land together. A split that writes contracts without their open items is not offered either: the method requires substantive ambiguity to be marked `CONFLICT`.

## Exact product grant

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once**.

- This ruling is the authority for the eight replacements, as the `D-PEC-100` ruling was for its seven.
- The scope-of-work workflow has no mode PEC has adopted that overwrites an existing contract. It supplies the authoring discipline (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`) and the independent `MODE=VERIFY`.
- Paths are relative to `projects/pec/execution/`.

| Deliverable | Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|
| DEL-04-01 | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae` | `98a3a3ec227380db2dd030c9c1ca31535d67071a44a3b79508ab4566b32771a0` |
| DEL-04-02 | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` | `a2b50f870aa30fb45e06b1f4cf1b300ff522a19490066c1e2d898b9022c0e65a` | `bcd69f503acf308e2ef7e73cc722efd61b59710877a5561624260aad71736b11` |
| DEL-08-01 | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` | `8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76` | `b8c021f581448d1ff5413938563d40b015672aefede15ed97da9dd9b92865e01` |
| DEL-08-03 | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` | `013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138` | `d4bb8ffa475a7165a00f4d383a210f3d232dd16af3a971b87d9c1bad77cf81bf` |
| DEL-08-04 | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` | `6d1ec1ad9796973656d6d0d60739b4dbf8cd134a2b17c8c878ee2ff4c098222b` | `16d731a51556cb644220c2c532696d8d0144972e20576db29495e200a775404c` |
| DEL-04-03 | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md` | `6ec7432bf8cfe86cc973c50b8c2a24a0305c55c7a64522d0c47778050e59ec6d` | `10819cb2ea90c7663a51bfc400d44e50a0d688325935d30472c8f29e3f087e18` |
| DEL-03-04 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md` | `e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02` | `5f7bd434694c8a87bba512ba74a8b8f2dee4f5e2a0ab10e5a50c234e432b196f` |
| DEL-10-03 | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/ScopeOfWork.md` | `cbcabbde6882baf5330e90cdd6e1cf4a9d9aa1da076643a27f84ff4cb7696ff8` | `e0df75bdcbdeaa2ecd0c320a3c36082c7c47551f2f514392856c761a96b99865` |

The postimages are the exact candidate files, copied byte for byte into the run root as `candidates/…`. They have no date slot.

Read-only files the act re-verifies and never writes (SHA-256 at `125cfacc1`, equal at `b990b0c90`; the first five also equal at the pin `189f205ff`):

- `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`
- `projects/pec/execution/_Decomposition/Deliverables.csv` `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`
- `projects/pec/execution/_Decomposition/ScopeLedger.csv` `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`
- `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c`
- `projects/pec/docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`
- `projects/pec/AGENTS.md` `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e`
- `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_STATUS.md` `41510909e60227808ff0e4b597603dea2eb8f28703cf2359b0b6058afe94ac31`
- `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_STATUS.md` `d876ae1a5ce679209baa0cf19b82e86f66d83d1f5608550b2a9d2faa60f2abad`
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_STATUS.md` `ac61a8db734b2767627d412cab419bf801b7382e0ba840b88e546445b8b4262d`
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_STATUS.md` `88cf8d11cbfc39375ce929f83b2a1080e3b322e7edc34d1f58ab6ed2fbe5f2ec`
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_STATUS.md` `fc3c58ad3ac877cdcef616aae75b31f26878c8f93b8ae319fbd520a4e0d33054`
- `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_STATUS.md` `c8a82497502085ba69b65dae496e8bfedaeff4d7129c35502416952718d4af34`
- `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_STATUS.md` `ec35873b5b95a4e1f6dee31f9abd34b2f9ddf5403b0c85b8ce0e1a6014f2573a`
- `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_STATUS.md` `ab9646cb68e4226a4d39e737a4a23c8ca28d563d9045c12c3cb5c88fd3f8e1fb`
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/Dependencies.csv` `4438197af5d66b5ebb642222547d9e9d2b40ffe7294cac7e52342badc99dc76d` (DEP-08-04-004, DEP-08-04-006)
- `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/Dependencies.csv` `1eb7eccf2f5390e7280711ae3cf56b71256787407ac8b56fb71c97a049a081d9` (DEP-08-05-005)
- `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/Dependencies.csv` `1ad180b4a85c0187458630da636c328344a841492a1c04750e675b7a1a96ae8d` (the cells correction DEL-04-02-REM-002 restates)
- `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/Dependencies.csv` `0d479ce3a539844a5387edc8c680b83c704b77ff1e1b6ae11c6c4c2984023518` (the cells correction DEL-04-03-REM-002 restates)

### Add-on M — MEMORY files (only if question 4 selects it)

None of the eight folders has a `MEMORY.md` at `125cfacc1` or at `b990b0c90`. At the undertaking's closeout (graph node M1), WORKING_ITEMS creates, under `PKG-…/1_Working/<DEL folder>/`, eight files. Each is `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a`) with `{{DEL-ID}}` replaced and exactly one `## Runs` row.

| Deliverable | Path | Preimage | Act |
|---|---|---|---|
| DEL-04-01 | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/MEMORY.md` | absent | created from the template |
| DEL-04-02 | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/MEMORY.md` | absent | created from the template |
| DEL-08-01 | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/MEMORY.md` | absent | created from the template |
| DEL-08-03 | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/MEMORY.md` | absent | created from the template |
| DEL-08-04 | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/MEMORY.md` | absent | created from the template |
| DEL-04-03 | `PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/MEMORY.md` | absent | created from the template |
| DEL-03-04 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/MEMORY.md` | absent | created from the template |
| DEL-10-03 | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/MEMORY.md` | absent | created from the template |

The row, in every file:

```text
| HELP-HUMAN-PEC-20260925-POST-SCA005 / {D} | Scope of Work brought current under D-PEC-102 (graph node S4). | <link to the central receipt>; PR #{PR}; <link to the D-PEC-102 ruling record> |
```

The slots `{D}`, `{PR}` and the two link targets are fixed at closeout (and "D-PEC-102" follows the final number). The verifier checks that no other byte departs from the template.

## Generation method (binding)

The eight postimages come from one run of `apply_s4p.py`, **SHA-256 `2b6792fee7b69266ad28f517734f89f9c01b60c6e6d4489118fd14375f364869`**. It is stdlib-only Python, prepared with CPython 3.13.7, rendered by `build_apply_s4p.py` from `apply_s4p.template.py` (the `D-PEC-100` script with the targets, pins, temporary suffix `.s4ptmp` and run-root prefix changed). It is copied byte for byte into the run root with the eight candidate files:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/SOW_CURRENCY_S4_{D}/apply_s4p.py --repo <REPO_ROOT> --candidates projects/pec/execution/_Coordination/SOW_CURRENCY_S4_{D}/candidates [--check-only]
```

**Failure semantics.**

- **Preflight.** Any failure exits 1 before any byte is written. The checks:
  - every candidate hashes to its postimage;
  - every target exists and holds its preimage;
  - no temporary sibling exists;
  - every pinned file hashes as tabled;
  - if the script's directory path begins with `projects/pec/`, it must begin with the run-root prefix `projects/pec/execution/_Coordination/SOW_CURRENCY_S4_`. A placement the guard does not refuse still fails closed at the write-set inventory.
- **Write.** Each postimage is written to a temporary sibling (`…ScopeOfWork.md.s4ptmp`), hash-checked and renamed over its target.
  - If any step after the first write fails (I/O error, hash mismatch, post-write inventory mismatch, changed pinned file), the script restores every replaced target from the preimage bytes it read at preflight, removes every temporary file, and exits 1.
  - On exit 1 every target holds its preimage and no temporary file remains. Exit 2 would report an incomplete rollback; it was never observed in testing.
- **Write set.** The script inventories every file under `projects/pec` (path and SHA-256), except its own directory (the run root), before and after the write. It requires the difference to be exactly the eight targets, each modified from preimage to postimage, with nothing created or removed.
- **Second run.** It fails preflight, because the targets no longer hold their preimages. The script never touches `_STATUS.md`, `_REVIEW.md` or `MEMORY.md`.

The check aids, which are not bound:

| Aid | SHA-256 | Role |
|---|---|---|
| `test_apply_s4p.py` | `644ee64a9175193a66c365cc92ed7e9c13b12060e7870346843cddd40ffcc9c4` | fault injection, nine cases |
| `verify_s4p_quotes.py` | `57bf8dfd85e835a9a36b7dde9389e2e36005d655afd56c644e8956a42dce6c78` | two-sided quote check, raw dependency quotes, forbidden phrase, observation commit, multiplicity (`MULT`) |
| `verify_s4p_state_claims.py` | `6feb6114b56359c6b22301d0b0356d5e1efb8edf7096f7e226047c64602643a9` | commit-anchored state claims, each also matched in the candidate |
| `check_sibling_ids.py` | `1e74c88a5a917b8d3e66af4432923a07adb0014c318fb5c51ffe287610146b69` | qualified sibling and external citations resolve against postimages |
| `check_quote_currency.py` | `f398b4b086b3bbb4fe7526dcaafecc215fd2cff94ec8fd967ed61b55c03c04d8` | corpus-wide `D-PEC-95` quote currency, before and after |
| `scan_s2_quotes.py` | `940bc2f78b509442fe6cf4c155254c5719dc7be64bd989a16d4b5de9f9ec7045` | heuristic S2 quotation-currency scan (a STALE line fails the runner) |
| `scan_external_quotes.py` | `bb2402e7b6ad77c43a8d6488e49ec389dbab0f2c022cc025c7dc9397c2d9d44f` | informational downstream consequence scan |
| `run_s4p_checks.sh` | `228ede0c38fd202e3a001ad8fd835f47e46ceea0d2a27939e7b56187b99a439a` | runs checks 2–10 on pre/post exports |
| `negative_controls.sh` | `6f7d2c7506d2d963ef1f469498d8928a2d08223438eef2e816fb32615f4e4a49` | six negative controls |
| `build_apply_s4p.py` / `apply_s4p.template.py` | `df714b6d3dfee3f378ced8a7633455daf2e6760ab247945c3a4e13126a0a4499` / `04e8507a2766a684782f7462aabbb45914fd6a3557f5b8e70cf6bc1c82050687` | renders the bound script |

## Finite verification

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1`, on the act branch. Record each command, exit code and output in the run root; the act script leaves its own directory out of its write-set inventory. `run_s4p_checks.sh` runs rows 2–10 on two `git archive` exports of one commit (pre and post), and is the rerun method.

| Check | Command | Required result |
|---|---|---|
| 1. Preconditions | ruling and register row on fetched `origin/main`; `apply_s4p.py --check-only`; `pec_reliance_hold.py --operation dispatch-for-production` on each target before dispatch and `rely-for-production` before fan-in | pins as tabled; `--check-only` exits 0 with `CHECK preflight passed`; `ALLOW` everywhere; on any pin mismatch, stop and route to the owner (no re-pin is pre-authorized) |
| 2. Contract validity | `python3 tools/scope_of_work/validate_scope_of_work.py <DEL folder>` ×8 | `PASS format=SOW_V1` ×8 |
| 3. Checklist | `python3 tools/scope_of_work/derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, each twice | exit 0; reruns byte-identical; each equal to the prepared checklist (hashes under Preparation evidence) |
| 4. Boundary owners (QA 21) | `python3 tools/scope_of_work/check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×8 | exit 0; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; every `NOT_CHECKABLE` clause resolved by hand as tabled below |
| 5. Quote fidelity | `python3 <run root>/verify_s4p_quotes.py --tree . --gitdir . --prep <run root> --observation 125cfacc1` | `RESULT PASS 740/740`. Every quotation carries a `commit` and is read there, so later edits to other files cannot fail this row |
| 6. State claims | `python3 <run root>/verify_s4p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 1144/1144` (reads the named commits; independent of the working tree) |
| 7. Sibling and external IDs | `python3 <run root>/check_sibling_ids.py <run root> .` | `RESULT PASS 57/57` |
| 8. Lifecycle preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv'` | empty |
| 9. Registers and quote currency | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution`, and `check_quote_currency.py`, before and after | outputs **identical** to the pre-act run. At `b990b0c90` strict gives exit 1, 0 errors, 26 `XRG-013` warnings (owner-deferred under D-GOV-48), and quote currency is 127/127. A new finding or a changed count fails |
| 10. Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .` | exit 0 each; output identical before and after |
| 11. Containment | `git diff --name-status origin/main...HEAD` | the eight modified contracts; M's files if selected; the run root and HELP_HUMAN's records under `execution/_Coordination/**` (and `docs/STATUS.md` under `D-PEC-88`); nothing else |
| 12. Whitespace | `git diff --check origin/main...HEAD` | clean |

Re-audit: not recommended. The act changes no decomposition truth, register or topology.

QA 21 hand resolution. These are the per-act clauses the tool reports as `NOT_CHECKABLE`. The claims in parentheses name the owner; where the requirement itself does not cite that claim, the row says so (verdict 01 F4). Those gaps are carried from the prior contracts, and the owner is still named in the contract.

| Contract | Requirement → owner (claim) |
|---|---|
| DEL-04-01 | REQ-003 → `DEL-03-01` (CLM-012, cited); its excluded feed-grammar act → `DEL-02-01`..`DEL-02-09` (named in CLM-015, which REQ-003 does not cite); REQ-005 → `DEL-04-03` (CLM-011, CLM-015); REQ-006 → `DEL-04-05` (CLM-012, CLM-015); REQ-011 → `DEL-08-06`, `DEL-08-03` (CLM-015); REQ-018 → `DEL-04-03`, `DEL-10-13` (CLM-023, cited). The tool checks REQ-012 |
| DEL-04-02 | REQ-006 → `DEL-04-05`; REQ-007 → `DEL-04-03`; REQ-008 → `DEL-01-01` (CLM-011, cited), `DEL-03-01`, `DEL-03-02` (named in CLM-015, which REQ-008 does not cite; carried byte-identical from the prior contract), feed grammar reaching PKG-02 (named in CLM-006, which REQ-008 does not cite); REQ-010 → `DEL-08-01`, `DEL-08-02`, `DEL-08-03`, `DEL-08-05`, `DEL-08-06` (CLM-015, CLM-012), PKG-09 (CLM-006) |
| DEL-08-01 | none reported. The tool checks REQ-009 (owners in CLM-005, CLM-010); the tier-0 profile act is named in CLM-010 as SCA-006 §B6's, not a deliverable's |
| DEL-08-03 | REQ-004 → `DEL-08-02` (CLM-006, cited; CLM-009 named, not cited); REQ-008 → `DEL-04-03`, `DEL-06-05`; REQ-009 → `DEL-04-05`; REQ-011 → `DEL-01-05` (CLM-009, now cited); REQ-017 → `DEL-04-05`; REQ-018 → `DEL-08-06`; REQ-020 → `DEL-04-03` (CLM-007, cited; CLM-009 named, not cited). The tool checks REQ-010 and REQ-019 |
| DEL-08-04 | REQ-012 → `DEL-01-05` (CLM-011, now cited). The tool checks REQ-007; its per-act owners are all in CLM-011 |
| DEL-04-03 | REQ-006 → `DEL-06-05` (CLM-014, CLM-016); REQ-008 → `DEL-04-05` (CLM-016); REQ-021 → `DEL-10-13` (CLM-021, CLM-020). The tool checks REQ-010 and REQ-022 |
| DEL-03-04 | REQ-003 → `DEL-01-01` (CLM-010); REQ-008 → `DEL-10-13` (CLM-017, CLM-015). The tool checks REQ-013 and REQ-016 |
| DEL-10-03 | REQ-013 is not an exclusion: it names `DEL-08-01` as owner of the credential mechanism (CLM-008, CLM-016). The tool checks REQ-015 |

### Independent verifier

The method's independent verification is a separate `MODE=VERIFY` run, read-only on production content, by a TASK that authored nothing. The preparation verdicts are in the prep folder (`VERIFIER_VERDICT_01.md` onward, each with the manager's dispositions); a fresh one runs again at the act. It returns a verdict file; defects return to the author, and the verifier does not repair. It checks:

1. **Basis.** The ruling and register row are on `origin/main`; the run-root script hashes as bound; the pins match.
2. **Byte identity.** The written files equal the tabled postimages.
3. **`MODE=VERIFY`.** The mode-applicable subset of `resources/checks.md` (items 1, 3, 4, 8, 9, 13, 16, 18–21), including the QA 21 hand resolution.
4. **Semantics.**
   - Every claim is true at the commit it names or at `125cfacc1`, and every quotation is verbatim.
   - No requirement adds scope beyond the deliverable's ledger rows, its `Deliverables.csv` row and PRD v2.4.
   - Every open item is `TBD`/`CON`.
   - Kept IDs keep their meaning, and no ID is retired or reused.
   - Nothing is built around verify-before-rely.
   - The Part B texts and gates are verbatim, and the DEL-04-01 gates are stated as still binding.
   - No Remaining section is read or presented as a surface.
5. **Containment and lifecycle.** As in the table above.

## Administrative grant

- **Scope.** One WORKING_ITEMS instance runs the act, the checks and, if selected, add-on M at closeout. It runs the reliance preflights. One fresh read-only TASK is the verifier.
- **Run root.** `execution/_Coordination/SOW_CURRENCY_S4_{D}/`, in the default-writable fence. It holds:
  - `apply_s4p.py` (exact bytes), `candidates/`, `quotes/`, `claims/`, the check aids and all outputs;
  - `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`;
  - `VERIFIER_VERDICT_NN.md`.

  No `_run_records/` entry is written in any deliverable.
- **Records not opened.** `docs/STATUS.md` and `README.md` stay with HELP_HUMAN under `D-PEC-88`. `_Evaluation/**`, registers, dependency files and each deliverable's `_REVIEW.md`/`Review_Findings.csv` stay closed.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning, unless the owner states otherwise. Role identity is instruction-asserted.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12, with required CI and independent review on the actual candidate. The register row, receipt and graph records are HELP_HUMAN's.

## Rollback

- **During execution.** On exit 1 the script leaves every target at its preimage and no temporary file. If a later check fails, discard the branch or worktree.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR restores the eight preimages tabled above, and removes M's eight created files if M ran. No lifecycle state changed, so nothing else is walked back. The ruling record and register row are never reverted; a rollback is its own register row and record. The run root stays as non-current evidence with a rollback note. No silent downstream repair is made.

## Limits

This proposal, and any ruling selecting A, A + M or an amendment, grants none of the following:

- any `v2/**`, `software-workflow.json` or `docs/PRD.md` write, or any source, fixture or test file. The DEL-04-01 Part B production obligations stay gated as their contract states. No API-schema field (SCA-006 §B8) is added;
- any `_Decomposition/**` or `_ScopeChange/**` write, or any register write: no `Deliverables.csv`, `ScopeLedger.csv`, `ContextBudgetQA.csv`, `Companion_Inventory.csv`, `Dependencies.csv` or `_DEPENDENCIES.md` change, no dependency edge (including any edge from DEL-08-06 or to DEL-02-07 that a `CON` records), and no action on the D-GOV-48 warnings;
- any `_CONTEXT.md`, `_REFERENCES.md`, `_SEMANTIC.md`, `_REVIEW.md` or `Review_Findings.csv` write, or any file of a deliverable outside the eight. The disclosed consequences in DEL-04-05, DEL-10-11 and other contracts are for their own packets;
- any lifecycle change or `_STATUS.md` write, or any review state. No `## Remaining` entry is written or read;
- `CHECKING`, `ISSUED`, artifact acceptance, a REVIEW gate act, or any readiness or reliance claim;
- a registry, profile or tier-0 act (including the SCA-006 §B6 profile entry), any tool declaration or invocation, or a resolution of any `CON` item;
- a first Scope of Work for DEL-08-06 or DEL-10-13 (graph node K2);
- a Task Management disposition, an audit run, a pointer move, or an edit of the `D-PEC-99` exhibit;
- a foreign, Root, tier-0 or instruction-surface write, including `projects/pec/AGENTS.md`;
- adoption of `scope-of-work` `MODE=REVISE` or any other new Root mode;
- a schedule reading: blocker output stays advisory.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**, the eight exact replacements in one act, authored under `INIT` discipline and verified by `MODE=VERIFY`, as described under Method.
2. **Part B reading.** Confirm that the ruling on this packet does the following:
   - places DEL-04-01-REM-001 and REM-002 into the DEL-04-01 contract verbatim, with their gates **still binding**: production stays gated on a separate exact owner-ruled DEL-04-01 production packet, WORKING_ITEMS activation and a current reliance preflight;
   - is the owner's acceptance of the exact documentary wording of DEL-04-02-REM-002 and DEL-04-03-REM-002 at their named loci **only**, as tabled;
   - discharges only the exhibit's carry of that text.

   Recommendation: **confirm**. Without an answer, the text is applied and the DEL-04-01 gates stay binding.
3. **Two readings the candidates take, for confirmation.**
   - (a) DEL-04-01 `REQ-001` counts **seven** components, adding terminal completion from local Git merge reachability. Grounds: revision-1.6 SOW-004 and PRD v2.4 PEC-ORI-001 name it, and DEL-01-01 and DEL-02-08 attribute its derivation to DEL-04-01. This is what makes DEL-04-05's quotation go stale.
   - (b) DEL-04-03 treats the reliance envelope as a declaration **beside** the three-field stamp, not a fourth stamp field. Grounds: the SOW-097 Notes "distinct from SOW-006 stamping" and SCA-006 IA §13.2. This keeps DEL-04-03 `REQ-001` byte-identical.

   Recommendation: **confirm both**. Otherwise say which to amend; the affected candidates would be re-drafted.
4. **Add-on M — MEMORY files.** Create the eight `MEMORY.md` files at closeout, as tabled (recommended); or record the run only in the graph and central receipt. `projects/pec/AGENTS.md` allows either on your decision.
5. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran on `git archive` exports in the session scratchpad, never on a checkout. Interpreter: Python 3.13.7 (CPython); local date 2026-09-26. The final run (`evidence/run_main/SUMMARY.out`, from `run_s4p_checks.sh` at `b990b0c90`; every raw output is beside it):

```text
basis commit: b990b0c909e88176c1afcf82ca24623ba8172a40
python: Python 3.13.7
PASS act: check-only 0, apply 0, rerun refuses 1
PASS containment: 8 differing files, all ScopeOfWork.md
PASS validate / checklist (rerun byte-identical) / boundary (no UNRESOLVED_OWNER/UNDEFINED_CLAIM) — for each of the eight
PASS quotes: RESULT PASS 740/740
PASS state claims: RESULT PASS 1144/1144
PASS sibling and external IDs: RESULT PASS 57/57
INFO consequence scan (informational): SUMMARY stale=13 kept=25
PASS S2 quotation currency (heuristic scan): SUMMARY stale=0 kept=2
PASS strict identical before/after, export root normalized (exit=1)
PASS harness identical before/after, export root normalized (exit=0)
PASS receipts identical before/after, export root normalized (exit=0)
PASS dependency quote currency identical before/after (SUMMARY active_execution_quotes_verbatim 127/127)
PASS whitespace
PASS fault injection: RESULT PASS 9/9
OVERALL PASS
```

(`SUMMARY.out` lists the per-contract validate, checklist and boundary lines individually; they are condensed to one line here.) The 13 informational scan lines are heuristic. The verified consequences are the three tabled above; the rest are the scanner pairing unrelated quotation marks or matching shared register text.

Negative controls (`evidence/negative_controls.out`, scratch copies), each of which tripped its check:

1. a shortened DEL-04-01 Gate line fails its exhibit quote through the `MULT` rule;
2. a one-character change to DEL-08-01 `OUT-001` fails both raw dependency quotes;
3. a shortened DEL-04-02 Part B replacement (4) fails its exhibit quote;
4. a wrong hash fails its state claim;
5. a citation of an undefined `DEL-04-03/REQ-099` fails the sibling check;
6. a removed matrix row fails validation.

Checklists (`evidence/run_main/checklist_<DEL>.json`):

- DEL-04-01 `1d8cccbc189dbab444dd91defcc5e7aa9cb7b41d75351aad45571129eadf61f5`
- DEL-04-02 `4b0399562616101e31181bc22fa0656c9c9c5e57388e8c779f792b533e009fa7`
- DEL-08-01 `2b5beadb0edaf471a25706ac4c4022aa83ab598bfeb1b216c3a6bf42bc7e50b4`
- DEL-08-03 `b91cf9f452134c60f7e569fb415a5842770e61df120aacf3dc6f8e9ed361c1af`
- DEL-08-04 `afe85efd4dd03949737c8f2d4edd9b2da08b853ceaecad562242d58ceb7b61c1`
- DEL-04-03 `85f0d3bcb133687e7ad0d721e1e5980b4a56adff21c286e9b265b7fa9c000e0c`
- DEL-03-04 `1a86fa421c0d79bb8c0a080979d4e4f1bbde3c3beed95b832244fcc86d0dbeda`
- DEL-10-03 `24272d5dc8fd2907fc1b87259b449623d6015bdaf6a02936c2c7ec1f34a060fd`

Preparation artifacts (all in this prep folder; hashes in `SHA256SUMS`):

- `candidates/projects/pec/execution/…/ScopeOfWork.md` ×8 (postimages as tabled);
- `quotes/DEL-*.json` ×8 and `claims/DEL-*.json` ×8 (the verifier inputs);
- `apply_s4p.py` (bound), `apply_s4p.template.py`, `build_apply_s4p.py`, `test_apply_s4p.py`, the verifiers and scans, `run_s4p_checks.sh`, `negative_controls.sh`;
- `DRAFTER_BRIEF.md` (the drafters' shared brief);
- `evidence/` (every check output, the reliance preflight, the checklists and the negative controls);
- `VERIFIER_VERDICT_01.md` onward (the preparation verdicts, with dispositions).

Basis at `125cfacc1` (equal at `b990b0c90` unless noted):

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` / `agents/AGENT_TASK.md` / `projects/pec/AGENTS.md` | `c8ce87ef…1dffd` / `9ae4bea2…9665` / `1a13a5b0…8fb7` / `df9196d1…5eb8` |
| `_Decomposition/SOFTWARE_DECOMP.md` / `Deliverables.csv` / `ScopeLedger.csv` / `ContextBudgetQA.csv` / `_LATEST.md` | `9374c21f…8eb1` / `94ee5d18…9805` / `1d24a4b8…916e` / `93b0bb07…4c7c` / `768ae4c4…a771` |
| `docs/PRD.md` (v2.4) | `ae49b806…3fbe` |
| SCA-006 `Propagation_Plan.md` / `Impact_Assessment.md` / `Amendment_Actions_CP2.csv`; SCA-005 `Propagation_Plan.md` | `f95d00d1…d7d8` / `93253b7d…b691` / `d901b432…c1de`; `50cd0b1d…1350` |
| `D-PEC-90` / `D-PEC-94` / `D-PEC-96` / `D-PEC-98` / `D-PEC-99` / `D-PEC-100` / `D-PEC-101` rulings | `43a0c663…efab` / `b6814e90…5a6b` / `852057f0…399e` / `039dc7e2…8361` / `3e34403a…c989` / `13690e20…729b` / `baa4fc09…ba28` |
| `D-PEC-99` exhibit / `D-PEC-100` proposal / `_REGISTER.md` (at `125cfacc1`) | `69b646f8…f45e` / `39c4331e…e25b` / `33b43ae8…5a2f` |
| Work graph (at `125cfacc1`) | `8296ad0c…b148` |
| `validate_decomposition_registers.py` / `MEMORY_TEMPLATE.md` | `300a321f…ee20` / `5a9564f4…6a5a` |
| Notices: project-setup incremental / D-GOV-48 package home | `8829ac84…64af` / `15ea36ee…e8e6` |

Attribution: prepared by WORKING_ITEMS (Type 1) under HELP_HUMAN, node S4 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with eight TASK drafters and fresh read-only reviewers (one per verdict) as described under Method. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The roles and the `high` reasoning effort are instruction-asserted.
