# N1-SCOPE-CHANGE-01 — Return

**Status:** `COMPLETE`
**Verdict:** `PASS`
**Authority effect:** `NONE`
**ReadyForNextPhase:** `NO`

## Output

| Artifact | SHA-256 | Bytes |
| --- | --- | ---: |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2b/K_CONTROL_1_REGENERATED_CONTRACT_ROW_CANDIDATE.md` | `cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8` | `8053` |

## Exact identities

| Identity | Value |
| --- | --- |
| Live App K-CONTROL-1 LF-terminated pre-row | `2f56b652642874f82c9580574bc88bb6ef0ec1c4e1a91ef4c291ea11da2894c5` |
| Regenerated K-CONTROL-1 LF-terminated post-row | `add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616` |
| Reconstructed Phase-2 full-contract control | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` (`34317` bytes) |
| Preliminary Phase2b full-contract candidate | `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9` (`34877` bytes) |

## Basis and semantic results

- Live App contract matched
  `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`;
  its K-CONTROL-1 pre-image occurs once at line 200.
- Ratified Root contract matched
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`.
- The prior Root contract
  `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`
  differs from the ratified contract at exactly line 162, K-CONTROL-1.
- Root K-RUNTIME-1 line 161 is byte-identical across the two contracts at
  LF-terminated row SHA-256
  `03985c419f2704e9529c3c9e4247f0dadb4ff47243ceafebd3ae1492dbd741f4`.
- Root K-STORE-2 line 164 is byte-identical across the two contracts at
  LF-terminated row SHA-256
  `ab84004cf36b4ba414c237170396b037744f29d44f1086f09969d4114ed98e09`.
- The other four A4-A Root blobs matched their steer pins.
- The post-image preserves the ratified two-socket design while stating
  exactly one socket is live today; the supervisor socket activates only
  through DEL-02-07/WP-03 and is never renderer- or CLI-callable.
- Root daemon ownership is explicit; the App is neither a second owner nor a
  writer of `{userData}/runtime` control state.
- All required App strengthenings, the no-peer-credential disclaimer, the
  no-third/no-TCP prohibition, and the live-versus-design-gated test split are
  present.

## Validation

```text
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

The validator ran against
`ef92fab10f40aa95da484701982d83fa1abca874` after the candidate was written
and before this hash-bearing return and `STATUS.json` were generated.

Independent reconstruction subsequently returned:

```text
N1 row LF SHA-256: add623f40502dbf71bd2b7023ae50cfe4f10a398a3f127ac308eac05b3cef616
reconstructed full SHA-256: 842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9
reconstructed full bytes: 34877
PASS: exact N1 reconstruction
```

`WORK_GRAPH.json` parses and `git diff --check` passes. All writes are within
the sealed N1 write set.

## N2 handoff

N2 may consume candidate artifact
`cf889103744df7fe4f20b85e9c8d4610a85af287cbfe60f0f6471a7bd642e3b8`.
Re-pin only the Phase-2 K-EVENT-4 Root-contract grounding from
`ed87eaff4…` to `ad0a4e6a…`. Preserve its LF-terminated resolved row exactly at
`92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93`
and preserve the other four Root blob pins. Stop if any resolved row byte
would change. N3 then independently reconstructs the preliminary full
contract at `842bf170…` before rebuilding the companion register.

No live target, existing snapshot file, N2/N3/N4 output, receipt, pointer,
register, frontend, docs, or Root-loop path was written.
