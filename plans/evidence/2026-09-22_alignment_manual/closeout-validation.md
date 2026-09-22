# Documentation closeout validation

Prepared by WORKING_ITEMS `/root/closeout_manager`, 2026-09-22, under
HELP_HUMAN `/root`. Branch: `codex/alignment-manual-and-agent-guide-20260922`.
Base and initial HEAD: `9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8`.

## Preflight — authors still active

This is preparation evidence, not final-candidate validation or acceptance.
`closeout-preflight.json` records the commands, exit codes and summarized
results. All nine preflight commands exited 0: role validation, workflow
metadata validation (74 packages, none invalid), practitioner-harness
self-check, live G0–G3, G4 schema validation (93 manifests including this
tranche), and affected-test selection. The selection is the
`practitioner_harness` and `validation` suites; no test execution is claimed
by a dry run. G4 range coverage awaits the actual submitted revision.

The configured remote is `git@github.com:sgttomas/chirality.git`. Git uses
the owner's configured Ryan C Tufts identity; authenticated GitHub account
`sgttomas` is available and configured for SSH Git operations. No credential
values are retained. A read-only remote query found main at the initial HEAD
and no remote task branch. Protection inspection found the required status
check `harness`, with admin enforcement enabled and no GitHub-enforced PR
review rule. The independent review required by Root still applies.

Python 3.13.14 has PyYAML, pytest, pytest-xdist and NumPy for the affected
checks, and markdown-it-py for HTML generation. CI uses Python 3.12. The
publisher reports the renderer pins markdown-it-py 4.2.0 and mdurl 0.1.2;
its final production and visual checks are separate pending evidence.

The docs change triggers governance-harness and Harness pre-merge. Piping's
selection workflow runs on every PR and determines its own applicability.
The authorized README navigation link also matches the desktop artifact
workflow, whose artifact job requires workflow dispatch or `artifact-proof`.
PEC's workflow paths do not match the declared documentation scope. No CI
workflow, protection, label or project instruction has been changed here.

## Candidate closeout procedure

1. Wait for the root's content-ready signal and the independently returned
   review. Confirm all intended artifacts and source records are present,
   the README change is only the declared navigation link, preserved
   originals match `INPUTS.json`, and the complete diff stays in scope.
2. Run renderer `--check` on final Markdown, verify local links/anchors and
   content parity, and use the publisher/root's final visual inspection.
   Run the affected Python suites, self-check and live guards against the
   candidate. Reassess affected checks after any repair.
3. Commit only the bounded submission using the configured owner identity
   and truthful agent attribution. Run conflict-marker and added-manifest
   G4 range checks over the complete base-to-candidate diff. Bind independent
   review to that revision or show its content identity and affected recheck.
4. Push through the configured SSH remote, create the PR, attach it to the
   task, and retain the source revision, independent review and validation
   in ordinary PR history. Observe required CI on the actual head and
   investigate material failures from other triggered checks.
5. Verify the source HEAD at merge. Under the standing owner authorization,
   merge only after required CI passes and independent review has no
   unresolved blocking findings. Report the resulting PR/merge without
   representing Git integration as personal owner review, governed
   acceptance, downstream adoption or release.

No staging, commit, push, PR or merge was performed during this preflight.
At the preflight return, all three preserved v1 files (Markdown, DOCX and PDF)
matched their `INPUTS.json` SHA-256 values, HEAD still matched the base, and
the Git index was empty. These checks will be repeated on the final submission.

## Drafted candidate checks — before review and visual closeout

The maintained affected-test command completed on 2026-09-22 with **897 tests
and 48 subtests passed** in the selected practitioner-harness and validation
suites. `closeout-candidate-tests.json` records its basis, command, timing and
scope. Role/workflow validation, self-check and live G0–G4 then all exited 0
against the drafted tree; results are in `closeout-candidate-guards.json`.
No product-wide test suite was needed for this additive documentation scope.

`closeout-candidate-checks.json` binds the inspected authored document bytes
and records these passing checks:

- The complete currently visible change set stays within the authorized
  scope; all 12 protected paths are covered by the new G4 declaration.
- All three preserved originals retain their input hashes.
- The six authored/entry documents contain 303 local link or fragment
  targets, all resolving to tracked or intended-submission files. The v2
  manuscript's local figure also exists in the submitted assets directory.
  Preserved v1 bytes are excluded from link repair.
- Renderer `--check` passes on guide SHA-256 `2b749f8f12dcd803c6017c93fa6e850257f4aaf88b3d07781842a8a4c0d2ab2b`
  and HTML SHA-256 `77bbc449bca0daa3ba4dd3644119a6deaedff3f89f606b26824a0bce504339b5`.
  The publisher's parity evidence matches these bytes and all its checks pass.
- The renderer also passes from an isolated four-file copy containing only
  its script, requirements, guide Markdown and expected HTML, with installed
  pinned dependencies. Dated run evidence is not a rendering dependency.
- No unresolved conflict-marker lines were found in the working candidate.

The content/publication reviewers and visual-inspection attempt were still
active during these checks. The browser tool rejected the file URL under its
security policy; no alternate browser route was used. The bounded offline
WeasyPrint attempt then stopped because native Pango was unavailable; it
created no PDF or page image. Browser desktop/mobile interaction, browser
print preview and static print-layout inspection are **NOT VERIFIED**. See
`html-publisher-offline-qa.json` for the actual boundary. No further visual
attempt or installation is planned; structural checks do not establish layout.

## Final review and authorized Git closeout

The independent content reviewer completed `final-content-review.md` and its
source record with no unresolved blocking or actionable findings. The
independent publication reviewer completed `publication-review.md` and its
source record after repairing and backchecking the two publication findings;
none remains open. Both reviewers were separate from the publication authors.
The closeout manager compared every reviewed subject's recorded SHA-256 with
the submitted bytes, including v2, review, guide, HTML, renderer, requirements,
and both navigation documents. `closeout-review-binding.json` records the
comparison without attempting to hash a commit into its own contents.

The root authorized Git closeout after those returns, with the visual limit
explicitly disclosed. No publication content changed after the reviewed
hashes or passing candidate checks; subsequent closeout edits record review
and validation state. The full Python suites therefore need no repetition
for evidence-only notes. Complete committed-range G4/conflict checks, source
commit identity, PR checks and resulting merge are retained in ordinary
PR/Git history. Required CI and the actual source HEAD must still be verified
before merging. This is Git integration under the standing owner grant, not
owner acceptance, project adoption or release.
