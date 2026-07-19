# RATIONALE — D-APP-64 tranche design selections (2026-07-18)

**Run:** `D-APP-64_REASONED_SELECTION_OVERLAY_2026-07-18`

**Attribution and basis.** The design selections recorded below were made by
the Agent 0 orchestrator BEFORE the D-APP-64 overlay is active, under the
direction's own rationale requirement and existing per-instance
implementation latitude — NOT as D-APP-64 exercises (recording them as
overlay exercises would be anticipatory, the NM-3 class). The owner approved
the implementation plan containing them in-session (evidence: the session
plan approval; the authority remains the §3 direction transcribed in the
D-APP-64 packet). Each selection records its reasons and the materially
important rejected alternative(s).

## Selections

1. **Overlay-by-reference vs Shared-Block amendment.**
   Selected: an app-dev-local refining overlay that resolves the gate (b)
   referral consequence by reference, leaving Shared-Block v1 byte-identical.
   Reasons: the owner's direction excludes a block edit ("Keep Shared-Block
   v1 byte-identical"), and any change to block bytes is a paired owner act
   in every adopting project's register.
   Rejected alternative: amending Shared-Block v1 itself — excluded by the
   owner's direction and by the paired-act requirement.

2. **Successor filename `WORKPLAN_2026-07-18b_app_dev_loop.md`.**
   Selected: the `b` suffix, which under bytewise `LC_ALL=C` ordering sorts
   after `WORKPLAN_2026-07-18_…` (`b` = 0x62 > `_` = 0x5F) and before any
   later date, so the successor governs.
   Rejected alternatives: a `_2` suffix — sorts before the current file, so
   the successor would silently never govern; `2026-07-19` dating — misdates
   the owner act.

3. **Hybrid candidate isolation (Appendix W + run-dir candidate file).**
   Selected: the ruled bytes live both in the packet's Appendix W and,
   byte-identically, in this run directory's
   `WORKPLAN_CANDIDATE_2026-07-18b_app_dev_loop.md`; both homes are outside
   `loop/`.
   Rejected alternatives: appendix-only — newline-extraction ambiguity when
   materializing the file from an embedded span; run-dir-only — departs from
   packet self-containment.

4. **Committed-HEAD loader adoption.**
   Selected: `LOOP_INIT.md` §2 moves plan discovery to committed-`HEAD`-only
   selection, fail-closed.
   Reasons: keeping newest-worktree-file discovery leaves the documented
   staged-plan premature-activation hazard (D-APP-60 S2) open; the owner
   listed committed-HEAD loading among the mechanisms to adapt.
   Rejected alternative: retaining newest-worktree-file discovery.

5. **Activation at the atomic branch commit.**
   Selected: the refined discretion and the successor plan take effect at
   the single atomic landing commit on the working branch.
   Reasons: the piping precedent treats the branch commit as durable
   landing; HEAD-only discovery already fences `main` (sessions based on
   `main` select the successor only after the owner's merge); and
   merge-as-activation would blur attribution of the already-given
   direction.
   Rejected alternative: strictly-after-merge activation.

6. **HELPS_HUMANS-posture authoring child.**
   Selected: a HELPS_HUMANS-posture Agent 1 child executes the governed
   writes under a sealed brief.
   Reasons: no deliverable is touched; instruction/governance surfaces are
   HELPS_HUMANS's charter.
   Rejected alternative: a WORKING_ITEMS child — its charter is
   package-level deliverable production, which this tranche does not touch.

7. **Three separate verifiers vs one combined.**
   Selected: three independent verifiers (carry-forward; invariant matrix
   I1–I12; enumeration-derived governed-diff adversarial verifier per the
   NM-5 rule with the whole-diff claim).
   Reasons: the verifiers have disjoint refutation targets, and the piping
   precedent ran carry-forward and semantic verification separately.
   Rejected alternative: one combined verifier.

8. **GEN8 baseline: conscious re-pin vs relativizing the flagged records.**
   (Orchestrator selection, post-N5, on the closeout battery's findings.)
   Selected: consciously update the practitioner-harness live-baseline pins
   (severity anchor REVIEW to thirty; GEN8 file set plus the three D-APP-64
   records) and widen the landing scope by that one test file, recorded as
   Landing Manifest amendment v2.
   Reasons: the owner standing-direction verbatim span cites the piping
   precedent worktree by machine-absolute path, so its governed home (the
   packet) and the two sealed control-plane briefs that carry the span
   necessarily trip GEN8; verbatim owner text and sealed briefs are
   detect-never-rewrite, and the test file itself documents conscious pin
   updates as the governed path (its dated 25-to-24 note is a prior app-dev
   loop example). The app-dev loop already integration-owns repo-root
   validators (D-APP-61 precedent).
   Rejected alternatives: rewriting or paraphrasing the verbatim span or the
   sealed briefs to strip the path (violates verbatim transcription and
   sealed-record integrity); leaving the pins stale (lands a failing test
   battery on main, violating closeout).
