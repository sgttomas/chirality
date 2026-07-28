# Evidence correction record

During final validation after rebasing to `db4d3e4a2`, the baseline-only
`TOOLS/build_inventory.py` was rerun after contract repairs. It refreshed
`PRE_REPAIR_MANIFEST.sha256` from current contract bytes. The mistaken output
is preserved byte-for-byte as `MISTAKEN_POST_REPAIR_REFRESH.sha256`.

The eleven correct pre-repair values are independently reproducible from:

- `R1_BASELINE/VALIDATION_SUMMARY.csv`;
- W1 deliverable notes and checklists; and
- the contract blobs at Git basis `db4d3e4a2`.

The owner-facing root session applied the manager's recommended bounded
correction under Ryan Tufts's in-session direction of 2026-07-28:

> "Finish out your plan now (attaining your goal) with self merge of PRs and
> auto approve for owners rulings, which should still be recorded in the usual
> manner with your recommendation standing as what I approved."

Exactly eleven `PRE_REPAIR_MANIFEST.sha256` rows were restored from the
mutually corroborating R1 and Git-basis evidence. The corrected manifest has
SHA-256
`33a2f54646d74d12bf619ec039dc69ecb403ffd7e0acc5e17d0b558220f31547`;
the other twenty-one rows are unchanged.

A second baseline-only tool invocation had replaced the original W1 PASS
report with expected post-repair claim-text mismatches. Those mistaken bytes
are preserved at
`MISTAKEN_POST_REPAIR_W1_LEDGER_VALIDATION.json`, SHA-256
`7ea83d44bd172894552d969077edc2141071d554f578dde7a8096971ba4a5234`.
The deterministic baseline PASS was restored at
`WAVES/W1/W1_LEDGER_VALIDATION.json`, SHA-256
`8e3d91e034559cb126e6fa42676aa4eb30d72042c623a38dea7aeedff4160e92`.

No contract byte was changed by either evidence correction. The post-repair
state remains governed by the terminal independent PASS and the regenerated
backcheck.

Before first Git publication, one Markdown hard-break sequence was removed
from each of the second and third independent-verification reports so the
new tranche conforms to the repository's trailing-whitespace guard. The
quoted words, verdicts, and findings are unchanged; the third report's
internal hash citation and the package hash manifest were regenerated.
