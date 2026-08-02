# D-PEC-75 decision packet — second P1 source slice

**Packet state:** AWAITING_RULING / NO SOURCE AUTHORITY

**Decision:** D-PEC-75

**Prepared:** 2026-08-02

**Presentation basis:** `f98e678b1cfd80d7d03e035e5a434bdb58ca13ae`

**Owning loop:** PEC

## 1. Question and authority boundary

Which bounded P1 slice should follow the accepted DEL-08-02 API-contract
canary, and under which contract-currency, source-path, check-profile,
verification, rollback, lifecycle, and artifact-fitness gates?

This packet presents two executable-but-contingent options, amendment, and
deferral. It selects nothing. Advisory dependency status at `INITIALIZED` is
planning evidence, not production authority. Until the owner rules,
`F-PEC-1` remains closed over every path named below; no ScopeOfWork, source,
project workflow profile, domain-engine profile, status, or accepted artifact
byte may change.

Both executable options reach the successor trigger in the live historical
PEC domain profile. A separately adopted D-T0-27 PEC-v2 domain-profile
successor must therefore be effective before either source activation. This
packet does not adopt that profile, narrow its trigger, or make the project
workflow profile a substitute for it.

## 2. Accepted basis and live state

| Basis | SHA-256 |
|---|---|
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| accepted DEL-00-01 ADR | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |
| accepted DEL-00-03 SPEC | `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315` |
| current `projects/pec/software-workflow.json` | `46f8495444de922d5f85bd71ee473d8ff980fac0b8c30392d7ddf76fee4fff82` |
| stale `_DomainEngines/profiles/pec.yaml` | `0d6e1505003cffeba0393bdebaa48f19f27e2b1de8964e2c2bd262331f9ccca6` |

The accepted decomposition revision is commit
`11a494e9ae0cca795aa460deec19b9eac4d922a8`. The dependency corpus remains
64 local registers / 254 rows / 119 execution edges / zero nontrivial SCCs.

D-PEC-74 closed with DEL-08-02 at `CHECKING`, zero review findings, AC-001
through AC-005 satisfied, and these exact accepted bytes:

- schema: `0a4e42737e628be604bd163e8c6f835cda488f7978ae9e973cff03d1f8695c67`;
- compatibility test:
  `efdd32f24c0045160d7a736b1ffbdc2b8685246a66c8c362aba8899747decc92`;
- additive fixture:
  `b3ed8554e93e1380617ceb9d1de6030e684ddd91c89763d0d7565af56e079718`;
- removal fixture:
  `eb25e52b14e4fcf98e48fec7a66d4988e5bfac590c6c30806cde3ed78338bacb`;
  and
- meaning-change fixture:
  `bd2617a7cc47049af503c45fe6f86ec2c5f8270ae47950c9970288780c318cb8`.

The live option comparison is:

| Candidate | Position | Consequence |
|---|---|---|
| DEL-01-06 loop registry local default | S-sized P1 raw-DAG root; downstream DEL-02-07, DEL-03-01, DEL-09-02 | Small directed-bootstrap locator with a typed core port and replaceable local-JSON filesystem adapter. |
| DEL-01-01 record-tier schema & entity model | L-sized P1 node; sole predecessor DEL-00-01 now `CHECKING`; 11 downstream consumers | Establishes the 14-type core model and declarative store DDL, but DDL/persistence shape is conservatively treated as reaching the domain-profile successor trigger. |

## 3. Domain-profile prerequisite and D-PEC-76 reservation

`_DomainEngines/profiles/pec.yaml` is a historical v0.4 binding with
`profile_status: STALE` and
`execution_policy: DENY_ALL_PROFILE_MEDIATED_INVOCATIONS`. Its own successor
clause requires a separately adopted v2 profile before any v2
profile-mediated integration, or no later than activation of the first
accepted PEC-v2 adapter/runtime-client deliverable.

DEL-01-06 unambiguously creates a filesystem/config adapter. DEL-01-01 creates
a declarative DDL store representation; the accepted ADR classifies query
dialect, schema migration, and physical persistence as adapter concerns.
Accordingly this packet makes no confident trigger-escape claim for either
option. D-T0-27 must be separately adopted and effective before source
activation. If the owner wants a narrower trigger reading, that is a separate
owner ruling; it is not inferred here.

D-T0-27 is now presented at
`_DomainEngines/bridge/PEC_V2_PROFILE_SUCCESSOR_D-T0-27_2026-08-02/PACKET.md`;
its exact candidate profile is SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`.
The tier-0 decision record is
`_DomainEngines/_DECISIONS/D-T0-27_pec_v2_profile_successor.md`.

The D-T0 packet reads the exact DEL-01-01 declarative-DDL fence as not reaching
the trigger. D-PEC-75 deliberately applies the stricter local sequence to O-B:
because accepted ADR-PEC-V2-001 classifies query dialect, schema migration,
and physical persistence as adapter concerns, the local packet does not make
a confident trigger escape out of DDL. This is a conservative prerequisite,
not an amendment to D-T0-27; the owner may amend O-B to the narrower tier-0
reading.

D-PEC-76 is added to the PEC decision register as the local pointer/request
row, following the D-PEC-11 precedent. It points to D-T0-27 and does not create
a second profile-adoption authority: the semantic ruling is D-T0-27. If the
owner rules D-T0-27 O-A, the D-PEC-76 row and only the exact local pointer
corrections in the D-T0 application plan may close atomically with that
application. D-PEC-75 does not edit, promote, replace, or adopt a domain
profile.

`projects/pec/software-workflow.json` is different: it only registers
project-local deterministic checks and path selection. Extending it under an
option grants no runtime, domain-engine, source, lifecycle, or acceptance
authority and cannot discharge D-T0-27.

## 4. Common staged gates

Each executable option has two phases:

1. **contract-currency phase** — only the named `ScopeOfWork.md` may be
   normalized within the option's exact record fence; the deterministic SOW
   validator and derived checklist rerun; and separate REVIEW/owner acts bind
   the resulting hash;
2. **source-production phase** — the exact source, project workflow profile,
   tests, run records, and execution handoff may be produced only after the
   option's SOW-fitness gate and effective D-T0-27 profile successor.

An O-A or O-B ruling opens only the bounded contract-currency phase
immediately. It freezes the source phase as conditional authority, dormant
until both named human gates are evidenced. It does not silently select
`SELF_CHECK`, authorize review from `INITIALIZED`, accept the revised SOW, or
adopt D-T0-27. A green validator, checklist, commit, push, PR, or merge is
evidence or Git transport, not a semantic ruling.

The producer output remains candidate work until REVIEW and an exact-hash
owner artifact-fitness act. Lifecycle stays `INITIALIZED` unless the owner
separately authorizes Gate 5; no `ISSUED` act is included. No later node opens
automatically.

## 5. Option O-A — DEL-01-06 typed local loop registry (recommended)

### 5.1 Selection and production contract

Select only **DEL-01-06 Loop registry (local config default)** in PKG-01. Its
current contract is
`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md`,
SHA-256
`bd28a3426882d19e53a6a46b196005a0a9f445e7b6436125590cfab07d01ae47`.
It validates as `SOW_V1` and derives six acceptance items, AC-001 through
AC-006. It is a dependency-lawful S-sized raw-DAG root and gives the directed
bootstrap an early locator without opening parser, reconciler, store, service,
transport, or runtime-client work.

### 5.2 O-A contract-currency phase

The first phase may modify only the DEL-01-06 `ScopeOfWork.md` path above and
only to:

- change frontmatter and accepted-basis references from revision 1.2 /
  `3623b958b` to revision 1.3 / `11a494e9a`;
- change CLM-007 and any direct lifecycle mirror from `OPEN` to current
  `INITIALIZED`, still with no implementation; and
- remove obsolete prose claiming `_REFERENCES.md` names revision 1.1, because
  the live file already names revision 1.3.

No requirement, output, AC/VER identifier, field obligation, objective,
dependency, lifecycle state, or OI-003 posture may change. Validation must
remain `PASS format=SOW_V1`, and the same six AC identifiers must derive.
Source activation remains held until REVIEW is owner-selected from
`INITIALIZED`, all six criteria are populated, every finding is dispositioned,
and the owner accepts the resulting SOW hash as the production contract. No
lifecycle transition is implied by that contract gate.

### 5.3 Exact core/adapter contract and local defaults

After both common prerequisites, production uses:

- immutable core value `RegisteredLoop(loop_id, loop_init_path)`;
- core-owned port
  `LoopRegistry.registered_loops() -> tuple[RegisteredLoop, ...]`;
- replaceable `JsonLoopRegistry` adapter whose path and serialization do not
  leak through the core port;
- Python 3 standard library only; and
- a checked-in P1 default containing exactly the PEC loop, located by
  `_DomainEngines/pec/LOOP_INIT.md`.

The JSON object carries `schema_version: 1` and a `loops` array whose one P1
entry has `loop_id: "pec"` and
`loop_init_path: "_DomainEngines/pec/LOOP_INIT.md"`. Later loop entries are
additive and deferred. OI-003's long-term home and shape remain open. Naming a
loop grants no authority over it, and no governed act depends on the registry.

### 5.4 Exact O-A production paths

After the SOW-fitness and D-T0-27 gates, WORKING_ITEMS may create or modify
only:

- projects/pec/v2/config/loops.schema.json;
- projects/pec/v2/config/loops.json;
- projects/pec/v2/src/pec_v2/__init__.py;
- projects/pec/v2/src/pec_v2/core/__init__.py;
- projects/pec/v2/src/pec_v2/core/ports/__init__.py;
- projects/pec/v2/src/pec_v2/core/ports/loop_registry.py;
- projects/pec/v2/src/pec_v2/adapters/__init__.py;
- projects/pec/v2/src/pec_v2/adapters/config/__init__.py;
- projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py;
- projects/pec/v2/tests/config/test_loop_registry_contract.py;
- projects/pec/v2/tests/config/test_json_loop_registry.py;
- projects/pec/v2/tests/config/fixtures/missing_loop_id.json;
- projects/pec/v2/tests/config/fixtures/duplicate_loop_id.json;
- projects/pec/v2/tests/config/fixtures/malformed.json;
- projects/pec/software-workflow.json with the exact O-A bytes in §5.5;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-75_ACTIVATION.md;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-75_REGISTERED_CHECKS.json;
- projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md and its updated manifest; and
- the D-PEC-75 decision record, register row, PEC status pointer, and loop
  receipt needed to record later execution and owner gates.

No configuration-file location, JSON serialization detail, or adapter
exception type may enter the port. The repo-relative `loop_init_path` remains
allowed semantic locator data required by SOW REQ-001. Absent/unreadable tests
use isolated temporary paths and never mutate a governed file.

### 5.5 Exact O-A project workflow profile

The existing `v2-api-contract` check and path rule remain byte/semantically
intact. The accepted API regression becomes always-run, and O-A adds one
registry check:

```json
{
  "schema": "chirality-software-workflow/v1",
  "project_root": ".",
  "workspace_root": "../..",
  "checks": {
    "v2-api-contract": {
      "cwd": ".",
      "command": ["python3", "-m", "unittest", "discover", "-s", "v2/tests/contracts/api", "-p", "test_*.py"]
    },
    "v2-loop-registry": {
      "cwd": ".",
      "command": ["python3", "-m", "unittest", "discover", "-s", "v2/tests/config", "-p", "test_*.py"]
    },
    "harness-self-check": {
      "cwd": "../..",
      "command": ["python3", "tools/practitioner_harness/harness.py", "self-check"]
    }
  },
  "always_checks": ["v2-api-contract", "harness-self-check"],
  "path_rules": [
    {
      "paths": ["v2/contracts/api/**", "v2/tests/contracts/api/**", "software-workflow.json"],
      "checks": ["v2-api-contract"]
    },
    {
      "paths": ["v2/config/**", "v2/src/pec_v2/**", "v2/tests/config/**", "software-workflow.json"],
      "checks": ["v2-loop-registry"]
    },
    {
      "paths": ["execution/**", "docs/**", "AGENTS.md"],
      "checks": ["harness-self-check"]
    }
  ]
}
```

### 5.6 O-A verification and expected results

The producer must:

1. prove effective D-T0-27 adoption and obtain `ALLOW` from the reliance-hold
   preflight for DEL-01-06 production;
2. validate the owner-accepted normalized SOW and reproduce its exact six-item
   checklist;
3. prove the five accepted D-PEC-74 API hashes are unchanged;
4. validate the exact project profile and show every O-A path selects
   `v2-loop-registry`, `v2-api-contract`, and `harness-self-check`;
5. run all three checks, expected `PASS`, including the existing six API
   contract tests;
6. exercise valid-single-loop, malformed, duplicate, missing-field,
   absent-file, and unreadable-file cases with located explicit failures;
7. prove the core imports no adapter and the port exposes no configuration-
   file location, JSON serialization detail, or adapter error; the semantic
   repo-relative `loop_init_path` remains present;
8. prove no third-party import or network call exists and record VER-005's
   future DEL-01-05 enforcement rerun as pending, not passed;
9. rerun strict registers and dependency closure, expected 64 / 254 / zero
   findings and 119 edges / zero SCCs;
10. prove exact changed-path containment, reproduce the package manifest, run
    harness self-check, committed-range `coord-check`, and `git diff --check`;
    and
11. confirm no frozen-corpus, store, service, transport, runtime, external
    network, other-loop, lifecycle, ruling, or unlisted profile write.

## 6. Option O-B — DEL-01-01 record-tier model and DDL

### 6.1 Selection and tradeoff

Select only **DEL-01-01 Record-tier schema & entity model** in PKG-01. Its
current contract is
`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md`,
SHA-256
`43f1f57a13bb96b3235bbbb460342bd03518c503f23cb8b0560914f27a2f0170`.
It validates as `SOW_V1` and derives 12 acceptance items, AC-001 through
AC-012.

Its sole predecessor, DEL-00-01, now exceeds the required `INITIALIZED`
maturity: it is `CHECKING`, its SELF_CHECK has zero findings, and its exact
ADR bytes are accepted. O-B establishes the 14-type core model consumed by 11
recorded downstream relations. It is L-sized and more consequential than O-A,
and its DDL is conservatively held behind D-T0-27 rather than represented as a
profile-trigger escape.

### 6.2 O-B contract-currency phase

Only the DEL-01-01 `ScopeOfWork.md` may change, and only to:

1. update frontmatter and accepted-basis references from revision 1.2 /
   `3623b958b` to revision 1.3 / `11a494e9a`;
2. update CLM-002/003 revision labels without changing objective mappings;
3. update CLM-009 from DEL-00-01 `INITIALIZED` / no ADR to its exact
   `CHECKING` state and accepted ADR hash;
4. update CLM-013 and AX-010 from `OPEN` to current `INITIALIZED`, still with
   no DEL-01-01 implementation;
5. record OI-012 in CON-001 and AX-009 as resolved by D-PEC-72 O-B and the
   accepted ADR, while leaving OI-008 and all other unknowns open;
6. normalize REQ-009 and AC-008 from the stale either-style/no-selection
   posture to acceptance-neutral conformance with the selected hexagonal seam:
   core entity definitions do not import persistence, and persistence depends
   inward on core types; and
7. update AX-006 and only direct cross-references required by those currency
   changes.

No output, scope item, objective, entity, relationship, requirement/criterion
substance, AC/VER identifier, dependency, or lifecycle state may change. The
same 12 AC identifiers must derive and SOW validation must pass. Source
activation requires owner-selected REVIEW from `INITIALIZED`, all findings
dispositioned, and owner acceptance of the resulting SOW hash.

### 6.3 Exact O-B production decisions and paths

After both common gates, O-B selects:

- Python 3 standard-library immutable typed records for the exact 14 record-
  tier types in one cohesive core module;
- a shared immutable source-provenance value carrying optional file path,
  anchor, and SHA locators without file or diff content;
- SQLite-compatible declarative DDL as the first OUT-001 representation; and
- in-memory `sqlite3` only to parse and exercise the DDL in tests.

The DDL is not a connector, database file, migration runner, or DEL-01-03
store activation. No production code opens SQLite or imports persistence.
Receipt availability remains explicit, OI-008 remains open, and no
presence-tier or daemon user-data state is representable.

Exact paths are:

- projects/pec/v2/contracts/store/record_tier.sql;
- projects/pec/v2/src/pec_v2/__init__.py;
- projects/pec/v2/src/pec_v2/core/__init__.py;
- projects/pec/v2/src/pec_v2/core/entities/__init__.py;
- projects/pec/v2/src/pec_v2/core/entities/record_tier.py;
- projects/pec/v2/tests/core/test_record_tier_entities.py;
- projects/pec/v2/tests/core/test_record_tier_ddl.py;
- projects/pec/v2/tests/core/fixtures/record_tier_valid.json;
- projects/pec/v2/tests/core/fixtures/record_tier_rejected_content.json;
- projects/pec/v2/tests/core/fixtures/record_tier_rejected_presence.json;
- projects/pec/software-workflow.json with the exact O-B bytes in §6.4;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_run_records/D-PEC-75_ACTIVATION.md;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_run_records/D-PEC-75_REGISTERED_CHECKS.json;
- the same bounded D-PEC-75 execution-handoff and coordination closeout
  surfaces named under O-A.

### 6.4 Exact O-B project workflow profile

```json
{
  "schema": "chirality-software-workflow/v1",
  "project_root": ".",
  "workspace_root": "../..",
  "checks": {
    "v2-api-contract": {
      "cwd": ".",
      "command": ["python3", "-m", "unittest", "discover", "-s", "v2/tests/contracts/api", "-p", "test_*.py"]
    },
    "v2-record-tier-model": {
      "cwd": ".",
      "command": ["python3", "-m", "unittest", "discover", "-s", "v2/tests/core", "-p", "test_record_tier_*.py"]
    },
    "harness-self-check": {
      "cwd": "../..",
      "command": ["python3", "tools/practitioner_harness/harness.py", "self-check"]
    }
  },
  "always_checks": ["v2-api-contract", "harness-self-check"],
  "path_rules": [
    {
      "paths": ["v2/contracts/api/**", "v2/tests/contracts/api/**", "software-workflow.json"],
      "checks": ["v2-api-contract"]
    },
    {
      "paths": ["v2/contracts/store/**", "v2/src/pec_v2/**", "v2/tests/core/**", "software-workflow.json"],
      "checks": ["v2-record-tier-model"]
    },
    {
      "paths": ["execution/**", "docs/**", "AGENTS.md"],
      "checks": ["harness-self-check"]
    }
  ]
}
```

O-B verification must prove effective D-T0-27 and satisfy the common checks;
preserve all five accepted API hashes; select and pass
`v2-record-tier-model`, `v2-api-contract`, and `harness-self-check`; enumerate
exactly 14 entity types and 11 PRD rows; prove the core imports no store,
adapter, `sqlite3`, network, or third-party module; exercise the DDL only in
memory; test provenance, SHA comparison, deterministic rebuild, receipt
availability, content rejection, and presence/runtime-state rejection; and
record DEL-01-05's future enforcement rerun as pending. Strict registers,
closure, containment, manifest, coordination, whitespace, REVIEW, lifecycle,
fitness, and non-effect gates are identical to O-A.

## 7. Candidates deliberately not selected

### DEL-01-05 guard-first

DEL-01-05 is a lawful root and its checks can be adapter-free, but it is not a
genuinely executable source slice on the live tree. Its SOW REQ-005 makes an
absent service-core target fail closed, while OUT-001/OUT-002 require
registration on every service-core change and release candidate. No v2 core
package exists. Creating a marker or core source would add an artifact outside
its register-bounded `CI/lint check + posture note`; scanning all of `v2/`
would misstate the service-core boundary. It therefore follows an established
core, or requires a separately owner-ruled contract/scope amendment. This
packet does neither.

### DEL-08-03 response format

DEL-08-03 remains a later candidate, but its SOW still says DEL-08-02 is
`INITIALIZED` and no schema artifact exists. DEL-08-02 is now `CHECKING` with
exact accepted bytes. Its REQ-004/REQ-010 schema-ownership tension must be
reconciled before it can modify the accepted schema. A later packet must first
repair and re-review its 14-item SOW, preserve every accepted v1 element and
meaning, use DEL-08-02's additive check, treat absent DEL-04-03 capability as
fixture/pending, and avoid inventing limitation semantics owned by DEL-04-05.
It also reaches D-T0-27 because an API serializer is an adapter. TM-PEC-005
already tracks the limitation/format seam; no duplicate TM candidate is
created.

## 8. Common prohibited paths and acts

Under either executable option, every unlisted path remains closed. No ruling
under this packet authorizes:

- edits to frozen `projects/pec/{core,server,web,agent-sidecar,tools,fixtures}`
  or its frozen package manifests;
- root `runtime/**`, shared-contract, App, Root, Task Management, Piping,
  Bridge, or other-loop writes;
- any domain-profile edit or adoption under D-PEC-75;
- a live database, store connector, migration runner, parser, reconciler,
  service, socket, listener, authentication, transport, event, dashboard,
  runtime client, daemon, external network, or live-instance act;
- dependency-register, decomposition, PRD, accepted ADR/SPEC, Task Management
  register, or dated-slate edits;
- lifecycle transition, artifact acceptance, `ISSUED`, release, merge,
  professional reliance, or architecture mandate outside PEC; or
- adoption, acceptance, ruling, rejection, force, or another human-only act
  through source code.

`F-PEC-1` opens only after the matching gates and only for the exact option
paths. `F-PEC-2..4`, graceful absence, files-govern, content-minimality,
consumer-owned use, and no-second-loop boundaries remain in force.

## 9. Bootstrap, rollback, and failure isolation

O-A supplies the local loop locator used by three recorded consumers. O-B
supplies the core record vocabulary used by 11 recorded consumers. Neither
performs self-ingestion, creates runtime coordination state, or authorizes a
downstream node. The file-native DAG remains execution truth. A later
DEL-10-10 record may cite execution evidence, but this packet does not write
DEL-10-10.

Before publication, rollback removes only newly created option paths,
restores `projects/pec/software-workflow.json` to exact SHA-256
`46f8495444de922d5f85bd71ee473d8ff980fac0b8c30392d7ddf76fee4fff82`,
and reverts only the option's unaccepted SOW-currency and coordination pointer
edits. It never targets an accepted D-PEC-74 byte or frozen corpus. After
publication, correction is forward-only. A failed SOW or D-T0-27 gate blocks
source activation; a failed producer/review gate blocks only declared
dependants and leaves lifecycle unchanged.

## 10. Choices and recommendation

### O-C — Amend

State a different deliverable, exact paths, language/dialect, stage gate,
profile posture, check, verification, or rollback condition. A consequential
amendment requires packet revision before source work.

### O-D — Defer or decline

Make no SOW, source, project-profile, status, or domain-profile change. Keep
`F-PEC-1` closed over every second-slice path.

Recommend **O-A**. DEL-01-06 is the smaller reversible slice, exposes a
core-owned typed capability contract, and directly advances the directed-
bootstrap path while preserving OI-003. The recommendation is conditional,
not a trigger bypass: no adapter source may activate until D-T0-27 is
separately adopted and effective.

The owner may rule:

```text
D-PEC-75: O-A.
D-PEC-75: O-B.
D-PEC-75: O-C — <exact amendment>.
D-PEC-75: O-D.
```

An O-A or O-B ruling opens only its contract-currency phase immediately. The
packet then returns the normalized SOW hash and exact derived checklist for
the next owner gate. Source authority remains dormant until both the SOW-
fitness gate and D-T0-27 are effective.
