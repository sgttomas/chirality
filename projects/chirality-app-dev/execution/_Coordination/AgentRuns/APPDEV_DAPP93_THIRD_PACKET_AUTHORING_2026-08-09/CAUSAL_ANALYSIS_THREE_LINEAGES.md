# Manager causal analysis — three D-APP-93 authoring failure families

Status: `MANAGER-VALIDATED COMPARISON — THIRD LINEAGE BLOCKED`

This comparison uses only the prior blocked lineages' terminal manager and
handoff records named in `validation/HISTORICAL_ROOT_PRESERVATION.md`; those
records are coordination evidence, not authoring sources.

| Lineage/family | Durable outcome | Proximate failure | Manager causal analysis | What the next direction changed / did not cure |
|---|---|---|---|---|
| Attempt-3, including successor and V2 | Initial/successor drafts preserved; successor's required 149-row ledger absent; V2 preserved nine unaccepted supporting drafts but no ledger or author return | The draft corpus remained aligned to inherited/historical command identities while the sole complete successor ledger disappeared; the V2 ledger author then returned nothing and supporting authors could not align | Content was produced before one accepted, durable, complete command-authority source governed it. The ledger was both a single point of loss and semantically downstream of already-misaligned drafts. Fan-in could not prove one-to-one command authority | Owner ordered a wholly new lineage, no copying/repair, and ledger-first authoring. That correctly retired the dead scheme but did not yet add stage durability or progress telemetry |
| Prior fresh lineage | Zero source-reconstruction artifacts and zero child return; all author/freeze/verifier nodes held | A monolithic N1 produced no durable output before being interrupted after 6m40s under two finite closeout prompts | The supervisor could observe only chat quietness, not work-in-progress. The graph had no bounded stage outputs, shared time budget, or output-growth liveness criterion, so useful progress and true stall were indistinguishable | Third-lineage direction added named stages, per-stage/total budgets, first checkpoint at minute 10, durable-growth telemetry, and no interruption for quietness |
| Third lineage (this run) | Seven N1 outputs preserved; 80-row fresh ledger mechanically complete; historical-ID scan zero; N2-N6 held | A Stage 3 `rg -l` discovery used exclusion globs that did not match and necessarily searched bytes in all three roots excluded by the sealed N1 brief | Pacing and observability succeeded: six reconstruction stages and a terminal return appeared durably, with checkpoint 1 at minute 10 (2 files/18,078 bytes) and checkpoint 2 at minute 22 (6 files/110,306 bytes). The failure moved to scope enforcement: the child command relied on ineffective pattern exclusions instead of a path allowlist. Supervisory design contributed: HELP_HUMAN/WORKING_ITEMS operationalized the owner's no-resume/no-copy/no-repair direction as a stricter absolute child-read fence, but the pre-dispatch graph and brief did not mandate path-allowlisted search enforcement for that fence. No excluded content was displayed, cited, copied, or used. The search violated the sealed manager/Agent0 fence; it does not by itself prove violation of the owner's stated non-reuse requirement | The new cadence cured the prior opacity/no-return failure, but not enforcement of the stricter supervisory read boundary. Any future direction would need a new lineage and an owner-approved graph that makes allowed-path enumeration/tool enforcement a pre-dispatch invariant. This record authorizes no such fourth lineage |

## Comparative conclusion

The three blocks are not repetitions of one symptom:

1. attempt-3 failed at authoritative-content ordering and durable ledger
   custody;
2. the prior fresh lineage failed at observable staged production; and
3. the third lineage produced the requested staged evidence on pace but failed
   the stricter absolute child-read boundary imposed by HELP_HUMAN/WORKING_ITEMS.

The third lineage's mechanically complete ledger is preserved only as blocked
evidence. Its semantic quality and zero historical-ID result do not cure the
scope violation and do not make it an authoring input for a later lineage.
No fourth lineage may begin without owner direction.

The closeout does not attribute the absolute no-read rule to the owner. The
owner prohibited resuming, copying, or repairing prior drafts. The broader
no-read fence was a conservative supervisory operationalization, and the
supervisor shares causal responsibility for imposing it without requiring a
deterministic allowed-path search mechanism.
