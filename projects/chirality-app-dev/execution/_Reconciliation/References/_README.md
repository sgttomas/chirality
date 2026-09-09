# Authority-Doc Reference Reconciliation (D-APP-38)

**Model:** D-APP-38 Option D (hybrid) — an automated reconciliation tool (A) feeding versioned corpus
snapshots (B). Authority-document edits are allowed; a content change triggers a corpus **version bump**,
not a breakage.

## Why this exists

Each deliverable's `_REFERENCES.md` records the `sha256` of the common
authority documents (`docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`,
`docs/TYPES.md`, `docs/PLAN.md`, and `docs/PRD.md`) and its applicable method
corpus. Current deliverables cite the complete `software-decomp` workflow
closure; D-APP-45 limits the `domain-engine` workflow closure to DEL-10-01 and
DEL-10-03. Each workflow closure contains its `WORKFLOW.md` plus
`resources/contract.md` and `resources/method.md`. The authority
docs are living documents, so the
per-deliverable `Status` column drifts silently as they are edited. On 2026-06-20 a live recompute found
six of the seven references stale across the corpus while only REF-006 was flagged (D-APP-38 packet).
This tool makes drift detectable and reconciliation reproducible.

## Files

- `AUTHORITY_CORPUS.json` — the versioned snapshot store: `current_version`, the corpus `refs`, and a
  `versions[]` history (each with `date`, `binding_commit`, `reason`, and per-ref `hashes`).
- `reconcile_authority_corpus.py` — the reconciliation tool.

## Usage

```
python3 execution/_Reconciliation/References/reconcile_authority_corpus.py <command>
```

| Command | Effect |
|---|---|
| `status` | Recompute live authority-doc hashes; compare to the current snapshot version; report drift (exit 1 if drift). |
| `bump --reason "..."` | If the live hashes drifted, mint a new corpus version with the current hashes and make it current. |
| `apply` | Rewrite every deliverable `_REFERENCES.md` authority-doc row to the current corpus version (`Expected`=`Actual`=corpus hash, `Status`=`MATCH`). |
| `audit` | Report any deliverable rows not reconciled to the current corpus version (exit 1 if any). |
| `init` | One-time creation of the snapshot store (already done for `v1`). |

## Standard flow after editing an authority document

1. `status` — confirms drift and which docs changed.
2. `bump --reason "<what changed>"` — mints the next corpus version.
3. `apply` — re-reconciles table-form and bullet-form deliverable references to
   the new version, including canonical path migration for recognized retired
   method aliases.
4. `audit` — confirms 0 unreconciled rows.

A deliverable stays bound to the corpus version it was last reconciled against (encoded in its per-row
`ExpectedSHA256`); until it is re-`apply`-ed, `audit` keeps its drift visible. This preserves
per-deliverable content-binding while keeping the corpus honest.

## Boundaries

This tool reconciles reference records only. It does not edit authority documents, change any deliverable
lifecycle state, or authorize any `CHECKING -> ISSUED` transition. Corpus `v1` was established
2026-06-20 and all authority-doc references were reconciled to it (0 `HASH_MISMATCH`). Corpus `v4` adds
the framework-root domain-engine persona as a tracked authority source for PKG-10 conformance. Corpus
`v21` replaces the two retired role-file members with their complete canonical
workflow closures. This follows the Root four-role registry and its explicit
legacy-role mapping. Pinning the entrypoints and both referenced substantive
resources ensures that a contract or method change creates detectable drift.
The corpus does not add every active role instruction to each deliverable's
substantive source corpus. The PKG-00
control deliverables (`DEL-00-01`, `DEL-00-02`) use a control-reference table without authority-doc hash
pins and are intentionally out of scope.
