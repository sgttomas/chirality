# R16 observed UI follow-up

Type 2 author: r14_ui_cleanup, gpt-6-astra medium. Lead directly tested signed R16 and owns native verification. Work only in /Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335. Read applicable AGENTS and R16_FUNCTIONAL_FINDINGS.md.

Inspect two observations and make a minimal App-only correction where warranted:
1. Successful native tool interruption returns Idle and kills the sleep, and fresh read succeeds, but transcript retains only starting commentary with no Interrupted marker. Preserve truthful terminal status in live and reopened history without turning expected cancellation into failure or changing Runtime/account behavior.
2. Clicking a chat in navigator loads its main history correctly but replaces the open document viewer with an empty Agents / Session detail ('Select a recorded session to inspect its replay.'). Remove unintended obsolete sidebar routing while retaining explicit session-inspection entry points if they exist.

Write scope: relevant frontend UI/projection and focused tests plus this R16_UI_FINDINGS directory. No Runtime/supplier/auth changes, build/sign, live trial data, browser/native access, registration/process changes, Git commit or delegation. Preserve other working files. Do not modify RUN_LOG or R16_FUNCTIONAL_FINDINGS (lead-owned). Inspect source before editing; explain if either issue needs a broader contract. Run only meaningful focused regression tests. Return exact changed files, results, limitations and review-ready diff. Independent reviewer follows author; do not self-certify acceptance.


Owner follow-up after restart adds a third observed UI issue: unable to scroll to the composer in the other chat (first chat has long transcript and expanded native plan/revision history). Diagnose scroll containers/layout and minimally keep composer accessible with long content; no redesign. Main restart admission failure is a separate Runtime diagnosis lane.
