# Chirality Runtime — software decomposition v1.0 candidate

Package role: **working surface**. Status: **GATE3_REVIEW_NOT_ACCEPTED**.
Proposed home: `projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md`.
Source basis: Root PRD revision 8 / decomposition revision 1.3 / accepted SCA-004; exact hashes in SOURCE_PINS.csv. SCA-005 Gate 2 accepts migration impact, not this decomposition.

## Authority and vocabulary

| Canonical term | Synonyms / historical term | Meaning |
|---|---|---|
| Runtime project | generic runtime; historical Root runtime | Product owner after effective transfer; not a client or a second governance root |
| Root | repository control plane / instruction root | Shared governance, tools and owner decisions; historical product evidence remains readable |
| Qualified identity | root::DEL… / chirality-runtime::DEL… | Project qualifier distinguishes reserved source history and proposed destination authority |
| Compatibility identity | root-runtime-1, epoch 1 | Stable protocol subject; the historical name does not imply continued Root product ownership |
| Held binding | HELD_UNAVAILABLE | Required actual act or evidence absent; relocation and CI do not release it |

## SSOW and package partition

SOW-104 is IN: consequential generic runtime semantics use the runtime-project standing carrier and declared project write locus; preserve D-GOV-20's authority, security, residency, exclusions and implementation gates; produce versioned-contract, affected-client and regression evidence; return release disposition to an accountable human; do not transfer ownership to a client.

`RUNTIME_SCOPE_LEDGER.csv` is the authoritative companion register proposed for this one inherited scope row. It changes ownership/location explicitly, not requirement content. Its requirement-level expansion is `INHERITED_REQUIREMENT_TRACE.csv`, which preserves every numbered requirement from the seven pinned ScopeOfWork source files. These are requirement identifiers within SOW-104, not invented additional scope IDs. Entire source contracts, including outputs, values and evaluation matrices, remain incorporated through `SOURCE_SCOPE_REQUIREMENTS/` and SOURCE_PINS.csv.

| PackageID | Name | Work domain / inclusions | Exclusions |
|---|---|---|---|
| PKG-02_Runtime_Product | Generic Runtime Product | Shared generic runtime contract, bounded implementation slices, and product assurance | Client UI/hosting, Root instruction governance, operational credentials/state, unrelated project duties |

There is one flat package. Retain numeric PKG-02 and DEL-02-06 through DEL-02-12 and full slugs; do not invent preceding packages or renumber IDs for cosmetic continuity. Full slugs follow the existing canonical materialized IDs; bare numeric IDs are aliases, project-qualified in cross-root references.

## Objectives, deliverables and artifacts

`RUNTIME_OBJECTIVE_REGISTER.csv` is the proposed authoritative objective register. Each of OBJ-001, OBJ-002, OBJ-004 and OBJ-007 carries exact source statement plus explicit runtime partition. Coherent authority, human issuance, no self-authorization and file-native recoverability are preserved. Historical Root/situated demonstration success and deferrals remain separate; none is declared achieved.

`RUNTIME_DELIVERABLE_REGISTER.csv` is the proposed authoritative seven-carrier register; it declares names, complete descriptions, accountable/production roles, types, anticipated artifacts, scope/objective references and Context Envelopes. Every carrier belongs only to PKG-02. All seven envelopes are M: integration fan-in (06), supervisor/control (07), supply/protocol (08), account/consent (09), event/API (10), retirement/recovery (11), conformance evidence (12). These are bounded production contracts, not authority to execute a whole migration or every feature concurrently.

Artifacts retain the source carrier taxonomy: requirement and release-assurance records; code/tests for bounded behavior; contracts/schemas and fixtures; consent/security controls and tests; conformance evidence. An anticipated artifact is not completed evidence. Responsible human is Ryan Tufts; WORKING_ITEMS manages a bounded production brief and its Agent 2 executor after activation.

## Inherited contract interpretation

Later custody disposition: `CUSTODY_DISPOSITION_D36.md` binds D-GOV-36/D-APP-126 to DEL-02-06 REQ-041 and DEL-02-09 REQ-001/002 only after the exact Runtime owning amendment is accepted and applied. Its limited exception and supplementary lifecycle/bootstrap detail govern those facts; all other inherited requirements and immutable historical evidence remain.

`OWNERSHIP_OVERLAY.md` supplies the only prospective interpretation changes to immutable source contracts: qualified owner and locus, governance/client split, and later recorded dispositions. No blanket replacement of the word Root is permitted. Preserve DEL-02-06 REQ-027: first activation is specification, read-only inventory, evidence-matrix design and planning; it writes no implementation bytes. Later actual authorization must name its exact subject. Read all inherited conditions, exclusions and evaluation matrices, not only the generated requirement rows.

`HOLD_SUCCESSOR_MAP.csv` preserves ten historical markers. Nine are still held; R16-B separately records Tier-0 continue-separate. TM-ROOT-106 remains open; R18 closed TM-ROOT-122. `ACCEPTED_EVIDENCE_CONTINUITY.csv` preserves six semantic files and the compatibility JSON at source paths/hashes. Keep root-runtime-1 epoch 1 and null held identities. Acceptance of a historical semantic subject is not acceptance of current implementation or release.

## Dependencies and lifecycle

`DEPENDENCY_DISTRIBUTION_PREVIEW.csv` previews all eight accepted ordering edges: six runtime carrier evidence inputs to DEL-02-06, and two Root governance inputs to the receipt-validator successor GOV-04-11. The latter stay outside this runtime package. Receipt-validator-to-runtime and App coordination relations remain non-gating; no inter-carrier ordering or new gate is inferred. Deliverable-local dependency truth must be propagated and independently checked at later gates; this preview is not the live dependency register.

Zero destination carriers are activated. No materialization, status change, source retirement, project registration or _LATEST move occurs in this candidate. Source status/history stays unchanged until an accepted successor and propagation instrument permit a non-destructive retirement. Qualified successor references never mutate accepted historical files.

## Coverage, issues and decisions

`TRACE_PREVIEW.csv` and `COVERAGE_PREVIEW.json` are **derived publication artifacts**, regenerated from candidate registers. One scope row, one package, seven deliverables and four supported objectives have no unmapped entries in this partition; all envelopes M, zero XL. Requirement count is computed in coverage JSON. This is structural accounting, not accepted audit, production completion or closure of the four baseline historical snapshot gaps.

- OI-01: exact charter/decomposition and combined owning amendments await owner acceptance; SOFTWARE_DECOMP gates are NOT_CONFIRMED in GATE_READINESS.md.
- OI-02: Gate4/5 setup, materialization, metadata, guards and effective transfer remain unapplied.
- OI-03: dependency extraction, remaining effort, ordering, trace/audit and other accepted Gate2 derivatives need their owning reruns; none is silently deferred.
- OI-04: inherited historical findings and production-contract warnings remain in the SCA-005 baseline; this partition cannot waive or backfill them.

Decisions proposed: preserve stable IDs and historical evidence; use one domain package; partition objectives explicitly; retain scope through pinned full contracts; keep nine holds and later dispositions; make source retirement conditional on accepted successors. CHANGE_JOURNAL.csv records exact source-to-destination changes. No new scope, held feature work, release, or PR merge is selected by this draft.

### Custody amendment record — candidate for owning acceptance

D36/D126 choices are owner-selected and observable at main e1dee34315ff4ca448b0fbc14e5542b6bad9fac2. The exact Runtime postimages and propagation remain candidate until the owning SCOPE_CHANGE acceptance/application. This revision introduces the named custody supplement and updates SOW-104 decision references without changing partition, IDs, inherited requirement count, lifecycle or holds. The owning immutable amendment snapshot must record the exact acceptance/application identity; no historical migration snapshot or hash map is rewritten.

### Account-control authority amendment record — candidate for owning acceptance

`ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md` supplies the narrow later binding for DEL-02-09 REQ-001/002 and DEL-02-06 CLM-003/REQ-010: dedicated authenticated account-only PUBLIC Unix control for nonexecuting bootstrap/status/cancellation and hosted-account lifecycle only. Project operations, including folder disconnect and result retrieval, retain project authorization and all consequential-work preconditions. The owner selected this narrow authority boundary on 2026-09-07; the newly reviewed Root D36 candidate is `/Users/ryan/.codex/worktrees/85d6/chirality/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/root/author-v1/D36_PROPOSED_POSTIMAGE.md`, SHA256 `2697862a31ee856ae923c91af38a5e07f8997115a4bd1baabf083afb069939b1`, with independent review `/Users/ryan/.codex/worktrees/85d6/chirality/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/root/review-v1/FINAL_PREAPPLICATION_REVIEW.md`, SHA256 `32d44dcc5de4dfc6056ce4e430966f7b46248cd477fc66814f049d08c001d439`, verdict `PASS — READY FOR FAITHFUL CANONICAL APPLICATION`. Parent confirms local Root application, but the Root candidate remains unpublished and no accepted main identity was supplied. This binding therefore remains `PROSPECTIVE / NOT EFFECTIVE` for Runtime. These exact Runtime postimages remain ineffective until Runtime acceptance/application, publication/main identity where required for reliance and required successor adoption. Complete wire/recipient delivery/successor recovery and source gates remain explicit in the supplement. Existing custody disposition, partition, IDs, requirement count, historical snapshots, lifecycle and holds are unchanged; SOW propagation must bind the actual accepted decomposition commit under its own reviewed application.
