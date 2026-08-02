# D-PEC-74 decision packet — first actual P1 source slice

**Packet state:** RULED O-A / AUTHORITY RECORDED / PRODUCTION NOT YET EXECUTED

**Decision:** D-PEC-74

**Prepared:** 2026-08-01

**Preparation basis:** `5830546ab0912100f0f5b0c4b51ba788e5b9fb5a`

**Owning loop:** PEC

## 1. Question and authority boundary

Which exact dependency-lawful P1 root should open PEC v2 source production,
and under which source-tree, check-profile, verification, rollback, and
authority fence?

This packet presents two executable options, amendment, and deferral. It does
not select an option. Until the owner rules, `F-PEC-1` remains closed over all
source work; no P1 deliverable is selected or activated; no v2 source tree or
projects/pec/software-workflow.json is authorized; and no lifecycle,
artifact-fitness, release, or professional-reliance act occurs.

The dated
`projects/pec/execution/_Coordination/PEC_NEXT_WORK_SLATE_2026-07-29.md`
remains unchanged historical readiness evidence. Its indicative D-PEC-72
reservation is stale: D-PEC-72 closed the pre-P1 foundation, D-PEC-73 adopted
Task Management, and this successor packet is D-PEC-74.

## 2. Accepted basis and live preconditions

The packet is grounded on:

- `projects/pec/docs/PRD.md` v2.2, SHA-256
  `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba`;
- accepted `SOFTWARE_DECOMP` revision 1.3, SHA-256
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`;
- `Deliverables.csv`, SHA-256
  `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`;
- `ScopeLedger.csv`, SHA-256
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`;
- the accepted DEL-00-01 ADR, SHA-256
  `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`;
- the accepted DEL-00-03 SPEC, SHA-256
  `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`;
  and
- `docs/SOFTWARE_WORKFLOW_PROFILE.md`, SHA-256
  `f97af1d323524f9a2be1dab8b5b33c1350c8f48c38cd3c6f8d0f8a9cd9821ea2`.

The D-PEC-72 handoff and the owner's closure ruling establish that C-05 is
closed: DEL-00-01, DEL-00-03, and DEL-10-01 are each `CHECKING`; their final
SELF_CHECKs have no open findings; and AC-007, AC-011, and AC-008 are accepted
at their recorded hashes. No P1 node began before that closure.

Live discovery also confirms:

- all 29 P1 wave deliverables are `INITIALIZED`;
- the dependency corpus is 64 local registers / 254 rows / 119 execution
  edges / zero SCCs;
- projects/pec/v2/ and projects/pec/software-workflow.json are absent;
- the v0.4 corpus and its workspace manifests remain frozen; and
- the active-reliance-hold register is valid and contains no active row.

## 3. Slice analysis

The accepted raw DAG has six P1 roots: DEL-01-03, DEL-01-04, DEL-01-05,
DEL-01-06, DEL-08-01, and DEL-08-02. The comparison below is a planning
judgment, not decomposition truth.

| Root | Envelope/type | First-slice consequence |
|---|---|---|
| DEL-01-03 | M / backend feature | Opens store lifecycle and ingest-boundary implementation before a typed public contract exists. |
| DEL-01-04 | S / observability | Opens operational logging without first establishing a product capability boundary. |
| DEL-01-05 | S / CI/CD | Requires a concrete service-core and runtime-dependency boundary plus the unresolved C-08 release-force owner act. |
| DEL-01-06 | S / backend feature | Lawful local-config canary, but selects an application implementation language and module interface earlier than needed. |
| DEL-08-01 | M / security control | Opens transport and token work while auth reuse and API transport remain owner-open. |
| DEL-08-02 | S / API contract | Opens a language-neutral, versioned contract and executable compatibility canary without server, store, transport, auth, or runtime integration. |

DEL-08-02 is therefore the smallest root that directly exercises the owner's
PEC-local ports-and-adapters decision and typed-contract intent. It has no
upstream predecessor. Its current live downstream relations are DEL-08-03
`CONSUMES` and DEL-10-03 `TESTS`; the former DEL-07-05 proposal edge was
declined under D-PEC-66 and is not treated as live.

## 4. Option O-A — DEL-08-02 API-contract canary (recommended)

### 4.1 Selection and required production decisions

Select and activate only **DEL-08-02 Versioned additive API schema** in
PKG-08. Its current production contract is
`projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/ScopeOfWork.md`,
SHA-256
`eb171e9dac40b313be8ea8ff75ad395171b599a41d2a1dbf290a9c5b44290c20`.

This option resolves only the production-time TBDs that the selected
deliverable cannot avoid:

1. **Source-tree root:** projects/pec/v2/.
2. **Schema language:** JSON Schema draft 2020-12, stored as canonical JSON.
3. **Initial version scheme:** integer API schema version `1`, reflected in
   the `v1/` path and a machine-readable constant in the schema.
4. **PEC-local API-contract home:**
   projects/pec/v2/contracts/api/v1/schema.json.
5. **Compatibility floor:** a successor may add new definitions and optional
   elements, but may not remove or alter a published element. The executable
   check treats the canonical signature and declared meaning of every existing
   published element as immutable and fails closed on an unclassifiable
   change.
6. **Test implementation language:** Python 3 standard library only. This is
   test-tooling selection, not selection of the PEC service implementation
   language.

The schema content remains bounded by DEL-08-02 REQ-001..004 and AC-001..004.
It may define only the versioned machine-consumer API surface necessary for
that contract. It must use capability/use-case names, not App, Root, Task
Management, Piping, or another actor as a core type. It must not absorb
DEL-08-01 transport/access, DEL-08-03 compact citation-bearing response
format, DEL-08-04 latency, or DEL-08-05 subscription scope.

This local API-contract home does not decide OI-009's event-contract home or
API transport. No shared-root mirror and no `runtime/packages/contracts`
write is authorized.

### 4.2 Exact production paths

The initial WORKING_ITEMS activation may create or modify only:

- projects/pec/v2/contracts/api/v1/schema.json;
- projects/pec/v2/tests/contracts/api/test_api_schema_compatibility.py;
- projects/pec/v2/tests/contracts/api/fixtures/v1_additive_candidate.json;
- projects/pec/v2/tests/contracts/api/fixtures/v1_removed_element_candidate.json;
- projects/pec/v2/tests/contracts/api/fixtures/v1_meaning_changed_candidate.json;
- projects/pec/software-workflow.json with the exact O-A content below;
- projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_run_records/D-PEC-74_ACTIVATION.md;
- projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_run_records/D-PEC-74_REGISTERED_CHECKS.json;
- a D-PEC-74 execution handoff and updated manifest inside this packet
  directory; and
- the D-PEC-74 decision record, decision-register row, PEC status pointer, and
  PEC loop receipt needed to record execution and later owner gates.

No `_STATUS.md`, `ScopeOfWork.md`, dependency register, decomposition file, or
accepted ADR/SPEC artifact is opened by the production act.

### 4.3 Exact O-A software-workflow profile

If O-A is ruled, projects/pec/software-workflow.json is created with these
exact bytes apart from the terminating newline:

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
    "harness-self-check": {
      "cwd": "../..",
      "command": ["python3", "tools/practitioner_harness/harness.py", "self-check"]
    }
  },
  "always_checks": ["harness-self-check"],
  "path_rules": [
    {
      "paths": ["v2/contracts/api/**", "v2/tests/contracts/api/**", "software-workflow.json"],
      "checks": ["v2-api-contract"]
    },
    {
      "paths": ["execution/**", "docs/**", "AGENTS.md"],
      "checks": ["harness-self-check"]
    }
  ]
}
```

The profile registers commands and path-to-check selection only. It grants no
write permission, source authority, acceptance, lifecycle transition, or
release authority. Each run brief remains narrower than or equal to this
packet and names the selected checks.

### 4.4 O-A verification and expected results

The producer must:

1. run the PEC reliance-hold preflight with target
   `execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/ScopeOfWork.md`
   and operation `dispatch-for-production`; expected `ALLOW`;
2. validate the unchanged contract with
   `python3 tools/scope_of_work/validate_scope_of_work.py <DEL-08-02-path>`;
   expected `PASS format=SOW_V1`;
3. validate the profile through
   `tools/software_workflow/select_affected_checks.py`; expected selection of
   `v2-api-contract` for every listed source/test/profile path and
   `harness-self-check` from `always_checks`;
4. run both registered checks through
   `tools/software_workflow/run_registered_checks.py`; expected both `PASS`;
5. demonstrate that the additive fixture passes and both the removal and
   meaning-change fixtures fail with located explanations; expected AC-002 /
   AC-003 evidence complete;
6. run strict decomposition-register validation and dependency-closure
   analysis; expected 64 registers / 254 rows / 119 execution edges / zero
   SCCs / zero strict findings;
7. prove exact changed-path containment against the paths in §4.2 with
   `tools/software_workflow/validate_change_scope.py`; expected `PASS`;
8. reproduce a SHA-256 manifest over every created artifact and cited accepted
   basis; expected no mismatch;
9. run practitioner-harness `self-check`, `coord-check` over the committed
   range, and `git diff --check`; expected no new blocking finding; and
10. confirm no frozen-corpus, root-runtime, store, service, socket, network,
    dependency-manifest, ruling, lifecycle, or other-loop write occurred.

The initial source output remains candidate work. It goes to REVIEW against
the deterministic DEL-08-02 checklist and then to the owner for AC-005's
qualified objective-attribution confirmation and exact-hash artifact fitness.
Writing or checking files does not advance `INITIALIZED`, satisfy AC-005,
accept the artifacts, or make the deliverable `CHECKING` or `ISSUED`.

## 5. Option O-B — DEL-01-06 local-loop-registry canary

### 5.1 Selection and tradeoff

Select and activate only **DEL-01-06 Loop registry (local config default)** in
PKG-01. Its production contract is
`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md`,
SHA-256
`bd28a3426882d19e53a6a46b196005a0a9f445e7b6436125590cfab07d01ae47`.

O-B is dependency-lawful and S-sized. It establishes PEC's directed-bootstrap
loop locator before parsers/reconciliation. Unlike O-A, it selects Python 3 as
the first PEC service implementation language and creates a service-core
module interface before the language-neutral API contract exists. It is more
implementation-committing and less directly aligned with the owner's typed
cross-application boundary intent.

O-B resolves only these required production choices:

- source-tree root projects/pec/v2/;
- checked-in local JSON registry schema and instance under
  projects/pec/v2/config/;
- Python 3 standard-library loader under projects/pec/v2/src/pec_v2/;
- public in-process interface `registered_loops()` with no path or
  serialization parameter; and
- P1 default containing exactly the PEC loop, with additive entries deferred
  to P2.

The local default does not decide OI-003's long-term registry home or shape and
creates no authority over the PEC loop or another loop.

### 5.2 Exact O-B production paths

The O-B activation may create or modify only:

- projects/pec/v2/config/loops.schema.json;
- projects/pec/v2/config/loops.json;
- projects/pec/v2/src/pec_v2/__init__.py;
- projects/pec/v2/src/pec_v2/loop_registry.py;
- projects/pec/v2/tests/config/test_loop_registry.py;
- projects/pec/v2/tests/config/fixtures/missing_id.json;
- projects/pec/v2/tests/config/fixtures/duplicate_id.json;
- projects/pec/v2/tests/config/fixtures/unreadable_path_marker.json;
- projects/pec/software-workflow.json with the exact O-B content below;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-74_ACTIVATION.md;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-74_REGISTERED_CHECKS.json;
- the same bounded D-PEC-74 coordination closeout surfaces named in O-A.

The `unreadable_path_marker.json` file is fixture metadata naming the path
whose permissions are changed only inside an isolated temporary-directory
test; the checked-in fixture itself remains readable. No test mutates a
governed project file.

### 5.3 Exact O-B software-workflow profile

```json
{
  "schema": "chirality-software-workflow/v1",
  "project_root": ".",
  "workspace_root": "../..",
  "checks": {
    "v2-loop-registry": {
      "cwd": ".",
      "command": ["python3", "-m", "unittest", "discover", "-s", "v2/tests/config", "-p", "test_*.py"]
    },
    "harness-self-check": {
      "cwd": "../..",
      "command": ["python3", "tools/practitioner_harness/harness.py", "self-check"]
    }
  },
  "always_checks": ["harness-self-check"],
  "path_rules": [
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

O-B uses the same authority semantics as O-A. Its verification substitutes the
DEL-01-06 contract/check paths and demonstrates valid-single-loop, malformed,
duplicate, absent, and unreadable cases; `registered_loops()` returns exactly
the PEC loop; no third-party import or network call exists. VER-005's future
DEL-01-05 rerun remains deferred until that deliverable is available and must
not be falsely reported as executed. REVIEW and owner acceptance remain
separate; lifecycle remains `INITIALIZED` absent a later Gate 5 act.

## 6. Common prohibited paths and acts

Under either executable option, every path not expressly listed is closed.
In particular, the ruling would not authorize:

- any edit under frozen
  `projects/pec/{core,server,web,agent-sidecar,tools,fixtures}` or the frozen
  `package.json`, `package-lock.json`, and `tsconfig.base.json` manifests;
- any root `runtime/**`, shared-contract, App, Root, Task Management, Piping,
  Bridge, or other-loop write;
- any PEC v2 service, store, database, socket, listener, event feed, daemon
  client, dashboard, or external-network execution;
- dependency-register, decomposition, PRD, accepted ADR/SPEC, `AGENTS.md`,
  domain-profile, or Task Management register changes;
- lifecycle transition, artifact acceptance, `ISSUED`, release, merge,
  professional reliance, or architecture mandate outside PEC;
- any adoption, ruling, direction, acceptance, rejection, or other human-only
  act through PEC code; or
- copying v0.4 machinery into v2. Historical modules may be cited as patterns
  only.

`F-PEC-1` is amended only for the exact option paths after the corresponding
owner ruling. `F-PEC-2..4`, content-minimality, files-govern, graceful absence,
consumer-owned use, and no-second-loop boundaries remain fully in force.

## 7. Bootstrap/self-ingest relationship

Either executable option is the first source-producing node in PEC's accepted
full DAG. The file-native DAG remains the sole coordination state. Because no
reconciler exists yet, this slice performs no runtime self-ingestion and no PEC
capability cutover.

The execution handoff must record the selected node, exact source hashes,
review state, and any observed coordination friction as input evidence for the
later DEL-10-10 bootstrap progression record. That routing is evidence only;
it does not write DEL-10-10, propose a new product function, or authorize an
amendment. Later DAG nodes may consume only a predecessor capability after its
separate artifact-fitness and lifecycle gates are satisfied. Manual/file-native
Step 0 remains the fallback throughout.

Deferred under both options: reconciler and store implementation; PEC runtime
self-ingestion; API transport/server/auth; response format; no-ruling-write
test; kill test; parity; release; all P2–P4 work; and every open PRD §16
decision not expressly identified above as a local, reversible P1 default.

## 8. Review, owner gates, rollback, and failure isolation

After an executable option is ruled:

1. HELP_HUMAN activates one WORKING_ITEMS Agent 1 for the selected package and
   deliverable with an exact-path brief.
2. WORKING_ITEMS runs the reliance preflight, records the selected profile,
   and dispatches bounded implementation/testing work through the approved
   software workflow. Shared writes are serialized under one package
   integration owner.
3. Producer checks and path containment must pass before fan-in. Failure keeps
   the deliverable `INITIALIZED` and blocks only work that declares this output
   as a predecessor.
4. REVIEW type selection, any review-from-`INITIALIZED` override, findings
   dispositions, Gate 5 lifecycle act, exact-hash artifact acceptance, and any
   objective-attribution confirmation remain separate owner acts unless the
   owner states them explicitly in a later ruling.
5. A source commit, push, PR, or merge is Git transport only and infers none of
   those semantic acts.
6. No later P1 node opens automatically. Its source paths and acts require the
   authority then applicable under the standing per-tranche packet rule.

Before publication, rollback deletes only the newly created option paths and
restores the D-PEC-74 coordination pointer edits; the frozen corpus is never a
rollback target. After publication, correction uses a successor record and a
normal forward commit; ruled or accepted bytes are never silently rewritten.

## 9. Remaining choices

### O-C — Amend

State a different selected P1 root/set, source-tree root, schema/language,
profile, exact path list, check, gate, or rollback condition. Any amendment
that selects a non-root or multiple nodes must name dependency staging and the
intermediate owner acceptance gates. A consequential amendment requires a
revised packet before source work.

### O-D — Defer or decline

Create no source tree and no profile. Leave all 29 P1 deliverables
`INITIALIZED`; `F-PEC-1` remains closed over source work. D-PEC-72 C-05 remains
closed and unaffected.

## 10. Recommendation and ruling mechanism

Recommend **O-A**. It is the smallest dependency-lawful and reversible source
slice, directly implements a PEC-owned typed port contract under the accepted
hexagonal ADR, keeps service language/transport/store/runtime choices open,
and exercises the new source tree plus registered-check machinery without
copying the frozen product.

The owner may rule with one of:

```text
D-PEC-74: O-A.
D-PEC-74: O-B.
D-PEC-74: O-C — <exact amendment>.
D-PEC-74: O-D.
```

Only the owner's ruling selects and opens the matching exact fence.

## 11. Owner ruling and activation state

Owner ruling recorded verbatim (2026-08-01, in-session, Ryan Tufts):

```text
D-PEC-74: O-A.
```

O-A is selected. Only DEL-08-02 is activated for the exact production paths,
profile bytes, checks, rollback, owner gates, and non-effects in §4 and the
frozen activation authority
`O-A_ACTIVATION_AUTHORITY_2026-08-01.md`.

This section records semantic authority before production. At this checkpoint
projects/pec/v2/ and projects/pec/software-workflow.json remain absent; no
deliverable-local file has changed; DEL-08-02 remains `INITIALIZED`; and no
artifact acceptance, lifecycle transition, later P1 node, release, merge,
professional reliance, or architecture mandate outside PEC is inferred.
