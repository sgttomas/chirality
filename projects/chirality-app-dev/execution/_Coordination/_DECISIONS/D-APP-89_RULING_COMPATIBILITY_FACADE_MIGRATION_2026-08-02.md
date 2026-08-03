# D-APP-89 — Ruling: Compatibility-Facade Migration Cycle

Status: `RULED — OPTION B`

DecisionID: `D-APP-89`

Date: `2026-08-02`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Selected proposal:
`execution/_Coordination/_DECISIONS/D-APP-89_PACKET_COMPATIBILITY_FACADE_RETIREMENT_2026-08-02.md`
at SHA-256
`7dc274ac9d8d081947420c2155954adef9e5f0d2987e8e0913c0b84f8eabb8dc`.

Task Management link: `TM-APP-031` (maintenance remains a separate
`TASK_MANAGEMENT` act).

## Exact owner ruling

The owner returned exactly:

> APPROVE D-APP-89 OPTION B

No omitted retirement approval, deletion authority, Root act, or broader
effect is inferred.

## Selected semantics

Option B is selected exactly as proposed. The App loop may execute one bounded
migration-only tranche that moves every current executable App importer and
build/config consumer from `@chirality/harness-contract` to the equivalent
Root-owned `@chirality/runtime-contracts` root or subpath.

The compatibility facade remains present and tested as the rollback path
through this migration cycle. This ruling does not authorize facade deletion
or close DEL-03-01 / `TM-APP-031`. Retirement returns to a later owner gate
only after the migration lands and a fresh execution-time census and evidence
package satisfy D-APP-76.

## Required return

The migration tranche must provide the selected packet's:

- path-complete before/after consumer census;
- facade-to-Root export/subpath mapping;
- exact edited-path manifest and SHA-256 values;
- source-versus-reliance distinctions preserving historical records;
- affected-client evidence;
- tested rollback procedure;
- Root package build/typecheck and focused export probes;
- App test, typecheck, contract-dependency, build, and package evidence; and
- release/no-reliance disposition.

Any missing Root export, consumer ambiguity, affected-client conflict, or
failed rollback/validation proof stops the migration fan-in without deleting
the facade.

## Later retirement gate

The later retirement packet must bind to a fresh execution-time zero-consumer
census, exact deletion and rollback bytes, affected-client evidence, Root/App
build and focused tests, release disposition, and the applicable Root and App
owner rulings required by D-APP-76. Elapsed time or the present packet-time
census cannot substitute for that gate.

## Preserved boundaries

- D-APP-49, D-APP-73, and D-APP-76 remain immutable historical/routing
  authority; D-APP-48 successor identity is not resolved.
- No Root runtime semantic, generic contract, Agent-2 Bash, provider/network,
  lifecycle, Checking Approval SHA, release, distribution, publication, or
  professional-reliance act is authorized.
- Task Management register maintenance remains outside this ruling tranche.
- The six D-APP-81 historical relations remain
  `HISTORICAL_RELATION_UNKNOWN`.

## No-effect boundary

Recording this ruling changes no import, package, config, lockfile, facade,
Root runtime, deliverable/state, Task Management, receipt, commit, push, or
merge byte. It authorizes only the migration-only Option B tranche, with the
facade retained and retirement separately gated.
