---
amendment_id: SCA-004
doc_kind: scope_change.amendment_preview
decomp_variant: SOFTWARE
gate: 3
created: 2026-08-23
status: awaiting_gate_3_approval
accepted_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md revision 1.2 at sha256 23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d
requested_by: Ryan Tufts through R2-A
---

# SCA-004 Gate 3 — exact amendment preview

## Approval scope

This is the complete proposed revision 1.2 → 1.3 amendment for the eight
Gate-1 actions accepted at R1-C and impact-assessed at Gate 2 under R2-A. It
is a candidate only. No file under `execution/_Decomposition/`, no live
deliverable folder, no `_STATUS.md`, and no `_LATEST.md` pointer has changed.

The exact candidate bytes are the seven files under `Gate_3_Candidate/`. The
complete native-line-ending patch is `Gate_3_Exact_Amendment.diff`; apply
checking uses `git apply --unidiff-zero --check`. The deterministic validator
reports `PASS`: 98 checks, 0 failures.

## Change register — addition

```diff
+ DEC-025 (2026-08-23): preserve DEL-02-06 as the standing semantic-
+ integration/release-assurance carrier; allocate bounded runtime
+ implementation and conformance to DEL-02-07..DEL-02-12 under PKG-02; add
+ DEL-04-11 under PKG-04 as a TEST_SUITE mapped to SOW-041, SOW-053, and
+ OBJ-003; retain every existing ID, package, scope item, objective, REQ-027
+ boundary, and all ten HELD_UNAVAILABLE bindings.
```

The working surface becomes an explicitly non-effective SCA-004 revision 1.3
candidate. Revision 1.2 at SHA-256
`23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`
remains the accepted live basis.

## Deliverables — before → after

### Topology

```diff
- total 46; PKG-02 6; PKG-04 10
+ total 53; PKG-02 12; PKG-04 11
  packages 6; scope items 104; objectives 7
```

### DEL-02-06 — modified, stable ID and lineage retained

```diff
- standing generic-runtime carrier whose activation could include a bounded
- implementation/client tranche
+ standing semantic-integration and release-assurance carrier that preserves
+ SOW-104, OBJ-001/002/004/007, REQ-027, D-GOV-20, the versioned contract,
+ affected-client fan-in, and the ten-binding hold matrix; implementation and
+ conformance domains are split to DEL-02-07..DEL-02-12
```

`Type=REQ_SLICE`, `ContextEnvelope=M`, `CoversScopeItems=SOW-104`, and
`SupportsObjectives=OBJ-001;OBJ-002;OBJ-004;OBJ-007` remain unchanged.

### Seven leaf additions

| Deliverable | Parent | Type | Envelope | Scope | Objectives | Primary artifact shape |
|---|---|---|---|---|---|---|
| `DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control` | PKG-02 | `BACKEND_FEATURE_SLICE` | M | SOW-104 | OBJ-001/002/004/007 | supervisor port, private-socket token/owner/generation/stale-recovery controls, worker fencing, two-job launch, role parity and hard-containment tests |
| `DEL-02-08_Exact_Supply_and_Protocol_Pinning` | PKG-02 | `API_CONTRACT` | M | SOW-104 | OBJ-001/002/004/007 | exact supply/protocol contract, enumerated service endpoints, three-posture exact-pin G-APPR fixtures |
| `DEL-02-09_Hosted_Account_and_Consent_Boundary` | PKG-02 | `SECURITY_CONTROL` | M | SOW-104 | OBJ-001/002/004/007 | consent port, root-private home, role posture/parity, labelled fallback, three network postures |
| `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2` | PKG-02 | `API_CONTRACT` | M | SOW-104 | OBJ-001/002/004/007 | Root API v2, attributed approvals, role evidence, closed event union with only `turn.completed` / `turn.failed` / `turn.interrupted` / `turn.cancelled`, exact prompt routing |
| `DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation` | PKG-02 | `BACKEND_FEATURE_SLICE` | M | SOW-104 | OBJ-001/002/004/007 | retirement port/journal, exactly-once terminalization, conditional resume/fresh-thread recovery |
| `DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in` | PKG-02 | `TEST_SUITE` | M | SOW-104 | OBJ-001/002/004/007 | Root/client conformance, exact source identity, A3/A7 exact-pin evidence, shared-release fan-in |
| `DEL-04-11_Root_Loop_Receipt_Validator` | PKG-04 | `TEST_SUITE` | M | SOW-041; SOW-053 | OBJ-003 | Root-specific deterministic receipt validator and fixtures |

Every row has an exact name, description, responsible party, type,
anticipated artifacts, Context Envelope and notes, scope/objective mappings,
and anticipated write locus in the candidate deliverable register. The loci
are planning notes, never authorization. `tools/** (M2)` for DEL-04-11 remains
separately gated.

The candidate also makes the current OI-011 responsibility state concordant
with the 53-row register: D-GOV-27 assigned Ryan Tufts to the original 45
deliverables, SCA-001 carried that assignment to DEL-02-06, and all seven
SCA-004 candidate rows carry the same assignment. The working surface and
coverage telemetry both record OI-011 closed across all 53 deliverables.
The candidate's other current-state narrative is synchronized as well:
D-12 names PKG-04's projected 11 deliverables, and telemetry retains
DEL-04-09 at Context Envelope `L` as already accepted by D-GOV-25 Gate 5 with
OI-010 `CLOSED_ACCEPTED_AT_GATE_5`; neither assertion reopens a ruling.
DEL-02-07 also binds every socket request to an authentication token tied to
the socket owner and worker generation and invalidated by stale-socket
recovery, while preserving Unix-only `0700`/`0600`, sole-broker,
renderer/CLI exclusion, and no-TCP controls. DEL-02-10 names the exact four
and only HarnessEvent v2 terminal identifiers while preserving attributed
approvals, unknown-payload rejection/projection/redaction, A3/A7 carriage,
and the provider-shaped-persistence exclusion.

### Accepted G0 A3/A4/A7 carriage

The exact candidate deliverable rows, rather than this preview alone, carry
the controlling amendments:

- A3 is allocated across DEL-02-07/09/10/12. Agent 0/1/2 role entry is always
  offered for Codex sessions. If G-ROLE cannot mechanically prove Agent-2
  non-delegation, explicit Agent 2/TASK remains offered labelled
  `role not mechanically enforced`; governed-workflow evidence is
  `instruction-asserted`; delegated-harness-native K-SUBAGENT
  non-delegation is instruction+config asserted rather than mechanism-proven;
  hard filesystem/network/process containment is unchanged.
- A4 remains exact in DEL-02-11: active turns terminalize; `thread/resume`
  occurs only with canonical-root, account-identity, policy-digest, and cwd
  continuity; otherwise a fresh thread; no in-flight re-attach is claimed.
- A7 is allocated across DEL-02-08/09/10/12. Each canonical root chooses no
  command network by default; ask per destination through routed
  `networkApprovalContext` showing host/protocol, with the caveat that a
  grant may unblock queued requests to the same destination and
  `acceptForSession` allowed only by explicit user act; or labelled command
  network on (`network_access = true`). OpenAI service endpoints are
  separately enumerated, and G-APPR must prove prompt delivery and observe
  destination grouping empirically at the exact pin.

## Scope Ledger — exact allocation

```diff
  SOW-104 PackageID = PKG-02 (unchanged)
- DeliverableIDs = DEL-02-06
+ DeliverableIDs = DEL-02-06; DEL-02-07; DEL-02-08; DEL-02-09;
+                  DEL-02-10; DEL-02-11; DEL-02-12
  ObjectiveIDs = OBJ-001;OBJ-002;OBJ-004;OBJ-007 (unchanged)
  DecisionRef = DEC-022 → DEC-022;DEC-025

  SOW-041 PackageID = PKG-04 (unchanged)
- DeliverableIDs = DEL-04-05
+ DeliverableIDs = DEL-04-05;DEL-04-11

  SOW-053 PackageID = PKG-05 (unchanged; partition fact)
- DeliverableIDs = DEL-05-02
+ DeliverableIDs = DEL-05-02;DEL-04-11
```

The SOW-053 cross-package coverage mapping is lawful under DEC-010: only the
scope item's `PackageID` is exclusive. This exact allocation keeps DEL-04-05
as the loop/receipt doctrine carrier, DEL-05-02 as the snapshot/handoff/
receipt evidence carrier, and DEL-04-11 as their deterministic validator.

## Objective mappings

```diff
+ OBJ-001: add DEL-02-07..DEL-02-12
+ OBJ-002: add DEL-02-07..DEL-02-12
+ OBJ-003: add DEL-04-11
+ OBJ-004: add DEL-02-07..DEL-02-12
+ OBJ-007: add DEL-02-07..DEL-02-12
  OBJ-005 and OBJ-006: no change
```

Every new deliverable supports at least one objective and covers at least one
scope item. Every objective retains support; every IN scope item retains a
deliverable mapping.

## Forward trace, reverse trace, and telemetry — recomputed

| Surface | Before | Candidate |
|---|---:|---:|
| Forward PRD items | 85 | 85 |
| Forward covered / recorded deferral / uncovered | 84 / 1 / 0 | 84 / 1 / 0 |
| Reverse units | 52 (6 packages + 46 deliverables) | 59 (6 packages + 53 deliverables) |
| Reverse untraced | 0 | 0 |
| Context envelopes | S=14, M=31, L=1, XL=0 | S=14, M=38, L=1, XL=0 |
| Normative-basis category deliverables | 21 | 21 |
| Operative-product category deliverables | 19 | 25 |
| Developmental-machinery category deliverables | 25 | 26 |
| Evidence category deliverables | 17 | 24 |

The forward register adds the six runtime carriers to O-11 and OBJ-1/2/4/7,
and adds DEL-04-11 to D-7, E-2, and OBJ-3. The reverse register is fully
recomputed for all 59 units as the inverse of the candidate forward register
and scope ledger, with objective rows checked against candidate objective and
deliverable truth. This repairs inherited objective omissions for DEL-01-04,
DEL-03-01, DEL-03-06, and DEL-06-04 and recomputes package consequences,
including PKG-04 coverage of E-2. Counts for packages, scope items, and
objectives remain 6, 104, and 7.

## Derivative classification

| Surface | Classification | Candidate disposition |
|---|---|---|
| Working surface | `DIRECT_EDIT` | exact candidate copy; live file unchanged |
| Deliverable register | `DIRECT_EDIT` | DEL-02-06 modified; seven rows added |
| Scope ledger | `DIRECT_EDIT` | SOW-041, SOW-053, SOW-104 mapping cells and trace notes only |
| Objective register | `DIRECT_EDIT` | five mapped-deliverable cells updated |
| Forward trace | `RECOMPUTE` | 85-row synchronized candidate |
| Reverse trace | `RECOMPUTE` | 59-row synchronized candidate |
| Coverage telemetry | `RECOMPUTE` | projected topology and trace counts synchronized |
| `_LATEST.md` | `NO_CHANGE` | pointer change requires its own accepted authority |
| Live folders, SOWs, statuses, dependencies, estimates, schedules | `NO_CHANGE` | Gate-4 plan only; no materialization or lifecycle act |
| `WORK_GRAPH.json` / `DAG.md` | `NO_CHANGE` now | re-derive only after folders are live |

The Gate-4 `Amendment_Actions.csv` uses the exact current STRUCTURE schema:
nine columns and eight ordered actions. `SupersessionBindingPresent=NO` for
all eight because these are structural/allocation actions and no admitted-
authority fact is superseded on the present evidence.

## Exact candidate identity

| Candidate surface | SHA-256 |
|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` |
| `chirality_root_deliverable_register_v1_0.csv` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| `chirality_root_scope_ledger_v1_0.csv` | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` |
| `chirality_root_objective_register_v1_0.csv` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| `chirality_root_prd_coverage_forward_v1_0.csv` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| `chirality_root_trace_reverse_v1_0.csv` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| `chirality_root_coverage_telemetry_v1_0.md` | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` |

## Authority boundary and Gate-3 question

This preview applies nothing. Gate 5 is not open. The ten
`HELD_UNAVAILABLE` bindings, G0 A3/A4/A7 carriage, TM-ROOT-106/122 blockers,
C1 artifact-download prohibition, and App notice-only boundary remain
unchanged.

**Do you approve these exact amendments to the decomposition working surface
and six companion/trace/telemetry files?**
