# Sealed Launch Brief — N1 GOV-WRITES (D-APP-64 governed authoring)

- **Parent:** HELP_HUMAN (Agent 0), RunID `D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18`
- **Child role:** Agent 1, HELPS_HUMANS posture (instruction/governance-surface
  authoring), mechanical conformance to this brief; the design selections were
  made by the orchestrator and approved in-session by the owner at plan
  approval — the child exercises no delegated judgment.
- **Repo root:** the current working tree on branch
  `claude/dapp64-reasoned-selection-overlay` (base `34774f579…`).
- **Write scope (exactly five targets; nothing else):**
  1. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-64_PACKET_REASONED_SELECTION_OVERLAY_2026-07-18.md` (create)
  2. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` (append one row; every existing byte unchanged)
  3. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/WORKPLAN_CANDIDATE_2026-07-18b_app_dev_loop.md` (create)
  4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18/RATIONALE_D-APP-64.md` (create)
  5. `projects/chirality-app-dev/loop/LOOP_INIT.md` (one enumerated §2 edit)
- **Prohibitions:** do NOT create any file under `projects/chirality-app-dev/loop/`
  other than the LOOP_INIT edit (the successor workplan is materialized later by
  the orchestrator per the frozen choreography); do NOT touch Shared-Block v1
  bytes, any D-APP-59..63 record, any prior workplan, `LOOP_RECEIPTS.md`,
  `projects/chirality-piping/**`, `_DomainEngines/**`, `projects/pec/**`; do NOT
  commit, stage, push, or merge; do NOT record any verifier verdict, hash you
  have not computed, or commit id that does not yet exist.

## Owner direction (verbatim — the authority this tranche executes)

Canonical span SHA-256 (UTF-8 bytes strictly between the marker lines,
excluding the marker lines and the delimiter newlines adjacent to them):
`1bba870869e096ebd975ba503ce4afbc69de3b1b2360508bc6e8b680fb502e39`
(3,081 bytes). Copy the span into the packet §Owner Direction BYTE-EXACTLY
(read it from this file; do not retype), then independently recompute the
hash from the packet's own marker span and confirm equality before recording
it there.

<!-- BEGIN OWNER RULING VERBATIM -->
You have my standing approval to exercise bounded discretion in opening and pursuing development lanes within the project’s accepted purpose and scope, including when several viable or defensible options exist. Evaluate the alternatives through consistency and coherence across the project’s ontology, epistemology, praxeology, and axiology, using the full architecture, existing codebase, accepted requirements, live governance, and project history as your anchors. Select and advance the single outcome that, from your informed perspective, best serves the project as a whole.

Do not stop or escalate merely because another defensible option exists. The requirement is one reasoned decision to move forward, not proof that only one viable option was possible. Record a concise rationale and any materially important rejected alternative, without surfacing every ordinary design choice for owner review.

Treat this as owner-granted standing authority for bounded discretion. Attribute each selected outcome as the agent’s judgment under my standing approval, not as my case-specific personal selection.

Preserve the owner gate where a decision cannot responsibly be grounded in the accepted project—for example, irreducible personal preference; material changes to project purpose or accepted scope; new normative or acceptance criteria; professional, safety, legal, fiduciary, accountability, or residual-risk decisions; spending or external commitments; publication, release, issuance, or lifecycle advancement; protected-data exposure; destructive or irreversible action; or any existing app-dev hard fence or fresh-ruling stop.

Apply this prospectively to chirality-app-dev through its governed amendment process. Inspect the live D-APP-59 through D-APP-62 basis and mint the next lawful record; do not rewrite landed decisions, workplans, or verifier history. Treat the result as an app-dev-local refining overlay. Keep Shared-Block v1 byte-identical and do not modify chirality-piping.

For implementation precedent, inspect the final chirality-piping refinement in worktree `/Users/ryan/ai-env/projects/chirality-session-20260718`, branch `codex/session-20260718`, commit `8825065d5150bbeafc48fe5fd5bebbb679b9820e`. Adapt its attribution, evidence, nondelegable-boundary, candidate-isolation, committed-HEAD loading, invariant-review, and atomic-landing mechanisms to app-dev’s live governance and workplan conventions; do not copy identifiers or filenames mechanically.

Follow app-dev’s existing D-APP-60/D-APP-61 re-mint, verification, and sibling-review rules. Piping is a review baseline only and is not expected to adopt another change. A sibling review need not be repeated unless the reviewed policy semantics or frozen contract materially changes.

Bind the resulting governance record and active instruction surface durably to Git before using the refined discretion. This amendment grants no product implementation, lifecycle, issuance, release, publication, merge, push, protected-data, domain-engine, provider/network, or other external effect.
<!-- END OWNER RULING VERBATIM -->

## Task A — candidate successor workplan (write target 3)

Create `WORKPLAN_CANDIDATE_2026-07-18b_app_dev_loop.md` in this run directory
by COPYING `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18_app_dev_loop.md`
byte-for-byte and then applying EXACTLY the six edits below (exact
old-string → new-string replacements; every other byte carries forward
verbatim). Do not reflow, retab, or "improve" anything else.

**EDIT-1 (epistemic header).** Replace:

```
> **Epistemic status: agent-authored plan — not authority.** Written at owner adoption
> (Ryan Tufts, K-AUTH-1) on 2026-07-18 through the D-APP-61 ruling; supersedes
> `WORKPLAN_2026-07-17_app_dev_loop.md` in this directory.
```

with:

```
> **Epistemic status: agent-authored plan — not authority.** Re-minted at owner
> standing direction (Ryan Tufts, K-AUTH-1) on 2026-07-18 through the D-APP-64
> overlay; supersedes `WORKPLAN_2026-07-18_app_dev_loop.md` in this directory,
> carried forward verbatim except the clauses marked *(D-APP-64)*, with the
> carry-forward gated by an independent verifier.
```

**EDIT-2 (owner-intent bullet).** Immediately after the bullet ending
`instruments instead of restating their mechanics.` append this new bullet:

```
- **2026-07-18** (D-APP-64): the reasoned-selection refinement — under the owner's
  transcribed standing approval, plurality of surviving defensible outcomes is no
  longer itself a referral condition; inside the overlay's fast-reject boundary the
  agent selects and advances one reasoned outcome, recording a concise rationale
  and materially important rejected alternatives.
```

**EDIT-3 (Step 1 delegation-triage arm).** Replace:

```
Decide what clearly passes under the
   D-APP-60 instrument with a recorded rationale artifact; slate what fails or
   survives ambiguously, naming the failed gate in near-miss form. The asymmetry that
```

with:

```
Items that touch a fast-reject boundary
   are slated in near-miss form naming the touched boundary; among surviving
   defensible alternatives the agent selects and advances the one outcome it judges
   most consistent and coherent across the four lenses *(D-APP-64)*, recording a
   concise rationale and materially important rejected alternatives. The asymmetry that
```

(The following asymmetry sentence carries forward verbatim.)

**EDIT-4 (Step 2).** Replace:

```
design forks are resolved with recorded agent decision latitude — under the
   D-APP-60 instrument for disposition-class items (decide, record the rationale
   artifact, cite the exercise in the receipt), per-instance latitude otherwise.
```

with:

```
design forks are resolved with recorded agent decision latitude — under the
   D-APP-60 instrument as refined by the D-APP-64 overlay *(D-APP-64)* for
   disposition-class items (decide, record the rationale artifact, cite the
   exercise in the receipt), per-instance latitude otherwise.
```

**EDIT-5 (Step 3 gate).** Replace:

```
The STOP applies to owner-class items;
   disposition-class items proceed under the D-APP-60 method binding and verifier.
```

with:

```
The STOP applies to owner-class items;
   disposition-class items proceed under the D-APP-60 method binding and verifier,
   as refined by D-APP-64: ambiguity about whether a fast-reject boundary is
   touched is owner-class; plurality of surviving defensible outcomes is not
   itself owner-class *(D-APP-64)*.
```

**EDIT-6 (pointer index, Delegation instrument bullet).** Replace:

```
- **Delegation instrument:** D-APP-60 (frozen shared block v1 + app-dev local
  bindings; supersedes D-APP-59's reach/method definition by reference) — delegation
  exercises cite D-APP-60 and follow its method binding, calibrated verifier scope,
  and rejection-recording convention.
```

with:

```
- **Delegation instrument:** D-APP-60 (frozen shared block v1 + app-dev local
  bindings; supersedes D-APP-59's reach/method definition by reference), as refined
  by the D-APP-64 reasoned-selection overlay (fast-reject boundary, selection
  method, attribution schema) *(D-APP-64)* — delegation exercises cite D-APP-60
  and follow its method binding, calibrated verifier scope, and rejection-recording
  convention.
```

After writing, compute and note (for use in Task B §12): the candidate file's
byte count, its `git hash-object` blob id, and the SHA-256 of its span
(file bytes without the single trailing LF).

## Task B — the D-APP-64 packet (write target 1)

Create the packet with the section plan below. Where a clause is given in
quotes or a fenced block, use it verbatim; connective prose may be composed
but must claim nothing beyond this brief. The packet is self-contained (the
D-APP-63 packet is the ceremony model).

1. **Title + Status.** Title: `# D-APP-64 — Reasoned-Selection Standing-Approval
   Overlay (app-dev-local refinement of the D-APP-60 gate (b) referral
   consequence)`. Status block: `RULED — owner standing direction, 2026-07-18,
   transcribed in §3` ; prepared and executed by the Agent 0 orchestrator with a
   HELPS_HUMANS-posture authoring child under this run's sealed brief; effect
   held until the single atomic landing commit; owner merge remains the terminal
   integration act; this record grants no product implementation, lifecycle,
   issuance, release, publication, merge, push, protected-data, domain-engine,
   provider/network, or other external effect.
2. **Context.** The live basis inspected: D-APP-59 (standing decision-latitude
   delegation), D-APP-60 (frozen shared block v1 instrument; Shared-Block v1
   SHA-256 `76438ab0e00dc70e5f6db751a32d0ff07b681c7b7fb12eeda338157c5ebe7668`),
   D-APP-61 (loop entry + instruction separation; supersession-only workplan
   changes), D-APP-62, D-APP-63 (ceremony precedent). Implementation precedent:
   the chirality-piping reasoned-discretion refinement D-54/DEC-087 at worktree
   `/Users/ryan/ai-env/projects/chirality-session-20260718`, branch
   `codex/session-20260718`, commit `8825065d5150bbeafc48fe5fd5bebbb679b9820e`
   — its attribution, evidence, nondelegable-boundary, candidate-isolation,
   committed-HEAD-loading, invariant-review, and atomic-landing mechanisms are
   adapted to app-dev conventions, not copied.
3. **Owner Direction (verbatim).** The span from this brief between
   `<!-- BEGIN OWNER RULING VERBATIM -->` and `<!-- END OWNER RULING VERBATIM -->`,
   byte-exact, followed by: `**Canonical direction-text SHA-256:**
   1bba870869e096ebd975ba503ce4afbc69de3b1b2360508bc6e8b680fb502e39` with the
   parenthetical "(UTF-8 text between the verbatim markers, excluding the marker
   lines and delimiter newlines; computed by the orchestrator before recording
   and independently recomputed by the authoring instance from this packet's
   marker span after writing — both equal the recorded value)". Only record the
   sentence after your recomputation actually equals it.
4. **Prospective supersession and preserved history.** Verbatim clause: "This
   overlay refines only the locally bound referral consequence of Shared-Block
   v1 item 2 gate (b) as adopted through D-APP-60: for items that pass the
   fast-reject boundary below, the owner's standing approval transcribed in §3
   is the pre-given answer to the gate (b) referral — the agent selects and
   advances one reasoned outcome instead of returning the item to the owner.
   The block's bytes are unchanged and its text still reads 'returns to the
   owner'; that referral is resolved through this app-dev-local binding, not by
   editing the block. D-APP-59, D-APP-60, and every ruled register row remain
   byte-stable immutable history, superseded on this one point by reference.
   Any change to Shared-Block v1 bytes remains a paired owner act in every
   adopting project's register; a solo change is declared divergence."
5. **Reasoned-selection contract.**
   - **5.1 Fast-reject boundary (nondelegable; screened first, before any lens
     analysis).** Preamble: "A matter remains owner-gated when it cannot
     responsibly be grounded in the accepted project, including when it depends
     on or performs:" then exactly this numbered list:

```
1. irreducible personal preference or identity;
2. material change to project purpose or accepted scope, including any scope
   inclusion/exclusion/boundary amendment or its acceptance (the NM-1 class);
3. new normative content or new or changed acceptance criteria;
4. professional, safety, legal, fiduciary, contractual, residual-risk, or
   accountability content — including ResponsibleParty or evidence-owner
   naming (the NM-2 class) and any release-readiness, professional, or
   certification posture;
5. spending, procurement, licensing, third-party consent, or any other
   external commitment;
6. publication, release, distribution, issuance (`CHECKING -> ISSUED`),
   lifecycle or stage advancement, `**Checking Approval SHA**` transitions,
   and reliance or acceptance acts;
7. protected, private, or proprietary-data exposure;
8. destructive, irreversible, or history-rewriting action, and any merge or
   push of an accepted baseline (merge authority is never granted; never
   self-merge);
9. any hard fence (F-APP-1..F-APP-5), any standing fresh-ruling stop, the
   domain-engine and piping write boundaries, adoption/ruling/direction
   themselves (K-AUTH-1; D-GOV-04), and every other recorded D-APP-59 /
   D-APP-60 limit;
10. unavailable or stale evidence, an unresolved authority conflict, or a
    claim stronger than its warrant.
```

     Closing sentences, verbatim: "Ambiguity about whether a fast-reject
     boundary is touched remains a hit. Several viable or defensible
     alternatives surviving is not itself a hit. Referral remains correct when
     no responsible project-grounded judgment can be made."
   - **5.2 Selection method (all duties, every exercise).** Ground every
     alternative in the live tree; use existing accepted authority only (apply
     authority, create none); evaluate through all four lenses — ontology,
     epistemology, praxeology, axiology — omitting none; identify the material
     alternatives before selecting; select and advance the single outcome
     judged most consistent and coherent with the accepted project as a whole;
     keep the selected outcome bounded and reversible short of every
     nondelegable gate; record a concise rationale naming the selected outcome
     and the materially important rejected alternatives; obtain the D-APP-60
     calibrated verification (including the independent adversarial verifier
     wherever the instrument requires one) before effect.
   - **5.3 Attribution schema.** Every exercise records, in its rationale
     artifact:

```
OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: <the bounded, project-grounded outcome>
JudgedBy: <agent role and run/instance id>
OwnerCaseSelection: NONE
RejectedAlternatives: <materially important alternatives + concise reasons>
RationaleArtifact: <path>
IndependentVerifier: <COMMIT-SAFE return path | BLOCK return path | NOT_REQUIRED per D-APP-60 calibration>
EffectStatus: <HELD | EFFECTIVE>
PreservedGates: <the fast-reject boundary classes and fences the exercise stayed inside>
```

     Plus the sentence: "A selection under this overlay is the agent's judgment
     under the owner's standing approval, never an owner case-specific
     selection; recording it otherwise violates the truthful-attribution limit
     (K-AUTH-1; D-GOV-04)."
6. **Relationship to D-APP-59 / D-APP-60 and congruence note.** Shared-Block v1
   recomputes to `76438ab0e00dc70e5f6db751a32d0ff07b681c7b7fb12eeda338157c5ebe7668`
   (state that this was verified in this tranche only if you actually recompute
   it from the D-APP-60 packet's marker span — do so). The sibling overlay of
   the same policy semantics is piping D-54/DEC-087; declared divergences in
   block bytes: none. The near-miss corpus NM-1..NM-5 remains in force,
   supersede-never-edit.
7. **Sibling-review disposition (S5).** The D-APP-60 S5 amendment-time
   owner-mediated cross-project review is facially triggered by this overlay;
   it is NOT repeated here by the owner's direction in §3 ("A sibling review
   need not be repeated unless the reviewed policy semantics or frozen contract
   materially changes"), on the recorded basis that the identical policy
   semantics were cross-project reviewed at the piping D-54 S5 event, that
   Shared-Block v1 is byte-identical, and that the owner's D-54 §1A curtailment
   is precedent. This is an owner-directed disposition inside the hashed
   verbatim direction, not an agent waiver. Re-trigger condition: any material
   change to this overlay's policy semantics or to Shared-Block v1 bytes
   re-invokes S5.
8. **Workplan re-mint.** Successor plan
   `loop/WORKPLAN_2026-07-18b_app_dev_loop.md` supersedes
   `WORKPLAN_2026-07-18_app_dev_loop.md` by filename-dated supersession
   (D-APP-60 S2; D-APP-61 M2-A; the prior file is never edited). Same-day
   collision resolved by the `b` suffix: under bytewise `LC_ALL=C` ordering
   `WORKPLAN_2026-07-18b_…` sorts after `WORKPLAN_2026-07-18_…` (`b` = 0x62 >
   `_` = 0x5F) and before any later date. Delta set: exactly the six edits
   enumerated in this run's `LAUNCH_BRIEF_GOVERNED_WRITES.md` Task A
   (cite it), each marked `*(D-APP-64)*` in the plan text where it lands;
   everything else carries forward byte-verbatim, gated by the independent
   carry-forward verifier. Candidate isolation: the ruled bytes live in
   Appendix W below and, byte-identically, at this run's
   `WORKPLAN_CANDIDATE_2026-07-18b_app_dev_loop.md`; both homes are outside
   `loop/`, so no plan-discovery path can select them before landing.
   Activation: the refined discretion and the successor plan take effect at
   the single atomic landing commit on the working branch (durable Git
   binding); under the committed-HEAD loader, sessions based on `main` select
   the successor plan only after the owner's merge, which remains the terminal
   integration act.
9. **LOOP_INIT §2 amendment.** Summarize: plan discovery moves from
   newest-worktree-file to committed-`HEAD`-only selection (deterministic
   bytewise ordering, single mode-100644 blob, `git show HEAD:<path>`,
   fail-closed), permanently curing the staged-plan premature-activation
   hazard documented in D-APP-60 S2; exact wording lands in `LOOP_INIT.md`
   in the same atomic commit.
10. **Verification.** Name the three independent verifiers (carry-forward;
    invariant matrix I1–I12; enumeration-derived governed-diff adversarial
    verifier per the NM-5 rule with the whole-diff claim) and the
    deterministic closeout battery. Verdict lines MUST be written
    staged-empty: `Verdict: (recorded after the return exists)` — the
    orchestrator fills them only after each return file exists.
11. **On-direction mechanics.** Numbered list of the landing steps (candidate
    → V1 → landing artifacts → materialization with byte-equality proof → V2
    → Receipt-70 → V3 → single atomic commit of the declared six-item scope →
    closeout battery → PR → owner merge). Close with: "This record grants no
    implementation approval beyond its text."
12. **Appendix W — successor plan candidate (ruled bytes).** State the span
    convention: "the candidate is the text strictly between the markers below,
    joined by LF with no leading or trailing newline; the minted file is that
    span plus one trailing LF." Record the span SHA-256 and byte count you
    computed in Task A. Then:
    `<!-- BEGIN APPENDIX W D-APP-64 -->`, the candidate bytes (file content
    without its single trailing LF), `<!-- END APPENDIX W D-APP-64 -->`.

## Task C — register row (write target 2)

Append exactly one row to the register table (after the D-APP-63 row; all
existing bytes unchanged), single line, six cells:

```
| D-APP-64 | Adopt the reasoned-selection standing-approval overlay: under the owner's transcribed standing direction, plurality of surviving defensible outcomes ceases to be a referral condition for items passing the overlay's fast-reject boundary; the agent selects and advances one reasoned outcome under the D-APP-64 contract (fast-reject boundary, selection method, attribution schema), with the governing workplan re-minted and `LOOP_INIT.md` moved to committed-HEAD plan discovery | The D-APP-60 gate (b) referral consequence (refined by reference, app-dev-local; Shared-Block v1 bytes untouched); the governing workplan (re-minted `WORKPLAN_2026-07-18b_app_dev_loop.md`); `LOOP_INIT.md` §2 plan discovery; future delegation-exercise recording | RULED (owner standing direction) | `execution/_Coordination/_DECISIONS/D-APP-64_PACKET_REASONED_SELECTION_OVERLAY_2026-07-18.md` | owner standing direction transcribed in packet §3 (2026-07-18; canonical SHA-256 `1bba870869e096ebd975ba503ce4afbc69de3b1b2360508bc6e8b680fb502e39`); app-dev-local refining overlay; Shared-Block v1 byte-identical (`76438ab0…7668`); S5 sibling review not repeated by owner direction (piping D-54/DEC-087 reviewed the identical semantics); activation at the atomic landing commit under the amended committed-HEAD loader; owner merge remains the terminal integration act |
```

## Task D — rationale artifact (write target 4)

Create `RATIONALE_D-APP-64.md` in this run directory recording the tranche's
design selections, each with reasons and the materially important rejected
alternative(s). These selections were made by the orchestrator BEFORE the
overlay is active, under the direction's own rationale requirement and
existing per-instance implementation latitude (NOT as D-APP-64 exercises —
recording them as overlay exercises would be anticipatory, the NM-3 class),
and the owner approved the implementation plan containing them in-session
(evidence: the session plan approval; the authority remains the §3
direction). Record at least:
1. Overlay-by-reference vs Shared-Block amendment (block edit excluded by the
   owner's direction; paired-act requirement).
2. Successor filename `WORKPLAN_2026-07-18b_app_dev_loop.md` vs `_2` suffix
   (sorts before the current file — silently never governs) vs `2026-07-19`
   dating (misdates the owner act).
3. Hybrid candidate isolation (Appendix W + run-dir candidate file) vs
   appendix-only (newline-extraction ambiguity) vs run-dir-only (departs from
   packet self-containment).
4. Committed-HEAD loader adoption vs keeping newest-worktree-file discovery
   (leaves the documented premature-activation hazard open; owner listed
   committed-HEAD loading among mechanisms to adapt).
5. Activation at the atomic branch commit vs strictly-after-merge (piping
   precedent treats the branch commit as durable landing; HEAD-only discovery
   already fences `main`; merge-as-activation would blur attribution of the
   already-given direction).
6. HELPS_HUMANS-posture authoring child vs WORKING_ITEMS (no deliverable
   touched; instruction/governance surfaces are HELPS_HUMANS's charter).
7. Three separate verifiers vs one combined (disjoint refutation targets;
   piping precedent ran carry-forward and semantic verification separately).

## Sequencing and return contract

Order: Task A → Task B → Task C → Task D → Task E (LOOP_INIT edit, below) —
then return.

**Task E (write target 5).** In `projects/chirality-app-dev/loop/LOOP_INIT.md`
§2, replace exactly:

```
The standing plan is the protocol — read it and do what it says: the newest
`WORKPLAN_*.md` in this file's directory. Its **Step 0 (Discover)** runs
before anything else.
```

with:

```
The standing plan is the protocol — read it and do what it says. It is
selected only from committed `HEAD`, never from the working tree: from
`REPO_ROOT`, enumerate the `HEAD` tree entries under
`projects/chirality-app-dev/loop/`, keep basenames matching
`^WORKPLAN_.*\.md$`, sort them bytewise (`LC_ALL=C`), and select the last.
Require the selected path to resolve to exactly one `HEAD` tree entry of
mode `100644`, type `blob`, and read the plan bytes only with
`git show HEAD:<path>` — never the worktree copy. An untracked, staged-only,
or worktree-only filename is never selectable. If enumeration, validation,
or committed-byte reading fails, stop before Step 0 and report the loader
failure; never silently select an older plan. (Committed-`HEAD` selection
adopted through D-APP-64.) Its **Step 0 (Discover)** runs before anything
else.
```

Every other byte of LOOP_INIT.md unchanged.

**Return (final message, structured):** paths written; candidate byte count,
blob id, span SHA-256; the direction-hash recomputation result from the
packet's marker span (must equal `1bba8708…2e39`); the Shared-Block v1
recomputation result from the D-APP-60 packet span (must equal
`76438ab0…7668`); confirmation that no path outside the five write targets
was touched; any deviation or anomaly (report, do not improvise).
