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
