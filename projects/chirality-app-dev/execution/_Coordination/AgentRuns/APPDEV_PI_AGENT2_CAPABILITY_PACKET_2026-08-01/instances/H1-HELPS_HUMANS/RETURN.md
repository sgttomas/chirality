# HELPS_HUMANS Manager Return — D-APP-84 Packet

Status: `COMPLETE / VALIDATED`
RunID: `APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01`
AcceptedBasis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

## Changed paths

- `execution/_Coordination/_DECISIONS/D-APP-84_PACKET_PI_OMLX_AGENT2_CAPABILITY_EXPANSION_2026-08-01.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md` — one D-APP-84 `AWAITING_RULING` row.
- `execution/_Coordination/AgentRuns/APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01/**`

All paths resolve under `projects/chirality-app-dev/`. No other surface was
changed.

## Evidence basis

The packet rederives claims from D-APP-60, D-APP-64, D-APP-72, D-APP-73,
D-APP-76, D-APP-83, SCA-APP-002/003, the accepted App decomposition, Root
DEL-02-06 ScopeOfWork/status, App CONTRACT/SPEC/PRD/PLAN/TYPES, and current
Root/App runtime seams. The owner-intent record is treated as coordination
only.

Three bounded read-only Agent 2 evidence returns and one independent
refutation return are persisted under `children/`: runtime seams,
authority/classification, packet conventions, and final packet verification.

## Decision request

```text
DecisionID: D-APP-84
RequestedBy: HELPS_HUMANS
Question: Which bounded App policy, Root-routing, exact-version, multi-tool/write, shell, and durable-resume selections should govern a prospective Pi/oMLX Agent 2 expansion beyond D-APP-72?
Options: Select B1 with one token each from V, T, S, and R; S2 requires T1; B2, B3, and D are standalone terminal responses.
Recommendation: B1 + V1 + T1 + S1 + R1. This is explicitly non-binding.
Evidence: D-APP-84 packet §§1-9 and the persisted Agent 2 returns.
DownstreamBlocked: Capability implementation; K-ENGINE-6 amendment; Root DEL-02-06 activation/identity/runtime semantics; version concordance; App SCOPE_CHANGE and affected-client conformance.
```

## Options and recommendation

- B separates App affected-client authority from Root semantic ownership;
  only B1 opens the V/T/S/R selections.
- V makes the `0.80.10` authority / `0.82.0` executable conflict owner-visible.
- T separates multi-read/read-write/registered-tool policy.
- S presents arbitrary Bash separately with its full-root/serialized cost.
- R separates strict replay-and-bind, deferral, and fresh-session-only posture.
- D declines expansion without pretending to resolve version drift.

The recommendation is `B1 + V1 + T1 + S1 + R1`: proceed with the App
affected-client envelope and separate Root route; conditionally align to
`0.82.0`; allow multi-tool reads, exact-target writes, and registered tools;
defer arbitrary Bash; accept the resume design but hold activation behind
Root identity and exact-version gates.

## Conflicts, gaps, and blocked work

1. Root OUT-002 remains Root-owned despite the App register's “carries”
   direction. The packet preserves and returns that conflict through B.
2. The Pi version is not concordant between authority and executable bytes.
   The packet returns it through V.
3. Root DEL-02-06 is initialized but not activated; OUT-001..009 are absent.
4. The promoted Root Pi engine factory is not the active packaged-daemon
   caller; App compatibility and Root runtime seams would otherwise be edited
   twice.
5. There is no durable Pi resume implementation, unified identity tuple, or
   registered shared-runtime Pi tool execution plane.

No conflict requires silent reconciliation. Downstream work stops at the
owner gate and, under B1/B2, the later separate Root gate.

## Checks

- `git diff --check`: PASS.
- AgentRuns JSON parse: PASS.
- D-APP-84 uniqueness and packet/register linkage: PASS.
- Referenced prospective file existence: PASS after removal of one nonexistent
  draft path.
- Write containment: PASS; only the packet, register row, and RunID records
  differ from HEAD.
- Protected surfaces: PASS; no authority docs, runtime, frontend,
  decomposition, deliverable, Task Management, receipt, SCOPE_CHANGE, parity,
  or historical-UNKNOWN surface changed.
- Independent adversarial packet review: `COMMIT-SAFE`; persisted at
  `children/A2-PACKET-ADVERSARIAL/RETURN.md`. The verifier found and caused
  repair of one nonexistent path, version-pin wording, and two option-interface
  contradictions before returning the verdict.

## Git and lifecycle

No commit, push, merge, scope acceptance, implementation, or lifecycle effect.
The branch remains a proposal worktree. The next lawful owner is the App
owner, after independent verification and Agent 0 fan-in.
