# Group-2 handoff — SCA-APP-011

**Decision.** Checkpoint group 2 is accepted, as recorded in `DECISION.md`
and `ACCEPTED_MANIFEST.csv` (owner act 2026-09-27). The owner chose W-a and
Q-a, with the revision-2 corrections and register row 29 (DEL-07-01, a
reopened group-1 item decided by this act).

**Authoritative register.** `Amendment_Actions.csv`, SHA-256
`416097312beffa47143b2993bfe17721e5c312630789a1101e6cbda688edbc22` (29 rows).
`Intake_Actions.csv` is group-1 evidence only.

**Next owning stage.** WORKING_ITEMS prepares checkpoint group 3 from this
snapshot (`ACCEPTED_GROUP2_DECISION_SNAPSHOT`):
1. Write the candidate with `build_amendment_preview.py --candidate` and
   verify its hashes.
2. Generate the candidate `Supersession_Map.csv` and
   `Post_Change_Coverage.json`.
3. Run the post-change validation.
4. Write `RUN_SUMMARY.md` and `Handoff_State.md` in the SCA folder.

The App loop prepares the code change (`Propagation_Plan.md` §4). An
independent review then covers the scope-text candidate and the code
candidate together (Q-a).

**Status of later stages.**

| Stage | State |
|---|---|
| Exact amendment and propagation decision | Accepted (this snapshot) |
| Candidate poststate | Not started |
| Canonical application | Not started; E47 and pointer moves wait for group 3 |
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

**Remains unauthorized until group 3:**
- E47;
- `_LATEST.md` and other pointer moves;
- sending the Runtime notice;
- merging the code;
- any lifecycle, dependency-register or release act.

Reopen only on a material departure from the accepted exact amendment or
register.
