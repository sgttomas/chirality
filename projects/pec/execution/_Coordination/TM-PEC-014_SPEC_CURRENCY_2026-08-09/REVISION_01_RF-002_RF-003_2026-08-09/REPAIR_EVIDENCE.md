# DEL-00-03 RF-002/RF-003 repair evidence

**Status:** REPAIR CANDIDATES PRODUCED / REVIEW RERUN NOT STARTED
**Authority:** owner ruling, 2026-08-09: `REVIEW findings: REVISE all eight.
Authorize one bounded WORKING_ITEMS repair and PEER_REVIEW rerun confined to
the cited SOW/SPEC claims and regenerated review evidence; preserve lifecycle,
dependencies, source, and all unrelated content.`

## Inputs and successors

| Surface | Preimage SHA-256 | Successor SHA-256 |
|---|---|---|
| `ScopeOfWork.md` | `0e2cfad8fcb377381042fd63c7e73002ad93037bffd17b7a3b9eb58889469f54` | `3e4f0efc775849b11ae5bdfa851e0d3c125804db87d70f55aac9bc7c77e65741` |
| `artifacts/v2/SPEC.md` | `28de769a82945fc4b2586a36c89870c7e1f78dd1698fa6f028b30236014bd34c` | `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` |

Accepted upstream remains SOFTWARE_DECOMP revision 1.4 SHA-256
`7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`
and `ScopeLedger.csv` SHA-256
`2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25`.

## Exact repair scope

RF-002 changed only the six directly linked SOW statements:

- `CLM-011`: records OI-003 resolved at revision 1.4 and preserves the other
  issue dispositions.
- `REQ-007`: excludes resolved OI-003 from the decisions the SPEC must leave
  open and requires only the accepted resolution statement.
- `AC-008`: checks accepted OI-003 resolution plus preservation of remaining
  dispositions and TBD rows.
- `VER-006`: verifies those same accepted-decomposition facts.
- `AX-005`: distinguishes governed SCA-004 resolution from impermissible
  prose pre-decision.
- The `OUT-001 / REQ-007 / AC-008 / VER-006` matrix row now expects accepted
  OI-003 resolution and no ungoverned remaining movement.

RF-003 changed only two SPEC statements:

- §6: `71 IN / 14 OUT / 9 TBD` → `72 IN / 14 OUT / 8 TBD`.
- §8: `nine TBD scope rows` → `eight TBD scope rows`.

The already-correct §8 OI-003 paragraph remains unchanged from candidate
SHA-256 `28de769a...`.

## Regenerated review inputs

- Exact SOW-derived eleven-row checklist:
  `DEL-00-03_REVIEW_CHECKLIST.json`, SHA-256
  `1c4d492728e3e7a5c031bdb2a6f915e855916effa7cc1644f8bd7031b73ffbdb`.
- Additive owner custom focus:
  `OWNER_CUSTOM_CU-001.json`, SHA-256
  `36ec35f3869f02e935c21b62a767309c8763afbd97ff5f13e515da6e44507dc3`.

The generated checklist is not edited to embed CU-001; this preserves exact
byte-for-byte reproducibility from the successor SOW. REVIEW consumes both
files.

## Deterministic validation

| Check | Result |
|---|---|
| Reliance-hold production preflights for SOW and SPEC | `ALLOW` |
| SOW validator | `PASS`, `SOW_V1` |
| Checklist derivation and independent byte reproduction | `PASS`, 11 rows |
| CU-001 JSON syntax and exact successor binding | `PASS` |
| RF-002 stale OI-003 contract language absent; governed resolution present | `PASS` |
| RF-003 accepted counts `72 IN / 14 OUT / 8 TBD` present; stale counts absent | `PASS` |
| Strict decomposition registers | `PASS`, 64 registers / 255 rows / zero findings |
| DEL-00-03 dependency schema | `PASS`, 29 columns / 2 rows |
| PEC API contracts | `PASS`, 6/6 |
| PEC loop registry | `PASS`, 12/12 |
| PEC service-core posture | `PASS`, dependency/locality/registration |
| Root practitioner-harness self-check | exit `0`; inherited `REVIEW=4`, `WARN=31`, `INFO=14`, `NOT_APPLICABLE=1` |
| Scoped whitespace, product/evidence containment, and no staging | `PASS` |

## Preservation boundary

No lifecycle, dependency, source, historical review snapshot, review control,
finding, pointer, Task Management, receipt, plan, PRD, or unrelated product
content is changed by this repair. REVIEW remains the next owner and must rerun
separately as `PEER_REVIEW` against the two exact successor hashes and these
regenerated inputs.
