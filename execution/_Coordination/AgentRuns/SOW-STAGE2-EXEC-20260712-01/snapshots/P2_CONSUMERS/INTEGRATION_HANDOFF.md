# P2_CONSUMERS Integration Handoff

Verdict: `PASS — READY FOR REMOTE PR RETRY`

The accepted upstream snapshot remains `P2_CONSUMERS`, an immutable derivative
package at C2F-R2 PASS, source-bound to the validated 48-root-plus-four-App
candidate from `main@e150c972889d05a8fc270239451a35c7512dc9a9`.

CHANGE created `codex/sow-stage2-consumers` from that exact base and committed
the contained source tranches serially:

- root consumers: `2af7e705fba0856b26d55b880bde5767c13ab961`;
- App runtime: `bb8ae7424de427ffe656fbbb6c22abc51266a851`;
- evidence binding: `75c74fa2784c802494e3e0d3892b858081891eb4`.

All bounded preintegration, source-hash, authority, caller-manifest, and source
containment gates passed. The first evidence staging found six C2F-R1 records
with a terminal blank line; HELP_HUMAN authorized and applied formatting-only
normalization under `C2F-REMEDIATION-001` 001-D. Restaged diff hygiene passed.
No finding, verdict, reference, or P2-bound hash changed.

The branch contains exactly the three required source/evidence tranches and no
fourth semantic tranche. Working state is tracked-clean except the pre-existing
untracked `.claude-worktrees/` container. Blockers and waivers: none.

Remote closure still requires the source-binding-only record commit, push, one
non-draft PR to `main`, remote changed-path/check verification,
blanket-approved repository-default merge, and synchronized-main verification.
If rollback is required after merge, revert the merge commit in a new approved
change; do not rewrite or force-push history. If the source branch changes,
authority/hashes/manifests/checks change, or remote main advances before merge,
rerun the affected readiness and remote gates.

B1 is the next dependency after C2G remote merge and synchronized-main PASS.
This handoff authorizes no conversion, lifecycle mutation, H1, H2, release, or
legacy retirement.

## PR #221 portability retry

The first remote validation left PR #221 open and unmerged: Harness pre-merge
passed, while governance-harness failed because ten newly tracked App run
evidence files carried checkout-specific absolute paths. Parent fan-in accepted
`HELPS-C2G-P1 PASS` under `C2G-EVIDENCE-PORTABILITY-001` 001-A/001-B.

The repair is a derivative-evidence portability tranche only: exact literal
substitutions in twelve already-bound App evidence files plus the amendment,
HELPS-C2G-P1 records, work graph, and CHANGE retry records. Existing P2 hashes,
source commits, verdicts, counts, authority, and lifecycle meaning remain
unchanged. Local containment, JSON parse, prefix absence, focused live anchors,
P2 hashes, and diff hygiene passed. Blockers and waivers: none. Remote merge
remains contingent on every required check passing against the new PR head.
