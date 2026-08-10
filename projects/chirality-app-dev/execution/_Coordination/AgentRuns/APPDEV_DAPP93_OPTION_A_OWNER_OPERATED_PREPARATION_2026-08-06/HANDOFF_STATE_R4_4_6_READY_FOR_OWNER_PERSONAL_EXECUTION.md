# Handoff state R4.4.6 — ready for owner-personal execution

Handoff: `READY_FOR_OWNER_PERSONAL_EXECUTION — AWAITING OWNER-RETURNED EVIDENCE`

- verbatim owner authority:
  `R4_4_6_OWNER_EXECUTION_AUTHORITY_ADOPTION.md`;
- frozen token file:
  `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md`, SHA-256
  `b3f917f7c1b0fe7d4a1a99a00e5371a86fb049ff7417d63acc009e7ca2023b4b`;
- accepted R4.4.6 freeze:
  `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89`;
- sole fresh-verifier PASS:
  `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748`;
- accepted predecessor evidence: the R4.4.5 `returned/` snapshot remains
  byte-exact at 28 objects with ordered aggregate identity
  `ea52c8ee03ba3e5cd0ce04013885aae35d3ac283026f5ca4a42626e95a81d618`;
- successor start state: sibling `returned_r4_4_6/` and fixed temporary root
  `/private/tmp/chirality-dapp93-owner-operated-20260807` are absent.

The owner-personal attempt begins at frozen runbook step 1 in a fresh logged-in
macOS GUI session. The owner personally opens the `CONTROL` and `LLDB`
Terminal tabs and sets both to
`/Users/ryan/.codex/worktrees/7388/chirality`. Every successor return operation
uses the frozen sibling `returned_r4_4_6/` namespace; the accepted R4.4.5
`returned/` snapshot is not moved, deleted, overwritten, or reused as the live
destination.

Follow `prepared/OWNER_OPERATED_RUNBOOK.md` literally and preserve all frozen
sequencing, phase, retention, terminal-cut, and failure-route gates. Stop
forward execution on any command failure, presence mismatch, network
indicator, stale or wrong PID, helper exit, unexpected prompt, breakpoint,
deadline or debugger state, missing byte, credential-bearing output, or other
deviation. Do not improvise, retry, search for another PID, choose another
target, or execute a command whose prerequisites do not hold.

No packet command or execution receipt has been run or written by this
manager. Stop here until the owner returns the immutable
`returned_r4_4_6/` evidence snapshot or an out-of-band blocker notice to App
HELP_HUMAN for governed intake.
