# C2A-R1 Exact-Authority Behavior Matrix

Accepted authority: `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`.

| Dual-format condition | Resolution | Valid | Selected production documents | Evidence |
|---|---|---:|---|---|
| accepted authority + exact binding + isolated + exact path + valid SOW + complete legacy | `MIGRATION_DUAL` | yes | `ScopeOfWork.md` | positive scanner regression |
| unruled valid-looking `D-GOV-16@0123456` | `AMBIGUOUS` | no | none | negative scanner regression |
| whitespace-padded accepted authority | `AMBIGUOUS` | no | none | reviewer-found negative scanner regression |
| malformed authority | `AMBIGUOUS` | no | none | negative scanner regression |
| missing authority | `AMBIGUOUS` | no | none | negative scanner regression |
| accepted authority but non-isolated | `AMBIGUOUS` | no | none | negative scanner regression |
| accepted authority but wrong deliverable path | `AMBIGUOUS` | no | none | negative scanner regression |
| accepted supplied authority but unruled candidate binding | `AMBIGUOUS` | no | none | mismatch scanner regression |
| invalid SOW | `INVALID` | no | none | structural scanner regression |
| partial legacy coexistence | `INVALID` | no | none | partial-kit scanner regression |
| misleading requested format | resolved fail-closed state + mismatch error | no | none | mismatch scanner regression |

SOW-only remains `SOW_V1`; legacy-only remains `LEGACY_FOUR_DOC`. The repair
does not touch route, DocumentView, DOMAIN/KTY, control-plane, lifecycle, or
deliverable files.
