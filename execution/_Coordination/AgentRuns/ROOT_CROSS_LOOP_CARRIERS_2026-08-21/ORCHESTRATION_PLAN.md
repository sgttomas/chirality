# Orchestration plan — Root cross-loop carrier unblock

- RunID: `ROOT_CROSS_LOOP_CARRIERS_2026-08-21`
- Plan version: `1`
- Selection authority: `HUMAN`
- Descriptive posture: `MIXED`
- Repository basis: `origin/main@e3e18d277a4b902e2a3347235239e90e946b91f4`
- Working branch: `codex/root-cross-loop-carriers-20260821`
- Integration owner: `HELP_HUMAN`
- Human gate owner: Ryan Tufts

## Aligned objective and authority

The owner directed one Root tranche to: (1) implement `TM-ROOT-125` by
aligning the Root agent-instruction validator, tests, and
`AGENT_HELP_HUMAN.md` frontmatter with the ratified Agent 0 direct-`TASK` and
explicit-generalist doctrine; (2) prepare, but not rule or implement, the
`TM-ROOT-117` D-APP-48 successor-identity decision; and (3) assess
`DEL-02-06` compatibility completion, produce the largest lawful slice, or
return the exact owner slate. The same direction requires one branch, one PR
against `main`, dependency-ordered commits, one Root receipt transcribing the
steer, no `artifact-proof` label, and no merge.

The standing Root workplan is idle and creates no production authority. The
current owner direction is the separate bounded lane. Human-only acceptance,
Task Management dispositions not expressly directed here, DEL-02-06 epoch
selection, exact-byte semantic acceptance, lifecycle, release, reliance, PR
review, and merge remain human acts.

## Nodes, ownership, and dependencies

| Node | Role | Scope | Writes | Depends on | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|
| H1 | `HELPS_HUMANS` | `TM-ROOT-125` validator/frontmatter/tranche/notice engineering | `agents/AGENT_HELP_HUMAN.md`; `tools/validation/validate_agent_instructions.py`; `tools/validation/test_validate_agent_instructions.py`; one new G4 manifest; affected-loop notices; H1 return | Step-0 preflight | exact diff, test evidence, pin/mirror census, compatibility statement | validator tests, full agent validator, G4, targeted policy checks, diff hygiene |
| T1 | `TASK_MANAGEMENT` | mandatory federation; `TM-ROOT-117` decision preparation; `DEL-02-06` activation/compatibility-gate assessment | T1 return only; no register, deliverable, foreign-loop, or authority writes | Step-0 preflight | decision-ready options, non-binding recommendations, exact gates/evidence | parent reopens cited live sources and confirms no human ruling was inferred |
| I1 | `HELP_HUMAN` | cross-node fan-in and decision-support materialization | this RunID's decision packet, validation, and handoff records | H1 + T1 | integrated tranche and parked human decisions | disjoint-write check; current-source revalidation |
| C1 | `TASK_MANAGEMENT` through `HELP_HUMAN` | owner-directed `TM-ROOT-125` closure after engineering commit evidence exists | Root register/archive and ordinary Root receipt/notice closeout surfaces only | H1 engineering commit + validation | `RESOLVED_WITH_CHANGE` row move with exact evidence SHA; no foreign-register write | register validation, federation, receipt rules, G0–G4, full scoped tests |
| G1 | `CHANGE` through ordinary Git closeout | dependency-ordered commits, push, and one ready PR against `main` | Git metadata only | I1 + C1 | branch/commit/PR evidence; no merge and no artifact-proof label | clean status, branch ancestry, required checks |

## Concurrency and failure isolation

H1 and T1 may run concurrently because T1 is read-only and their content
ownership does not overlap. I1 serializes their returns. C1 is held until the
validated H1 engineering commit exists so `TM-ROOT-125` closure can bind exact
evidence. A T1 decision gate does not block H1 or C1. Any failed H1 check
blocks only `TM-ROOT-125` closure and its App notice; decision preparation may
still land with the exact blocker recorded.

## Human decision points

1. `TM-ROOT-117`: select an exact Root successor identity and accept its
   recorded bytes, or direct App to re-scope `TM-APP-032`.
2. `DEL-02-06`: supply the future positive decimal Root epoch and rule the
   exact compatibility-completion package, or return/defer it. No agent may
   mint that owner-supplied epoch.
3. Review and merge the final PR. No agent merge is authorized.
