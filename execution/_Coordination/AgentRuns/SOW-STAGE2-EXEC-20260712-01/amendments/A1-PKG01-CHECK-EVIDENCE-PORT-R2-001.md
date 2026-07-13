# A1 PKG-01 Check-Evidence Portability R2 Amendment 001

Status: `ACTIVE — RECONCILIATION-FINDING REPAIR ROUTED TO OWNING MANAGER`

## Trigger and exact defect

Independent `RECON-A1-F` found that the accepted PKG01 generated-check
postimages each retain one unclassified checkout root in the generated
`workspace_root` field, contradicting the package claim that generated check
metadata has zero checkout-root prefixes.

| Artifact | Bytes | Current SHA-256 | Exact remaining defect |
|---|---:|---|---|
| `instances/WORKING-A1-PKG01/PROJECT_CHECKS.json` | 45,934 | `756aa875a1279526dc192b4e338f049167a7de1134f18a6478450269931972a3` | one `workspace_root: /Users/ryan/ai-env/projects/chirality` |
| `instances/WORKING-A1-PKG01/PROJECT_CHECKS_PREMERGE.json` | 12,902 | `9ca4aac07fa13ace3794e1fe1a136a210a751519007991bc026839cd3b8a6638` | one `workspace_root: /Users/ryan/ai-env/projects/chirality` |

The initial `CHECK_NORMALIZATION_MANIFEST.tsv` remains valid historical R1
proof: its recorded postimages are the exact current R2 preimages. It must not
be rewritten or misrepresented as the final current binding. The two current
hashes are directly bound by package `MANIFEST.tsv` and by that historical R1
manifest; the former must be refreshed, while the latter must remain frozen
and be classified as the intermediate chain.

## Exact owning-manager repair

`WORKING-A1-PKG01` may replace only the exact string
`/Users/ryan/ai-env/projects/chirality` with `~` once in the `workspace_root`
field of each named JSON file. No other occurrence or field may change. It
must write a new package-local R2 normalization manifest/check record with
exact pre/post paths, byte counts, hashes, one substitution per file, and
reverse-substitution hashes reproducing the two exact preimages above.

Both postimages must parse as JSON; every command, status, exit code,
stdout/stderr byte, and substantive result must be unchanged; all six App
checks must remain PASS. Generated package/child evidence must then have zero
checkout/temp prefixes outside the already accepted exact copied
source/control and marker-bound `PRESERVED_SOURCE_LITERAL` inventory.

The owning manager may update only generated package closure surfaces needed
to bind and explain the repair: a coordination notice, `CHECKS.md`,
`PACKAGE_HANDOFF.md`, `RETURN.md`, `STATUS.json`, and `MANIFEST.tsv`. These
updates may add the RECON finding, R2 chain/proof, final postimage hashes, and
rerun disposition only; all member/candidate hashes, counts, verdicts,
replacement/rollback manifests, author/verifier evidence, project-read-only
claim, and lifecycle/integration posture must remain unchanged. Regenerate
the package manifest last so every required current and historical binding,
including this amendment and R2 proof, reproduces. Record the old and new
package-manifest hashes and row counts.

## Return and rerun gate

Return terminal PASS/BLOCKED to HELP_HUMAN with exact changed paths and proof.
`RECON-A1-F` must then rerun package fan-in against the updated PKG01 package;
no prior 186-binding aggregate result is accepted without that rerun.

Any different JSON edit, failed reverse proof, stale current binding,
unclassified prefix, failed check, candidate/input/status/child-evidence
mutation, project write, or write outside the exact owning package/amendment
surfaces blocks A1 fan-in.

This amendment changes no scope, migration authority, acceptance criterion,
candidate meaning, lifecycle, risk, integration gate, H1/H2 posture, ISSUED
state, release state, or retirement state. It repairs generated evidence only.
