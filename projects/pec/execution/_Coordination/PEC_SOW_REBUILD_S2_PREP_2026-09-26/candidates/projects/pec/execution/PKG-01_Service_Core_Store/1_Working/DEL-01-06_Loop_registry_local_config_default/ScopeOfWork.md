---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-06
package_id: PKG-01
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@189f205ff02df4111b33c20be441ce06e65ada7a
project_scope_refs: [SOW-077, SOW-094]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-01-06 Loop registry (local config default)

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-01-06` — "Loop registry
(local config default)" — in `PKG-01` Service Core & Store of the PEC v2 build.
It covers project scope items `SOW-077` and `SOW-094` in service of package
objective `OBJ-004`. It rebuilds, as a whole, the earlier contract with SHA-256
`5fdcfd968345…a2fa8` (AX-012).

The accepted basis is `execution/_Decomposition/SOFTWARE_DECOMP.md`
**revision 1.6** (`current_basis`, SCA-006 successor), accepted by the owner at
SCA-006 checkpoint group 3 on 2026-09-26. The frontmatter pin
`189f205ff02df4111b33c20be441ce06e65ada7a` is the checkpoint-3 acceptance
commit, an ancestor of `origin/main`. At that commit `SOFTWARE_DECOMP.md` has
SHA-256 `9374c21fb87b…8eb1`, `Deliverables.csv` `94ee5d182ae9…9805`,
`ScopeLedger.csv` `1d24a4b86f05…916e` and `ContextBudgetQA.csv`
`93b0bb075a0e…4c7c`, and `docs/PRD.md` v2.4 has SHA-256 `ae49b8065698…3fbe`.

**Observation commit.** The pin binds the accepted decomposition bytes only.
Unless a claim names another commit, every statement below about the state of a
file, record, lifecycle or decision is an observation at `origin/main`
`aca930622`. There the four decomposition files and the PRD named above are
byte-identical to the pin. The registry source and this deliverable's
folder are byte-unchanged between the `D-PEC-96` act merge `73ed349ed` and
`aca930622`. At `aca930622` the deliverable-local `_CONTEXT.md` carries the
register `Description` of CLM-010 and a provenance tail ending at revision 1.5,
and `_REFERENCES.md` names revision 1.5 and PRD v2.3.

**Objective warrant.** Revision 1.6 maps both `SOW-077` and `SOW-094` through
`DEL-01-06` to `OBJ-004`: the §3 objective row lists both items and this
deliverable. The `SOW-094` attribution rests on its PRD anchor `PEC-DSH-002`,
which requires a "Lifecycle census across all registered loops'
packages/deliverables"; "all registered loops" is resolvable only once
something names them. PRD v2.4 §12 states the P2 scope in the same
registry-relative terms: "The loops the loop registry lists (§16.3); Overview,
census, registers, decision slate". The `SOW-077` attribution entered under
SCA-004 after `D-PEC-78` O-A settled the registry home and shape, and SCA-005
added a closed, PEC-versioned feed profile to each row of both items. The
attribution is indirect: the registry names the loops and the feeds that the
census and orientation surfaces of `OBJ-004` read, and it renders no view
itself. AC-015 puts that qualification before the review gate.

- **CLM-001** — `SOW-094` states: "Maintain the loop-registration configuration naming the loops PEC serves and each row's feed-profile selection (local config default)", with `SourceRef` "§12 P2, PEC-DSH-002" and `DecisionRef` "D-PEC-78; SCA-005".
- **CLM-002** — `OBJ-004` states: "The human owner has one live view: loops, gates, lifecycle census, decisions waiting on them, and who is working where" (PRD §3.4).
- **CLM-003** — `SOW-077` states: "Maintain the PEC-owned long-term service registry naming the loop locators PEC serves through the strict, versioned JSON/schema paths and core-owned typed LoopRegistry port, each row declaring a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record)". Its `Notes` cell adds: "A feed profile is PEC's reading hypothesis, never the loop's truth; feed-profile declarations need a strict schema v2 plus a `RegisteredLoop` port field through a later D-PEC source packet (no `v2/**` write here), within D-PEC-78 O-A (version 1 remains strict; supplementary extension, no supersession)". The first sentence of the `SOW-094` `Notes` cell records the implementation basis: "Local JSON configuration is the implementation basis for the long-term PEC-owned service registry confirmed by D-PEC-78; the core port keeps filesystem and JSON details replaceable." The second sentence of that cell is the stale design text of CON-003.
- **CLM-008** — PRD v2.4 §16.3, decision 3, is the product text for the registry:

> **Resolved 2026-08-02 by `D-PEC-78` O-A.** The long-term home and shape
> of PEC's loop registry is the existing PEC-owned strict, versioned
> JSON/schema paths with the core-owned typed `LoopRegistry` port. PEC owns
> only its configured service set; each listed loop remains authoritative
> for its own entrypoint and governed truth. Later row changes remain
> owner-gated PEC configuration changes. Listing or removing a loop creates
> no duty, lifecycle effect, cadence, conformance obligation, or authority
> over that loop, and no governed act may depend on PEC or the registry.
> Registry rows may declare closed, PEC-versioned feed profiles (profile
> ID, version, live or historical, and a basis citation to the loop's own
> record); a profile is PEC's reading hypothesis, never the loop's truth.
> Schema version 1 remains strict; a strict schema version 2 carrying feed
> profiles, with a `RegisteredLoop` port field, arrives only through a
> later D-PEC packet, within D-PEC-78 O-A.

  The "later D-PEC packet" this text anticipates is `D-PEC-96`, ruled and applied as CLM-015 records.

## Deliverable Definition — Ontology

`DEL-01-06` is typed `BACKEND_FEATURE_SLICE` at Context Envelope `S` with
`PhaseHint` `P1`. The decomposition register records its anticipated artifacts
as "Config format + loader + tests" and carries no `ContextEnvelopeNotes`;
`ContextBudgetQA.csv` rates it `Risk` `LOW` with no recommended action. The
three outputs below are that list and nothing beyond it.

- **OUT-001** — A loop-registry configuration format at schema version 2: documented field semantics for a local configuration file that names the loops PEC serves and each loop's feed-profile declarations, together with the checked-in local default instance of that file.
- **OUT-002** — A loader in the PEC service core that reads the registry configuration, validates it against OUT-001, and exposes the resulting registered-loop set, each loop with its typed feed profiles, to record-tier consumers through the core-owned typed port.
- **OUT-003** — An automated test suite covering the format and the loader, implementing the verification methods declared in this contract.

### Identity of record

- **CLM-009** — `DEL-01-06` is named "Loop registry (local config default)", Type `BACKEND_FEATURE_SLICE`, Context Envelope `S`, `PhaseHint` `P1`, `ResponsibleParty` `TBD`, `CoversScopeItems` `SOW-077;SOW-094`, `SupportsObjectives` `OBJ-004`; sources `execution/_Decomposition/Deliverables.csv` row `DEL-01-06` and `SOFTWARE_DECOMP.md` §5 PKG-01 table ("| DEL-01-06 | Loop registry (local config default) | BACKEND_FEATURE_SLICE | S | P1 | SOW-077, SOW-094 |"). The folder was scaffolded under `D-PEC-62`; its `_STATUS.md` reads `INITIALIZED`. Its `MEMORY.md`, created under `D-PEC-96` from the template, holds no run row.
- **CLM-010** — The register `Description` of record reads:

> PEC-owned local configuration naming the loop locators PEC serves: one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes. The strict, versioned JSON/schema paths and core-owned typed port are the long-term home and shape under D-PEC-78; each listed loop remains authoritative for its own entrypoint and truth, and no governed act depends on PEC or the registry. Each row declares a closed, PEC-versioned feed profile (profile ID, version, live/historical, basis citation to the loop's own record), PEC's reading hypothesis and never the loop's truth; PEC's own row declares `remaining-loop` now. Feed-profile declarations need a strict schema v2 (`loops.schema.json` v2, `loops.json`, a `RegisteredLoop` field) through a later D-PEC source packet within D-PEC-78 O-A, with VER-001/VER-003 re-run: a new Scope of Work currency obligation (RF-002 stays resolved).

  ID-shaped text inside this quotation is upstream source context, not a local definition or reference. The clause "PEC's own row declares `remaining-loop` now" is stale design text: it records the SCA-005 intent, not the ruled and applied row (CON-003). The source packet it anticipates is `D-PEC-96` (CLM-015), and this contract is the currency obligation it names.
- **CLM-004** — `Loop` is the PRD v2.4 §7.1 record-tier entity: "Tenancy unit, above Project: a `LOOP_INIT.md`-governed work loop that the loop registry lists (§16.3); PEC reads only loop identity, entrypoint and procedure SHA from `LOOP_INIT.md`". The decomposition vocabulary (§9) states: "PEC serves only the loops its registry (`loops.json`) lists". Which loops exist outside the registry is not this contract's concern, and it asserts no count of them.
- **CLM-005** — Registry coverage is phase-staged. At P1 exactly one loop is registered, PEC v2's own build, per `OI-010` as resolved at Gate 2 (2026-07-24, `DL-10`) and per the register description's "one loop at P1 (PEC's own build, OI-010), extendable by owner-gated PEC configuration changes". At P2 coverage is the loops the registry lists (PRD v2.4 §12). Which further loops are listed, and when, is decided only by owner-gated PEC configuration changes; no accepted source fixes their number.

### Placement in the work graph

`DEL-01-06` is a root node of the accepted dependency DAG: `_DEPENDENCIES.md`
declares no upstream predecessors, and `Dependencies.csv` holds only three
non-gating `ANCHOR` rows (`DEP-01-06-001` package anchor, `DEP-01-06-002`
`SOW-094` requirement trace, and `DEP-01-06-003` `SOW-077` requirement trace).

- **CLM-006** — Three accepted consumer edges depend on this deliverable, all at `RequiredMaturity` `INITIALIZED` and all currently `PROPOSAL` stratum: DEL-02-07 `[E-N16]` (row `DEP-02-07-003`, `Statement` "Per-loop manifest consumption requires the registered-loop set from the loop registry"), DEL-03-01 `[E-P18]` (row `DEP-03-01-007`, `Statement` "Reconciler needs the loop registry"), and DEL-09-02 `[E-P62]` (row `DEP-09-02-006`, `Statement` "Census spans the registered loops"). Each row sits in the consumer's own register and is `ACTIVE`, `EXECUTION`, `PREREQUISITE`, `SatisfactionStatus` `PENDING`. The `[E-N16]` exhibit rationale ("DEL-02-07 reads per-project manifests per loop") predates SCA-005, which re-purposed `DEL-02-07` as a parity-peer reader. The `DEL-02-07` contract rebuilt in the same S2 packet says the reader shall "obtain the set of loops it serves only through the core-owned typed `LoopRegistry` port" (`DEL-02-07/REQ-003`), and it holds the relation between a registered loop and the project or projects whose `adapter.yaml` it reads as its unresolved `DEL-02-07/CON-002`; the applied `RegisteredLoop` carries no project field (CLM-017). That edge's currency belongs to `DEL-02-07`'s contract and to the dependency workflow, not to this contract.
- **CLM-011** — Two further contracts bind to this deliverable's port without a register edge. The `DEL-02-08` and `DEL-02-09` contracts each read feed-profile declarations "through the loop-registry port of `DEL-01-06`", and each records that no dependency row links it to this deliverable, leaving the question to the dependency workflow. They left the profile identifier and surface name open until this rebuild; CLM-016 states them.
- **CLM-012** — Phase staging, checked against the `PhaseHint` column of `Deliverables.csv` for every deliverable this contract names in its own voice: `DEL-01-06`, `DEL-01-01`, `DEL-01-03`, `DEL-01-05`, `DEL-02-01` through `DEL-02-09` and `DEL-03-01` carry `P1`, and `DEL-09-02` carries `P2`. No claim here stages any of them differently.

### Boundaries

- **CLM-013** — The acts adjacent to the registry are owned elsewhere and are cited here, never discharged. The feed grammars are the `PKG-02` parsers' (decision-log entries `DL-4` and `DL-20`): `_STATUS.md` is `DEL-02-01`'s (`SOW-011`); decision registers and packets are `DEL-02-02`'s (`SOW-012`); `LOOP_RECEIPTS.md` ledgers and central `RECEIPT.md` receipts are `DEL-02-03`'s (`SOW-013`); `STATUS.json` and `RUNTIME_SUMMARY.json` are `DEL-02-04`'s (`SOW-014`); `Dependencies.csv` and historical `WORK_GRAPH.json` are `DEL-02-05`'s (`SOW-015`); `LOOP_INIT.md` identity, entrypoint and procedure SHA are `DEL-02-06`'s (`SOW-016`); the `_harness/adapter.yaml` parity-peer read is `DEL-02-07`'s (`SOW-017`); Markdown work graphs are `DEL-02-08`'s (`SOW-095`); and the deliverable `MEMORY.md` run index is `DEL-02-09`'s (`SOW-096`). Full rebuild, which ingests each loop per its declared profile, is `DEL-03-01`'s (`SOW-010`, `SOW-021`); the lifecycle census dashboard is `DEL-09-02`'s (`SOW-046`); the record-tier Loop type is `DEL-01-01`'s (`SOW-001`); the store and its content-minimal ingest guard are `DEL-01-03`'s (`SOW-056`); and zero-dependency and locality enforcement is `DEL-01-05`'s (`SOW-052`, `SOW-053`).
- **CLM-014** — `D-PEC-78` O-A fixes the governance of the registry. PEC owns only its configured service set; each listed loop remains authoritative for its own entrypoint and truth; later row changes are owner-gated PEC configuration changes; and registry or PEC absence blocks no governed act (CLM-008). The packet it ruled states the compatibility rule in its §4.2: "Adding, removing, or changing a field's meaning requires a new schema version and a successor D-PEC migration packet. Version 1 is not silently widened. A dual-read transition, if needed, must be time-bounded and tested; unknown versions fail closed."

### Current registry (observation)

- **CLM-015** — `D-PEC-96` is the registry source packet that SCA-005 `Propagation_Plan.md` §B6 names. The owner ruled its revision 4 (SHA-256 `4506597b1bfd…180e`) on 2026-09-26 with "D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults" (`D-PEC-96_RULING_2026-09-26.md`, SHA-256 `852057f0ff69…399e`). The act commit is `c55362095`, and PR #950 merged as `73ed349ed`, an ancestor of `aca930622`. There `v2/config/loops.json` (SHA-256 `fd342b4f29ed…53d7`) carries `"schema_version": 2` and one row, `pec` → `projects/pec/loop/LOOP_INIT.md`, and `v2/config/loops.schema.json` has SHA-256 `104ed64820b7…b143`. The ruled and applied PEC row (question 2) is:

  | Profile | Version | State | Basis |
  |---|---|---|---|
  | `shared-dev-loop` | 1 | `live` | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` |
  | `loop-receipts-ledger` | 1 | `historical` | `projects/pec/AGENTS.md` |
  | `agentruns-json` | 1 | `historical` | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` |

  The ruling records the `agentruns-json` basis as the `D-PEC-94` record "by implication". The three basis paths and the `loop_init_path` exist at `aca930622`.
- **CLM-016** — The closed vocabulary at `aca930622` is three profiles, each at version 1, with these surfaces (schema option descriptions and the adapter's `FEED_PROFILE_SURFACES`): `shared-dev-loop` covers `central-receipts`, `decision-registers`, `dependency-registers`, `memory-run-index`, `status-lifecycle` and `work-graphs`; `loop-receipts-ledger` covers `receipt-ledger`; `agentruns-json` covers `json-run-evidence`. The three are pairwise disjoint. As the `D-PEC-96` proposal puts it, "`loop_init_path` is read for loop identity on every row, whatever its profiles, as PRD PEC-RCN-002 requires, so it is not a profile surface"; no profile lists a `LOOP_INIT.md` or workplan surface. No profile and no surface covers `## Remaining` sections: the owner's 2026-09-26 direction on revision 4 was "revision 4: drop remaining-items and remaining-loop", and under `D-PEC-99` `projects/pec/AGENTS.md` states "No PEC feed profile reads such sections, so the coordination plane does not scan them, and they are not a work-selection surface." PRD v2.4 §7.1 makes remaining items a per-loop optional field, read only where the loop's feed profile declares it, and no profile in this vocabulary declares it.
- **CLM-017** — The core port at `aca930622` (`v2/src/pec_v2/core/ports/loop_registry.py`, SHA-256 `a509bfb74920…c8a9`) defines `FeedProfileState` (`LIVE` = `live`, `HISTORICAL` = `historical`), a frozen `FeedProfile` with fields `profile`, `version`, `state` and `basis`, a frozen `RegisteredLoop` with fields `loop_id`, `loop_init_path` and `feed_profiles: tuple[FeedProfile, ...]`, and the `LoopRegistry` protocol whose only method is `registered_loops() -> tuple[RegisteredLoop, ...]`. The JSON adapter (`v2/src/pec_v2/adapters/config/loop_registry.py`, SHA-256 `620a173d19d8…2f07`) accepts only `schema_version` 2.
- **CLM-018** — Lifecycle and production status. The deliverable is at lifecycle `INITIALIZED`. Produced source exists: the `D-PEC-75` slice (merged as `ccd9a2178`) and the `D-PEC-96` act that changed it. Neither artifact set is accepted. `_REVIEW.md` records the owner's Gate 5 outcome as `HOLD` at `INITIALIZED`, and `Review_Findings.csv` records `RF-001` and `RF-002` as `RESOLVED`; that review predates the `D-PEC-96` act. The act's run record (`VALIDATION.md`) reports 19 tests run and passing for the registered registry check. That is run evidence, not acceptance: this contract discharges no acceptance criterion. Every requirement, acceptance criterion and verification method below states a contract on the production and its evaluation, and the produced bytes are what that evaluation will examine.
- **CLM-019** — `SOW-077` and the register description say each row declares "a closed, PEC-versioned feed profile", in the singular, while `SOW-094` speaks of "each row's feed-profile selection". The `D-PEC-96` proposal (its finding 1) made `feed_profiles` a list, because the migration the accepted records foresee already needs more than one entry on a row, and the owner confirmed that shape under question 3. This contract follows the confirmed list reading; no conflict remains open on it.
- **CLM-020** — The stale design text. SCA-005 checkpoint-1 answer `SCA005-CP1-Q8` (a) and `Propagation_Plan.md` §B6 gave PEC's row the `remaining-loop` profile. `D-PEC-96` question 2 ruled PEC's row migrated, as the one owner-gated row change those records foresaw, departing from their wording for PEC's row only. Three decomposition surfaces still carry the earlier wording at `aca930622`: the second sentence of the `SOW-094` `Notes` cell ("PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7)"), the register description's clause quoted in CLM-010, and the §9 vocabulary example for "feed profile", which lists "e.g. `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger`, `agentruns-json`". Each is quoted here as stale design text. The post-change audit records them as `COV-083`, and `_Decomposition/_LATEST.md` states that they are "carried knowingly for a later PEC scope change".
- **CLM-021** — SCA-005 `Propagation_Plan.md` §B4 records a carry-forward for the parser contracts:

> Carry-forward for the parser SOWs (DEL-02-01, DEL-02-08, DEL-02-09): the
> DEL-01-03 content-minimal guard admits only `OPEN`..`ISSUED` as STATE values
> (true before and after D-PEC-87/89/91), so `RETIRED`, graph node states and
> run tokens are CON-001 cases those SOWs must address.

  ID-shaped text inside this quotation is upstream source context, not a local definition or reference; the constraint it cites is `DEL-01-03/CON-001`. The produced but unaccepted guard source (`v2/src/pec_v2/core/content_minimal_guard.py`, SHA-256 `740a4a741221…19ee9`; `DEL-01-03` is `IN_PROGRESS`) admits five field classes (path, count, SHA, state, hash) and a state set of `OPEN` through `ISSUED`.

- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation.
- **TBD-003** — Path normalization is not fully fixed. The rule shared by `loop_init_path` and `basis` rejects absolute paths, `..` segments and backslashes, and it accepts forms such as `projects/./pec/x`, `projects//pec/x`, a trailing `/`, a leading space and `C:x` (the `D-PEC-96` proposal's finding 3, inherited from version 1). Whether to tighten it is open; the responsible party is a later owner-ruled D-PEC packet.
- **TBD-004** — The schema text does not state every rule the adapter enforces: `loop_id` uniqueness, the `loop_init_path` normalization rule, and the rejection of `2.0` and `1.0`, which JSON Schema `integer` admits, are enforced but not described (`D-PEC-96` verifier verdict 01, note N3, carried as residual 9 of its handoff). Whether the schema text is completed is open; the responsible party is a later owner-ruled D-PEC packet.
- **TBD-005** — The loader validates the form of `loop_init_path` and `basis`, not the existence of their targets. `D-PEC-78` O-A's packet §4.4 requires PEC to report the located failure when "a target entrypoint is absent or invalid" and to serve no false data for that row. Which deliverable reports an absent target at run time is fixed by no accepted contract; the undertaking graph and its owner decide it.

## Completion and Reliance Basis — Epistemology

The requirements below state what the production must satisfy. Nothing in this
section asserts that a requirement is met.

- **REQ-001** — The configuration shall be strict at schema version 2. The document shall hold exactly `schema_version` and a non-empty `loops` array. Each row shall hold exactly a stable lower-case `loop_id` (pattern `^[a-z][a-z0-9-]*$`), a normalized repository-relative `loop_init_path` locating that loop's own file truth, and the `feed_profiles` list of REQ-008. Missing fields, unknown fields, duplicate identifiers, and absolute, traversing or backslash-bearing paths shall fail with located errors.
- **REQ-002** — The registry shall be delivered as a local configuration file with a checked-in default instance, per the "local config default" wording of `SOW-094`, which `DL-14` created as a replaceable local-config default (AX-003).
- **REQ-003** — The loader shall reject a configuration that does not validate and shall state the failure explicitly, naming the offending entry or field by its location in the document; silent omission and silent substitution of a partial or empty loop set are prohibited, consistent with `PEC-ORI-006`. No failure message shall echo a document value, except a profile identifier or surface name already validated against the closed vocabulary.
- **REQ-004** — The loader shall expose the registered-loop set to the record-tier consumers declared in CLM-006 through a stable in-process interface.
- **REQ-005** — Consumers shall depend only on the core-owned typed `LoopRegistry` port and shall not depend on the registry's JSON paths, serialization, or adapter errors. The selected schema-version-2 JSON/schema files remain replaceable behind that port; a path, schema, or field-meaning change requires a separately governed migration without amending DEL-02-07, DEL-03-01, or DEL-09-02 merely for adapter details.
- **REQ-006** — The registry format, default instance, and loader shall introduce no third-party runtime dependency and no external network egress, per `PEC-SVC-001` and `PEC-SVC-002`, whose standing enforcement is `DEL-01-05` covering `SOW-052` and `SOW-053`.
- **REQ-007** — Tests shall implement the verification methods declared in this contract; they shall not define scope, requirements, or acceptance criteria.
- **REQ-008** — Each row's `feed_profiles` shall be a non-empty list of entries, each holding exactly `profile`, `version`, `state` and `basis`: `profile` an identifier from the closed vocabulary of REQ-010; `version` an exact integer in that profile's supported version set; `state` exactly `live` or `historical`; and `basis` a citation to the loop's own record, as a normalized repository-relative path under the rule of REQ-001. A profile identifier shall appear at most once per row. Each violation shall fail at the location of the offending entry or field, and an empty list at the row's `feed_profiles`.
- **REQ-009** — The profiles declared on one row shall cover pairwise-disjoint surfaces, so that no surface is read under two grammars or declared both live and historical, and at least one profile per row shall be `live`. An overlap shall fail at the later entry's `profile`, naming the surface and the earlier entry; a row with no live profile shall fail at its `feed_profiles`. Both rules shall be enforced when the configuration is loaded, not left to the parsers.
- **REQ-010** — The feed-profile vocabulary shall be closed and PEC-versioned: `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1, with the surface lists of CLM-016. The schema shall state each profile's surface list, and the schema's profile set, versions, states and surface lists shall equal the adapter's and the port's. No profile or surface shall cover `## Remaining` sections. Adding a profile, version or surface shall be a PEC code change under an owner-ruled D-PEC packet within schema version 2; a loop never declares vocabulary. Path conventions and grammars for each profile stay with the parsers (REQ-014).
- **REQ-011** — The loader shall accept exactly `schema_version` 2. A version-1 document, or any other version, shall fail at `$.schema_version` with a located error; it shall never be read, defaulted or migrated in memory, and no dual read is provided.
- **REQ-012** — `RegisteredLoop` shall carry a required `feed_profiles: tuple[FeedProfile, ...]` field with no default. The core shall own immutable `FeedProfile` (`profile`, `version`, `state`, `basis`) and `FeedProfileState` (`live`, `historical`) types. The port method `registered_loops() -> tuple[RegisteredLoop, ...]` shall keep its signature, and the core shall import no JSON, filesystem or adapter module.
- **REQ-013** — Each row of the checked-in default instance, including every feed-profile entry, shall be the row as last set by an owner ruling. Adding, removing or retargeting a row, or changing a row's profiles, states or bases, is an owner-gated PEC configuration change under an owner-ruled D-PEC packet. At the observation commit the ruled and applied PEC row is the `D-PEC-96` question-2 row of CLM-015.
- **REQ-014** — The registry shall parse no feed owned by a sibling deliverable and shall perform no act owned by another package. It shall parse no file of a registered loop and hold no grammar for one: no `_STATUS.md` (`DEL-02-01`), decision register or packet (`DEL-02-02`), ledger or central receipt (`DEL-02-03`), run-evidence JSON (`DEL-02-04`), dependency register or `WORK_GRAPH.json` (`DEL-02-05`), `LOOP_INIT.md` (`DEL-02-06`), `adapter.yaml` (`DEL-02-07`), work graph (`DEL-02-08`) or `MEMORY.md` (`DEL-02-09`). It shall perform no ingest or rebuild (`DEL-03-01`), census rendering (`DEL-09-02`), record-tier typing of Loop (`DEL-01-01`), store write or ingest guarding (`DEL-01-03`), or dependency and locality enforcement (`DEL-01-05`). Each is cited to its owner in CLM-013.

- **AC-001** — The configuration format documents every field it defines, names each served loop with a stable identifier, and is validatable deterministically, with a valid instance accepted and every malformed fixture rejected.
- **AC-002** — The checked-in default instance registers exactly one loop at P1, identified as PEC v2's own build per OI-010, and admits further loops by adding rows only, with no schema change and no row that an owner ruling has not set.
- **AC-003** — The loader rejects an invalid or unreadable configuration with an explicit failure that names the offending entry or field, and never returns a silently defaulted, partial, or empty loop set in its place.
- **AC-004** — The loader exposes the registered-loop set through an interface whose signature carries no configuration path or serialization detail, so that relocating or reshaping the registry changes no consumer deliverable.
- **AC-005** — The format, the default instance, and the loader add no third-party runtime dependency and make no network call, leaving the DEL-01-05 zero-dependency and locality assertion intact.
- **AC-006** — The automated test suite implements VER-001 through VER-005 and VER-007 through VER-014, executes in the service-core test run, passes, and introduces no acceptance criterion absent from this contract.
- **AC-007** — Each malformed feed-profile case (an empty list, a missing or unknown entry field, an identifier outside the vocabulary, a repeated identifier, a non-integer or unsupported version, a state other than `live` or `historical`, and a non-normalized `basis`) is rejected at its location, and a valid entry is returned as a typed `FeedProfile`.
- **AC-008** — Each overlap kind (one surface both live and historical, two live readers of one surface, two historical grammars for one surface) is rejected at the later entry, naming the surface and the earlier entry; a row with no live profile is rejected at its `feed_profiles`; and a row of disjoint profiles with one live profile loads.
- **AC-009** — The schema's profile set, versions, states and per-profile surface lists equal the adapter's and the port's; the shipped profiles are pairwise disjoint; and neither the schema nor the adapter names a `## Remaining` surface or a profile outside the three.
- **AC-010** — The version-1 fixture and every other version value fail at `$.schema_version`, and no loop set is returned.
- **AC-011** — `RegisteredLoop` carries the required typed `feed_profiles` field; `FeedProfile` and `FeedProfileState` are core-owned and immutable; the port method's signature is unchanged; and the core imports only standard-library modules with no I/O module.
- **AC-012** — Every row and feed-profile entry of the checked-in default matches the owner ruling that last set it (for PEC's row, `D-PEC-96` question 2 unless a later ruling changes it), and each `loop_init_path` and `basis` names a file present at the evaluated commit.
- **AC-013** — The registry module parses no file of a registered loop, holds no feed grammar, and performs none of the excluded acts of REQ-014.
- **AC-014** — No failure message echoes a document value other than a validated vocabulary identifier or surface name.
- **AC-015** — The review gate confirms this contract's traceability to `SOW-077`, `SOW-094` and `OBJ-004`, confirms the objective attribution is stated no more strongly than the objective warrant states it, confirms the current registry row is stated as the ruled and applied row with the stale design text of CON-003 labelled as such, and confirms no sibling feed grammar, `PKG-03` rebuild or `PKG-09` census scope has been absorbed.

- **CON-002** — **Guard admission.** Registry values — `loop_id` tokens, profile identifiers and versions, the `live` and `historical` states, and surface names — are outside the produced guard's admitted classes as typed: they are not paths, counts, SHAs, hashes or `OPEN`..`ISSUED` states (CLM-021). The registry writes nothing to the store (REQ-014). Where a consumer persists such a value, it is a `DEL-01-03/CON-001` case, and its record-tier typing belongs to `DEL-01-01`. The `DEL-01-01` contract rebuilt in the same S2 packet types identifiers carried as field values and source-generation labels as their own kinds (`DEL-01-01/REQ-017`), records the store-admission side as `DEL-01-01/CON-003`, and leaves open whether its Loop type refers to a registry row's feed-profile selection (`DEL-01-01/TBD-005`). This contract shall not coerce a profile state into a lifecycle state, encode a token to pass the guard, or widen the guard; how the store admits these values is decided under `DEL-01-03` and `DEL-01-01`, through their own packets.
- **CON-003** — **Stale design text.** The `SOW-094` `Notes` cell, the register description and the §9 vocabulary example still give PEC's row the `remaining-loop` profile, while the ruled and applied row is the migrated three-profile row, and `remaining-loop` is no longer in the vocabulary (CLM-015, CLM-016, CLM-020). This contract states the ruled row and treats that decomposition text as stale design text. It edits no decomposition surface; the correction belongs to a later PEC scope change, as the owner's checkpoint-3 answer carried it.

## Production and Verification Method — Praxeology

The source this contract governs already exists as produced, unaccepted bytes
(CLM-018). Further production is a change to them: each change needs an
owner-ruled D-PEC packet naming the exact paths, acts, verification and
rollback, because the PEC source fence opens no path by itself. This contract
authorizes no register, decomposition, PRD, registry-row or source edit.
Evaluation checks the format, the default instance, the loader and the tests,
in that order, because each is the acceptance surface of the next. Tests
implement the verification methods below and create no scope.

- **VER-001** — Validate the documented format against the checked-in default instance and against a fixture set of deliberately malformed configurations; the valid instance validates and every malformed fixture is rejected with a located failure.
- **VER-002** — Inspect the default instance and assert exactly one registered loop at P1 whose identity is PEC v2's own build, then confirm by construction that adding further loops requires new rows only and no schema change.
- **VER-003** — Execute the loader against invalid, unreadable, and absent configuration fixtures and assert an explicit located failure in each case, with no fallback, partial, or empty loop set returned.
- **VER-004** — Exercise the loader's consumer-facing interface, assert the returned loop set matches the configuration, and inspect the interface signature for configuration-path or serialization leakage.
- **VER-005** — Inspect the service-core dependency manifest and the registry module import graph for third-party runtime dependencies and network calls, and re-run the DEL-01-05 locality and zero-dependency enforcement once that deliverable is available.
- **VER-006** — Run the service-core test suite and confirm that each of VER-001 through VER-005 and VER-007 through VER-014 has a corresponding executing automated test and that no test asserts a criterion absent from this contract.
- **VER-007** — Execute the loader over one fixture per malformed feed-profile case of AC-007 and over a valid entry; assert each failure location and the typed `FeedProfile` returned for the valid entry.
- **VER-008** — Execute the loader over rows exhibiting each overlap kind, using probe profiles added to the vocabulary for the test only and removed afterwards, over a row with no live profile, and over a disjoint control row; assert each failure location and message and the control row's acceptance.
- **VER-009** — Compare the schema's profile options, version, states and surface lists with the adapter's vocabulary and surface maps and the port's state type; assert pairwise disjointness of the shipped profiles; scan the schema and the adapter for any `## Remaining` surface or dropped profile identifier.
- **VER-010** — Execute the loader over the version-1 fixture and over documents with other version values; assert the `$.schema_version` failure and that no loop set is returned.
- **VER-011** — Inspect the port's type definitions and method signature, assert immutability of `RegisteredLoop` and `FeedProfile`, and inspect the core's imports.
- **VER-012** — Compare the default instance row by row and entry by entry with the owner rulings that set them, and check that each `loop_init_path` and `basis` names a file present at the evaluated commit.
- **VER-013** — Inspect the registry module's file access and call surface for any parse of a registered loop's files, any feed grammar, and any of the excluded acts of REQ-014.
- **VER-014** — Execute failure cases carrying distinctive document values in every field and assert that no failure message contains them.

## Governing Values and Decisions — Axiology

- **AX-001** — `PEC-K-01` graceful absence governs: no governed act may require a PEC read or write. The registry is PEC-internal configuration; naming a loop confers no authority over it, and its absence blocks nothing outside PEC.
- **AX-002** — `PEC-K-02` files govern: the registry records where each loop's file truth is read from and never becomes an alternative source of truth about a loop. Registry contents are not citable as authority.
- **AX-003** — Lineage. `DL-14` (Phase 6 adversarial verification, applied at revision 0.9) created `SOW-094` and `DEL-01-06` as a replaceable local-config default so P1 could proceed. `D-PEC-78` O-A then selected the existing PEC-owned JSON/schema paths and core-owned typed port as the long-term architecture, and SCA-004 `DL-19` propagated that ruling into `SOW-077` and this deliverable without changing source or dependency topology. SCA-005 `DL-20` added the per-row feed-profile declarations and the schema-version-2 obligation to both items and to the register description (amendment actions A-10, A-11 and A-13), and its §B4 classed the earlier contract as needing a rebuild gated on the §B6 source packet. `D-PEC-96` is that packet, and this contract is the rebuild. SCA-006's Impact Assessment §7.1 classes this deliverable `NOT_AFFECTED`.
- **AX-004** — Gate 2 (2026-07-24, `DL-10`) resolved `OI-010`: the first loop the P1 reconciler ingests is PEC v2's own build, the §12 closing paragraph governing over the P1 table's "(piping or root)" parenthetical. The P1 registry default follows that ruling.
- **AX-005** — `C-04` PHASE_PRECEDENCE and `C-10` STRATUM_RULE are register-wide non-gating constraints. The P1→P2 coverage step is release-strategy ordering. The consumer edges in CLM-006 are `PROPOSAL` stratum and are accepted: `D-PEC-62` §1(4) accepted the candidate v0.2 exhibit "all strata as presented", reading acceptance as carrying the exhibit's flags as flags, so what remains recorded-but-unresolved is the specific annotated set (E-A11, E-P69/E-N02, E-N13/E-N18, C-02 direction, C-08 standing-node set) — none of which touches E-N16, E-P18, or E-P62. Stratum is provenance, not authority; it records how an edge was derived, not whether it has been accepted.
- **AX-006** — A feed profile is PEC's reading hypothesis, never the loop's truth (PRD §16.3). The registry declares how PEC reads a loop; the parsers read. A `historical` profile marks a frozen generation whose silence is never reported as staleness, so declaring the state correctly is what keeps a closed ledger from being reported as a stale one.
- **AX-007** — Versions fail closed (CLM-014). A version-1 file cannot meet `SOW-077`, which asks every row to declare a profile: reading one would mean inventing a profile, which REQ-003 forbids as silent substitution, or returning loops without one. The one version-1 document was the checked-in default, which the `D-PEC-96` act migrated. The proposal recorded that "PEC runs nowhere, and no store or consumer holds registry data", and at `aca930622` the only files under `projects/pec/v2` that name `RegisteredLoop` are the registry's own port, adapter, package re-exports and tests. No dual read is needed.
- **AX-008** — Coherence is checked at load (REQ-009) because the registry is the single declaration point. If each parser resolved overlaps itself, each would need its own precedence rule: a hidden policy, applied late and possibly differently per parser. The overlap rule has no shipped case to fire on, and it stays as the guard against a later vocabulary change that introduces one.
- **AX-009** — PEC's `## Remaining` sections are retired under `D-PEC-99` and are not read (CLM-016). This contract presents no such section as a surface and gives the registry no way to declare one.
- **AX-010** — Unknowns stay marked. TBD-001, TBD-003 through TBD-005, CON-002 and CON-003 are recorded rather than resolved by inference; a production choice that settled a CON item would be a decision taken in the wrong place.
- **AX-011** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by the run that authored this document. The rebuild accepts no artifact, re-enters no review gate, and reopens neither `RF-001` nor `RF-002`.
- **AX-012** — Rebuild provenance. This contract replaces, as a whole, the prior contract with SHA-256 `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8` (revision-1.4 basis). It is that contract's rebuild under the S2 Scope of Work rebuild packet (provisional `D-PEC-100`). Retired IDs, cited here in qualified form against the prior contract: `DEL-01-06/CLM-007` (lifecycle with no implementation present; superseded by CLM-018), `DEL-01-06/TBD-002` (the registry home and shape, recorded as resolved; now CLM-008 and CLM-014) and `DEL-01-06/CON-001` (the `D-PEC-78` O-A resolution recorded as a conflict; now CLM-014 and AX-007). Kept IDs keep their meaning, with their text brought to the current basis; new IDs take the next unused number for their prefix.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-077 SOW-094 OBJ-004 | REQ-001, CLM-004, TBD-003, TBD-004 | AC-001 | VER-001 | Format documentation, the checked-in default instance, the malformed-fixture set, and validation output showing accept/reject per fixture |
| OUT-001 | SOW-077 SOW-094 OBJ-004 | REQ-002, CLM-005, AX-004 | AC-002 | VER-002 | The checked-in default instance and the rows-only extension result |
| OUT-001 | SOW-077 SOW-094 OBJ-004 | REQ-006 | AC-005 | VER-005 | Dependency-manifest plus import-graph inspection records |
| OUT-001 | SOW-077 SOW-094 OBJ-004 | REQ-010, CLM-016, AX-009 | AC-009 | VER-009 | Schema-to-adapter-to-port vocabulary comparison, the disjointness result, and the scan result |
| OUT-001 | SOW-077 SOW-094 OBJ-004 | REQ-013, CLM-015, CLM-020, CON-003, TBD-005 | AC-012 | VER-012 | Row-by-row comparison of the default instance with the owner rulings, and path-presence results at the evaluated commit |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-003, AX-007 | AC-003 | VER-003 | Loader failure-path transcripts |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-003 | AC-014 | VER-014 | Failure messages for distinctive-value fixtures, with the no-echo result |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-004, REQ-005, CLM-006, CLM-011 | AC-004 | VER-004 | The consumer-facing interface signature |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-006 | AC-005 | VER-005 | Dependency-manifest plus import-graph inspection records |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-008, CLM-019 | AC-007 | VER-007 | Per-case feed-profile failure transcripts and the typed valid entry |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-009, AX-008 | AC-008 | VER-008 | Overlap, no-live and control transcripts, with evidence that the probe profiles were removed |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-011, CLM-014, AX-007 | AC-010 | VER-010 | Version-1 and other-version failure transcripts |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-012, CLM-017 | AC-011 | VER-011 | Port type and signature inspection record and the core import inspection |
| OUT-002 | SOW-077 SOW-094 OBJ-004 | REQ-014, CLM-013, CLM-021, CON-002 | AC-013 | VER-013 | File-access and call-surface inspection records |
| OUT-003 | SOW-077 SOW-094 OBJ-004 | REQ-007, CLM-018, TBD-001 | AC-006 | VER-006 | Service-core test-run output mapping each executed test to its declared verification method |
| OUT-001 | SOW-077 SOW-094 OBJ-004 | CLM-001, CLM-002, CLM-003, CLM-008, CLM-009, CLM-010, CLM-012, AX-001, AX-002, AX-003, AX-005, AX-006, AX-010, AX-011, AX-012 | AC-015 | HUMAN_REVIEW: review gate confirms traceability to SOW-077, SOW-094 and OBJ-004, confirms the indirect objective attribution is stated no more strongly than the warrant, confirms the ruled and applied registry row with CON-003's stale design text labelled, and confirms no sibling, PKG-03 or PKG-09 scope absorption | Review record citing the ledger rows, the §3 objective row, the D-PEC-96 ruling and the sibling boundaries |
