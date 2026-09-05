# PREVIEW — N1-TASK-DEL-02-05 — TASK + dependency-extract (report-only; amended v1.1)

Rerun under `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/AMENDMENT_v1.1_N1_PREVIEWS.md` (sections A, B, D) on 2026-09-05T01:03:00-0600; the v1 brief (`LAUNCH_BRIEF.md`) remains binding except as the amendment narrows it. The v1 preview (post-image hashes `34166944f5328e18b41e1d66c6d4f574ba0c27f52f70056232358c3ce956561a` / `2719efe64ff38ad2c98cc115ae44283f340b93eaffb31f6c799d8c5f4d632a01`, run record `_run_records/TASK_RUN_2026-09-05_0036.md`) is superseded by this file and the files it names.

## 1. Header

| Field | Value |
|---|---|
| RunID / Node / Instance | `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` / N1 / `N1-TASK-DEL-02-05` (amendment v1.1) |
| Carrier | `DEL-02-05` API Key UI and Runtime Feedback (UX_UI_SLICE, PKG-02); `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback` |
| Basis | `git rev-parse HEAD` = `d66395d101143df68d956984f7ab93f5027418ec` on `claude/sca-app-010-dependency-closure` (exact; PR #713 merge); re-verified at the rerun |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed at the rerun; matches the pinned content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`; pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` |
| Applied row | L311; scope refs SOW-013, SOW-019, SOW-023; objectives OBJ-001, OBJ-008; amended Scope Ledger rows for this carrier: none (SOW-081 to SOW-084 are not carried here) |
| Pre-image `Dependencies.csv` | SHA-256 `c39a3d533bf5f811f35d3a3b7fbfd839e7c1baedc28607cc4d59ad9eb200b8d0` (matched at the rerun; 10 data rows) |
| Pre-image `_DEPENDENCIES.md` | SHA-256 `e172982d34981ce52f04d8776c53d2a09712559ae648f660923b4457d0fc080e` (matched at the rerun) |
| Post-image `POSTIMAGE_Dependencies.csv` | SHA-256 `03d3d7bcf405e98e7096d24f6322b2a7bc0fd68a239e620f8d27191616c66f17` (v1.1) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | SHA-256 `5dfb3da66a0c128569e0fd9714a65a14df28c3d2ffa5cedf710cc3b40d21fcc9` (v1.1) |
| Row census PRE | total 10 / ACTIVE 10 / RETIRED 0 / ANCHOR 4 / EXECUTION 6 |
| Row census POST (v1.1) | total 13 / ACTIVE 13 / RETIRED 0 / ANCHOR 6 / EXECUTION 7 (v1 was 15 / 15 / 0 / 6 / 9; two rows held) |
| SatisfactionStatus POST (v1.1) | TBD 6 / PENDING 6 / SATISFIED 1 |
| Reserved IDs | DEP-02-05-014 (H-013), DEP-02-05-015 (H-014); not emitted, not renumbered |

Carrier-byte check: no byte under the carrier folder or anywhere outside this instance folder was written by the v1 preview or by this rerun (`git status` shows only the untracked run-packet tree).

## 2. Row-level diff

`UNCHANGED` means byte-identical to the carrier pre-image. Every emitted row keeps its `DependencyID`, `Origin=EXTRACTED`, and `Status=ACTIVE`; no row was deleted or retired. Rows other than DEP-02-05-004 and -006 are byte-identical to the v1 post-image.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-02-05-001 | REFRESHED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | PACKAGE PKG-02 | `_CONTEXT.md#Identity` | `TargetLocation` L286 to L280 (PKG-02 package row moved after SCA-APP-010); `LastSeen` 2026-09-05; Notes rewritten to cite L280/L311 |
| DEP-02-05-002 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-013 | `ScopeOfWork.md#Purpose-and-Objective-Traceability` | `TargetLocation` L401 to L416; `LastSeen`; Notes appended |
| DEP-02-05-003 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-019 | `ScopeOfWork.md#Purpose-and-Objective-Traceability` | `TargetLocation` L407 to L422; `LastSeen`; Notes appended |
| DEP-02-05-004 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION/NOT_APPLICABLE | UPSTREAM/PREREQUISITE | DELIVERABLE DEL-04-05 | `ScopeOfWork.md#CLM-016-Prerequisites` | **SCC-001 internal (F1; amendment v1.1 B).** Relation still stated (CLM-016 line 320; `EvidenceFile`, `SourceRef`, `EvidenceQuote` unchanged). `TargetLocation` line pointer L316 to L330 (DEL-04-05 applied row); `LastSeen` 2026-09-05; Notes provenance clause appended. Frozen fields (class, anchor type, direction, type, target type, target ID, status, statement, satisfaction, origin, FirstSeen) byte-identical to the pre-image |
| DEP-02-05-005 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DOCUMENT `@chirality/harness-contract` typed error taxonomy | `ScopeOfWork.md#CLM-010-Requirements` (DEL-02-05-R10) | Evidence moved from excluded `Evidence_ORN-08_Runtime_Error_Taxonomy_Ownership.md#Disposition`; new quote from R10; `LastSeen`; Notes appended. `TargetLocation=frontend/packages/harness-contract` preserved (see F2 observation) |
| DEP-02-05-006 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-03-03 | `ScopeOfWork.md#CLM-010-Requirements` (DEL-02-05-R07) | **SCC-001 internal (F1; amendment v1.1 B).** Relation still stated (R07 line 235; `EvidenceFile`, `SourceRef`, `EvidenceQuote` unchanged). `TargetLocation` line pointer L305 to L319 (DEL-03-03 applied row); `LastSeen` 2026-09-05; Notes provenance clause appended. Frozen fields byte-identical to the pre-image |
| DEP-02-05-007 | REFRESHED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-023 | `ScopeOfWork.md#Purpose-and-Objective-Traceability` | `TargetLocation` L411 to L426; `LastSeen`; Notes appended |
| DEP-02-05-008 | REFRESHED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | EXTERNAL Root-owned `HostedEngineConsentPort` (`TargetLocation=TBD`) | decomposition`#L311` | `SourceRef` L297 to L311 (quoted text unchanged on the applied row); `LastSeen`; Notes appended |
| DEP-02-05-009 | REFRESHED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | EXTERNAL accepted Root/App account/consent contract; G3; G-CSP; G4 (`TargetLocation=TBD`) | decomposition`#L311` | `SourceRef` L297 to L311; `LastSeen`; Notes appended |
| DEP-02-05-010 | REFRESHED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/ENABLES | DELIVERABLE DEL-09-06 | `ScopeOfWork.md#Purpose-and-Objective-Traceability` (D-APP-80 note) | `TargetLocation` L369 to L383; `LastSeen`; Notes appended (L311 restates the retained validation) |
| DEP-02-05-011 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-001 (decomposition L262) | `ScopeOfWork.md#Purpose-and-Objective-Traceability` | Objective trace anchor; `TargetType=UNKNOWN` per the brief's objective convention (kept by amendment C.7); `SatisfactionStatus=TBD` |
| DEP-02-05-012 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-008 (decomposition L269) | `ScopeOfWork.md#Purpose-and-Objective-Traceability` | Objective trace anchor; same convention |
| DEP-02-05-013 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | EXTERNAL Root DEL-02-09 root-private login home and shared-login amendment, OI-008 (`TargetLocation=TBD`) | decomposition`#L311` | Introduced by the SCA-APP-010 L311 Notes (SR-19) and OI-008 L602; corroborated by SOW acceptance obligation 4 and the seated V3-03/V3-05 Depends lines; `PENDING` |

## Held proposals (amendment v1.1)

Removed from the post-image under section A; recorded in `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` for the owner's separate transaction (`docs/CYCLE_DRIVEN_RESOLUTION.md`; cut and merge are human-gated). The IDs stay reserved; the remaining rows are not renumbered. Neither row was ever written to the carrier.

| HeldID | Reserved DependencyID | Edge | Evidence it would have cited | Note |
|---|---|---|---|---|
| H-013 | DEP-02-05-014 | DEL-02-05 UPSTREAM PREREQUISITE DEL-02-01 (Woven Dialogue Shell and Compatibility Navigation; account row host) | `_STATUS.md#Remaining`, seated DEL-02-05-V3-05 `Depends: DEL-02-01-V3-01 (account row host)` (`NOT_SELECTABLE_UNTIL: DEL-02-01-V3-01 landed`); applied row L311 (account row and popover on this carrier); applied DEL-02-01 row L307 (account row host among its outputs); revised SOW-001 L404 | FACT that the seated line and the two applied rows state it; `Confidence=HIGH`; would be `PENDING` until DEL-02-01-V3-01 lands. Fan-in simulation: joins SCC-001 into the simulated 20-node SCC together with the other held edges (any one alone changes nothing) |
| H-014 | DEP-02-05-015 | DEL-02-05 UPSTREAM PREREQUISITE DEL-02-03 (Working Root File Tree and Scope Scan UI; right-panel view switcher for the Settings view) | `_STATUS.md#Remaining`, seated DEL-02-05-V3-05 Depends line "the Settings view mounts in the right-panel view switcher from DEL-02-03-V3-01 and cannot land before it"; DEL-02-03 exists at decomposition L309 | FACT that the owner-adopted seating (D-APP-108) states it; `Confidence=MEDIUM`. CONFLICT carried with the proposal: the applied DEL-02-03 row (L309) does not name a right-panel view switcher and revised SOW-001 (L404) places the one-view-at-a-time right panel under DEL-02-01; the target question (DEL-02-03 versus DEL-02-01) is for the owner's ruling. Amendment C.1 notes the DEP-02-02-021 treatment (keep target, MEDIUM, ASSUMPTION note) would have applied had the row not been held |

## 3. Fence results

- **F1** (SCC-001 member; no new `EXECUTION` row with both endpoints inside SCC-001; no SCC-internal retirement): `NONE`. Existing SCC-internal rows DEP-02-05-004 (DEL-04-05) and DEP-02-05-006 (DEL-03-03) are still evidenced by live bytes. Under amendment v1.1 section B only their `TargetLocation` line pointers, `LastSeen`, and a Notes provenance clause changed; `EvidenceFile`, `SourceRef`, and `EvidenceQuote` were already live and are unchanged; every frozen field is byte-identical to the pre-image (asserted by a deterministic field-by-field comparison).
- **F2** (no Root path; `TargetLocation` only under `projects/chirality-app-dev/**`, `_REFERENCES.md`-pinned repo-root files, or `TBD` for Root-owned targets): `NONE` for every new or changed field (the refreshed pointers name `execution/_Decomposition/...#L330` and `#L319`). Observation for the reviewer (unchanged from v1): pre-existing DEP-02-05-005 `TargetLocation=frontend/packages/harness-contract` is an App-owned repository path (not a Root path) outside the F2 whitelist; it dates from 2026-05-20, is cited by `ScopeOfWork.md` R10 as a source, and is preserved unchanged rather than rewritten to `TBD`.
- **F3** (permitted effect DEP-007/DEP-008; no edges from SCC ordering, schedule, or coordination-only statements): `NONE` emitted outside the permitted effect. Not emitted (unchanged from v1): an UPSTREAM PREREQUISITE from DEL-02-05 to DEL-09-06 that the seated DEL-02-05-V3-03 Depends line (`DEL-09-06-V3-03`) would support; that relation predates SCA-APP-010 (A12 seating, 2026-09-03) and is outside this write set; existing DEP-02-05-010 continues to carry the retained-validation relation the applied row restates.
- **NEEDS_HUMAN_GRAPH_DECISION:** `none` (both SCC-internal rows remain evidenced; nothing held under F1).
- **FENCE_F1_CANDIDATES:** `none`. The seated DEL-02-05-V3-03 Depends line naming `DEL-04-05-V3-02` (evidence I would have cited: `_STATUS.md#Remaining`, line 14, "Depends: Root DEL-02-09 accepted account/consent contract (routed notice); DEL-02-05-V3-02; DEL-04-05-V3-02; DEL-09-06-V3-03") maps onto existing DEP-02-05-004 by match precedence rule 2 (same class, direction, target) and is not a new SCC-internal edge; it was not merged into that row's evidence.
- **FENCE_F2_CANDIDATES:** `none`. No candidate row required a Root path; every Root-owned target is `EXTERNAL`/`TBD`.

The v1 information note about stale line pointers on DEP-02-05-004 (`#L316`) and DEP-02-05-006 (`#L305`) is closed by this rerun: both now cite the live applied rows (L330, L319).

## 4. Validator outputs (verbatim, rerun on the v1.1 post-image)

Schema (`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-05/POSTIMAGE_Dependencies.csv`):

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-05/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 13
```

Enum summary (`python3 tools/validation/validate_enum.py <ENUM> <value>` for every distinct value in the v1.1 post-image; 25 invocations, all exit 0; `CONFIDENCE MEDIUM` no longer occurs because its only bearer, DEP-02-05-015, is held):

```text
DEPENDENCY_CLASS ANCHOR -> VALID: ANCHOR is a valid DEPENDENCY_CLASS (exit 0)
ANCHOR_TYPE IMPLEMENTS_NODE -> VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE (exit 0)
DIRECTION UPSTREAM -> VALID: UPSTREAM is a valid DIRECTION (exit 0)
DEPENDENCY_TYPE OTHER -> VALID: OTHER is a valid DEPENDENCY_TYPE (exit 0)
TARGET_TYPE PACKAGE -> VALID: PACKAGE is a valid TARGET_TYPE (exit 0)
EXPLICITNESS EXPLICIT -> VALID: EXPLICIT is a valid EXPLICITNESS (exit 0)
CONFIDENCE HIGH -> VALID: HIGH is a valid CONFIDENCE (exit 0)
ORIGIN EXTRACTED -> VALID: EXTRACTED is a valid ORIGIN (exit 0)
STATUS ACTIVE -> VALID: ACTIVE is a valid STATUS (exit 0)
SATISFACTION_STATUS TBD -> VALID: TBD is a valid SATISFACTION_STATUS (exit 0)
ANCHOR_TYPE TRACES_TO_REQUIREMENT -> VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE (exit 0)
TARGET_TYPE REQUIREMENT -> VALID: REQUIREMENT is a valid TARGET_TYPE (exit 0)
DEPENDENCY_CLASS EXECUTION -> VALID: EXECUTION is a valid DEPENDENCY_CLASS (exit 0)
ANCHOR_TYPE NOT_APPLICABLE -> VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE (exit 0)
DEPENDENCY_TYPE PREREQUISITE -> VALID: PREREQUISITE is a valid DEPENDENCY_TYPE (exit 0)
TARGET_TYPE DELIVERABLE -> VALID: DELIVERABLE is a valid TARGET_TYPE (exit 0)
SATISFACTION_STATUS PENDING -> VALID: PENDING is a valid SATISFACTION_STATUS (exit 0)
DEPENDENCY_TYPE INTERFACE -> VALID: INTERFACE is a valid DEPENDENCY_TYPE (exit 0)
TARGET_TYPE DOCUMENT -> VALID: DOCUMENT is a valid TARGET_TYPE (exit 0)
SATISFACTION_STATUS SATISFIED -> VALID: SATISFIED is a valid SATISFACTION_STATUS (exit 0)
TARGET_TYPE EXTERNAL -> VALID: EXTERNAL is a valid TARGET_TYPE (exit 0)
DEPENDENCY_TYPE CONSTRAINT -> VALID: CONSTRAINT is a valid DEPENDENCY_TYPE (exit 0)
DIRECTION DOWNSTREAM -> VALID: DOWNSTREAM is a valid DIRECTION (exit 0)
DEPENDENCY_TYPE ENABLES -> VALID: ENABLES is a valid DEPENDENCY_TYPE (exit 0)
TARGET_TYPE UNKNOWN -> VALID: UNKNOWN is a valid TARGET_TYPE (exit 0)
```

ID-format warning (`zsh tools/validation/validate_id_format.sh <TYPE> <value>`; the generic three-digit profile rejects the accepted App two-digit identifiers; recorded as the known `PROJECT_ID_FORMAT_PROFILE` warning; no identifier changed):

```text
INVALID: DEL-02-05 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-02 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-02-05-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-02-05-013 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-013 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-023 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-001 matches OBJ format
VALID: OBJ-008 matches OBJ format
```

Anchor check and other Function 5 checks (deterministic script over the v1.1 post-image, private scratch subfolder; recorded here):

```text
implements_node_active 1            (exactly one ACTIVE IMPLEMENTS_NODE: DEP-02-05-001; no FLOATING_NODE, no AMBIGUOUS_ANCHOR)
unique DependencyID                 PASS (13 of 13)
held IDs absent                     PASS (DEP-02-05-014, -015 not present)
FromDeliverableID=DEL-02-05         PASS (13 of 13)
Status in {ACTIVE, RETIRED}         PASS; CANDIDATE absent
EXTERNAL rows TargetLocation=TBD    PASS (DEP-02-05-008, -009, -013)
all pre-image IDs preserved         PASS (10 of 10)
amendment B frozen fields           PASS (DEP-02-05-004, -006: frozen fields byte-identical to the pre-image; only TargetLocation, LastSeen, Notes differ)
other rows vs v1 post-image         PASS (11 of 11 byte-identical; header identical to the pre-image)
evidence resolves to live bytes     PASS for every row (EvidenceFile exists; SourceRef heading or line exists; quote text present, allowing the pre-existing paraphrase on DEP-02-05-001 and the line-wrap on DEP-02-05-010)
TargetLocation line pointers        PASS (each #L<n> line names the target ID: L280 PKG-02, L416 SOW-013, L422 SOW-019, L330 DEL-04-05, L319 DEL-03-03, L426 SOW-023, L383 DEL-09-06, L262 OBJ-001, L269 OBJ-008)
_DEPENDENCIES.md reconciliation     PASS (13 register rows, one per DependencyID, fields matching; counts 13/0/6/7; SatisfactionStatus 6/6/1; Run History row under ## Run History; two HELD bullets)
LF, no trailing whitespace, EOF newline   PASS for both post-image files
```

## 5. Epistemic notes

- DEP-02-05-004 and -006 (RE-EVIDENCED, SCC-internal, evidence fields only) — FACT: the relations are still stated by live bytes (`ScopeOfWork.md` CLM-016 line 320; CLM-010 DEL-02-05-R07 line 235) and the applied rows for DEL-04-05 and DEL-03-03 now sit at L330 and L319. ASSUMPTION: amendment B lists `Notes` in neither the refreshable nor the frozen set; a dated provenance clause was appended to `Notes` (the register's existing convention for pointer refreshes, see rows 001 to 003 and 007 to 010) so the pointer change is auditable in the row itself. The reviewer may strip the clause if `Notes` is to be read as frozen; no graph field is touched either way.
- DEP-02-05-005 (RE-EVIDENCED) — FACT: `ScopeOfWork.md` DEL-02-05-R10 restates the consume-not-redefine relation verbatim; the original disposition file is excluded as a source by the brief, not contradicted. PROPOSAL (not applied): the reviewer may rewrite `TargetLocation` to `TBD` if the F2 whitelist is to be read as applying to pre-existing rows.
- DEP-02-05-011/-012 (ADDED) — FACT: both objectives are explicit in the SOW front matter and on L311. `TargetType=UNKNOWN` is kept per the brief and amendment C.7 (matches the pre-existing rows in these carriers); the v1 harmonization proposal against the DEL-08-04 precedent is withdrawn.
- DEP-02-05-013 (ADDED) — FACT: L311 Notes and OI-008 name Root DEL-02-09; the edge is a constraint on the app-wide account presentation, distinct from the port (008) and the contract-and-gates row (009). No Root path exists in App scope; `TBD` is deliberate.
- Held H-013 / H-014 — FACT that the seated V3-05 line and the applied rows state the relations (see the held-proposals table); their emission is a graph question the fan-in simulation made a cut, so it belongs to the owner's transaction, not to this pass.
- Not emitted (F3): DEL-02-05 to DEL-09-06 UPSTREAM PREREQUISITE from the V3-03 Depends line. FACT that the seated line states it; outside the DEP-007/DEP-008 permitted effect.
- Not emitted (F1, absorbed): DEL-04-05-V3-02 from the V3-03 Depends line, already represented by DEP-02-05-004.

## 6. Process notes

- v1 (retained for the record): the session scratchpad was shared by the concurrent N1 instances; one Bash call executed sibling N1-TASK-DEL-03-02's same-named generator, which wrote only `instances/N1-TASK-DEL-03-02/POSTIMAGE_Dependencies.csv` (observed SHA-256 `972b9e818892488325ca86410a91111e4e54322c52b0d69136a9832f80567415`); no carrier, decomposition, or Root byte was touched. See `_run_records/TASK_RUN_2026-09-05_0036.md`.
- v1.1 rerun: all helper scripts lived in an instance-private scratch subfolder (`.../scratchpad/n1-del-02-05-v11/`); the CSV was revised by textual edit of the v1 post-image (two line deletions, two pointer substitutions, two Notes appends) so the pre-image quoting convention is preserved byte-for-byte; no sibling script was executed. The `git status` after the rerun still shows only the untracked run-packet tree.

## 7. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview, amendment v1.1 rerun), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
