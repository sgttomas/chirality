# Dependencies: DEL-09-07 Two-Job Runtime-Control Installer Migration and Rollback

## Coordination (human-owned)
- **Mode:** NOT_TRACKED
- **Notes:** Structural initialization only; dependency extraction has not run.

## Upstream (I need these before I can proceed) — human-owned declarations
- Dependencies coordinated externally by humans.
- Declared upstream dependencies: NONE.

## Downstream (These need me) — human-owned declarations
- Dependencies coordinated externally by humans.
- Declared downstream dependencies: NONE.

## Extracted Dependency Register (populated by TASK+dependency-extract)
- **Status:** EXTRACTED
- **Dependencies.csv:** `Dependencies.csv` (v3.1; 29 canonical columns).
- **Summary:** 8 ACTIVE extracted rows: 2 ANCHOR and 6 EXECUTION; 0 RETIRED.

| DependencyID | Class / type | Target | Closure state |
|---|---|---|---|
| DEP-09-07-001 | ANCHOR / IMPLEMENTS_NODE | SOW-080 | NOT_APPLICABLE |
| DEP-09-07-002 | ANCHOR / TRACES_TO_REQUIREMENT | OBJ-008 | NOT_APPLICABLE |
| DEP-09-07-003 | EXECUTION / PREREQUISITE | Root DEL-02-07 routed control contract | PENDING |
| DEP-09-07-004 | EXECUTION / PREREQUISITE | Root DEL-02-11 routed state semantics | PENDING |
| DEP-09-07-005 | EXECUTION / PREREQUISITE | Adapter adoption evidence | TBD |
| DEP-09-07-006 | EXECUTION / PREREQUISITE | Installer journal and inspection contract disposition | PENDING |
| DEP-09-07-007 | EXECUTION / PREREQUISITE | Source-version and recovery fixture rules | PENDING |
| DEP-09-07-008 | EXECUTION / CONSTRAINT | Separate production authorization and applicable release rulings | PENDING |

## Run Notes & History (populated by TASK+dependency-extract)

### Run Notes

- Extraction date: 2026-09-05; basis `4b6d2bb2c1b6e798c0000f51b38755d92055f65d`.
- MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=RECONCILIATION.
  SCOPE=DEL-09-07; RUN_ROOT=`projects/chirality-app-dev/execution` relative to REPO_ROOT.
- SOURCE_DOCS=[ScopeOfWork.md, _CONTEXT.md]; ANCHOR_DOC=ScopeOfWork.md;
  EXECUTION_DOC_ORDER=[ScopeOfWork.md]. Defaults: DOC_ROLE_MAP=DEFAULT;
  ARCHITECTURE_BASIS_POLICY=NONE. _REFERENCES.md read for pointers only.
- DECOMPOSITION_PATH=`projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
  SOW-080, OBJ-008, DEL-09-07 and PKG-09 exist in that accepted decomposition.
- Pass 1 completed before Pass 2: SOW-080 is the single existing parent definition
  anchor; OBJ-008 is its objective trace. Pass 2 extracted only explicit information
  inputs and constraints from ScopeOfWork.md. No FLOATING_NODE, AMBIGUOUS_ANCHOR
  or MISSING_DECOMPOSITION warning applies.
- All EvidenceFile paths are deliverable-relative; TargetLocation paths are
  repo-root-relative. Root DEL-02-07 and DEL-02-11 use EXTERNAL with qualified
  TargetRefID and empty TargetDeliverableID/TargetPackageID, preventing collision
  with App identifiers. Root SOW locations are taken from the local SOW source
  keys; Root files were not independently inspected by this extraction.
- Root contract existence is not implementation readiness or routed acceptance.
  TBD-001 preserves unknown App entry/job details; the private supervisor socket
  is not an App entry. TBD-002 and TBD-003 remain unresolved owner contract inputs.
- No execution edge was emitted merely for App DEL-09-04/DEL-09-05 or Root
  DEL-02-06 ownership exclusions. No downstream consumer transfer is explicitly
  assigned by these sources. The release constraints apply to the appropriate
  acts; G5/G6a are not inferred prerequisites to every installer activity.
- The human-owned Coordination and declaration sections above are byte-preserved.
  Their initialization-era note that extraction has not run is historical; this
  extracted register records the later run without changing NOT_TRACKED or
  declared NONE. Machine extraction does not elect human tracking policy.
- ID helper limitation: the skill's TASK-enforced allowlist excludes
  `validate_id_format.sh`; its inspected legacy patterns also do not accept
  the decomposition's two-digit App IDs or SOW-080. The helper was not run.
  Identity was checked against the explicit accepted source/decomposition;
  no identifier was rewritten to satisfy an incompatible legacy pattern.

### Run History

- 2026-09-05T04:20:11Z — UPDATE / CONSERVATIVE; explicit decomposition found
  and anchors validated; 8 ACTIVE (2 ANCHOR, 6 EXECUTION), 0 RETIRED.
  New register; no previous CSV rows to merge or retire. ID-helper limitation
  recorded above. Evidence: `_run_records/TASK_RUN_2026-09-05_0420.md`.

## Lifecycle Summary (populated by TASK+dependency-extract)

- Extraction lifecycle: 8 ACTIVE, 0 RETIRED; all Origin=EXTRACTED.
- Closure lifecycle: 5 PENDING, 1 TBD, 2 NOT_APPLICABLE; none SATISFIED or WAIVED.
- RequiredMaturity captures needed input state; ProposedMaturity remains TBD.
  ACTIVE means the relationship is observed in the source, not satisfied.

## Consumer Handoff Notes (optional)

### Downstream Handoff Notes

RECONCILIATION may consume this local register with the accepted SOW and its
decomposition basis. Preserve Root qualification and distinguish input evidence
from gate satisfaction. Adapter-adoption carrier/evidence location, Root routing,
and TBD-001 through TBD-003 remain pending verification or disposition.
This run does not authorize implementation, lifecycle promotion, dependency
tracking-policy changes, or an SCC resolution. No local mutual dependency was
found in this one-deliverable extraction; the separate nine-node SCC was not
evaluated or reordered.
