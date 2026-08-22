# Sealed Agent 2 brief — fresh R16 whitespace repair review

- Parent: WORKING_ITEMS instance `WI-PKG09-R16-STAGING-01`
- Role/form: genuinely fresh ephemeral generalist Agent 2 reviewer
- Session: `A2-PKG09-R16-WHITESPACE-REVIEW-01`
- Review cycle: fresh review after repair cycle 1
- Basis: branch `codex/app-login-proof-r16-staging`; exact HEAD
  `06f60e42e35ea5c39abf9e33c4d3e877d77c4497`; empty real index
- Subject: the exact 35 paths enumerated in
  `repair-cycle-1/executor/SUBJECT_INVENTORY.md`
- Write scope: only `repair-cycle-1/review/REVIEW.md` and read-only-check logs
  beneath `repair-cycle-1/review/`
- Delegation, repair, build, proof, GUI, operator-path, temp-root, or Git
  mutation: prohibited

## Objective

Independently attempt to refute the executor's claim that the complete
35-path R16 candidate has exactly the twelve reported whitespace defects
repaired, with only necessary current hash/reference refreshes and no semantic
change. Treat every existing return, review, and manager verdict as an
assertion rather than proof. Return exactly `PASS` or `FINDINGS`.

## Mandatory review matrix

1. Require exact branch/HEAD, empty real index, App-only dirty containment,
   and exactly the frozen original 35-path subject plus additive repair-cycle
   controls.
2. Reconstruct all six pre-repair authored files by appending one LF and
   require the six exact old SHA-256 identities recorded in
   `PRE_REPAIR_EVIDENCE.md`; prove repaired files end in exactly one LF.
3. Reconstruct both pre-repair logs by inserting only bytes `20 0d` before the
   LF on lines 16, 17, and 18; require old hashes
   `900a08787bdeaa946a85997f12824dcc73af0ad5cb18febad483cbcf6da8bf16`
   and `e1f3bc133fb1a993611acf7952fcabd89bb5bdab09ae5e58519c5b1b01b262e9`.
   Prove their current hashes are respectively
   `827459042c5115f7b0e1ac14d9a25d9550bc48ddf1b1cf5442adafc4d1975ee5`
   and `67f9c2de21de732f819e59cad4f4b94429cd654c227fc27653ed676d9937ce62`,
   with visible text and line boundaries otherwise unchanged.
4. Independently inverse-substitute only authorized hash tokens to reconstruct
   the pre-repair R16, executor return, prior review, and manager return.
   Require current hashes `348397ce3f7a217492017f187c7068b7b41cd9ea0e279f8b4bf86c1daaf9108e`,
   `f24635a2392e6c5bc716a35dbf87615dbfaaa2a52e48c845b60d21558df07e88`,
   `2f027dc8fcf25663f625d2d89a67b715b258ffd14b883689886c8e9bf08e312f`,
   and `537c7936823ed9c2f21dfaeca7a9f6c838a86494e4e0cfce58c0d5f07e725496`.
5. Search all current-reference-bearing subject and repair controls for stale
   old identities. Distinguish explicitly historical pre-repair evidence from
   current identity claims; report any stale current reference.
6. Prove package identity, R16 command/procedure, DEL lifecycle/state,
   owner-facing values, verdicts, fences, counts, and all non-hash semantic
   claims are unchanged. Require DEL status SHA-256
   `4f9e04a3d229b9d64c83a038ba980518709684b3ed36fbb5e1d96172653b21a6`.
7. Require JSON validity for every subject/control JSON and verify no raw
   evidence outside the two exact logs was rewritten.
8. Run `python3 tools/validation/validate_candidate_whitespace.py --repo-root .
   --base-ref origin/main --paths projects/chirality-app-dev`, actual
   `git diff --check -- projects/chirality-app-dev`, and actual
   `git diff --cached --check`.
9. Run `git diff --no-index --check /dev/null <path>` separately for every
   current non-ignored untracked App text file, accepting only content-difference
   exit `1` with no whitespace diagnostic.
10. Independently construct a staged-equivalent patch or isolated temporary
    index for every current candidate/control path; require Git's whitespace
    check to pass while proving the real index hash and emptiness unchanged.
11. Verify executor return SHA-256
    `d92a47a4c5c7d5fc7f42914bfea0469da5ca428f1c7749e0199095f0589bf2a6`,
    exact 35-entry inventory content hash
    `7ee24b24f7922916d1a1b5a768f05b3f5f9f226d3e62e0b5761201aa667d5d23`,
    and all declared command outcomes.
12. Confirm no build, proof, GUI, operator job/plist/launcher, authorized-temp
    recovery root, stage, commit, push, merge, signing, notarization,
    deployment, distribution, or release act occurred during this cycle.

Any discrepancy is `FINDINGS`; do not repair it. The review return must name
exact findings, hashes, command exit statuses, subject/control path counts,
rerun triggers, and any blocker. Do not delegate or mutate the subject.
