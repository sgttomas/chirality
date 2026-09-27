# Group-1 handoff — SCA-APP-012

**Decision.** Checkpoint group 1 is accepted, as recorded in `DECISION.md`
and `ACCEPTED_MANIFEST.csv` (owner act 2026-09-27). The selection is BASE + S
+ R-b + W-b + P-keep, with the defaults L-lib (delete both portal helpers,
port registry case 1, add the role-picker test), S-tool (narrow to the
read-only scaffold preview), E (no CONTRACT change) and the KG-033
acknowledgment unchanged.

**Next owning stage.** WORKING_ITEMS prepares checkpoint group 2 from this
snapshot: the exact amendment text, `Amendment_Actions.csv` (24 rows),
`Supersession_Delta.csv` and the propagation plan with the code
specification.

**Status of later stages.**

| Stage | State |
|---|---|
| Exact amendment and propagation decision | Pending (group 2) |
| Canonical application | Not started |
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

**Basis refresh G1B-01 (not an owner act).** The accepted package was
prepared at `adc8bdae1`. Group 2 is prepared at `origin/main` `830913331`
(PRs #1015 and #1016). All 57 inputs hashed in the accepted `Brief.md` are
byte-identical there, including every file an SCA-APP-012 edit touches. Main
changed, outside every SCA-APP-012 edit:
- the DEL-02-01 dependency register (owner's HGD-1 ruling): DEP-02-01-006,
  which the baseline lists, moved from `DOWNSTREAM`/`HANDOVER` to
  `UPSTREAM`/`INTERFACE` with DEL-08-02 unchanged as its target, and
  DEP-02-01-012 now resolves to DEL-05-03; with `_DEPENDENCIES.md`;
- the `MEMORY.md` of DEL-02-01, DEL-05-03 and DEL-08-02, an App notice, the
  loop receipts, new evaluation and dependency-closure runs, and Root
  materializer tooling.

A rerun of the accepted builder at `830913331` differs from the accepted
`Pre_Change_Coverage.json` in exactly three values:
`governed_inputs_identical_to_basis` (`true` → `false`, because the builder
compares against `adc8bdae1`), DEP-02-01-006's `Direction`/`Type`, and the
dependency-closure edge count (103 → 104). No accepted finding depends on
them: Impact Assessment §11 says DEP-02-01-006 is unchanged under P-keep, and
P-keep was accepted. The accepted baseline stays bound at its hash; the file
was restored unchanged after the rerun.

**Carried into group 2.**
- The code specification of Impact Assessment §15 under W-b and P-keep, with
  the L-lib tests (§3.3, §3.4) and `renderer-window-policy.ts` kept unchanged.
- The expected dependency outcomes DX-01, DX-02, DX-03 and DX-05 (DX-04 is
  P-x only and does not apply).
- The TM-APP-051 handoff note (§13, R-b column).
- The incremental `project-setup`, `dependency-extract` and audit handoffs
  (§21).
- The `_LATEST.md` note that the SCA-APP-011 Runtime scaffold-API item was
  closed by the Runtime loop (PR #1012), for the group-3 pointer.

Reopen only on a material departure from the accepted impact assessment.
