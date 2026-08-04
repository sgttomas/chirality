# Existing-schema mechanics proposal for typed non-mapping

**Status:** `PROPOSAL ONLY / OWNER SELECTION REQUIRED`
**Constraint:** no decomposition-schema change is pre-authorized.

## Existing field semantics

The accepted SOFTWARE decomposition has these relevant existing surfaces:

| Surface | Existing semantics | Constraint |
|---|---|---|
| `ScopeLedger.csv.ObjectiveIDs` | semicolon-separated objective IDs for one scope item | mapped values must be bare `OBJ-NNN` tokens |
| `Deliverables.csv.SupportsObjectives` | union of the objective IDs of the deliverable's covered IN scope items | typed non-objective tokens would corrupt the objective set |
| `ScopeLedger.csv.DecisionRef` | prior decision/amendment reference(s) for the row | must preserve existing `DL-11` / `DL-12` lineage where present |
| `ScopeLedger.csv.Notes` | row-local explanatory metadata | can hold a typed disposition without changing columns |
| `SOFTWARE_DECOMP.md` §3 Mapping notes | canonical narrative explanation of mapping and abstention semantics | can hold an exact keyed table without changing register schemas |
| SCA `Decision_Log.md` and immutable snapshot | accepted owner act and evidence | created only after all five SCOPE_CHANGE gates |

The current deterministic register validator enforces propagation from
`ObjectiveIDs` to `SupportsObjectives`; it treats blank objective fields as an
empty set. It does not define non-objective tokens in either field. Therefore
`SupportsObjectives=INVARIANT_EVIDENCE_OBJECTIVE_FREE` (or any similar token)
is not a lawful no-schema-change mechanic.

## Mechanic M1 — keyed mapping-notes disposition table

**Recommended default when the owner selects NONMAP.**

1. Leave `ScopeLedger.ObjectiveIDs` and
   `Deliverables.SupportsObjectives` empty.
2. Add an exact table under `SOFTWARE_DECOMP.md` §3 Mapping notes:

```markdown
| DeliverableID | ScopeItemIDs | NonMappingDisposition | Rationale | DecisionRef |
|---|---|---|---|---|
| DEL-NN-NN | SOW-NNN[;...] | TYPE_TOKEN | exact owner-ruled rationale | SCA-NNN/D-NNN |
```

3. Record the same exact selection in the SCA `Decision_Log.md` and
   `Amendment_Actions.csv`, and include the accepted table in the immutable
   SCA snapshot.
4. Change the coverage/audit rule so it resolves an empty objective field as
   `TYPED_NON_MAPPING` only when one exact keyed accepted row exists; absence,
   duplication, or a stale decision reference remains an open finding.

Any such consumer change is not implicitly authorized by selecting M1. The
future SCOPE_CHANGE Gate 4 propagation plan must name the exact audit/validator
consumer files, owner, write authority, validation, and sequencing. If no
consumer change is authorized, the handoff must leave that rerun/change as an
explicit open downstream obligation.

Benefits: deliverable-level identity, human-readable rationale, no pollution
of objective-ID fields, and a direct place to distinguish typed non-mapping
from an untyped blank. Cost: audit consumers must parse a canonical markdown
table or a snapshot evidence table.

## Mechanic M2 — ScopeLedger `Notes` annotation plus §3 index

**Recommended when machine-readable row locality is important.**

1. Leave both objective fields empty.
2. Append, without deleting existing notes, this exact grammar to each covered
   scope-item `Notes` cell:

```text
NonMappingDisposition=<TYPE_TOKEN>;NonMappingDecision=<SCA-NNN/D-NNN>
```

3. Preserve prior `DecisionRef` lineage. The future Gate 3 preview must choose
   whether to append the new decision reference to `DecisionRef` or keep it
   solely in the new Notes grammar; it must not overwrite `DL-11` or `DL-12`.
4. Add the M1 §3 table as a deliverable-level index, especially for
   `DEL-05-01`, whose one deliverable covers two scope rows.
5. Teach the audit to require exact agreement between the Notes annotations
   and the §3 table.

Benefits: disposition is co-located with each authoritative scope-item row.
Cost: it introduces a new grammar inside an existing free-text field and
requires an exact validator rule even though it adds no CSV column.

## Mechanic M3 — SCA snapshot and §3 table only

Leave both CSV registers byte-unchanged and use the M1 §3 keyed table plus the
immutable SCA decision package. This is schema-safe but less machine-local than
M2. It is suitable if the owner declines any CSV annotation.

## Rejected mechanic — objective-field annotation

Do not write a type token, bracketed prose, sentinel such as `NONE`, or
qualified objective such as `OBJ-003(indirect)` into `ObjectiveIDs` or
`SupportsObjectives`. Those fields are sets of objective IDs. Such a value
would either invent an objective, break bare-token consumers, or make the
union invariant ambiguous. Using it would be a schema change, which the owner
has not authorized.

## Proposed type vocabulary

The vocabulary below is candidate text, not an adopted enum:

| Type token | Intended use |
|---|---|
| `SHARED_INFRASTRUCTURE_INDIRECT_ONLY` | a contract/infrastructure unit that enables objective-bearing consumers but is not itself attributed |
| `INVARIANT_GUARANTEE_NO_DIRECT_OBJECTIVE` | a behavior guarantee enforcing an invariant absent from the objective layer |
| `ADVISORY_GATE_CAPABILITY_NO_DIRECT_OUTCOME` | an advisory evaluator whose consumer view carries the outcome attribution |
| `SHARED_BRIDGE_INFRASTRUCTURE_INDIRECT_ONLY` | a declared input bridge with attribution retained at the derived consumer |
| `OPTIONAL_ENRICHER_NO_DIRECT_OBJECTIVE` | an optional contributor whose absence changes no objective contract |
| `SHARED_RUNTIME_SEAM_INDIRECT_ONLY` | an integration seam without a direct accepted objective link |
| `TRANSPORT_CAPABILITY_INDIRECT_ONLY` | an API transport attributed only through its consumers |
| `INVARIANT_EVIDENCE_OBJECTIVE_FREE` | evidence of an invariant intentionally outside the objective layer |

The dedicated owner session may rename or consolidate these tokens. Doing so
changes candidate text, not schema, provided the selected mechanic records the
exact type and rationale consistently.

## Required future validation

After a future owner-ruling and Gate 5 execution:

- validate all objective tokens as bare `OBJ-NNN`;
- validate deliverable objective sets equal the union of covered IN scope
  rows;
- validate each blank objective set has exactly one accepted typed
  disposition or remains an open finding;
- validate §3 objective-side mapped lists against both registers;
- validate COV-062..COV-070 retire only against the accepted successor
  snapshot, not this preparation package; and
- verify every audit/validator consumer change named at Gate 4 was executed by
  its authorized owner or remains explicitly open; and
- regenerate deliverable-local `_CONTEXT.md` mirrors through PROJECT_SETUP
  only after SCOPE_CHANGE emits the accepted successor handoff.
