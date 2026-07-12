Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`. You need to be working in the dedicated
worktree for the chirality-piping D-41 concordance run. Before doing substantial
work:

1. Find the worktree for the chirality-piping D-41 concordance run. As of
   2026-07-12 it is `{REPO_ROOT}/.claude/worktrees/chirality-piping-d41-concordance-9811cb`
   on branch `claude/chirality-piping-d41-concordance-9811cb` (verify with
   `git worktree list`; if your harness cannot use it, create a fresh worktree
   from that branch — never work on the primary checkout). The read-only
   frozen evidence worktree is `{REPO_ROOT}/.claude-worktrees/piping-frozen-551f84ef6`.
2. Write only inside `projects/chirality-piping/` in this worktree. Never touch
   chirality-app-dev, the primary checkout, or another active worktree.

Set `WORKING_ROOT={REPO_ROOT}/projects/chirality-piping` and enter through:

`init/init-prompt.md` → `loop/LOOP_INIT.md` → newest `loop/WORKPLAN_*.md` →
`loop/LOOP_RECEIPTS.md`

Resume:
`projects/chirality-piping/execution/_Reconciliation/DeliverableConcordance/
DELIVERABLE_CONCORDANCE_2026-07-11_1305`

Enter through the project’s current loop instructions. Then read, in authority
order:

- latest 3 loop Receipts (23–25);
- the run folder’s `RUN_BASIS.md` end-to-end (including the W3-complete,
  addendum-9 incident, and pause entries);
- `R1_CONVENTIONS.md` Parts A–D;
- the W1–W3 calibration carry-forward in `PACKAGE_SUMMARIES/PKG-00..08.md`
  (each summary’s "Cross-ledger risks carried forward" section is binding
  calibration for W4);
- R0/R0b review files for calibration context;
- the pinned plan §§6–8 at
  `551f84ef6be656f1603ce0acfa5e3935aa9683c7`.

<last-work>
PAUSED at owner direction after W3 (Receipt 24). Waves W1–W3 are complete: 55
of 101 ledgers (W1 504 rows, W2 242, W3 399 post-correction), all fan-ins
clean, package summaries PKG-00..08 written. W3: 19/19 SOUND, 199 PASS / 49
QUALIFIED / 7 FAIL (all string-corrected by owning pilots), Part-C SECURITY
spot-check of DEL-08-05 convention-6 encoding PASS.

PR #198 (W3 wave boundary) was merged to main by owner direction as
`0129780f38d`; PR #199 (model-agnostic conversion; Receipt 25) was merged to
main by owner direction as `a58eab87c` — the revised LOOP_INIT §7 and
Receipt 25 are now on main. Note for wave-boundary PRs ahead: the Receipt-22 standing
self-merge grant is on record, but this session's permission layer blocked
the orchestrator's self-merge; expect to merge per-PR yourself or re-confirm
the grant in-session.

Owner acts pending before/at resume:
1. **Frozen-tree restoration (addendum-9 incident):** six untracked
   git-ignored artifact sets sit in the frozen evidence worktree
   (`.claude-worktrees/piping-frozen-551f84ef6`) — enumerated in RUN_BASIS.
   Restore via scoped `git clean -fdX` there (or recreate from the pinned
   SHA), or direct the orchestrator to treat them as allow-listed
   contamination.
2. **Two items listed in Receipt 25 for owner ruling (not repaired):**
   (a) RUN_BASIS's W3 pause entry names the rescinded Receipt-17 steer in
   its forward-looking resume lines — superseded by LOOP_INIT §7, left
   frozen as a run record; (b) a factual defect in the W3 package
   summaries: `PACKAGE_SUMMARIES/PKG-06/07/08.md` say "All pilots fable
   per the Receipt-17 steer," but W3 discovery pilots were opus (fan-in
   statements are correct). Do not treat that sentence as fact, and do not
   repair it without owner direction; the calibration content of those
   summaries is unaffected and remains binding.

Next work on resume: dispatch R2 W4 (PKG-09..12, 20 deliverables) in ≤4
concurrency batches. Model assignment is MODEL-AGNOSTIC per LOOP_INIT §7
(owner direction 2026-07-12; the prior Receipt-17 named-model steer is
rescinded going forward — see Receipt 25): the owner names the model(s) at
session or dispatch time; absent that, standard capability tier for
discovery pilots, highest available capability tier for the fan-in
verification and anything recorded as fact. NOTE the steer's risk shape
survives model-agnostically: PKG-12 (security/privacy, F-PIP-1
fence-adjacent) warrants the highest-capability tier for its discovery
pilots too — confirm with the owner at dispatch. W4 brief must carry:
R1_CONVENTIONS + the W1–W3 calibration items from PKG-00..08 summaries + the
addendum-9 mitigations now binding (porcelain checks with
`--ignored=matching` and the six known paths allow-listed until restored;
cargo re-execution on lockless crates only via copy-out; `pytest -p
no:cacheprovider`; no in-tree `py_compile`). Then the high-effort fan-in
(one verifier per package; scope: all self-flagged rows, all non-ALIGNED
rows, ≥2 ALIGNED rows per ledger), owning-pilot corrections, full-wave
revalidation, package summaries, RUN_BASIS entry, receipt (recording which
model performed each role), wave-boundary commit/push/PR. After W4: W5
(PKG-13..17, 26), then R3 synthesis and R6 backcheck per the durable method,
RUN_SUMMARY.md, and STOP.

Durable working artifacts from the last session (recreate if absent; the
scratchpad copies may be gone): the W3 pilot/fan-in/corrections briefs were
reconstructed from durable records alone — R1_CONVENTIONS, R0B_CONVENTIONS,
package summaries, and the W2/W3 verification reports as exemplars. The
structural validator is re-derivable: 20-column header byte-exact to any
committed ledger; enums from R0B conventions + addenda; ClaimID
`DEL-XX-XX-<REQ|ACC|EXC|DECL|REM>-NNN` contiguous per token and matching
ClaimType; RFC-4180 CRLF; addendum-6 DECL rows NOT_APPLICABLE; histograms in
notes must recount from the CSV.
</last-work>

Run-local conventions override generic defaults where they say so. Live Git and
durable run records override this prompt if they reveal a contradiction; STOP
and report any material contradiction rather than guessing.

After W5, complete R3 and R6 per the durable method, write `RUN_SUMMARY.md`, and
STOP. No lifecycle transitions or R4/R5 repair work without my explicit ruling.
All claim dispositions are agent judgments, never human rulings.
