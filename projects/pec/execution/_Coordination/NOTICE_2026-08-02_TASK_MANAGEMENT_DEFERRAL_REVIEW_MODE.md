# Routed Change Notice — TASK_MANAGEMENT deferral-review mode adoption

Routed by: Root loop, 2026-08-02, under the `AGENTS.md` agent-index
change-notice rule.

This notice is coordination, never authority. The PEC loop adopts,
acknowledges, amends, declines, or defers any local response through its own
instruments and cadence. Reading any Task Management register or instruction
creates no duty for this loop (K-TM-3/K-TM-4).

## What changed

`agents/AGENT_TASK_MANAGEMENT.md` was amended by owner direction
(2026-08-02) to adopt the deferral review as a named mode, after its
successful exercise across all four loop registers on 2026-08-02 (this
loop's two-row ACTIVATABLE classification and D-PEC packet routing was one
of the reference implementations):

- A new mode 5, **Deferral review**, classifies every `DEFERRED` row as
  `TRIGGER_FIRED` (proposed closure with exact evidence; `DUPLICATE` to a
  surviving linked row where the concern remains open elsewhere),
  `ACTIVATABLE` (named instrument plus undispatched draft handoff), or
  `STILL_BLOCKED` (trigger-accuracy check with proposed sharper checkable
  text). Output is a decision-support classification report; no row change,
  dispatch, or routing before owner rulings; cross-loop triggers evaluate
  against committed bytes only.
- Former modes 5 and 6 (row maintenance; resolution orchestration) are
  renumbered 6 and 7, unchanged in content.
- An **Invocation cadence** note records the owner's generational rhythm
  (dev loops run to exhaustion or blockage; TASK_MANAGEMENT then runs per
  register, children before Root; the owner rules; the next generation
  consumes). It is expressly owner practice only and non-binding per
  K-TM-4: nothing anywhere requires a Task Management invocation.
- The title and frontmatter description now name the deferral review.

Instruction SHA-256:
`1114f487f72e178775a1ea5ee59d94b7990487c168549c6995f3922bd40a0179`
(superseding
`d8e50e1c35c6e512986800515c2642ea4696fe447f5a97f502a76cbb87625f28`).

## What did not change

Write scope, tool access, K-TM-1..6 and all other invariants, the mandatory
federation preflight, the §7.3 disposition taxonomy, the resolution paths,
the closeout contract, and the content of every pre-existing mode are
untouched. The adopted TM PRD (Revision 2, D-GOV-32) is unamended; it pins
tool subcommands and scanner scope, not the agent mode list. No lifecycle,
reliance, release, or professional-judgment act is performed by this notice
or the amendment. The two staged D-PEC packet requests
(`TASK_MANAGEMENT_DPEC_REQUESTS_2026-08-02/`) are unaffected.

## Follow-on for this loop

This loop's 2026-08-02 records cite the superseded instruction SHA as a
currency observation; those records remain accurate historical evidence and
need no rewrite. On this loop's next Task Management invocation or currency
pass, the live instruction hash to observe is the superseding value above.
The next PEC TASK_MANAGEMENT invocation may name `deferral-review` as a
mode directly.

## Related in-tranche launcher changes

The same tranche adds `projects/pec/init/taskmgmt-init-prompt.md` — a
paste-ready launcher for one TASK_MANAGEMENT session bound to this loop's
register (write scope `_DomainEngines/pec/_TaskManagement/`; sweep covering
both PEC trees), carrying the generational pass (preflight, harvest, deferral
review, archive, closeout) with owner rulings as the only gates — and renames
the development-loop launcher `projects/pec/init/init-prompt.md` to
`projects/pec/init/dev-loop-init-prompt.md`, with the root catalog's
references updated. Historical records are untouched.
