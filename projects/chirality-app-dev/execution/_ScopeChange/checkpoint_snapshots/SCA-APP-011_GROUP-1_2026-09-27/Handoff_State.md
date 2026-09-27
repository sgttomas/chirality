# Group-1 handoff — SCA-APP-011

**Decision.** Checkpoint group 1 is accepted, as recorded in `DECISION.md`
and `ACCEPTED_MANIFEST.csv` (owner act 2026-09-27). The selection is BASE +
DQ-R + S-c, with D restate, L excluded, E no change, M-a and the scaffold
library kept.

**Next owning stage.** WORKING_ITEMS prepares checkpoint group 2 from this
snapshot: the exact amendment text, `Amendment_Actions.csv`,
`Supersession_Delta.csv` and the propagation plan.

**Status of later stages.**

| Stage | State |
|---|---|
| Exact amendment and propagation decision | Pending (group 2) |
| Canonical application | Not started |
| Current basis | Decomposition v3.2, SCA-APP-010 and `_LATEST.md` remain current |
| Pointer posture for group 3 | `ACCEPTED_PREDECESSOR` (SCA-APP-010) |

**State fields.**

| Field | Value |
|---|---|
| `DecompositionTruthState` | `NOT_STARTED` |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_REQUIRED` |
| `AuditState` | `NOT_RUN` |
| `ReadyForNextPhase` | `NOT_APPLICABLE` |

**Carried into group 2.**
- M-a wording for the retained Chirality tool contracts.
- The informational Runtime notice about its scaffold API.
- The DEL-07-02 note about the `<project>/execution` follow-up.
- Porting the route-level CHECKING-reversal and ISSUED-reopening gate tests.
- The candidate code change `dcd37f9ae`, which must be rebased and completed.
- The `/api/working-root/scope` residual, recorded but not proposed.

Reopen only on a material departure from the accepted impact assessment.
