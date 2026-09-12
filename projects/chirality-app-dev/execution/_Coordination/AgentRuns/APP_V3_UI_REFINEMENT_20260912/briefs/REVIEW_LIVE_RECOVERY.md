# TASK: independent review of live-verification repairs

Fresh Type 2, `gpt-6-astra`, medium, no authorship and no delegation. Use
`.agents/skills/software-code-review/SKILL.md` after reading Root/App AGENTS
and the active TASK role. Fable is unavailable in this session; the owner's
previously authorized Astra Type 2 model is used with that fact disclosed.

Repository: `/Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality`.
Basis: `85f19f019589b798331c804c4b206e34849eeab5`. The parent supplies the
immutable candidate commit in dispatch. Read 100% of that Git diff, including
tests and records. No file writes, commits, source fixes, App launches, process
signals, or delegation. Return findings to the parent, who records them verbatim.

The owner explicitly requested the three verification gaps closed before a
replacement package: service stall/loss/reload, right-panel controls at two
widths, and preparation of the owner-only install-over check. Parent performed
the live checks. `LIVE_VERIFICATION_20260912.md` names observations and limits.
The earlier 85f19f019 package completed before that steering and is preserved;
it is historical evidence, not the final repair candidate.

Check the actual connection and shutdown path, not only mock assertions:

- Runtime stream opening and byte inactivity are bounded separately from model
  output. Runtime heartbeat bytes keep a healthy quiet turn attached. App proxy
  heartbeats cannot mask upstream loss. Real Runtime attachment clears the
  Reconnecting display, including an attachment with no buffered output.
- Subscription cancellation/reload only loses observation. No automatic second
  POST, implicit Stop, authentication weakening, or cancellation of owned work.
- Typed known pre-acceptance rejection restores draft/method/attachments;
  ambiguous transport loss preserves the sent message without enabling resend.
- Runtime interruption cause reaches persistence and live events even when the
  supplier constructs the terminal. Service shutdown is Failed, restart without
  a known ending is Outcome unknown, and operator Stop remains Stopped. Replay
  and plan execution settlement preserve the distinction. Generic exit frames
  must not erase a more specific terminal cause.
- Panel accessibility and resize origins agree with the constrained grid width,
  while per-tab preferences and expansion return remain intact.
- Tests exercise the failure conditions without weakening prior checks. Record
  any gap, flake or missing live evidence separately from actionable defects.

The default available tools are shell/source readers and bounded offline tests.
Reuse recorded full-suite results unless a finding warrants another check.
Never read identity/auth/token/binding/keychain/Codex-home or live session/event
files, including isolated spike userData. Do not inspect `intro-rehearsal/`.
Already-filtered evidence logs under
`/Users/ryan/.claude/chirality-build-ui-85f19f019-evidence` may be read. Filter
any newly produced logs to exclude lines containing `@`. No `security`, cleanup,
publication, protected-branch changes, or trial credential operations.

Return PASS only with no actionable finding, otherwise FAIL. Give file/line,
trigger, impact, evidence, and repair direction for each finding. Separately list
residual risks and verification limits, exact checks performed, and confirmation
of whole-diff coverage with any exclusions. Review is not owner approval or
product release approval.
