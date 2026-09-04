# Independent Review Handoff — R6 / Remediation R2

Status: `REVIEW_READY_CANDIDATE_ONLY`

Preparation basis: `287b82f16c0d3970bac71e40b0e41fdd50569b08`

Application authority: none

Review the entire candidate, not only the live-path diff.

For every Python command, set `PYTHONDONTWRITEBYTECODE=1` or an absolute
`PYTHONPYCACHEPREFIX` outside both review and candidate worktrees. The frozen
commands standardize `PYTHONDONTWRITEBYTECODE=1`; do not run an uncontained
Python invocation inside the proposal tree.

1. Independently compute the SHA-256 of
   `APPROVAL_EFFECT_MANIFEST.sha256`, `ARTIFACT_HASHES.sha256`, and
   `APPLICATION_PAYLOAD_HASHES.sha256`. Run
   `PYTHONDONTWRITEBYTECODE=1 python3 tools/render_approval.py verify`;
   confirm the approval root binds every authoritative effect and that the
   artifact manifest hashes the exact 46-leaf acyclic set: every proposal
   file except itself, `OWNER_QUESTION.md`, and the proposal ruling postimage.
   Confirm the renderer exactly verifies both excluded outputs from the root
   and artifact digest.
2. Confirm `PROPOSAL_FILESET.txt`, observed proposal files, and the literal
   proposal rows in `LIVE_SURFACE_MANIFEST.csv` are exactly equal. Confirm
   every non-proposal live effect is also listed literally. Inject an unlisted
   FIFO into an independent proposal reconstruction and require the verifier to
   fail nonzero with a diagnostic naming that path; restore the proposal and
   prove clean verification still passes. Confirm the production branch fails
   closed for every entry that is neither a directory nor a regular file.
3. Review 100% of the all-binary `COMPLETE_CANDIDATE.diff` against the
   preparation basis, then test it forward from a clean detached basis with
   `git apply --check --whitespace=error-all`. Confirm it materializes the 53
   static paths; add the patch and artifact-manifest files; render the two
   digest-dependent outputs; and prove the reconstructed 57-path candidate is
   byte-identical to the frozen source. Strict reverse-check and reverse-apply
   must restore the exact clean basis without `--unidiff-zero`.
4. Compare every `postimages/**` file with its prospective live path and
   manifest binding. Verify all preimages against the exact basis.
5. Confirm normal ScopeOfWork scan and HOLD parity precede bootstrap
   evaluation; ordinary held targets always block; known clear targets retain
   all four operations and arbitrary declared entry paths.
6. Re-run both APP-HOLD test layouts independently. Do not collect the two
   identically named APP-HOLD modules in one pytest process. Separately run
   the approval-renderer tests.
7. Recreate the disposable exact-postimage simulation and verify absent,
   subset, and all-five scaffold states for both exact entry tokens. Re-run
   every adversarial class: wrong target/package/operation/token; each
   authority or pointer hash; ScopeOfWork appearance; extra, nested,
   non-regular and symlink paths; malformed/duplicate rows; contract
   collision; and active-HOLD collision.
8. Confirm D-APP-104 is still free on the preparation basis; the packet is a
   proposal; and the ruling is uniquely derived only from the exact answer
   `Yes`. Confirm the rendered question literally names the authoritative
   approval root and exact acyclic artifact-manifest digest; preserves the
   prior exact question/answer/root/artifact as dated history; and states that
   prior `Yes` does not authorize the replacement artifact.
9. Confirm the receipt remains `NEXT_AVAILABLE`, with Receipt-225 used only
   as the preparation-basis cursor. Later application must re-read the live
   ledger and remint from the then-current cursor. Reconstruct the complete
   61-path future tree with a provisional `AWAITING_OWNER` receipt that says
   simulation only and disclaims every unperformed act; require the receipt
   validator, registered harness checks, staged diff check, and basis-to-tree
   diff check to pass. Reject `SIMULATION_ONLY` as a Gate-Outcome value.
10. Confirm application instructions require current-main rebase, unchanged
    preimages, fresh independent PASS, exact owner approval, checks, PR-head
    review, and owner-gated merge before any Gate-5 checkout consumes the
    guard.
11. After every Python/test/manifest/patch/scope check and after restoring all
    intended candidate bytes, run the contained approval verifier as the
    last filesystem-sensitive check. Confirm exactly 49 proposal files, 49
    literal proposal rows, 46 artifact leaves, three exact acyclic exclusions,
    and no cache directory or bytecode. Do not run Python or an
    artifact-producing command afterward.
12. Reject any claim that this proposal authorizes PREPARATION, creates the
    DEL-09-07 scaffold or contract, applies SCA authority files, moves the
    pointer, waives audit, or changes product/release/Root state.

Return `PASS` only with zero BLOCKER or MAJOR findings. This preparation is
not an application, ruling, acceptance, lifecycle transition, or reliance
surface.

## Prior-review disposition focus

Verify every row in `REVIEW_R1_DISPOSITION.md` and
`REVIEW_R2_DISPOSITION.md` against the immutable review SHA-256 named in each.
In particular, confirm the single-token transform instruction is internally
consistent; independently challenge bytecode containment, the last-check
ordering, the acyclic approval identity, exact proposal-file enumeration,
artifact-manifest acyclic exclusions, and strict forward whitespace behavior.

Also read the post-application FAIL report at
`/private/tmp/chirality-app-v3-app-hold-bootstrap-20260904/post-reviews/POST_APPLICATION_REVIEW_R1.md`
and reproduce SHA-256
`8257d40edb46709cd16b5a4f7511cba3c5d78d246ac67d7c186c58b6fadbc9d1`.
Verify the remediation closes both blockers: exact current-main rebasing and a
global future tracked-application `git diff --check` over every path including
the embedded patch artifact.

Also read the immutable artifact-remediation R1 review at
`/private/tmp/chirality-app-v3-app-hold-bootstrap-20260904/remediation/reviews/REVIEW_REMEDIATION_R1.md`
and reproduce SHA-256
`39e43788ea83d1f44d8526976bd2e0c850af2d1a1209d8f151c6b20296fb909e`.
Independently verify the two-MAJOR disposition in `CANDIDATE.md`; do not reuse
either future-tree hash reported by that review.

## Known residuals for review

- The receipt validator exits successfully but its legacy summary says
  "frozen through Receipt-52" while the physical ledger tail is Receipt-225.
  The candidate uses the physical tail and never treats the summary text as a
  cursor.
- Bootstrap row retirement after pointer movement or ScopeOfWork appearance
  is separate maintenance. Runtime admission expires mechanically without
  waiting for that cleanup.
- Filesystem and current-main evidence is point-in-time. Later application
  repeats every preimage, file-kind, symlink, authority, pointer, and cursor
  check in a clean isolated worktree.
