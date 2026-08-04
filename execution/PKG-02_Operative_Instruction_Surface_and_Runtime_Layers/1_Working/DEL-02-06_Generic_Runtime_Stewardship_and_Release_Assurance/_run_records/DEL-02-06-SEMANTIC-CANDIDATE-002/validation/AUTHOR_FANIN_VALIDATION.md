# AUTHOR fan-in validation

- Node: `AUTHOR`
- Attempt accepted: `2`
- Manager verdict: `ACCEPTED_FOR_FRESH_REFUTATION`
- Author return SHA-256:
  `9ee6195bd1d7464be5d8f5b4cc60aa40064cb3c2122060b14313beaf0c257e32`

## Retry disposition

Attempt 1 emitted no candidate bytes and stopped on the manager-transcribed
owner-selection-matrix hash mismatch. `briefs/BRIEF_AMENDMENT_1.md` corrected
the single identity to the value reproduced by the live matrix, signed
package manifest, and decision-support acceptance record. Attempt 2 reproduced
all 14 source identities before writing.

## Accepted exact candidate set

| File | SHA-256 |
|---|---|
| `candidate/AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` | `6578357f894cb30243764b512593ab2b1856675b0ac34d2cac513b235320061e` |
| `candidate/DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V1.md` | `60522ec49032c15b62aab86405b113eac5e46d08dca1054af759313e05843b5f` |
| `candidate/EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V1.md` | `00fb1b716efcd61fb9a4fefd4438c9406f17c0938ae9113cfef5bcf574af8480` |
| `candidate/OWNER_DECISION_RECORD_CANDIDATE_V1.md` | `64882a27df256f85b5c105b691805a3f4fa208995e920b7792cfc9b8cf004ecb` |
| `candidate/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` | `5b4aff46f32432e816bcebe39984758b86d81b7f9321153d73b2de5adde0f7c4` |
| `candidate/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` | `798cebc5175d8b07c95d0bd3af390c7466b94fc7e33102ee350e0b84b1f864ba` |
| `application_trace/SELECTION_APPLICATION_TRACE.md` | `bf9a17b87f273e974deaed805029f42e16a1bc6817f0e48e862e08b01ea896f1` |

## Deterministic checks

- Exact ordered selection equals the signed 27-token tuple: `PASS`.
- Trace contains 27 unique numbered mappings: `PASS`.
- Owner record contains 27 selected/unselected rows and all 27 unselected IDs:
  `PASS`.
- Candidate membership is exactly six planned files: `PASS`.
- Census tuple is exact allowed member 1: `PASS`.
- No `root-runtime-[0-9]+` minted epoch appears: `PASS`.
- Exact future-owner epoch placeholder is present: `PASS`.
- N3 remains `DESIGN_COMPLETE_NOT_EXECUTED`: `PASS`.
- App ownership, PEC `UNRESOLVED`, Piping `NOT_AFFECTED`, Tier-0
  preparation-only, conditional compatibility delta, and separate
  implementation gate are explicit: `PASS`.
- Author hashes reproduce exactly: `PASS`.
- Author write containment: `PASS`.

The author return is accepted only as input to independent refutation. No
candidate byte is adopted, and no implementation or foreign-owner effect is
authorized.
