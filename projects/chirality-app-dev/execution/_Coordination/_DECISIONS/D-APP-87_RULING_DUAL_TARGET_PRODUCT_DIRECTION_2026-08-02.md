# D-APP-87 — Ruling: Dual-Target Product Direction and Re-plan

Status: `RULED — OPTION B WITH OWNER AMENDMENT`

DecisionID: `D-APP-87`

Date: `2026-08-02`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Selected proposal:
`execution/_Coordination/_DECISIONS/D-APP-87_PACKET_DUAL_TARGET_PRODUCT_DIRECTION_2026-08-02.md`
at SHA-256
`079d9b9874a3a0e37d6778d907329a360efab63996a134fa67738ef3f186a577`.

Task Management link: `TM-APP-025` (maintenance remains a separate
`TASK_MANAGEMENT` act).

## Exact owner ruling

The owner returned exactly:

> APPROVE D-APP-87 OPTION B — AMENDMENT: treat "one lightly skinned codebase rather than a shared core with target-specific shells" as a hypothesis the re-plan must test; the two-target requirement and domain-first delivery emphasis are adopted as stated.

No omitted architectural selection, scope amendment, generic runtime grant,
or broader effect is inferred.

## Selected semantics

Option B is selected with the exact owner amendment above.

The App loop adopts these planning inputs as stated:

- two delivery targets: the standalone Chirality Desktop app and a per-domain
  control-plane target; and
- domain-specific applications as the primary delivery vehicle for the agents.

The implementation form is not adopted. Specifically, “one lightly skinned
codebase rather than a shared core with target-specific shells” remains a
hypothesis that the bounded re-plan must test against the live architecture,
source/package topology, accepted scope, deliverables, and validation needs.
The re-plan must present the evidence and tradeoffs without silently selecting
either implementation form.

## Authorized re-plan

The packet's bounded App re-plan is authorized across UI, packaging, affected
deliverables, validation, and runtime affected-client needs. It must return a
later `PROPOSAL` for owner ruling before any PRD, decomposition, SCOPE_CHANGE,
deliverable, public-contract, packaging-identity, runtime, or implementation
effect.

Generic runtime, sandbox, identity, version, resume, and Bash work remains
`BLOCKED_BY_ROOT` while Root `TM-ROOT-105`, `TM-ROOT-107`, and
`TM-ROOT-109`, together with their Piping-response prerequisites, remain
unresolved. The re-plan may inventory App affected-client requirements but may
not define or implement the generic contract.

## Preserved boundaries

- The Root owner-intent record and routed notices remain coordination inputs;
  this App ruling is the planning-input act.
- This ruling does not amend the PRD, accepted decomposition, SCOPE_CHANGE,
  deliverables, or source.
- It grants no Agent-2 Bash, sandbox, Pi capability, provider/network
  expansion, Root/Piping/PEC write, lifecycle, release, publication, or
  professional-reliance authority.
- Task Management register maintenance remains outside this ruling tranche.
- The six D-APP-81 historical relations remain
  `HISTORICAL_RELATION_UNKNOWN`.

## No-effect boundary

Recording this ruling creates no re-plan result, architectural selection,
runtime/frontend/deliverable write, Task Management disposition, receipt,
commit, push, or merge effect. It authorizes only the bounded planning work
and preserves its later owner gates.
