# Dependencies: DEL-02-08_Exact_Supply_and_Protocol_Pinning Exact Supply and Protocol Pinning

## Coordination (human-owned)
- **Mode:** DECLARED
- **Notes:** execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/RUNTIME_METADATA_BINDINGS.csv (repository-relative); approved fan-in declarations only.

## Upstream (I need these before I can proceed) — human-owned declarations
- None declared.

## Downstream (These need me) — human-owned declarations
- chirality-runtime::DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance — Reason: runtime evidence fan-in.
  - Required maturity: Not specified; no maturity inferred.
  - Location: projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance (repository-relative).

## Extracted Dependency Register
- **Status:** RUN_COMPLETE
- **Dependencies.csv:** Dependencies.csv (v3.1)
- **Summary:** 7 ACTIVE rows: 6 ANCHOR (1 parent, 5 trace), 1 EXECUTION; 0 RETIRED.

| DependencyID | Class | Direction | Target | Satisfaction |
|---|---|---|---|---|
| DEP-02-08-001 | ANCHOR | UPSTREAM | PKG-02_Runtime_Product | NOT_APPLICABLE |
| DEP-02-08-002 | ANCHOR | UPSTREAM | SOW-104 | NOT_APPLICABLE |
| DEP-02-08-003 | ANCHOR | UPSTREAM | OBJ-001 | NOT_APPLICABLE |
| DEP-02-08-004 | ANCHOR | UPSTREAM | OBJ-002 | NOT_APPLICABLE |
| DEP-02-08-005 | ANCHOR | UPSTREAM | OBJ-004 | NOT_APPLICABLE |
| DEP-02-08-006 | ANCHOR | UPSTREAM | OBJ-007 | NOT_APPLICABLE |
| DEP-02-08-007 | EXECUTION | DOWNSTREAM | DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance | TBD |

## Run Notes
- MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; DOC_ROLE_MAP=DEFAULT; ARCHITECTURE_BASIS_POLICY=NONE.
- RUN_ROOT=projects/chirality-runtime/execution; SCOPE=PKG-02_Runtime_Product.
- Explicit decomposition: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md; anchors validated against accepted package/scope/objective records.
- ANCHOR_DOC=_CONTEXT.md; execution source order ScopeOfWork.md, declared _DEPENDENCIES.md, exact Gate4 DEPENDENCY_DISTRIBUTION.csv; _REFERENCES.md used only for resolution.
- Six unique accepted runtime evidence prerequisites have twelve local mirrors across seven registers. Do not count each mirror as another gate. Parent/trace anchors never gate execution.
- Two Root edges GOV-04-05/GOV-05-02 to GOV-04-11 stay in the Root owner view, as recorded in execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/DEPENDENCY_DISTRIBUTION.csv. No runtime targets created for them.
- Receipt-validator/runtime and App/client relationships remain non-gating coordination, outside this execution register. Nine compatibility holds remain; R16-B disposes Tier-0 separately. No satisfaction follows from contract presence or INITIALIZED status.
- Historical no-edge wording is read only with the accepted six-edge destination declaration; no inter-carrier ordering inferred.
- Required/proposed maturity and execution satisfaction are TBD, not inferred. No source/content/status/activation/acceptance changes.
- Source pins and actual QA: projects/chirality-runtime/execution/_Coordination/AgentRuns/SCA005_SETUP/DEPENDENCY_RUN/. A changed source hash requires dependency refresh before reliance.
- ID validation uses accepted full-slug registry identity: generic validate_id_format.sh uses incompatible legacy three-digit PKG/DEL widths and is outside the skill frontmatter allowlist; no identifier rewritten to fit it.

## Run History
- 2026-09-06T00:59:58.877209+00:00: UPDATE CONSERVATIVE; decomposition present and accepted wrapper read; 7 ACTIVE, 0 RETIRED; source pins recorded. No floating or ambiguous parent anchor. No evidence satisfaction inferred.

## Lifecycle Summary
- ACTIVE=7; RETIRED=0; ANCHOR satisfaction NOT_APPLICABLE=6; EXECUTION satisfaction TBD=1.
- Source lifecycle remains unchanged; metadata initialization is not evidence satisfaction.

## Current-state refresh
- 2026-09-06T01:02:10.864086+00:00: observed concurrent manager-authorized guarded OPEN→INITIALIZED transition; production unchanged. Manager evidence: execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_GATE5_2026-09-06/SETUP/INITIALIZATION_TRANSITIONS.json. Memory paired where present. No evidence satisfaction or activation follows; execution satisfaction remains TBD.
