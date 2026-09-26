# Coordination Notice — PEC SCA-006: operational reliance on PEC data adopted in PEC's PRD and instructions

**Status:** NON-BINDING NOTICE
**Receiving loop:** Chirality App (app-dev)
**Sending loop:** PEC (`projects/pec`), HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`

PEC's earlier `D-PEC-90` notice said PEC would amend its PRD and
`projects/pec/AGENTS.md` in a later scope change. SCA-006 is that change. The
owner adopted PEC PRD v2.4 by accepting SCA-006 checkpoint group 2
(`projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/`).
PEC-K-03 now describes operational reliance: an explicitly PEC-enabled
consumer may act on a record-tier claim as true as of its examined-through
SHA, within the pin, coverage and trust tier each response declares
(PEC-ORI-007), with file fallback. The verify-before-rely precondition of the
`D-PEC-67` K03-A row is superseded under `D-PEC-90` R-A; the K03-A bytes stay
as historical exact input, and PEC-K-11 is byte-identical. PEC-API-006 adds
response-size budgets, PEC-API-007 a read-only query surface for agent tool
calls under a new `agent` access class, and PRD §12 a standing
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

For this loop: use stays consumer-owned (PEC-K-03, PEC-K-11). The App decides
whether and when its harness consumes or exposes PEC data, and whether any
agent tool-call surface is enabled; injection is not required. Operational
reliance begins only at a PEC release that passes the PRD §12
reliance-advertisement gate. No PEC release has passed it, so nothing here is
usable now.

This notice grants no authority in the receiving loop, creates no
requirement there, and asks for no write. The receiving loop may adopt,
amend, defer or decline any implication under its own instruments.
