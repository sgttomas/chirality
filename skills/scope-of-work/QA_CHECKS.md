# QA CHECKS — scope-of-work

1. The exact pilot variance covers the deliverable path.
2. All four source files exist, remain byte-identical, and retain authority.
3. `_STATUS.md` is byte-identical and remains `IN_PROGRESS`.
4. Candidate frontmatter, headings, IDs, references, and matrix validate.
5. Every source line is covered by a source marker and disposition.
6. Every marker binds the current source hash and a defined target ID.
7. `MERGED` and `SPLIT` mappings preserve all contributing references.
8. Every `OUT-*` maps to declared scope/objective references.
9. Every `AC-*` maps to `VER-*` or an explicit human-review method.
10. REVIEW can consume the candidate `AC-*` definitions without minting new IDs.
11. Parity passes with no silent drop or text mismatch.
12. Repeated HTML rendering is byte-identical, source-hash-bound, script-free,
    and contains no external resource reference.
13. The return distinguishes schema, project-content, and execution-substrate
    findings.
14. No accepted branch is left in dual-format state.

Any failure produces a failed return and rerun requirements; it does not
silently weaken the acceptance gate.

