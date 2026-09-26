---
amendment_id: SCA-006
doc_kind: scope_change.propagation_plan
decomp_variant: SOFTWARE
checkpoint_group: 2
created: 2026-09-25
status: candidate_awaiting_checkpoint_2_acceptance
accepted_impact_assessment_sha256: 93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691
accepted_intake_sha256: c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891
amendment_preview_sha256: 737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4
---

# SCA-006 — checkpoint-group-2 propagation plan

## Status and authority

This plan, together with `Amendment_Preview.md` and the other package files listed in owner question Q-CP2-A, is the checkpoint-group-2 package that the owner accepts or revises as one unit. **It applies nothing.** It was prepared by WORKING_ITEMS (brief B5, work-graph node R2 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`). Its authority is the owner's checkpoint-1 acceptance of 2026-09-25 (group-1 snapshot `checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/`), verbatim:

> SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded

Those selections are applied exactly and are not re-asked:
- DQ-a: direct query through tool calls, with a read-only `agent` access class;
- ENV-a: PEC-ORI-007 → SOW-097 → DEL-04-03;
- BUD-a: PEC-API-006 → SOW-098 → DEL-08-03, with numbers at P1;
- GATE-a: a standing §12 gate, SOW-100 and DEL-10-13, with the §12 P1 row text not edited;
- INS-a: the `AGENTS.md` change is an instruction tranche at checkpoint 3;
- R-C excluded.

The write scope the amendment needs is the SOFTWARE default:
- the decomposition document and its companion registers;
- the affected `_CONTEXT.md` files;
- SCA-owned `_ScopeChange` state;
- the owner-adopted PRD successor (the SCA-005 precedent);
- the `projects/pec/AGENTS.md` instruction tranche with its manifest and notices (INS-a).

Everything else is a downstream rerun owned elsewhere, and WORKING_ITEMS does **not** execute it. Nothing in this package makes operational reliance on PEC data available: it begins only at a PEC release that has passed the PRD §12 reliance-advertisement gate.

Package files and candidate postimages:

| File | Role | SHA-256 |
|---|---|---|
| `Amendment_Preview.md` | exact decomposition amendment (Seq 18–43), diff-style, mechanically proved | `737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4` |
| `Amendment_Actions_CP2.csv` | final action register (54 rows) | `d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de` |
| `Supersession_Delta.csv` | 16 bindings | `e69f97814294ccd993fceff12cdf992623156c33ca4993adb103b61774e5977b` |
| `PRD_V2_4_SUCCESSOR_DIFF.md` | exact PRD amendment (Seq 1–13), section by section | `a743a5273c66dc679a99888c4dc2b865a318dab64fcaaa7768ecb71f35696a4c` |
| `AGENTS_MD_CANDIDATE_DIFF.md` | exact instruction amendment (Seq 14–17), I1 hunks separated, tranche manifest and notice drafts | `7c57a1b2c02c872fae6f778beeddf7f812809d469b504e34d1e6f79bbb48a158` |
| `CP2_CANDIDATE/docs/PRD.md` | PRD v2.4 successor candidate (preimage v2.3 `fff27a66…dfc32`) | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `CP2_CANDIDATE/AGENTS.candidate.md` | `projects/pec/AGENTS.md` postimage with I1 (preimage `c9d3b44d…197a`) | `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` |
| `CP2_CANDIDATE/AGENTS.candidate_without_I1.md` | the same without I1 | `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188` |
| `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` | revision 1.6 (preimage `dc2b8479…9660`; pre-acceptance variant `3ad0de686616f895c5fc63cceccef15dca3cd45ba1ca154d9797c2b9551f8a8b`) | `4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71` |
| `CP2_CANDIDATE/_Decomposition/ScopeLedger.csv` | 100 rows (preimage `83152a94…d9df`) | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `CP2_CANDIDATE/_Decomposition/Deliverables.csv` | 68 rows (preimage `b8628fc4…d65a`) | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv` | 68 rows (preimage `2a194105…eb0df`) | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv` | counts (preimage `7c8a24a8…6ef8`) | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |

The candidate files `AGENTS.candidate*.md` are deliberately not named `AGENTS.md`, so that no harness discovers them as live nested instructions. The hashes are computed with every acceptance-bound slot at its default value, `2026-09-25` and `SCA-006_GROUP-2_2026-09-25`. The slots are listed in each diff document, and the hash rule of `Amendment_Preview.md` §"Acceptance-bound tokens" applies.

## Checkpoint-3 preconditions

Checkpoint-3 preparation stops before its first write unless every value holds:

| Precondition | Required value |
|---|---|
| Accepted group-2 decision snapshot | exists under `_ScopeChange/checkpoint_snapshots/` and binds every file in the table above at its SHA-256 (with the slot rule) |
| Live preimages | `SOFTWARE_DECOMP.md` `dc2b8479…9660`, `ScopeLedger.csv` `83152a94…d9df`, `Deliverables.csv` `b8628fc4…d65a`, `ContextBudgetQA.csv` `2a194105…eb0df`, `Companion_Inventory.csv` `7c8a24a8…6ef8`, `docs/PRD.md` `fff27a66…dfc32`, `projects/pec/AGENTS.md` `c9d3b44d…197a` |
| `_ScopeChange/_LATEST.md` | names SCA-005 (posture `ACCEPTED_PREDECESSOR`), SHA-256 `e92b3b16a48cd72288c8b6eddc08d62e3e79e0c9bec521864ee7d5484a307d24` |
| `_Decomposition/_LATEST.md` | revision 1.5, SHA-256 `626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd` |
| Direct-propagation preimages | the three `_CONTEXT.md` pre-SHA-256 values in A2 |
| Reliance-hold preflight | `pec_reliance_hold.py` returns `ALLOW` for every write target (operation `exact-correction-preparation`, then `candidate-validation`) |

A mismatch returns the package to checkpoint 2 with drift evidence. It is not reconciled during execution.

## Package-role classification of every touched surface

| Surface | Package role | Classification | Owner at checkpoint-3 preparation | Planned state |
|---|---|---|---|---|
| `_Decomposition/SOFTWARE_DECOMP.md` | working surface | `DIRECT_EDIT` | SCOPE_CHANGE (WORKING_ITEMS) | candidate postimage with the two pre-acceptance front-matter lines; `CURRENT` after checkpoint-3 acceptance |
| `ScopeLedger.csv`, `Deliverables.csv` | authoritative companion registers | `DIRECT_EDIT` | SCOPE_CHANGE | candidate bytes |
| `ContextBudgetQA.csv`, `Companion_Inventory.csv` | authoritative companion registers | `RECOMPUTE` (rows and counts, as candidate bytes) | SCOPE_CHANGE | candidate bytes |
| `docs/PRD.md` | upstream product authority outside the decomposition | `DIRECT_EDIT` (owner-adopted bytes) | SCOPE_CHANGE, applying the adopted candidate | v2.4 candidate bytes with slots filled |
| `projects/pec/AGENTS.md` | PEC instruction file | `DIRECT_EDIT` through the instruction tranche (INS-a) | the checkpoint-3 manager as tranche integration owner | the candidate the owner selects at Q-CP2-1 |
| `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260925.yaml` | Root instruction-surface record | `DIRECT_EDIT` (new file; draft in `AGENTS_MD_CANDIDATE_DIFF.md` §6.1) | same, with the checkpoint-2 act quoted in its slot | new |
| DEL-04-03, DEL-08-01, DEL-08-03 `_CONTEXT.md` | variant-local derived metadata | `DIRECT_EDIT` | SCOPE_CHANGE | exact mirrors (A2) |
| 63 other `_CONTEXT.md`, 66 `_REFERENCES.md` | variant-local derived metadata / reference packets | `NO_CHANGE` now | PROJECT_SETUP (B7) | `STALE_REPIN_REQUIRED` on version only after checkpoint 3 |
| all `_STATUS.md` | lifecycle truth | `NO_CHANGE` (no REMOVE action) | none | unchanged |
| DEL-08-06, DEL-10-13 folders | new deliverable scaffolds | `NO_CHANGE` now | preparation via PROJECT_SETUP under its own packet (B1) | `NOT_CREATED` |
| `Dependencies.csv` / `_DEPENDENCIES.md` | downstream structured dependency truth | `NO_CHANGE` now | dependency-extract (B2, B3) | two EvidenceQuotes `STALE_REBUILD_REQUIRED`; new rows `NOT_CREATED` |
| 9 affected `ScopeOfWork.md` (IA §7.1) | derived production contracts | `NO_CHANGE` | WORKING_ITEMS + artifact gates (B4) | per B4 |
| DEL-00-03 `artifacts/v2/SPEC.md` (CHECKING) | accepted derivative artifact | `NO_CHANGE` | DEL-00-03 owning workflow (B5) | `STALE_REVIEW_REQUIRED` |
| `_DomainEngines/profiles/pec.yaml` | tier-0 profile (foreign to PEC's write scope) | `NO_CHANGE` | tier-0 owner (B6) | unchanged until its own act |
| `v2/**` (API schema) | source | `NO_CHANGE` | later D-PEC source packet (B8) | `STALE_SOURCE_PACKET_REQUIRED` when built |
| `_ScopeChange/SCA-006_2026-09-25_1912/` | snapshot / handoff artifact | `RECOMPUTE` | SCOPE_CHANGE | completed at checkpoint-3 preparation (A5) |
| `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_*` | snapshot / handoff artifact | `RECOMPUTE` | HELP_HUMAN after the owner acts | immutable group-2 decision record |
| `_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_*` | derived publication artifact (audit evidence) | `RECOMPUTE` | TASK `audit-decomp` (C4) | new immutable snapshot |
| `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md` | snapshot / handoff pointers | `RECOMPUTE` | SCOPE_CHANGE, only after checkpoint-3 acceptance (A6) | revision 1.6 / SCA-006 |
| Root, App and Runtime `execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | foreign notice files | `DIRECT_EDIT` (new, non-binding) | HELP_HUMAN (A4) | written with the tranche |
| `docs/STATUS.md`, `README.md`, `_COORDINATION.md`, the work graph | ordinary orientation surfaces | `NO_CHANGE` by SCA-006 | HELP_HUMAN under `D-PEC-88` | refreshed after each owner act |
| decisions, receipts, prior SCA and audit snapshots, frozen corpus | history / evidence | `NO_CHANGE` | none | `HISTORICAL_CURRENT` |

## Lane A — direct writes executed after checkpoint-2 acceptance (checkpoint-3 preparation)

### A1. Apply the decomposition, register and PRD postimages

1. Write `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` over the live file, with the two pre-acceptance front-matter lines (`Amendment_Preview.md` §"Acceptance-bound tokens"). The acceptance-date slots take their actual dates.
2. Copy the four register postimages over the live registers byte for byte.
3. Write `CP2_CANDIDATE/docs/PRD.md` over `projects/pec/docs/PRD.md`, with its slots filled: the date, the adoption date and the `SCA-006_GROUP-2_<date>` folder token (`PRD_V2_4_SUCCESSOR_DIFF.md` §6).
4. Prove that every live postimage SHA-256 equals its accepted candidate after slot substitution, and record both hashes.

### A2. `_CONTEXT.md` mirrors (MODIFY propagation for Seq 30, 31, 32)

Each deliverable's `_CONTEXT.md` exactly mirrors its accepted `Deliverables.csv` row, plus the revision-1.6 provenance clause (the SCA-005 Lane A2 precedent). All other bytes stay unchanged. No other `_CONTEXT.md` or `_DEPENDENCIES.md` carries text this amendment changes: a scan of all 66 of each found hits only in these three files. Paired read: none of the three has a sibling `_MEMORY.md` or `MEMORY.md`.

#### DEL-04-03

Path `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md`; preimage `a505c2686af7c6d51fe4d1d8dad25bcadd3a5d9c59372c3f9226d31fed2263da`; postimage `b28ada4674662515ed7f975cb59c1ee2c2f9cac3c4bcf0d919ced22af79a7b22`.

DEL-04-03 — table CoversScopeItems:

```diff
-| CoversScopeItems | SOW-006;SOW-007 |
+| CoversScopeItems | SOW-006;SOW-007;SOW-097 |
```

DEL-04-03 — section Description:

```diff
-## Description
-
-Per-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness).
+## Description
+
+Per-claim citations (path/anchor/SHA) and response stamping (examined-through SHA, generation time, per-feed freshness), with the reliance envelope (pin, per-feed coverage and limitations, per-claim trust tier, file-fallback signal).
```

DEL-04-03 — provenance tail (SCA-005 Lane A2 precedent):

```diff
-then by revision 1.5 (`current_basis`, SCA-005 successor).
+then by revision 1.5 (`current_basis`, SCA-005 successor),
+then by revision 1.6 (`current_basis`, SCA-006 successor).
```

#### DEL-08-01

Path `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md`; preimage `151e1e34330a58467ef0f9aa28a3283b50b84bf5f563b03039f5c6bcd9273985`; postimage `74b12e7358a71000b8cd544f2db8a736289e7ca4b1e3f94dbadbf98154292d22`.

DEL-08-01 — section Description:

```diff
-## Description
-
-Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.
+## Description
+
+Local-only Unix-socket binding with token-scoped access classes (owner, harness, agent, admin; agent is read-only query for tool calls); auth-reuse choice tracked by OI-006.
```

DEL-08-01 — provenance tail (SCA-005 Lane A2 precedent):

```diff
-then by revision 1.5 (`current_basis`, SCA-005 successor).
+then by revision 1.5 (`current_basis`, SCA-005 successor),
+then by revision 1.6 (`current_basis`, SCA-006 successor).
```

#### DEL-08-03

Path `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md`; preimage `4644758f07a93eb203bce19533916fbf4e55d52e867895f2a87a5b99b4aec73d`; postimage `95fa815a31a38e59c001dd3596bc47053508cd3ff59c9d3eae67d64ba9d037b5`.

DEL-08-03 — table ContextEnvelope:

```diff
-| ContextEnvelope | S |
+| ContextEnvelope | M |
```

DEL-08-03 — table CoversScopeItems:

```diff
-| CoversScopeItems | SOW-043 |
+| CoversScopeItems | SOW-043;SOW-098 |
```

DEL-08-03 — section Description:

```diff
-## Description
-
-Machine-first response envelope carrying citations.
+## Description
+
+Machine-first response envelope carrying citations. Responses are bounded by declared size budgets met by pagination or continuation, with any truncation stated.
```

DEL-08-03 — section Envelope notes:

```diff
-## Envelope notes
-
-(none)
+## Envelope notes
+
+M under SCA-006: declared response-size budgets met by pagination or continuation, with stated truncation, join the compact citation-bearing format (SOW-043, SOW-098); kept one cohesive format slice
```

DEL-08-03 — provenance tail (SCA-005 Lane A2 precedent):

```diff
-then by revision 1.5 (`current_basis`, SCA-005 successor).
+then by revision 1.5 (`current_basis`, SCA-005 successor),
+then by revision 1.6 (`current_basis`, SCA-006 successor).
```

### A3. `_STATUS.md` acts

None. SCA-006 has no REMOVE action. No `_STATUS.md` is written, and no lifecycle changes: DEL-00-03 stays CHECKING, and every other lifecycle stays as it is.

### A4. Instruction tranche (INS-a)

The checkpoint-3 PR carries the instruction tranche `PEC-SCA006-OPERATIONAL-RELIANCE-20260925`; the date part is the application date:

1. Write the candidate the owner selects at Q-CP2-1 over `projects/pec/AGENTS.md`, with its slots filled (the front-matter `amended:` date and the group-2 folder token; `AGENTS_MD_CANDIDATE_DIFF.md` §9).
2. Write the manifest at `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-<YYYYMMDD>.yaml`. The draft is in `AGENTS_MD_CANDIDATE_DIFF.md` §6.1 (draft SHA-256 `852b1d5b876500fb4970df8b688394ad2c15883ede6f4a8e8cd821989efbbc45`). Fill the slot for the verbatim checkpoint-2 act and the group-2 `DECISION.md` path. Set `m6_notice.disposition: routed`.
3. HELP_HUMAN writes the three non-binding notices in the same PR. This follows the SCA-005 group-2 precedent, where HELP_HUMAN writes notice files during checkpoint-3 preparation, and INS-a's "with its own manifest and notices". It carries the content of graph node R4. The notices:
   - `execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (Root)
   - `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (App)
   - `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (Runtime)

   Their texts are drafted in `AGENTS_MD_CANDIDATE_DIFF.md` §6.3. The date in each name is the application-date slot. They are the only foreign-path writes this plan covers, and they grant nothing in the receiving loops.
4. Run the checks the draft names: `validate_instruction_entrypoints.py`, the G4 check `validate_instruction_tranche_manifest.py` in CI mode and in `--added-manifests-only` diff mode over the PR range, `validate_pec_loop_receipts.py`, and `git diff --check`.

Lineage citation: both `AGENTS.md` candidates cite the SCA-006 adoption by its group-2 snapshot folder, not by a D-PEC number, because no such number exists at preparation and the canon forbids inventing one. Under Q-CP2-2 (a) the new D-PEC register row points to that same folder, as `D-PEC-92` does for SCA-005. The tranche adds the register-row number to the Product Posture and Governance Pointers lines only if the owner's checkpoint-2 act directs it; otherwise the folder citation stands and the candidate bytes are applied unchanged.

If the owner prefers the notices after checkpoint-3 acceptance instead, the manifest records `disposition: pending`, which the G4 guard accepts. The notices then go out as graph node R4 without editing the manifest. A later edit to the manifest would itself need a new manifest.

### A5. SCA-owned snapshot completion

In this snapshot folder, keep `Brief.md`, `Impact_Assessment.md`, `Amendment_Actions.csv`, `Pre_Change_Coverage.json` and every checkpoint-2 artifact byte-unchanged. Generate `Supersession_Map.csv` with the deterministic accumulator, never by hand:

`python3 tools/coordination/accumulate_supersession_map.py --prior-map projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Supersession_Map.csv --delta projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Supersession_Delta.csv --output-map projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Supersession_Map.csv`

A dry run to scratch during this preparation gave exit 0, 45 rows (29 prior and 16 new) and 0 findings. Then:
- copy the post-change audit's `coverage_summary.json` bytes to `Post_Change_Coverage.json`;
- write `RUN_SUMMARY.md`;
- update `Decision_Log.md` and `Handoff_State.md` with hashes, results and the closure verdict.

### A6. Pointers, only after checkpoint-3 acceptance

`_Decomposition/_LATEST.md` becomes the revision-1.6 handoff, and `_ScopeChange/_LATEST.md` names SCA-006. The decomposition front-matter lines return to their accepted postimage values in the same act. No pointer moves before the owner's checkpoint-3 acceptance.

## Lane B — downstream reruns not executed by WORKING_ITEMS

Each item is recorded open in `Handoff_State.md`. None is authorized or satisfied by the Lane A writes. Downstream reruns stay `FROZEN` until their own packets.

### B1. PROJECT_SETUP for DEL-08-06 and DEL-10-13 (ADD propagation; a later owner-ruled packet)

Checkpoint 2 does **not** open this lane (the SCA-005 precedent: its Lane A4 was found not exact enough to be a D-PEC packet and was deferred; `D-PEC-93` later opened it as its own packet). Through WORKING_ITEMS with project-setup, the eligible actor runs the effective source-qualified `preparation` skill, recorded in the ordered `methods` field as `[{kind: "skill", name: "preparation", source: <descriptor.source>, sourceRootId: <descriptor.sourceRootId>}]` from the discovered descriptor (no origin is hard-coded here), under a later `D-PEC` packet that names exact paths, acts, verification and rollback.

| New deliverable | Parent | Expected folder (the PROJECT_SETUP naming rule decides; recorded, not pre-empted) | Expected files |
|---|---|---|---|
| DEL-08-06 Agent tool-call query surface (SOW-099; P3; M) | PKG-08 | `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/` | `_CONTEXT.md` (mirroring the accepted revision-1.6 row), `_STATUS.md` (`OPEN`), `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` if the D-PEC-93 precedent is followed, and a deliverable-local `Dependencies.csv` with ANCHOR rows (B2) |
| DEL-10-13 Reliance-advertisement gate (SOW-100; P1; S) | PKG-10 | `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/` | same |

Until that packet lands, the strict register validator reports DRB-008 for the two absent folders, and `audit-decomp` reports two missing folders. Both are expected consequences of this deferral, not defects (C2, C4). Any read of `_STATUS.md` is paired with a sibling `MEMORY.md` when present. First Scope of Work contracts for the two deliverables follow setup through the ordinary preparation → Scope of Work path (B4).

### B2. Dependency extraction for the new deliverables and edges

Owner: dependency-extract (via TASK) under the B1 packet or its own. Planned rows (final rows are dependency-extract's; the closure tool must stay acyclic):

| From | Kind | To | Basis |
|---|---|---|---|
| DEL-08-06 | ANCHOR `IMPLEMENTS_NODE` / `TRACES_TO_REQUIREMENT` | PKG-08; SOW-099 | A-26, A-28 |
| DEL-08-06 | EXECUTION | DEL-08-01 (agent access class), DEL-08-02 (versioned schema), DEL-08-03 (response format and budgets), DEL-04-01 (orientation it serves) | IA §9.1 |
| DEL-10-13 | ANCHOR `IMPLEMENTS_NODE` / `TRACES_TO_REQUIREMENT` | PKG-10; SOW-100 | A-27, A-29 |
| DEL-10-13 | EXECUTION | DEL-03-04 (parity), DEL-04-03 (reliance envelope), DEL-04-05 (coverage honesty), DEL-10-02 (kill test), and the PKG-02 parser deliverables whose fixture suites the gate composes | IA §9.1 |
| DEL-04-03, DEL-08-03 | ANCHOR `TRACES_TO_REQUIREMENT` | SOW-097; SOW-098 | A-24, A-25, A-30, A-32 |

Topology now (the scratch overlay of the candidate registers, `analyze_dep_closure.py`): 111 EXECUTION edges, 66 nodes, 0 SCCs, identical to the live tree. The planned new edges add 4 (DEL-08-06) plus 4 or more (DEL-10-13, depending on which parser deliverables dependency-extract binds), with 0 SCCs expected. DEL-10-13 depends only on upstream producers and nothing depends on it, and DEL-08-06 has no dependants, so no cycle can form. The final count is UNKNOWN until dependency-extract writes the rows. Closure requires the strict validator at 0/0 and `analyze_dep_closure.py` at 0 SCCs / 0 bidirectional pairs.

### B3. EvidenceQuote refresh (exact set)

Owner: dependency-extract (via TASK). Exact scan (T2 `evidence_quotes.py`, 263 rows, 243 ACTIVE, rerun by the manager against the PRD v2.4 candidate): exactly **two** ACTIVE EXECUTION quotes stop being verbatim once A1 applies:

| Row | Register | Quoted locus | Refresh |
|---|---|---|---|
| DEP-09-06-003 | `PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/Dependencies.csv` | `Deliverables.csv` DEL-08-01 Description | re-quote the revision-1.6 description verbatim |
| DEP-10-03-003 | `PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/Dependencies.csv` | same | same |

The intake's other two cells stay verbatim by construction and need no refresh: DEP-09-06-004 (the DEL-08-03 description keeps "Machine-first response envelope carrying citations." as its prefix) and DEP-10-12-004 (the PKG-08 charter keeps its revision-1.5 text as its prefix). No `_DEPENDENCIES.md` mirrors either broken quote (scan of all 66). No PRD-cited quote breaks against the PRD v2.4 candidate. Until the refresh, the strict validator does not check verbatim quote currency, and the post-change audit reports the two rows as an expected SCA-006 consequence (C4). Representation: the rows keep their IDs; only `EvidenceQuote` and `LastSeen` change, as in the `D-PEC-95` N3 refresh.

### B4. Scope of Work currency (graph S4 and D1)

The SOW currency set is exactly the accepted Impact Assessment §7.1 AFFECTED set: 9 of the 32 existing contracts. The other 23 stay NOT_AFFECTED by SCA-006 and keep their SCA-005 classes (graph S1/S2).

**Graph mapping, recorded as a deliberate choice.** §7.1 routes the three review-level members (DEL-03-04, DEL-10-03, DEL-00-03) to "S1 or D1". The work graph (`WORK_GRAPH.md`, node S4) instead holds all three until checkpoint 3 (R3): DEL-03-04 and DEL-10-03 in S4, DEL-00-03 through D1. This is more conservative than §7.1: no review-level contract is refreshed against PRD v2.3 text that SCA-006 is about to change. This plan adopts the graph's hold. Checkpoint-2 acceptance fixes the S4 membership below.

| DEL | Lifecycle | Current SOW SHA-256 | SCA-005 class (SCA-005 plan §B4) | SCA-006 cause (IA §7.1 loci) | Combined class after SCA-006 | Graph node |
|---|---|---|---|---|---|---|
| DEL-04-01 | INITIALIZED | `6f4e8c66a571…` | `STALE_REBUILD_REQUIRED` | CLM-016 L266, AX-007 L363 restate verify-before-rely; REQ-010 L290, trace L400; `D-PEC-90` grant item 1 bars rebuilding it around verify-before-rely | `STALE_REBUILD_REQUIRED` | S4 |
| DEL-04-02 | INITIALIZED | `a2b50f870aa3…` | `current` | CLM-016 L225 restates verify-before-rely and "names possible consumers only at one remove" (false under direct query); REQ-013 L252; L363 provenance note | `STALE_REVIEW_REQUIRED` | S4 |
| DEL-08-01 | INITIALIZED | `8ac1dc050efb…` | `STALE_REVIEW_REQUIRED` | CLM-004 L92; L50–55 quote §8; REQ-003/REQ-004/AC-003/VER-002/VER-003 enumerate the class set, which gains `agent` (new obligation); SCA-005 residue L48, CON-001 L127 in the same pass | `STALE_REBUILD_REQUIRED` | S4 |
| DEL-08-03 | INITIALIZED | `013c615a0c91…` | `STALE_REVIEW_REQUIRED (quotation)` | REQ-005 L256; REQ-006 L257, AC-006 L274, CON-001 L286, VER-006 L321 rest on "no accepted size threshold" (false once PEC-API-006 lands); CLM-009 L229 "three" classes; scope grows by SOW-098 | `STALE_REBUILD_REQUIRED` | S4 |
| DEL-08-04 | INITIALIZED | `6d1ec1ad9796…` | `STALE_REVIEW_REQUIRED (quotation)` | CLM-011 L288 "three token-scoped access classes" | `STALE_REVIEW_REQUIRED (quotation)` | S4 |
| DEL-04-03 | INITIALIZED | `6ec7432bf8cf…` | `STALE_REVIEW_REQUIRED` | quotes no changed text; covered scope grows by SOW-097 (the reliance envelope) | `STALE_REBUILD_REQUIRED` (new obligation) | S4 |
| DEL-03-04 | INITIALIZED | `e007f5307fce…` | `STALE_REVIEW_REQUIRED` | CON-001 L248, CON-002 L249, AC-016 L296: the §12 reliance-advertisement gate makes parity's gating force and "or explained" load-bearing; SCA-005 residue L105 | `STALE_REVIEW_REQUIRED` (review level) | S4 (held to R3; §7.1 said S1) |
| DEL-10-03 | INITIALIZED | `cbcabbde6882…` | `housekeeping only` | CLM-008 L191 paraphrases the three-class set; the `agent` class joins the no-ruling-write negative surface | `STALE_REVIEW_REQUIRED` (review level) | S4 (held to R3; §7.1 said S1) |
| DEL-00-03 | CHECKING | `3e4f0efc7758…` | `STALE_REVIEW_REQUIRED` | CLM-004 L70, CLM-006 L77: the "46 requirements" premise (49 after SCA-006); review level, premise only | `STALE_REVIEW_REQUIRED` (premise only; exact-byte gate) | D1 (held to R3) |

Pass rules for every S4 packet:
- One pass per contract carries both its SCA-005 and SCA-006 causes; the contract re-quotes PRD v2.4 and revision 1.6, never v2.3 text that SCA-006 changed.
- No contract is rebuilt around verify-before-rely (`D-PEC-90` grant item 1). Operational reliance is written as available only from a release that has passed the §12 gate.
- `D-PEC-95` carry-forward: 11 ACTIVE dependency rows cite a deliverable `ScopeOfWork.md`, three of them in S4 contracts (two of DEL-08-01's, one of DEL-08-03's). Each S4 packet runs the corpus-wide quote-currency check (`CURRENCY_REV15_D95_2026-09-25/verify_d95.py` or `gen_d95.py`'s check mode) as an acceptance check, so SOW work does not leave those quotes stale.
- DEL-00-03 is CHECKING: its SOW and SPEC change only through its owning workflow and exact-byte gate (B5); nothing here moves its lifecycle.

New contracts: DEL-08-06 and DEL-10-13 receive first Scope of Work contracts after B1. The graph has no node for them yet (see the return's "for the caller").

### B5. DEL-00-03 SPEC premise (graph D1)

`artifacts/v2/SPEC.md` (CHECKING; SHA-256 `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae`, equal to the `D-PEC-90` pin) is already `STALE_REVIEW_REQUIRED` under SCA-005. SCA-006 adds a premise-only amendment, by the DEL-00-03 owning workflow under an exact-byte gate: the K-03 row L46 ("an enabled consumer owns use and verify-before-rely"), the requirement counts L23 and L62 (46 → 49), the API row L73 (response budgets and the tool-call surface) and the release-proof list L78 (the reliance-advertisement gate). Accepted bytes remain history. D1 also carries the DEL-00-01 ADR premise (SCA-005); SCA-006 leaves `ADRs.md` `CURRENT` for its own causes (IA §7.2).

### B6. Tier-0 profile act (before any PEC tool surface is declared or invoked)

The live tier-0 profile `_DomainEngines/profiles/pec.yaml` (SHA-256 `6858d567ee27bae9b832115a40a41b106a9a2a58a62d661ca0e0c2acff9b314f`; `D-T0-27` O-A, `ADOPTED` / `READ_ONLY`, effective at `d9dc65804`) binds PEC's tool surface:

- L81, a human gate: "profile amendment before any runtime, adapter-client, mutating, proposal, or external-result tool is declared or invoked";
- L104, an open issue: "Before any future adapter or runtime-client invocation, amend this profile with exact inputs, outputs, paths, modes, side effects, failure behavior, result schemas, and human gates";
- L14 `execution_policy: "DECLARED_READ_ONLY_AND_SUMMARY_TOOLS_ONLY"`: only tools the profile declares may run.

PEC-API-007 (SOW-099, DEL-08-06) is such a tool surface. SCA-006 states the requirement (the PRD candidate's PEC-API-007 row, the SOW-099 Notes and the DEL-08-06 envelope note). It writes nothing under `_DomainEngines/**`.

**Planned act (not written or ruled here).**

| Element | Plan |
|---|---|
| Instrument | A tier-0 packet in `_DomainEngines/_DECISIONS/` (next free `D-T0` number when prepared), with a pointer row in PEC's register, in the pattern of `D-T0-27` / `D-PEC-76`. The tier-0 owner rules it. PEC prepares it and brings it to the owner; it is outside PEC's default write scope |
| When | After DEL-08-06's first Scope of Work fixes the tool's shape, and **before** any agent tool-call query tool is declared or invoked in the profile, a harness, the App or an agent configuration. It is not a precondition of checkpoint 3, of the B1 setup packet or of Scope of Work authoring, which declare and invoke nothing |
| Exact change | One declared tool entry for the agent tool-call query surface, with exact inputs (query kinds), outputs (the versioned response carrying the reliance envelope and budgets), paths (reads only PEC's own store through the versioned API), mode `read_only`, side effects (none), failure behavior (the file-fallback signal), result schemas and human gates (enabling it stays consumer-owned); the `open_issues` lines that then misstate what exists; `integration_level` stays `READ_ONLY` and `profile_status` stays `ADOPTED`. The stale header comment (L3 "Candidate only … awaiting owner ruling"), already noticed under SCA-005, may be repaired in the same act if its owner chooses |
| Coupled checks | `tools/practitioner_harness/test_live_baseline.py` asserts `profile_status` `ADOPTED` and `READ_ONLY` for `pec`; the App's `frontend/src/__tests__/contract-pins.manifest.ts` pins `id: "pec"`. An act that keeps these values breaks neither; any change to them needs a conscious pin amendment (the `D-T0-28` precedent) and an App notice |
| Rollback | Revert to the preimage bytes; no tool is declared until the act is effective |

### B7. Metadata re-pin after revision 1.6

After checkpoint-3 acceptance, 63 `_CONTEXT.md` (all but the three A2 mirrors) and all 66 `_REFERENCES.md` name revision 1.5 and PRD v2.3 (the `D-PEC-95` re-pin). They become stale on version only. A later PROJECT_SETUP re-pin (the `D-PEC-95` P generator is the precedent) moves them to revision 1.6 and PRD v2.4, and the two new deliverables' packets are born at 1.6 (B1). The post-change audit reports this as an expected SCA-006 consequence (C4).

### B8. Source and other owners

| Item | Owner | Trigger |
|---|---|---|
| `v2/contracts/api/v1/schema.json`: additive fields for pagination/continuation, stated truncation, the reliance envelope and the `agent` class | later `D-PEC` source packet (PEC-API-003 additive evolution) | when DEL-08-03/08-06/04-03 are built |
| Post-change `audit-decomp` | TASK `audit-decomp` | checkpoint-3 preparation (C4) |
| Decision-register row for the checkpoint-2 act | HELP_HUMAN | after the owner acts (Q-CP2-2) |
| `docs/STATUS.md`, `README.md` | HELP_HUMAN under `D-PEC-88` | after each owner act |
| Work-graph updates (S4 membership, new nodes for B1/B4/B6) | HELP_HUMAN | after the owner acts |

## Derivative status per package

| Package | Owner | Status after the accepted amendment | Next required action |
|---|---|---|---|
| Decomposition + registers | SCOPE_CHANGE | `CURRENT` after checkpoint 3 | A1, C1–C3 |
| PRD v2.4 | owner-adopted; SCOPE_CHANGE applies | `CURRENT` after application | A1, C1 |
| `projects/pec/AGENTS.md` | instruction tranche | `CURRENT` after A4 | A4, C1 |
| 3 direct `_CONTEXT.md` | SCOPE_CHANGE | `CURRENT` after A2 | C1 |
| 63 other `_CONTEXT.md`, 66 `_REFERENCES.md` | PROJECT_SETUP | `STALE_REPIN_REQUIRED` (version only) | B7 |
| DEL-08-06 / DEL-10-13 scaffolds | PROJECT_SETUP (preparation) | `NOT_CREATED` | B1 |
| New dependency rows; DEP-09-06-003 and DEP-10-03-003 quotes | dependency-extract | `STALE_REBUILD_REQUIRED` | B2, B3 |
| 9 affected Scope of Work contracts | WORKING_ITEMS + artifact gates | per B4 (4 rebuild, 5 review) | B4 |
| First SOWs for DEL-08-06, DEL-10-13 | WORKING_ITEMS | `NOT_STARTED` | B4, after B1 |
| DEL-00-03 SPEC | owning workflow | `STALE_REVIEW_REQUIRED` | B5 |
| Tier-0 profile | tier-0 owner | `CURRENT` until a tool is to be declared; then `ACT_REQUIRED` | B6 |
| API schema (`v2/**`) | later D-PEC packet | `STALE_SOURCE_PACKET_REQUIRED` when built | B8 |
| Post-change audit | TASK audit-decomp | `NOT_RUN` | C4 |
| Pointers | SCOPE_CHANGE | unchanged until checkpoint-3 acceptance | A6 |
| Notices | HELP_HUMAN | written with the tranche (A4) | A4 |
| Orientation surfaces | HELP_HUMAN (`D-PEC-88`) | refreshed per act | B8 |

None of these is described as satisfied by the Lane A writes.

## Lane C — closure validation before the root may claim a later phase

### C1. Exact-write containment

After Lane A and before any pointer move:
1. Compare the changed paths with the Lane A allowlist:
   - the decomposition and its four registers;
   - `docs/PRD.md`;
   - the three `_CONTEXT.md`;
   - `projects/pec/AGENTS.md`, the tranche manifest and the three notices;
   - this snapshot folder;
   - the post-change audit folder.
2. Assert that each written file's SHA-256 equals its planned postimage under the slot hash rule.
3. Assert that every other `_CONTEXT.md`, `_STATUS.md`, SOW, SPEC, dependency register, `v2/**`, `pec.yaml` and foreign file is byte-identical.
4. Run `git diff --check`.

### C2. Structural validation

- `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict`: 0 errors, with exactly two DRB-008 warnings, for DEL-08-06 and DEL-10-13, until B1. Evidence: a scratch overlay of the five candidates now gives 0 ERROR and 2 WARNING, both DRB-008, exit 1 by design of `--strict`. The live tree gives 0/0 and exit 0.
- `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <evidence>`: unchanged topology of 111 execution edges and 0 SCCs. The dependency registers do not change in Lane A. The scratch overlay gives exactly this, identical to the live run.

### C3. Exact successor assertions

| Measure | Required value |
|---|---|
| Scope items | 100 (74 IN / 18 OUT / 8 TBD) |
| Packages | 11 |
| Deliverable rows | 68 (64 active / 4 RETIRED) |
| Objectives | 6, statements unchanged |
| ContextBudgetQA rows | 68 |
| Unmapped | 0 IN items without package, deliverable or objective; 0 active deliverables without objectives |
| Union rule | holds on all 64 active rows |
| Active envelopes | S 28 / M 34 / L 2 / XL 0 |
| PKG-04 / 08 / 10 assigned scope | 7 / 8 / 13 |
| Open / resolved issues | 10 / 3 |
| Vocabulary terms | 29 |
| PRD | 49 `PEC-*-NNN` requirements; PEC-K-01, K-02, K-11 and the §12 P1 row byte-identical |
| Stable identity | IDs, names and paths unchanged |

Package-discipline isolation for DEL-08-06 and DEL-10-13 is recorded explicitly (`Amendment_Preview.md` §10).

### C4. Post-change audit and review

1. Dispatch TASK `audit-decomp` with `DECOMP_VARIANT=SOFTWARE`, full scope, expected revision 1.6 and SCA-006 as candidate. Write its output to a new `COV_SCA006_POSTCHANGE_*` snapshot.
2. Compare it with the reused baseline `COV_SCA005_POSTSETUP_2026-09-25_1606` (`Pre_Change_Coverage.json`). The comparison must:
   - attribute the resolution of COV-068, COV-069, COV-072 and COV-073 to `D-PEC-95`, not to SCA-006 (§"Basis currency since checkpoint 1");
   - report as expected SCA-006 consequences the two absent folders (B1), the two stale EvidenceQuotes (B3), and the contexts and references naming revision 1.5 or PRD v2.3 (B7).
3. Then a separate review instance, one that authored nothing, audits the poststate against:
   - checkpoints 1 and 2;
   - the invariants;
   - write containment;
   - pre/post coverage;
   - derivative disposition;
   - closure claims.

### C5. Snapshot and handoff completeness

The following must be present, with hashes recorded:
- `Brief.md`, `Impact_Assessment.md`, `Amendment_Preview.md`, `Propagation_Plan.md`;
- `Amendment_Actions.csv`, `Amendment_Actions_CP2.csv`;
- `Supersession_Delta.csv`, `Supersession_Map.csv`;
- `Pre_Change_Coverage.json`, `Post_Change_Coverage.json`;
- `Decision_Log.md`, `Handoff_State.md`, `RUN_SUMMARY.md`;
- `PRD_V2_4_SUCCESSOR_DIFF.md`, `AGENTS_MD_CANDIDATE_DIFF.md`;
- `CP2_CANDIDATE/`.

### Planned closure state

| Field | Planned value at checkpoint 3 |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` (Lane B open) |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` unless the owner separately authorizes Lane B items |
| `MetadataAlignmentState` | `IN_PROGRESS` (3 direct mirrors done; B7 re-pin open) |
| `AuditState` | as observed by C4 |
| `ReadyForNextPhase` | `NO` |
| Closure verdict | `CLOSED_FOR_SCOPE_CHANGE_ONLY` only after owner checkpoint-3 acceptance; otherwise `OPEN_PENDING_DERIVATIVE_CLOSURE` |

### Failure and rollback

- **Preimage mismatch:** no write; return to checkpoint 2.
- **Validation failure before pointer movement:** the pointers stay on revision 1.5 / SCA-005. The failed candidate state is kept as non-current evidence and is repaired only through a refreshed accepted plan.
- **Instruction-tranche rollback:** a revert PR restores `projects/pec/AGENTS.md` `c9d3b44d…197a` and removes the manifest and notices.

No Git reset, deletion, foreign write or silent downstream repair is a rollback mechanism.

## Supersession binding policy

`Supersession_Delta.csv` holds 16 rows. Impact Assessment §9.3's candidates map as follows:
- SB-1 = D-001 (PEC-K-03);
- SB-2 = D-002 (§8 Agents);
- SB-3 = D-003 (§8 access classes);
- SB-4 = D-018 (C3);
- SB-5 = D-005..D-008 (PEC-ORI-007, PEC-API-006, PEC-API-007 and the §12 gate, all `SUPPLEMENTARY_EXTENSION`);
- SB-6 = D-011 (§15 byte identity).

The exact text needs seven more:

| Row | Binding | Type |
|---|---|---|
| D-009 | §12 P3 "daemon consumers" | `SUPERSESSION` |
| D-010 | §11 metric 4 candidate-consumer definition | `SUPERSESSION` |
| D-012 | §16.6 scope | `SUPPLEMENTARY_EXTENSION` |
| D-014 | the `AGENTS.md` K-02 verify-before-rely sentence, which the Runtime DEL-02-06 Scope of Work pins as a source | `SUPERSESSION` |
| D-020 | SOW-003 | `SUPERSESSION` |
| D-021 | SOW-060 | `SUPERSESSION` |
| D-022 | SOW-080 | `SUPPLEMENTARY_EXTENSION` |

Actions that only mirror a bound fact carry `NO`. These are the deliverable rows, the vocabulary, the objective views, the ADDs of SOW-097..100 and DEL-08-06/10-13 (whose authority facts are the extensions D-005..D-008), and the telemetry and traceability rows.

This differs in form from SCA-005, which bound its SOW rows because its whole PRD change was one action (its Seq 75). SCA-006 splits the PRD loci into Seq 1–13, so the bindings attach to them directly.

## Basis currency since checkpoint 1 (`D-PEC-95`)

The accepted Impact Assessment §2.1 states that the audited inputs of the reused pre-change baseline `COV_SCA005_POSTSETUP_2026-09-25_1606` equal the pre-change state byte for byte. **That statement no longer holds exactly.** The `D-PEC-95` act (PR #924, merge `abfd0897b`; run root `execution/_Coordination/CURRENCY_REV15_D95_2026-09-25/`) changed 119 derivative paths after that audit: both `_LATEST.md` pointers, `_Coordination/_COORDINATION.md`, 42 `_CONTEXT.md`, 64 `_REFERENCES.md` and 10 `Dependencies.csv`.

Three of those paths are in SCA-006 `AffectedFiles`: the DEL-04-03 and DEL-08-03 `_CONTEXT.md` (Seq 30, 32) and the DEL-10-12 `Dependencies.csv` (Seq 54 intake). `git diff 13df8b795 4d5f7b911` on them shows one provenance clause ("then by revision 1.5 …") in each context and a change to the DEP-10-12-003 row only. No text SCA-006 amends changed, and DEP-10-12-004, the Seq 54 intake cell, is byte-identical. The decomposition, its four registers, `docs/PRD.md` and `projects/pec/AGENTS.md` are byte-identical to the Impact Assessment's pins. This candidate is computed from the current bytes at `4d5f7b911`, including the `D-PEC-95` provenance lines.

Consequence for checkpoint 3: the reused baseline still carries COV-068 (42 contexts at revision 1.4), COV-069 (64 references at revision 1.4), COV-072 (19 non-verbatim EvidenceQuotes) and COV-073 (stale-conservative SCA-005 handoff surfaces and pointers). The `D-PEC-95` act addressed them without a further audit (its ruling: "no re-audit"). The SCA-006 post-change audit is the first audit to observe the post-`D-PEC-95` state. Its pre/post comparison must attribute the resolution of COV-068/069/072/073 to `D-PEC-95`, not to SCA-006, and must not report them as SCA-006 effects (§C4).

## Foreign-surface notices (PEC does not write these beyond A4's notice files)

| Receiving loop | Basis | Route |
|---|---|---|
| Root | `D-PEC-90` grant item 2 (Root and App notices). Root `AGENTS.md`: "Notify each affected project loop whose authority corpus or contract mirrors pin changed instructions". Root `AGENTS.md` L54–55 ("reliance remains grounded in the source records and their authority") is arguably compatible, and that reading is Root's to confirm (IA §7.4) | A4 notice; non-binding |
| App | `D-PEC-90` grant item 2; PEC-K-03 was adopted under `D-PEC-67` K03-A in coordination with consumer loops | A4 notice; non-binding; the App decides whether and when its harness consumes or exposes PEC |
| Runtime | Not in `D-PEC-90`'s grant. The basis is Root `AGENTS.md`'s instruction-change notice rule. Runtime's DEL-02-06 Scope of Work names `projects/pec/AGENTS.md`, `Deliverables.csv` and `ScopeLedger.csv` as read-only sources (L459–461), and its `_run_records/DEL-02-06-RUNTIME-SPEC-001/clients/SOURCE_PINS.json` pins them as S4–S6. SCA-006 changes all three. The `D-PEC-94` instruction tranche routed a Runtime notice on the same basis. PEC-API-007 also touches the tool path that Root CONTRACT K-RUNTIME-1 and the Runtime's application-tools interface own; PEC adds no Runtime path | A4 notice; non-binding; included in the Q-CP2-A acceptance as the manager's recommendation |
| Piping | none: no Piping file pins these surfaces | no notice |
| Tier-0 (`pec.yaml`) | L81 human gate | its own act (B6); no notice now |

## Checkpoint-2 owner question set

The owner answers these as one package. The settled selections are not re-asked: DQ-a, ENV-a, BUD-a, GATE-a, INS-a, R-C excluded, and the envelope re-assessment of DEL-08-03 from S to M carried in the accepted intake. Nothing here asks about CHECKING, ISSUED or acceptance of any deliverable.

**Q-CP2-A — accept the exact amendment and propagation plan together.** Accept, as one checkpoint-group-2 decision, the package at these SHA-256 values (all in `_ScopeChange/SCA-006_2026-09-25_1912/`):

| Artifact | SHA-256 |
|---|---|
| `Amendment_Preview.md` | `737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4` |
| `Amendment_Actions_CP2.csv` | `d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de` |
| `Supersession_Delta.csv` | `e69f97814294ccd993fceff12cdf992623156c33ca4993adb103b61774e5977b` |
| `PRD_V2_4_SUCCESSOR_DIFF.md` | `a743a5273c66dc679a99888c4dc2b865a318dab64fcaaa7768ecb71f35696a4c` |
| `AGENTS_MD_CANDIDATE_DIFF.md` | `7c57a1b2c02c872fae6f778beeddf7f812809d469b504e34d1e6f79bbb48a158` |
| `CP2_CANDIDATE/docs/PRD.md` | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `CP2_CANDIDATE/AGENTS.candidate.md` (if Q-CP2-1 (a)) | `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` |
| `CP2_CANDIDATE/AGENTS.candidate_without_I1.md` (if Q-CP2-1 (b)) | `a8b8d906f7df22f35fc8489a04fcb5476700e919af896c8256c0b713bf961188` |
| `CP2_CANDIDATE/_Decomposition/SOFTWARE_DECOMP.md` | `4eed1247de47d1921e5526ef5027c12d504bffd4b8393b59645bb973fac62d71` |
| `CP2_CANDIDATE/_Decomposition/ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `CP2_CANDIDATE/_Decomposition/Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `CP2_CANDIDATE/_Decomposition/ContextBudgetQA.csv` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `CP2_CANDIDATE/_Decomposition/Companion_Inventory.csv` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
| `Propagation_Plan.md` (this file; a file cannot quote its own hash) | quoted in `Decision_Log.md` row SCA006-CP2 and the run return |

Acceptance means:
- **The PRD v2.4 candidate is adopted** for application with the decomposition during checkpoint-3 preparation; its Status row names this group-2 snapshot.
- **The S4 membership is fixed** as §B4 states.
- **The instruction tranche and its three notices** (Root, App, Runtime) go at checkpoint 3.
- **Lane A only is authorized.** Lane B stays recorded as open work, and no pointer moves.

The hash values are computed with every slot at its default. If the owner acts on another date, the slot hash rule applies and no other byte changes. Checkpoint 3 remains the owner's audited-poststate acceptance. **Recommendation: accept.**

Genuinely open choices besides Q-CP2-A:

| # | Choice | Options | Recommendation |
|---|---|---|---|
| Q-CP2-1 | Whether the work-graph node I1 residual corrections ride the SCA-006 instruction tranche. I1 has two parts: (i) "Implementation does not exist yet" becomes a verified statement naming the owner-ruled `v2/**` source slices (`D-PEC-74`, `75`, `77`, `84`, `85`, `87`, `89`, `91`); (ii) the pre-v3 names in the Primary Agents table become Root's roles with their current workflows or skills, per `workflows/index.json` `legacy.retiredRoles` (verified at `origin/main` `7f33b4dd5`, after the Root Wave 2a tranche retired `software-bounded-implementation`). They are separated in `AGENTS_MD_CANDIDATE_DIFF.md` §4 as the only difference between the two candidates | (a) ride: apply `AGENTS.candidate.md`, and graph node I1 completes with R3; (b) do not ride: apply `AGENTS.candidate_without_I1.md`, and I1 stays PLANNED for its own tranche | **(a)** — Root `AGENTS.md` requires a tranche and manifest for every instruction change, so one tranche costs one set of checks and notices instead of two. Both corrections are factual, they change no fence, check or authority, and the work graph already allows I1 to ride R3 |
| Q-CP2-2 | Which instrument opens PEC's write fence for Lane A. `projects/pec/AGENTS.md` requires an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback for every write outside the default surfaces | (a) the checkpoint-group-2 decision snapshot, with a D-PEC register row that HELP_HUMAN adds pointing to it, is that packet (the `D-PEC-92` precedent for SCA-005). It opens A1, A2, A4, A5 and A6 (A6 only after checkpoint 3), plus C4's `COV_SCA006_POSTCHANGE_*` folder, with Lane C as verification and §"Failure and rollback" as rollback. It does **not** open B1 (PROJECT_SETUP for DEL-08-06 and DEL-10-13) or any other Lane B item; (b) a separate D-PEC ruling adopting the same bytes and opening the same paths | **(a)** — one exact gate. The plan already names the paths, acts, checks and rollback, and the PRD candidate's Status row cites the group-2 snapshot |
