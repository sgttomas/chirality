# Group-2 handoff — SCA-APP-012

**Decision.** Checkpoint group 2 is accepted, as recorded in `DECISION.md`
and `ACCEPTED_MANIFEST.csv` (owner act 2026-09-27). The owner chose T-a and
Q-a on the revision-2 package (`a4295f9ed`, with the corrections N1–N9).

**Authoritative register.** `Amendment_Actions.csv`, SHA-256
`a9ff78f2be8356b7727d7bb853bd758a55cb6a976b42dc2fc8dc1d1365e114ad` (24 rows).
`Intake_Actions.csv` is group-1 evidence only.

**Next owning stage.** WORKING_ITEMS prepares checkpoint group 3 from this
snapshot (`ACCEPTED_GROUP2_DECISION_SNAPSHOT`):
1. Write the candidate with `build_amendment_preview.py --candidate`, in an
   environment with no `GIT_*` variables, and verify its hashes.
2. Generate the candidate `Supersession_Map.csv` and
   `Post_Change_Coverage.json`.
3. Run the post-change validation.
4. Write `RUN_SUMMARY.md` and `Handoff_State.md` in the SCA folder, with the
   exact acceptance-conditional post-images.

A separate agent prepares the code change of `Propagation_Plan.md` §4. An
independent review then covers the scope-text candidate and the code
candidate together (Q-a).

**Status of later stages.**

| Stage | State |
|---|---|
| Exact amendment and propagation decision | Accepted (this snapshot) |
| Candidate poststate | Not started |
| Canonical application | Not started; E26 and the pointer move wait for group 3 |
| Current basis | Decomposition v3.2 as amended by SCA-APP-011; `_LATEST.md` names SCA-APP-011 |
| Pointer posture for group 3 | `ACCEPTED_PREDECESSOR` (SCA-APP-011) |

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
- E26;
- `_LATEST.md` and other pointer moves;
- merging the code;
- any lifecycle, dependency-register, Task Management or release act.

Reopen only on a material departure from the accepted exact amendment or
register.
