# Steers

Owner-carried standing-direction prompts that the owner pastes into a governed
loop session (Root, App, Piping) to direct one bounded tranche, plus the
owner-ruling records they are pasted with. Each steer names its basis gate
(exact `main` commit and file SHAs), write-disjoint nodes with check surfaces,
a not-selectable list, the failure rule, and the closeout contract (one
tranche, one branch, one PR, receipt after the fact, no merge).

Steers are non-governing plans-folder instruments under `plans/README.md`.
They authorize nothing by themselves: the receiving loop transcribes the steer
and any ruling record verbatim into its receipt as CHAT_TRANSCRIPTION and acts
under its own instruments. A steer whose basis gate no longer matches `main` is
stale and must be re-issued, not patched in the session.
