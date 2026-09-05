# Gate 2 Impact Assessment — App S-1/S-2/S-4a/S-7

**State:** `GATE2_READY_FOR_HUMAN_CONFIRMATION`
**Date:** 2026-09-04
**Basis:** `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f`
**Variant:** `SOFTWARE`
**Candidate amendment ID:** `SCA-APP-009` (not reserved)
**Authority:** Ryan Tufts confirmed the Gate-1 partition and authorized Gate 2 only. No amendment preview, project write, pointer movement, application, implementation, commit, or push is authorized.

## Confirmed partition

- In this impact assessment: S-1, S-2, S-4a, S-7.
- No App amendment: S-3, S-4b, S-5.
- Separate owner write-scope decision: S-6 and repo-root `.github/workflows/**`.
- Separate cycle-resolution transaction: the live nine-node dependency-register SCC.
- Mandatory pre-closure obligation: replace the active role of incomplete-layout SCA-APP-008 with a complete current-contract snapshot without altering SCA-APP-008's immutable bytes.

## Resolution summary

Gate 2 resolves S-2 as **`ADD DEL-09-07`** under PKG-09, provisionally `MIGRATION_SCRIPT` with Context Envelope `M`; DEL-09-04's decomposition scope remains unchanged. Independent review found that the SCA-APP-008 Carrier Map is explicitly `PROPOSED_NOT_APPLIED`, while the accepted decomposition requires one primary artifact shape and already treats DEL-09-04 as an `L` DMG/instruction-root/SDK-package proof. The two-job runtime-control installer/migration/rollback transaction is a separate artifact shape. The owner must explicitly approve the resulting topology change before Gate 3. See `S2_GRANULARITY_DECISION.md` and `analyst/Impact_Analyst_Memo.md`.

The resulting candidate preserves 10 packages but changes 51→52 deliverables and Context Envelope counts from `S=9, M=40, L=2, XL=0` to `S=9, M=41, L=2, XL=0`. Existing stable IDs, types, responsible-party fields, package lineage, and envelopes remain unchanged; the new ID is the next unused PKG-09 ID. Gate 3 would need two dedicated new scope items (S-1 and S-2) plus bounded edits to existing SOW-043 (S-4a) and SOW-006 (S-7). Exact scope-row IDs and text are intentionally deferred to Gate 3.

## Impact summary

| Action | Decomposition structure | Variant-local metadata | Consumers and reruns | Main risk/control |
| --- | --- | --- | --- | --- |
| S-1 | Modify DEL-04-01 at line 312; add one dedicated App Server probe SSOW/Scope-Ledger item; retain PKG-04/REQ_SLICE/M/OBJ mapping subject to exact Gate-3 validation | DEL-04-01 ScopeOfWork, `_CONTEXT`, `_STATUS`, MEMORY, `_REFERENCES`; dependency register downstream-only | Root DEL-02-08 supply notice; DEL-03-01, DEL-04-02/03/05, DEL-05-01/04; companion reconciliation; dependency extraction; loop discovery | App probe must not imply Root supply ownership or implementation activation |
| S-2 | Add DEL-09-07 under PKG-09 as provisional MIGRATION_SCRIPT/M; add one dedicated two-job installer SSOW/Scope-Ledger item mapped to OBJ-008; preserve DEL-09-04 decomposition scope | PREPARATION creates a new canonical package after application; WORKING_ITEMS authors its paired working surfaces and updates DEL-09-04 status/history plus paired MEMORY only to replace the stale unseated-carrier claim | Root DEL-02-07/11, DEL-02-06 implementation act; PKG-09 packaging/validation fan-in; companion reconciliation; dependency extraction; loop discovery | Explicit owner topology approval; Root control/storage ownership and F-APP-2/D-APP-97; no release claim |
| S-4a | Modify DEL-05-01 line 322 and existing SOW-043 at SSOW line 205 / Scope Ledger line 431; no new scope item | DEL-05-01 paired working surfaces; dependency register downstream-only | Root DEL-02-11; DEL-03-03, DEL-05-02/04/05; companion reconciliation; dependency extraction; loop discovery | Backup-before-write/rollback only for App session migration; retain A13 source bytes and `legacySource`; no consent/account-policy ownership |
| S-7 | Modify DEL-02-02 line 294 and existing SOW-006 at SSOW line 168 / Scope Ledger line 394; no new scope item | DEL-02-02 paired working surfaces; dependency register downstream-only | DEL-08-02/03/04/05, DEL-05-04, Root G-ROLE; companion reconciliation; dependency extraction; loop discovery | Role entry is UI over accepted semantics; exact labels remain `role not mechanically enforced` and `Opt-in Preview` |

Machine-readable detail is in `ACTION_IMPACT_MATRIX.csv`.

## Lens 1 — decomposition structure

### Direct authoritative effects after later approval

1. **Deliverables section:** modify Description, AnticipatedArtifacts, CoversScopeItems where a new scope row is added, and ContextEnvelopeNotes for DEL-02-02, DEL-04-01, and DEL-05-01; add DEL-09-07 under PKG-09. Existing names, IDs, ResponsibleParty, Types, package parents, and Context Envelopes remain unchanged. DEL-09-04 remains unchanged.
2. **SSOW and Scope Ledger:**
   - add one specific App Server observation/adoption-probe scope item for S-1;
   - add one specific App two-job installer/runtime-control integration scope item for S-2;
   - modify existing SOW-043 only for App session backup-before-write/rollback under S-4a;
   - modify existing SOW-006 only for Work/Agents role-entry presentation and exact posture labels under S-7.
3. **Objectives:** no objective text change is presently required. The S-2 scope row maps to OBJ-008; S-4a remains OBJ-003; S-7 remains OBJ-001/OBJ-007. S-1 must be mapped without converting App Server supply into App authority; existing DEL-04-01 support for OBJ-004 is the starting point, with final mapping validated in Gate 3.
4. **Coverage/open issues:** if both dedicated new scope rows and DEL-09-07 are accepted, ScopeItemCount rises 78→80, `IN` rows 73→75, DeliverableCount 51→52, and Context Envelopes `M=40→41`; PackageCount remains 10 and S/L/XL counts remain 9/2/0. Existing OI-001/OI-003/OI-007 implications must be reviewed; no issue may be silently closed.
5. **Decision/change log:** a later exact amendment would add a new prospective SCA entry. Gate 2 creates no project decision row.

### S-2 MODIFY versus ADD

`ADD DEL-09-07` is supported. The software method requires the smallest agent-executable unit and one primary artifact shape (`AGENT_SOFTWARE_DECOMP.md:8,41-53,192-209`). DEL-09-04 is already the only PKG-09 `L` slice and is narrowly a DMG/instruction-root/SDK-package proof (`decomposition:367,493`; its ScopeOfWork lines 80-87,112-128). S-2 is a distinct product IPC installer/migration/rollback transaction. The older Carrier Map's DEL-09-04 assignment is proposed history, not applied granularity truth (`Carrier_Map.md:1-7`). This topology change requires explicit owner acceptance under decomposition line 74 before Gate 3.

## Lens 2 — variant-local metadata

SCOPE_CHANGE owns the authoritative decomposition and its own immutable snapshot. It does not directly edit deliverable collateral, `Dependencies.csv`, estimates, schedules, or Root surfaces (`AGENT_SCOPE_CHANGE.md:90,103,116-122`).

After an accepted application, PREPARATION must first create DEL-09-07's canonical folder/package; WORKING_ITEMS then aligns or authors four packages (DEL-02-02, DEL-04-01, DEL-05-01, DEL-09-07): `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, sibling `MEMORY.md`, and `_REFERENCES.md`. A fifth downstream package, DEL-09-04, needs status/history and paired MEMORY alignment because `_STATUS.md:105` currently says the installer is unseated at DEL-09-04; after ADD DEL-09-07 that handoff claim would be stale. DEL-09-04 scope, lifecycle, and approval fields remain unchanged. Other status changes are limited to accurately gated Remaining items and History. Each status read remains paired with MEMORY.

The dependency-extract owner must then regenerate affected `Dependencies.csv` rows from accepted deliverable truth, including reciprocal consumers. No manual edge edit is authorized, and the separate nine-node SCC transaction is not absorbed into this amendment.

Full classifications appear in `SURFACE_CLASSIFICATION.csv`.

## Lens 3 — downstream consumers and derivative packages

| Package/surface | Owner | State after hypothetical application | Required closure action |
| --- | --- | --- | --- |
| New SCA-APP-009 snapshot | SCOPE_CHANGE | Incomplete until full current layout exists | Include Brief, Impact, Propagation, actions, pre/post coverage, Decision Log, Handoff, Run Summary, Supersession Delta/Map; move `_LATEST` only after owner-approved application and complete checks |
| SCA-APP-008 | SCOPE_CHANGE | Historical residue only after a valid pointer move | Preserve all bytes; cite the package-shape blocker and supersession by the complete snapshot |
| Companion invariant register | RECONCILIATION | Stale pending recomputation | Produce an exact accepted post-image if affected rows change, or deterministic byte-identical NO_CHANGE proof |
| Four existing plus one new deliverable working packages | PREPARATION / WORKING_ITEMS | Stale or absent pending alignment | Create DEL-09-07; update/author DEL-02-02/04-01/05-01/09-07; align DEL-09-04 status/history and paired MEMORY only; keep scope, gates, and lifecycle truthful |
| Dependency registers | TASK `dependency-extract` | Stale pending re-extraction | Re-extract affected/reciprocal records, then rerun full closure analysis |
| App loop workplan | HELP_HUMAN / loop owner | Review required | Decide separately whether a successor/amendment is necessary; discovery remains deliverable-local |
| App authority corpus | RECONCILIATION | Expected no change | Run no-drift status before and after any later application; stop on drift |
| Release Quality Gates | docs / release-quality owner | Review required | Recheck `docs/RELEASE_QUALITY_GATES.md:161-178` carrier/evidence mapping; align or record verified NO_CHANGE |
| S-6 Root workflow lane | Root owner | Separate, not started | Obtain explicit write-scope grant; no `.github/workflows/**` write here |
| Live SCC transaction | dependency/cycle owner | Separate, not started | Declare objective and obtain named-move ruling before any register mutation |

The complete machine-readable derivative table is `DERIVATIVE_PACKAGE_STATUS.csv`.

## Lens 4 — invariant and telemetry risk

### Orphan-risk summary

| Risk measure | Gate-2 result |
| --- | ---: |
| Package additions/removals/reclassifications | 0 |
| Deliverable additions/removals/reclassifications | 1 / 0 / 0 |
| Parent-lineage changes | 0 |
| Stable-ID reuse/renumbering | 0 |
| New scope rows proposed | 2 |
| Existing scope rows modified | 2 |
| Expected unmapped new scope rows after atomic candidate | 0, provided each new row is created and mapped in the same transaction |
| Objective removals or unsupported objectives | 0 |
| Contract/invariant ID additions | 0 expected; companion recomputation still mandatory |

### Semantic risks

- **S-1 authority inversion:** App may observe/adopt only; Root owns exact App Server supply/protocol/config/role semantics and download authority.
- **S-2 topology/release drift:** the distinct transaction becomes DEL-09-07/MIGRATION_SCRIPT/M. It remains App packaging integration around Root semantics; F-APP-2 and D-APP-97 remain active and seating authorizes no implementation or release act.
- **S-4a policy creep:** limit amendment to App session migration transaction safety. Consent, root-home, account invalidation, and resume/fresh policy remain excluded and Root-owned.
- **S-7 authority inference:** UI must present exact accepted role posture and recorded evidence; it cannot infer role, model, parentage, or enforcement success.
- **Companion count drift:** the baseline audit already found stale 81-ID/48-family prose versus authoritative 83/50. A later candidate must not worsen or mask this unrelated warning.
- **Active snapshot integrity:** SCA-APP-008's missing current-layout artifacts are a baseline blocker. The lawful repair is a complete new current snapshot and later pointer move, not retroactive edits.

### Supersession determination

All four actions are `SUPPLEMENTARY_EXTENSION`, not `SUPERSESSION`: they add App observation, transaction safety, installer integration, or presentation while preserving the admitted Root and App authority facts they cite. A complete new snapshot therefore requires `Supersession_Delta.csv` rows binding each action to the specific prior authority fact and a regenerated cumulative `Supersession_Map.csv`. No upstream fact is overridden. Exact bindings are Gate-3/4 artifacts, not invented at Gate 2.

## Estimate and schedule staleness

No dedicated estimate or schedule package exists under the App execution root, and no estimate/schedule file referencing the three existing carriers was found. Therefore no numeric estimate can be declared stale. DEL-09-07 would require a new estimate if the project later activates an estimate workflow. The active workplan and deliverable-local discovery state require review after application because newly seated items are gated future work. Any schedule or estimate outside the execution root is a downstream owner responsibility and must be cited before alteration.

## Recommended rerun and handoff order

1. Gate-3 exact semantic/structural candidate validation.
2. Reconciliation of the authoritative companion register against that exact candidate.
3. Gate-4 propagation planning and owner approval; then atomic Gate-5 application only if separately authorized.
4. PREPARATION creates DEL-09-07; WORKING_ITEMS aligns/authors four packages and updates the DEL-09-04 stale handoff claim as the fifth downstream package.
5. TASK `dependency-extract` over affected carriers, new DEL-09-07, and reciprocal consumers.
6. Full dependency closure analysis, preserving the nine-node SCC as its separate transaction.
7. Fresh full-scope AUDIT_DECOMP and authority-corpus no-drift checks.
8. The docs/release-quality owner reviews `RELEASE_QUALITY_GATES.md:161-178`; HELP_HUMAN re-derives deliverable-local Remaining inventory and decides whether a loop workplan successor/amendment is needed.

Exact triggers and expected evidence are in `RERUN_HANDOFF_MATRIX.csv`.

## Gate-2 blockers and unknowns

- **B-1 active snapshot package shape:** mandatory before any future closure/pointer move; immutable SCA-APP-008 stays untouched.
- **G-1 explicit topology approval:** the owner must accept DEL-09-07 and 51→52 deliverables before Gate 3; without that acceptance, return to Gate 2.
- **U-1 S-1 objective/scope-row exact mapping:** structural need is clear; exact new row ID/text and whether OBJ-002 is also supported belong to Gate 3.
- **U-2 companion-register post-image:** recompute may prove byte identity or require changed evidence/carrier rows; exact result cannot be invented at Gate 2.
- **U-3 downstream loop plan form:** successor versus amendment is a later loop-owner decision.

None of these authorizes product work. B-1 prevents a clean SCA closure until satisfied. U-1/U-2 are bounded Gate-3/4 tasks if the owner accepts this impact assessment.

## Human-facing Gate-2 question

**Do you accept this impact assessment?**

- **Yes — proceed to Gate 3:** explicitly approve the topology impact of adding DEL-09-07 (51→52 deliverables) and authorize an exact amendment preview for three existing deliverables, the new deliverable, two new scope rows, two existing scope-row modifications, SUPPLEMENTARY_EXTENSION bindings, and a complete new snapshot contract; still no application.
- **No — revise:** return to Gate 2 with the requested correction; do not draft amendment text.

Stop before Gate 3 until HELP_HUMAN relays the owner's answer.
