# DEL-06-06 — reverse-pass notes (pass 2)

## Scope

Capability files answered, in this order: BUILD, ELECTRON, HARNESS, RTCONTRACT, RTCORE, SHELL. That
is 284 capability rows.

Responses:

| Response | Rows |
|---|---:|
| CLAIMED_BY | 0 |
| PARTIAL | 17 |
| NOT_MINE | 267 |

## Why none are CLAIMED_BY

DEL-06-06 is a mirroring slice. Every capability it touches is also carried by an owner package:

- PKG-05: event log, vocabulary, replay and artifacts;
- PKG-03: delegated adapter, supervisor, terminal and turn coordination;
- DEL-06-04: path hooks;
- DEL-09-02: Section 9 runner.

For that reason each touched capability is answered `PARTIAL` with the covering forward key.

## Errata

No errata file. The capability notes agree with the sealed forward rows:

- CAP-HARNESS-038 and CAP-HARNESS-047 are `LEGACY_ONLY`/`DISABLED`.
- CAP-RTCORE-025 and CAP-RTCORE-029 are `LIVE` and preserve upstream Codex method names and payloads.
- The da95ec194 lines named in CAP-RTCORE-029 (526, 535-544, 570-573) are not among the lines the
  forward ledger relied on (546, 584-600, 705-733), so PostReleaseBasis `NO` stands.

Census: the sealed and errata-applied figures are identical (see `DEL-06-06_notes.md` §1).

## Coverage gaps

No capability shows a missing forward row. One point for the manager: CAP-RTCONTRACT-036 has no
dedicated forward row. It matters here only for the descriptor's `compaction` flag, which is noted
under CLM-010.7.

## Validation

- `validate_ledger.py reverse` passes once per capability file (6 runs): 0 errors, 0 warnings each.
- The claims SHA-256 is unchanged:
  `f00395edccefb57330a2c36275fe6f0fdba500e4eec783cbf7c0a91a9616d641`.
