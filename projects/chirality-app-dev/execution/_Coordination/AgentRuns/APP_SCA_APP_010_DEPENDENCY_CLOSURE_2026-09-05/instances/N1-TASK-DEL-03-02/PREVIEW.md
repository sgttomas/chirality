# PREVIEW — N1-TASK-DEL-03-02 — TASK + dependency-extract (report-only; rerun under brief amendment v1.1)

## 1. Header

| Field | Value |
|---|---|
| RunID / Node / Instance | `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` / N1 / `N1-TASK-DEL-03-02` |
| Brief version | `LAUNCH_BRIEF.md` v1 (binding) narrowed by `AMENDMENT_v1.1_N1_PREVIEWS.md` (sections A, B, D applied to this carrier); v1 outputs superseded in place, v1 run record `_run_records/TASK_RUN_2026-09-05_0038.md` retained |
| Carrier | `DEL-03-02` Thin TurnEngine and Session Locking (BACKEND_FEATURE_SLICE, PKG-03); `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-02_Thin_TurnEngine_and_Session_Locking` |
| Basis | `HEAD` = `d66395d101143df68d956984f7ab93f5027418ec` (exact; PR #713 merge) |
| Decomposition identity | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61` (match); content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291` (matches `ScopeOfWork.md` front matter pin); companion register `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca` (match); pointer `_ScopeChange/_LATEST.md` `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0` (match) |
| Authorization | SCA-APP-010 `FUTURE_WRITE_SET.csv` DEP-009 / DEP-010; `OWNER_ACTION_MATRIX.csv` step 19; `DOWNSTREAM_HANDOFFS.csv` row 3; APP-HOLD preflight `Evidence/app_hold/DEL-03-02.json` verdict ALLOW; amendment v1.1 (HELP_HUMAN supervisory disposition; widens no authority, changes no fence) |
| Pre-image `Dependencies.csv` | `f8efee202c2e4f35fb3fea34b536b7d339abd52a1940a099320dff15f89758dd` (match; 10 data rows, 29 columns, no quoted fields, LF) |
| Pre-image `_DEPENDENCIES.md` | `98fe53bec8b3b1c5d4199bd68e27c00f84a3d570034c8749bb650fbed44c9a40` (match) |
| Post-image `POSTIMAGE_Dependencies.csv` | `be877cffd700069afae17a3f604af28bc2e666c5608b833aff814ce51c291458` (14 data rows, 29 columns, no quoted fields, LF; v1 post-image was `972b9e818892488325ca86410a91111e4e54322c52b0d69136a9832f80567415`) |
| Post-image `POSTIMAGE__DEPENDENCIES.md` | `dffe9d126bebeb967dc9e0a109c528b44b22b7daf374cda4079f3fc349da7eb8` (v1 post-image was `a056c1949b4bfb7254b994d35ed089a3ec87824939ff3ca20a484ce7f645a40c`) |
| Row census pre | total 10 / ACTIVE 10 / RETIRED 0 / ANCHOR 5 / EXECUTION 5 |
| Row census post | total 14 / ACTIVE 14 / RETIRED 0 / ANCHOR 7 / EXECUTION 7 (v1 preview: 15 / 15 / 0 / 7 / 8; one row held under amendment section A) |
| Satisfaction pre → post | SATISFIED 5, PENDING 5 → SATISFIED 5, PENDING 9 |
| Carrier bytes | unchanged (`Dependencies.csv` `f8efee20…`, `_DEPENDENCIES.md` `98fe53be…`, `ScopeOfWork.md` `1651f6a7…`, `_CONTEXT.md` `0cd3509b…`, `_STATUS.md` `c8506e6b…`, `_REFERENCES.md` `38cca550…` re-hashed before and after the rerun; `git status` shows only the run folder as untracked) |

SCC-001 membership used for F1 (from `Evidence/baseline_closure/scc_summary.csv`): DEL-02-05, DEL-03-02, DEL-03-03, DEL-03-04, DEL-04-03, DEL-04-05, DEL-05-02, DEL-05-03, DEL-05-05.

## 2. Row-level diff

`UNCHANGED` means byte-identical. `RE-EVIDENCED` means `EvidenceFile`/`SourceRef`/`EvidenceQuote` moved to live bytes, `TargetLocation` line refreshed, `LastSeen` refreshed, and a dated `Notes` suffix appended; every other field is preserved. `RE-EVIDENCED (SCC-internal, evidence fields only)` is the amendment v1.1 section B class: only `EvidenceFile`, `SourceRef`, `EvidenceQuote`, the `TargetLocation` line pointer, and `LastSeen` changed; `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `TargetDeliverableID`, `Status`, `Statement`, `SatisfactionStatus`, `Origin`, `FirstSeen`, and (outside the enumerated set) `Notes` are byte-identical to the pre-image.

| DependencyID | Change | Class/AnchorType | Direction/Type | Target | EvidenceFile#SourceRef | Note |
|---|---|---|---|---|---|---|
| DEP-03-02-001 | RE-EVIDENCED | ANCHOR/IMPLEMENTS_NODE | UPSTREAM/OTHER | WBS_NODE PKG-03 (decomp L281) | `ScopeOfWork.md#CLM-002 — Identification` | was `Datasheet.md#Identification`; TargetLocation `:257` → `:281` |
| DEP-03-02-002 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-009 (ledger L412) | `ScopeOfWork.md#Purpose and Objective Traceability` | was `Datasheet.md#Identification`; `:385` → `:412` |
| DEP-03-02-003 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-010 (ledger L413; SSOW L180 amended) | `ScopeOfWork.md#Purpose and Objective Traceability` | was `Datasheet.md#Identification`; `:386` → `:413`; TargetName label refreshed to "Session boot-request binding including per-chat delegation policy" |
| DEP-03-02-004 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-011 (ledger L414) | `ScopeOfWork.md#Purpose and Objective Traceability` | was `Datasheet.md#Identification`; `:387` → `:414` |
| DEP-03-02-005 | RE-EVIDENCED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-038 (ledger L441) | `ScopeOfWork.md#Purpose and Objective Traceability` | was `Datasheet.md#Identification`; `:414` → `:441` |
| DEP-03-02-006 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-03-01 (decomp L317; not SCC-001) | `ScopeOfWork.md#CLM-009 — Requirements (DEL-03-02-REQ-002)` | was `Specification.md#Requirements`; `:293` → `:317`; SATISFIED preserved |
| DEP-03-02-007 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | DELIVERABLE DEL-05-02 (decomp L337; SCC-001) | `ScopeOfWork.md#CLM-009 — Requirements (DEL-03-02-REQ-008)` | was `Specification.md#Requirements`; `:313` → `:337`; quote now REQ-008 L203 "Persist turn.accepted before SDK/model/provider execution begins; …"; `LastSeen` 2026-07-12 → 2026-09-05; SATISFIED, Statement, Notes preserved |
| DEP-03-02-008 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/INTERFACE | DELIVERABLE DEL-03-03 (decomp L319; SCC-001) | `ScopeOfWork.md#CLM-009 — Requirements (DEL-03-02-REQ-007)` | was `Procedure.md#Steps`; `:295` → `:319`; quote now REQ-007 L202 "Preserve existing browser-facing SSE event names during SDK adoption and TurnEngine extraction."; `LastSeen` refreshed; SATISFIED, Statement, Notes preserved |
| DEP-03-02-009 | RE-EVIDENCED (SCC-internal, evidence fields only) | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/INTERFACE | DELIVERABLE DEL-03-04 (decomp L320; SCC-001) | `ScopeOfWork.md#CLM-023 — Trade-offs` | was `Guidance.md#Trade-offs`; `:296` → `:320`; quote now CLM-023 L466 "Implement lock cleanup/cancellation signal boundary now; defer full interrupt/cancel outcome handling to DEL-03-04 where needed."; `LastSeen` refreshed; SATISFIED, Statement, Notes preserved |
| DEP-03-02-010 | RE-EVIDENCED | EXECUTION/NOT_APPLICABLE | DOWNSTREAM/ENABLES | DELIVERABLE DEL-09-03 (decomp L380; not SCC-001) | `ScopeOfWork.md#CLM-017 — Verification` | was `Procedure.md#Verification`; `:356` → `:380`; SATISFIED preserved |
| DEP-03-02-011 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | REQUIREMENT SOW-083 (ledger L486; SSOW L253) | `ScopeOfWork.md#Purpose and Objective Traceability` | new scope ref on applied row L318 (DEC-025); PENDING |
| DEP-03-02-012 | ADDED | ANCHOR/TRACES_TO_REQUIREMENT | UPSTREAM/OTHER | UNKNOWN OBJ-002 (decomp L263) | `ScopeOfWork.md#Purpose and Objective Traceability` | objective anchor; `TargetType=UNKNOWN` per the existing App convention (no OBJECTIVE enum) |
| DEP-03-02-014 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/CONSTRAINT | EXTERNAL `ROOT-DEL-02-11-DELEGATION-POLICY-FIELD`, TargetLocation TBD | `…SOFTWARE_DECOMP_v3_2.md#L318` | Root-owned session-record field (OI-008 L602); PENDING; no Root path |
| DEP-03-02-015 | ADDED | EXECUTION/NOT_APPLICABLE | UPSTREAM/INTERFACE | EXTERNAL `ROOT-DAEMON-SESSION-LIFECYCLE-AND-LOCK`, TargetLocation TBD | `…SOFTWARE_DECOMP_v3_2.md#L318` | generic TurnEngine and lock ownership remain Root-owned; PENDING; no Root path |

Rows retired: none (every pre-image relation is restated in the live sources; no anchor points to a scope ref that left the applied row). Rows deleted from the carrier register: none (DEP-03-02-013 was never written to the carrier; its removal from this post-image is a held proposal, not a register deletion, and its ID stays reserved). `Status=CANDIDATE`: not emitted. `Origin=DECLARED` rows: none existed. IDs are not renumbered: the register runs 001..012, 014, 015.

## Held proposals (amendment v1.1)

| HeldID | Reserved DependencyID | Edge | Direction/Type | Evidence it would have cited | Disposition |
|---|---|---|---|---|---|
| H-015 | DEP-03-02-013 | DEL-03-02 → DEL-08-04 Type 2 Subagent Governance Bridge (bound per-chat delegation policy honoured by the managed delegation bridge) | DOWNSTREAM/INTERFACE, EXPLICIT, HIGH | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md#L253` ("with the session and honour it in the Chirality-managed delegation bridge"); DEL-08-04 row L371; `ScopeOfWork.md#Current acceptance obligations` item 3; `_STATUS.md#Remaining` DEL-03-02-V3-01 Depends (the bridge that honours the bound policy) | HELD_NON_EMITTED_PENDING_OWNER_RULING — with the other fourteen held edges it would join SCC-001 into the simulated 20-node SCC (`Evidence/fanin_simulation_v1/edge_analysis.json`); recorded in `HELD_EDGE_PROPOSALS.csv` H-015 for the owner's separate transaction; reciprocal DEL-08-04 row held as H-019 |

## 3. Fence results

- **F1 (SCC-001):** `NONE` — no new EXECUTION row has both endpoints inside SCC-001 (014 and 015 are EXTERNAL; the DEL-08-04 edge is held, and DEL-08-04 is not an SCC-001 member in any case). No SCC-internal edge added or retired. SCC-internal rows 007/008/009 had only the amendment-permitted evidence fields refreshed; every graph-bearing field is byte-identical to the pre-image.
- **F2 (Root path):** `NONE` — no `TargetLocation` names a Root path; both Root-owned targets are `EXTERNAL` with `TargetLocation=TBD`. Resolved deliverable `TargetLocation`s name only `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:<line>` under `projects/chirality-app-dev/**`.
- **F3 (permitted effect):** `NONE` — emitted rows derive only from SOW-010 L180, SOW-083 L253, the applied row L318 prose, and their restatements in `ScopeOfWork.md`/`_CONTEXT.md`/`_STATUS.md#Remaining`. The `NOT_SELECTABLE_UNTIL: DEL-08-04-V3-02 selected` gate is schedule and was not converted into an edge; no "keep aligned"/coordination statement was converted.
- **NEEDS_HUMAN_GRAPH_DECISION:** `none`. The v1 entries for `DEP-03-02-007`, `DEP-03-02-008`, `DEP-03-02-009` are cleared: amendment v1.1 section B permits the evidence-field-only refresh, which this rerun performed; all three rows now resolve to `ScopeOfWork.md` live bytes (REQ-008 L203, REQ-007 L202, CLM-023 L466).
- **FENCE_F1_CANDIDATES:** `none` — no SCC-internal edge was considered for addition or retirement. (Observation only: the applied row L318 and `ScopeOfWork.md` also restate the DEL-05-02, DEL-03-03, and DEL-03-04 relations already carried by 007/008/009; no additional SCC-internal edge is stated.)
- **FENCE_F2_CANDIDATES:** `none` — no candidate required a Root path. Evidence that would have been cited for a Root location: none available in the allowed sources (OI-008 L602 names Root DEL-02-11 by ID only).

## 4. Validator outputs (verbatim)

`PYTHONDONTWRITEBYTECODE=1 python3 tools/validation/validate_dependencies_schema.py projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-03-02/POSTIMAGE_Dependencies.csv`

```text
VALID: projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-03-02/POSTIMAGE_Dependencies.csv
  Columns: 29 (29 required + 0 extension)
  Data rows: 14
exit=0
```

`python3 tools/validation/validate_enum.py <ENUM> <value>` for every emitted or changed value (23 calls, all exit 0):

```text
VALID: ANCHOR is a valid DEPENDENCY_CLASS
VALID: EXECUTION is a valid DEPENDENCY_CLASS
VALID: IMPLEMENTS_NODE is a valid ANCHOR_TYPE
VALID: TRACES_TO_REQUIREMENT is a valid ANCHOR_TYPE
VALID: NOT_APPLICABLE is a valid ANCHOR_TYPE
VALID: UPSTREAM is a valid DIRECTION
VALID: DOWNSTREAM is a valid DIRECTION
VALID: OTHER is a valid DEPENDENCY_TYPE
VALID: INTERFACE is a valid DEPENDENCY_TYPE
VALID: ENABLES is a valid DEPENDENCY_TYPE
VALID: CONSTRAINT is a valid DEPENDENCY_TYPE
VALID: WBS_NODE is a valid TARGET_TYPE
VALID: REQUIREMENT is a valid TARGET_TYPE
VALID: UNKNOWN is a valid TARGET_TYPE
VALID: DELIVERABLE is a valid TARGET_TYPE
VALID: EXTERNAL is a valid TARGET_TYPE
VALID: EXPLICIT is a valid EXPLICITNESS
VALID: HIGH is a valid CONFIDENCE
VALID: MEDIUM is a valid CONFIDENCE
VALID: EXTRACTED is a valid ORIGIN
VALID: ACTIVE is a valid STATUS
VALID: PENDING is a valid SATISFACTION_STATUS
VALID: SATISFIED is a valid SATISFACTION_STATUS
```

`zsh tools/validation/validate_id_format.sh` (known `PROJECT_ID_FORMAT_PROFILE` warning; no ID changed):

```text
INVALID: DEL-03-02 does not match DEL format (^DEL-[0-9]{3}-[0-9]{2}$)
DEL exit=1
INVALID: PKG-03 does not match PKG format (^PKG-[0-9]{3}$)
PKG exit=1
INVALID: DEP-03-02-011 does not match DEP format (^DEP-[0-9]{3}-[0-9]{2}-[0-9]{3}$)
DEP exit=1
INVALID: SOW-083 does not match SOW format (^SOW-[0-9]{4}[a-z]?$)
SOW exit=1
VALID: OBJ-002 matches OBJ format
OBJ exit=0
```

Anchor and register checks (Python over the post-image CSV; frozen-field assertions on 007/008/009 passed before write):

```text
unique ids True 14
from ok True
one active IMPLEMENTS_NODE 1
active evidence True
{'total': 14, 'ACTIVE': 14, 'ANCHOR': 7, 'SAT=PENDING': 9, 'PM=TBD': 9, 'ORIG=EXTRACTED': 14, 'EXECUTION': 7, 'SAT=SATISFIED': 5, 'PM=SATISFIED': 5}
candidate False
root paths []
legacy kit refs []
md table ids == csv ids: True 14
```

Live-bytes resolution: `ScopeOfWork.md` headings `## Purpose and Objective Traceability` (L12), `### Current responsibility` (L29), `### Current acceptance obligations` (L44), `### CLM-002 — Identification` (L66), `### CLM-009 — Requirements` (L190), `### CLM-017 — Verification` (L366), `### CLM-023 — Trade-offs` (L457); `_CONTEXT.md#Deliverable Scope` (L26); `_STATUS.md#Remaining` (L9). Every `EvidenceQuote` on a RE-EVIDENCED, RE-EVIDENCED (SCC-internal), or ADDED row is a verbatim substring of its cited source with backticks stripped, except the `## Purpose and Objective Traceability` quote shared by rows 002..005, 011, 012, which additionally drops the bracket-list punctuation of L14 (`[SOW-009, SOW-010, …]`) to keep the register comma-free; that quote is unchanged from v1 and is not part of this rerun. No row cites the retired legacy kit.

Whitespace: both post-images have LF endings, no trailing whitespace, and a final newline. `_DEPENDENCIES.md` count tables reconcile to the CSV (Total 14; ACTIVE 14; RETIRED 0; ANCHOR 7; EXECUTION 7; DECLARED 0; EXTRACTED 14; PENDING 9; SATISFIED 5; ProposedMaturity=TBD 9). The 2026-09-05 Run History row sits under `## Run History` with ACTIVE 14.

## 5. Epistemic notes

- DEP-03-02-001..005, 010 — FACT: relation unchanged; only evidence moved from the retired kit to `ScopeOfWork.md` and decomposition line pointers refreshed. For 003 the `TargetName` label follows the amended ledger statement (SSOW L180 / ledger L413); the SOW-010 identity and anchor are unchanged.
- DEP-03-02-006 — FACT: REQ-002 now names the `IAgentSdkManager` port used by `TurnEngine`; CLM-003 still names `AgentEnginePort` / `RuntimeEngineContract`. The Statement was left as written (relation to DEL-03-01 unchanged); the quote cites REQ-002.
- DEP-03-02-007 — FACT: REQ-008 (L203) restates the accepted-turn persistence relation to the runtime event surface owned by DEL-05-02; REQ-009 (L204) restates the terminal-outcome half. The quote cites REQ-008 because it is the pre-image statement's direct restatement; the Statement and Notes are frozen under the amendment.
- DEP-03-02-008 — FACT: REQ-007 (L202) restates the browser-facing SSE event-name preservation relation to DEL-03-03 verbatim in substance; Scope Ledger L414 lists DEL-03-03 as co-carrier of SOW-011.
- DEP-03-02-009 — FACT: CLM-023 (L466) restates the pre-image `Guidance.md#Trade-offs` statement ("defer full interrupt/cancel outcome handling to DEL-03-04 where needed") and names DEL-03-04 as owner of interrupt/cancel terminal handling; REQ-005 (L200) carries the same boundary ("Exact interrupt semantics TBD with DEL-03-04"). CLM-023 was chosen as the like-for-like successor of the legacy Trade-offs pointer.
- DEP-03-02-011 — FACT: SOW-083 is on the applied row L318 and ledger L486 (DEC-025). ASSUMPTION (labelled in Statement): DEL-03-02's half is the boot-request binding, per L253 "App binds the request (SOW-010)" and the seated item DEL-03-02-V3-01.
- DEP-03-02-012 — FACT: OBJ-002 is in `ScopeOfWork.md` front matter and the applied row. Convention choice (`TargetType=UNKNOWN`) follows the brief and the existing App convention (e.g. DEL-03-04 register).
- DEP-03-02-013 (held) — FACT: SSOW L253 and DEL-08-04 row L371 state the bridge honours the policy carried with the session; `_STATUS.md#Remaining` names DEL-08-04-V3-02 as "the bridge that honours the bound policy". PROPOSAL (direction): DOWNSTREAM because the bound policy flows from this carrier's boot binding to the bridge. Held, not emitted: see the Held proposals section; the evidence stands as recorded in `HELD_EDGE_PROPOSALS.csv` H-015 and is not re-argued here.
- DEP-03-02-014 — FACT: Root DEL-02-11 owns the session-record field (L318 Notes; OI-008 L602; `ScopeOfWork.md` obligation 3). `DependencyType=CONSTRAINT` because Root ownership bounds what this carrier may persist; `SatisfactionStatus=PENDING` until Root acceptance is routed (OI-008).
- DEP-03-02-015 — FACT: L318 Description and Notes ("generic TurnEngine and lock ownership remain Root-owned"), restated by `ScopeOfWork.md` obligation 1 and `_CONTEXT.md#Deliverable Scope`. `DependencyType=INTERFACE` follows the App convention for consumed Root-owned semantics (e.g. DEL-05-01-013, DEL-03-01-009). PROPOSAL: this row is the Root-side counterpart to the App-side deliverable edges 006..010; it does not replace them.
- Not emitted (CONSERVATIVE): edges to DEL-07-01 (registered project identity/root), DEL-04-04 (persona), DEL-04-02/DEL-02-04 (options), and DEL-05-01 (SOW-009 co-carrier) — none is stated as an information/artifact transfer for this carrier in the allowed sources.

## 6. Attribution

Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) as a Claude Code subagent acting as TASK + dependency-extract (report-only preview), dispatched by HELP_HUMAN; role not mechanically enforced; no descendant launched.
