# Supplementary owner direction — 2026-09-05

Verbatim text (Markdown formatting preserved; displayed underscore escapes are equivalent literal path characters):

Supplementary instruction (replaces the earlier "make the newest workplan an overlay, do not edit it" step):

Retire the workplan overlay entirely, as the app-dev loop did under D-APP-114 and D-APP-115 (both on main in projects/chirality-app-dev/execution/_Coordination/_DECISIONS/). The loop init must point the operator at deliverables, never at a plan.

1. Move every loop/WORKPLAN_*.md (and any plan-currency note beside them) byte-identically with git mv into the project's historical archive, plans/workplans/ under the project root (for PEC, projects/pec/plans/workplans/). Record SHA-256 before and after for each file in the packet; do not edit or delete any of them. Ruled plans stay immutable at their new path.
2. Confirm the committed-HEAD loader line in the candidate init reports "no committed plan: deliverables alone" after the commit (the loader reads HEAD, so this only shows post-commit), and that the pointer index names plans/workplans/ under "Historical archive (never selection surfaces)".
3. Before retiring, read the newest plan's owner-intent paragraph, parked-lane list, and any temporary constraints. Carry them into a ruling record in that loop's own register (the app-dev form is D-APP-115_RULING_OWNER_INTENT_OF_RECORD_2026-09-05.md): the intent paragraph verbatim with the source hash as the loop's standing purpose; the parked list quoted as dated history only, with a sentence that live parked state is re-derived from the items' own (gated: ...), (stage-gated: ...), and NOT_SELECTABLE_UNTIL: markers and the register; each temporary constraint either located in a surviving home (an item's own pin, a landed receipt) or, if it has none, listed for the owner to rule on. That ruling record creates no plan, queue, or status surface and selects no item.
4. If any Remaining item's gating exists only in the plan (a parked lane the plan named that no item marker carries), add the marker to the item, with one dated history line and no scope change, so nothing that was parked becomes selectable by the plan's absence. List every such item in the packet.
5. If tools, validators, launchers, or the root catalog reference the plan path (grep the whole tree for loop/WORKPLAN_), update live code and launchers; leave immutable records alone and list them.
6. The retirement is one more separately rulable item in the same packet and PR (item C for piping; item D for PEC, after the migration). On the owner's merge direction it rules with the rest.
