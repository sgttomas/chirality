# D-APP-112 — `loop/LOOP_INIT.md` consolidation (item A) and run-based PR boundary (item B)

Status: `PROPOSAL — AWAITING_RULING`

DecisionID: `D-APP-112`

Date: `2026-09-05`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Candidate: branch `claude/loop-init-consolidation-d-app-112` from `origin/main`
`7cb41194f55d7747f6c388e6afbedf88cfd1d9f4`; the candidate bytes are applied
to `loop/LOOP_INIT.md` on the branch (SHA-256
`3a6c0713d3d501f25e23760e1f7cb4335e5d5db902eae7f5ad97b4221ee55979`, 264
lines, 15,758 bytes; the ruled D-APP-105 text is 386 lines, 23,838 bytes).
Two separately rulable items: **A**, the consolidation and ordering; **B**,
the run-based PR boundary (below). The owner rules by reply; on acceptance
the register row flips to `RULED` with a one-line ruling record on the same
PR before merge.

## Owner direction (verbatim, chat, 2026-09-05)

<!-- BEGIN OWNER DIRECTION VERBATIM -->
I read the LOOP_INIT.md for this project and it is way too dense.  Section 9 and 10 are almost sufficient by themselves.  Don't explain if the agent will just discover.  Point to where it should go discover.  Only for repeated failures or issues that haven't yet been resolved through better testing, or different instructions, should anything else be said to the agent about what it is supposed to do and how it's supposed to go about it.  First, what's your read of this, and second how would you try to resolve this matter and satisfy my concerns? (one way to satisfy my concerns is to justify what's there, the other is to fix it or remove it).
<!-- END OWNER DIRECTION VERBATIM -->

<!-- BEGIN OWNER DIRECTION VERBATIM -->
Proceed accordingly.  Remove as much as you can justify.
<!-- END OWNER DIRECTION VERBATIM -->

On the first cut (386 to 242 lines, same section order):

<!-- BEGIN OWNER DIRECTION VERBATIM -->
It's much much much better.  Are you as timely and clear as you need to be about the location of the deliverables?  I'm not saying you aren't.  Just assess and make changes if you think it's warranted.  The agent ought to be reading the entire thing, but ordering and consistency, and repetition can matter.  Consider the overall ordering of the LOOP_INIT.md and if you want to change it to make it clearer and more cohesive.
<!-- END OWNER DIRECTION VERBATIM -->

These directions authorize preparing this packet and candidate; none is read
as a ruling on the candidate bytes.

## Test applied

Each clause of the D-APP-105 text was assigned exactly one disposition:

| Code | Disposition | Rule |
|---|---|---|
| POINT | replaced by a pointer | the content is discoverable at a named source the agent reads anyway |
| MECH | deleted; the check stays in Step 0 or §8 | the failure it described is now caught by a deterministic check |
| KEEP | kept, compressed | a rule the agent cannot discover, born of a recorded failure or ruling, with no check yet |
| OWNER | kept verbatim | owner text; changing it is an owner act |
| DROP | deleted | explanation, motivation, or provenance; no behavioural content |

## Triage table (D-APP-105 text, by clause)

| # | Clause (D-APP-105 §) | Provenance | Failure it addressed | Check that now catches it | Disposition |
|---|---|---|---|---|---|
| 1 | Header: file carries protocol, posture, fences, evidence, checks, pointers; no status; not authority | D-APP-105 | none | — | KEEP (three sentences) |
| 2 | §1 Bootstrap: `REPO_ROOT`, surfaces relative to this dir, receipts hold handoff context | Receipt 0 | none | — | KEEP (two bullets) |
| 3 | §2 overlay rule (narrows, never holds work, never relaxes a fence) | D-APP-105 | workplans had accumulated work and protocol | `validate_instruction_entrypoints.py` structural-duplication check on the newest plan | KEEP, one paragraph (the void-clause rule is not mechanized) |
| 4 | §2 committed-HEAD loader, spelled out in prose | D-APP-64 §9 | an uncommitted plan was selected | the Step 0 `git ls-tree … git show` line | MECH (prose deleted; one sentence names the rule the line implements) |
| 5 | §2 loader-failure stop, immutability of ruled plans | D-APP-64, D-APP-106 | silent fallback to an older plan | validator `test_accepts_project_without_workplan`; loader line fails loudly | MECH for the failure stop; KEEP one sentence on immutability |
| 6 | Step 0 command block | D-APP-61/64/105 | — | it is the check surface | KEEP verbatim |
| 7 | Step 0 "what each line establishes": git/branch awareness, concurrent loops, disjoint scopes | AGENTS.md "there may be other agents" | agents staged unrelated dirty files | project `AGENTS.md` carries the rule | POINT (§9 "Agent posture") |
| 8 | Step 0: receipt validator blocks the cursor | D-APP-57 | ledger drift | `validate_app_dev_loop_receipts.py` | KEEP one line (the consequence, not the mechanism) |
| 9 | Step 0: committed plan bytes; decision register; Root notices; corpus check; work surface; self-check bullets | D-APP-38, D-APP-105 | none beyond what the commands print | the commands print it | DROP (the two non-printed consequences kept as one bullet: rulings and notices unlock work; drift is repair-first) |
| 10 | Step 0: verify before relying | Receipt 5; K-AUTH-1 | agents relied on stale maps | none mechanical | KEEP (compressed) |
| 11 | Step 0: A1 re-stage declaration | A1 2026-08-23 | none recorded; owner rule | none mechanical | KEEP one bullet with the pointer |
| 12 | Step 0: pin preflight | D-APP-64 | none recorded | none mechanical | KEEP one line |
| 13 | Step 1 selectability rule and blockedness re-derivation | A12; R17 | items selected past unruled gates; hand-maintained summaries | none mechanical (DepClosure pointer currency is checked by `self-check` GEN-7) | KEEP (compressed; points to §9 for the snapshot) |
| 14 | Step 1 executability definition (scope, lifecycle, dependencies, gates, check surface, write locus) | A12 | — | the harness `status` command reports lifecycle; the rest is in the item text | DROP |
| 15 | Step 1 parked-gate enumeration (Root acceptance, Root act, DEL-02-06 binding, owner act, release act) | A12; WORKPLAN 2026-09-03 | — | the items carry their own `(gated: …)` markers | DROP (subsumed by "observable on `main`") |
| 16 | Step 1 precedence (a)–(e) | D-APP-38, Receipt 5, D-APP-105 | busywork before repair | none mechanical | KEEP one sentence |
| 17 | Step 1 K-ENGINE-6 lens | CONTRACT K-ENGINE-6 | off-strategy harness parity work | none mechanical | POINT (one sentence names the contract row) |
| 18 | Step 1 "never manufacture work / never revive ruled-shut items" | Receipt 5; F-APP-5 | agents revived closed items | none mechanical | KEEP one sentence |
| 19 | Step 1 delegation triage prose (fast-reject ordering, four-lens test, over-slating asymmetry) | D-APP-60, D-APP-64 §5 | — | the instrument text governs | POINT (D-APP-64 §5; D-APP-60) |
| 20 | Step 2 packet criteria; decision latitude; CANDIDATE briefs; decision slate | D-APP-60/64 | — | — | KEEP, compressed to one paragraph; latitude mechanics POINT to D-APP-64 §5.3 |
| 21 | Step 3 STOP rule; owner acts; ambiguity is owner-class; verbatim recording; chat-only to receipt; record no-ops | K-AUTH-1; D-GOV-04; D-APP-57; D-APP-64 | agents performed owner acts; chat directions lost | receipt validator enforces the Owner-Direction record | KEEP, compressed; "directions recoverable from Git need no transcription" and "terminus slates pre-triaged in near-miss form" DROP |
| 22 | Step 4 branch-first, never self-merge, one branch/PR/receipt, write scope, adopted brief is live authority, CI green | Receipt 0; A12 | self-merge; PR stacking | none mechanical | KEEP (compressed) |
| 23 | Step 4 independent-review path, APP-HOLD-1 preflight, D-APP-60 verification requirement | AGENTS.md | — | AGENTS.md carries both, with the exact command | POINT |
| 24 | Step 5 closeout writes; rationale-artifact homes; receipt citation convention; validator as pre-commit gate | D-APP-57/60/64 | closeout skipped state writes | receipt validator (partly) | KEEP the write list and the validator gate; rationale-home and citation-convention prose POINT (D-APP-64 §5.3) |
| 25 | §4 first return | D-APP-61 M1-A | agents opened with a recap of the plan | none mechanical | KEEP (compressed) |
| 26 | §5 pacing paragraph (R17-E as carried by A12) | A12 | evidence-only iterations | none mechanical | KEEP one bullet |
| 27 | §5 ambition inside the fence | WORKPLAN 2026-09-03 | under-selection | none mechanical | merged into the pacing bullet |
| 28 | §5 terminus; truthful attribution; gate state register-derived | Receipt 5; D-APP-64; D-APP-105 | busywork; a `RULED` row written for an act that did not occur | none mechanical for attribution | KEEP two bullets; "register-derived" DROP (Step 0 grep and Step 1 already say so) |
| 29 | §6 fences F-APP-1 to F-APP-5 and fresh-ruling stops | owner-adopted | — | — | OWNER (verbatim) |
| 30 | §6 "Observation beside the fences" | agent-authored (A12 plan) | — | — | DROP; the closing sentence "fence wording is an owner act" KEEP |
| 31 | §7 evidence contract | A12; Root R17 N3 | prose summaries offered as acceptance evidence | none mechanical | KEEP, compressed to one paragraph |
| 32 | §8 checks table | D-APP-36/38; AGENTS.md | — | the rows are the check index | KEEP; the host-surface row shortened to its pointer |
| 33 | §9 pointer index | D-APP-105 | — | pointer currency in `self-check` | KEEP; SCA-APP-008 post-application audit entry DROP (superseded by the accepted DepClosure snapshot under D-APP-111); AGENTS.md entry gains the concurrent-loop rule so item 7 has a home |
| 34 | §10 per-run steer; "LOOP_INIT §7 defaults" mapping | D-APP-61 M4-A | — | — | KEEP in substance; the mapping sentence generalized to cover the D-APP-105 numbering as well |
| 35 | Appendix provenance | D-APP-105 | — | the register holds provenance; this table records it for the rewrite | DROP |

## Item B — run-based PR boundary (amends the A12 "one branch, one PR, one receipt" rule)

Owner direction (verbatim, chat, 2026-09-05), after the dry run showed the
operator deciding on its own whether independent nodes ride one PR:

<!-- BEGIN OWNER DIRECTION VERBATIM -->
I read its response too.  I see that it made a decision about PRs and Nodes (and bundling or stacking work).  I do indeed want to maximize concurrency and persistence in work, before having to get the human to approve PR merger.  There's many pitfalls in this, but I've tried to put the scaffolding in place to make this possible.  How did you approach this in the LOOP_INIT?
<!-- END OWNER DIRECTION VERBATIM -->

<!-- BEGIN OWNER DIRECTION VERBATIM -->
Conceptually (and I haven't mentioned where this breaks and why) I want to give the agent freedom to continue acting and working as far as the scaffolding and instructions permit, before stopping and opening a PR.  Considering that all work will be orchestrated by an Agent 0 instance, what do you recommend doing in this matter?
<!-- END OWNER DIRECTION VERBATIM -->

HELP_HUMAN recommended making the PR boundary the terminus rather than the
iteration, with a gate-class split so dependency chains proceed within a
run. The owner replied:

<!-- BEGIN OWNER DIRECTION VERBATIM -->
I agree.  Revise accordingly.  Include in PR #717.
<!-- END OWNER DIRECTION VERBATIM -->

### Rule as written in the candidate

- **Step 4.** One branch per run, cut from `origin/main`; Steps 0 to 5
  iterate on it with one commit and one receipt per iteration and a push
  after every closeout. Independent nodes run concurrently within an
  iteration under one work graph with disjoint write loci; dependent nodes
  run in later iterations of the same run. One PR opens at terminus (§7) or
  when the next lawful step needs a merged act. Never self-merge; the owner
  merges or rejects by commit; a rejected commit's item returns to Step 0 on
  the next run.
- **Step 1.** Owner acts, rulings, and routed Root notices are observable
  only on `origin/main`. A predecessor item is observable once its commit,
  checks, and run record are on the run's branch.
- **Step 5.** The run's first receipt names the base commit; each later
  receipt chains to the previous; commit, push, and start the next iteration
  at Step 0 on the same branch.
- **§7.** Continue iterating on the run's branch until every lawful path of
  advancement is exhausted except human decision; only then open the PR
  (restores the D-APP-105 sentence item A had cut).

### Why this shape

Agent 0 is the sole author of receipts, register rows, and `_STATUS.md`
state on the run's branch, so the three append-only surfaces that would
conflict across parallel branches stay linear. Concurrency lives inside the
iteration, where the work graph, sealed briefs, disjoint write loci, and
APP-HOLD-1 preflight already govern it. Persistence lives across iterations
on one branch, which the gate-class split makes possible for dependency
chains. One commit and one receipt per iteration keep the PR reviewable and
rejectable by commit. The independent-review path for product source runs
per iteration before its commit, so review stays fresh and small however
long the run.

### What it does not change

Owner merge remains the only path to `main`; no self-merge; fences, checks,
and the APP-HOLD-1 preflight are unchanged; owner acts still count only on
`origin/main`. The receipt validator needs no change for a linear chain on
one branch; a run whose PR is rejected starts its next run from
`origin/main` with the rejected items back at Step 0.

## Ordering (second cut)

The first cut kept the D-APP-105 order. Read top-down, that order named the
deliverable path only inside a Step 0 command and plainly only in the last
content section, and placed the fences after the protocol that tells the
agent to stop at them. The second cut orders the file map, then limits, then
motion: §1 bootstrap, §2 pointer index (was §9), §3 fences (was §6), §4
workplan overlay (was §2), §5 protocol (was §3), §6 first return (was §4),
§7 posture (was §5), §8 checks (unchanged), §9 evidence contract (was §7),
§10 steer (unchanged). The header names the deliverable path and the
`## Remaining` surface in its second sentence; Step 1 names them again at
the point of selection and points to §2. Cross-references inside the file
are updated; one duplicated "drift is repair-first" line was removed from
Step 0 (the §8 table carries it).

Section numbers change. §10 now states that historical receipts cite the
numbering of the revision current when they were written and that the
D-APP-105 text remains in git history, so every earlier citation still
resolves through that sentence.

## Dry run (third cut)

On the owner's direction, a fresh Claude Code subagent was given only the
second-cut text (no `AGENTS.md`, no persona, no prior context), a read-only
steer, and told to run Step 0, give the first return, select under Step 1,
stop before Step 2, and list every point of friction. It produced a correct
orientation return (newest receipt, the one open register row, the plan's
focus with its hash pin recomputed, the accepted acyclic DepClosure
snapshot, three `SELECTABLE` items, every parked lane with its unparking
act) and selected the same three-node tranche HELP_HUMAN had identified,
with the APP-HOLD-1 preflight run and the live tree checked. It listed
fourteen frictions; dispositions:

| # | Friction | Disposition |
|---|---|---|
| 1 | `harness.py status --project projects/chirality-app-dev` exits 2 (the tool takes `chirality-app-dev`); broken since the D-APP-105 text of 2026-09-04 | FIXED in Step 0 |
| 2 | The file at `HEAD` is itself an unruled candidate | dry-run artifact; no change |
| 3 | APP-HOLD-1 `--entry-path` vocabulary undocumented | `AGENTS.md` residual, outside this file |
| 4 | Blockedness re-derivation had no method | FIXED: Step 1 names the item's `Depends` line, `ACTIVE` rows gating per `SatisfactionStatus`, and the snapshot |
| 5 | One PR per iteration versus concurrent independent nodes | FIXED, then superseded by item B: one branch per run, one PR at terminus |
| 6 | Whether "observable on `main`" permits a fetch | FIXED: Step 1 says `origin/main` after `git fetch` |
| 7 | D-APP-60 / D-APP-64 cited by ID with no path | FIXED: §2 names both packet files |
| 8 | Legacy prose markers in some `Remaining` items ("packet authorized; awaiting ruling") | item-text residual, outside this file |
| 9 | An OPEN deliverable without `## Remaining` is silently dropped by the grep | FIXED: Step 0 rule restored (absent section means no recorded open scope) |
| 10 | `self-check` exit 0 with findings outside the project | no change; exit status is the stated bar |
| 11 | `PKG-00/…/DAG_CLOSURE_CONTROL.md` still names the July closure snapshot | live stale-map delta, a D-APP-111 residual reported to the owner; not this file |
| 12 | How to tell which Root notices are newer than the last receipt | no change; filename dates against receipt dates is the method and the agent found it |
| 13 | Hash pins inside `Remaining` items | FIXED: the pin rule now covers items as well as the plan |
| 14 | `tail -60` of the ledger omits the ledger's own rules | FIXED: Step 0 also prints the ledger header |

Net effect: +12 lines. Every addition answers a question the fresh operator
actually asked; none restates something it discovered.

## What the candidate does not do

It changes no fence wording, no check in §8, and no pointer target other
than the superseded SCA-APP-008 audit entry. One Step 0 command is repaired
(see "Dry run"). It moves sections (see "Ordering") but changes no rule by
the move. It retains
every D-APP-64 element that D-APP-105 listed as retained (§3 standing
approval by pointer, §5 contract by pointer, the committed-HEAD reading in
§2 and Step 0, the M4-A mapping sentence). It adds no rule.

## Residuals the owner may rule later (not proposed here)

- Items 10, 13, 16, 18, 22, 26, 31 stay as prose because no check catches
  their failure. Each is a candidate for a validator (for example a receipt
  check that `Pointers` never names `plans/**` as a selection source), after
  which its sentence can go.
- §7 could move to a `docs/` home and be pointed to; that is a docs-corpus
  act under D-APP-38 and is not bundled here.

## Verification on the candidate

`validate_instruction_entrypoints.py` PASS; repo-wide `self-check` exit 0;
receipt validator VALID after Receipt 241; `git diff --check` clean;
candidate whitespace PASS on the committed range. No product source changed;
frontend gates skipped.

## On-ruling mechanics

Accept: the owner replies; the register row flips to `RULED`, a one-line
ruling record is added beside this packet, and the owner merges. Amend: the
owner names the clause; the candidate is re-cut on the same branch. Decline:
the branch is closed and the D-APP-105 text stands.

## Attribution

Prepared by Claude Fable 5.1 (Anthropic, `claude-fable-5-1`) in an untyped
Claude Code session acting as HELP_HUMAN (Agent 0); the triage dispositions
are the agent's; the owner rules. Role not mechanically enforced.
