# Coordination Notice — PEC SCA-005: Root `LOOP_INIT` points at frozen loop ledgers

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality Root
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`

While surveying loop feeds for PEC scope change SCA-005 (survey finding
DR-17, `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/A1_SURVEY.md`),
PEC observed that Root `execution/_Coordination/LOOP_INIT.md` L15 lists
"relevant App and Piping `loop/LOOP_RECEIPTS.md`" among its handoff sources.
Those ledgers are frozen (App at Receipt-264, Piping at Receipt-162, as of
the survey); the App and Piping loops now write one central
`execution/_Coordination/.../RECEIPT.md` per undertaking alongside their work
graphs. PEC's accepted SCA-005 amendment (owner checkpoint-2 acceptance
2026-09-25, register row `D-PEC-92`) treats those ledgers as historical
grammar and reads central receipts and work graphs as current feeds.

For this loop: Root may update its `LOOP_INIT` handoff list, keep it, or
decline. PEC reads no Root instruction as changed by this notice.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
