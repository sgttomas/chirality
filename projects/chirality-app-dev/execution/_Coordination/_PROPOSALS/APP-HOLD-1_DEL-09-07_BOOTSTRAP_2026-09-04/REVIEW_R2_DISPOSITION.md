# Independent Review R2 Disposition

Review: `/private/tmp/chirality-app-v3-app-hold-bootstrap-20260904/reviews/REVIEW_R2.md`

Immutable review SHA-256:
`e56563ab57cda8ce06c69faba7c9b88285da19ef3bd1916a1545f49f6836b589`

Verdict received: `FAIL` — zero BLOCKER, one MAJOR, one MINOR, four NOTE.

## Findings

| Finding | R4 disposition |
| --- | --- |
| M1 — root-bound transform required one owner-question token but said to replace both occurrences | Remediated. The authoritative transform now requires exactly one occurrence and says `Replace that occurrence with ROOT`. The renderer retains the same single-token cardinality check. The transform leaf, approval manifest/root, owner question, conditional ruling, live-surface identities, artifact manifest, complete patch, and dependent evidence are all reminted. |
| MINOR m1 — Python checks could leave ignored bytecode/cache artifacts inside the exact proposal tree | Remediated. The application and review contracts now require `PYTHONDONTWRITEBYTECODE=1` for every Python invocation or an absolute `PYTHONPYCACHEPREFIX` outside the worktree. The renderer rejects an uncontained execution, rejects a relative or in-worktree cache prefix, rejects Python cache directories and bytecode, and the test suite proves those failures. Exact proposal-file-set verification is the last filesystem-sensitive check before `git add`; no later Python or artifact-producing command is permitted. |

## Notes

| Note | R4 disposition |
| --- | --- |
| N1 — runtime behavior is suitable once approval bytes are repaired | Accepted and preserved. No runtime semantic was weakened; live/proposal suites and exact simulations are rerun on R4. |
| N2 — inventory and cryptographic identities reproduced | Accepted. The R3 identities remain historical evidence only. R4 regenerates every affected identity and independently verifies the new graph and literal inventory. |
| N3 — basis was current at R2 review but must refresh if main moves | Applied. Final R4 is rebuilt on PR #699 merge `77ea8aa68affdb0485134b23d55303c362a312ac`, physical Receipt-225. The intervening PR #698 Node O evidence/status/receipt paths and PR #699's five `plans/shell-redesign_2026-09-04/**` paths do not overlap the candidate write set; all preimages, ID availability, authority hashes, and the absent target folder are rechecked. |
| N4 — review scratch restored after simulations | Accepted as historical review hygiene. R4 uses new isolated candidate, simulation, and patch-check worktrees and leaves prior candidates/reviews untouched. |

## Prior remediation status

R1-M2 and R1-m1 remain closed: the literal proposal/live inventory is retained,
the artifact manifest still excludes only itself, and strict clean-basis patch
checking/application remains required. R1-M1 is closed only through this R4
repair of the last contradictory transform sentence and fresh independent
review over the reminted approval root.

No finding was waived or silently deferred. The R3 owner question and approval
root are unsafe historical candidate bytes and must never be presented or
accepted.
