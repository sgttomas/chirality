---
amendment_id: SCA-006
doc_kind: scope_change.run_summary
decomp_variant: SOFTWARE
checkpoint_group: 3
created: 2026-09-26
status: checkpoint_3_prepared_awaiting_owner
---

# SCA-006 — checkpoint-group-3 run summary (audited poststate, pre-acceptance)

This summary was prepared by WORKING_ITEMS under brief B6 (work-graph node R3 of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`). The brief's SHA-256 is `8bdc718105f05dd2f72378e50fea246eb99a38a937938da72afa221bb8872df4`, read from `origin/main` `94e9255b6`.

The run used the scope-change workflow at its **pinned** edition, read from Git at `4d5f7b911`:
- `WORKFLOW.md` `58f5d1d5…7a90`;
- `contract.md` `4453a719…4f344d02`;
- `method.md` `34187e83…d167f5`.

The owner chose that edition ("SCA-006 pinned"; group-2 amendment 1). The post-change audit used the **current** `audit-decomp`, which is a separate workflow:
- `WORKFLOW.md` `7ba6291c…246b`;
- `contract.md` `704929c7…4e75`;
- `method.md` `51a0c69b…8827`.

The owner was told about this mix of editions before choosing.

**It accepts nothing.** Revision 1.5, SCA-005 as `_LATEST.md` and fences F-PEC-1..4 remain the accepted basis until the owner accepts checkpoint 3. Revision 1.6, PRD v2.4 and the instruction tranche are applied as the candidate poststate. The application date is 2026-09-26 (local date, America/Edmonton).

## 1. Amendment

SCA-006 writes the `D-PEC-90` R-A direction, operational reliance on PEC data, into PEC's text:
- **PRD v2.4:** PEC-K-03, the §8 `agent` class, PEC-ORI-007, PEC-API-006, PEC-API-007, and the standing §12 reliance-advertisement gate. The PRD goes from 46 to 49 requirements.
- **Decomposition revision 1.6:** SOW-097..100, DEL-08-06 and DEL-10-13, DEL-08-03 re-enveloped S → M, and the C3, PKG-04/08/10, objective-view, telemetry and vocabulary changes.
- **`projects/pec/AGENTS.md`:** Seq 14–17 plus the I1 corrections (Q-CP2-1 (a)), plus the group-2 amendment-1 Remaining-sections correction.

Authority: the owner's checkpoint-2 act "SCA-006 CP2: accept; Q1 a; Q2 a" (2026-09-25). The packet is `D-PEC-97` with `../checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`. Group-2 amendment 1 (2026-09-26) is at `../checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`.

Pointer posture: `ACCEPTED_PREDECESSOR`. `_ScopeChange/_LATEST.md` names SCA-005 (`e92b3b16…7d24`) and is unchanged.

## 2. Preconditions (checked before the first write)

Every precondition held. The script is `CP3_EVIDENCE/precheck.py`, and it reported 0 fails.
- **Live preimages** matched: the decomposition, the four registers, the PRD, `AGENTS.md`, both `_LATEST.md` files and the three A2 `_CONTEXT.md` files.
- **Group-2 manifest:** every artifact had its listed hash. `Decision_Log.md` and `Handoff_State.md` had been updated in place by the acts, as the manifest's boundary column states.
- **`origin/main`** carried `D-PEC-97` and amendment 1 with its §"Verification rule".
- **Reliance-hold preflight** (`CP3_EVIDENCE/preflight.py`): all 66 runs returned `ALLOW`. That is 22 write targets under each of `exact-correction-preparation`, `candidate-validation` and `dispatch-for-production`. The hold register has a header and no rows.

## 3. Actions taken (Lane A)

| Lane | Path | Preimage | Postimage |
|---|---|---|---|
| A1 | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` | `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59` |
| A1 | `…/_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| A1 | `…/_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| A1 | `…/_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| A1 | `…/_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
| A1 | `projects/pec/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| A2 | `…/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md` | `a505c268…63da` | `b28ada4674662515ed7f975cb59c1ee2c2f9cac3c4bcf0d919ced22af79a7b22` |
| A2 | `…/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md` | `151e1e34…3985` | `74b12e7358a71000b8cd544f2db8a736289e7ca4b1e3f94dbadbf98154292d22` |
| A2 | `…/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md` | `4644758f…c73d` | `95fa815a31a38e59c001dd3596bc47053508cd3ff59c9d3eae67d64ba9d037b5` |
| A3 | none: no `_STATUS.md`, no lifecycle change | — | — |
| A4 | `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| A4 | `docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml` | new (draft `852b1d5b…bc45`) | `2b29af181947ba0ed75cd83a286c56a2863802d1d6a7e5b3ca9ab82330cdee74` (first written as `f7f48690…0a72`; its `group2_amendment_1` block was then updated in place, at HELP_HUMAN's direction, to record the owner's hunk approval) |
| A4 | `execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` (Root) | new (draft `43cfa318…b930`) | `b3c60bf489e41d45465bd38a0a7f3f3ca73ea4d392f987eff84a95bd888fc601` |
| A4 | `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | new (draft `eb927e1f…704a`) | `af4f63426b55a96c4f18fee702b9af8eb5394b2b531dfddef3f8f090622f68ef` |
| A4 | `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-26_PEC_SCA-006_OPERATIONAL_RELIANCE.md` | new (draft `385e5e2f…c8bc`) | `e883efac1829f0f2a10cceae778c92cd6baec6a37d1f4e6349442dd4c8f7bb93` |
| A5 | `Supersession_Map.csv` (this folder; accumulator; 45 rows = 29 SCA-005 + 16 SCA-006; 0 findings) | new | `010ce5c423530123f923413dbfad03ce70fc0ba0c072ee7726f7718847caab92` |
| A5 | `Post_Change_Coverage.json` (byte copy of the audit's `coverage_summary.json`) | new | `b9a068c078ba6ca4daf5d6129c2823141cae787f7770068e1d70644b13a09cf0` |
| A5 | `AGENTS_MD_AMENDMENT1_DIFF.md`, `CP3_EVIDENCE/`, this file; `Decision_Log.md`, `Handoff_State.md` (additive) | — | recorded in `Handoff_State.md` §"Checkpoint-3 preparation" |
| A6 | not done: both `_LATEST.md` pointers unchanged | — | — |

Every write was made by a script that asserts the preimage, the candidate and the postimage by hash, and aborts before writing on any mismatch. The scripts are in `CP3_EVIDENCE/`:
- `apply_a1_a2.py`;
- `apply_a4_agents.py`;
- `extract_drafts.py` with `apply_a4_manifest_notices.py`.

### 3.1 Slot values (proved under each document's slot rule)

| File | Slot | Default | Applied | Rule |
|---|---|---|---|---|
| `SOFTWARE_DECOMP.md` | front-matter `date:` (L7), §7 `Revision` row (L574), §11 DL-21 date cell (L700) | `2026-09-25` | `2026-09-26` | application date (brief B6 A1). See the A6 note below |
| `SOFTWARE_DECOMP.md` | `status:` (L5), `accepted:` (L8) | accepted values | the two pre-acceptance lines of `Amendment_Preview.md` | pre-acceptance application state. The pre-acceptance variant at defaults is `3ad0de68…a8b` |
| `docs/PRD.md` | S1–S4 and the group-2 folder token | `2026-09-25` / `SCA-006_GROUP-2_2026-09-25` | unchanged | act-date values; the written file equals the candidate byte for byte |
| `projects/pec/AGENTS.md` | L6 `amended:` first token | `2026-09-25` | `2026-09-26` | application-date slot (`AGENTS_MD_CANDIDATE_DIFF.md` §9) |
| `projects/pec/AGENTS.md` | L209 group-2 folder token | `SCA-006_GROUP-2_2026-09-25` | unchanged | the actual folder name |
| manifest | `tranche_id`, file name, notice dates | `20260925` / `2026-09-25` | `20260926` / `2026-09-26` | application date |
| manifest | `date` | `2026-09-25` | `2026-09-26` | application date |
| manifest | `basis` | `4d5f7b911…` | `94e9255b68d6cda15926c7ee0187d6e9a759a43b` | checkpoint-3 basis |
| manifest | CP2-ACT, CP2-VARIANT | slot text | `'SCA-006 CP2: accept; Q1 a; Q2 a'`; `AGENTS.candidate.md` with I1 | the group-2 record |
| manifest | `m2_gate.authorization_date` | `2026-09-25` | `2026-09-25` (kept) | the date of the checkpoint-2 act that authorized the tranche (confirmed by HELP_HUMAN). The amendment-1 block carries the 2026-09-26 direction |
| notices | manifest path date part | `20260925` | `20260926` | application date |
| notices | group-2 folder token | `SCA-006_GROUP-2_2026-09-25` | unchanged | the actual folder name |

**Slot proofs:**
- *Decomposition:* substituting the defaults back gives the pre-acceptance variant `3ad0de68…`. Restoring the two accepted lines as well gives `4eed1247…`. With the application-date slots filled, the accepted candidate hashes to `86de50c3b56812dec9537210c0202ec9efc98aac7b328a8736cac8a6c688ecb3`.
- *`AGENTS.md`:* the accepted candidate with its slot filled is `6f6f2ed1c0ed6e009323beaa004a79b72b717b4cd9431199eb2f9b990cf264e6`. Taking out the amendment-1 hunk and restoring the slot default gives `49ce993a…070d`.
- *Manifest and notices:* removing the one named amendment-1 addition and restoring the slot defaults gives each draft's hash.

**A6 note (decomposition date slots).** `Amendment_Preview.md` binds `date:`, the §7 Revision row and the DL-21 date to the checkpoint-3 acceptance date. The brief directed the application date, and HELP_HUMAN confirmed that choice. If the owner accepts checkpoint 3 on a date later than 2026-09-26, the A6 act substitutes the acceptance date at exactly these three loci, under the preview's slot rule, when it restores the two accepted front-matter lines.

### 3.2 The amendment-1 hunk (owner approval gate: satisfied)

**Approval gate satisfied.** Amendment 1 requires the owner's explicit approval of the exact hunk before the application PR merges. The owner gave it on 2026-09-26, verbatim: "approve hunk". HELP_HUMAN had presented the exact paragraph, the dropped clause and the COV-083 observation. HELP_HUMAN transcribed the act under K-AUTH-1; it is recorded in `Decision_Log.md` row SCA006-G2-A1 and in the manifest's `group2_amendment_1.owner_hunk_approval`. The approved postimage is `projects/pec/AGENTS.md` `4400c4e9…139c`.

The hunk replaces exactly `CP2_CANDIDATE/AGENTS.candidate.md` L261–270, which is live preimage L241–250. It occupies L261–272 of the applied file. The full record is `AGENTS_MD_AMENDMENT1_DIFF.md`. Before:

```text
PEC's deliverable `_STATUS.md` `## Remaining` sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). They are no longer a work-selection surface: steering
selects the undertaking and its graph accounts for the Remaining items it
touches. A Remaining item's own gate markers still bind that item. When an
undertaking completes or changes an item, update it under the packet that
opens that `_STATUS.md`; without that grant, record the consequence in the
graph and bring it to the owner. Record new open scope in the graph and its
governing records rather than as a new Remaining entry. Retiring the sections,
as App and Piping did, is a separate owner-directed undertaking.
```

After (verbatim):

```text
PEC adds no new deliverable `_STATUS.md` `## Remaining` sections or entries
(owner direction of 2026-09-26, recorded as SCA-006 checkpoint group 2
amendment 1). No PEC feed profile reads them, so the coordination plane does
not scan them, and they are not a work-selection surface. Steering selects the
undertaking; record new open scope in its work graph and governing records.
Until any retirement ruling, the existing sections stay in place as
deliverable-local records of open scope under their owning decisions (for
example `D-PEC-83`). A Remaining item's own gate markers still bind that item.
Update an item only under the packet that opens that `_STATUS.md`. If an
undertaking completes or affects an item without such a grant, record the
consequence in the graph and bring it to the owner. Retiring the sections, as
App and Piping did, is a separate owner-directed undertaking.
```

**Dropped clause (disclosed).** The candidate's "its graph accounts for the Remaining items it touches" is not carried. The owner said "no need to scan for them", and that clause implies each undertaking's graph looks for Remaining items. The duty that still applies when an undertaking does touch an item is kept: update the item under the opening packet, or record the consequence in the graph and bring it to the owner.

**Known tension (audit COV-083, INFO).** Revision 1.6 keeps, unchanged from 1.5, the text "PEC's own `pec` row declares the `remaining-loop` profile now". It appears in:
- SOW-094 (§2 L259; `ScopeLedger.csv` row SOW-094);
- the DEL-01-06 Description;
- the §9 "feed profile" examples.

The hunk's sentence "No PEC feed profile reads them" is true of the code: `projects/pec/v2/config/loops.json` declares no feed profiles, and no `v2/**` file names `remaining-loop`. It is also the owner's direction. It differs, however, from that design text. Since the audit ran, `D-PEC-96` has been ruled (2026-09-26, "D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults"; `_Coordination/_DECISIONS/D-PEC-96_RULING_2026-09-26.md`, SHA-256 `852057f0…399e`, on `origin/main` through PR #946). PEC's row is migrated, with no `remaining-loop` profile. That ruling changes no decomposition text and leaves the "declares `remaining-loop` now" sentences to graph node S2 (the DEL-01-06 rebuild) and to a later PEC scope change. SCA-006 cannot correct them without enlarging its accepted amendment. The audit output, which says the basis change "still needs its ruling", is not edited. See Q-CP3-1. HELP_HUMAN presented this observation to the owner before the hunk was approved.

## 4. Validation (Lane C)

| Check | Command (cwd = worktree root; `python3` 3.13.7) | Exit | Result |
|---|---|---:|---|
| C1 containment | `CP3_EVIDENCE/c1_containment.py` over `git diff --name-status origin/main HEAD` (after merging `origin/main` `f90320c1d`, so the diff is this PR's own changes) | 0 | 43 changed paths, all inside the Lane A allowlist or B6 returns; 34 hash checks pass (14 planned postimages, the manifest at `2b29af18…`; 18 frozen checkpoint-1/2 artifacts; both `_LATEST.md` unchanged); no deletion |
| C2 registers | `python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict` | 1 (by design of `--strict`) | **At the basis `94e9255b6`:** 0 ERROR, exactly 2 WARNING DRB-008 (DEL-08-06, DEL-10-13), as planned. **At the merged head (validator `869df1d5…` after Root `D-GOV-48`, PR #942):** 0 ERROR, 2 DRB-008 as above, plus 26 WARNING XRG-013 (OUT/TBD ledger items without a PackageID). The 26 are pre-existing: they are exactly the revision-1.5 OUT/TBD items without a PackageID (same 26 IDs), and SCA-006 does not cause them. SOW-097..100 are IN, with packages PKG-04/08/08/10, so they add no XRG finding. Per PEC's `NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md`, the owner defers action and PEC's registers are not edited |
| C2 closure | `python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <scratch>` (basis and merged head) | 0 | 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs; unchanged |
| C3 assertions | `python3 CP3_EVIDENCE/c3_assert.py <preimage dir>` (the preimages are `git show 94e9255b6:<path>`) | 0 | 31/31 PASS (see below) |
| C4 audit | TASK `audit-decomp` (current edition), output `../../_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/` | — | `WARNINGS` / closure readiness `WARN`: 0 BLOCKER, 3 WARNING, 71 INFO, 12 EXPECTED_CONSEQUENCE |
| C4.3 separate review | fresh `pec-reviewer`, authored nothing; reviewed `c5efad489` | — | **PASS WITH MINOR**, 0 BLOCKING (2 MINOR, 7 NOTE). Saved verbatim with the manager's dispositions in `CP3_EVIDENCE/C4_3_REVIEW.md` |
| C5 completeness | `python3 CP3_EVIDENCE/c5_completeness.py` | 0 | every §C5 artifact present with its hash; all seven state fields in this file and in the `Handoff_State.md` checkpoint-3 section (hashes in `Handoff_State.md`) |
| A4 entrypoints | `python3 tools/validation/validate_instruction_entrypoints.py .` | 0 | PASS |
| A4 G4, CI mode | `python3 tools/validation/validate_instruction_tranche_manifest.py` (rerun on the merged head with the final manifest) | 0 | PASS, 126 manifests; INFO over-declaration for `projects/pec/AGENTS.md` and the notices (as the `D-PEC-94` precedent) |
| A4 G4, diff mode | `… --base origin/main --head HEAD --added-manifests-only` (merged head; also at the basis with `--base 94e9255b6`) | 0 | PASS: 43 changed paths, 1 on the instruction surface, covered by 1 added manifest |
| A4 receipts | `PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | 0 | VALID; the closed ledger is unchanged |
| A4 whitespace | `git diff --check origin/main HEAD` | 2 | 46 trailing-whitespace reports, all in `Supersession_Map.csv`: the accumulator writes CRLF line endings, as SCA-005's map has. The map is generated and never hand-edited (plan §A5), and cosmetic whitespace is not a gate (`projects/pec/AGENTS.md`). With that file excluded, the check exits 0. The interim return's "clean" was measured before the map existed; it is superseded |
| extra | `pytest -q tools/validation/test_validate_instruction_entrypoints.py tools/validation/test_validate_pec_loop_receipts.py` | 0 | 33 passed |
| extra | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | 0 | no finding names a changed file |

**C3 results (31/31 PASS):**
- 100 scope items (74 IN / 18 OUT / 8 TBD), in 11 packages;
- 68 deliverable rows (64 active / 4 RETIRED) and 68 ContextBudgetQA rows;
- active envelopes S 28 / M 34 / L 2 / XL 0;
- 0 IN items without a package, deliverable or objective, and 0 active deliverables without objectives;
- the union rule holds on 64/64 rows;
- PKG-04/08/10 assigned IN scope 7/8/13;
- 10 open and 3 resolved issues, and 29 vocabulary terms;
- 6 objectives, statements byte-identical to revision 1.5;
- every revision-1.5 ID, name and package retained, with the new IDs append-only (SOW-097..100, DEL-08-06, DEL-10-13);
- 66 folders, none new;
- 49 unique PRD requirements, with the PEC-K-01, PEC-K-02, PEC-K-11 and §12 P1 rows byte-identical to v2.3.

Package-discipline isolation for DEL-08-06 and DEL-10-13 is recorded in `Amendment_Preview.md` §10. The audit found no violation.

## 5. Pre-change vs post-change

The baseline is `COV_SCA005_POSTSETUP_2026-09-25_1606`. `Pre_Change_Coverage.json` (`b7b432a2…`) equals its `coverage_summary.json`. The post-change audit is `COV_SCA006_POSTCHANGE_2026-09-26_0051`; its `coverage_summary.json` is `b9a068c0…` and its `RUN_SUMMARY.md` is `f97bde4e…`.

| Measure | Baseline | Post-change |
|---|---|---|
| Issues (BLOCKER / WARNING / INFO / EXPECTED_CONSEQUENCE) | 0 / 3 / 70 / — | 0 / 3 / 71 / 12 |
| Forward deliverable coverage | 100 % (66/66) | 97.06 % (66/68; the two B1 deliverables have no folder) |
| Context fidelity | 66/66 | 66/66 |
| Strict validator | 0 / 0 | 0 errors / 2 DRB-008 |
| Closure | 111 / 66 / 0 SCC | byte-identical |

- **Intended amendments occurred.** C3 passes, and the registers and PRD are byte-identical to the accepted candidates. The decomposition differs from its candidate only at the pre-acceptance and slot lines (L5, L7, L8, L574, L700).
- **No unintended coverage regression, and no new orphan.** The only coverage drop is the two deliverables whose PROJECT_SETUP is deferred (B1).
- **The 3 WARNINGs are pre-existing** Check-6 artifact-location findings, carried from the baseline: COV-008 (DEL-01-03), COV-010 (DEL-01-05) and COV-046 (DEL-08-02).
- **Baseline COV-068, COV-069 and COV-072** are resolved by `D-PEC-95` (N2 for the first two, N3 for COV-072), not by SCA-006.
- **Baseline COV-073** is partly resolved. `D-PEC-95` N1 made the pointers current. The SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` stay byte-identical under the ruling's option P, and are carried as COV-086 INFO. None of these four is reported as an SCA-006 effect.
- **The 12 EXPECTED_CONSEQUENCE rows** each cite `D-PEC-97` and a plan section:
  - B1: COV-003, COV-004, COV-073 and COV-074 (the two absent folders);
  - B3: COV-075 and COV-076 (exactly DEP-09-06-003 and DEP-10-03-003; DEP-09-06-004 and DEP-10-12-004 stay verbatim);
  - B7: COV-077 (63 `_CONTEXT.md` at 1.5) and COV-078 (66 `_REFERENCES.md` at 1.5 / PRD v2.3);
  - A2: COV-079 (the three mirrors already say revision 1.6 before acceptance; rollback must include those lines);
  - B2: COV-080 (no register traces SOW-097..100 yet);
  - A6/A1: COV-084 (pointers on 1.5 / SCA-005; pre-acceptance front matter);
  - A5/C5: COV-085 (the snapshot was mid-A5 while the audit ran).
- **Reading notes on the audit.** The new audit reuses the IDs COV-068, COV-069, COV-072 and COV-073 for different findings. `PrePost_Comparison.md` maps them correctly; wherever this summary names those IDs, it means the baseline findings. The C4.3 reviewer argued that COV-083 could be WARNING rather than INFO, because the same poststate's `AGENTS.md` hunk contradicts that text. The audit output is not edited; the manager carries the point as Q-CP3-1.
- **New INFO findings:**
  - COV-083: the `remaining-loop` design text (§3.2).
  - COV-001 and COV-002: the first run of the now-required `audit_structure.py`. The packages lack the SHOULD-level `0_References/`, `2_Checking/` and `3_Issued/` folders, and the tool roots `_Aggregation/`, `_Estimates/` and `_Sources/` are absent. Both conditions predate SCA-006.

## 6. Recommended downstream reruns (not executed; `DownstreamRerunState = FROZEN`)

Each item below needs its own owner-ruled packet. None is satisfied by Lane A.

| Item | Owner | What |
|---|---|---|
| B1 | PROJECT_SETUP (preparation skill) under a later `D-PEC` packet | scaffold DEL-08-06 and DEL-10-13 |
| B2 | dependency-extract | rows for the new deliverables and the SOW-097..100 anchors (closes COV-080) |
| B3 | dependency-extract | re-quote DEP-09-06-003 and DEP-10-03-003 |
| B4 | WORKING_ITEMS + artifact gates | the 9 affected Scope of Work contracts (graph S4/D1), and first contracts for DEL-08-06 and DEL-10-13 after B1 |
| B5 | DEL-00-03 owning workflow | the SPEC premise (46 → 49; K-03 row; API and release-proof rows) under the exact-byte gate |
| B6 | tier-0 owner | a `pec.yaml` tool entry before any agent tool-call query tool is declared or invoked |
| B7 | PROJECT_SETUP | re-pin 63 `_CONTEXT.md` and 66 `_REFERENCES.md` to revision 1.6 / PRD v2.4 |
| B8 | later `D-PEC` source packet | additive `v2/contracts/api/v1/schema.json` fields when the deliverables are built |
| COV-083 follow-up | a later PEC scope change (`D-PEC-96` now ruled: PEC's row migrated) | correct SOW-094, the DEL-01-06 Description and the §9 "feed profile" example for the `remaining-loop` direction |

## 7. State fields

| Field | Value | Note |
|---|---|---|
| `DecompositionTruthState` | `COMPLETE` | revision 1.6 applied (pre-acceptance front matter until A6) |
| `DerivativePackageState` | `INCOMPLETE` | Lane B open |
| `ContentRemediationState` | `NOT_REQUIRED` | SOFTWARE variant |
| `DownstreamRerunState` | `FROZEN` | no Lane B item authorized |
| `MetadataAlignmentState` | `IN_PROGRESS` | 3 direct mirrors done; the B7 re-pin is open |
| `AuditState` | `WARNINGS` | 0 BLOCKER; the 3 WARNINGs are pre-existing and unrelated to SCA-006 |
| `ReadyForNextPhase` | `NO` | |
| Closure verdict | `OPEN_PENDING_DERIVATIVE_CLOSURE` now | `CLOSED_FOR_SCOPE_CHANGE_ONLY` only after the owner's checkpoint-3 acceptance (plan §"Planned closure state") |

## 8. Repository-change evidence

- **PR:** https://github.com/sgttomas/chirality/pull/943, branch `claude/pec-sca006-cp3-execution`, cut from `origin/main` `94e9255b6`. It later merged `origin/main` `f90320c1d` (Root `D-GOV-48`, the `D-PEC-96` ruling, workflows wave 3), with no overlap with any SCA-006 path.
- **Rerunning `CP3_EVIDENCE` scripts:** set each script's `R` constant to the value of `git rev-parse --show-toplevel` (they were written against this worktree's absolute path).
- **Modified or added paths:** exactly those in §3, plus the audit folder and the B6 return files.
- **The hunk-approval gate is satisfied** ("approve hunk", 2026-09-26; §3.2). Before merge, HELP_HUMAN still reviews the notices and adds its `docs/STATUS.md` correction under `D-PEC-88`. The ordinary merge conditions (required CI and independent review) still apply. Checkpoint 3 remains the owner's.
- **Recommended commit message** (for the checkpoint-3 act):

```text
scope: SCA-006 — operational reliance on PEC data (PRD v2.4, decomposition revision 1.6, AGENTS.md tranche)

Variant: SOFTWARE
Actions: 54 (ADD:12, MODIFY:42)
Affected entities: SOW-003/060/080, SOW-097..100, DEL-04-03, DEL-08-01, DEL-08-03, DEL-08-06, DEL-10-13, PKG-04/08/10, OBJ-001/002, C3, OI-006, vocabulary
```

## 9. Checkpoint-3 owner question

**Q-CP3-A: accept the audited poststate.** Accept, as the checkpoint-group-3 decision, SCA-006's audited poststate:
- **Live decomposition revision 1.6:** `SOFTWARE_DECOMP.md` `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59`. This is the pre-acceptance form; at A6 the two accepted front-matter lines are restored, giving `86de50c3…ecb3` with the 2026-09-26 date slots.
- **Registers:** `ScopeLedger.csv` `1d24a4b8…e916e`, `Deliverables.csv` `94ee5d18…9805`, `ContextBudgetQA.csv` `93b0bb07…7c7c`, `Companion_Inventory.csv` `1597ceec…8662`.
- **PRD v2.4:** `docs/PRD.md` `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`.
- **Instruction file:** `projects/pec/AGENTS.md` `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`. It includes **the exact amendment-1 hunk quoted verbatim in §3.2**. The owner explicitly approved that hunk on 2026-09-26 ("approve hunk"), so amendment 1's pre-merge gate is satisfied. The dropped clause and the COV-083 tension are disclosed there.
- **Audit:** `_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/`, verdict `WARNINGS` (0 BLOCKER / 3 pre-existing WARNING / 71 INFO / 12 EXPECTED_CONSEQUENCE). Its C4.3 separate review is in `CP3_EVIDENCE/C4_3_REVIEW.md`.
- **Closure state:** the §7 fields. The verdict becomes `CLOSED_FOR_SCOPE_CHANGE_ONLY` on acceptance.
- **Known Lane B consequences:** B1 (the two folders), B2, B3 (two quotes), B4, B5, B6, B7 (the revision-1.6 re-pin) and B8, all `FROZEN` until their own packets.

On acceptance, HELP_HUMAN performs A6:
- `_Decomposition/_LATEST.md` becomes the revision-1.6 handoff.
- `_ScopeChange/_LATEST.md` names SCA-006.
- The two front-matter lines return to their accepted values. If the acceptance date is later than 2026-09-26, the acceptance date is also substituted at the three decomposition date slots (§3.1).

**Rollback if checkpoint 3 is returned.** Use the plan's §"Failure and rollback". Also name the provenance lines that anticipate acceptance: the three A2 `_CONTEXT.md` lines "then by revision 1.6 (`current_basis`, SCA-006 successor)" (audit COV-079), and the notices' present-tense "revision 1.6 adds …" wording. The notices would need a withdrawal notice, since they are foreign files.

**Recommendation: accept.**

Genuinely open choices besides Q-CP3-A:

| # | Choice | Options | Recommendation |
|---|---|---|---|
| Q-CP3-1 | The `remaining-loop` design text in revision 1.6 (COV-083). SOW-094 (decomposition L259, `ScopeLedger.csv` L72), the DEL-01-06 Description (`Deliverables.csv` L10) and the §9 example (L652) still say PEC's own row declares `remaining-loop` now. This contradicts the approved `AGENTS.md` hunk and the `D-PEC-96` ruling of 2026-09-26 (PEC's row migrated) | (a) accept revision 1.6 as accepted at checkpoint 2, knowingly carrying this drift, and record the correction for a later PEC scope change (the `D-PEC-96` ruling already routes it there and to graph node S2); (b) return SCA-006 to checkpoint 2 to add the correction, which enlarges the accepted amendment and needs a new group-2 act | **(a)**. The text changes no code (`v2/config/loops.json` declares no `remaining-loop` profile). SCA-006 may not enlarge its accepted amendment. The follow-up is recorded in §6 and in `Handoff_State.md` |
| Q-CP3-2 | The audit pointer `_Evaluation/DecompCoverage/_LATEST.md`, which names `COV_SCA005_POSTSETUP_2026-09-25_1606`. `D-PEC-97` opens the two A6 pointers but not this one | (a) name it in the checkpoint-3 acceptance, so that HELP_HUMAN moves it to `COV_SCA006_POSTCHANGE_2026-09-26_0051` with A6 (the audit has 0 BLOCKERs, which is the audit contract's condition); (b) leave it until a later packet | **(a)**. It keeps the audit pointer consistent with the accepted poststate at no extra cost |

Nothing here asks about CHECKING, ISSUED or acceptance of any deliverable.
