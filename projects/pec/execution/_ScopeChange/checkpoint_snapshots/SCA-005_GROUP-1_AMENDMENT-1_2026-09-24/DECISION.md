# SCA-005 checkpoint group 1 — amendment 1: TM-PEC-023 selections and cmux deferral

Recorded 2026-09-24 by HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`,
node G6) as a faithful transcription of two owner acts under K-AUTH-1. This
snapshot is additive: the accepted group-1 snapshot
`../SCA-005_GROUP-1_2026-09-24/` stays immutable, and this record amends the
accepted intake only where stated. Checkpoint-2 preparation consumes both.

## What the owner had in front of them

HELP_HUMAN's chat message explained that the nine TM-PEC-023 blanks are
leftovers of three separate events rather than a category, and that
infrastructure elsewhere in the decomposition is mapped to the objective
whose surface it directly makes possible. It also explained PEC-K-07. It then
gave one read per live row: row 3 OBJ-004; row 5 OBJ-003; row 6 OBJ-003,
"consistent with row 5"; row 1 OBJ-003 alone, as an owner replacement; row 8
OBJ-001 plus OBJ-003, as an owner replacement; row 2 OBJ-001; row 9 matching
row 2. It noted that any objective set not listed on the decision surface is
available as an owner replacement.

A later HELP_HUMAN message offered: "If you'd rather mark it deferred and out
of scope, as SCA-005 already does for the other presence items it defers,
that is one more action at checkpoint 2."

## The owner's acts (verbatim)

First act:

> Row 6 should not move with row 5 because row 6 is optional and I do not want it as an objective.  I don't need cmux compatibility anytime soon (no plans for it).  Besides that, I reviewed and accept your  read for each mapping.

Second act, answering the offer above:

> yes add cmux to what's been deferred and out of scope.

## HELP_HUMAN's interpretation (interpretation, not owner text)

### TM-PEC-023 selections

Surface: `execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/DECISION_SURFACE.md`,
SHA-256 `3a61a24db9a0c5019302588831e5245e5c9436ef03b9e4595ea70615941071ef`.
The owner's 2026-08-03 reservation, "every selection is mine to make in
that session", is satisfied by these acts.

| Row | Deliverable / scope items | Selected `ObjectiveIDs` = `SupportsObjectives` | Surface option | Authority effect |
|---|---|---|---|---|
| 1 | DEL-00-02 / SOW-034 | `OBJ-003` | OWNER REPLACEMENT (the surface offered `OBJ-001;OBJ-003` or NONMAP, and noted that an `OBJ-003`-only option was intentionally not offered) | owner ruling is the mapping authority; supersedes the §3 "intentionally not force-mapped" abstention for SOW-034 |
| 2 | DEL-03-05 / SOW-038 | `OBJ-001` | MAP-A (`INDIRECT_SUPERSESSION_CANDIDATE`) | owner ruling is the mapping authority; supersedes the same abstention for SOW-038 |
| 3 | DEL-05-01 / SOW-022, SOW-023 | `OBJ-004` on both scope items and the deliverable | MAP-A (`DIRECT_ACCEPTED_LINK`) | carries the accepted link into the blank registers |
| 4 | DEL-07-02 / SOW-035 | none | moot | retired under R1 at checkpoint 1; leaves the union invariant |
| 5 | DEL-07-03 / SOW-036 | `OBJ-003` | MAP-A (`INDIRECT_SUPERSESSION_CANDIDATE`) | owner ruling is the mapping authority; supersedes the abstention for SOW-036 |
| 6 | DEL-07-04 / SOW-037 | none | moot by the second act | the owner declined an objective ("I do not want it as an objective"); the second act defers SOW-037 OUT and retires DEL-07-04, so no mapping or typed non-mapping is recorded |
| 7 | DEL-07-05 / SOW-087 | none | moot | retired under R1 at checkpoint 1 |
| 8 | DEL-08-05 / SOW-044 | `OBJ-001;OBJ-003` | OWNER REPLACEMENT (the surface offered `OBJ-003`, `OBJ-001;OBJ-003;OBJ-004` or NONMAP) | owner ruling is the mapping authority for this out-of-wave row |
| 9 | DEL-10-08 / SOW-063 | `OBJ-001` | OWNER REPLACEMENT (the surface offered `OBJ-001;OBJ-003` or NONMAP) | owner ruling is the new mapping authority and expressly supersedes DL-14's objective-free rationale for SOW-063 (surface authority A3) |

Because no live row selects a typed non-mapping, the surface's session-wide
rulings 1 (recording mechanic for NONMAP rows) and 2 (objective-side table
form for non-mappings) have no subject and are moot. Rulings 3–5 (amendment
ID, exact postimage and propagation plan, execution) are SCA-005's checkpoints
2 and 3.

### cmux deferral

The second act adds to the accepted intake, in the form checkpoint 1
already accepted for the other deferrals (R1: `OUT` with a bold `**Deferred**`
note; non-destructive retirement at Gate 5). The exact rows are in
`Amendment_Actions_Addendum.csv`:

- **New Seq 77, MODIFY SOW-037:** status IN to OUT, `**Deferred**`, with no
  trigger other than a later owner direction; PKG-07 / DEL-07-04 lineage
  cleared; TM-PEC-023 row 6 disposed by this status change, not by a mapping.
- **New Seq 78, REMOVE DEL-07-04:** retire non-destructively under R1, the
  same mechanics as DEL-07-02 and DEL-07-05. It is `OPEN`. No surviving
  register row targets it; its outgoing DEP-07-04-003 (to DEL-00-02) and
  DEP-07-04-004 (to DEL-07-01) retire with its register, and the consumer
  mirrors in DEL-00-02 and DEL-07-01 `_DEPENDENCIES.md` are refreshed.
- **Seq 43 (PKG-07 charter) narrowed:** the cmux bridge is deferred with the
  daemon bridge and the runtime seam; assigned scope items become SOW-033,
  SOW-036 and SOW-039.
- **Seq 68 (row 6 carry-in) dropped:** moot under Seq 77/78.
- **Seq 75 (PRD successor candidate) extended:** PEC-STR-003 and the §12 P4
  row stop naming the cmux adapter as a supported bridge and record it as
  deferred.

Consequences checkpoint 2 must carry: active deliverables drop by one more
(DEL-07-04 joins DEL-06-04, DEL-07-02 and DEL-07-05 as retired); the
`ContextBudgetQA.csv` row retires; accepted artifacts that mention cmux (the
DEL-00-01 ADRs, the DEL-00-03 SPEC seed, the DEL-01-03 SOW) are listed for
stale review, not rewritten by the amendment.

## Impact delta against the accepted group-1 evidence

The accepted `Impact_Assessment.md` and `Amendment_Actions.csv` stay
byte-unchanged. Under the contract's affected-decision rule, these accepted
statements are superseded by this amendment and checkpoint 2 must carry the
new values:

| Accepted statement | Accepted value | Value after amendment 1 |
|---|---|---|
| IA §5 IN / OUT / TBD after change | 71 / 17 / 8 | 70 / 18 / 8 (SOW-037 IN to OUT Deferred) |
| IA §5 deliverable rows, active / RETIRED | 66 (63 / 3) | 66 (62 / 4) (DEL-07-04 retired) |
| IA §5 PKG-02 / PKG-06 / PKG-07 assigned scope | 9 / 6 / 4 | 9 / 6 / 3 |
| IA §5 IN rows without objective mapping | 9 before selection | 1 after selection: SOW-033, whose deliverable DEL-07-01 already carries `OBJ-003` through SOW-039, so the union invariant holds |
| IA §5 active deliverables without SupportsObjectives | 7 before selection | 0 after selection |
| IA §5 active context envelopes | S 28 / M 33 / L 2 | S 28 / M 32 / L 2 (DEL-07-04 was M) |
| IA §5 execution edges before new edges | 110 | 108 (DEP-07-04-003/004 retire with DEL-07-04's register) |
| IA "PKG-07 keeps 3 active children" (two places) and Seq 35 "keeps 3 active children" | 3 | 2 (DEL-07-01, DEL-07-03) |
| IA INV-020 row, PEC-STR-003 | "Daemon bridge deferred; hooks/cmux stay" | daemon and cmux bridges deferred; hooks CLI stays |
| Seq 24, §1.2 streams bullet | daemon SSE bridge deferred | daemon SSE and cmux bridges deferred |
| Seq 32 / 39 / 41, "hooks CLI and adapters" | adapters remain | the hooks CLI is the only remaining bridge; wording follows |
| Seq 60 / Seq 62 objective views and IA "3 objective views" | OBJ-001 and OBJ-003 views list the pre-selection sets; OBJ-004 has no view action | the OBJ-001 view gains DEL-03-05, DEL-08-05, DEL-10-08; the OBJ-003 view gains DEL-00-02, DEL-07-03, DEL-08-05; the OBJ-004 view gains DEL-05-01 and needs its own view action |
| Every IA count of the retired set (IA §1 summary, "SOW-029/035/087 leave IN", "3 retirement annotations", "three retired deliverables'", the §8.1 edge trace) | three scope items / three deliverables; 8 EXECUTION rows owned by retired registers, 119 − 8 − 1 = 110 | four scope items (adds SOW-037) / four deliverables (adds DEL-07-04); 10 EXECUTION rows, 119 − 10 − 1 = 108 |
| Action mix | 8 ADD / 65 MODIFY / 3 REMOVE | 8 ADD / 64 MODIFY / 4 REMOVE (+Seq 77, +Seq 78, −Seq 68, −Seq 72) |
| `SOFTWARE_DECOMP.md` runtime-surfaces bullet "external-process bridges (daemon SSE, cmux)" | no accepted action covers it | checkpoint 2 adds the wording change for both deferred bridges |

The single SOW-033 residue is not a TM-PEC-023 row and is not selected here;
checkpoint 2 reports it for the owner.

## Boundary

This record selects the TM-PEC-023 dispositions above and adds the cmux
deferral to the intake. It applies no decomposition, register, PRD, SOW,
`_CONTEXT.md`, `_STATUS.md`, `v2/**` or foreign change, moves no active
pointer, and closes no Task Management row: TM-PEC-023 closes
`RESOLVED_BY_DECISION` only after the SCA-005 amendment applies. The exact
postimage remains subject to checkpoint 2 and the audited poststate to
checkpoint 3.
