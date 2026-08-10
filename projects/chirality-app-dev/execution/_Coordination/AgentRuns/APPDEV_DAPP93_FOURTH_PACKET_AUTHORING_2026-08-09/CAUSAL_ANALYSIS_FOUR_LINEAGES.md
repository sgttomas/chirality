# Manager causal analysis — four D-APP-93 authoring failure families

Status: `MANAGER-VALIDATED COMPARISON — FOURTH LINEAGE BLOCKED`

| Lineage/family | Durable outcome | Proximate failure | Causal analysis | Design effect / remaining lesson |
|---|---|---|---|---|
| Attempt-3, successor, and V2 | Misaligned drafts and supporting artifacts preserved; no accepted ledger/author return | Drafts targeted inherited/dead command identities; the successor ledger was lost and V2's ledger author returned nothing | Content preceded a durable accepted command-authority source. The ledger was a single point of loss and downstream drafts could not prove one-to-one authority | Owner retired the dead lineage and required ledger-first fresh authoring |
| Prior fresh lineage | Zero N1 artifact and zero terminal return | Monolithic N1 was interrupted at 6m40s after quiet finite checkpoints | No staged durable output, shared time budget, or output-growth liveness criterion made progress indistinguishable from stall | Owner added bounded stages, durable writes, shared clocks, and progress telemetry |
| Third lineage | Six staged outputs plus terminal return; mechanically complete zero-hit 80-row ledger; downstream held | Broad `rg -l` crossed the stricter sealed absolute read fence because exclusion globs failed | Pacing worked, but path enforcement relied on negative patterns instead of an exact allowlist. No excluded content was displayed, copied, cited, or used. Owner later ruled this did not violate the owner's non-reuse direction; the historical manager BLOCK still stands | Owner authorized byte-exact conditional salvage and required positive path allowlists plus pre-dispatch/fan-in command validation |
| Fourth lineage | Stage 1 hash PASS, Stage 2 BLOCK, terminal return; 3 files / 8,911 bytes in 2m44s; downstream held | Frozen preflight specified absent `/usr/bin/rg`; frozen BSD `sed ... --` syntax also attempted nonexistent `--` path | Positive path containment worked and no forbidden existing byte was read. The manager's preflight was syntactic only: it failed to resolve executable location and exercise platform CLI semantics before sealing the brief | Any fifth lineage would require owner direction and a preflight that executes non-reading capability probes or otherwise proves exact executable paths/options before child dispatch; this record grants no fifth lineage |

## Comparative conclusion

The failure boundary moved each time: authority ordering, observability,
read-fence enforcement, then exact tool-form portability. The fourth lineage
did not repeat the third's scope traversal: explicit file arguments prevented
blocked-root discovery, Stage 1 lawfully reproduced all salvage identities,
and the failed scan opened no file. It nevertheless cannot clear taint because
the mandatory zero-hit result and 80-row provenance checks were not completed.

The exact fourth cause belongs to manager pre-dispatch validation. The child
correctly stopped rather than substituting `/opt/homebrew/bin/rg` or silently
editing the frozen command forms. No fifth lineage is authorized.
