# W6 launch brief — complete post-N0 DEL-02-06 planning graph

Role: `WORKING_ITEMS` (Agent 1)
Node: `W6`
Plan: `ORCHESTRATION_PLAN_V12.md`

## Objective

Accept the validated W5/N0 fan-in, release the already sealed N1/N2/N3
planning nodes through actual bounded Agent 2 sessions with disjoint writes,
validate their returns, then execute the declared N4→N5→N6 sequence. Return a
decision-ready no-implementation recovery planning package and stop at the
human semantic/implementation gate.

## Frozen upstream evidence

- accepted Scope of Work `dc78196e…0146`;
- owner packet acceptance `7ddbef04…a70f7`;
- accepted manifest `360f8f12…d508f`;
- acceptance record `ee035e91…40760c`;
- application evidence `ae5b423e…ebd57`;
- fresh N0 return `ca8c1b18…ac522`;
- N0 basis report `e11d4c28…97cd8`;
- W5 return `93889920…7c3e` and status `1308e3ee…c5c6c`.

## Required execution

1. Verify frozen evidence and the exact existing briefs `briefs/N1.md`,
   `N2.md`, and `N3.md`.
2. Dispatch N1/N2/N3 concurrently through three real fresh bounded Agent 2
   sessions; accept only terminal, source-cited, write-contained returns.
3. If their fan-in is complete and non-contradictory, dispatch N4 using
   `briefs/N4.md` as the sole integration writer.
4. Validate N4, then dispatch a fresh read-only N5 using `briefs/N5.md`.
   The verifier must not repair; material findings return to WORKING_ITEMS/N4
   for explicit disposition and recheck.
5. After accepted N5, dispatch N6 using `briefs/N6.md` to assemble the exact
   owner-gate handoff from accepted returns only.
6. Persist actual child parentage, briefs, statuses, returns, hashes, manager
   acceptance, held gates, and terminal W6 return/status.

## Hard stops

No implementation or executable tests; no runtime/client/project writes; no
software-profile or registered-check adoption; no semantic choice by
implication; no SCA/decomposition/PRD, lifecycle/release/reliance, Task
Management, Git, merge, or foreign-loop write. Do not claim DEL closure:
closure still requires applied runtime bytes, executable restart/replay proof,
exact evidence, and owner acceptance. Escalate any need to expand reads,
writes, authority, or select a semantic value.
