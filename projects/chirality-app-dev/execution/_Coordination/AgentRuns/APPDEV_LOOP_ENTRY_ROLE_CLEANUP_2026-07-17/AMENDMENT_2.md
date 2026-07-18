# Verifier brief amendment 2 — tagged-launcher remediation

**Date:** 2026-07-17

**Predecessors:** `LAUNCH_BRIEF.md`, `RETURN_BLOCK_1.md`, `AMENDMENT_1.md`,
and `RETURN_BLOCK_2.md`

**Objective and acceptance contract:** unchanged

The parent accepted the second `BLOCK` and replaced unscoped substring
containment with project-specific tagged-launcher extraction:

1. The validator extracts only complete root-catalog blocks delimited by
   line-anchored `<init-prompt>` / `</init-prompt>` tags.
2. It selects blocks containing the exact `projects/<project-name>` token,
   requires exactly one such block, and byte-compares that block with the
   project-local launcher.
3. Tests now cover ordinary tagged-launcher drift and a stale exact local copy
   elsewhere in the catalog that attempts to mask drift in the actual tagged
   project launcher.
4. The full validation and practitioner-harness suites have been rerun after
   remediation.

Re-evaluate the original six sealed claims against the entire current diff.
Read-only scope and the binary `COMMIT-SAFE | BLOCK` return contract remain
unchanged. Do not write to the repository.
