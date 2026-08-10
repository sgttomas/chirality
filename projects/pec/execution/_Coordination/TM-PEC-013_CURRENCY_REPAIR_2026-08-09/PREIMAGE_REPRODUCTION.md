# TM-PEC-013 preimage reproduction

**Recorded:** 2026-08-09

**Repository basis:** `d269f0e04204bc463a11684499213b2283bd28f7`

**Branch:** `codex/pec-currency-repair-20260809`

**Method:** `sha256sum` against the live checkout before any successor
`ScopeOfWork.md` edit.

| Deliverable | Preimage path | Reproduced SHA-256 | Handoff match |
|---|---|---|---|
| DEL-02-07 | `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` | `ddc837ca8b87ad8af52cfc4ec8b06c8fef883bbc3eeca9eea9949fb6280b007b` | PASS |
| DEL-03-01 | `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md` | `756c5f2af726272645a3cee491862cf3ca1fb751becad39f82ff310128d5ba19` | PASS |
| DEL-04-01 | `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` | `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f` | PASS |

## Accepted authority reproduction

| Authority surface | Reproduced SHA-256 | Handoff match |
|---|---|---|
| `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Handoff_State.md` | `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c` | PASS |
| `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Decision_Log.md` | `c377d7f094b46ede1b0ec8f108e7c52e61dada9565227820415b47301a87cd3c` | PASS |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` | PASS |

No target `ScopeOfWork.md` had been edited when these hashes were reproduced.
