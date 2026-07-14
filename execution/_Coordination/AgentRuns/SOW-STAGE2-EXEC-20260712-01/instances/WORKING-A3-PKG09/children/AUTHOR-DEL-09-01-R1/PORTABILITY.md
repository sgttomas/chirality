# Portability Record — AUTHOR-DEL-09-01-R1

- All authored evidence references are repository-relative or use the `{REPO_ROOT}` token required by the TASK run-record contract.
- The candidate path, child evidence path, and live source path are expressed from the repository root.
- The sole machine-specific source literal is separately recorded in `PRESERVED_SOURCE_LITERAL_INVENTORY.md`; it was not normalized.
- `MANIFEST.tsv` is repository-relative and self-excluding.
- Replay requires only the repository checkout and registered local `tools/scope_of_work/` tools.

Verdict: **PASS**.
