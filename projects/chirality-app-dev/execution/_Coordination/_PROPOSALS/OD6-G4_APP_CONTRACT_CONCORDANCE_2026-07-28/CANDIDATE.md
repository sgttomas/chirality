# OD6-G4 — Complete App Contract Concordance and One-Time Repin

Status: `AUTO-APPROVED AND APPLIED — GIT_CLOSEOUT_PENDING`

Prepared and applied: 2026-07-28

Decision record: `D-APP-80`

Source basis: `main@deb01644e324af2b39cff7b52abae43784cd071b`

Terminal decomposition basis:
`projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca`

## Recommendation

Accept and apply one complete, serialized contract-concordance act:

1. inspect all 53 App `ScopeOfWork.md` contracts at execution time;
2. repin the 51 decomposition-derived contracts once to the terminal basis
   accepted by D-APP-78;
3. keep `DEL-00-01` and `DEL-00-02` as PKG-00 controls on their existing
   README basis;
4. reconcile the seven SCA-APP-006 downstream contracts to their accepted
   `_CONTEXT.md` scope mappings and boundary meanings;
5. preserve the six formerly unresolvable historical relations as
   `HISTORICAL_RELATION_UNKNOWN`;
6. repair those six contracts' prospective current basis and validate them
   without releasing APP-HOLD-1; and
7. preserve the exact six-row `REPAIR_VALIDATION_PENDING` state, all four
   prohibited operations, `entry_path_scope=ANY`, and scan-authoritative
   discovery of any new unresolvable contract.

This is the smallest act that makes the complete contract population
concordant with the accepted App decomposition while preserving the
post-repin validation interval selected through D-APP-79.

## Exact candidate identity

- live-surface manifest:
  `LIVE_SURFACE_MANIFEST.csv`
- live-surface manifest SHA-256:
  `6507828512e247f4cd96c1b2ae84cf72c7b1c1973bd2b69dfb21ef32206c7218`
- exact application surfaces: 56
- contract concordance rows: 53
- decomposition-derived repins: 51
- unchanged PKG-00 controls: 2
- semantic downstream reviews: 7
- preserved historical-UNKNOWN relations: 6
- active repair-validation holds after repin: 6

`CONTRACT_CONCORDANCE.csv` gives every contract an exact disposition.
`HISTORICAL_RELATIONS.csv` separates the six unknowable historical relations
from their repaired prospective current basis. `VALIDATION.json` records the
deterministic population and class checks. The runnable
`validate_contract_concordance.py` reproduces those three artifacts and the
live-surface manifest from the Git-pinned preimage and current postimage.

## Seven downstream semantic dispositions

| Deliverable | Added accepted relation | Disposition |
|---|---|---|
| DEL-02-05 | SOW-023 | Supported attachment-selection and retry-preservation UI; DEL-09-06 retains security validation |
| DEL-04-02 | SOW-076 | OUT boundary-only trace; no non-App provider-scope activation |
| DEL-06-02 | SOW-064 | Supported App/project catalog, requested-tool validation, and collision prevention |
| DEL-06-03 | SOW-064 | Supported in-process deterministic MCP wrappers and App extension boundary |
| DEL-07-01 | SOW-075 | Supported deterministic root-boundary enforcement |
| DEL-07-06 | SOW-077 | OUT boundary-only trace; no resource-governance activation |
| DEL-09-04 | SOW-078 | OUT boundary-only trace; no Windows/Linux packaging activation |

## Hold behavior after repair

The execution-time corpus scan now reports 53 contracts and zero
unresolvable current basis declarations. That does not release the six
registered targets. The live guard:

- treats all six as active `REPAIR_VALIDATION_PENDING` holds;
- blocks reliance, dispatch, `CHECKING` promotion, and
  accepted-dependency consumption through every entry path;
- requires all six D-APP-79 repair-pending IDs to remain present in the
  register, so deletion fails closed even after the basis resolves;
- still requires every newly scan-derived unresolvable contract to appear in
  the register; and
- permits an unaffected clear target.

The six final register rows retain `NO_REPIN`: D-APP-80 is the exact
one-time repin authority for this application, and the final posture grants
no further repin or exception.

## Validation contract

- `validate_contract_concordance.py`: PASS
- 53/53 `validate_scope_of_work.py`: PASS
- 14/14 APP-HOLD-1 tests: PASS, including post-repin hold and
  missing-repair-row failures
- APP-HOLD scan/register comparison: PASS
- exact 51/2/7/6 population classes: PASS
- six historical missing objects remain unresolvable: PASS
- terminal basis path resolves at the accepted commit: PASS
- exact path and preimage/postimage hash manifest: PASS
- decision, receipt, containment, whitespace, and diff checks: required
  before Git closeout

## Non-effects

This candidate does not:

- release, weaken, or bypass APP-HOLD-1;
- reconstruct any missing historical decomposition object;
- change the App PRD, decomposition, invariant register, package or
  deliverable topology, or lifecycle state;
- repin either PKG-00 control;
- change implementation, runtime, dependency, estimate, schedule, identity,
  version, compatibility, facade-retirement, issuance, release, or
  professional-reliance state; or
- authorize a future repin, hold transition, or OD6 gate.
