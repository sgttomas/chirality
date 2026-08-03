# D-PEC-78 decision packet — OI-003 loop-registry home and shape

**Packet state:** AWAITING_RULING / NO REGISTRY-HOME SELECTION

**Decision:** D-PEC-78

**Prepared:** 2026-08-02

**Presentation basis:** `97678a841ef58345c73d3470ed8de57c9b1405d2`

**Owning loop:** PEC

**Task Management route:** `TM-PEC-010`

## 1. Question and authority boundary

What is the long-term governed home and typed shape of the registry naming the
loops PEC serves?

This packet presents three faithful choices without selecting one:

1. retain the existing PEC-owned typed registry as the long-term service
   configuration;
2. adopt a shared declaration contract with loop-owned declarations while PEC
   retains a separate local service-selection list; or
3. keep the current local file explicitly replaceable and defer the long-term
   decision under a sharper trigger.

The question is not where other loops' authority lives. Each loop's own files
remain authoritative for that loop. A registry row is only a locator PEC may
serve; it grants PEC no ruling, lifecycle, write, dispatch, cadence, or
conformance authority over the named loop. No governed act may depend on the
registry or on PEC.

This packet is a product-decision interface only. It authorizes no source,
schema, configuration, declaration, foreign-loop, decomposition, SCA,
consumer, lifecycle, artifact-acceptance, release, or professional-reliance
act before the owner rules and the owning successor instruments open them.

## 2. Routed authority and accepted basis

| Basis | SHA-256 |
|---|---|
| Task Management owner ruling | `ce96dcaf8f73b9c9cb6963b372fc72df3080378bd9ccc9d8551efd41583efe78` |
| routed request `REQUEST_TM-PEC-010_OI-003_PACKET.md` | `3ff95f9a38a86f11e715faa0144df83109c3c34ed92ec1d568f75d6492829169` |
| routed controlling draft | `ebecf0ac1f00230966152fe9b3855e51711cbc95d9c73f64f463909f3752efcb` |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv`, including SOW-077 | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| accepted DEL-00-01 ADRs | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |
| D-PEC-75 execution handoff | `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` |
| current `projects/pec/v2/config/loops.json` | `e24db354841e1b33d3ec4f74330351deaa7a18df0e0cd9e26bde248b6aed503e` |
| current `projects/pec/v2/config/loops.schema.json` | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` |
| current core port | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` |
| current JSON adapter | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` |

PRD §16.3 asks for the home and shape of the loop registry and says none of
the §16 questions blocks P0–P2. Accepted `SOW-077` remains `TBD`; OI-003's
closing action is a §16 owner ruling. `SOW-094` separately authorizes the
replaceable local default implemented by DEL-01-06 and expressly leaves the
long-term decision open.

The present local default is schema version 1 with exactly one PEC row:
`loop_id: "pec"` and
`loop_init_path: "_DomainEngines/pec/LOOP_INIT.md"`. The immutable core value
is `RegisteredLoop(loop_id, loop_init_path)`, exposed through the core-owned
`LoopRegistry.registered_loops()` port. The JSON path, serialization, and
adapter error do not enter that port.

The accepted hexagonal ADR makes that separation deliberate: adapters may be
replaced while the core depends inward on a typed capability contract. It does
not choose a universal shared-types package or impose architecture on another
loop.

## 3. Decision principles common to every option

1. **Two authorities remain distinct.** A loop owns its own identity,
   entrypoint, and governed truth. PEC owns only its choice of which locators
   it attempts to serve.
2. **Typed and versioned.** Every accepted shape has an explicit version,
   strict validation, located failures, compatibility rules, and a governed
   migration path.
3. **Graceful absence.** A missing registry, missing declaration, invalid
   entry, or absent PEC yields a located PEC limitation; it never blocks the
   named loop or another governed act.
4. **No implied uptake.** Listing a loop creates no consumer enablement,
   polling cadence, data injection, dashboard duty, or receiving-loop work.
5. **Files govern.** PEC output is never authority. A locator is verified
   against the cited live file before use.
6. **Separate propagation.** A D-PEC-78 ruling records the product decision;
   it does not edit accepted decomposition. Any SOW-077/OI-003 propagation
   routes through `SCOPE_CHANGE`, and any foreign write requires the receiving
   loop's own instrument.

## 4. Option O-A — PEC-local long-term service registry (recommended)

### 4.1 Authority owner and source of truth

Confirm the existing PEC-owned paths as the long-term registry home:

- `projects/pec/v2/config/loops.json`; and
- `projects/pec/v2/config/loops.schema.json`.

The config file governs only the set of locators PEC is configured to serve.
For each row, `loop_init_path` points to the named loop's own governed
entrypoint, which remains authoritative over its contents and current state.
PEC never becomes authoritative for the loop merely because its locator
appears here.

### 4.2 Typed contract and compatibility

Retain schema version 1 and the current core contract:

```text
RegisteredLoop(loop_id: str, loop_init_path: str)
LoopRegistry.registered_loops() -> tuple[RegisteredLoop, ...]
```

Version-1 JSON remains an exact object with `schema_version: 1` and a nonempty
`loops` array. Each row has only a stable lower-case `loop_id` and normalized
repository-relative `loop_init_path`; duplicate IDs, missing fields, unknown
fields, absolute/traversing paths, unreadable files, and unknown versions fail
with located errors.

- Adding a valid row is shape-compatible but changes PEC's configured service
  set and therefore remains an owner-gated PEC configuration change.
- Removing or retargeting a row is shape-compatible but changes service
  coverage and requires the same review and exact-hash acceptance.
- Adding, removing, or changing a field's meaning requires a new schema
  version and a successor D-PEC migration packet. Version 1 is not silently
  widened. A dual-read transition, if needed, must be time-bounded and tested;
  unknown versions fail closed.

### 4.3 Proposal, validation, acceptance, and removal

While `F-PEC-1` remains the outer fence, a later loop entry is proposed
through a D-PEC packet naming the exact row, locator, receiving-loop evidence,
tests, rollback, and non-effects. No foreign-loop write is needed. The owner
accepts the exact config/schema/test bytes only after deterministic schema and
adapter contract tests and REVIEW.

Removal follows the same PEC-local path. Removing a row stops PEC from serving
that locator but does not disable, retire, or alter the loop itself. Rollback
restores only the prior PEC config bytes through a forward governed change.

### 4.4 Read/write, absence, migration, and consumers

PEC reads the local config through the replaceable adapter; no other loop
writes it. The core port remains independent of JSON and filesystem details.
If the file or a target entrypoint is absent or invalid, PEC reports the
located failure and serves no false data for that row; manual/file-native loop
operation continues unchanged.

No current DEL-01-06 source change is required to confirm O-A. The ruling
would settle the upstream product question but would not directly change
accepted `SOW-077`/OI-003 bytes. A separate SCOPE_CHANGE intake must propagate
the settled decision before any later contract relies on OI-003 as closed.
Future P2 consumers continue to use the core-owned port and require their own
source packets and acceptance gates.

### 4.5 Why O-A is recommended

The registry answers a PEC-local consumer question: which file-truth locators
PEC chooses to serve. The current typed port already provides replaceability
and application isolation. Keeping the service set local avoids creating a
cross-loop publication duty or shared availability dependency while preserving
typed contracts at PEC's boundary. It is the smallest long-term authority
shape consistent with the user's interchangeable-application intent.

## 5. Option O-B — shared declaration contract plus loop-owned contributions

### 5.1 Authority split and prospective homes

Adopt a two-layer model:

1. a Root-owned, language-neutral declaration contract at the prospective
   path
   `runtime/packages/contracts/schemas/loop-declaration.v1.schema.json`; and
2. one optional declaration owned by each loop at its own coordination home:
   - Root: `execution/_Coordination/LOOP_DECLARATION.json`;
   - App: `projects/chirality-app-dev/loop/LOOP_DECLARATION.json`;
   - Piping: `projects/chirality-piping/loop/LOOP_DECLARATION.json`;
   - PEC: `_DomainEngines/pec/LOOP_DECLARATION.json`; and
   - Bridge: `_DomainEngines/bridge/LOOP_DECLARATION.json`.

PEC would still retain a PEC-owned service-selection file at
`projects/pec/v2/config/loops.json`, but a successor schema would list
declaration paths rather than duplicating another loop's identity fields.
Thus each loop owns what it declares; PEC owns whether it consumes that
declaration.

All paths in this section are prospective only. D-PEC-78 cannot create or
authorize any of them.

### 5.2 Typed contracts and compatibility

Each declaration-v1 object would carry exactly:

```json
{
  "schema_version": 1,
  "loop_id": "pec",
  "loop_init_path": "_DomainEngines/pec/LOOP_INIT.md"
}
```

The shared JSON Schema is the contract of interchange; each loop's accepted
file is the source of its own declared fields. PEC's successor local registry
would carry its own version plus a nonempty ordered set of normalized
repository-relative `declaration_path` values. PEC's adapter validates both
layers and maps them inward to the unchanged semantic
`RegisteredLoop(loop_id, loop_init_path)` core value.

Unknown versions, duplicate IDs, duplicate declaration paths, missing files,
invalid locators, and contract-hash mismatches fail with located errors. An
additive declaration field is not visible to a strict v1 consumer until a
new compatible contract version and consumer support are accepted. Meaning
changes or removals require a major successor and explicit dual-read or atomic
cutover plan. No loop is required to publish every version merely because the
shared contract exists.

### 5.3 Proposal, validation, acceptance, and removal

- Root, through HELPS_HUMANS and its own owner-ruled shared-contract
  instrument, would own the schema bytes, compatibility suite, and version
  policy.
- Each loop would separately decide whether to adopt, amend, or decline its
  own declaration under its own packet route. A PEC ruling cannot perform that
  act for it.
- PEC would separately decide whether to add an accepted declaration path to
  its service-selection config. Publication by a loop does not force PEC
  consumption; PEC selection does not force loop publication.
- A loop may remove or supersede its declaration under its own authority.
  PEC then reports absence/staleness and may remove its local reference under
  a PEC packet. Neither act disables the loop.

Reciprocal notices must cite the D-PEC-78 ruling, shared-contract hash, each
loop-local adoption record, and the exact PEC selection evidence. Notices are
coordination only and are drafted in PEC but dispatched only by the owning
cross-loop instrument.

### 5.4 Absence, migration, rollback, and consumers

The current inline schema-v1 local default remains the fallback until the
shared schema, at least the PEC declaration, the successor PEC adapter, and
the migration tests are separately accepted. Missing foreign declarations
are normal absence and create no receiving-loop failure. A failed migration
restores PEC's prior local adapter/config through a forward change; no foreign
declaration is a rollback target.

O-B settles the product direction but requires:

1. a Root-owned shared-contract decision and production instrument;
2. separately accepted loop-local declaration choices;
3. a PEC SCOPE_CHANGE intake propagating SOW-077/OI-003;
4. a successor exact-path D-PEC migration packet for DEL-01-06; and
5. later consumer packets.

It therefore creates more interoperability machinery and coordination than
O-A, but it gives each loop a typed, self-owned declaration that any conforming
consumer—not only PEC—could adapt.

### 5.5 Tradeoff relative to O-A

O-B most directly expresses a federation of interchangeable applications
through a shared typed contract. Its cost is a shared contract owner, five
independent adoption decisions, version-skew handling, and more failure modes.
It is faithful and viable, but it is not required merely to keep PEC's own
adapter replaceable and would be disproportionate if PEC is the only actual
consumer.

## 6. Option O-C — retain the replaceable default and defer

Make no long-term home or shape selection. The current version-1 PEC-local
file remains an explicitly replaceable P1 default under SOW-094, containing
only PEC. `SOW-077` and OI-003 remain open.

Replace the now-fired “owner initiates §16 ruling” Task Management trigger
with this sharper trigger:

> Reopen before the first non-PEC loop entry is proposed for
> `projects/pec/v2/config/loops.json`, or before any P2 consumer is authorized
> to rely on a stable long-term registry home or shape, whichever occurs first.

No later-loop activation, consumer duty, cross-loop authority, inferred
permanence, or decomposition change follows. This option is lawful because the
PRD says OI-003 does not block P0–P2, but it deliberately postpones a decision
that must precede the first multi-loop registry change.

## 7. Option O-D — amend

State a materially different authority owner, contract shape, current or
prospective path, contribution model, compatibility rule, migration gate,
absence posture, consumer effect, SCOPE_CHANGE route, or Task Management
disposition. A consequential amendment requires a revised packet.

## 8. Effect on accepted decomposition and Task Management

No option directly edits `ScopeLedger.csv` or `SOFTWARE_DECOMP.md`.

- **O-A:** records the upstream product decision; recommend closing
  `TM-PEC-010` as `RESOLVED_BY_DECISION` at the exact ruling evidence and
  opening a separate SCOPE_CHANGE intake to propagate SOW-077/OI-003.
- **O-B:** records the upstream product direction; recommend the same
  `RESOLVED_BY_DECISION` closure, plus separate Root/loop notices,
  shared-contract instruments, and SCOPE_CHANGE. If the owner instead
  explicitly transfers the Task Management concern into a named SCA, the row
  may close as `SUPERSEDED_BY_SCOPE_CHANGE` only with that exact evidence.
- **O-C:** retain `TM-PEC-010` as `DEFERRED` and replace its fired trigger with
  the sharper §6 trigger.
- **O-D:** disposition follows the amendment's actual effect.

Task Management performs none of the product, decomposition, shared-contract,
or foreign-loop acts itself.

## 9. Common non-effects and rollback boundary

No D-PEC-78 ruling alone:

- changes `loops.json`, its schema, the port, adapter, tests, or any other
  source byte;
- creates a shared schema or loop declaration;
- writes Root, App, Piping, Bridge, Task Management, runtime, or another
  foreign surface;
- changes accepted decomposition, PRD bytes, lifecycle, artifact fitness, or
  another open §16 decision;
- activates a P1/P2 node, consumer, service, store, transport, daemon client,
  dashboard, or registry entry;
- imposes hexagonal architecture on another loop; or
- authorizes release, professional reliance, or a governed dependency on PEC.

Because this packet makes no source change, it has no source rollback. A later
instrument must define rollback only for its own exact paths. Accepted
decisions and artifacts are corrected through successor records and forward
changes, never silent rewrites.

## 10. Owner ruling interface

The owner may rule:

- `D-PEC-78: O-A`;
- `D-PEC-78: O-B`;
- `D-PEC-78: O-C`; or
- `D-PEC-78: O-D` with exact amendments.

No selection is inferred from the recommendation.
