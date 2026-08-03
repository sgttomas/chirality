# D-PEC-77 decision packet — DEL-01-05 contract currency and enforcement

**Packet state:** AWAITING_RULING / NO CONTRACT OR SOURCE AUTHORITY

**Decision:** D-PEC-77

**Prepared:** 2026-08-02

**Presentation basis:** `97678a841ef58345c73d3470ed8de57c9b1405d2`

**Owning loop:** PEC

**Task Management route:** `TM-PEC-009`

## 1. Question and authority boundary

Should PEC activate one staged DEL-01-05 tranche that first repairs and
reviews the stale production contract, then conditionally produces the
zero-third-party-runtime-dependency and no-external-egress assertions against
the live PEC v2 service core? If so, should the delivered blocking verdict be
release-binding for PEC or advisory?

This packet presents the production choice and the independent CON-002 /
AC-011 authority choice. It selects neither. Until the owner rules, it grants
no ScopeOfWork edit, manager dispatch, source, test, workflow registration,
review, lifecycle, artifact acceptance, release, professional reliance, or
DEL-01-06 rerun authority.

The routed Task Management boundary remains exact: selecting or completing
DEL-01-05 does not close `TM-PEC-009`. Closure requires the later DEL-01-06
SELF_CHECK rerun to reopen and close RF-001 with exact DEL-01-05 evidence.
VER-005 is not waived.

## 2. Routed authority and accepted basis

| Basis | SHA-256 |
|---|---|
| Task Management owner ruling | `ce96dcaf8f73b9c9cb6963b372fc72df3080378bd9ccc9d8551efd41583efe78` |
| routed request `REQUEST_TM-PEC-009_DEL-01-05_PACKET.md` | `0afc44750797dd27cb6093c3a2509be5ca711bd4f8563e55fe21debf47f3d847` |
| routed controlling draft | `105795bcff6e5c1e15c795caaa95f878f338a02d46160326259557e83fc7b962` |
| `projects/pec/docs/PRD.md` v2.2 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.3 | `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5` |
| accepted DEL-00-01 ADRs | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |
| current DEL-01-05 `ScopeOfWork.md` | `ce51490178a4e07f4266a09e156e2b8d7bca618a41477f57eb746b4596b49824` |
| current DEL-01-05 `_STATUS.md` | `f7cb08a6e229b6195a239547c09b47f00cdccd73a723f93ea05a8cb25feae9d9` |
| DEL-01-06 `Review_Findings.csv`, including RF-001 | `fa04561fe97cc33cc8198ef2f5dfa31b4c92f4aff41d591556e312f1e2e735bb` |
| D-PEC-75 execution handoff | `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` |
| current `projects/pec/software-workflow.json` | `4ef630f4ab0bf51480ff83e3e8844e71cc827cf4ddddb1268c727a03d1b45cbc` |

The accepted decomposition basis is revision 1.3 at commit
`11a494e9ae0cca795aa460deec19b9eac4d922a8`. D-T0-27 is effective at
`ADOPTED / READ_ONLY` through merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`. DEL-01-05 is
`INITIALIZED`; no DEL-01-05 implementation exists.

The live core target now exists at
`projects/pec/v2/src/pec_v2/core/**`. It is Python 3 / standard-library code,
uses the owner-selected ports-and-adapters boundary, and currently contains no
third-party import or network behavior. This removes D-PEC-75's earlier
physical bootstrap absence; it does not itself authorize work.

The current SOW validates as `PASS format=SOW_V1` and deterministically derives
exactly AC-001 through AC-011. Its basis, lifecycle, OI-012, core-target, and
toolchain statements are stale or unresolved against accepted intervening
state. Requirements and acceptance identifiers remain suitable.

## 3. Option O-A — staged DEL-01-05 enforcement (recommended)

Select only DEL-01-05. The option is serialized into two phases. The owner
ruling opens phase 1 only; phase 2 remains dormant until the repaired SOW is
reviewed and accepted at its exact hash.

### 3.1 Phase 1 — bounded contract currency

Only this file may change:

`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md`

WORKING_ITEMS may revise only statements made stale or resolvable by accepted
intervening state:

1. bind the accepted basis to SOFTWARE_DECOMP revision 1.3 at
   `11a494e9ae0cca795aa460deec19b9eac4d922a8`;
2. record current lifecycle `INITIALIZED` while preserving that no DEL-01-05
   implementation exists;
3. record OI-012 as resolved by D-PEC-72 O-B and accepted
   ADR-PEC-V2-001's ports-and-adapters isolation;
4. name `projects/pec/v2/src/pec_v2/core/**` as the operative service-core
   target;
5. define the live implementation posture as Python 3 plus the standard
   library, with workspace-internal runtime-contract packages permitted only
   when explicitly enumerated;
6. define a runtime dependency as an import reachable from a production
   Python module under the operative core target, excluding standard-library,
   PEC-local, and explicitly admitted workspace-contract imports; build,
   test, and development imports outside the core are not runtime
   dependencies; and
7. resolve the mechanism/home unknowns only to the exact checker,
   configuration, tests, posture note, and workflow registration in this
   packet.

The repair may make only direct cross-reference and tense adjustments required
by those seven changes. It must not change outputs, requirements, AC/VER
identifiers, objective attribution, scope items, the continuing-assertion
character, CON-001, CON-002, AC-010, AC-011, lifecycle state, or artifact
class.

The repaired SOW must validate as `SOW_V1` and derive the same ordered eleven
items, AC-001 through AC-011. It then returns for owner selection of REVIEW
type, any review-from-`INITIALIZED` override, finding dispositions, Gate 5,
and exact-hash contract fitness. Contract acceptance satisfies no future
production AC and changes no lifecycle by implication.

### 3.2 Phase 2 — exact source-production paths

Only after the phase-1 exact SOW bytes are owner-accepted as the production
contract may WORKING_ITEMS create or modify:

- `projects/pec/v2/config/service_core_posture.json`;
- `projects/pec/v2/tools/check_service_core_posture.py`;
- `projects/pec/v2/docs/SERVICE_CORE_POSTURE.md`;
- `projects/pec/v2/tests/enforcement/test_dependency_assertion.py`;
- `projects/pec/v2/tests/enforcement/test_locality_assertion.py`;
- `projects/pec/v2/tests/enforcement/test_gate_registration.py`;
- `projects/pec/v2/tests/enforcement/fixtures/dependency/conforming/core/app.py`;
- `projects/pec/v2/tests/enforcement/fixtures/dependency/workspace_contract/core/app.py`;
- `projects/pec/v2/tests/enforcement/fixtures/dependency/workspace_contract/contracts/chirality_contracts/__init__.py`;
- `projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_direct/core/app.py`;
- `projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/app.py`;
- `projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/helper.py`;
- `projects/pec/v2/tests/enforcement/fixtures/locality/external_call/core/app.py`;
- `projects/pec/v2/tests/enforcement/fixtures/locality/external_config/core/settings.py`;
- `projects/pec/v2/tests/enforcement/fixtures/locality/local_unix/core/app.py`;
- `projects/pec/v2/tests/enforcement/fixtures/locality/local_loopback/core/app.py`;
- `projects/pec/software-workflow.json`, only to the additive postimage in
  §3.4;
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_run_records/D-PEC-77_ACTIVATION.md`;
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_run_records/D-PEC-77_REGISTERED_CHECKS.json`;
- `projects/pec/execution/_Coordination/D-PEC-77_DEL-01-05_ENFORCEMENT_2026-08-02/EXECUTION_HANDOFF.md` and its manifest; and
- the D-PEC-77 decision record, register row, PEC status pointer, and loop
  receipt required to record later execution and owner gates.

The checker is a deterministic Python-standard-library tool. It reads but
does not edit the core, configuration, workflow profile, or repository. Its
dependency assertion fails on any non-standard-library, non-PEC-local import
not named in the exact admitted set. Dynamic or unresolved imports fail
closed. Its locality assertion fails on external-network call sites and
external endpoint configuration while treating Unix-domain and loopback-only
transport as local. That classification does not authorize loopback transport
and produces the same result under either future OI-009 disposition.

The production configuration is schema version 1, targets exactly
`v2/src/pec_v2/core`, identifies `v2/src` as the PEC-local source root, and
starts with an empty workspace-runtime-contract admitted set. Adding an
admitted workspace contract is a visible reviewed configuration change. No
wildcard or implicit admission exists.

### 3.3 Standing verdict and graceful absence

The checker exits nonzero and emits located findings when either assertion
fails, when the target/config/workflow surface is absent or unreadable, when
an import cannot be classified, or when the registered check is missing. It
does not report a pass over an unevaluated surface.

The mechanism constrains PEC's own build only. It does not run a service,
open a socket, call a network, edit a manifest, prevent Git operations, or
bind any governed act outside PEC. PEC may be deleted without blocking any
governed act. Whether the nonzero verdict binds a PEC release is the separate
§4 choice.

### 3.4 Exact additive project workflow postimage

O-A preserves the three live checks and adds one standing check. The exact
semantic postimage is:

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
    "v2-core-posture": {
      "cwd": ".",
      "command": ["python3", "v2/tools/check_service_core_posture.py", "--config", "v2/config/service_core_posture.json", "--workflow", "software-workflow.json"]
    },
    "harness-self-check": {
      "cwd": "../..",
      "command": ["python3", "tools/practitioner_harness/harness.py", "self-check"]
    }
  },
  "always_checks": ["v2-api-contract", "v2-core-posture", "harness-self-check"],
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
      "paths": ["v2/src/pec_v2/core/**", "v2/config/service_core_posture.json", "v2/tools/check_service_core_posture.py", "v2/tests/enforcement/**", "v2/docs/SERVICE_CORE_POSTURE.md", "software-workflow.json"],
      "checks": ["v2-core-posture"]
    },
    {
      "paths": ["execution/**", "docs/**", "AGENTS.md"],
      "checks": ["harness-self-check"]
    }
  ]
}
```

The project workflow remains a deterministic check registry. It is not a
domain profile, release act, CI service, runtime, or authority surface.

### 3.5 Required verification

The producer must:

1. obtain `ALLOW` from the PEC reliance-hold preflight for contract repair,
   source production, and fan-in at the applicable stages;
2. validate the owner-accepted SOW and reproduce exact AC-001 through AC-011;
3. run conforming, explicitly admitted workspace-contract, direct third-party,
   and transitive third-party dependency fixtures with located outcomes;
4. run external call, external endpoint, Unix-domain, and loopback-only
   locality fixtures under both readings of OI-009 and reproduce identical
   classifications;
5. fault-inject absent/unreadable config, absent/unreadable core, malformed
   configuration, unclassifiable import, and induced tool failure; every case
   must fail explicitly;
6. mutate a scratch workflow profile by disabling and removing
   `v2-core-posture`; the checker must report the missing registration;
7. bind every result to the exact source/config/workflow SHA evaluated and
   prove that an earlier pass is not reused for a later state;
8. compare the core tree and all dependency/configuration manifests before and
   after a full run, and inspect the checker itself; no file mutation,
   third-party runtime dependency, or network call may occur;
9. inspect `SERVICE_CORE_POSTURE.md` element by element against REQ-009 and
   REQ-010 and preserve OI-009 as open;
10. prove the exact §3.4 workflow postimage and affected-check selection; run
    `v2-api-contract`, `v2-loop-registry`, `v2-core-posture`, and
    `harness-self-check`;
11. prove all accepted D-PEC-74 and D-PEC-75 source hashes outside the exact
    path list are unchanged;
12. rerun strict decomposition-register validation and dependency closure,
    expected 64 registers / 254 rows / zero findings and 119 execution edges /
    zero nontrivial SCCs;
13. run the standing graceful-absence kill test and practitioner-harness
    parity comparison applicable to this implementation tranche; and
14. prove exact changed-path containment, reproduce the manifest, run
    committed-range coordination checking, and run `git diff --check`.

Producer output remains candidate work. REVIEW type, review-from-
`INITIALIZED`, findings, Gate 5, AC-010, AC-011, exact-hash artifact fitness,
`ISSUED`, and release remain separate owner gates.

## 4. CON-002 / AC-011 authority choice

This choice is independent of O-A's mechanical blocking verdict.

### G-A — PEC release-binding force (recommended)

Confirm the policy that a failed, missing, or unevaluated delivered DEL-01-05
assertion blocks a PEC release candidate. The force applies only to PEC
release. It grants no authority over another loop, no Git veto, no governed-act
dependency on PEC-held state, and no release by itself.

This is recommended because DEL-01-05 is typed `CI_CD_CHANGE`, its contract is
standing by construction, and its explicit blocking verdict otherwise becomes
advisory at precisely the release boundary it is designed to protect.

Selecting G-A records the policy direction. AC-011 is satisfied only after the
owner later confirms that the produced exact artifacts implement this ruled
force faithfully.

### G-B — advisory verdict

Decline release-gating authority. The same assertion runs, fails closed, and
reports a blocking-shaped verdict, but the release owner may proceed despite
it. This leaves the contract's continuing character and AC-001 through AC-010
intact. AC-011 is later satisfied by recording the owner declination against
the produced exact artifacts.

### G-C — defer the force choice

Leave CON-002 and AC-011 open. O-A production may still be selected, but the
mechanism remains advisory until a later owner ruling; no later artifact may
describe it as release-binding meanwhile.

## 5. Option O-B — amend

State a different contract fence, service-core definition, language,
mechanism, admitted-set policy, exact path list, check registration,
verification requirement, authority choice, or rollback rule. A consequential
amendment requires a revised packet before work opens.

## 6. Option O-C — defer or decline

Change no SOW, source, test, workflow profile, run record, finding, lifecycle,
or register row. DEL-01-05 remains `INITIALIZED`; DEL-01-06 RF-001 remains
`DEFERRED`; `TM-PEC-009` remains `DEFERRED`; VER-005 remains mandatory and
unsatisfied.

## 7. Common prohibited paths and acts

Every path not expressly listed is closed. In particular, no option authorizes:

- edits under the frozen v0.4 corpus or its manifests;
- edits to PEC v2 core, adapter, API-contract, loop-registry, service, store,
  transport, daemon-client, dashboard, or other product source;
- PRD, accepted decomposition, dependency-register, accepted ADR/SPEC,
  domain-profile, Task Management register, or another deliverable's source
  change;
- root runtime, shared-contract, App, Piping, Bridge, Task Management, or any
  other-loop write;
- resolution or foreclosure of OI-009 / SOW-083;
- reopening DEL-01-06 RF-001 before reviewed DEL-01-05 evidence exists;
- lifecycle transition, artifact acceptance, later P1 activation, release,
  merge, professional reliance, or cross-loop mandate; or
- a PEC write, dispatch, ruling, acceptance, or lock surface.

`F-PEC-1` is amended only for the exact phase reached after its named owner
gates. `F-PEC-2..4`, files-govern, content-minimality, graceful absence,
consumer-owned use, human-only acts, and no-second-loop remain in force.

## 8. Rollback, failure isolation, and downstream sequence

Before publication, rollback removes only new §3.2 files and restores
`software-workflow.json` to its preimage. After publication or owner
acceptance, correction uses a successor record and forward commit; accepted
SOW or artifact bytes are never silently rewritten.

A failed contract repair leaves source dormant. A failed producer or review
leaves DEL-01-05 `INITIALIZED` and blocks only declared dependants. No later P1
node opens automatically.

If DEL-01-05 is produced, reviewed, and accepted, REVIEW may then reopen
DEL-01-06 RF-001 and rerun its deterministic six-item SELF_CHECK with exact
DEL-01-05 VER-005 evidence. Only that later result can support closing
`TM-PEC-009`; DEL-01-05 selection, production, Gate 5, or acceptance alone
cannot.

## 9. Owner ruling interface

The owner may rule:

- `D-PEC-77: O-A; CON-002: G-A`, `G-B`, or `G-C`;
- `D-PEC-77: O-B` with exact amendments; or
- `D-PEC-77: O-C`.

No selection is inferred from the recommendation.
