# INSP-01a Status Writer Preflight Evidence

**Date:** 2026-06-20
**Tranche:** `INSP-01a` Normalize preflight
**Prepared by:** WORKING_ITEMS
**Status:** BLOCKER FOUND - do not run `INSP-01` until resolved
**Dry-run SHA input:** `77d7233ff02bcfbb5b691797ef5b04ca097bce43`

This artifact records the read-only preflight over all deliverable `_STATUS.md` files before the
planned `IN_PROGRESS -> CHECKING` inspection-entry transition. The SHA above was used only as a
valid formatter input; it is not recorded here as the owner-blessed `approvalSha` for `INSP-01`.

## Command Shape

Because this checkout did not have `frontend/node_modules/` installed, Vitest could not be run
directly. The preflight used a read-only Node stdin script that mirrored the small parser/writer
logic from:

- `frontend/src/lib/lifecycle/status-parser.ts`
- `frontend/src/lib/lifecycle/status-writer.ts`
- `frontend/src/lib/lifecycle/transition.ts`

The script enumerated canonical deliverable folders by reading
`execution/PKG-*/1_Working/DEL-*`, parsed each `_STATUS.md`, normalized it through the writer shape,
then applied an in-memory `CHECKING` transition with actor `HUMAN`, date `2026-06-20`, and the
planned metadata fields:

- `Authorization Basis: D-APP-19 Option D ruling 2026-06-20`
- `Directive: owner inspection-phase directive 2026-06-20`
- `Checking Approval SHA: <dry-run SHA input>`

No project files were written by the preflight.

## Results

| Check | Result |
|---|---:|
| Deliverables enumerated | 53 |
| Parsed successfully | 53 |
| Current state `IN_PROGRESS` | 53 |
| Transition would add required fields in all files | yes |
| Files changed by normalization before transition | 53 |
| Files with unparsed history bullets that would be dropped | 52 |
| Total unparsed history bullets | 52 |

Normalization-loss patterns:

| Pattern | Count |
|---|---:|
| `removed4_added2` | 18 |
| `removed2_added0` | 1 |
| `removed3_added1` | 32 |
| `removed3_added2` | 1 |
| `removed4_added1` | 1 |

The preflight therefore does **not** satisfy the `INSP-01a` acceptance condition
"Predicted diffs = normalization + row + fields only." The current writer would discard historical
prose in 52 status files before adding the expected `CHECKING` row and fields.

## Affected Deliverables

The only deliverable with no unparsed history bullet was:

- `DEL-05-04` -
  `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/DEL-05-04_Runtime_Replay_and_Transcript_View/_STATUS.md`

Affected deliverables:

`DEL-00-01`, `DEL-00-02`, `DEL-01-01`, `DEL-01-02`, `DEL-01-03`, `DEL-01-04`, `DEL-02-01`,
`DEL-02-02`, `DEL-02-03`, `DEL-02-04`, `DEL-02-05`, `DEL-03-01`, `DEL-03-02`, `DEL-03-03`,
`DEL-03-04`, `DEL-04-01`, `DEL-04-02`, `DEL-04-03`, `DEL-04-04`, `DEL-04-05`, `DEL-05-01`,
`DEL-05-02`, `DEL-05-03`, `DEL-05-05`, `DEL-06-01`, `DEL-06-02`, `DEL-06-03`, `DEL-06-04`,
`DEL-06-05`, `DEL-06-06`, `DEL-07-01`, `DEL-07-02`, `DEL-07-03`, `DEL-07-04`, `DEL-07-05`,
`DEL-07-06`, `DEL-08-01`, `DEL-08-02`, `DEL-08-03`, `DEL-08-04`, `DEL-08-05`, `DEL-09-01`,
`DEL-09-02`, `DEL-09-03`, `DEL-09-04`, `DEL-09-05`, `DEL-09-06`, `DEL-10-01`, `DEL-10-02`,
`DEL-10-03`, `DEL-10-04`, `DEL-10-05`.

## Sample Dropped Bullets

- `DEL-00-01`: `- 2026-05-24 - State reset to OPEN (TASK / direct ORCHESTRATOR-authored SEMANTIC_READY entry invalidated as provisional because it lacked independent TASK evidence; semantic readiness pending TASK pipeline regeneration)`
- `DEL-01-01`: `- 2026-05-20 - Semantic matrix generated and validated by TASK + semantic-matrix-build; Current State intentionally remains INITIALIZED per Phase 2.3 override reserving SEMANTIC_READY for after lensing and P3 enrichment.`
- `DEL-02-01`: `- 2026-05-20 - Semantic matrix lens generated and validator passed; Current State intentionally kept INITIALIZED for Phase 2.3 per ORCHESTRATOR override reserving SEMANTIC_READY for post-lensing/P3 enrichment (TASK + semantic-matrix-build)`

## Blocker

`INSP-01` must not run yet. A live status transition would preserve the parsed lifecycle state and
would add the required `CHECKING` fields, but it would also drop noncanonical history prose. That is
a substantive history-loss risk under the `INSP-01a` preflight gate.

Prepared decision packet:

- `execution/_Coordination/_DECISIONS/D-APP-33_PACKET_2026-06-20.md`

Optional decision-support preview for D-APP-33 Option B:

- `plans/artifacts/insp01a_option_b_canonicalization_preview_2026-06-20.md`
