# App Objective-Relative DAG — v3 Release Pathway

**Graph source:** `WORK_GRAPH.json`
**State:** `ASSESSMENT_ONLY — AWAITING_OWNER_ACCEPTANCE`
**Objective:** establish an App-side path from governed carriers to an owner-gated rc.1 operation while preserving Root ownership, holds, class distinctions, and exact-candidate gates.

## Reading rule

Every App node is a live deliverable folder. The two Root nodes are typed notice edges, not App-owned work and not foreign-loop writes. A solid edge is proposed gating order. A dashed edge is objective feedback inside an SCC and is explicitly non-gating until the proposed move is owner-accepted.

```text
E-001  ROOT_NOTICE_D_GOV_35           ──> DEL-08-04
E-002  ROOT_NOTICE_D_GOV_35           ──> DEL-08-05
E-003  ROOT_NOTICE_SCA_004_APPLIED    ──> DEL-04-01
E-004  ROOT_NOTICE_SCA_004_APPLIED    ──> DEL-03-01
E-005  ROOT_NOTICE_SCA_004_APPLIED    ──> DEL-03-03
E-006  ROOT_NOTICE_SCA_004_APPLIED    ──> DEL-02-05
E-007  ROOT_NOTICE_SCA_004_APPLIED    ──> DEL-05-01
E-008  DEL-01-01                      ──> DEL-04-01
E-009  DEL-04-01                      ──> DEL-03-01
E-010  DEL-03-01                      ──> DEL-03-03
E-011  DEL-03-03                      ──> DEL-05-02
E-012  DEL-05-02                      ──> DEL-05-03
E-013  DEL-02-05                      ──> DEL-04-05
E-014  DEL-04-05                      ──> DEL-09-06
E-015  DEL-05-01                      ──> DEL-05-04
E-016  DEL-03-03                      ──> DEL-05-04
E-017  DEL-02-05                      ──> DEL-05-01
E-018  DEL-05-04                    - -> DEL-02-05  [NON-GATING]
E-019  DEL-08-04                      ──> DEL-08-05
E-020  DEL-08-05                    - -> DEL-08-04  [NON-GATING]
E-021  DEL-08-04                      ──> DEL-09-02
E-022  DEL-08-05                      ──> DEL-09-02
E-023  DEL-02-02                      ──> DEL-09-03
E-024  DEL-03-01                      ──> DEL-09-01
E-025  DEL-05-02                      ──> DEL-09-02
E-026  DEL-05-03                      ──> DEL-09-06
E-027  DEL-09-04                      ──> DEL-09-05
E-028  DEL-09-01                      ──> DEL-09-05
E-029  DEL-09-02                      ──> DEL-09-05
E-030  DEL-09-03                      ──> DEL-09-05
E-031  DEL-09-06                      ──> DEL-09-05
E-032  DEL-09-05                    - -> DEL-09-06  [NON-GATING]
```

This is an exact adjacency rendering of all 32 JSON edges. `WORK_GRAPH.json` remains authoritative for this derivative assessment.

## Stage interpretation

| Objective stage | App carriers | Required upstream | Result supported |
| --- | --- | --- | --- |
| Governed basis | DEL-01-01 and this SCA assessment | Owner acceptance of exact SCA bytes | Carrier/contract proposal only; no implementation. |
| Probe and contract evidence | DEL-04-01, DEL-03-01 | Root SCA-004 notice edge; separate supply authority | Exact evidence for G1/G2; no adoption inferred. |
| Account/consent and session vocabulary | DEL-02-05, DEL-04-05, DEL-05-01, DEL-05-04 | Accepted Root account/consent/storage contract | Root-private login, consent, migration, and honest resume/fresh behavior. |
| Adapter/event consumption | DEL-03-03, DEL-05-02/03 | Root API/event schema v2 | App compatibility, typed terminals, redacted sinks. |
| Delegation/containment | DEL-08-04/05 | D-GOV-35 notice edge plus WP-03/05 fixtures | Managed/native class-aware App behavior and evidence. |
| Desktop UX/privacy | DEL-02-02/05, DEL-09-06 | Stable contracts and carrier acceptance | Labelled role entry, consent/login, typed storage, sender checks, accessibility/security. |
| Unsigned preparation | DEL-09-04/05/06 | Supply freeze and accepted carrier | Unsigned/ad-hoc package and reviewed procedure, no release claim. |
| Conformance fan-in | DEL-09-01/02/03/06 | Each activated carrier and RQG §13 | Evidence for later owner gate; no automatic readiness. |
| Owner release operation | DEL-09-05 | G6a exact-candidate owner ruling; D-APP-97/F-APP-2 lifted only for that candidate | Owner/CHANGE procedure may run under separate authority. |

## Cross-loop notice edges

### ROOT_NOTICE_D_GOV_35

- Evidence: `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`
- SHA-256: `9b8ebfe16e5241bc2c58b4bbc71032837632f5b07d776e82f11a273d2469cee7`
- Meaning: D-GOV-35 is ruled/applied; App may adopt/amend/decline only through its own SCA/WP-06 instruments.
- App consequence: DEL-08-04 remains the managed carrier while DEL-08-04/05/09-02 also consume and evidence the distinct native class.

### ROOT_NOTICE_SCA_004_APPLIED

- Evidence identity: Root SCA-004 revision 1.3, Gate-5 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`, owner confirmation R6-A, seven accepted Root-carrier SOWs at R7-A.
- Meaning: Root contract/implementation carriers exist as accepted context; App does not re-derive or edit them.
- App consequence: App probe, account/consent, adapter/event, migration, validation, and packaging work wait for the exact accepted Root outputs they consume.

## SCC register

### SCC-DELEGATION-EVIDENCE

- Members: DEL-08-04, DEL-08-05.
- Objective-relative cycle: governance semantics define evidence, while evidence requirements feed back into reconstructibility.
- Proposed move: `DECOMPOSE`.
- Proposed order: accept managed/native class semantics and role calibration in DEL-08-04; then define DEL-08-05 evidence fields.
- Non-gating edge: DEL-08-05 → DEL-08-04 evidence feedback.
- Human gate: SCA-APP-008 acceptance. No silent linearization.

### SCC-ACCOUNT-MIGRATION-UX

- Members: DEL-02-05, DEL-05-01, DEL-05-04.
- Objective-relative cycle: UX names account/consent/resume states, migration must materialize them, and replay/resume findings can change UX treatment.
- Proposed move: `DECOMPOSE`.
- Proposed order: accept account/consent vocabulary; define non-destructive migration; then render resume/fresh/replay behavior.
- Non-gating edge: DEL-05-04 → DEL-02-05 UX feedback.
- Human gate: accepted Root/App account/consent contract.

### SCC-RUNBOOK-VALIDATION

- Members: DEL-09-05, DEL-09-06.
- Objective-relative cycle: the runbook states security checks and security review feeds corrections into the runbook.
- Proposed move: `INVERT` the misleading “release procedure first” reading.
- Proposed order: author a WP-09 draft, validate its security assumptions and exact preparation evidence, then freeze the procedure for the G6a exact candidate; WP-11 execution remains later.
- Non-gating edge: DEL-09-05 → DEL-09-06 review feedback.
- Human gate: G6a exact-candidate ruling.

No SCC is resolved by cut or merge in this assessment. Cycle-participating feedback edges stay non-gating.

## Gating overlays

1. **WP-00/A1:** R20 proves the prior staged revision. Future frontend mutation requires re-stage and fresh owner proof for any future claim.
2. **G0.5/G1:** exact SCA carrier/contract acceptance and RQG §13 mapping; Electron drift remains a G1 blocker.
3. **WP-03/05:** explicit implementation act required; carrier acceptance alone is insufficient.
4. **WP-06:** D-GOV-35 landing is necessary but not sufficient; App carrier and containment/role/approval gates remain.
5. **Preparation:** D-APP-97/F-APP-2 remain active. Unsigned/ad-hoc evidence cannot lift them.
6. **G6a:** only the owner can name the exact candidate and authorize the separate release lane.
7. **Target:** macOS arm64 only; second target requires post-rc.1 scope change.

## Resolution check

All `APP_DELIVERABLE` paths in `WORK_GRAPH.json` exist at basis commit `3af765222bbd4f43a52dcbe17bd151c13942e5ac`. The only non-App-deliverable nodes are the two explicitly typed Root notice edges above. The graph grants no foreign-loop write or authority inference.
