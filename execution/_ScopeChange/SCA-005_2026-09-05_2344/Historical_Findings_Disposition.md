# Historical findings — proposed disposition only

Gate1 and Gate2 acceptance did not waive findings. The following is part of the proposed Gate3 review subject, not a selected disposition or retrospective edit.

| Finding | Exact historical gap | Proposed current treatment | Closure evidence still required |
|---|---|---|---|
| COV-184 | SCA004 lacks Pre_Change_Coverage.json under current contract filename | Preserve historical snapshot; use actual source audit copied in this new SCA phase | Owner accepts historical-layout gap treatment; do not fabricate past audit |
| COV-185 | SCA004 lacks Post_Change_Coverage.json | Preserve history; obtain an actual post-application independent audit at Gate5 | Gate5 audit exists and remaining findings have owners |
| COV-186 | SCA004 lacks RUN_SUMMARY.md | Preserve original evidence and pointer claims; new complete snapshot must expose current phase truthfully | Gate5 complete artifacts and exact pointer act |
| COV-187 | SCA004 lacks Supersession_Map.csv | Retain gap; proposed new delta and mechanically accumulated candidate map preserve claim bindings | Resolve prior-map completeness explicitly before active-map adoption |

Read-only inspection finds SCA001 and SCA002 prior Supersession_Map.csv are valid header-only maps with no data rows. The registered accumulation tool successfully reads the prior SCA002 map. The candidate cumulative map uses that supplied prior map plus this phase's proposed delta; it does not reconstruct an absent SCA004 map or invent prior accepted bindings. Proposal: preserve the SCA004 historical filename gap, use the verified prior map and exact current overrides for the successor map, and require conflict review before adoption. Any newly discovered admitted prior binding must be added through a new review subject, never silently omitted or backfilled into old snapshots.

Seven production-contract warnings (DEL-02-07..12 and DEL-04-11) remain open under their runtime/governance successors. Preserve source _CONTEXT/_STATUS and source Scope.md wording; PROJECT_SETUP/PREPARATION and owning document-production workflows must reconcile successor artifact contracts. Retirement does not mean warnings passed. The source audit's artifact filename information and15 IN ledger rows without objective values are preserved; no synthetic artifact-completion result is introduced.

The existing OI005/008/009/011 and accepted OI013 situated-working-root deferral remain attributable historical states. Current owning controls/charter must track unresolved duties under successor vocabulary. Old snapshots and accepted semantic/compatibility bytes stay immutable; nine live holds are neither waived nor filled, and Tier0's later R16-B continue-separate disposition remains separate from the historical tenth marker.
