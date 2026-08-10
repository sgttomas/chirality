# TM-PEC-014 DEL-00-03 SPEC currency — production and validation evidence

**Status:** CANDIDATE PRODUCED / VALIDATED / REVIEW NOT STARTED
**Owning workflow:** WORKING_ITEMS, package `PKG-00`, selected deliverable
`DEL-00-03` only
**Owner direction:** 2026-08-09 execution of TM-PEC-014 candidate production
only

## Activation and frozen work graph

- `RunID`: `TM-PEC-014_SPEC_CURRENCY_2026-08-09`
- `InstanceID`: `WORKING_ITEMS-DEL-00-03-TM-PEC-014`
- `PackageID`: `PKG-00`
- `SelectedDeliverables`: `DEL-00-03`
- `AcceptedGitBasis`: `origin/main@d269f0e04204bc463a11684499213b2283bd28f7`
- `Branch`: `codex/pec-currency-repair-20260809`
- `WorkGraphVersion`: `1`
- `SelectionAuthority`: owner direction 2026-08-09 plus routed handoff
  `_DomainEngines/pec/_TaskManagement/HANDOFF_TM-PEC-014_DEL-00-03_SPEC_CURRENCY.md`
- `Posture`: `TERMINAL_FAN_OUT_IN` with one direct deterministic integration
  node; no Agent 2 dispatch was necessary for the exact mechanical amendment.
- `Node N1`: reproduce the accepted preimage, replace only the routed first
  paragraph of SPEC §8, and return the successor plus deterministic evidence.
- `Edges`: none.
- `Concurrency`: not applicable; one node and one product.
- `IntegrationOwner`: this WORKING_ITEMS instance.
- `AllowedWriteTargets`: the exact SPEC product path and evidence/return files
  in this coordination directory.
- `FanInGate`: exact semantic diff, basis/citation resolution, preserved bytes,
  containment, registered checks, and successor SHA binding.
- `Escalation`: REVIEW Gate 1 and owner exact-byte acceptance remain outside
  this run; any required SOW/checklist or other product change must HOLD.

## Path containment and disjointness

The exact product is:

`projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md`

TM-PEC-013 owns three different products:

1. `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md`
2. `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md`
3. `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md`

The TM-PEC-014 product is therefore path-disjoint from all three TM-PEC-013
products. Before evidence files were added, `git diff --name-only` contained
exactly the single SPEC path. The product diff is 5 inserted lines and 4
deleted lines in one hunk, confined to the first paragraph of §8.

## Hash binding

| Surface | SHA-256 | Result |
|---|---|---|
| SPEC accepted preimage | `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315` | reproduced before edit |
| SPEC candidate successor | `28de769a82945fc4b2586a36c89870c7e1f78dd1698fa6f028b30236014bd34c` | produced and check basis |
| SCA-004 Gate 5 handoff | `919d40bba285ebdab987c17c4443d9583528f845fde0681c460788f5701dbc1c` | reproduced |
| SCA-004 decision log | `c377d7f094b46ede1b0ec8f108e7c52e61dada9565227820415b47301a87cd3c` | reproduced |
| SOFTWARE_DECOMP revision 1.4 | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` | reproduced |
| D-PEC-78 decision record | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` | reproduced |
| Preserved DEL-00-03 ScopeOfWork | `0e2cfad8fcb377381042fd63c7e73002ad93037bffd17b7a3b9eb58889469f54` | unchanged |
| Preserved DEL-00-03 `_STATUS.md` | `629ca0dda894954943b694680ebbaf8688615e0ca3fefa1a18ef84c2cd606cfb` | unchanged |
| Preserved DEL-00-03 `Dependencies.csv` | `5b42f2de2a098fb8f833736ebaf15445bd50734a9341b7fb19e7fa1d0112cde2` | unchanged |

## Deterministic checks bound to successor

| Check | Result |
|---|---|
| Reliance hold preflight, `dispatch-for-production` | `ALLOW` |
| Reliance hold preflight, `candidate-validation` | `ALLOW` |
| Exact old paragraph absent and exact routed successor statements present once | `PASS` |
| One-hunk semantic diff confined to SPEC §8 | `PASS` |
| D-PEC-78 O-A decision and SCA004-G1 citation resolution | `PASS` |
| Revision-1.4 basis: OI-003 resolved, SOW-077 IN, DL-19/SCA-004 present | `PASS` |
| SOW, lifecycle, and dependency byte preservation | `PASS` |
| Git whitespace (`git diff --check`) | `PASS` |
| PEC API contract suite, Python 3.13 | `PASS`, 6/6 |
| PEC loop-registry suite, Python 3.13 | `PASS`, 12/12 |
| PEC service-core posture | `PASS`, dependency/locality/registration |
| Root practitioner-harness self-check | command exit `0`; inherited summary `REVIEW=4`, `WARN=31`, `INFO=14`, `NOT_APPLICABLE=1`; no TM-PEC-014 finding |

The workflow-registered loop-registry command was first attempted with the
system `python3` (3.9) and failed during test collection because Python 3.9
does not support the source's `dataclass(..., slots=True)` argument. The same
unchanged suite passed 12/12 with the available Python 3.13 interpreter. This
is an interpreter mismatch in the first attempt, not a candidate defect.

## Boundary and blocker

No REVIEW type was selected and REVIEW was not run. No exact bytes were
accepted, no lifecycle or register state moved, and no SOW, source,
dependency, receipt, plan, PRD, or historical surface was edited.

The preserved current DEL-00-03 SOW still contains revision-1.3-era
`REQ-007`/`AC-008`/`VER-006` wording that lists OI-003 among decisions to
remain unchanged. The routed handoff expressly forbids changing that SOW in
this production run. REVIEW must decide whether exact conformance requires a
HOLD and return for owner direction. This does not prevent completion of the
authorized candidate-production node.
