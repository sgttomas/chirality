# Decomposition Coverage Report — SCA003_S3_POST_APPLY

## Verdict

`BLOCKER`. Structural coverage passes and prior `COV-001` is closed, but the
applied live decomposition contains a new current-state acceptance/application
contradiction.

## Check verdicts

| Check | Verdict | Evidence |
|---|---|---|
| 1 — Forward packages | `PASS` | 6/6 Root; scoped 3/3. |
| 2 — Forward deliverables | `PASS` | 46/46 Root; 20/20 package context; 4/4 targets. |
| 3 — Reverse folders | `PASS` | No reverse-only package or deliverable. |
| 4 — ID consistency | `PASS` | All checked folder/register IDs agree. |
| 5 — Context fidelity | `PASS` | Target contexts 4/4 `MATCH`. |
| 6 — Artifact/contract | `PASS` with 14 `INFO` | 4/4 valid `SOW_V1`; 0/14 accepted production outputs at `INITIALIZED`. |
| 7 — Objective mapping | `PASS` | All seven register aggregates agree; target mappings complete. |
| 8 — Ledger integrity | `PASS` | 104/104 parse; zero unresolved refs; scoped 39 rows/41 refs valid. |
| 9 — Derivative parity | `SKIPPED` | Not variant-owned for SOFTWARE. |
| 9b — Package shape | `PASS` | Explicit working-surface/companion inventory; no derived authority confusion. |
| 10 — Snapshot/handoff consistency | `BLOCKER` | Prior SCA-002 mismatch closed; new SCA-003 pending-vs-applied mismatch present. |
| 11 — Lifecycle | `PASS` (informational) | Four targets `INITIALIZED`. |

## Prior finding disposition

Prior `COV-001` is **CLOSED**. The live decomposition at SHA-256
`69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`
now states revision 1.2 is the accepted current basis (lines 1 and 13), cites
the exact SCA-002 acceptance token/application/Git lineage (lines 14–20), pins
REF-001 to live PRD SHA-256
`d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`
(line 67), preserves DEC-023 as proposal history (line 563), adds DEC-024
(line 565), and agrees with unchanged `_LATEST.md` SHA-256
`b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.

## New blocker COV-POST-001

**Severity: `BLOCKER`.** Three live current-facing statements say the SCA-003
basis reconciliation remains pending exact owner acceptance/application:

- line 11: the header says it “remains pending exact owner acceptance and application”;
- line 565: DEC-024 says its candidate effect remains pending those acts;
- lines 622–623: the current change-log entry repeats that the metadata bytes remain pending those acts.

Current evidence proves both acts occurred. Owner ruling SHA-256
`12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`
contains exact acceptance and application authorization. `S3_Applied_File_Hashes.json`
SHA-256 `f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8`
records `APPLIED_PENDING_HUMAN_POST_CHANGE_CONFIRMATION` and exact candidate
parity. `S3_Applied_Validation.json` SHA-256
`18e00b070e7eb889043688531ed4dfcdeca2f168b4e031ba2dfe86761fd08c61`
records 17/17 PASS. Human post-change confirmation remains pending; exact
acceptance and application do not.

## Cleaner rerun

Through a governed amendment or an owner-authorized current-disposition append,
make the three current-facing statements distinguish completed exact
acceptance/application from pending human post-change confirmation. Preserve
DEC-023 and immutable candidate history. Rerun this check afterward.
