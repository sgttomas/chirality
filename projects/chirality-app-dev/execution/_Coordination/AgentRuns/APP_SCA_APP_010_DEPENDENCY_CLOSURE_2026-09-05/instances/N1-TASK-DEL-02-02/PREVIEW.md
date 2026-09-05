# PREVIEW — N1-TASK-DEL-02-02 — TASK + dependency-extract (report-only; amendment v1.1 rerun)

## 1. Header

| Field | Value |
|---|---|
| Instance | `N1-TASK-DEL-02-02` (RunID `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05`, Node N1) |
| Amendment | v1.1 (`AMENDMENT_v1.1_N1_PREVIEWS.md`, section A holds for this carrier, section C item 1, section D rerun contract); brief v1 otherwise binding. This rerun supersedes the v1 preview outputs in place; the v1 run record `_run_records/TASK_RUN_2026-09-05_0038.md` stays. |
| Carrier | `DEL-02-02` Right-Panel Coordination, Workflows, and Proposal UX (UX_UI_SLICE, PKG-02); folder `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX` |
| Basis | HEAD `d66395d101143df68d956984f7ab93f5027418ec` = `origin/main` (PR #713 merge); branch `claude/sca-app-010-dependency-closure`; working tree clean apart from this run folder |
| Decomposition identity | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (recomputed; matches) at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`; companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (matches); pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (matches) |
| Pre-image `Dependencies.csv` | `ccc6f4018a0c61eb3ff59105080bf3f6cd807c2a326a67d2a5f4d5998cafeb92` (recomputed; matches brief; 9 data rows) |
| Pre-image `_DEPENDENCIES.md` | `77360b1b8f8ba69f594ba7ab10c013d21a01836d0d78fa0ae105e3867931a925` (recomputed; matches brief) |
| v1 post-image `POSTIMAGE_Dependencies.csv` (superseded) | `00f6a880ab6f965ef684ede0668e4cf897e1743dc0cab00315db94c38400823d` (22 data rows) |
| v1 post-image `POSTIMAGE__DEPENDENCIES.md` (superseded) | `a2826a395df96b1136a1876f00daed7abc0938cb546a89233ee4bfd01903d61d` |
| Post-image `POSTIMAGE_Dependencies.csv` (v1.1) | `d4f6dad83cc9538186214b6ab9a116c85c6ae2a8578acfb5a65acd56e61c3cff` |
| Post-image `POSTIMAGE__DEPENDENCIES.md` (v1.1) | `adeb89260b62b2a86268b99505f08a6df2ea2eb98a22185961767fbad09b1df0` |
| Row census pre | 9 total / 9 ACTIVE / 0 RETIRED / 4 ANCHOR / 5 EXECUTION |
| Row census post (v1.1) | 16 total / 15 ACTIVE / 1 RETIRED / 7 ANCHOR / 9 EXECUTION (ACTIVE: 6 ANCHOR, 9 EXECUTION; SatisfactionStatus: 12 TBD, 4 PENDING). Reserved, absent by design: DEP-02-02-015, 017, 018, 019, 020, 022 |
| Held rows removed | 6 (H-002 to H-007); see section 3a |
| Writes | Only `POSTIMAGE_Dependencies.csv`, `POSTIMAGE__DEPENDENCIES.md`, `PREVIEW.md`, `RETURN.md`, `STATUS.json` rewritten in place, plus the new `_run_records/TASK_RUN_2026-09-05_0105.md`, all under this instance folder; no byte changed under the carrier or anywhere else (`git status --porcelain` shows only the untracked run folder) |

## 2. Row-level diff

`UNCHANGED` means byte-identical to the carrier pre-image. No row is byte-identical: `FromDeliverableName` was refreshed on every row to the applied row L308 display name and `LastSeen` was set to `2026-09-05` on every ACTIVE row. `RE-EVIDENCED` means `EvidenceFile`/`SourceRef` changed; `REFRESHED` means other fields changed with evidence unchanged. Decomposition line pointers below are `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L<n>`. Changes relative to the v1 preview are marked `v1.1:` in the Note column.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-02-02-001 | RE-EVIDENCED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | PKG-02 (PACKAGE) #L280 | `ScopeOfWork.md#CLM-002` | Was `Datasheet.md#L7-L10` (legacy kit). TargetName refreshed to the L280 label; TargetLocation L256 to L280. |
| DEP-02-02-002 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | SOW-006 (REQUIREMENT) #L176 | `ScopeOfWork.md#Purpose and Objective Traceability` | Was `_CONTEXT.md#Traceability` (still live, corroborates). TargetName refreshed to the L409 label; TargetLocation L382 to L176; Statement rewritten for the amended SOW-006. |
| DEP-02-02-003 | RETIRED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | SOW-007 (REQUIREMENT) #L177 | `_CONTEXT.md#Traceability` (unchanged) | SOW-007 not on applied row L308; DEC-025 L634 retired its presentation half. LastSeen kept at 2026-05-20; TargetLocation L383 to L177; Notes cite L308 and DEC-025. |
| DEP-02-02-004 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | OBJ-001 (UNKNOWN) #L262 | `ScopeOfWork.md#Purpose and Objective Traceability` | Was `_CONTEXT.md#Traceability`. TargetLocation L238 to L262; `TargetType=UNKNOWN` convention kept with the existing note. |
| DEP-02-02-005 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | DEL-02-01 (DELIVERABLE) #L307 | `ScopeOfWork.md#DEL-02-02-REQ-002` | Was `Specification.md#L25-L27`. TargetName refreshed to L307; Confidence HIGH to MEDIUM (retained routes only; DEL-08-02 retains routing). |
| DEP-02-02-006 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | DEL-02-03 (DELIVERABLE) #L309 | `ScopeOfWork.md#CLM-025` | Was `Guidance.md#L19-L22`. Quote kept (with the live backticks); retained Pipeline code only. |
| DEP-02-02-007 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | DEL-07-04 (DELIVERABLE) #L360 | `ScopeOfWork.md#DEL-02-02-REQ-003` | Was `Specification.md#L27-L43`. Retained Workbench code only; Confidence stays MEDIUM. |
| DEP-02-02-008 | RE-EVIDENCED | EXECUTION | UPSTREAM/INTERFACE | DEL-07-05 (DELIVERABLE) #L361 | `ScopeOfWork.md#DEL-02-02-REQ-003` | Was `Specification.md#L27-L43`. TargetName refreshed to L361 label. |
| DEP-02-02-009 | RE-EVIDENCED | EXECUTION | UPSTREAM/CONSTRAINT | DEL-08-03 (DELIVERABLE) #L370 | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` | Was `Guidance.md#L19-L31`. Statement now records no active-shell consumer; prior SOW-007 ownership CONFLICT marked RULED (D-APP-56 R4-P35; DEC-025). |
| DEP-02-02-010 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | SOW-081 (REQUIREMENT) #L251 | `ScopeOfWork.md#Purpose and Objective Traceability` | New scope ref on applied row L308 (SCA-APP-010). |
| DEP-02-02-011 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | SOW-082 (REQUIREMENT) #L252 | `ScopeOfWork.md#Purpose and Objective Traceability` | New scope ref on applied row L308 (SCA-APP-010). v1.1: `Notes` cross-reference to DEP-02-02-015 replaced by held proposal H-002 (015 reserved); no other field changed. |
| DEP-02-02-012 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | OBJ-007 (UNKNOWN) #L268 | `ScopeOfWork.md#Purpose and Objective Traceability` | Objective present on the row but previously without a trace anchor; `UNKNOWN` convention kept. |
| DEP-02-02-013 | ADDED | EXECUTION | UPSTREAM/INTERFACE | DEL-07-03 (DELIVERABLE) #L359 | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` | Workflow file contract read/written by the Workflows view; PENDING on DEL-07-03-V3-01. |
| DEP-02-02-014 | ADDED | EXECUTION | UPSTREAM/INTERFACE | DEL-06-03 (DELIVERABLE) #L348 | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)` | `propose` tool emits the `proposal.offered` payload the card renders; Confidence MEDIUM; PENDING. v1.1: `Notes` cross-reference to DEP-02-02-015 replaced by held proposal H-002 (015 reserved); no other field changed. |
| DEP-02-02-016 | ADDED | EXECUTION | UPSTREAM/CONSTRAINT | ROOT-PROPOSAL-EVENT-ACCEPTANCE (EXTERNAL) `TBD` | `_STATUS.md#Remaining` | Root DEL-02-10 acceptance of the additive `proposal.*` event types; Gate-5/A12 convention (no Root path); PENDING. |
| DEP-02-02-021 | ADDED | EXECUTION | UPSTREAM/PREREQUISITE | DEL-02-03 (DELIVERABLE) #L309 | `_STATUS.md#Remaining` | Right-panel view-switcher host of the Workflows view from the seated V3-04 Depends line; PENDING. v1.1 (C.1): target kept DEL-02-03, `Confidence=MEDIUM` (unchanged), `Notes` rewritten as an ASSUMPTION citing the owner-adopted `_STATUS.md` Depends line (DEL-02-03-V3-01, D-APP-108) as evidence and the L307/L309 silence as the reason for MEDIUM; the NEEDS_HUMAN_GRAPH_DECISION flag is withdrawn from the row. No other field changed. |

Every `DependencyID` and every pre-image row is preserved; no pre-image row was deleted; `Status=CANDIDATE` is not emitted; `Origin=DECLARED` rows: none existed. The six removed IDs were v1 proposals never written to the carrier and stay reserved (not renumbered). Quoting follows the pre-image minimal convention (quote only fields containing a comma or a quote); the pre-image's quoted `"Objective OBJ-001"` is preserved and `"Objective OBJ-007"` mirrors it. The line diff of the v1.1 CSV against the v1 CSV is exactly: rows 011, 014, and 021 changed (`Notes` only) and rows 015, 017, 018, 019, 020, and 022 removed.

## 3. Fence results

- **F1:** `NONE`. DEL-02-02 is not an SCC-001 member (SCC-001 = DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05 per `Evidence/baseline_closure/scc_summary.csv`). After amendment v1.1 no row in this register targets an SCC-001 member: the v1 row DEP-02-02-015 (DEL-05-02, UPSTREAM) is held as H-002. The v1 scan of every `PKG-*/1_Working/*/Dependencies.csv` for rows targeting DEL-02-02 found exactly one, DEL-02-01 `DEP-02-01-007` (DOWNSTREAM supply, ACTIVE; not an SCC-001 member), and no carrier register changed since (basis unchanged), so no SCC-001 member holds an ACTIVE row back to this carrier. No SCC-internal row exists in this register (amendment section B does not apply).
- **F2:** `NONE`. Every `TargetLocation` is `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L<n>` (under `projects/chirality-app-dev/**`) or `TBD`; the single Root-owned target (DEP-02-02-016, Root DEL-02-10) is `TargetType=EXTERNAL`, `TargetLocation=TBD`, `SatisfactionStatus=PENDING`. No repo-root file is named as a target.
- **F3:** `NONE`. Emitted new rows trace to applied row L308 prose (013, 014), amended rows SOW-081 L251, SOW-082 L252 and the front matter (010, 011, 012), OI-008 L602 with the seated V3-04 Depends line (016), or the seated V3-04 Depends line with the applied row's "in the right panel" prose (021). No edge was inferred from SCC ordering, schedule, or a keep-aligned statement. Not emitted for lack of a named transfer: DEL-04-04, DEL-08-01, Root DEL-02-11, Root DEL-02-09, and a DEL-02-01 right-panel-frame edge.
- **NEEDS_HUMAN_GRAPH_DECISION:** `none`. The v1 flag on DEP-02-02-021 is disposed by amendment v1.1 C.1 (HELP_HUMAN disposition-class, not an owner ruling): target DEL-02-03 kept, `Confidence=MEDIUM`, ASSUMPTION note recorded on the row. The underlying question (DEL-02-03 as seated versus DEL-02-01 per L307/L404) remains visible in the row `Notes` and the handoff notes for any later owner act; it is no longer an open graph decision for the N3 write.
- **FENCE_F1_CANDIDATES:** `none`.
- **FENCE_F2_CANDIDATES:** `none`.

### 3a. Held proposals (amendment v1.1)

Recorded as non-emitted proposals in `AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv` for the owner's separate transaction; removed from the post-image; IDs reserved. Each would have been `EXECUTION`, `UPSTREAM`, `Origin=EXTRACTED`, `Explicitness=EXPLICIT`, `FirstSeen=LastSeen=2026-09-05`, `Status=ACTIVE`.

| HeldID | Reserved ID | Edge (from → to) | Type | Evidence it would have cited | Would form or join |
|---|---|---|---|---|---|
| H-002 | DEP-02-02-015 | DEL-02-02 → DEL-05-02 (HarnessEvent Schema and Append-Only JSONL) #L337 | INTERFACE, HIGH, PENDING | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`, quote "live `proposal.*` consumption waits on DEL-05-02 after Root DEL-02-10 acceptance"; SCA-APP-010 acceptance obligation 4; SOW-082 L484; seated V3-04 Depends (DEL-05-02-V3-02) | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| H-003 | DEP-02-02-017 | DEL-02-02 → DEL-08-05 (Subagent Child Run Records and Artifacts) #L372 | INTERFACE, HIGH, PENDING | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`, quote "DEL-08-05 retains child records"; SOW-006 L176/L409; seated V3-01 gate and Depends (DEL-08-05-V3-01) | joins SCC-001 into the simulated 20-node SCC |
| H-004 | DEP-02-02-018 | DEL-02-02 → DEL-05-04 (Runtime Replay, Dialogue, and Agent Transcript Projection) #L339 | INTERFACE, HIGH, TBD | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`, quote "DEL-05-04 retains replay/projection semantics"; SOW-006 L176/L409; SCA-APP-004 dated history | joins SCC-001 into the simulated 20-node SCC |
| H-005 | DEP-02-02-019 | DEL-02-02 → DEL-08-04 (Type 2 Subagent Governance Bridge) #L371 | CONSTRAINT, MEDIUM, PENDING | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`, quote "DEL-08-04 retains role/delegation semantics"; SOW-006 L176; seated V3-02 Depends (DEL-08-04-V3-01); V3-01 seating CONFLICT recorded | joins SCC-001 into the simulated 20-node SCC |
| H-006 | DEP-02-02-020 | DEL-02-02 → DEL-08-02 (Persona Alias, Agent/Session Routing, and Legacy Matrix Compatibility Contract) #L369 | CONSTRAINT, MEDIUM, TBD | `ScopeOfWork.md#SCA-APP-010 Gate-5 Current Contract (Controlling)`, quote "DEL-08-02 retains routing"; SOW-005 L408; SOW-006 L409 | joins SCC-001 into the simulated 20-node SCC |
| H-007 | DEP-02-02-022 | DEL-02-02 → DEL-02-04 (Dialogue Toolkit, Context, and Local UI State) #L310 | INTERFACE, MEDIUM, PENDING | `_STATUS.md#Remaining`, quote "DEL-02-04-V3-01 (chat rung and declined-trigger convenience fields)"; revised SOW-008 L411; DEL-02-04 row L310; seated V3-04 Depends and Write locus | joins SCC-001 into the simulated 20-node SCC |

## 4. Validator outputs (verbatim)

`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/POSTIMAGE_Dependencies.csv`

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-02/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 16
```

`python3 tools/validation/validate_enum.py <ENUM> <value>` over every distinct value emitted in the ten enum columns (23 checks; the same 23 values as v1, since the held rows introduced no distinct value):

```text
ANCHOR_TYPE IMPLEMENTS_NODE: VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
ANCHOR_TYPE NOT_APPLICABLE: VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
ANCHOR_TYPE TRACES_TO_REQUIREMENT: VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
CONFIDENCE HIGH: VALID: HIGH is a valid CONFIDENCE
CONFIDENCE MEDIUM: VALID: MEDIUM is a valid CONFIDENCE
DEPENDENCY_CLASS ANCHOR: VALID: ANCHOR is a valid DEPENDENCY_CLASS
DEPENDENCY_CLASS EXECUTION: VALID: EXECUTION is a valid DEPENDENCY_CLASS
DEPENDENCY_TYPE CONSTRAINT: VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE INTERFACE: VALID: INTERFACE is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE OTHER: VALID: OTHER is a valid DEPENDENCY_TYPE
DEPENDENCY_TYPE PREREQUISITE: VALID: PREREQUISITE is a valid DEPENDENCY_TYPE
DIRECTION UPSTREAM: VALID: UPSTREAM is a valid DIRECTION
EXPLICITNESS EXPLICIT: VALID: EXPLICIT is a valid EXPLICITNESS
ORIGIN EXTRACTED: VALID: EXTRACTED is a valid ORIGIN
SATISFACTION_STATUS PENDING: VALID: PENDING is a valid SATISFACTION_STATUS
SATISFACTION_STATUS TBD: VALID: TBD is a valid SATISFACTION_STATUS
STATUS ACTIVE: VALID: ACTIVE is a valid STATUS
STATUS RETIRED: VALID: RETIRED is a valid STATUS
TARGET_TYPE DELIVERABLE: VALID: DELIVERABLE is a valid TARGET_TYPE
TARGET_TYPE EXTERNAL: VALID: EXTERNAL is a valid TARGET_TYPE
TARGET_TYPE PACKAGE: VALID: PACKAGE is a valid TARGET_TYPE
TARGET_TYPE REQUIREMENT: VALID: REQUIREMENT is a valid TARGET_TYPE
TARGET_TYPE UNKNOWN: VALID: UNKNOWN is a valid TARGET_TYPE
enum checks: 23 values, 0 invalid
```

`zsh tools/validation/validate_id_format.sh <TYPE> <value>` (known `PROJECT_ID_FORMAT_PROFILE` warning; no ID changed):

```text
INVALID: DEL-02-02 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
INVALID: PKG-02 does not match PKG format (^PKG-[0-9]{3}$)
INVALID: DEP-02-02-001 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: DEP-02-02-021 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
INVALID: SOW-006 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-081 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
INVALID: SOW-082 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
VALID: OBJ-001 matches OBJ format
VALID: OBJ-007 matches OBJ format
INVALID: DEL-02-03 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
```

Anchor, evidence, and reconciliation checks (Python over the v1.1 post-image; script in the run record):

```text
total 16 ACTIVE 15 RETIRED 1 ANCHOR 7 EXECUTION 9
ACTIVE anchor/exec 6 9
IMPLEMENTS_NODE active 1
sat Counter({'TBD': 12, 'PENDING': 4})
unique ids True
ids 001,002,003,004,005,006,007,008,009,010,011,012,013,014,016,021
from ok True
quotes>30w []
evidence check done
```

Evidence check: for every ACTIVE row the `SourceRef` heading or ID and the `EvidenceQuote` are substrings of the live `ScopeOfWork.md` or `_STATUS.md`; for every non-`TBD` `TargetLocation` the cited decomposition line begins with `| <TargetRefID> `. `_DEPENDENCIES.md` counts (16/15/1; 7 ANCHOR/9 EXECUTION; 12 TBD/4 PENDING; 15 in the Run History row; 16 register-table rows) match the CSV. All written text files use LF endings, carry no trailing whitespace, and end with a newline.

## 5. Epistemic notes

- DEP-02-02-001, 002, 004, 010, 011, 012 — FACT: identifiers appear verbatim in the `ScopeOfWork.md` front matter and applied row L308; the decomposition resolves each label. OBJ rows keep `TargetType=UNKNOWN` because the v3.1 enum has no objective type (existing convention; amendment C.7).
- DEP-02-02-003 — FACT that SOW-007 is absent from L308 and that DEC-025 retired its presentation half; retirement follows the brief's rule, not a judgment. The `_CONTEXT.md` residue is reported, not resolved.
- DEP-02-02-005 to 009 — FACT that each relation is still stated in live `ScopeOfWork.md` bytes; ASSUMPTION-free but dated: the SCA-APP-010 section labels these clauses compatibility history and L308 retains the code, routes, and tests. PROPOSAL (in `Notes`): retire them when an owner act removes the retained routes/code. They are kept ACTIVE at `Confidence=MEDIUM` because the brief's rule retires only relations no longer stated anywhere.
- DEP-02-02-013, 016 — FACT: stated on L308, the amended SOW rows, OI-008, and the seated Depends lines; `PENDING` bound to a named gate.
- DEP-02-02-014 — FACT that DEL-06-03 owns the tool and that the card renders `proposal.*`; ASSUMPTION that the card's payload follows the `propose` tool schema (L348 artifacts), not restated in this carrier's sources; hence `Confidence=MEDIUM`.
- DEP-02-02-021 — ASSUMPTION (amendment v1.1 C.1) that the host is DEL-02-03 as seated; FACT that the owner-adopted V3-04 Depends line names DEL-02-03-V3-01 as the host; FACT that L307 and L309 name no right-panel view switcher. `Confidence=MEDIUM` for that silence. Disposition-class, not an owner ruling.
- Held rows H-002 to H-007 — each was FACT-grounded in the v1 preview (see section 3a); holding them is a cycle-governance act by HELP_HUMAN, not a finding that the relations are unstated.
- Cross-reference edits to DEP-02-02-011 and DEP-02-02-014 `Notes` — PROPOSAL: the amendment names only the rows to remove and the counts to reconcile; leaving a `Notes` pointer to a now-absent register row would have carried a dangling reference into the carrier, so the pointer was redirected to H-002 with the reserved ID named. No non-`Notes` field changed; the reviewer may revert to the v1 wording if a stricter reading of section A is preferred.
- `FromDeliverableName` refresh on all rows — PROPOSAL: the stable ID governs; the display name follows L308 per `_REFERENCES.md` (no folder rename).
- Instruction root — the shell environment does not export `CHIRALITY_INSTRUCTION_ROOT`; the sealed brief names `agents/`, `skills/`, and `tools/` under the repository root, so the instruction root was resolved to `REPO_ROOT` from the brief and recorded as a warning in the run record rather than a stop.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
