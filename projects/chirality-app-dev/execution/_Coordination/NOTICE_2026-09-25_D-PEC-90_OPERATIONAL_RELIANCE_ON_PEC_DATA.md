# Coordination Notice — D-PEC-90 operational reliance on PEC data

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality App (app-dev)
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`

The PEC owner ruled `D-PEC-90` R-A on 2026-09-25
(`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-90_RULING_2026-09-25.md`;
proposal SHA-256 `b04a8aa25c1d402fb03f6f15b6fb1eb27a0110e5cd3f3ded1db3717649a5e147`).
PEC product direction is now that agents may act on PEC record-tier data as
true as of the examined-through commit each response carries, without
re-reading the cited source, within stated bounds (pinned, coverage-honest,
record tier only for correctness, file fallback). Authority is unchanged:
rulings, acceptance, lifecycle transitions, merges and citations in governed
records rest on the file-native record; deleting PEC still blocks nothing.
The owner also stated that agents may eventually query PEC directly through
tool calls.

No PEC text changes yet. PEC will amend its PRD (PEC-K-03, §8, §9, §12) and
`projects/pec/AGENTS.md` in a scope change after PEC SCA-005 checkpoint 2
is accepted; reliance begins only at a PEC release whose gates prove parity
and coverage.

For this loop: PEC-K-03 is the exact row adopted under `D-PEC-67` K03-A. A later PEC scope change will replace its verify-before-rely precondition with operational reliance within the declared pin, coverage and tier, and PRD §8 will allow agents to query PEC directly through tool calls. Consumer use stays consumer-owned (PEC-K-03, PEC-K-11): the App decides whether and when its harness consumes or exposes PEC.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
