# Coordination Notice — PEC SCA-006: operational reliance on PEC data adopted in PEC's PRD and instructions

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality Runtime (`projects/chirality-runtime`)
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`

PEC scope change SCA-006 carries the `D-PEC-90` R-A direction into PEC's
text. The owner adopted PEC PRD v2.4 by accepting SCA-006 checkpoint group 2
(`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`).
PEC-K-03 now describes operational reliance on PEC record-tier claims within
the pin, coverage and trust tier each response declares (PEC-ORI-007), with
file fallback. PEC-API-007 adds a read-only query surface for agent tool
calls under a new PEC-local `agent` access class, and PRD §12 a standing
reliance-advertisement gate. PEC output stays never citable as authority.

**SCA-006 checkpoint group 2 amendment 1 (2026-09-26).** The owner directed,
verbatim:

> Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them.

> revision 4: drop remaining-items and remaining-loop; yes, ride checkpoint 3.  SCA-006 pinned.

Recorded at
`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/`.
The one correction it adds to `projects/pec/AGENTS.md`: PEC adds no new
deliverable `## Remaining` sections or entries, and no PEC feed profile reads
them. The existing sections stay in place until any retirement ruling, which
is a separate owner-directed undertaking.

Changed paths and authority:
`docs/governance_harness/tranche_manifests/PEC-SCA006-OPERATIONAL-RELIANCE-20260926.yaml`.

For this loop: the DEL-02-06 Scope of Work names `projects/pec/AGENTS.md`,
`projects/pec/execution/_Decomposition/Deliverables.csv` and
`projects/pec/execution/_Decomposition/ScopeLedger.csv` as read-only sources,
and run record `DEL-02-06-RUNTIME-SPEC-001` pins them as S4–S6
(`clients/SOURCE_PINS.json`). SCA-006 changes all three: this tranche changes
`AGENTS.md`, and decomposition revision 1.6 adds SOW-097..100 and
DEL-08-06 and DEL-10-13 to the two registers. The `agent` access class is
token-scoped and local to PEC. Its credentials remain part of PEC's open
token-mechanism decision (PRD §16.6, OI-006). Operational reliance begins only at a PEC release that
passes the PRD §12 reliance-advertisement gate. No PEC release has passed it.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
