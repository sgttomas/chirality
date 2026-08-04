# Validation — Root Task Management ruling application

Status: `PASS`

## Deterministic checks

- Ruling transcript SHA-256:
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`
  — match.
- Derivative application-map SHA-256:
  `87ccfdbe4cf2fb89adc275b330c958c0810973096c8a6749448f3bb8bbef12a5`
  — match.
- Mandatory preflight: `COMPLETE`, 4 canonical registers, 71 findings,
  zero register writes, no excluded lookalikes or unresolved errors.
- Live-register validator: `PASS`, 24 rows.
- Closed-archive validator: `PASS`, 98 rows.
- Final federation: `COMPLETE`, 4 canonical registers, 71 findings, zero
  register writes.
- Register delta validator: `PASS`; only `TM-ROOT-105`, `TM-ROOT-109`, and
  `TM-ROOT-121` moved from live to archive with owner-ruled closure fields.
- `TM-ROOT-112`: `OPEN` and row-equivalent to the pre-run `HEAD` basis.
- Pre-existing live and archived rows: field-equivalent to the pre-run basis.
- Mandatory closure-note phrases and separate carrier IDs: present.
- Foreign App, Piping, and PEC live registers: byte-equivalent to `HEAD`.
- `git diff --check`: `PASS`.

## Final identities

| Artifact | SHA-256 |
|---|---|
| `execution/_Coordination/_TaskManagement/REGISTER.csv` | `c0b61ca5c6ddab44c8ea782997d5f1108e2ee7959d546220284a02c2ce0a3dbe` |
| `execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv` | `abeb1d1f4f588218a246bee6b4d7ebe04d9bf84f39fcdf3b9fe2e779e86e490c` |
| `execution/_Coordination/NOTICE_2026-08-03_ROOT_TM-ROOT-105_109_SUBSTANTIVE_RULINGS.md` | `123c3a0f54ce3d03ba3cee67e6724faf659d54e2c8dda80d264d79d98e8ea40e` |

## Final counts

- Root live: 24 (`OPEN=13`, `DEFERRED=11`, `ELEVATED=0`, `CLOSED=0`).
- Root archive: 98 (`CLOSED=98`).
- Program federation: PEC 17/3 plus 1 live CLOSED and 4 archived; App
  12/3 and 25 archived; Piping 8/26 and 3 archived; Root 13/11 and 98
  archived.

## Closure echo and staleness

All newly recorded closure evidence hashes match the authoritative ruling
bytes. App `TM-APP-027/028` remain correctly unfired because no contract bytes
were ruled. Piping `TM-PIP-032` now has actual ruling evidence for its own
next trigger evaluation; no foreign-row effect was applied. Federation
finding-class counts are unchanged from preflight.

