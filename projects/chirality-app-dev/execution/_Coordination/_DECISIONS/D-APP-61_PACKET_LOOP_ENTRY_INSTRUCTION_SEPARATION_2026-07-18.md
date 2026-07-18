# D-APP-61 — Development-loop entry and instruction separation recovery

**Status:** PROPOSAL — AWAITING_RULING
**Date prepared:** 2026-07-18
**Prepared by:** app-dev loop operator (agent) at the owner's direction below.
Packet preparation is authorized; adoption, ruling, and every implementation
selection remain the owner's acts (K-AUTH-1; D-GOV-04).

## Preparation direction — evidence, not ruling

The following owner direction is the durable preparation basis. It is quoted
in full so the packet's authorization and constraints are reconstructible. It
does **not** select any option in this packet.

<!-- BEGIN OWNER PREPARATION DIRECTION VERBATIM -->
Your assessment is accepted, with these amendments to the recovery plan:

1. **Nothing on `main` needs repair.** PR #268 never merged, so the ruled workplan bytes, the receipts ledger through Receipt-61, and the LOOP_INIT convention home are all intact on `main`. Drop your step 3 as a separate action — build the new tranche from `main` directly. Close PR #268 unmerged (owner concurs), keep the branch as reference; do not force-push over it, since your AgentRuns evidence lives there.

2. **Prepare D-APP-61 as a decision packet from `main`**, with your five enumerated matters as a separable slate. Two hardening requirements: (a) the packet must quote **verbatim** every piece of standing text it proposes to delete or relocate — the full model-agnostic convention and the LOOP_INIT §7/§8 text — so the owner's ruling binds enumerated content and the authorization is durably reconstructible; this is the direct fix for the Receipt-62 defect. (b) The model-convention disposition is presented as owner options (rescind / re-home to a named surface), not as your selection.

3. **Workplan changes go through supersession only**: the packet stages the amended plan as an appendix, and after ruling you mint it under the next actual local-date filename. The 2026-07-17 file is never edited again.

4. **Validator contract in the packet**: keep the tagged-launcher byte-parity check unchanged (it is verified good); replace vocabulary bans with structural-duplication detection plus an explicit allowance for by-reference citations of canonical instructions; agent-name patterns case-sensitive.

5. **Record this episode as a near-miss in the app-dev corpus (NM-5)**: calibrated verification ran, but the sealed brief was authored by the same context that produced the change and scoped its claims to the change's *intent* rather than to what the *ruled record protects* — so exact-text provenance of an adopted artifact and disposition of a deleted owner convention went untested. The standing correction: refutation claims for governed-artifact writes are derived from the D-APP-60 S1 governed-artifact enumeration — every governed artifact the diff touches generates a claim about that artifact's rules — not from the tranche's own description of itself. Record it supersede-never-edit, and note it is a candidate offer to the piping loop, which is importing near-misses.

6. **Hold the piping mirror** (`codex/piping-help-human-entry-separation`) until D-APP-61 is ruled; the packet should name the mirror explicitly so the corrected pattern ports once.

7. Your step 7 stands, strengthened: the redo verifier's brief must include the claim "the staged diff equals the ruled delta exactly, and no other byte differs from `main`," alongside the enumeration-derived claims from item 5.

Stage the packet, stop at AWAITING_RULING, and return it to the owner. No merges, no piping writes.
<!-- END OWNER PREPARATION DIRECTION VERBATIM -->

## Why a new decision is required

Closed PR #268 established useful candidate mechanics but did not establish a
recoverable owner ruling over their content. It also would have edited the
D-APP-60-minted workplan in place, removed an owner-revised convention without
an explicit disposition, and enforced vocabulary rather than duplicated
mechanics. Because these are normative and adopted-record changes, D-APP-60's
class test rejects them at the limits screen: they are owner-class.

Nothing defective landed on `main`. PR #268 is closed unmerged and its branch
is retained at `35c922e2a83297db7434bb9a3986f6be55154f9d` as evidence. This
packet is a fresh, separable decision gateway from `main` at
`b495fe19b470b68a87a791708c1b21bf75951900`.

## Requirements, objectives, methods, and predeclared validation

| ID | Requirement and source | Objective | Validation before implementation |
|---|---|---|---|
| R1 | Human entry may be untyped, Agent 0, or Agent 1; TASK is not top-level (`AGENTS.md`, Delegation and Entry Rules). | If selected, make the open-ended app-dev launcher instantiate only its entry role and leave downstream runtime behavior canonical. | Local/root tagged launcher byte parity; launcher contains root and HELP_HUMAN reads; no Agent 2 entry. |
| R2 | The workplan is the single development-loop instruction surface; runtime doctrine lives in canonical agent instructions (F-APP-5; root and project `AGENTS.md`). | Remove duplicated runtime topology/mechanics from loop surfaces without removing loop protocol, authority, gates, or verification obligations. | Exact carry-forward diff; by-reference semantics remain resolvable; current plan untouched. |
| R3 | Owner-revised model convention currently declares LOOP_INIT as its home (verbatim Appendix Q). | Obtain an explicit owner disposition: rescind, or relocate verbatim to one named governed surface. | Selected option named in ruling; source and destination exact-text comparison; no silent loss. |
| R4 | Immutable receipts refer to former “LOOP_INIT §7 defaults” (LOOP_INIT §8). | Preserve a durable historical interpretation after renumbering. | Compatibility sentence survives in the ruled LOOP_INIT delta; old receipts remain untouched. |
| R5 | Validator evidence must test mechanics, not ban ordinary vocabulary; closed PR #268's tagged-launcher parity check survived adversarial repair. | Retain parity behavior and detect structural duplication while allowing canonical citations. | Positive citation fixtures; negative duplicated-mechanics fixtures; case-sensitive role-name fixtures; no bare-word rejection. |
| R6 | Ruled workplans are immutable historical artifacts; app-dev supersedes by newer dated file (D-APP-60 S2 and owner direction). | Stage a full candidate in this packet and mint only after ruling under the actual local date. | SHA equality of current plan to `main` and D-APP-60 Appendix W; carry-forward verification of candidate; newest-file resolution after mint. |
| R7 | D-APP-60 verification is enumeration-derived and verdict-after-event. | Ensure the redo verifier covers every touched governed class plus adopted instruction surfaces and the whole diff. | Sealed brief in AgentRuns; independent `COMMIT-SAFE` required; any `BLOCK` remediated and re-run. |

### Evaluation outcome and gateway

The current architecture supports a thin HELP_HUMAN entry without putting
agent selection or operational orchestration into the development-loop
protocol. The launcher chooses only the top-level role; root/project
`AGENTS.md` and that role's canonical instruction package govern runtime
behavior. LOOP_INIT and the workplan remain concerned with discovery,
authority, gates, execution obligations, checks, and handoff.

The five matters below are therefore presented separately. The non-binding
recommendation is **M1-A, M2-A, M4-A, M5-A**. Matter M3 deliberately has no
agent selection: the owner must choose rescission or one named re-home.

## Separable ruling slate

### M1 — Open-ended app-dev entry role

- **M1-A (recommended): HELP_HUMAN entry.** Replace both matching app-dev
  launcher copies with Appendix L; update the app-dev agent table to describe
  HELP_HUMAN as the default supervising entry for this open-ended loop while
  preserving direct Agent 1 entry for already manager-bounded matters. The
  launcher says nothing about selecting downstream managers or specialists.
- **M1-B: retain the current untyped launcher.** No launcher or app-dev agent
  table change. Runtime typing, if any, remains supplied by per-run steer.
- **M1-C: defer.** Leave the entry question open; M2–M5 may be ruled
  independently.

**Risk:** M1-A makes a role selection explicit, but does not guarantee that a
given platform can execute governed children. Canonical runtime instructions
remain responsible for capability/delegation behavior and fail-closed rules.

### M2 — Remove duplicated runtime mechanics from loop surfaces

- **M2-A (recommended): instruction separation.** Replace the complete current
  LOOP_INIT §7/§8 span quoted in Appendix Q with Appendix I, and, only after
  ruling, mint Appendix W under the next actual local-date filename. Appendix W
  removes the Step-4 runtime-topology paragraph and compresses the D-APP-60
  verifier restatement to a binding citation. It otherwise carries the ruled
  plan forward.
- **M2-B: retain current loop mechanics.** Leave LOOP_INIT and the workplan
  unchanged. M1, M3, M4, and M5 may still be ruled independently.
- **M2-C: defer.** No loop/workplan change.

**Supersession rule:** `WORKPLAN_2026-07-17_app_dev_loop.md` is never edited.
If M2-A is ruled, Appendix W is minted under
`WORKPLAN_<ACTUAL_LOCAL_RULING_DATE>_app_dev_loop.md`; only its three explicit
date/lineage tokens are substituted if the ruling date differs from
2026-07-18, and the post-ruling verifier must validate that substitution and
the whole minted file.

### M3 — Owner disposition of the model-agnostic convention

The exact convention is Appendix Q2. **No option is selected or recommended by
the agent.** The owner chooses one:

- **M3-A: rescind.** Delete the convention from LOOP_INIT through M2-A or an
  M3-only LOOP_INIT superseding edit. The ruling must say it is rescinded going
  forward; historical receipts and Git retain its prior status.
- **M3-B: re-home verbatim to root `AGENTS.md`.** Move the full Q2 text, without
  semantic alteration, into root `AGENTS.md` under `Multi-Agent Orchestration`,
  making it repository-wide runtime doctrine. Delete the source copy only in
  the same ruled implementation.
- **M3-C: re-home verbatim to
  `projects/chirality-app-dev/AGENTS.md`.** Move the full Q2 text, without
  semantic alteration, into a named `Runtime capability convention` section,
  retaining project-local scope. Delete the source copy only in the same ruled
  implementation.

**Risk/tradeoff:** M3-B broadens the convention's applicability; M3-C preserves
its current project scope; M3-A removes standing model-assignment guidance.
Only the owner can choose among those value-bearing outcomes.

### M4 — Historical “LOOP_INIT §7 defaults” mapping

- **M4-A (recommended): retain an explicit compatibility sentence.** Use the
  exact Appendix I sentence so historical receipts remain intelligible after
  the section change.
- **M4-B: omit the compatibility sentence.** Git and Appendix Q remain the only
  reconstruction path; no historical receipt is edited.
- **M4-C: defer.** No mapping change.

### M5 — Instruction-entrypoint validator contract

- **M5-A (recommended): parity plus structural duplication.** Implement
  Appendix V. Retain the closed branch's tagged-launcher extraction and exact
  byte-parity behavior unchanged. Replace bare vocabulary bans with
  paragraph/section-level structural signals, explicitly allow by-reference
  citations to canonical instructions, and recognize canonical agent names
  case-sensitively.
- **M5-B: tagged parity only.** Implement the verified parity check and no
  loop-surface duplication detector.
- **M5-C: retain the current validator.** No parity or duplication extension.

## Affected files if ruled

No file in this list is changed by packet staging.

| Matter | Prospective implementation files |
|---|---|
| M1-A | `init/init-prompt.md`; `projects/chirality-app-dev/init/init-prompt.md`; `projects/chirality-app-dev/AGENTS.md` |
| M2-A | `projects/chirality-app-dev/loop/LOOP_INIT.md`; new `projects/chirality-app-dev/loop/WORKPLAN_<ACTUAL_LOCAL_RULING_DATE>_app_dev_loop.md` |
| M3-A | `projects/chirality-app-dev/loop/LOOP_INIT.md` |
| M3-B | M2 source plus root `AGENTS.md` (requires owner-granted root write scope in the ruling) |
| M3-C | M2 source plus `projects/chirality-app-dev/AGENTS.md` |
| M4-A | `projects/chirality-app-dev/loop/LOOP_INIT.md` |
| M5-A/B | `tools/validation/validate_instruction_entrypoints.py`; `tools/validation/test_validate_instruction_entrypoints.py` (requires owner-granted root write scope in the ruling) |

All implementations also update the ruled packet/register disposition, append
a new receipt, and persist post-ruling verifier evidence in the existing
D-APP-61 AgentRuns home. No completion-log entry is written until an
implementation actually lands.

## Piping hold and one-time port

The branch `codex/piping-help-human-entry-separation` is explicitly held. This
packet authorizes no reads-as-writes, cherry-picks, rebases, commits, pushes, or
other modifications to that branch or `projects/chirality-piping/**`. After
D-APP-61 is ruled, the corrected pattern may be offered once to the piping
owner/loop through its own authority. NM-5 is a candidate near-miss offer, not
an imported piping record.

## On-ruling mechanics

1. Transcribe the owner's verbatim selection below, then compute and record its
   canonical SHA-256. Flip D-APP-61 to `RULED`; do not create a separate ruling
   file unless the owner directs one.
2. Derive the exact implementation delta only from selected matters and their
   appendices. Unselected matters produce no byte change.
3. If M2-A is selected, mint Appendix W under the actual local ruling date;
   never edit the 2026-07-17 plan.
4. If M3-B or M5-A/B is selected, treat the ruling as granting only the named
   repo-root write targets; no other root scope is implied.
5. Derive verifier claims first from D-APP-60 S1.2 for each governed artifact
   touched, supplement them for adopted/instruction surfaces, and include the
   exact whole-diff claim. Dispatch a fresh independent read-only verifier.
6. On `BLOCK`, remediate and re-run. On `COMMIT-SAFE`, run the applicable
   deterministic checks, append the execution receipt, commit, push, and open
   an implementation PR. Never self-merge.
7. Only after the app-dev ruling is durable may the corrected pattern and NM-5
   be offered to the held piping mirror through piping's own governed path.

## Human Ruling and Disposition

Reply with a separable selection such as:
`M1-A; M2-A; M3-C; M4-A; M5-A`.

<!-- BEGIN OWNER RULING VERBATIM -->
AWAITING_RULING
<!-- END OWNER RULING VERBATIM -->

Canonical ruling-text SHA-256: `TBD_AFTER_OWNER_ACT`

---

## Appendix L — exact M1-A app-dev launcher candidate

This block must be byte-identical in the project-local launcher and the tagged
app-dev block in the root launcher catalog.

```text
<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.

Set `WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`.

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.

Act as `HELP_HUMAN` for `{WORKING_ROOT}`.

Read `{WORKING_ROOT}/loop/LOOP_INIT.md` and follow it: pursue the loop's
inherent goals as far as live authority permits.

Steer (this run): <none>
</init-prompt>
```

The companion app-dev `AGENTS.md` table delta is exactly:

```text
| `HELP_HUMAN` | 0 | Default supervising entry for the open-ended standing development loop; aligns the human and workflow, supervises discovery and the selected Agent 1 managers, and validates cross-manager fan-in. Direct Agent 1 entry remains lawful for a matter already bounded to one manager. |
```

## Appendix Q — standing text affected by M2/M3/M4

### Q1 — complete current LOOP_INIT §7/§8 span, verbatim from `main`

Every byte below is standing text proposed for deletion, relocation, or
replacement by M2-A, M3-A/B/C, or M4-A/B. The code fence is not part of the
quoted span.

```text
## 7. Multi-agent orchestration

Root `AGENTS.md` and D-GOV-12 govern multi-agent work. The standing workplan
records owner intent, constraints, authorities, and gates; it is not the
current execution graph. At each turn:

1. HELP_HUMAN, when invoked, derives or applies the human-prescribed
   cross-package graph and launches one WORKING_ITEMS instance per activated
   package. A directly invoked WORKING_ITEMS instance derives only its one
   package graph.
2. Record selection authority (`HUMAN | AGENT_0 | AGENT_1`), posture
   (`TERMINAL_FAN_OUT_IN | SUPERVISED_MANY_TO_MANY | MIXED`), nodes,
   dependencies, concurrency, read/write ownership, expected returns, fan-in
   gates, and human decision points before dispatch.
3. Use terminal fan-out/fan-in when terminal child returns are sufficient.
   Use supervised parent-mediated notices when active findings may affect
   siblings. Arbitrary dependency-valid mixed stages need no additional name.
4. Preserve claim status and minimum sufficient evidence in every relay.
   Version objective, basis, scope, ownership, risk, or acceptance changes;
   consequential amendments return to the owner.
5. Shared reads are allowed. Concurrent writes must be disjoint. Serialize
   overlaps or assign one integration owner. Hold only declared dependants
   when a node fails.
6. Persist the actual graph, child sessions, notices, amendments,
   acknowledgments, returns, and handoff under
   `execution/_Coordination/AgentRuns/<RunID>/`. If managed delegation is
   unavailable, defer the multi-agent stage; a receipt may preserve the
   blocker but may not represent brief-only work as an executing child run.

Agent 1 siblings do not delegate or message directly. Agent 2 reports to its
WORKING_ITEMS parent; WORKING_ITEMS reports cross-package notices to
HELP_HUMAN or, in direct mode, to the human.

## 8. Session conventions, constraints, and any per-run steer (formerly §7)

Immutable receipts that say a steer overrides “LOOP_INIT §7 defaults” refer to
this conventions section as numbered when those steers were recorded.

Standing constraints and the loop protocol live in the plan — follow them as
written. The session conventions are:

- Subagent capability assignments (owner-revised 2026-07-12: MODEL-AGNOSTIC —
  no named-model conventions; this section is the convention's home and a
  per-run steer may override; earlier named-model steers, including the
  2026-07-05 convention and loop Receipt 18, are rescinded going forward and
  survive only as historical record): use the session's available models by
  capability tier, not by name. Standard-capability agents for discovery,
  research, summaries, running deterministic checks, and breadth
  verification; highest-capability agents (at high reasoning effort where the
  harness supports it) for planning, for adversarial verification of anything
  that will be recorded as fact, and for execution that touches governed
  artifacts, fences, or rulings; reduced effort only for mechanical execution
  of fully specified changes. Record which model actually ran each dispatched
  role in the governed AgentRuns record and point to it from the receipt;
  when no AgentRuns record exists, the receipt may carry the minimum model
  attribution directly. Never silently substitute mid-wave — a capability-
  tier change within a wave is a receipt-worthy event.

If the owner appended a steer for this run (the launcher's `Steer` line, their
message, or a line below), honor it on top of the plan and over §5's defaults;
the plan still governs the protocol, the fences, and the gate above.
```

### Q2 — full model-agnostic convention, verbatim and separately bound

Q2 duplicates the relevant Q1 bytes deliberately so an M3 ruling binds the
convention independently and reconstructibly.

```text
- Subagent capability assignments (owner-revised 2026-07-12: MODEL-AGNOSTIC —
  no named-model conventions; this section is the convention's home and a
  per-run steer may override; earlier named-model steers, including the
  2026-07-05 convention and loop Receipt 18, are rescinded going forward and
  survive only as historical record): use the session's available models by
  capability tier, not by name. Standard-capability agents for discovery,
  research, summaries, running deterministic checks, and breadth
  verification; highest-capability agents (at high reasoning effort where the
  harness supports it) for planning, for adversarial verification of anything
  that will be recorded as fact, and for execution that touches governed
  artifacts, fences, or rulings; reduced effort only for mechanical execution
  of fully specified changes. Record which model actually ran each dispatched
  role in the governed AgentRuns record and point to it from the receipt;
  when no AgentRuns record exists, the receipt may carry the minimum model
  attribution directly. Never silently substitute mid-wave — a capability-
  tier change within a wave is a receipt-worthy event.
```

## Appendix I — exact M2-A/M4-A LOOP_INIT replacement candidate

This candidate assumes M2-A and M4-A, and assumes the owner's required M3-A,
M3-B, or M3-C selection removes Q2 from LOOP_INIT.

```text
## 7. Per-run steer

Historical receipts that say a steer overrides “LOOP_INIT §7 defaults” refer
to the former session-conventions section quoted verbatim in D-APP-61.

Standing constraints and the loop protocol live in the plan — follow them as
written.

If the owner appended a steer for this run (the launcher's `Steer` line, their
message, or a line below), honor it on top of the plan and over §5's defaults;
the plan still governs the protocol, the fences, and the gate above.
```

## Appendix V — exact validator contract for M5-A

### V1 — retained tagged-launcher parity behavior

Retain, without semantic change from closed PR #268 at reference commit
`35c922e2a83297db7434bb9a3986f6be55154f9d`, these behaviors:

1. extract only complete root-catalog blocks delimited by line-anchored
   `<init-prompt>` / `</init-prompt>` tags;
2. select the block containing exactly the relevant `projects/<name>` token;
3. require exactly one tagged block per governed project;
4. require the project-local launcher bytes to equal that complete tagged
   block exactly; and
5. do not permit an untagged stale copy elsewhere in the catalog to satisfy or
   mask the tagged-block comparison.

### V2 — structural duplication, not vocabulary prohibition

For a project whose launcher explicitly selects HELP_HUMAN, inspect the
current LOOP_INIT and newest workplan by **section or paragraph**, not by bare
word. Report duplication only when one of these structural conditions holds:

- a section declares an execution topology, runtime role-routing matrix, or
  work-graph schema that canonical agent instructions already govern;
- one paragraph couples at least two case-sensitive canonical role names
  (`HELP_HUMAN`, `WORKING_ITEMS`, `TASK`, `CHANGE`, or `Agent 0`/`Agent 1`/
  `Agent 2`) with a routing/dispatch verb (`invoke`, `launch`, `delegate`,
  `dispatch`, `report`, `fan-in`, or `select`) and thereby prescribes runtime
  mechanics; or
- one section contains at least two mechanics clusters from this set:
  selection-authority/posture enumeration; child-session persistence schema;
  parent/sibling relay rules; concurrent-write ownership/fan-in gates; or
  model/capability assignment rules.

Canonical agent-name recognition is case-sensitive. Ordinary lowercase words
such as “task,” and isolated vocabulary such as “work graph,” “fan-in,” or
“orchestration,” never fail by themselves.

### V3 — explicit by-reference allowance

A paragraph is allowed when its operative function is only to cite canonical
instructions or a governed instrument, including:

```text
Runtime hierarchy and delegation are governed by root `AGENTS.md`, the
project `AGENTS.md`, and the active canonical agent instructions.
```

The allowance applies even when the citation uses a canonical agent name or
ordinary mechanics vocabulary. It does not allow a citation paragraph that
also restates who selects, launches, delegates to, reports to, or persists
which child.

### V4 — predeclared fixtures

- PASS: the exact M1-A launcher pair; root/project byte parity.
- FAIL: divergent tagged root block despite an untagged identical stale copy.
- PASS: Appendix I and Appendix W with only canonical by-reference citations.
- PASS: ordinary singular lowercase “task” and isolated mechanics terms.
- PASS: case variants such as `help_human` when they are not canonical role
  names and do not independently satisfy a structural condition.
- FAIL: a paragraph that says HELP_HUMAN launches WORKING_ITEMS.
- FAIL: a paragraph that says WORKING_ITEMS dispatches TASK.
- FAIL: a section that defines child-session persistence plus fan-in ownership.
- PASS: the V3 citation sentence, including named surfaces.

---

## Appendix W — full M2-A workplan supersession candidate

Appendix W is non-operative while this packet is awaiting ruling. Relative to
the ruled 2026-07-17 plan, its enumerated deltas are only: (1) header lineage
and actual-date mint instruction; (2) one D-APP-61 owner-intent bullet; (3)
deletion of the seven-line Step-4 runtime-topology paragraph; and (4)
replacement of the expanded D-APP-60 verifier restatement with a binding
three-line citation. All other bytes must carry forward. The current
`WORKPLAN_2026-07-17_app_dev_loop.md` remains untouched forever.

# App-Dev Work Loop — standing plan (development loop instructions)

> **Epistemic status: agent-authored plan — not authority.** Written at owner adoption
> (Ryan Tufts, K-AUTH-1) on 2026-07-18 through the D-APP-61 ruling; supersedes
> `WORKPLAN_2026-07-17_app_dev_loop.md` in this directory. This plan never authorizes
> work: owner rulings and directions do. Sources govern on any disagreement. This file
> is the project's single development-loop instruction surface — PROTOCOL plus pointer
> indexes; it carries NO status, NO work history, and NO measurements. Each iteration
> re-derives state from the live tree; loop closes append a minimal receipt to
> `LOOP_RECEIPTS.md` beside this file (rules live at the top of that file).

## Owner intent

- **2026-07-04** (Receipt 0): *"All projects should have the current development loop
  structure and workflow, and therefore same type of init prompt."* — this loop is the
  session entry convention (thin launcher → `LOOP_INIT.md` → this plan → receipts).
- **2026-07-10** (Receipt 5): consolidation adopted — *deliverables themselves are the
  means of discovering work*; the plans-as-queue convention is retired; this plan
  absorbs `_COORDINATION.md`'s operative mechanics, and that file is reduced to a
  ruled-record surface; open scope is recorded in deliverable-local `_STATUS.md`
  `## Remaining` sections. Which rehomed lanes are live remains the owner's ruling
  (`D-APP-53`, AWAITING_RULING — see its packet's 2026-07-10 addendum).
- **2026-07-17** (D-APP-59; D-APP-60): the standing decision-latitude delegation is
  adopted and refined into the frozen shared block v1 (one template shared with the
  chirality-piping loop, two local bindings); this plan integrates the D-APP-60
  instrument into selection, gating, execution, and closeout.
- **2026-07-18** (D-APP-61 M2-A): runtime hierarchy, role routing, and child-session
  mechanics remain in canonical agent instructions; this plan retains loop-specific
  discovery, authority, gates, checks, and handoff obligations, citing governed
  instruments instead of restating their mechanics.

**The loop's goal** (agent-phrased; owner may correct the wording): advance
chirality-app-dev per its ruled authorities toward issuance readiness and the PRD
runtime scope, as far as live authority permits — stopping at every owner gate.

## Non-negotiables (the compelling reasons staging remains)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04). **Truthful
   attribution is the one firm limit of the decision-latitude model**: agent decisions
   are recorded as the agent's own; never write a ruling record or `RULED` register row
   attributing to the owner an act that did not occur.
2. **Hard fences below** stop work regardless of eligibility.
3. **Gate state is register-derived** — open `D-APP-XX` rows and per-item `(gated: ...)`
   suffixes in `Remaining` sections are re-derived each iteration, never assumed.

## The loop protocol (every iteration)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log since the
   last receipt; concurrent loops may be live in this monorepo — keep write scopes
   disjoint from `_DomainEngines/**`, `projects/chirality-piping/**`, `projects/pec/**`,
   and treat unrelated dirty files as external state). Run
   `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` and only
   then read the latest applicable receipt(s) in `LOOP_RECEIPTS.md`; a validator
   failure blocks use of the cursor. Check
   `execution/_Coordination/_DECISIONS/_REGISTER.md` for
   rulings newer than the last receipt — new rulings are how work unlocks, look every
   time. Run the D-APP-38 corpus check from the project root
   (`PYTHONDONTWRITEBYTECODE=1 python3
   execution/_Reconciliation/References/reconcile_authority_corpus.py status`); any
   drift is repair-first work under selection principle (a), regardless of which
   tranche introduced it. Enumerate the work surface from deliverable folders:
   `grep -l '^## Remaining' 'execution/PKG-'*/1_Working/DEL-*/_STATUS.md` for open
   scope, and the repo-root practitioner harness `status` command for lifecycle posture
   (an absent `Remaining` section means no recorded open scope for that deliverable).
   Run repo-wide `PYTHONDONTWRITEBYTECODE=1` harness `self-check`. Verify any derivative
   statement — including this plan and your own tasking — against the live tree before
   relying on it; on disagreement the live tree wins and the delta goes in the receipt.
1. **Select — from deliverable folders only.** A `Remaining` item is *selectable* when
   it carries no `(gated: ...)` / `(stage-gated: ...)` suffix, or its named gate is
   ruled; blockedness beyond gates is re-derived from deliverable-local
   `Dependencies.csv` / `_DEPENDENCIES.md` and the accepted DepClosure snapshot
   (`execution/_Reconciliation/DepClosure/_LATEST.md`) — do not infer blocked/unblocked
   state from any hand-maintained summary. Principles, in order: (a) repair failing
   validation for already-landed work before new scope; (b) work that discharges a gate
   prerequisite beats work that doesn't; (c) owner-directed items beat agent-inferred
   ones; (d) the highest-value ungated `Remaining` item. Apply the CONTRACT
   **K-ENGINE-6** strategic lens to every item — Chirality is a
   governance/UI/audit/lifecycle/adapter layer over provider harness mechanics;
   standalone-harness or feature-parity work is OFF-STRATEGY. Never manufacture work
   outside the recorded `Remaining` scope or revive ruled-shut items (a revival takes a
   new register row). *Delegation triage (D-APP-60):* before slating any
   judgment-shaped fork, apply the class test with fast-reject ordering — any touch of
   a recorded limit is owner-class immediately, no lens analysis; the adversarial
   four-lens test runs only on survivors. Decide what clearly passes under the
   D-APP-60 instrument with a recorded rationale artifact; slate what fails or
   survives ambiguously, naming the failed gate in near-miss form. The asymmetry that
   governs the default: over-slating costs owner attention; over-deciding silently
   converts owner authority — only the first is cheap to recover from.
2. **Brief / slate.** Genuinely material or hard-to-reverse forks (a hard-fence
   question, a K-ENGINE-6 strategy fork, a costly public-contract or data-migration
   change, any `Remaining` item marked as needing its own decision packet) get a
   `PROPOSAL` packet registered in the decision register; within the fences, ordinary
   design forks are resolved with recorded agent decision latitude — under the
   D-APP-60 instrument for disposition-class items (decide, record the rationale
   artifact, cite the exercise in the receipt), per-instance latitude otherwise.
3. **Gate.** STOP at the hard fences and at owner-shaped acts; adoption/ruling/direction
   is the owner's (K-AUTH-1; D-GOV-04). The STOP applies to owner-class items;
   disposition-class items proceed under the D-APP-60 method binding and verifier.
   Terminus slates arrive pre-triaged in near-miss form, each item naming the failed
   gate or limit. In-session directions/rulings are recorded verbatim in their governed
   artifact; only chat-only directions with no governed home are transcribed into the
   receipt, labeled as evidence rather than ruling. Directions fully recoverable from
   Git/PR history need no receipt transcription. Record every gate outcome — including
   no-ops and their reason.
4. **Execute + check.** Branch-first + PR is the default; never self-merge; write scope
   stays inside `projects/chirality-app-dev/**` unless the owner grants wider scope.
   *Checks per the work type:* typecheck + vitest + build/premerge gates
   (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`,
   `docs/BUILD_AND_RELEASE.md`); the D-APP-36 render bar for UI work; D-APP-38 corpus
   reconciliation when an authority doc is edited; for governance/control-plane-only
   tranches record explicitly that frontend gates were skipped because no runtime
   source changed; stop the local dev server before build/package/premerge commands
   unless the command owns the server lifecycle; plus repo-wide `self-check` exit 0 and
   full practitioner-harness pytest at closeout. CI green; owner merges.
   *D-APP-60 verification:* every scope named by the instrument's calibrated
   verification requirement must satisfy that requirement before commit; verdicts are
   recorded only after they exist, and nothing lands on `BLOCK`.
5. **Update deliverable state + receipt.** Closeout writes deliverable-local state:
   `_STATUS.md` (`Remaining` updated to reflect what landed — landed scope removed,
   newly named residuals added; lifecycle transitions only through their ruled gates,
   `**Checking Approval SHA**` discipline intact), `MEMORY.md`, `_run_records/**`;
   landed narrative goes to `plans/PLAN_COMPLETION_LOG.md`. Rationale artifacts for
   delegation exercises live in existing homes only: deliverable-scoped → that
   deliverable's `_run_records/**`; cross-cutting → the tranche's AgentRuns record;
   the artifact records rejections alongside exercises. Receipt citation convention:
   `Gate-Outcome` names the exercised judgment; `Pointers` names the rationale
   artifact. Append one versioned minimal receipt to `LOOP_RECEIPTS.md` per its local
   rules, then rerun
   `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .`; receipt
   validation is a mandatory pre-commit and closeout gate. Next iteration starts at 0.

## Standing constraints — hard fences (all iterations; always stop for a human ruling)

- **F-APP-1 (provider/network):** no provider or network expansion beyond the Anthropic
  path; no remote MCP, plugin, or broad tool-search enablement without a fresh ruling
  (F1 as amended by D-APP-44: owner-permitted, default-closed provider/residency
  configuration).
- **F-APP-2 (release/distribution):** no signing, notarization, publication, external
  distribution, or release-readiness / professional / certification claims.
- **F-APP-3 (domain-engine boundary):** domain-engine work happens only inside what the
  tier-0 bridge loop's ruled decisions grant (the `D-APP-4x` F-series rows); this loop
  never writes `_DomainEngines/**` or piping surfaces, and never advances integration
  level, live binding, or apply-class tool exposure on its own authority.
- **F-APP-4 (issuance):** no `CHECKING -> ISSUED` lifecycle issuance.
- **F-APP-5 (single-surface rule; owner-adopted 2026-07-10):** work items live in
  deliverable folders (`_STATUS.md` `## Remaining`); owner decisions live in
  `execution/_Coordination/_DECISIONS/_REGISTER.md`; no new standing plan, queue,
  register, or status surface is created without an owner ruling. `plans/` is a
  historical archive — never select work from it.
- **Fresh-ruling stops** (carried from the pre-consolidation coordination record):
  Pi-backed execution (unapproved after D-APP-01/02); concrete non-Anthropic provider
  implementation or routing; write/edit/bash/tool-execution exposure beyond the current
  approved item; changes to the project-truth model for sessions, transcripts, chats,
  runtime logs, or completion logs; professional-boundary or release-readiness posture.

## Where live work is re-derived (pointer index — never a status surface)

- **Work surface (discovery + selection):** `execution/PKG-*/1_Working/DEL-*/` —
  `_STATUS.md` (lifecycle + `## Remaining` open scope), `MEMORY.md`, four-document
  kits, `Dependencies.csv` / `_DEPENDENCIES.md`, `_run_records/**`.
- **Ruled records:** `execution/_Coordination/_COORDINATION.md` (ruled-record stub) ·
  decision register `execution/_Coordination/_DECISIONS/_REGISTER.md` (`D-APP-XX`
  rows; packets/ruling records beside it; open rows are the owner-gated surface) ·
  discovery pointers: `execution/_Coordination/_LATEST.md`.
- **Delegation instrument:** D-APP-60 (frozen shared block v1 + app-dev local
  bindings; supersedes D-APP-59's reach/method definition by reference) — delegation
  exercises cite D-APP-60 and follow its method binding, calibrated verifier scope,
  and rejection-recording convention.
- **Dependency evidence:** `execution/_Reconciliation/DepClosure/_LATEST.md` → the
  accepted closure snapshot; SCC work follows the shared
  `docs/CYCLE_DRIVEN_RESOLUTION.md` doctrine (repo root).
- **What must be built and why:**
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` · scope
  amendments: `execution/_ScopeChange/_LATEST.md` · product yardstick: `docs/PRD.md` ·
  strategy: `docs/PLAN.md` (non-governing) · authority documents: `docs/DIRECTIVE.md`,
  `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md` — edits trigger D-APP-38 corpus
  reconciliation (`execution/_Reconciliation/References/reconcile_authority_corpus.py`).
- **Validation gates:** `docs/VALIDATION_STRATEGY.md` · `docs/RELEASE_QUALITY_GATES.md`
  · `docs/BUILD_AND_RELEASE.md`.
- **Agent posture:** `AGENTS.md` (personas, dispatch contract, CHANGE closeout).
- **Frontend contract surfaces:** `frontend/packages/harness-contract/**` (pull
  contract pinned at `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_*.json`).
- **Cross-loop awareness:** `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope dedup only —
  this loop never writes the bridge loop's surfaces).
- **Historical archive (never selection surfaces):** `plans/**` (queue rows closed or
  rehomed 2026-07-10; see `plans/PLAN_COMPLETION_LOG.md`) ·
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` (pre-loop session entry — dated
  historical map, never authority).
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `LOOP_RECEIPTS.md` beside this file.
