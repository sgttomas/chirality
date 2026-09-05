# PREVIEW — N1-TASK-DEL-08-04 — DEL-08-04 dependency register (report-only; amendment v1.1 rerun)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-08-04` (run `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, node N1; parent HELP_HUMAN) |
| Amendment | v1.1 (`AMENDMENT_v1.1_N1_PREVIEWS.md` sections A and D): DEP-08-04-013 removed from the post-image and held as `HELD_EDGE_PROPOSALS.csv` H-019 with its ID reserved; v1 brief otherwise binding; v1 instance outputs rewritten in place at 00:59 (v1 run record `_run_records/TASK_RUN_2026-09-05_0040.md` retained) |
| Carrier | `DEL-08-04` Type 2 Subagent Governance Bridge (BACKEND_FEATURE_SLICE, PKG-08); applied decomposition row L371 |
| Basis | `origin/main` `d66395d101143df68d956984f7ab93f5027418ec` (HEAD verified equal; worktree clean apart from this run folder) |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches `ScopeOfWork.md` front matter pin); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` — all recomputed, all match |
| Pre-image `Dependencies.csv` | `1f7c06a2d49689c9dc3ea7fb778c6763ab96b3ea929426e5d9269c3198612400` (11 data rows) — match |
| Pre-image `_DEPENDENCIES.md` | `e4c5ec7bc2efcffb534a04abf34054b64345ba10c075fb379ef833926199360b` — match |
| Post-image `POSTIMAGE_Dependencies.csv` | `902678b137b5600f0cd2202519b7906122c29168d74ab48846ca99b2f41d84e5` (v1 preview: `ccbf5649c7800a26f98f3de24e22751cd272149f44d1db39b58feb80fda7afce`) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `8d66e9dd97d16e2746ca295f01dab051fb9ac981accced36ef76855e9cd074c0` (v1 preview: `6ff3291f24a66753872bee93ac288865c1e8fe12d2838d93fbb79c72e791871b`) |
| Row census pre | 11 total / 10 ACTIVE / 1 RETIRED / 3 ANCHOR / 8 EXECUTION |
| Row census post | 13 total / 12 ACTIVE / 1 RETIRED / 4 ANCHOR / 9 EXECUTION (ACTIVE: 4 ANCHOR, 8 EXECUTION; satisfaction 6 SATISFIED / 4 PENDING / 3 TBD); v1 preview was 14 / 13 / 1 / 4 / 10 before the held row was removed |
| Authorization | SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-025, DEP-026 (report-only preview; no carrier byte changed) |

## 2. Row-level diff

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-08-04-001 | REFRESHED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | WBS_NODE: SOW-063 Project delegation authority daemon-client dispatch and checkout AgentRuns | `_CONTEXT.md#Traceability` | ACTIVE; LastSeen 2026-09-05; Notes: re-validated against applied row L371 (SOW-063, SOW-083). |
| DEP-08-04-002 | REFRESHED | EXECUTION | UPSTREAM/PREREQUISITE | DOCUMENT: REF-001..REF-007 Accepted source corpus for DEL-08-04 | `ScopeOfWork.md#CLM-019 — Prerequisites` | ACTIVE; LastSeen 2026-09-05; Notes: REF-001..REF-007 MATCH under corpus v20. Statement text (v19 wording) preserved as dated. |
| DEP-08-04-003 | REFRESHED | EXECUTION | UPSTREAM/PREREQUISITE | UNKNOWN: TBD evaluateSubagentGovernance contract | `ScopeOfWork.md#CLM-030 — Open Items` | ACTIVE; LastSeen 2026-09-05. Pre-existing TargetLocation `frontend/src/lib/harness/subagent-governance.ts` preserved (App-owned code; not a Root path; seated write locus). |
| DEP-08-04-004 | REFRESHED | EXECUTION | UPSTREAM/PREREQUISITE | UNKNOWN: TBD Permission overlay and hook infrastructure | `ScopeOfWork.md#CLM-019 — Prerequisites` | ACTIVE; LastSeen 2026-09-05. TARGET_UNRESOLVED warning persists (no single stable target in the local source). |
| DEP-08-04-005 | UNCHANGED | EXECUTION | UPSTREAM/PREREQUISITE | DELIVERABLE: DEL-04-01 SDK Probe and Version-Pinned Adoption Decision | `ScopeOfWork.md#CLM-004 — Conditions` | RETIRED; Byte-identical; RETIRED 2026-08-24 (Gate 5) preserved. |
| DEP-08-04-006 | REFRESHED | EXECUTION | DOWNSTREAM/HANDOVER | DELIVERABLE: DEL-08-05 Subagent Child Run Records and Artifacts | `ScopeOfWork.md#CLM-020 — Steps` | ACTIVE; LastSeen 2026-09-05. E-019 handoff to DEL-08-05 still stated at CLM-020 step 11. |
| DEP-08-04-007 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT: OBJ-005 Project capability policy and conformance | `ScopeOfWork.md#Purpose and Objective Traceability` | ACTIVE; LastSeen 2026-09-05; EvidenceQuote refreshed to the live line carrying [SOW-063, SOW-083]; Notes appended. TargetType=REQUIREMENT convention of this carrier kept. |
| DEP-08-04-008 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT: OBJ-007 Agent-suite integrity and project delegation authority | `ScopeOfWork.md#Purpose and Objective Traceability` | ACTIVE; As DEP-08-04-007. |
| DEP-08-04-009 | REFRESHED | EXECUTION | UPSTREAM/INTERFACE | EXTERNAL: Chirality-managed delegation class | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#PKG-08 DEL-08-04 carrier row` | ACTIVE; LastSeen 2026-09-05; Notes: carrier row re-validated at L371. SourceRef (semantic carrier-row pointer) kept. |
| DEP-08-04-010 | REFRESHED | EXECUTION | UPSTREAM/INTERFACE | EXTERNAL: delegated-harness-native descent class | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#PKG-08 DEL-08-04 carrier row` | ACTIVE; As DEP-08-04-009. |
| DEP-08-04-011 | REFRESHED | EXECUTION | UPSTREAM/CONSTRAINT | EXTERNAL: ROOT-WP03-WP05-FIXTURES Root WP-03/WP-05 fixtures: accepted DEL-02-07 process-supervisor and DEL-02-10 API v2 returns | `ScopeOfWork.md#REQ-005` | ACTIVE; LastSeen 2026-09-05 only; A12 additive row otherwise preserved. |
| DEP-08-04-012 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT: SOW-083 Per-chat delegation policy carried with the session and honoured by the managed delegation bridge | `ScopeOfWork.md#Purpose and Objective Traceability` | ACTIVE; ADDED: SOW-083 trace anchor (applied row L371; ledger L253; reverse view L486; DEC-025 L634). SATISFIED as an anchor. |
| DEP-08-04-014 | ADDED | EXECUTION | UPSTREAM/INTERFACE | EXTERNAL: ROOT-DEL-02-11-DELEGATION-POLICY-FIELD Root DEL-02-11 daemon session-record delegation-policy field | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L253 SOW-083 Notes; #L602 OI-008` | ACTIVE; ADDED: Root DEL-02-11 session-record delegation-policy field, EXTERNAL / TBD / PENDING (OI-008 L602). No Root path. |

Change census: 1 UNCHANGED, 8 REFRESHED, 2 RE-EVIDENCED, 2 ADDED, 0 RETIRED; 1 HELD (DEP-08-04-013, reserved, not in the post-image; see the held-proposals section). No pre-image row deleted; every pre-image `DependencyID` present; the 13 rows are byte-identical to their v1 preview counterparts; no `Origin=DECLARED` row exists in this register; `Status=CANDIDATE` absent.

Not emitted (considered): SOW-006 / DEL-02-02 ownership boundary ("DEL-08-04 retains role/delegation semantics") — no named artifact transfer stated for this carrier; SOW-081 workflow-file delegation-policy declaration — DEL-07-03 owns the file contract, no bridge consumption stated; `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-04 selected` on DEL-08-04-V3-02 — selection ordering, not information flow; root `AGENTS.md` graph reference — unchanged since Gate 5, not re-derived; E-020 reverse handoff from DEL-08-05 — non-gating, as at Gate 5.

## Held proposals (amendment v1.1)

| HeldID | Reserved DependencyID | Edge | Direction/Type | Statement | Evidence it would have cited | Why held |
|---|---|---|---|---|---|---|
| H-019 | DEP-08-04-013 | DEL-08-04 -> DEL-03-02 (Thin TurnEngine and Session Locking, PKG-03) | UPSTREAM/INTERFACE, `TargetType=DELIVERABLE`, `SatisfactionStatus=PENDING`, `Confidence=HIGH` | The managed delegation bridge consumes the per-chat delegation policy that DEL-03-02 binds into the App session boot request (SOW-010, SOW-083); `none` is the default and the policy only narrows managed delegation. | `_STATUS.md#Remaining` (DEL-08-04-V3-02 Depends line, L28: "Depends: DEL-03-02-V3-01 (the binding; selected together)", owner-adopted under D-APP-108); applied row L371 ("Honour the per-chat delegation policy carried with the session"); SOW-083 L253; DEL-03-02 row L318; SOW-010 L413 | Passed F1/F2/F3 in isolation (v1 preview; no SCC-001 member has a row or path back to DEL-08-04), but `Evidence/fanin_simulation_v1/edge_analysis.json` shows it lies on a collective cycle with fourteen other newly proposed edges that together would merge SCC-001 into a 20-node SCC; choosing which to keep is a human-gated cut (`docs/CYCLE_DRIVEN_RESOLUTION.md`; `DOWNSTREAM_HANDOFFS.csv` row 3 "SCC unchanged unless separately ruled"). Recorded in `HELD_EDGE_PROPOSALS.csv` H-019 for the owner's separate transaction; ID reserved, never reused; not a register deletion (the row never reached the carrier). |

The held row's full field set (29 columns) is preserved in `HELD_EDGE_PROPOSALS.csv` H-019 and in the v1 run record; the reciprocal DEL-03-02 -> DEL-08-04 edge is not stated anywhere and was never proposed.

## 3. Fence results

- **F1 (SCC-001 membership):** NONE. After amendment v1.1 no row in the post-image targets an SCC-001 member; the held DEP-08-04-013 would have targeted DEL-03-02, an SCC-001 member (SCC-001 = DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05 per `Evidence/baseline_closure/scc_summary.csv`). Check performed: grep of every `Dependencies.csv` under `RUN_ROOT` for rows targeting DEL-08-04 finds only DEL-08-05 (DEP-08-05-004, DEP-08-05-011) and DEL-09-02 (DEP-09-02-024); a reachability walk over all ACTIVE EXECUTION DELIVERABLE edges with the analyzer's direction semantics finds no path from any SCC-001 member to DEL-08-04 with or without the held DEL-08-04 -> DEL-03-02 edge. DEL-08-04 therefore remains outside SCC-001 in this post-image and was outside it in the v1 post-image taken alone; the collective fan-in cycle is the sole reason for the hold; no SCC-internal edge and no SCC-internal retirement is proposed.
- **F2 (Root path):** NONE. The only Root-owned target (DEL-02-11 session-record field) is `EXTERNAL` with `TargetLocation=TBD`. Observation, not a hit: pre-existing DEP-08-04-003 retains `TargetLocation=frontend/src/lib/harness/subagent-governance.ts` from Gate 5 (App-owned code under this repository, the seated items' write locus; not a Root path and not under `projects/**`); preserved as prior state for the reviewer's attention.
- **F3 (permitted effect):** NONE. Both new rows (and the held proposal) derive from the amended SOW-083 row (L253/L486) and the applied-row prose ("Honour the per-chat delegation policy carried with the session (`none` by default) as a narrowing input to managed delegation"); no row derives from SCC ordering, schedule, or "keep aligned" statements. No revised SOW-001/002/004/006/007/008/010 row maps this carrier; SOW-010 (L413) is cited only as evidence that DEL-03-02 binds the policy.
- **NEEDS_HUMAN_GRAPH_DECISION:** none.
- **FENCE_F1_CANDIDATES:** none.
- **FENCE_F2_CANDIDATES:** none.

## 4. Validator outputs (verbatim)

`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-08-04/POSTIMAGE_Dependencies.csv`

```
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-08-04/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 13
```

`python3 tools/validation/validate_enum.py <ENUM> <value>` over every distinct value in the amended post-image (29 distinct values across DEPENDENCY_CLASS, ANCHOR_TYPE, DIRECTION, DEPENDENCY_TYPE, TARGET_TYPE, EXPLICITNESS, CONFIDENCE, ORIGIN, STATUS, SATISFACTION_STATUS): all `VALID`, 0 invalid. Values emitted or changed by this run: `ANCHOR`, `EXECUTION`; `TRACES_TO_REQUIREMENT`, `NOT_APPLICABLE`; `UPSTREAM`; `OTHER`, `INTERFACE`; `REQUIREMENT`, `EXTERNAL` (`DELIVERABLE` remains only on pre-existing rows now that the held row is absent); `EXPLICIT`; `HIGH`; `EXTRACTED`; `ACTIVE`; `SATISFIED`, `PENDING`, `TBD` — each `VALID: <value> is a valid <ENUM>`.

`zsh tools/validation/validate_id_format.sh <TYPE> <ID>` over every distinct PKG/DEL/DEP/SOW/OBJ identity in the amended post-image, in row order (known `PROJECT_ID_FORMAT_PROFILE` warning; no ID changed):

```
INVALID: DEP-08-04-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: PKG-08 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEL-08-04 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: SOW-063 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: DEP-08-04-002 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-08-04-003 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-08-04-004 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-08-04-005 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: PKG-04 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEL-04-01 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: DEP-08-04-006 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEL-08-05 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: DEP-08-04-007 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
VALID: OBJ-005 matches OBJ format
INVALID: DEP-08-04-008 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
VALID: OBJ-007 matches OBJ format
INVALID: DEP-08-04-009 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-08-04-010 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-08-04-011 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-08-04-012 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-083 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: DEP-08-04-014 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
```

Anchor and integrity checks (script over the amended post-image): exactly one ACTIVE `IMPLEMENTS_NODE` (DEP-08-04-001) — PASS; 13 unique `DependencyID`s (DEP-08-04-013 reserved and absent) — PASS; `FromDeliverableID=DEL-08-04` on every row — PASS; every ACTIVE row has non-empty `EvidenceFile` and `SourceRef` — PASS; `_DEPENDENCIES.md` register table lists the same 13 IDs in the same order and its counts (13/12/1/4/9; SATISFIED 6 / PENDING 4 / TBD 3; Run History ACTIVE=12) equal the CSV — PASS; the held row was removed by whole-line deletion so every remaining line is byte-identical to the v1 post-image (which itself round-tripped the pre-image byte-identically) — PASS; no CR bytes, no trailing whitespace, final newline in both post-images — PASS.

SourceRef resolution (live bytes): `ScopeOfWork.md#Purpose and Objective Traceability` (L12-L14), `#CLM-019 — Prerequisites` (L323), `#CLM-020 — Steps` (L337), `#CLM-030 — Open Items` (L473), `#REQ-005` (L304); `_CONTEXT.md#Traceability` (L51); `_STATUS.md#Remaining` (L9, item DEL-08-04-V3-02 L23-L30); decomposition carrier row L371, L253, L602.

## 5. Epistemic notes

- DEP-08-04-012 — FACT. SOW-083 appears on the applied row (L371 scope refs) and in the `ScopeOfWork.md` front matter; TargetType=REQUIREMENT follows the repository convention for SOW trace anchors (this carrier does not use the `UNKNOWN` objective convention named in the generic brief text; its objective anchors are REQUIREMENT and were left so).
- Held H-019 (reserved DEP-08-04-013) — FACT for the relation (owner-adopted Depends line, applied row, SOW-083, DEL-03-02 row, SOW-010); ASSUMPTION only in the lifecycle field `SatisfactionStatus=PENDING` it would have carried. Held for the fan-in reason above, not for any evidential doubt; the reciprocal edge is not stated anywhere and was never proposed.
- DEP-08-04-014 — FACT for the Root-owned field and the consumption gate (OI-008, DEC-025, SOW-083 Notes); `TargetRefID=ROOT-DEL-02-11-DELEGATION-POLICY-FIELD` is a local label in the pattern of DEP-08-04-011's `ROOT-WP03-WP05-FIXTURES`, not a Root identifier claim; `TargetLocation=TBD` by convention.
- DEP-08-04-007/008 — FACT; only the quoted evidence line changed to its live form. DEP-08-04-002 — the Statement's "v19" wording is dated FACT; the current v20 corpus status is recorded in Notes rather than rewriting the Statement.
- DEP-08-04-003 — FACT preserved; its `TargetLocation` predates F2 and names App-owned code, flagged above as an observation for the reviewer rather than altered.
- [NOTE] CONTEXT_TRACEABILITY_LAG — `_CONTEXT.md#Traceability` and `ScopeOfWork.md` CLM-002 still show `CoversScopeItems: SOW-063` only; the front matter and applied row control. No source document was edited (outside this instance's write set).

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched. Amendment v1.1 rerun executed by a fresh instance of the same kind at 2026-09-05 00:59.
