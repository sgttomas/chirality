# Independent D85 ruling/publication verification

Verdict: **PASS**. The candidate faithfully records the owner's D85 P-A act
and is ready for bounded CHANGE publication. This verdict covers ruling and
publication fidelity only; it does not repeat the completed product review or
accept any product artifact.

## Authority and selection

The ruling, `OWNER_DIRECTION.md`, register row and Receipt 176 reproduce the
same owner sentence verbatim:

> I approve D85 P-A, the prepared production proposal, and starting that slice. Continue using the gpt-5.6-sol models as before.

The ruling selects the immutable V2 proposal SHA-256
`0da4d163c5d36fde15d7336256f412c1f31a6ac4e5d60c1d55c8e388c000541b`
and V2 output manifest SHA-256
`4f83533beadad4cdff56f061d50d34a556f4e54df12ffbe4da3218fd85321fd2`.
The current-selection hash
`e6b7fd693b0fee323314c4f64e64b4e143794a44c5dd8ed2f9d06d1298f6ab7e`
and completed-review manifest hash
`6bd963899a4cf670693950cda20f92c276df3a7eb725a394237befc6272abaa1`
also reproduce. The completed review verdict is
`PASS_FOR_RULING_PUBLICATION_AND_PROPOSAL_READINESS`, with IV-001 resolved and
zero open material findings. Historical pending-state wording remains in the
immutable preparation and is correctly identified as historical.

## Scope fidelity

The ruling enumerates exactly the proposal's nine product/configuration paths:

1. `v2/src/pec_v2/core/ports/store.py`
2. `v2/src/pec_v2/core/content_minimal_guard.py`
3. `v2/src/pec_v2/adapters/storage/__init__.py`
4. `v2/src/pec_v2/adapters/storage/sqlite_store.py`
5. `v2/tests/storage/test_store_lifecycle.py`
6. `v2/tests/storage/test_content_minimal_guard.py`
7. `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`
8. `.gitignore`
9. `software-workflow.json`

It incorporates the V2 acts and limits without enlarging them: seven new
source/test/doc paths, an additive ignore entry, and additive workflow check
and path-rule registration. The administrative grant is confined to
PKG-01 / DEL-01-03: `_run_records/P1_STORE_GUARD_01/**`, `MEMORY.md`, truthful
`_STATUS.md` maintenance, and bounded coordination activation/closeout.
`INITIALIZED -> IN_PROGRESS` occurs only when production actually starts and
must record the semantic-step skip, merged authority, actual date and history.
A differing observed pre-state is routed rather than overwritten.

The candidate grants exactly one later D85 production-closeout receipt. It is
Receipt 177 only if fresh discovery after Receipt 176 publication confirms 177
is next; otherwise it uses the then-next number. The clause preserves the full
published prefix and does not authorize a fixed-number overwrite or unrelated
ledger change.

The ruling and briefs consistently exclude `CHECKING`, `ISSUED`, artifact
acceptance, full DEL-01-03 or P1 completion, issuance, release, runtime
integration, and system kill/parity conclusions. They also preserve the
ScopeOfWork, dependency, decomposition, frozen-old-PEC, Root, sister-project,
registry, scanner and broader product boundaries.

## Sequencing and evidence boundaries

Production is expressly blocked until CHANGE publishes the ruling and its
single register-row successor and proves those exact bytes observable on
fetched `origin/main`. WORKING_ITEMS must then rerun current source, preimage,
dependency, and exact `dispatch-for-production` / `rely-for-production` hold
checks. The production graph requires one bounded TASK author followed by a
fresh read-only TASK verifier; verifier findings return to the author.

All later WORKING_ITEMS activation and production-closeout coordination is
routed to the separate sibling
`execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/**`. The ruling,
authorized-scope record, graph, WORKING_ITEMS brief and handoff agree that the
current D85 authority root freezes after its common seal. Across those author
surfaces, the only named future exclusion from the common authority manifest
is `D85_EXECUTION_2026-09-08/CHANGE_PUBLICATION/**`, reserved for CHANGE's
publication evidence. No second exclusion or production-write exception
inside the authority root is stated.

Runtime notices remain coordination evidence and import no PEC adoption,
account, daemon, credential, socket, user-data, or sister-loop authority. The
current hold register has zero data rows and reproduced its recorded SHA-256;
the verifier's exact ruling-target `candidate-validation` preflight returned
`ALLOW`. These facts support candidate review only and do not release
production before shared-main publication.

## Register, receipt and candidate checks

The fetched `origin/main` and HEAD are both
`55df51ac3201456e0f181823e3aefefef47a73bb`. The register preimage SHA-256
reproduces as `90611eb20c4f1acdb702d96eeab3af833eb073da2cd66b386f0839439a842606`.
Comparison with `origin/main` shows exactly one changed register row, D-PEC-85;
all other register lines are byte-equal.

The receipt preimage SHA-256 reproduces as
`efe77c70bb93984989a95d3d2f63fcabdd0182432f7e4df8b49b5458bdf15d14`.
The candidate begins with that complete byte prefix and appends only Receipt
176, whose parent is Receipt 175. The receipt validator exits 0. Receipt 176
is within the fixed 6-12-line guidance when its heading and nine fields are
counted as the receipt block, and it uses pointers plus bounded check/gate
summaries rather than becoming a substitute authority record.

The repository default candidate-whitespace validator with base
`origin/main` exits 0 and explicitly includes untracked candidate files. The
initial candidate contains only the D85 ruling, one register-row change,
Receipt 176, and the D85 coordination directory; no product, deliverable
status, MEMORY, or production-run file is changed.
