# Orchestration Plan — Root v3 Phase 0d

PlanVersion: `1`

SelectionAuthority: `HUMAN`

Posture: `TERMINAL_FAN_OUT_IN` (one bounded node, followed by fresh read-only review)

AcceptedBasis: `origin/main@3da1eb38bff55deb6d08e2c5e44947fe1fb56315`

Owner: `Ryan Tufts (K-AUTH-1)`

## Objective

Execute exactly N1 from the owner-carried Phase-0d steer: transcribe R3-A/R3-B
into SCA-004 and draft, without applying, the exact Gate-5 application package.

## Node and ownership

| Node | Executor | Content write target | Control evidence | Depends on | Expected return |
| --- | --- | --- | --- | --- | --- |
| N1 | bounded ephemeral Agent 2 (`role not mechanically enforced`; instruction-asserted) | `execution/_ScopeChange/SCA-004_2026-08-22_1749/**` only | `instances/N1_GATE5_PACKAGE/**` | passed basis gate; R3-A/R3-B | complete package, validator PASS/count, approved-byte preservation evidence, blockers |

The content write target is exclusive. The executor may not write live
decomposition, `_LATEST.md`, lifecycle, Task Management, tools, runtime,
projects, plans, docs, agents, or any other repository content. Runtime
control-plane evidence is not project authority.

## Fan-in gates

1. Every Phase-0d artifact required by the steer exists in the SCA-004 folder.
2. Gate-3 validator remains PASS 98/98 and its JSON is byte-identical.
3. Gate-5 validator passes with zero failures and records a deterministic
   check count.
4. All protected approved/live bytes remain identical.
5. Append dry-run passes against a scratch candidate-at-live-path layout.
6. A fresh read-only Agent 2 review returns zero actionable findings; findings
   trigger bounded repair and another fresh review.

## Human gates retained

Gate-5 append approval, Gate-5 execution authorization, and pointer authority
remain separate future owner acts. Gate 5 is not executed in this run.

