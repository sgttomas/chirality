# N2-SCOPE-CHANGE-01 — Return

**Status:** `COMPLETE`
**Verdict:** `PASS`
**Authority effect:** `NONE`
**ReadyForNextPhase:** `NO`

## Output

| Artifact | SHA-256 | Bytes |
| --- | --- | ---: |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2b/K_EVENT_4_REPINNED_CONTRACT_ROW_CANDIDATE.md` | `c6b6d31497f0399c319b9b1772964b5c003ca1b520289cd7238d14efd84ba463` | `8386` |

N1 was consumed only at candidate artifact SHA-256
`cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`.

## Re-grounding result

- Root `docs/CONTRACT.md` moved from A4-A's
  `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`
  to ratified
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`.
- The two Root contract blobs differ only at line 162, K-CONTROL-1.
- K-RUNTIME-1 line 161 is byte-identical at LF-terminated SHA-256
  `03985c419f2704e9529c3c9e4247f0dadb4ff47243ceafebd3ae1492dbd741f4`.
- K-STORE-2 line 164 is byte-identical at LF-terminated SHA-256
  `ab84004cf36b4ba414c237170396b037744f29d44f1086f09969d4114ed98e09`.
- The other four A4-A source blobs remain exactly at
  `40cec2df…`, `fe81bc9a…`, `d20fd7dc…`, and `22e49ccf…`.
- No carry-forward caveat remains: the new artifact is grounded directly in
  the ratified Root contract.

## Exact row identity proof

| Identity | Phase-2 value | Phase-2b value | Result |
| --- | --- | --- | --- |
| Live K-EVENT-4 pre-row, LF-terminated | `f172b56078f83dcc48019ff0fea3c867f96c3d79ab5143fa9bb668d6937fab2a` | `f172b56078f83dcc48019ff0fea3c867f96c3d79ab5143fa9bb668d6937fab2a` | `BYTE_IDENTICAL` |
| Resolved K-EVENT-4 post-row, LF-terminated | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` | `BYTE_IDENTICAL` |
| Phase-2 full resolved contract relationship | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`, `34317` bytes | preserved as historical reconstruction control | `PRESERVED` |

The exact resolved row required no byte change. N2 therefore completed rather
than taking the fail-closed stop path. N2 did not compute any N3 output.

## Artifact byte-delta accounting

Compared with immutable Phase-2 transaction artifact
`779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`:

| Measure | Phase 2 | Phase 2b | Delta |
| --- | ---: | ---: | ---: |
| Bytes | `6431` | `8386` | `+1955` |
| Lines | `93` | `141` | `+48` |
| Line diff (`--numstat`) | — | — | `65` added / `17` removed |

Byte-level sequence accounting reports `5936` unchanged subsequence bytes,
`495` Phase-2 nonmatching bytes, and `2450` Phase-2b nonmatching bytes. The
artifact-level delta consists of Phase-2b state/boundary metadata, explicit
A6-B re-grounding evidence and proofs, and the N3 handoff. It does not alter
the exact PRE-IMAGE or POST-IMAGE row bytes.

## Validation

```text
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

The validator ran against
`ef92fab10f40aa95da484701982d83fa1abca874` after the candidate was written
and before this hash-bearing return and `STATUS.json` were generated.

`git diff --check` passed. All writes are within the sealed N2 write set.

## N3 handoff

N3 may consume:

- N1 K-CONTROL-1 artifact
  `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`;
- N2 K-EVENT-4 artifact
  `c6b6d31497f0399c319b9b1772964b5c003ca1b520289cd7238d14efd84ba463`;
- N2 resolved K-EVENT-4 LF row
  `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`.

N3 must independently reconstruct the Phase-2 control image
`a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`
at `34317` bytes, then substitute N1's regenerated C-01 while retaining N2's
byte-identical C-06 row, and only then rebuild the companion-register
candidate. N2 makes no assertion about the resulting N3 identities.

No live target, existing snapshot file, shared run file, N1/N3/N4 output,
receipt, pointer, register, frontend, docs, or Root-loop path was written.
