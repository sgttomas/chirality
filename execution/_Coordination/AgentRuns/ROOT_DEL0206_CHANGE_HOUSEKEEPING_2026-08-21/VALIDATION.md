# Integrated validation — Root DEL-02-06 / CHANGE / housekeeping run

RunID: `ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21`

Verdict: `PASS_WITH_NODE_2_AUTHORITY_BLOCKER_AND_OWNER_GATES`

## Dependency-ordered commits

1. N1 `a22ebb592b08969277b8a9faa54eaa649f3b18bf` — DEL-02-06 exact
   compatibility-completion preparation.
2. N2 `fc0cf67c1f869c641b43d42bdfdc0f8924dc0aab` — independently
   reviewed missing-D-GOV-identity blocker; no instruction tranche landed.
3. N3 `a8025993c205eb7625cd6d0cf919028fc304de19` — federation, TM-ROOT-116
   closure, and two attention rows.

All are descendants of exact base
`1b375af4f1219ecfc00fc2755854aa7fd4220901`, which resolves as a commit and
contains required ancestor `adf805e0d9ac55787e8ac815c3018467babb7f50`.

## Node results

- N1: candidate SHA-256
  `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`,
  14,191 bytes; deterministic validator twice PASS; 6/6 negative cases PASS;
  fresh refutation admits exact bytes with zero findings; SOW_V1 PASS; REM-001
  satisfied without lifecycle change.
- N2: fresh authority review PASS; `agents/AGENT_CHANGE.md` unchanged at
  SHA-256 `950e96f4cfff13af48b9edd93a4b47356e8b388a430d70977fd528ffbd4120fa`;
  no G4 manifest/notices; 34 agent files with 0 errors/0 warnings; G4 corpus
  PASS; 66 focused tests PASS.
- N3: preflight and final federation COMPLETE over four canonical registers,
  79 typed findings, zero federation writes; Root validators PASS at 22 live
  / 105 archived; 49 Task Management tests PASS; keyed preservation and
  foreign-register hash preservation PASS.

## Integrated checks

- Root G0–G4: PASS at session entry; rerun required at final candidate HEAD.
- Candidate JSON parse/canonicalization/hash: PASS.
- Root live/archive Task Management validation: PASS.
- `git diff --check`: PASS through N3.
- Worktree before closeout artifacts: clean.
- No instruction-surface path differs from the base; no G4 tranche manifest is
  required for the failed/blocked N2 path.

Final pre-receipt rerun at published PR head
`0f3de6875e2e30b227f824131cd29e9884949600`:

- Root G0–G4 PASS; agent instructions 34/0/0; instruction entrypoints PASS;
- candidate validator and 6/6 negative cases PASS; SOW_V1 PASS;
- Root live/archive Task Management validation PASS;
- Task Management plus validation suites: 369 passed;
- practitioner harness suite: 350 passed;
- practitioner self-check exit 0 with standing findings only;
- Git diff hygiene PASS; branch based on unchanged
  `origin/main@1b375af4f1219ecfc00fc2755854aa7fd4220901`;
- PR #605 opened ready for review against `main`; governance harness check was
  in progress when the after-the-fact receipt was prepared.

## Holds and reruns

Final Root G0–G4, instruction entrypoints, agent validation, Task Management
federation/validation, candidate validation/negative cases, practitioner
self-check/tests, and Git hygiene must rerun after the receipt is appended.
If `origin/main` advances, no sync may occur without a later owner
authorization.
