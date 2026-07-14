# Retained finalizer attempts

Finalizer attempts 1 and 2 stopped before candidate mutation, evidence
normalization, terminal return creation, or manifest freeze. The added
frontmatter assertion rendered the already comma-space-delimited manifest
reference list with a second space after each comma. The production artifact
correctly contained the exact frozen list with one space, so the assertion
failed closed on `DEL-04-01`.

Reason code: `FINALIZER_ASSERTION_EXPECTED_REF_SPACING`.

Remediation: compare the production frontmatter directly to the exact frozen
TSV field inside brackets. No candidate or project content changed. Attempt 2
used Bash tracing solely to localize the failed assertion; its complete trace,
stdout, and exit code are retained. A fresh syntax check and complete
finalizer rerun are required.

Finalizer attempt 3 passed every member aggregate and terminalization check,
then the authorized-write-scope hygiene gate found six trailing spaces in two
copied historical run-record workspaces. The exact files and lines remain in
`WHOLE_DIFF_HYGIENE.warnings` from that attempt. Reason code:
`COPIED_EVIDENCE_TRAILING_WHITESPACE`.

Remediation: restore the four previously normalized copied evidence files from
their live read-only sources, expand the deterministic normalization step to
remove both trailing whitespace and terminal blank lines, regenerate all
direct/transitive determinism bindings, and rerun the complete finalizer.
