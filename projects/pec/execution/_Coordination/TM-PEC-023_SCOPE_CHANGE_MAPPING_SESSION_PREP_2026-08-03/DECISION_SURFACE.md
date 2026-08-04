# TM-PEC-023 dedicated SCOPE_CHANGE mapping-session decision surface

**Status:** `PREPARED / AWAITING_DEDICATED_OWNER_SESSION`
**Authority posture:** candidate decision support only; every checkbox is
owner-only and presently unselected.
**Current basis:** accepted PEC SOFTWARE_DECOMP revision 1.4 (`SCA-004`), with
`ScopeLedger.csv` SHA-256
`2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25`
and `Deliverables.csv` SHA-256
`49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72`.

## How to rule

For each row, the owner selects exactly one disposition in the dedicated
session:

- a mapping option, which supplies the exact `ObjectiveIDs` /
  `SupportsObjectives` token set; or
- the typed non-mapping option, which keeps those two objective fields empty
  but replaces the untyped semantic blank with an explicit keyed disposition
  and rationale using one of the mechanics in `SCHEMA_MECHANICS_PROPOSAL.md`;
  or
- owner-authored replacement text.

No option is selected by this preparation package. A mapping is not valid
merely because it appears below. A future SCOPE_CHANGE cycle must still pass
its five gates, apply the owner-selected exact text, create an immutable
snapshot, and validate the union invariant:

```text
Deliverables.SupportsObjectives
  = union(ScopeLedger.ObjectiveIDs for all covered IN scope items)
```

`DEL-10-01` is the accepted multi-objective precedent: `SOW-058` and
`DEL-10-01` both carry `OBJ-001;OBJ-006`, and its accepted ScopeOfWork records
that the attribution belongs to register truth rather than a downstream
invention. Multi-objective syntax is therefore the existing semicolon-separated
bare-token form, not a schema extension.

### Mapping-option authority model

Every mapping option carries exactly one `AuthorityStatus`:

| AuthorityStatus | Meaning |
|---|---|
| `DIRECT_ACCEPTED_LINK` | accepted sources already establish the exact scope-item/deliverable → objective relation; the future SCA carries that link into the blank registers |
| `INDIRECT_SUPERSESSION_CANDIDATE` | accepted sources support the surrounding function or indirect-contributor rationale but do **not** establish the exact objective relation; if selected, the future owner ruling becomes the mapping authority and expressly supersedes the prior abstention/rationale |
| `NEW_OWNER_ATTRIBUTION` | accepted sources supply context but do **not** identify the proposed objective relation; if selected, the future owner ruling is the new mapping authority and supersedes any incompatible prior abstention/rationale |

Only `DIRECT_ACCEPTED_LINK` may be described as a direct accepted mapping.
Indirect and new options are decision candidates, not evidence that the
mapping already governs.

## Authority key

| Ref | Accepted authority |
|---|---|
| A1 | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` §3 Objectives: exact statements and source refs for `OBJ-001`..`OBJ-006` |
| A2 | Same §3 historical mapping rationale: `SOW-033..039` serve `OBJ-001`/`OBJ-003` freshness indirectly through PEC-K-07 and were intentionally not force-mapped. It supplies supersession context only: the current owner ruling declines the "accepted residue" framing prospectively and leaves every selection open |
| A3 | Same document, DL-14: `SOW-063` is intentionally objective-free because it instruments PEC-K-07, which no §3 objective states directly |
| A4 | Same document, DL-17 and revision 1.2 history: SCA-002 mapped only the Phase 2.2 wave and left 11 rows unselected; it explains history but does not decide their present disposition |
| A5 | `projects/pec/docs/PRD.md` §3 outcomes 1–5 and §11 falsification outcome, from which `OBJ-001`..`OBJ-006` are derived |
| A6 | Same PRD §6, PEC-K-07: streams optimize freshness but reconciliation over file truth guarantees every record-tier fact |
| A7 | Same PRD §9.3, `PEC-GAT-001/-002`: deterministic file/Git-reducible gate checks and Explain-shaped advisory verdicts |
| A8 | Same PRD §9.5, `PEC-STR-002/-003/-004`: versioned event contracts, the three declared bridges, and reconciliation supremacy after stream loss |
| A9 | Same PRD §9.6, `PEC-API-005`: SSE subscription for deltas and presence changes for dashboards / long-running managers |
| A10 | Same PRD §13 plus `D-PEC-56_shared_runtime_agent_migration.md`: the shared-runtime client-seam concept carries to v2 entities while the one-loop and human-only-act boundaries survive |
| A11 | `ScopeLedger.csv` and `Deliverables.csv` exact rows named in each block; these registers are authoritative for assignments |
| A12 | SCA-002 `Decision_Log.md` finding F-3 and its `SOW-038` note: ingest/bridge mapping is an abstention that a later mapping must expressly supersede, and `SOW-038` is reconciliation-side despite the loose §3 class label |

## Class I — out-of-wave at SCA-002

The class label describes why SCA-002 did not decide the row. It is not itself
a final mapping or a final typed non-mapping disposition.

### Row 1 — DEL-00-02 / SOW-034

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-00-02` — Event-contract schema v1 |
| Scope item | `SOW-034` — versioned event contract types consumable by daemon, hooks CLI, and adapters |
| SourceRef | `PEC-STR-002` |
| Current `ObjectiveIDs` | empty string |
| Current `SupportsObjectives` | empty string |
| Residue basis | out-of-wave at SCA-002; also inside §3's `SOW-033..039` ingest/bridge rationale |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact token set to
  `SOW-034.ObjectiveIDs` and `DEL-00-02.SupportsObjectives`. Context/rationale: A1,
  A2, A5, A8, A11. A2 supports the indirect class rationale but does not
  establish this exact relation. If selected, the future owner ruling is the
  mapping authority and supersedes A2's prior no-force-map abstention.
- [ ] **NONMAP — `SHARED_INFRASTRUCTURE_INDIRECT_ONLY`.** Keep both objective
  fields empty. Record: "Versioned cross-consumer event-contract
  infrastructure enables objective-bearing bridges but does not itself
  achieve a §3 product outcome; attribution remains with the objective-bearing
  consumers." Authority: A8, A11; prior deferral: A4.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: MAP-A is available only as an indirect supersession
candidate. An `OBJ-003`-only MAP-B is intentionally not offered: the
session/status/scope detail belongs to `SOW-036`, not `SOW-034`. NONMAP is the
source-faithful alternative if the owner rejects indirect attribution.

### Row 2 — DEL-03-05 / SOW-038

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-03-05` — Stream-loss recovery guarantee |
| Scope item | `SOW-038` — recover stream loss by reconciliation; no record-tier fact rests on a stream event alone |
| SourceRef | `PEC-STR-004` |
| Current `ObjectiveIDs` | empty string |
| Current `SupportsObjectives` | empty string |
| Residue basis | out-of-wave at SCA-002; reconciliation-side guarantee grouped loosely with `SOW-033..039` |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-001`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact token to both objective
  fields. Context/rationale: A1, A5, A6, A8, A11, A12. The sources support the
  protective reconciliation rationale but do not establish this exact
  objective relation. If selected, the future owner ruling is the mapping
  authority and supersedes the prior abstention.
- [ ] **MAP-B — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact set to both fields.
  Context/rationale: A1, A2, A5, A6, A8, A11, A12. The sources support the indirect
  freshness context but do not establish the exact pair. If selected, the
  future owner ruling supplies the mapping authority and supersedes A2's
  abstention plus the loose-class rationale.
- [ ] **NONMAP — `INVARIANT_GUARANTEE_NO_DIRECT_OBJECTIVE`.** Keep both fields
  empty. Record: "This deliverable enforces PEC-K-07's record-tier truth
  invariant across stream loss. It protects objective-bearing consumers but
  does not directly instantiate a §3 objective." Authority: A6, A8, A11,
  A12; prior deferral: A4.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: NONMAP is the strongest source-faithful option
because PEC-K-07 is an invariant, not one of the six objectives. Both mapping
options require an owner-created indirect attribution and express
supersession.

### Row 3 — DEL-05-01 / SOW-022 + SOW-023

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-05-01` — Gate precondition evaluators (Explain-shaped) |
| Scope items | `SOW-022` (`PEC-GAT-001`); `SOW-023` (`PEC-GAT-002`) |
| Current `ObjectiveIDs` | empty string on both scope-item rows |
| Current `SupportsObjectives` | empty string |
| Residue basis | out-of-wave at SCA-002 |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-004`.** **AuthorityStatus: `DIRECT_ACCEPTED_LINK`.** Add `OBJ-004` to each of
  `SOW-022.ObjectiveIDs` and `SOW-023.ObjectiveIDs`, and to
  `DEL-05-01.SupportsObjectives`. Authority: A1, A5, A7, A11. Objective 4
  expressly names gates and decisions in the owner's one live view; these
  rows compute its cited advisory gate state.
- [ ] **NONMAP — `ADVISORY_GATE_CAPABILITY_NO_DIRECT_OUTCOME`.** Keep all
  three objective fields empty. Record: "Explain-shaped gate evaluation is a
  reusable advisory capability; the one-live-view objective is achieved by
  the decision-slate/dashboard consumers rather than by this evaluator
  alone." Authority: A7, A11; prior deferral: A4.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: MAP-A is the only direct accepted link in this
package because the exact objective statement names gates and decisions and
the two PRD rows define their deterministic advisory evaluation.

### Row 8 — DEL-08-05 / SOW-044

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-08-05` — SSE delta/presence subscription |
| Scope item | `SOW-044` — SSE subscription for deltas and presence changes |
| SourceRef | `PEC-API-005` |
| Current `ObjectiveIDs` | empty string |
| Current `SupportsObjectives` | empty string |
| Residue basis | out-of-wave at SCA-002 |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact token to both objective
  fields. Context/rationale: A1, A5, A9, A11. The sources establish a presence-change
  transport context, not the exact objective relation. If selected, the
  future owner ruling supplies the mapping authority and supersedes the prior
  unruled blank/deferral rationale.
- [ ] **MAP-B — `OBJ-001;OBJ-003;OBJ-004`.** **AuthorityStatus:
  `NEW_OWNER_ATTRIBUTION`.** Add this exact set to both fields. Context/rationale:
  A1, A5, A9, A11. The accepted source names deltas, presence changes,
  dashboards, and long-running managers but does not establish this three-way
  objective set. If selected, the future owner ruling is the new mapping
  authority; this option must not be represented as accepted-source fact.
- [ ] **NONMAP — `TRANSPORT_CAPABILITY_INDIRECT_ONLY`.** Keep both fields
  empty. Record: "The SSE subscription transports objective-bearing deltas
  and presence changes but does not itself create the underlying orientation,
  presence registry, or owner view." Authority: A9, A11; prior deferral: A4.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: MAP-A is an indirect transport-contributor
candidate. MAP-B is a new owner attribution inferred across consumers, not an
accepted link. NONMAP remains source-faithful if transport is left
unattributed.

## Class II — shared ingest/bridge infrastructure

### Row 4 — DEL-07-02 / SOW-035

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-07-02` — Daemon SSE subscriber bridge |
| Scope item / SourceRef | `SOW-035` / `PEC-STR-003` |
| Current `ObjectiveIDs` / `SupportsObjectives` | empty string / empty string |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact set to both fields.
  Context/rationale: A1, A2, A5, A8, A11. The sources support a daemon-feed freshness
  context but do not establish this exact objective pair. If selected, the
  future owner ruling supplies the mapping authority and supersedes A2's
  abstention.
- [ ] **MAP-B — `OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact token to both fields.
  Context/rationale: A1, A5, A8, A11. The sources support an indirect presence-input
  rationale but do not establish the exact relation. If selected, the future
  owner ruling is the mapping authority and supersedes the prior abstention.
- [ ] **NONMAP — `SHARED_BRIDGE_INFRASTRUCTURE_INDIRECT_ONLY`.** Keep both
  fields empty. Record: "The attributable daemon subscriber is a freshness
  input; reconciliation and presence consumers, not the bridge itself,
  achieve the objectives." Authority: A6, A8, A11.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: both mappings are indirect contributor candidates;
neither is a direct accepted relation. MAP-B is narrower but still needs the
future owner ruling as authority.

### Row 5 — DEL-07-03 / SOW-036

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-07-03` — Hooks CLI bridge |
| Scope item / SourceRef | `SOW-036` / `PEC-STR-003` |
| Current `ObjectiveIDs` / `SupportsObjectives` | empty string / empty string |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact token to both fields.
  Context/rationale: A1, A5, A8, A11. The source identifies session/status/scope event
  inputs, but it does not establish that this bridge supplies the full durable
  registry or collision surface or the exact objective relation. If selected,
  the future owner ruling is the mapping authority and supersedes the prior
  abstention.
- [ ] **MAP-B — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact set to both fields.
  Context/rationale: A1, A2, A5, A8, A11. A2 supports indirect freshness context, not
  this exact pair. If selected, the future owner ruling supplies authority and
  supersedes the prior abstention.
- [ ] **NONMAP — `SHARED_BRIDGE_INFRASTRUCTURE_INDIRECT_ONLY`.** Keep both
  fields empty. Record: "The bridge reports source events but does not itself
  own the durable presence registry, collision derivation, or orientation
  query." Authority: A8, A11.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: MAP-A is the tighter indirect-contributor candidate;
it is not an accepted direct relation.

### Row 6 — DEL-07-04 / SOW-037

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-07-04` — cmux socket adapter (optional) |
| Scope item / SourceRef | `SOW-037` / `PEC-STR-003` |
| Current `ObjectiveIDs` / `SupportsObjectives` | empty string / empty string |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact token to both fields.
  Context/rationale: A1, A5, A8, A11. The source supports optional-enricher context,
  not the exact objective relation. If selected, the future owner ruling is
  the mapping authority and supersedes the prior abstention; graceful absence
  is not itself grounds for `OBJ-005`.
- [ ] **MAP-B — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `INDIRECT_SUPERSESSION_CANDIDATE`.** Add this exact set to both fields.
  Context/rationale: A1, A2, A5, A8, A11. A2 supports the indirect class rationale,
  not the exact pair. If selected, the future owner ruling supplies authority
  and supersedes the abstention.
- [ ] **NONMAP — `OPTIONAL_ENRICHER_NO_DIRECT_OBJECTIVE`.** Keep both fields
  empty. Record: "This optional enricher improves an objective-bearing
  presence feed but its absence changes no objective contract." Authority:
  A8, A11.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: both mapping options require owner-created indirect
attribution. NONMAP is the source-faithful option if optional enrichers are
not mapped.

### Row 7 — DEL-07-05 / SOW-087

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-07-05` — Shared-runtime client seam (v2) |
| Scope item / SourceRef | `SOW-087` / `§13, D-PEC-56` |
| Current `ObjectiveIDs` / `SupportsObjectives` | empty string / empty string |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-003`.** **AuthorityStatus:
  `NEW_OWNER_ATTRIBUTION`.** Add this exact token to both fields. Context/rationale:
  A1, A5, A10, A11. Accepted sources establish that the seam concept carries
  into v2 and preserve its runtime boundary, but they do not identify an
  objective relation. If selected, the future owner ruling is the new mapping
  authority.
- [ ] **MAP-B — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `NEW_OWNER_ATTRIBUTION`.** Add this exact set to both fields. Context: A1,
  A5, A10, A11 and the owner's class framing in
  `OWNER_RULINGS_2026-08-03.md`. None establishes this exact pair. If
  selected, the future owner ruling is the new mapping authority and
  supersedes any incompatible prior abstention/rationale.
- [ ] **NONMAP — `SHARED_RUNTIME_SEAM_INDIRECT_ONLY`.** Keep both fields
  empty. Record: "The carried client-seam concept is an integration boundary,
  not a stated product outcome; objective attribution remains with the v2
  services and bridges using it." Authority: A10, A11.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: the accepted sources specify that the seam carries,
but not which §3 outcome it serves. NONMAP is the source-faithful alternative;
both mapping options would be new owner attributions.

## Class III — invariant evidence intentionally objective-free

### Row 9 — DEL-10-08 / SOW-063

| Field | Exact current value |
|---|---|
| Deliverable | `DEL-10-08` — Stream-loss recovery demonstration |
| Scope item | `SOW-063` — demonstrate stream-loss recovery by reconciliation |
| SourceRef | `§12 P4` |
| Current `ObjectiveIDs` | empty string |
| Current `SupportsObjectives` | empty string |
| Accepted rationale | DL-14: intentionally unmapped; instruments PEC-K-07, which no §3 objective directly states |

Candidate dispositions:

- [ ] **MAP-A — `OBJ-001;OBJ-003`.** **AuthorityStatus:
  `NEW_OWNER_ATTRIBUTION`.** Add this exact set to both objective fields.
  Context: A1, A5, A6, A8, A11. Those sources explain the invariant and the
  surrounding outcomes but do not establish this exact mapping. If selected,
  the future owner ruling is the new mapping authority and expressly
  supersedes A3/DL-14's accepted objective-free rationale.
- [ ] **NONMAP — `INVARIANT_EVIDENCE_OBJECTIVE_FREE`.** Keep both fields
  empty. Record: "This P4 exit test evidences PEC-K-07's reconciliation-over-
  stream invariant. No §3 objective states that invariant directly; the test
  is intentionally objective-free rather than missing attribution."
  Authority: A3, A6, A8, A11.
- [ ] **OWNER REPLACEMENT:** `____________________________________________`

Non-binding calibration: NONMAP is the source-faithful recommendation because
it converts DL-14's accepted prose rationale into a typed per-row disposition
without pretending PEC-K-07 is an objective. MAP-A remains available only as
an explicit new owner attribution and supersession of A3/DL-14.

## Session-wide owner rulings required after the nine rows

The dedicated session must also select:

1. one existing-schema recording mechanic from
   `SCHEMA_MECHANICS_PROPOSAL.md` for every selected NONMAP row;
2. whether the §3 objective-side table lists only mapped rows and a separate
   keyed typed-nonmapping table, or includes a textual cross-reference from
   each affected objective note;
3. the exact SCA amendment ID after scanning `_ScopeChange/` at session start;
4. the exact Gate 3 postimage and Gate 4 propagation plan; and
5. the Gate 5 execution/acceptance act after validation.

Until those rulings occur, all nine values remain byte-identical, TM-PEC-023
and COV-062..COV-070 remain open, no SCA is opened, and no downstream work is
gated.
