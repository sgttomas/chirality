# DEL-01-06 RF-002 revision/acceptance session — preparation manifest

**Status:** `PREPARED / EXECUTION_SEPARATELY_SCHEDULED`

## Authority and basis

- Branch/base: `codex/pec-sca004-metadata-alignment-20260803` at
  `1c6ecc6d97b4dcaf68927f3ecfba981dc7a155ff`.
- Owner ruling record:
  `projects/pec/execution/_Coordination/TM-PEC-023_SCOPE_CHANGE_MAPPING_SESSION_PREP_2026-08-03/OWNER_RULINGS_2026-08-03.md`,
  SHA-256 `579230cf7ed303f7722b88e0ac9abff2b768c3a5e5a7d475092c3407a0327f64`.
- Adopted effect: `RF-002 = REVISE_ADOPTED / EXECUTION_SEPARATELY_SCHEDULED`.
  RF-002 remains `HumanDisposition=TBD / Status=OPEN` until exact revised-SOW
  acceptance. Gate 5 HOLD and lifecycle `INITIALIZED` remain unchanged.

## Bound preimages

| Surface | SHA-256 |
|---|---|
| DEL-01-06 `ScopeOfWork.md` | `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a` |
| DEL-01-06 `_REVIEW.md` | `5967c12f57bd8815ccf59b8f66ac68015777c209a855e9f51a789d63258b9e95` |
| DEL-01-06 `Review_Findings.csv` | `a5e15e978e970bf76ce8497bd622ee41d73334366aeae9716c7424de96130a32` |
| DEL-01-06 `_STATUS.md` | `20e6db0216943cf93d734cf97a18c50ece47706e6a012e47580aea9745e5e90d` |
| `SOFTWARE_DECOMP.md` revision 1.4 | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` |
| SCA-004 `Handoff_State.md` | `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c` |

## Preparation write set

| Act | Path | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|
| UPDATE_MAP | `projects/pec/README.md` | `42fd5fd9480b899db1b864f02630fbfb8545b0d3ce1f3c9cd35d03281ad9b536` | `aa3812867804e6ae40717240d8ceec26da7998e24bb39ae39214f8e52d25c066` |
| UPDATE_MAP | `projects/pec/docs/STATUS.md` | `27b74f5e95665ca897c244e890f4feb85ae2c0eda23683ce2298bc7c0cfd5c72` | `deb64a8817e82639195425876bc5a96c6e62632931701c109e8aa7cc3c13ac1a` |
| UPDATE_MAP | `projects/pec/execution/_Coordination/_COORDINATION.md` | `3686360344f2927b6f8f8ea58867c2cbfe848f8c50dc7679c782e8852ebc4fbb` | `c477f0836b71e9352b9c8e6ad5db909a89adbd76c5c5a1aff520f520935abf2a` |
| UPDATE_MAP | `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | `fbf6d66bc2948f8ea53ed06eea434edd1e62891ba0920345524c512a0e925986` | `0be130ce5ee6bcf9ac54ef81c594eb6528fd66225f1334585a640e8145f4c207` |
| CREATE_PREP | `projects/pec/execution/_Coordination/DEL-01-06_RF002_REVISION_ACCEPTANCE_SESSION_PREP_2026-08-03/MANIFEST.md` | absent | self-referential |
| CREATE_PREP | `projects/pec/execution/_Coordination/DEL-01-06_RF002_REVISION_ACCEPTANCE_SESSION_PREP_2026-08-03/SESSION_BRIEF.md` | absent | `e7fc50aa9f41fdeb4d9caf0dd67befc0e837653befbdf012e98380ede6835319` |
| CREATE_PREP | `projects/pec/execution/_Coordination/DEL-01-06_RF002_REVISION_ACCEPTANCE_SESSION_PREP_2026-08-03/ACCEPTANCE_CONTRACT.md` | absent | `8feaa5215579c9b518415de0b14e190d8b66b09b72dd34cb43cb9963189eb486` |
| CREATE_PREP | `projects/pec/execution/_Coordination/DEL-01-06_RF002_REVISION_ACCEPTANCE_SESSION_PREP_2026-08-03/VALIDATION.md` | absent | `27880742be849ae7f2565ac0f902462b83d7432508fa2d9f7f91d344168d9d93` |
| CREATE_PREP | `projects/pec/execution/_Coordination/DEL-01-06_RF002_REVISION_ACCEPTANCE_SESSION_PREP_2026-08-03/HANDOFF_STATE.md` | absent | `6b5ba44c5a0a1f60c3c2d7b27328d790da7c7b842db4c8697a66315953f167c5` |

The six-file TM-PEC-023 SCOPE_CHANGE preparation package is external/disjoint
and must remain unchanged. No receipt is authorized before EVALUATION audits
both packages.

## Exclusions

No DEL-01-06 SOW, REVIEW, findings, lifecycle, producer/source, decomposition,
pointer, dependency, Task Management register, receipt, foreign-loop,
acceptance, release, reliance, stage, commit, push, or PR act occurs in this
preparation node.
