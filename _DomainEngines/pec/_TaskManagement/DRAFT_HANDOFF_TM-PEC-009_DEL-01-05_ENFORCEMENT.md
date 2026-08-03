# DRAFT — PEC handoff package for TM-PEC-009

**Delivery status:** ROUTED BY OWNER RULING — 2026-08-02

**Routed request:**
`projects/pec/execution/_Coordination/TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/REQUEST_TM-PEC-009_DEL-01-05_PACKET.md`

**From:** PEC TASK_MANAGEMENT

**To:** PEC Agent 0 / D-PEC packet route

**Register row:** `TM-PEC-009`

**Purpose:** Prepare, but do not presume, a successor D-PEC packet that can
make DEL-01-05 zero-dependency and locality enforcement executable, then
preserve the separate DEL-01-06 RF-001 SELF_CHECK rerun gate.

## Why this handoff is now activatable

D-PEC-75 declined DEL-01-05 as the second P1 slice because no v2 core package
then existed: its fail-closed SOW could not name a real service-core target,
and inventing a marker or scanning all of `v2/` would have exceeded or
misstated the deliverable. The current tree now contains an established typed
core port plus a replaceable JSON config adapter. That removes the earlier
physical bootstrap absence, but it neither authorizes source production nor
repairs the DEL-01-05 contract's stale and unresolved statements.

## Bound evidence

| EvidenceRef | EvidenceSha |
|---|---|
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv`, row `RF-001` | `fa04561fe97cc33cc8198ef2f5dfa31b4c92f4aff41d591556e312f1e2e735bb` |
| `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md` | `65064ec696ce57cb743ca50a99abef52ac58746a2fd04f820149ab71442e130d` |
| `projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/PACKET.md`, “DEL-01-05 guard-first” | `065241b87fe97b8b8227ef4e9ad09d74baa6b8b04043779018ae00c7aa10e300` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md` | `ce51490178a4e07f4266a09e156e2b8d7bca618a41477f57eb746b4596b49824` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_STATUS.md` | `f7cb08a6e229b6195a239547c09b47f00cdccd73a723f93ea05a8cb25feae9d9` |
| accepted DEL-00-01 `artifacts/v2/ADRs.md` | `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5` |
| `projects/pec/v2/src/pec_v2/core/ports/loop_registry.py` | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` |
| `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py` | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` |
| `projects/pec/software-workflow.json` | `4ef630f4ab0bf51480ff83e3e8844e71cc827cf4ddddb1268c727a03d1b45cbc` |

## Requested D-PEC packet contents

The successor packet should present the owner with a bounded option that,
only if selected, authorizes the following ordered work:

1. **Contract currency.** Route DEL-01-05 to `WORKING_ITEMS` to amend only
   the production contract statements made stale or resolvable by accepted
   intervening state: accepted decomposition revision 1.3; lifecycle
   `INITIALIZED`; the selected DEL-00-01 hexagonal core-isolation style; the
   real `projects/pec/v2/src/pec_v2/core/**` target; and the live Python /
   standard-library source posture. Preserve requirements, identifiers,
   objective attribution, open decisions, acceptance gates, and artifact
   class unless the packet expressly presents a consequential amendment for
   owner ruling.
2. **Contract review.** Route the resulting exact SOW bytes through `REVIEW`
   before source production. Contract acceptance must not satisfy any
   future-production criterion or advance lifecycle by implication.
3. **Source production.** Name every allowed path for the two assertions,
   admitted-set configuration, standing registration, posture note,
   fixtures/tests, run records, and workflow registration. Name prohibited
   paths explicitly. The packet must not authorize edits to decomposition,
   PRD, accepted DEL-00-01 bytes, DEL-01-06 source, or another loop.
4. **Verification.** Bind production to DEL-01-05 AC-001 through AC-011 and
   VER-001 through VER-009, including positive/negative dependency fixtures,
   egress and local-transport fixtures, missing/unreadable/tool-failure
   fail-closed cases, registration-removal mutation, before/after source and
   manifest checks, and explicit proof that the mechanism itself performs no
   network call or service-core mutation.
5. **Authority question.** Present CON-002 / AC-011 faithfully: the owner may
   confirm or decline release-gating force. Do not infer force merely from a
   blocking verdict. Preserve OI-009 / SOW-083 and the graceful-absence rule.
6. **Rollback and authority fence.** Define rollback as removal/reversion of
   only the packet-named DEL-01-05 additions and registrations. State that no
   governed act, later P1 node, release, lifecycle transition, artifact
   acceptance, or professional reliance follows without its separate gate.

## Required downstream sequence

If DEL-01-05 is lawfully produced and reviewed, the result must return to
`REVIEW` for its exact owner gates. Only after the enforcement is available
may DEL-01-06 RF-001 be reopened and its six-item SELF_CHECK rerun using the
exact DEL-01-05 enforcement evidence required by VER-005. `TM-PEC-009` is not
closed by packet selection, source production, or DEL-01-05 acceptance alone.
Its closure evidence is the later DEL-01-06 SELF_CHECK result that closes
RF-001 without waiving VER-005.

## Non-effects of this draft

Routing this draft does not mint a D-PEC ID, select an option, amend a deliverable,
authorize source, dispatch a manager, reopen RF-001, satisfy any acceptance
criterion, alter lifecycle, authorize release, or change `TM-PEC-009`.
