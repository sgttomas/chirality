# Validation — Root TM-ROOT-112 accepted-repair closure

Status: `PASS`

## Deterministic checks

- Signed transcript SHA-256 `a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046`: match.
- Acceptance manifest SHA-256 `73ae77fe496731987ea49170fad45a9d1297bc263c5ba1d8050631da58efcea2`: match.
- Product hashes: SPEC `647eee2d…d6a7f`, daemon `22440300…ddf2`, tests `c853f207…b352`: match.
- Source notice SHA-256 `4f52ed53…0056`: match; closure evidence is not stale.
- Exact delta: only `TM-ROOT-112` moved from the live register to the archive; only `Status`, `Disposition`, `EvidenceRef`, `EvidenceSha`, `EvidenceQuote`, `LastReviewed`, `Closed`, and `Notes` differ from its live predecessor. Every other row is field-equivalent to `HEAD`.
- Live/archive validators: PASS at 23 live and 99 archived.
- Final federation: COMPLETE over four canonical registers, 71 findings, zero register writes; Root `OPEN=12`, `DEFERRED=11`.
- Foreign App, Piping, and PEC live registers: byte-equivalent to `HEAD`.
- Root Receipt 96 continuity: PASS.
- `git diff --check` and candidate-whitespace validation: PASS.

## Final identities

- Live register SHA-256: `d395a0e652dbe8fa4a165dd33efc06ccab61917dc69d3d9f3fc1925ee96d7d05`.
- Archive SHA-256: `b30f67f9aadf8c42ad527ecd6ac3d61f7cb280476abff28552117f84324a821c`.

## Closure echo

Root `TM-ROOT-112` is closed `RESOLVED_WITH_CHANGE`. The source App concern remains downstream state: Root closure releases, but does not itself ship, the ordinary App notice and makes no App/process/parity/merge claim.
