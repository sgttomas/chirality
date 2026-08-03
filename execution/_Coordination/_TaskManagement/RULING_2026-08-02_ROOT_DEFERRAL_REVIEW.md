# Owner ruling — Root deferral review (2026-08-02)

Status: **OWNER RULING — AUTHORITATIVE FOR ROOT TASK MANAGEMENT ROW MAINTENANCE AND THIS CLOSEOUT TRANCHE**

Owning loop: Root

## Verbatim ruling

```text
RULING — Root deferral review 2026-08-02.

1. CLOSE all 23 TRIGGER_FIRED rows (TM-ROOT-036, 047, 077–097) as
   DUPLICATE to their exact App/Piping survivors, using the EvidenceRef/
   EvidenceSha sets in the classification report. Note for the record:
   the Piping loop's own deferral review independently classified every
   TM-PIP survivor as STILL_BLOCKED (open), which confirms DUPLICATE
   rather than any resolved-disposition is the correct closure.

2. DO NOT route DRAFT_HANDOFF_2026-08-02_APP_PACKET_RESIDUE_
   DEFERRAL_REVIEW.md. It is overtaken by events: the App loop's own
   TASK_MANAGEMENT session has already performed the packet-residue
   triage this handoff requests, and its dispositions for TM-APP-004
   through TM-APP-023 are before me now. Retain the draft as run
   provenance, unrouted. Leave the 20 ACTIVATABLE rows (TM-ROOT-055–061,
   063–067, 069–075, 101) DEFERRED with triggers unchanged; once the App
   closeout tranche lands on main, their triggers are fired with citable
   evidence, and a short follow-up pass will close them citing the
   recorded App dispositions.

3. ROUTE DRAFT_HANDOFF_2026-08-02_PIPING_RUNTIME_NEEDS_RESPONSE.md as
   drafted: ship it in this session's closeout tranche to
   projects/chirality-piping/execution/_Coordination/. Its bounded
   objective and non-product-basis boundary are approved as written.
   TM-ROOT-105 and TM-ROOT-109 remain DEFERRED on the response.

4. ADOPT the proposed sharper Trigger text for TM-ROOT-037, 039, 040,
   041, 042, and 102. TM-ROOT-035, 043, 046, and 104 keep their triggers
   as already exact.

5. Then relocate the newly closed rows with `taskmgmt archive`, validate
   live and archive registers, and assemble the closeout tranche for my
   Git gate — including the routed piping handoff and the consolidated
   App response notice already planned from the harvest ruling.
```

## Bounded effect

This ruling authorizes only the named Root register closures and trigger
maintenance, mechanical closed-row archiving, the exact Piping coordination
write, and assembly of the named closeout artifacts. It does not authorize
dispatch, App handoff routing, foreign-register edits, commit, PR update, or
merge.
