# Sealed Brief — Reviewer A Reciprocal Challenge of Reviewer B

## Gate and role

- `RequestedBy`: `EVALUATION`
- `ReviewerID`: `A`
- `Stage`: reciprocal challenge
- `ReviewFreeze`: `da31c19b5656dd74615e308c4215688971d33dc9`
- Independence precondition: satisfied. Both pass-1 returns were terminal, manager-validated with zero failures, and hash-frozen before this brief was issued.
- `InputFreeze`: `/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/PASS1_FREEZE.json`
- Target pass-1 directory: `/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/returns/B_PASS1/`
- Target report SHA-256: `4692e8bc2c05e0d0bf73e1a8dd9440f80166f77407aa36f5df98bcb4bdcc00f3`
- Target findings SHA-256: `9a14c635a1e7e235e50a6f233b637d4691e05bcb3010889b6cb98e3a38b3df85`
- Your frozen pass-1 report SHA-256: `1a1c857fd8241c892f7a7009bc44da7313fb00d1f0fee049f73d96da4aa4aa82`
- Your frozen pass-1 findings SHA-256: `b2f7f38ef8e987f8c48117e3c4869051f078555fbb4e52a1438cb3b99da44544`

Read both pass-1 packages only now. Do not modify either. Your purpose is adversarial evidence testing, not consensus formation and not revision of your pass-1 report.

## Write target and outputs

Write only to:

`/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/challenges/A_ON_B/`

Required outputs:

- `REPORT.md`
- `CHALLENGE.csv`
- `RETURN_MANIFEST.json`

Do not delegate. Do not edit any frozen input or product file.

## Required challenge population

Challenge every Reviewer B `BLOCK`/`REVIEW` finding and the deterministic lower-severity sample selected by sorted FindingID, first `ceil(N/4)`:

- High severity: `B-F-001`, `B-F-002`, `B-F-003`, `B-F-004`, `B-F-005`, `B-F-006`, `B-F-008`
- Lower sample: `B-F-007`, `B-F-009`

You may challenge additional B findings when evidence warrants it. Use exactly one row per target finding.

## Challenge schema

`CHALLENGE.csv` columns, in order:

```text
ChallengeID,TargetFindingID,Disposition,Assertion,EvidenceRefs,Consequence,Confidence
```

- Stable IDs: `A-C-001`, `A-C-002`, and so on.
- Allowed `Disposition`:
  - `CONFIRM` — evidence supports the target as written, including class/severity boundary.
  - `REFUTE` — frozen evidence disproves the target assertion.
  - `NARROW` — a material core is supported but assertion, severity, scope, consequence, or route is too broad.
  - `ADD-MISSING-EVIDENCE` — disposition cannot responsibly close without named evidence, or the target needs additional evidence to sustain its class/severity.
- `EvidenceRefs` must cite exact frozen product evidence using `da31c19…:<path>#<section|row|ID>`. Citing either report is allowed for comparison but is not product proof.
- `Confidence`: `HIGH`, `MEDIUM`, `LOW`, or `UNKNOWN`.

Do not convert semantic similarity into automatic agreement. Test assertion, evidence, class, severity, consequence, and smallest route independently.

## Report contract

`REPORT.md` must contain:

1. basis and hash attestation;
2. method;
3. required and additional challenge coverage;
4. result for each challenged finding;
5. convergences that survived adversarial testing;
6. standing divergences, including severity or route disagreements;
7. possible shared blind spots with frozen evidence;
8. implications for non-averaging fan-in;
9. explicit statement that challenge is not consensus or product acceptance.

`RETURN_MANIFEST.json` must record reviewer ID, review freeze, target reviewer, target report/findings hashes, output hashes/byte counts for `REPORT.md` and `CHALLENGE.csv`, row count, and confirmation that both pass-1 packages remained unchanged.

## Acceptance criteria

- All required target IDs appear exactly once.
- Every row uses an allowed disposition and has frozen evidence.
- Refutations/narrowings identify the exact failed portion.
- Shared blind spots remain evidence-linked and do not become invented scope.
- No input hash changes; no write outside the challenge target.
- No score and no attempt to force consensus.
