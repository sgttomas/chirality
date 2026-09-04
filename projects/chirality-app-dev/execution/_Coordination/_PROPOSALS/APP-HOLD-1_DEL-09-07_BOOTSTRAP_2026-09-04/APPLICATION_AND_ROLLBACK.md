# Exact Application and Rollback

Status: `CANDIDATE_INSTRUCTIONS_NOT_EXECUTED`

## Frozen identities

The SHA-256 of `APPROVAL_EFFECT_MANIFEST.sha256` is the acyclic owner-approval
root. The manifest hashes every authoritative leaf and intentionally excludes
itself. `tools/render_approval.py` derives the exact owner question and
conditional ruling from that root plus the external SHA-256 of
`ARTIFACT_HASHES.sha256`, and rejects any owner answer other than the exact
string `Yes`.

Preparation and independent review may reproduce the conditional ruling
postimage with that fixed input solely to verify exact future bytes. That
pre-approval reproduction is not an owner answer or ruling. Operational use
and copying to the live decision path remain gated on a new exact owner `Yes`
to the frozen two-digest question.

`ARTIFACT_HASHES.sha256` hashes every proposal file except exactly itself and
the two digest-dependent deterministic outputs: `OWNER_QUESTION.md` and the
proposal ruling postimage. Its own SHA-256 is external review evidence and a
literal input to both rendered outputs; the three exclusions are mechanically
necessary to avoid a digest cycle. The renderer verifies the excluded outputs
exactly from the bound templates, approval root, and artifact digest.
`PROPOSAL_FILESET.txt` lists every proposal file, including itself, both
manifests, and `COMPLETE_CANDIDATE.diff`. `LIVE_SURFACE_MANIFEST.csv` carries
one literal row for every proposal file and every non-proposal later live
effect. `tools/render_approval.py verify` enforces all three set relationships.
After rejecting symlinks, the verifier accepts only directories and regular
files: it fails closed on every other observed filesystem entry, including a
FIFO, and names the offending repo-relative path in its diagnostic.

Every Python command in preparation, independent review, application, PR-head
verification, and rollback checking must suppress or externally contain
bytecode writes. Use `PYTHONDONTWRITEBYTECODE=1` for every invocation, or use
an absolute `PYTHONPYCACHEPREFIX` outside the proposal and application
worktree. The
frozen commands below use `PYTHONDONTWRITEBYTECODE=1`. An uncontained Python
command invalidates the exact-file-set assurance until a fresh clean
reconstruction and review.

## Preconditions

Before any later application:

1. fetch and rebase a clean isolated application branch on then-current
   `origin/main`;
2. rerun receipt validation and remint `RECEIPT_CANDIDATE.md` as
   `NEXT_AVAILABLE` with the live parent cursor;
3. prove D-APP-104 remains unused and every existing live preimage in
   `LIVE_SURFACE_MANIFEST.csv` still matches; any mismatch requires a new
   candidate and owner question;
4. run
   `PYTHONDONTWRITEBYTECODE=1 python3 tools/render_approval.py verify` from the
   proposal directory and independently recompute the SHA-256 of
   `APPROVAL_EFFECT_MANIFEST.sha256`, `ARTIFACT_HASHES.sha256`, and
   `APPLICATION_PAYLOAD_HASHES.sha256`;
5. require a fresh independent PASS report that names the exact artifact-
   manifest SHA-256 and approval root shown by step 4;
6. present only the byte-exact generated `OWNER_QUESTION.md`, which names both
   the exact approval root and exact proposal-artifact digest from step 4 and
   states that the prior 2026-09-04 `Yes` is historical/non-authorizing;
   require the owner's new exact affirmative answer `Yes`; any other wording
   requires a new review and owner question; and
7. preserve the SCA-APP-009 Gate-5 worktree and candidate mirror until this
   amendment is merged and they can rebase or receive byte-identical guard
   inputs.

## Exact authoritative materialization

After, and only after, all preconditions and the exact owner answer `Yes`:

1. Verify every entry in `APPLICATION_PAYLOAD_HASHES.sha256`, then copy its
   eight listed proposal postimages to the corresponding repo-relative live
   paths byte-for-byte.
2. Copy the proposal packet postimage to
   `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-104_PACKET_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md`.
3. Run:

   ```text
   PYTHONDONTWRITEBYTECODE=1 python3 tools/render_approval.py render-ruling --owner-answer Yes --output /tmp/D-APP-104_RULING.md
   ```

   This command reads the frozen artifact manifest digest. Compare the
   temporary file byte-for-byte with the proposal ruling postimage, then copy
   that exact output to
   `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-104_RULING_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md`.
4. Copy the exact decision-register postimage only if its recorded preimage
   still matches current live bytes.
5. Add the complete proposal directory with an observed file set exactly
   equal to `PROPOSAL_FILESET.txt` and an artifact-manifest SHA-256 exactly
   equal to the digest named in the independent PASS report.
6. Generate a new minimal receipt from the then-live cursor. Replace every
   provisional token in `RECEIPT_CANDIDATE.md`; do not append that candidate
   verbatim.
7. Re-run the full candidate check matrix, strict forward patch application
   from the exact basis, exact change scope, decision-ID collision,
   receipt/corpus checks, and Git whitespace checks on the application branch.
   The binary `COMPLETE_CANDIDATE.diff` materializes the exact 53 static paths
   that do not depend on its own or the artifact-manifest digest. Complete
   reconstruction then adds the patch and artifact-manifest files and renders
   `OWNER_QUESTION.md` plus the proposal ruling postimage. The resulting exact
   57-path candidate must be byte-identical to the frozen source.
   Prefix every Python invocation with `PYTHONDONTWRITEBYTECODE=1` (or use the
   permitted absolute external cache prefix) and do not create or retain a
   cache inside the proposal or worktree.
8. After every other check and after all intended bytes are final, run
   `PYTHONDONTWRITEBYTECODE=1 python3 tools/render_approval.py verify` as the
   **last filesystem-sensitive check before `git add`**. It must prove the
   observed proposal file set exactly equals `PROPOSAL_FILESET.txt`, the 49
   literal proposal rows, and the 46 acyclic artifact-manifest leaves. Do not
   run another Python command or any command capable of creating a working-
   tree artifact between this PASS and staging. The verifier must reject and
   path-name every symlink, cache/bytecode artifact, and entry that is neither
   a directory nor a regular file. If it fails, stop; do not delete an
   unexplained artifact and continue from the same assurance.
9. Stage only the exact literal application set, commit, push, open a PR,
   independently verify the exact PR head under the same bytecode-containment
   and final-file-set rule, wait for
   required CI, and leave merge to the owner.

The bootstrap row is structurally valid but dormant while the old
decomposition preimage remains; DEL-09-07 must still block on the application
branch before the SCA authority pair is present. Any half-applied authority or
guard state therefore cannot be treated as a PASS.

## Post-merge SCA ordering

After the amendment merge, rebase the SCA-APP-009 Gate-5 lane on that merge.
Apply its separately authorized decomposition and companion postimages as one
rollback unit while `_LATEST.md` remains at the pinned old preimage. Copy the
same guard payload bytes into the disposable candidate mirror before its
preflight. Each checkout must pass its own exact token. No PREPARATION call may
start between partial file copies or before the relevant preflight returns
`ALLOW`.

## Rollback

Before amendment merge, restore each modified live file from its recorded
preimage, remove only the two new D-APP-104 live files and this new proposal
tree, and remove only the reminted receipt block. Re-run APP-HOLD integrity,
receipts validation, corpus status, exact scope, and `git diff --check`.

After amendment merge, do not rewrite history. A corrective PR may restore the
preimage guard behavior or retire the row only through a new exact owner
decision. The SCA transaction remains independently rollbackable: if its
authority pair is restored or its pointer moves, this bootstrap admission
already fails closed.

No rollback instruction deletes or changes SCA-APP-008 history, Root state,
product source, or any unrelated worktree content.
