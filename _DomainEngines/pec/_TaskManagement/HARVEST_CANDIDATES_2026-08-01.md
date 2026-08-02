# PEC Task Management — first candidate harvest

**Status:** PROMOTED — ALL SIX CANDIDATES MINTED 2026-08-01

**Date:** 2026-08-01

**Register basis:** `_DomainEngines/pec/_TaskManagement/REGISTER.csv`, schema
1.0, header-only at harvest

**Authority:** D-PEC-73 O-A permits on-demand Task Management and a first
harvest. K-TM-3 controls: this report proposes; only the owner promotes rows.

## Scan boundary

Read-only scan of PEC's structured decision register, routed notices, active
reliance-hold register, immutable run-record markers, and current
`ScopeOfWork.md` `CON-*`/`TBD-*` fields. No `FINDINGS.csv` or
`Review_Findings.csv` surface exists under the live PEC execution tree. The
active-reliance-hold register is valid and header-only.

Per the no-work-discovery rule, this pass did not harvest slates, work graphs,
`## Remaining` prose, ordinary planned work, or the already-live D-PEC-72
decision gate. D-PEC-03 is a non-operative pointer row, not an attention
candidate. The D-PEC-71 stale register note was corrected as ordinary
decision-register currency before this harvest and is not proposed as a row.

## Candidate proposals

### CAND-PEC-2026-08-01-01 — D-GOV-31 merge-policy succession

TM-CANDIDATE: Decide whether PEC acknowledges/adopts the simplified D-GOV-31 shared merge policy or deliberately retains its stricter local discipline | projects/pec/execution/_Coordination/NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md

| Field | Proposed value |
|---|---|
| Concern | The routed notice remains undispositioned. It says PEC must repin, adopt, acknowledge, amend, or decline; until then PEC's stricter local merge discipline controls. |
| SourceRef | `projects/pec/execution/_Coordination/NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md` |
| SourceSha | `f7b6a267f3149d3bf5af964570bbbfffbf827fe9cdab4fd230aa821310d236ac` |
| Domain lenses | Decisions; Approval; Checking |
| Suggested route | Owner triage. If acknowledged/adopted, `RESOLVED_BY_DECISION`; if stricter policy intentionally retained, record that decision rather than inferring it. |
| Priority / Assignment | `TBD` / human accountable; no agent as A |

### CAND-PEC-2026-08-01-02 — App/PEC client-boundary notice echo

TM-CANDIDATE: Disposition the two App-to-PEC notices whose acknowledgment remains tracked even though neither creates a PEC effect | projects/pec/execution/_Coordination/NOTICE_2026-07-27_D-APP-77_RB-PEC-ADAPTER_CURRENT_EVIDENCE_RETIREMENT.md; projects/pec/execution/_Coordination/NOTICE_2026-07-27_SCA-APP-005_APP_CLIENT_BOUNDARY.md

| Field | Proposed value |
|---|---|
| Concern | SCA-APP-005 confirms App owns client/package duties but not generic runtime semantics; D-APP-77 proposes retiring v0.4 adapter assertions as current evidence. Both state that PEC remains optional and unchanged, but acknowledgment is tracked as an open coordination item. |
| SourceRef | `projects/pec/execution/_Coordination/NOTICE_2026-07-27_D-APP-77_RB-PEC-ADAPTER_CURRENT_EVIDENCE_RETIREMENT.md`; `projects/pec/execution/_Coordination/NOTICE_2026-07-27_SCA-APP-005_APP_CLIENT_BOUNDARY.md` |
| SourceSha | `51e61ec4115d4f5ede2da352f5bbd06b9ea5ec559dcf88602758ffd5f9aa4ebd`; `22300269f7a8491ab65263bc5b76758e57ad9441a3f3ea67affa2c2faa2a2bf9` |
| Domain lenses | Decisions; Checking; Deliverables |
| Suggested route | Owner triage with likely `INFORMATIONAL_NO_ACTION`, citing PRD v2.2 §15 and the current DEL-07-05 contract posture; a different PEC client obligation would require its own instrument. |
| Priority / Assignment | `TBD` / human accountable; no agent as A |

### CAND-PEC-2026-08-01-03 — Legacy D-PEC-02 remains NOT_PREPARED

TM-CANDIDATE: Disposition the retired-product D-PEC-02 P3 decision row, which remains NOT_PREPARED after D-PEC-58 superseded the team-information-hub product | projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md row D-PEC-02

| Field | Proposed value |
|---|---|
| Concern | D-PEC-02 asks for post-pilot P3 scope of the retired reporting/team-information-hub product. D-PEC-58 retired that product framing, but this row remains mechanically open as `NOT_PREPARED`. |
| SourceRef | `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`, row `D-PEC-02` |
| SourceSha | `a5d7df0d77c07f4c37b1a39c19fc75c39182b6ef14d07265a7eb3a4a0603f8e3` |
| Domain lenses | Decisions; Planning; Deliverables |
| Suggested route | Owner triage; likely `OBE`, with a successor D-PEC decision/register-hygiene act citing D-PEC-58. Do not silently rewrite the historical row from this report. |
| Priority / Assignment | `TBD` / human accountable; no agent as A |

### CAND-PEC-2026-08-01-04 — DEL-04-01 feed-grammar boundary owner

TM-CANDIDATE: Resolve DEL-04-01 REQ-003's still-unnamed owner for the excluded feed-grammar act | projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md REQ-003

| Field | Proposed value |
|---|---|
| Concern | Immutable reconciliation marker `DEL-04-01-027` says `NEEDS_HUMAN_RULING`; the current contract still excludes defining a feed grammar but its cited claims name entity-model and rebuild owners, not the feed-grammar owners. W1 verification explicitly preserves this as an owner-resolution gap. |
| SourceRef | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md`, `REQ-003`; immutable marker at `projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_SOW_V22_SCA003_RECON_2026-07-28/WAVES/W1/DEL-04-01_claims.csv`, row `DEL-04-01-027` |
| SourceSha | current contract `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f`; immutable marker file `c710d17875712f731f9cfcdefac19da6649f61a00e557f241927a1f96c7e1b41` |
| Domain lenses | Deliverables; Work; Checking; Decisions |
| Suggested route | Owner triage, then a bounded deliverable-amendment package routed to PKG-04 WORKING_ITEMS. Candidate repair should name `DEL-02-01..07` as the feed-grammar owners without changing DEL-04-01 scope. |
| Priority / Assignment | `TBD` / human accountable; no agent as A |

### CAND-PEC-2026-08-01-05 — limitation inventory/response-format seam

TM-CANDIDATE: Decide whether the DEL-04-05 limitation-inventory and response-residence gaps require an SCA intake before the DEL-04-05/DEL-08-03 production seam is activated | projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md CON-002..004; projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md

| Field | Proposed value |
|---|---|
| Concern | DEL-04-05 records no accepted home/shape for the limitation inventory, no owner for absent-feed production, no settled residence/rendering point, and a trigger-set divergence that it identifies as scope-change-shaped. DEL-08-03 must preserve limitations but defines no limitation semantics. The current dependency basis has no direct edge joining the production seam. |
| SourceRef | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md`, `CON-002..004`; `projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` |
| SourceSha | `933c012cf16bb161b0ac1acdbf3caeaac408fa441b6e175b8fc2e7d8b265a579`; `013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138` |
| Domain lenses | Deliverables; Work; Planning; Checking; Decisions |
| Suggested route | Owner triage, then prepare an SCA intake for SCOPE_CHANGE if the owner wants upstream scope/edge correction before production. A production choice may declare representation inside existing bounds but may not silently widen `SOW-009`. |
| Priority / Assignment | `TBD` / human accountable; no agent as A |

### CAND-PEC-2026-08-01-06 — D-GOV-28 runtime-stewardship notice

TM-CANDIDATE: Disposition the unacknowledged D-GOV-28 runtime-stewardship notice without inventing a PEC client obligation | projects/pec/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md

| Field | Proposed value |
|---|---|
| Concern | The notice remains an open coordination item but expressly requires no immediate PEC adoption. It may matter only when a later PEC client-boundary or profile act cites the Root runtime basis. |
| SourceRef | `projects/pec/execution/_Coordination/NOTICE_D-GOV-28_ROOT_RUNTIME_STEWARDSHIP_PRD.md` |
| SourceSha | `28f6dfad9bab3bdfa0d3b81defd5d7a5fb4e98826175af6fc7bea744883af812` |
| Domain lenses | Decisions; Planning; Approval |
| Suggested route | Owner triage with likely `INFORMATIONAL_NO_ACTION`; retain the notice as citable basis for a later client/profile act. |
| Priority / Assignment | `TBD` / human accountable; no agent as A |

## Promotion outcome

Owner direction recorded verbatim on 2026-08-01:

```text
Promote: CAND-PEC-2026-08-01-01 through -06.
```

All six candidates were promoted in harvest order:

| Candidate | Register row |
|---|---|
| CAND-PEC-2026-08-01-01 | TM-PEC-001 |
| CAND-PEC-2026-08-01-02 | TM-PEC-002 |
| CAND-PEC-2026-08-01-03 | TM-PEC-003 |
| CAND-PEC-2026-08-01-04 | TM-PEC-004 |
| CAND-PEC-2026-08-01-05 | TM-PEC-005 |
| CAND-PEC-2026-08-01-06 | TM-PEC-006 |

The owner stated no assignment or priority judgment, so both remain `TBD` in
every row; no suggested route was promoted into a disposition. All rows are
`OPEN`, non-gating attention residue.

Promotion-time source hashes match the harvested hashes except for candidate
03's whole decision-register file: later D-PEC-72 activity changed that file
without changing the cited D-PEC-02 row. `TM-PEC-003.SourceSha` therefore uses
the current promotion-time file hash, while its Notes preserve the harvest-time
hash and the byte-identity finding. No candidate source concern was amended.
