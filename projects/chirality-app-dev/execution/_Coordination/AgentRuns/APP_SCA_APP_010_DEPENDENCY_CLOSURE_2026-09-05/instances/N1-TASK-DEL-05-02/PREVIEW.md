# PREVIEW — N1-TASK-DEL-05-02 — TASK + dependency-extract (report-only; revised under amendment v1.1)

This revision supersedes the v1 preview of 2026-09-05T00:39. It applies brief amendment v1.1 (`../../AMENDMENT_v1.1_N1_PREVIEWS.md`) section A (hold `DEP-05-02-016`), section B (evidence-field refresh of SCC-internal rows 009, 010, 012), and section D (rerun contract). The v1 brief remains binding for everything the amendment does not narrow.

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-05-02` (RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, node N1); brief v1 + amendment v1.1 |
| Carrier | `DEL-05-02` HarnessEvent Schema and Append-Only JSONL (DATA_MODEL_CHANGE, PKG-05); folder `projects/chirality-app-dev/execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-02_HarnessEvent_Schema_and_Append_Only_JSONL`; SCC-001 member |
| Basis | `HEAD` = `d66395d101143df68d956984f7ab93f5027418ec` (exact match at rerun; branch `claude/sca-app-010-dependency-closure`; `git diff --stat` basis..HEAD over the carrier, decomposition, register, and pointer is empty) |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed at rerun; matches the brief and the `ScopeOfWork.md` pin `@dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (match); pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (match) |
| Pre-image `Dependencies.csv` | `27ede0704416b2c0ffafeefd77fcd31a27ba7dc7d110c36bb26a90f876bb6269` (match at rerun; 13 data rows) |
| Pre-image `_DEPENDENCIES.md` | `f89e5f40240fac304aca71c49cfca965b38417693c4013e5717866152ff5b9af` (match at rerun) |
| Post-image `POSTIMAGE_Dependencies.csv` | `7a6da98003c9fc93caf3c602c09e242abb6105e90a1e45cff25e67d4a18f5380` (v1 was `73509dc9…069955`) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `8823be430d59a5060bff63a17d1474ff48c09ddc77a2ee7006dec0c7a91539a0` (v1 was `e5243e7c…068224`) |
| Row census (pre) | total 13 / ACTIVE 12 / RETIRED 1 / ANCHOR 5 / EXECUTION 8 |
| Row census (post) | total 15 / ACTIVE 14 / RETIRED 1 / ANCHOR 6 / EXECUTION 9 (ACTIVE: 6 ANCHOR, 8 EXECUTION; SatisfactionStatus: NOT_APPLICABLE 7, TBD 6, PENDING 2) |
| Held (not in post-image) | `DEP-05-02-016` (ID reserved; H-016) — see Section 2a |
| Carrier bytes | unchanged (this instance wrote only under its own folder; `git status` shows the run folder as the only change) |

## 2. Row-level diff

`UNCHANGED` means byte-identical to the pre-image. `RE-EVIDENCED (SCC-internal, evidence fields only)` means only `EvidenceFile`, `SourceRef`, and `LastSeen` changed on a row whose both endpoints are SCC-001 members; every field the amendment freezes is byte-identical to the pre-image (scripted check in Section 4).

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-05-02-001 | RE-EVIDENCED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | WBS_NODE PKG-05 | `ScopeOfWork.md#CLM-002` | Was `Datasheet.md#identification` (retired kit). Identification table preserved as CLM-002; front matter `package_id: PKG-05`. Parent anchor validated at decomposition L283. |
| DEP-05-02-002 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-014 | `ScopeOfWork.md#purpose-and-objective-traceability` | Was `Datasheet.md#identification`. TargetName refreshed to applied Scope Ledger L417 label. |
| DEP-05-02-003 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-015 | `ScopeOfWork.md#purpose-and-objective-traceability` | Was `Datasheet.md#identification`. TargetName refreshed to L418 label. |
| DEP-05-02-004 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-039 | `ScopeOfWork.md#purpose-and-objective-traceability` | Was `Datasheet.md#identification`. TargetName refreshed to L442 label. |
| DEP-05-02-005 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT OBJ-003 | `ScopeOfWork.md#purpose-and-objective-traceability` | Was `Datasheet.md#identification`. TargetName refreshed to OBJ-003 L264; TargetLocation corrected `#8-deliverables` -> `#6-objectives`. `TargetType=REQUIREMENT` preserved (this carrier's existing objective convention; amendment C.7 keeps the brief's `UNKNOWN` convention for pre-existing `UNKNOWN` rows only). |
| DEP-05-02-006 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | DELIVERABLE DEL-05-01 | `ScopeOfWork.md#CLM-017` | Was `Procedure.md#steps`. Step 1 and RQ-014 preserved in CLM-017/CLM-010; `_STATUS.md` `DEL-05-02-V3-01` Depends cites this row. Target not in SCC-001. |
| DEP-05-02-007 | UNCHANGED | EXECUTION | UPSTREAM/INTERFACE | DELIVERABLE DEL-03-04 | `Guidance.md#considerations` | RETIRED (RUL-SCC-001-RESIDUAL-001); SCC-internal; byte-identical. Stale legacy pointer tolerated on a RETIRED row (amendment B applies to rows still evidenced; a RETIRED row is not re-evidenced). |
| DEP-05-02-008 | RE-EVIDENCED | EXECUTION | DOWNSTREAM/ENABLES | DELIVERABLE DEL-05-04 | `ScopeOfWork.md#CLM-009` | Was `Specification.md#scope`. TargetName refreshed to applied L339 (`Runtime Replay Dialogue and Agent Transcript Projection`; commas omitted). Applied row L337 extends replay consumption to `proposal.*` after Root acceptance. Target not in SCC-001. |
| DEP-05-02-009 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION | UPSTREAM/CONSTRAINT | DELIVERABLE DEL-05-03 | `ScopeOfWork.md#CLM-009` | Was `Specification.md#scope` (file retired). Live line 183: "Redaction implementation details owned by DEL-05-03, except this deliverable must not permit secrets in event payloads"; existing `EvidenceQuote` is a verbatim substring and is unchanged. `_STATUS.md` V3-01 Depends cites this row. `TargetLocation` is a section anchor (no line pointer). Frozen fields byte-identical. Cleared from NEEDS_HUMAN_GRAPH_DECISION. |
| DEP-05-02-010 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION | UPSTREAM/INTERFACE | DELIVERABLE DEL-05-05 | `ScopeOfWork.md#CLM-009` | Was `Specification.md#scope`. Live line 185: "Tool-result artifact budget/storage implementation owned by DEL-05-05, except this deliverable must reference artifacts for large payloads"; corroborated by CLM-017 step 4 (line 317). Existing `EvidenceQuote` verbatim and unchanged. Frozen fields byte-identical. Cleared from NEEDS_HUMAN_GRAPH_DECISION. |
| DEP-05-02-011 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | DOCUMENT DEL-03-03-UIEVENT_HARNESSEVENT_SEPARATION | `ScopeOfWork.md#CLM-017` | Was `Procedure.md#steps`. TargetLocation moved from the retired DEL-03-03 `Specification.md#Requirements` to DEL-03-03 `ScopeOfWork.md#CLM-009` (DEL-03-03-REQ-005). `TargetDeliverableID` stays empty (SCC-SAFE-MOVES-001 decompose move preserved); not SCC-internal under the brief's rule; topology unchanged. Unchanged from v1. |
| DEP-05-02-012 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION | UPSTREAM/INTERFACE | DELIVERABLE DEL-04-03 | `ScopeOfWork.md#CLM-017` | Was `Procedure.md#steps` (file retired). Live line 337 (CLM-017 step 8): "Ensure SDK messages are mapped through an adapter rather than treated as the browser or persisted event contract"; existing `EvidenceQuote` verbatim and unchanged. Frozen fields byte-identical. Cleared from NEEDS_HUMAN_GRAPH_DECISION. |
| DEP-05-02-013 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | EXTERNAL ROOT-HARNESSEVENT-V2 (`TargetLocation=TBD`) | decomposition `#L337` | Was `#L323` (row moved by the Gate-5 amendment). PENDING preserved. Unchanged from v1. |
| DEP-05-02-014 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-082 | `ScopeOfWork.md#purpose-and-objective-traceability` | New scope ref on the applied row L337 (DEC-025 L634; Scope Ledger L485; SSOW L252). Unchanged from v1. |
| DEP-05-02-015 | ADDED | EXECUTION | UPSTREAM/PREREQUISITE | EXTERNAL ROOT-DEL-02-10-PROPOSAL-EVENTS (`TargetLocation=TBD`; PENDING) | `ScopeOfWork.md#current-acceptance-obligations` | Root DEL-02-10 acceptance of the four additive `proposal.*` types routed back to App (OI-008 L602; K-EVENT-3; `_STATUS.md` V3-02 gate). Distinct from 013 (schema v2 gate). Unchanged from v1. |

Retirements: none (no scope ref left the applied row; every legacy-kit-evidenced relation is restated in `ScopeOfWork.md`). Deletions: none (the removal of `DEP-05-02-016` from the post-image is not a register deletion; the row was never written to the carrier). `Status=CANDIDATE`: not emitted. `Origin=DECLARED` rows: none exist in this register. `Notes` on rows 009, 010, 012: deliberately unchanged (amendment B names evidence fields only; the existing Notes text "explicit in specification" / "explicit in procedure" remains accurate because `ScopeOfWork.md` CLM-008 and CLM-014 carry the Specification and Procedure labels).

## 2a. Held proposals (amendment v1.1)

| HeldID | Reserved DependencyID | Edge | Direction/Type | Evidence it would have cited | Why held |
|---|---|---|---|---|---|
| H-016 | `DEP-05-02-016` | DEL-05-02 -> DEL-02-02 (Right-Panel Coordination Workflows and Proposal UX; PKG-02) | DOWNSTREAM/INTERFACE; Confidence MEDIUM; SatisfactionStatus TBD | `ScopeOfWork.md#current-responsibility` ("consume the additive proposal.* event types for replay and the proposal card once Root accepts them (SOW-082)"); applied row L337 ("for replay and the proposal card"); Scope Ledger L485 note (DEL-02-02 owns the card; L308); `_STATUS.md` Remaining `DEL-05-02-V3-02` write locus (`session-events.ts` and `event-factory.ts` consumers; replay fixtures). PROPOSAL: direction DOWNSTREAM from the applied row prose; the reciprocal `DEL-02-02-V3-04` "fixture path first" signal was not emitted. Consumption gated by `DEP-05-02-015`. | Fan-in simulation (`Evidence/fanin_simulation_v1/edge_analysis.json`, `held_by_carrier.json`) shows this edge lies on a cycle with the other fourteen held edges and would join SCC-001 into a 20-node SCC; choosing which to keep is a human-gated cut (`docs/CYCLE_DRIVEN_RESOLUTION.md`; SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 3). Recorded as `HELD_NON_EMITTED_PENDING_OWNER_RULING` in `../../HELD_EDGE_PROPOSALS.csv` H-016. The ID is not renumbered or reused. |

## 3. Fence results

- **F1 (SCC-001; live nine-node set DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05 per `Evidence/baseline_closure/scc_summary.csv`):** NONE. No new EXECUTION row has both endpoints inside SCC-001 (the two remaining new EXECUTION/ANCHOR rows target EXTERNAL and a REQUIREMENT). No SCC-internal row is retired. SCC-internal rows 009, 010, 012 differ from the pre-image only in `EvidenceFile`, `SourceRef`, and `LastSeen` (amendment v1.1 section B; scripted frozen-field check in Section 4 reports zero violations); row 007 is byte-identical. Note for the reviewer (carried from v1): row 011's `TargetLocation` re-point is a pointer-only change on a DOCUMENT row with empty `TargetDeliverableID`, not SCC-internal under the brief's rule; the pre-image pointer can be restored without affecting any other row.
- **F2 (Root path):** NONE. Root-owned targets (013, 015) are `EXTERNAL` with `TargetLocation=TBD`. All other `TargetLocation` values resolve under `projects/chirality-app-dev/**` (decomposition section anchors; DEL-03-03 `ScopeOfWork.md#CLM-009`).
- **F3 (permitted effect):** NONE. New rows 014 and 015 derive from the SOW-082 relations on the amended applied row L337, Scope Ledger L485, OI-008 L602, and the seated `DEL-05-02-V3-02` item. The third SOW-082 relation (proposal card, DEL-02-02) is held, not emitted. No edge was inferred from SCC ordering, schedule, or "keep aligned" statements.
- **NEEDS_HUMAN_GRAPH_DECISION:** none. The v1 entries for `DEP-05-02-009`, `DEP-05-02-010`, `DEP-05-02-012` are cleared: amendment v1.1 section B permits the evidence-field refresh, each relation is stated in live `ScopeOfWork.md` bytes (lines 183, 185, 337), and the Function 5 live-evidence check now passes for every ACTIVE row.
- **FENCE_F1_CANDIDATES:** none (no SCC-internal edge was proposed or retired).
- **FENCE_F2_CANDIDATES:** none (no candidate needed a Root path; the outbound App notice named by `_STATUS.md`, `execution/_Coordination/NOTICE_2026-09-04_APP_SCA-APP-010_SHELL_REDESIGN_ROOT_DEPENDENCIES.md`, was not found at the basis commit and is recorded as an ASSUMPTION in row 015's Notes rather than as a location).

## 4. Validator outputs (verbatim, rerun 2026-09-05T01:00)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py <POSTIMAGE_Dependencies.csv>`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-05-02/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 15
rc=0
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` over every distinct value present in the post-image; 25 distinct checks, all `rc=0`; `CONFIDENCE MEDIUM` no longer appears because its only carrier row, 016, is held):

```text
DEPENDENCY_CLASS ANCHOR: rc=0 VALID: ANCHOR is a valid DEPENDENCY_CLASS
ANCHOR_TYPE IMPLEMENTS_NODE: rc=0 VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
DIRECTION UPSTREAM: rc=0 VALID: UPSTREAM is a valid DIRECTION
DEPENDENCY_TYPE OTHER: rc=0 VALID: OTHER is a valid DEPENDENCY_TYPE
TARGET_TYPE WBS_NODE: rc=0 VALID: WBS_NODE is a valid TARGET_TYPE
EXPLICITNESS EXPLICIT: rc=0 VALID: EXPLICIT is a valid EXPLICITNESS
CONFIDENCE HIGH: rc=0 VALID: HIGH is a valid CONFIDENCE
ORIGIN EXTRACTED: rc=0 VALID: EXTRACTED is a valid ORIGIN
STATUS ACTIVE: rc=0 VALID: ACTIVE is a valid STATUS
SATISFACTION_STATUS NOT_APPLICABLE: rc=0 VALID: NOT_APPLICABLE is a valid SATISFACTION_STATUS
ANCHOR_TYPE TRACES_TO_REQUIREMENT: rc=0 VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
TARGET_TYPE REQUIREMENT: rc=0 VALID: REQUIREMENT is a valid TARGET_TYPE
DEPENDENCY_CLASS EXECUTION: rc=0 VALID: EXECUTION is a valid DEPENDENCY_CLASS
ANCHOR_TYPE NOT_APPLICABLE: rc=0 VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
DEPENDENCY_TYPE INTERFACE: rc=0 VALID: INTERFACE is a valid DEPENDENCY_TYPE
TARGET_TYPE DELIVERABLE: rc=0 VALID: DELIVERABLE is a valid TARGET_TYPE
SATISFACTION_STATUS TBD: rc=0 VALID: TBD is a valid SATISFACTION_STATUS
STATUS RETIRED: rc=0 VALID: RETIRED is a valid STATUS
DIRECTION DOWNSTREAM: rc=0 VALID: DOWNSTREAM is a valid DIRECTION
DEPENDENCY_TYPE ENABLES: rc=0 VALID: ENABLES is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE CONSTRAINT: rc=0 VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
TARGET_TYPE DOCUMENT: rc=0 VALID: DOCUMENT is a valid TARGET_TYPE
TARGET_TYPE EXTERNAL: rc=0 VALID: EXTERNAL is a valid TARGET_TYPE
SATISFACTION_STATUS PENDING: rc=0 VALID: PENDING is a valid SATISFACTION_STATUS
DEPENDENCY_TYPE PREREQUISITE: rc=0 VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
distinct enum checks: 25
```

ID format (`zsh tools/validation/validate_id_format.sh <TYPE> <ID>`; known `PROJECT_ID_FORMAT_PROFILE` warning — the generic three-digit profile rejects the accepted App two-digit IDs; no ID was changed):

```text
INVALID: DEL-05-02 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-05 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-05-02-014 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-05-02-015 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-082 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-003 matches OBJ format
```

Anchor and integrity checks (scripted over the post-image):

```text
total=15 ACTIVE=14 RETIRED=1 ANCHOR=6 EXECUTION=9
ACTIVE anchor/exec: 6 8
Satisfaction: {'NOT_APPLICABLE': 7, 'TBD': 6, 'PENDING': 2}
IMPLEMENTS_NODE ACTIVE: 1
unique IDs: True From all DEL-05-02: True CANDIDATE absent: True 016 absent: True
```

Evidence resolution (ACTIVE rows; `EvidenceFile#SourceRef` and `TargetLocation` resolved against live bytes at HEAD; `QUOTE_NOT_VERBATIM` is this rerun's stricter substring check and flags only v1 rows whose quotes drop commas or backticks to keep the register unquoted, as v1 disclosed; the three section-B rows pass the verbatim check):

```text
DEP-05-02-001 | ScopeOfWork.md -> OK CLM-002 — Identification | TargetLocation: OK 7. Packages
   QUOTE_NOT_VERBATIM: PackageID PKG-05
DEP-05-02-002 | ScopeOfWork.md -> OK Purpose and Objective Traceability | TargetLocation: OK 9. Scope Ledger
   QUOTE_NOT_VERBATIM: project_scope_refs: [SOW-014 SOW-015 SOW-039 SOW-082]
DEP-05-02-003 | ScopeOfWork.md -> OK Purpose and Objective Traceability | TargetLocation: OK 9. Scope Ledger
   QUOTE_NOT_VERBATIM: project_scope_refs: [SOW-014 SOW-015 SOW-039 SOW-082]
DEP-05-02-004 | ScopeOfWork.md -> OK Purpose and Objective Traceability | TargetLocation: OK 9. Scope Ledger
   QUOTE_NOT_VERBATIM: project_scope_refs: [SOW-014 SOW-015 SOW-039 SOW-082]
DEP-05-02-005 | ScopeOfWork.md -> OK Purpose and Objective Traceability | TargetLocation: OK 6. Objectives
DEP-05-02-006 | ScopeOfWork.md -> OK CLM-017 — Steps | TargetLocation: OK 8. Deliverables
   QUOTE_NOT_VERBATIM: Use .chirality/sessions/<sessionId>/events.jsonl under the c
DEP-05-02-008 | ScopeOfWork.md -> OK CLM-009 — Scope | TargetLocation: OK 8. Deliverables
DEP-05-02-009 | ScopeOfWork.md -> OK CLM-009 — Scope | TargetLocation: OK 8. Deliverables
DEP-05-02-010 | ScopeOfWork.md -> OK CLM-009 — Scope | TargetLocation: OK 8. Deliverables
DEP-05-02-011 | ScopeOfWork.md -> OK CLM-017 — Steps | TargetLocation: OK CLM-009 — Requirements
   QUOTE_NOT_VERBATIM: Keep browser SSE event names and compact UIEvent payloads se
DEP-05-02-012 | ScopeOfWork.md -> OK CLM-017 — Steps | TargetLocation: OK 8. Deliverables
DEP-05-02-013 | execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md -> OK | | DEL-05-02 | HarnessEvent Schema and Append-Only JSONL | TBD | DATA_M | TargetLocation: TBD
   QUOTE_NOT_VERBATIM: Consume Root-owned daemon HarnessEvent records for App audit
DEP-05-02-014 | ScopeOfWork.md -> OK Purpose and Objective Traceability | TargetLocation: OK 9. Scope Ledger
   QUOTE_NOT_VERBATIM: project_scope_refs: [SOW-014 SOW-015 SOW-039 SOW-082]
DEP-05-02-015 | ScopeOfWork.md -> OK Current acceptance obligations | TargetLocation: TBD
```

SCC-internal frozen-field diff (post-image row vs carrier pre-image row; frozen set per amendment B = `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `TargetDeliverableID`, `Status`, `Statement`, `SatisfactionStatus`, `Origin`, `FirstSeen`):

```text
DEP-05-02-007 changed: [] frozen-violations: []
DEP-05-02-009 changed: ['EvidenceFile', 'SourceRef', 'LastSeen'] frozen-violations: []
DEP-05-02-010 changed: ['EvidenceFile', 'SourceRef', 'LastSeen'] frozen-violations: []
DEP-05-02-012 changed: ['EvidenceFile', 'SourceRef', 'LastSeen'] frozen-violations: []
```

Other checks: no new EXECUTION row targets an SCC-001 member; the CSV contains no quoted fields (pre-image convention); `_DEPENDENCIES.md` post-image counts (14/1/6/9; 2/7/6) reconcile to the CSV; Run History row placed under `## Run History` with ACTIVE 14; both post-image files are LF-only with no trailing whitespace and a final newline; `git status --porcelain` lists only the untracked run folder.

## 5. Epistemic notes

- **FACT** — 001 to 005 and 014: identifiers appear verbatim in `ScopeOfWork.md` front matter, the Purpose section, and CLM-002, and exist at the cited decomposition lines.
- **FACT** — 006, 008, 011: the legacy Procedure/Specification text is preserved line-for-line in `ScopeOfWork.md` CLM-009 and CLM-017 (AC-001 states the migration preserved every line), so the relations are stated in live bytes.
- **FACT** — 009, 010, 012 (section B refresh): the relations are stated verbatim at `ScopeOfWork.md` lines 183, 185, and 337; each row's pre-existing `EvidenceQuote` is a verbatim substring of the cited live line, so only the file and section pointer moved. No endpoint, direction, type, status, or statement was touched; this is not an SCC change.
- **FACT** — 013, 015: the Root-owned gates are stated on the applied row L337, in `ScopeOfWork.md` "Current acceptance obligations" items 1 and 2, in OI-008 L602, and in the seated Remaining items; `TargetLocation=TBD` is the Gate-5/A12 convention, not an unresolved lookup.
- **ASSUMPTION** — 015: the outbound App notice named in `_STATUS.md` was not found under `execution/_Coordination/` at the basis commit; the row does not depend on its existence (the gate is the Root return).
- **PROPOSAL (held)** — H-016 / reserved `DEP-05-02-016`: see Section 2a; the evidence and the DOWNSTREAM reading are unchanged from v1 and are carried in `HELD_EDGE_PROPOSALS.csv` for the owner's separate transaction.
- **Considered, not emitted (F3, CONSERVATIVE):** DEL-06-03 (`propose` tool owner; events reach this carrier via the Root record), DEL-08-01 (instruction clauses), DEL-09-02/DEL-09-03 (ledger co-listing), the D-APP-68 `coordination.*` ownership boundary (CLM-028), and the `_STATUS.md` check/gate lines (registered frontend gates, APP-HOLD-1, review path), which are process constraints rather than information-flow edges.
- Labels: refreshed anchor and deliverable labels omit commas to keep the register unquoted, following the pre-image OBJ-003 row's convention; the underlying names are unchanged in meaning.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched. Rerun instance under amendment v1.1 (2026-09-05T01:00); the v1 instance's run record `_run_records/TASK_RUN_2026-09-05_0039.md` is retained unmodified.
