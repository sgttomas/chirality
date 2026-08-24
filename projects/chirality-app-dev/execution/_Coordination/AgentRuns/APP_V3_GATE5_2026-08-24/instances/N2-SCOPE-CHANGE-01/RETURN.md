# N2 Return — Atomic Decomposition Application

**Node:** `N2-SCOPE-CHANGE-01`
**Role:** `SCOPE_CHANGE` Agent 1
**Basis commit:** `cc196023a5532fe58955655c1144cd09ee88343a`
**Verdict:** `PASS`
**Authority effect:** `AUTHORIZED_GATE5_DECOMPOSITION_POST_IMAGE_APPLIED`

## Fail-closed preconditions

Before the write, the live decomposition target was independently required at:

- SHA-256 `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`;
- `108079` bytes.

The private N1 candidate was independently required at:

- `/private/tmp/chirality-gate5-n1-candidates.eJwTTx/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`;
- SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`;
- `112419` bytes;
- mode `0600`.

The rollback copy was independently verified as source Git blob
`48ae8edf982f3ce92e7a686993f3832501e42576`, SHA-256
`dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`,
and `108079` bytes at
`/private/tmp/chirality-gate5-n1-recovery.UzeIkF/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.

The candidate diff contained exactly the approved D-01 through D-05 changes:
four removed transaction lines, six added transaction lines, four stable
carrier-row replacements, one DEC-023 insertion, and one SCA-APP-008 change-log
insertion. No other candidate difference existed.

## Atomic application result

The complete approved candidate was applied to the exclusive live target with
`apply_patch`; no copy, shell overwrite, checkout, reset, or broad restoration
operation was used.

Immediately after application:

| Check | Result |
| --- | --- |
| Live target SHA-256 | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` — PASS |
| Live target bytes | `112419` — PASS |
| Byte comparison with private approved candidate | identical (`cmp` exit `0`) — PASS |
| Removed D-01..D-05 transaction lines | four lines; each occurs `0` times — PASS |
| Added D-01..D-05 transaction lines | six lines; each occurs exactly `1` time — PASS |
| `DEC-023` row | exactly `1` — PASS |
| SCA-APP-008 change-log row | exactly `1` — PASS |
| Candidate diff size | `6` insertions, `4` deletions — PASS |
| `git diff --check` on the target | PASS |

## Topology and stable-relation proof

The verified Git-blob pre-image and applied post-image were parsed independently.

| Invariant | Result |
| --- | --- |
| Package topology | exactly `10`; package ID/order unchanged — PASS |
| Deliverable topology | exactly `51`; deliverable ID/order unchanged — PASS |
| Parent-package bindings | unchanged for all 51 deliverables — PASS |
| Deliverable stable identity | ID, name, responsible party, and type unchanged — PASS |
| SOW / covered-scope relations | unchanged for all 51 deliverables — PASS |
| Objective relations | unchanged for all 51 deliverables — PASS |
| Context-envelope relations | unchanged for all 51 deliverables — PASS |
| Context-envelope sizing | unchanged for all 51 deliverables — PASS |
| Objectives section | byte-identical; SHA-256 `f6225081d94096d443a5fab089c7806f168a89ce8501e829680d0eb3a714fb6d` — PASS |
| Packages section | byte-identical; SHA-256 `6d85a5c8bb6d40709aa02f5a08fbeef2bd605b7032ad91022ab9b25545482a67` — PASS |
| Scope Ledger | byte-identical; SHA-256 `b58500f1f842545f23fd98c3e70d778c1258a59a43580e6e4fb8011244143baa` — PASS |

The accepted SCA snapshot still states that D-APP-103 **defers**. No file whose
name matches a decision-replay packet exists in that snapshot, and N2 created
no decision-replay packet.

## Containment

N2 wrote only:

1. `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`;
2. this node's evidence files under
   `execution/_Coordination/AgentRuns/APP_V3_GATE5_2026-08-24/instances/N2-SCOPE-CHANGE-01/`.

Concurrent N3 changes to `projects/chirality-app-dev/docs/CONTRACT.md`, the
live companion register, and N3 evidence were observed as sibling-owned shared
worktree state. N2 did not inspect them as application inputs, modify them,
stage them, restore them, or treat them as N2 outputs.

N2 did not edit any dependency record, pointer, accepted snapshot file,
contract, companion register, frontend, Root path, Task Management register,
status/SOW/lifecycle surface, or receipt. N2 did not stage or commit.
