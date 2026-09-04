# Work Graph — APPDEV_V3_NODE_M_2026-09-04

**Basis:** `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f`

**Selection authority:** HUMAN — Ryan Tufts

**Execution class:** `delegated-harness-native`

**Role calibration:** every Agent-2 role is `role not mechanically enforced`;
governed-workflow role evidence is `instruction-asserted`.

**K-SUBAGENT calibration:** non-delegation is instruction+config asserted,
not mechanism-proven; no descendants were observed.

| Node | Role and boundary | Depends on | Status / return |
|---|---|---|---|
| `M1_IMPLEMENTER` | Instructed bounded ephemeral Agent-2 mode; role not mechanically enforced; writes only the declared Node M set | owner authorization and accepted basis | Initial candidate and deterministic evidence; freeze `f8522fcfcc74e0dd4363afa06d5d2ccf6fcac34c` |
| `M2_REVIEWER` | Instructed fresh read-only ephemeral Agent-2 reviewer mode; role not mechanically enforced; 100% basis-to-freeze review; external report only | `M1_IMPLEMENTER` | FAIL, three MAJOR; immutable report SHA-256 `089204ef41625fa08a1eee915df08686be9e66f8b84ebb9d1390ae6a1025caf4` |
| `M1_REMEDIATION_R1` | Same bounded M1; accepts/dispositions M2 findings; no scope expansion | `M2_REVIEWER` | Remediation freeze `4fa170341700e491dff8c72ce1229ba84735f073` |
| `M3_REVIEWER` | Instructed new fresh read-only ephemeral Agent-2 reviewer mode; role not mechanically enforced; 100% basis-to-remediation review; external report only | `M1_REMEDIATION_R1` | FAIL, two MAJOR; immutable report SHA-256 `66f61ef9cf9c4d433f19d6959b8b546768116c4eb67e3de97d9836347454e8e4` |
| `M1_REMEDIATION_R2` | Same bounded M1; makes V3-04's closure contract nonce-only and completes truthful orchestration evidence | `M3_REVIEWER` | `REVIEW_READY_R3`; freeze is the Git commit returned after these records are finalized |
| `M4_REVIEWER` | Instructed fresh read-only ephemeral Agent-2 reviewer mode; role not mechanically enforced; 100% basis-to-round-3-freeze review | `M1_REMEDIATION_R2` | FAIL, one MAJOR; immutable report SHA-256 `2c5ceb0c930f566b9f375d2f8f8b1f62b9123f55e175a438d37fcf9e160a8802` |
| `M1_REMEDIATION_R3` | Same bounded M1; calibrates native-descendant role and non-delegation evidence | `M4_REVIEWER` | `REVIEW_READY_R4`; freeze is the Git commit returned after these records are finalized |
| `M5_REVIEWER` | Instructed fresh read-only ephemeral Agent-2 reviewer mode; role not mechanically enforced; 100% basis-to-round-4-freeze review | `M1_REMEDIATION_R3` | FAIL, one MAJOR; immutable report SHA-256 `ceb24881cf877fce9771c2b7dc9c820c8d34aed9d079f42ec6cee0f9392fd47a` |
| `M1_REMEDIATION_R4` | Same bounded M1; corrects every mutable current-round, report-count, and handoff pointer | `M5_REVIEWER` | `REVIEW_READY_R5`; freeze is the Git commit returned after these records are finalized |
| `M6_REVIEWER` | Instructed fresh read-only ephemeral Agent-2 reviewer mode; role not mechanically enforced; 100% basis-to-round-5-freeze review | `M1_REMEDIATION_R4` | FAIL, one MAJOR; immutable report SHA-256 `08fb5bfc74abd294b47284fc5ebf836ee1b21ffb2051d30b81ff6db54234c88b` |
| `M1_REMEDIATION_R5` | Same bounded M1; calibrates the mutable A15 execution-attribution sentence and advances current pointers | `M6_REVIEWER` | `REVIEW_READY_R6`; freeze is the Git commit returned after these records are finalized |
| `M7_REVIEWER` | Fresh read-only descendant instructed for Agent-2 reviewer mode; role not mechanically enforced; 100% basis-to-round-6-freeze review | `M1_REMEDIATION_R5` | PASS over `52d220ec44486bd62923aea1ecd2bfab02c693d2`; no BLOCKER, MAJOR, or MINOR findings; two NOTES; immutable report SHA-256 `dc96448da18b81b1a3af333b63ade6eb6f6baa35e4453f9f2dcd7bf53bddb2c0` |
| `M1_NARRATIVE_CLOSEOUT` | Same bounded M1; files immutable R6 report and calibrated M7 records, records NOTES as residual context, appends Receipt 223, and prepares PR handoff; no substantive byte | `M7_REVIEWER` | CLOSEOUT_READY; owner PR merge remains the gate |

Edges:

`M1_IMPLEMENTER → M2_REVIEWER → M1_REMEDIATION_R1 → M3_REVIEWER → M1_REMEDIATION_R2 → M4_REVIEWER → M1_REMEDIATION_R3 → M5_REVIEWER → M1_REMEDIATION_R4 → M6_REVIEWER → M1_REMEDIATION_R5 → M7_REVIEWER → M1_NARRATIVE_CLOSEOUT`

The M2 launch/status/return metadata is a source-calibrated reconstruction,
not a verbatim prompt claim. M3's launch metadata is an accurate structured
record of the actual dispatch, not a byte-verbatim prompt claim. The filed
immutable reviewer reports are contemporaneous and authoritative for their
respective reviews. M4, M5, M6, and M7 launch metadata are source-calibrated
structured reconstructions of their actual dispatches, not byte-verbatim
prompt claims; creation of the M7 records was directly authorized by the
owner after the immutable PASS report existed. All actual nodes used the `delegated-harness-native`
execution class.
Governed-role evidence is `instruction-asserted`; Agent-2 roles were not
mechanically enforced. K-SUBAGENT/non-delegation is instruction+config
asserted, not mechanism-proven, and no descendants were observed. The R6
handoff is spent history; M7 returned PASS, and its immutable report plus the
final narrative-only closeout are now filed without changing ruling or
deliverable bytes.
