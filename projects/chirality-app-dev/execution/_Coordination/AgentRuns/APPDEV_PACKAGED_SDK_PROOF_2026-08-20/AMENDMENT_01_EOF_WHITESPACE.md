# Amendment 01 — candidate EOF whitespace correction

- Trigger: CHANGE precommit validation after staging the exact 22-path candidate.
- Finding: `git diff --cached --check` exited 2 because ten newly added AgentRuns records each carried one extraneous blank line at EOF.
- Classification: evidence/control-record formatting defect; no product, workflow, test, deliverable-state, authority, or acceptance semantic defect.
- Correction authority: HELP_HUMAN resumed the owning PKG-09 WORKING_ITEMS manager for this bounded correction.
- Correction: remove only the final empty line from `ACTIVATION.md`, `FROZEN_DIFF_MANIFEST.md`, `HANDOFF_STATE.md`, `LAUNCH_BRIEF_IMPLEMENTER.md`, `LAUNCH_BRIEF_REVIEWER.md`, `MANAGER_RETURN.md`, `MANAGER_VALIDATION.md`, `REVIEWER_RETURN.md`, `STATUS_REVIEW_COMPLETE.json`, and `WORK_GRAPH.md`.
- Review effect: the original frozen identities and reviewer PASS are superseded for candidate-closeout purposes. A corrected full candidate identity and a fresh read-only 100% review are required before returning to CHANGE.
- Product identity: `.github/workflows/desktop-release-template.yml`, its focused regression, DEL-09-04 product/state bytes, packaged verifier, and all dependency/runtime/provider boundaries remain byte-preserved.
- External proof: staged/mounted macOS execution and committed candidate-range G4 remain `REQUIRED / PR-CI-OWED`; neither is inferred by this correction.
