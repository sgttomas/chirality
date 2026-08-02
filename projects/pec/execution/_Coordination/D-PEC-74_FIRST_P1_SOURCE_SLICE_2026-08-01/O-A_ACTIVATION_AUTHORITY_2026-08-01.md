# D-PEC-74 O-A activation authority — DEL-08-02 API-contract canary

**State:** OWNER-RULED / READY FOR BOUNDED WORKING_ITEMS PRODUCTION

**Authority basis:** merged D-PEC-74 packet at
`bb13059a5397a21face9529e1449b624933ea4bc`

**Owner ruling verbatim (2026-08-01):**

```text
D-PEC-74: O-A.
```

## Selected activation

- Package: PKG-08 API & Access.
- Deliverable: DEL-08-02 Versioned additive API schema, and no other node.
- Current lifecycle: `INITIALIZED`; activation does not change it.
- Production contract:
  `../../PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/ScopeOfWork.md`,
  SHA-256
  `eb171e9dac40b313be8ea8ff75ad395171b599a41d2a1dbf290a9c5b44290c20`.
- Accepted architecture: PEC-local hexagonal isolation, accepted ADR SHA-256
  `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`.
- Accepted SPEC seed SHA-256
  `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`.

## Frozen production choices

- New source root: projects/pec/v2/.
- Contract home: projects/pec/v2/contracts/api/v1/schema.json.
- Schema language: JSON Schema draft 2020-12, canonical JSON.
- Initial version: integer `1`, represented by the v1 path and a
  machine-readable schema constant.
- Additive floor: new definitions and optional elements may be added;
  published elements may not be removed or altered; unclassifiable changes
  fail closed.
- Compatibility-test implementation: Python 3 standard library only. This is
  test tooling, not selection of PEC's service implementation language.
- Capability/use-case names remain PEC-owned; actor-specific App, Root, Task
  Management, Piping, or other-loop types do not enter the PEC core.
- DEL-08-01 transport/access, DEL-08-03 response format, DEL-08-04 latency,
  DEL-08-05 subscriptions, OI-009 event-contract home, and API transport remain
  outside this activation.

## Exact allowed production paths

One WORKING_ITEMS activation may create or modify only:

- projects/pec/v2/contracts/api/v1/schema.json;
- projects/pec/v2/tests/contracts/api/test_api_schema_compatibility.py;
- projects/pec/v2/tests/contracts/api/fixtures/v1_additive_candidate.json;
- projects/pec/v2/tests/contracts/api/fixtures/v1_removed_element_candidate.json;
- projects/pec/v2/tests/contracts/api/fixtures/v1_meaning_changed_candidate.json;
- projects/pec/software-workflow.json with the exact bytes below;
- projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_run_records/D-PEC-74_ACTIVATION.md;
- projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/_run_records/D-PEC-74_REGISTERED_CHECKS.json;
- the D-PEC-74 packet-directory execution handoff and manifest refresh; and
- the already-governed D-PEC-74 decision/register, PEC status, and PEC receipt
  updates required to record production and later owner gates.

No `_STATUS.md`, `ScopeOfWork.md`, dependency register, decomposition file,
PRD, accepted ADR/SPEC artifact, or other source path is opened.

## Exact software-workflow profile

projects/pec/software-workflow.json shall contain these exact bytes apart from
the terminating newline:

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

The profile registers commands and path selection only. It grants no write,
acceptance, lifecycle, release, or professional-reliance authority.

## Mandatory producer checks

1. Active-reliance-hold preflight for the selected contract with operation
   `dispatch-for-production`: `ALLOW`.
2. `validate_scope_of_work.py` on DEL-08-02: `PASS format=SOW_V1`.
3. Affected-check selection: `v2-api-contract` for every selected
   source/test/profile path plus the always-run `harness-self-check`.
4. Both registered checks: `PASS`.
5. Fixture behavior: additive candidate passes; removal and meaning-change
   candidates fail with located explanations.
6. Strict dependency registers: 64 registers / 254 rows / zero findings;
   closure: 119 execution edges / zero SCCs.
7. Changed-path containment against the exact allowed list: `PASS`.
8. Full SHA-256 manifest: no mismatch.
9. Practitioner-harness `self-check`, committed-range `coord-check`, and
   `git diff --check`: no new blocking finding.
10. Frozen-corpus, root-runtime, store, service, socket, network,
    dependency-manifest, ruling, lifecycle, and other-loop writes: none.

## Production handoff and human gates

WORKING_ITEMS owns one bounded PKG-08 activation and serializes its integration
write. Producer output remains candidate work. REVIEW type selection, any
review-from-`INITIALIZED` override, finding disposition, Gate 5 lifecycle act,
AC-005's qualified objective-attribution confirmation, exact-hash artifact
fitness, `CHECKING`, `ISSUED`, release, merge, and professional reliance remain
separate owner acts unless later stated explicitly.

No later P1 node opens automatically. This source slice records first-node
evidence for the later DEL-10-10 bootstrap progression; it performs no runtime
self-ingestion and no PEC capability cutover.

## Rollback and strict non-effects

Before publication, rollback deletes only newly created O-A source/profile/run
records and restores D-PEC-74 coordination pointer edits. The frozen corpus is
never a rollback target. After publication, corrections use a forward commit
and successor record; ruled or accepted bytes are never silently rewritten.

This authority creates no v2 bytes by itself, advances no lifecycle, accepts
no artifact, opens no other P1 node, resolves no retained product decision,
starts no service/store/runtime/network act, authorizes no release or
professional reliance, and imposes no architecture or consumer duty on
another loop.
