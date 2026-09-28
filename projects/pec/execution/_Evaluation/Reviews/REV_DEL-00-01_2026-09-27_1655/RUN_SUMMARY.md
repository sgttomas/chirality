# Run summary — DEL-00-01 exact-byte re-acceptance (`REV_DEL-00-01_2026-09-27_1655`)

REVIEW reproduced DEL-00-01 `artifacts/v2/ADRs.md` SHA-256
`ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` and
`ScopeOfWork.md` SHA-256
`3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647`. Both PEC
`promote` preflights returned `ALLOW`; both hashes exactly match the bytes the
owner re-accepted on 2026-09-27 ("ACC: option 1; accept all findings as is;
re-accept DEL-00-01 and DEL-00-03 exact bytes; retire CU-001").

The ADRs and contract are recorded as accepted current DEL-00-01 artifacts;
this is the contract's first owner acceptance. AC-007 is satisfied for these
bytes. RF-001..RF-005 are `ACCEPT_AS_IS / RESOLVED` as known limitations;
RF-001 stays `MAJOR` and AC-002 is accepted as partly met. Zero findings are
open and none is deferred. Gate 5 remains unentered and `_STATUS.md` remains
`CHECKING`; there is no C-05 act.
