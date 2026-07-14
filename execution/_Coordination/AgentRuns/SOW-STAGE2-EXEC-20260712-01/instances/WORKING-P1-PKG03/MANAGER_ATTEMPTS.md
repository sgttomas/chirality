# Manager Attempts

| Attempt | Layer | Class | Reason code | Disposition |
|---:|---|---|---|---|
| 1 | manager fan-in | execution substrate | `FINALIZATION_SCHEMA_KEY_GUESS` | Failed before candidate mutation; inspected registered `chirality-sow-finalization/v1` keys, corrected the deterministic reader, and reran the full package. |

The attempt did not write project paths or alter any candidate. Native manager
token/context occupancy is unavailable and is not inferred.
