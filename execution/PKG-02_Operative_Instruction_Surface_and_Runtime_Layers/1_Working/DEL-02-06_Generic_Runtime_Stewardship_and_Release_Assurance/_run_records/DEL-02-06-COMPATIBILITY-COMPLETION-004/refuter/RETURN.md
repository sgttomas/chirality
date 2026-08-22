# N2 fresh compatibility-completion refutation return

- Child: `N2-FRESH-REFUTER`
- Candidate: `candidate/COMPATIBILITY_COMPLETION_CANDIDATE.json`
- Exact reviewed SHA-256:
  `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`
- Exact byte length: `14191`
- Verdict: `ADMIT_FOR_OWNER_EXACT_BYTE_REVIEW`

This verdict admits the exact prepared bytes for the owner's separate review.
It is not acceptance, implementation authority, lifecycle effect, cutover,
release, publication, reliance, notice, foreign-loop authority, Git authority,
or a substitute for any held binding.

## Finding ledger

| ID | Severity | Refutation target and exact evidence | Disposition |
|---|---|---|---|
| `N2R-001` | `NONE` | Independent SHA-256 is `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`; byte length is `14191`; parsed bytes equal canonical indent-2, key-sorted JSON with exactly one terminal LF. | `PASS` |
| `N2R-002` | `NONE` | The top-level binding-group key set is exactly the eight groups required by accepted `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md`. The candidate contains exactly six semantic-member entries, one per accepted member, and binds the sorted package manifest SHA-256 `6005a00695a96eb46e59896f01653d3504ef85b35a7d28509bba8d33171425e2`. | `PASS` |
| `N2R-003` | `NONE` | Current bytes reproduce the six accepted member SHA-256 identities: `2bff966d...7d13`, `7f64cfd2...9153`, `d7c1838c...d95a`, `2ce3aeae...2e6c`, `cbe36a27...7bc1`, and `9b023b34...f5f8`. They match both `ACCEPTED_SEMANTIC_MEMBERS.sha256` and `V2_CANDIDATE_PACKAGE_MANIFEST.sha256`; accepted snapshot SHA-256 remains `3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`. No accepted historical member was changed by this review. | `PASS` |
| `N2R-004` | `NONE` | Every candidate path marked available exists as a regular file and hashes exactly. Additional available identities were independently resolved and reproduced: accepted N2 census `14abde6b...4ee52`, N3 evidence design `e05b56d3...80dd0`, repaired application trace `0f49b9f9...bd564`, owner authority transcript `6396dd26...0c566`, Root Scope of Work `dc78196e...0146`, App decomposition `dd6027b4...5c83`, and SCA-APP-005 run summary `bce5b987...7621`. | `PASS` |
| `N2R-005` | `NONE` | The Root CLI and App exact-operation text is reproduced from accepted N2 census `14abde6b...4ee52`; the Root accepted basis is `ScopeOfWork.md` clauses `REQ-004`, `REQ-005`, `REQ-009`, and `REQ-048`; App bases and clauses are exactly the two paths and hashes recorded in group 3. No PEC, Piping, Tier-0, route, Flow-A, session, residency, package, repository, or version label is substituted as a compatibility, source, or release identity. | `PASS` |
| `N2R-006` | `NONE` | Epoch `1` is a canonical positive decimal; `root-runtime-1` matches `root-runtime-<positive-decimal-epoch>` and uses no reserved unresolved value. The 24 frozen-basis mentions of `root-runtime-1` belong to the 2026-08-21 owner-supplied preparation carrier. In particular, the T1 carrier's line-130 analysis describes the accepted grammar while preserving the identity as non-binding until exact package acceptance. No prior accepted or adopted runtime identity collision was found. New-run mentions are likewise briefs, activation/basis records, validator constants, author evidence, or the expressly unaccepted candidate. | `PASS — NO COLLISION` |
| `N2R-007` | `NONE` | The document contains exactly ten `HELD_UNAVAILABLE` objects. Each has `identity: null` and non-empty `reason`, `owner`, `gate`, and `blocking_posture`. The held values are source identity, release identity, App conformance, Root CLI conformance, Root semantic/regression evidence, release-fan-in notice, Tier-0 relationship, implementation act, cutover act, and release act. | `PASS` |
| `N2R-008` | `NONE` | Held postures are semantically honest: accepted N3 remains `DESIGN_COMPLETE_NOT_EXECUTED`; SCA-APP-005 closed scope change only and preserved later App implementation/conformance; the accepted semantic snapshot expressly left the complete compatibility binding unproduced, Tier-0 unadopted, and implementation/cutover/release behind later gates. | `PASS` |
| `N2R-009` | `NONE` | The candidate's top-level `status` is exactly `PREPARATION_ONLY_UNACCEPTED`. Group 1's accepted status applies to the six-member semantic basis and manifest; the bound `root-runtime-1` value remains the owner-supplied candidate identity under the top-level status and authorization handoff. No authority or lifecycle effect is inferred. | `PASS` |
| `N2R-010` | `NONE` | The deterministic validator passed twice with zero issues. Its six negative mutations all failed as intended: zero epoch, reserved alias, missing group, member drift, invented held identity, and incomplete hold. | `PASS` |

No repair finding survives refutation.

## Enumerated unavailable bindings and consequence

1. Exact implemented Root source identity — blocks implementation, cutover,
   and release.
2. Exact release/distributable identity — blocks implementation, cutover, and
   release.
3. Accepted Root CLI/generic-client conformance evidence — blocks cutover and
   release.
4. Accepted App conformance or migration evidence — blocks cutover and
   release.
5. Executed and accepted complete Root semantic/regression evidence — blocks
   cutover and release.
6. Adopted Tier-0 relationship record for this candidate identity — blocks
   cutover and release fan-in.
7. Accepted compatibility cutover/release notice state — blocks cutover and
   release.
8. Accountable-human implementation act — blocks implementation, cutover,
   and release.
9. Accountable-human cutover act — blocks cutover and release.
10. Accountable-human release act — blocks release, publication, and reliance.

These are honest release blockers, not defects in a preparation-only binding
manifest. None was supplied, inferred, or replaced.

## Final disposition

`ADMIT_FOR_OWNER_EXACT_BYTE_REVIEW`

Only an accountable-human act may accept or return exact candidate SHA-256
`e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`.
