# Frozen work graph v1

Frozen before child dispatch. Selection authority: direct owner direction,
2026-08-09. Posture: `MIXED`, dependency-serialized.

| Node | Objective | Depends on | Write owner | Release gate |
|---|---|---|---|---|
| N1 | Fresh taint clearance of six exact salvage files and all 80 ledger rows | none | fresh Agent 2, `taint_clearance/**` and its return only | durable PASS plus independent manager acceptance |
| M1 | Independently reproduce N1 hashes, full pattern scan, row/provenance resolution, actual-command allowlist conformance, and four-root preservation | N1 | manager, `validation/TAINT_ACCEPTANCE.md` | explicit `ACCEPT` only |
| N2 | Author packet components aligned bijectively to cleared ledger | M1 | fresh Agent 2, `packet/components/**` only | terminal author-component return |
| N3 | Integrate literal runbook, LLDB script, evidence/ingestion contracts, index, and terminal author return | N2 | fresh integration Agent 2, `packet/**` excluding `components/**` plus `returns/AUTHOR_RETURN.md` | manager packet acceptance |
| M2 | Reproduce allowlist/actual-command checks, 80-row bijection, whole-packet historical-identity zero scan, completeness and coherence | N3 | manager, `validation/PACKET_ACCEPTANCE.md` | explicit `ACCEPT` only |
| M3 | Freeze every governed packet byte into deterministic manifest and aggregate packet hash; authors stop writing first | M2 | manager, `freeze/**` | immutable freeze recorded |
| N4 | Exactly one genuinely fresh read-only verifier over frozen bytes and current authority | M3 | fresh Agent 2, `verifier/**` only | durable `PASS` or whole-lineage BLOCK |
| M4 | Validate verifier return and stop at exact-execution-approval gate | N4 | manager terminal records | hash-bound owner request only |

Edges are `N1 -> M1 -> N2 -> N3 -> M2 -> M3 -> N4 -> M4`. No node may
release a dependant without the predecessor's explicit accepted state. N2 and
N3 overlap semantically but not in write ownership: N2 owns component drafts;
N3 is the sole integration owner and must not mutate N2's component evidence.

## Structural allowlist fence

Every child brief must enumerate every readable file or run-local readable
directory, exact writes, forbidden roots, outputs, checks, stage and total time
expectations, and proposed inspection commands. Pre-dispatch and fan-in
validation reject:

- any read/search path not present in the applicable exact allowlist;
- any repository-root, project-root, AgentRuns-root, or directory-recursive
  search;
- any unresolved glob, command substitution, environment-expanded search
  root, or pattern-exclusion-only fence;
- any command whose explicit path arguments can traverse a forbidden root.

At each checkpoint the manager records exact durable file count, total bytes,
delta, current stage, and native-context telemetry availability. The first
checkpoint is no earlier than the first-stage expectation. A child is
interrupted only after one full declared checkpoint interval with zero new
durable output; the on-disk state is recorded in that event.

## Absolute forbidden roots

1. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_2026-08-09`
2. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_ATTEMPT3_PACKET_PREPARATION_V2_2026-08-09`
3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_FRESH_PACKET_AUTHORING_2026-08-09`
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_THIRD_PACKET_AUTHORING_2026-08-09`, except the six exact salvage files enumerated in the N1 allowlist. All other third-root bytes are forbidden.

Manager access to blocked roots is limited to Git tree identities, the six
owner-authorized salvage bytes, and terminal records for preservation/causal
closeout. Blocked prose is never an authoring source.
