# DEL-02-08 App Server 0.149.0 Supply-Unit Candidate

**State:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

**N4 result:** `PASS_WITH_DOCUMENTED_GAPS`

**Basis:** `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`

**Correction return:** PR #673 was returned by the owner for deterministic
evidence correction. No new vendor execution was authorized or performed.
The corrected packet records nine complete per-run gates and one unavailable
`version`-run gate record. Dependent candidate and review hashes are
regenerated from the corrected bytes.

This immutable run packet assembles exact-source, exact-supply, equivalence,
license, signature, configuration, feature, containment, egress, and drift
evidence for the macOS arm64 App Server 0.149.0 supply unit. It is a derivative
candidate under the accepted DEL-02-08 Scope of Work, not accepted supply
truth and not a pin amendment.

## Packet map

| Path | Purpose |
| --- | --- |
| `01_SOURCE_IDENTIFICATION/` | Official release and current-document identities |
| `02_SUPPLY_INVENTORY_PRIMARY/` | Primary artifact, signature, license, and redistribution inventory |
| `02B_EQUIVALENCE/` | Three-packaging identity and ancillary-executable inventory |
| `03_EMPIRICAL_EVIDENCE/` | Contained exact-pin readback, feature, egress, and gap evidence |
| `SUPPLY_MANIFEST.json` | Consolidated exact supply identity |
| `SUPPLY_UNIT_CANDIDATE.md` | Owner-readable candidate synthesis |
| `CONFIG_METHOD_FEATURE_MATRIX.md` | Exact-pin configuration, method, and 118-feature result |
| `SCHEMA_TYPES_METHOD_INDEX.md` | Produced evidence and bounded gaps |
| `OUT-002_ENDPOINT_INVENTORY.md` | Observed destination inventory and downstream policy handoff |
| `G2_ACCEPTANCE_SHEET.md` | Exact owner decision surface |
| `EVIDENCE_HASH_MANIFEST.csv` | Stable evidence-chain identities |
| `04_REVIEW/` | Fresh N4 review and hash backcheck |

## Governing boundary

No file in this packet records G2 acceptance, changes a pin, disposes the G5
signature finding, authorizes implementation or cutover, lifts a blocker or
hold, establishes release/publication/reliance, or adopts an App-side policy.
TM-ROOT-106 and TM-ROOT-122 remain G1 blockers. All ten existing DEL-02-06
bindings remain held and unchanged.
