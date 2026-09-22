# RETURN: W_DOC_VAL (EXT item 4b: VALSTRAT and RELIANCE)

This is the TASK worker return to the EXT manager. The mechanism was a Claude Code harness-native descendant. It did not delegate. It wrote only inside `R2/EXT/DOC_VAL/`.

Both claims files are sealed at the SHA-256 values below. The notes files carry the census, the least-confident rows, the direction and cause, method friction and effort.

## DOC-VALSTRAT (`docs/VALIDATION_STRATEGY.md`, 9 units)

- **Rows:** 22. Split rate 1 of 9 units: §3's 14-row command table is `#4.1`..`#4.14`. SEE rows: 0.
- **Dispositions:** ALIGNED 13, STALE_SPECIFICATION 7, NOT_AUDITABLE 2. Confidence: HIGH 9, MEDIUM 13.
- **HumanDecisionNeeded:** NO 18, R4-Q1 4 (`#4.5`, `#4.6`, `#4.7`, `#5`).
- **Validator:** `RESULT PASS errors=0 warnings=0`.
- **SHA-256** `DOC-VALSTRAT_claims.csv`: `1726771a8f4098a499832ea697f4a3f9928e5b5e1bba7bc362b9cc5e442fe427`

## DOC-RELIANCE (`docs/harness/reliance_boundary_register.md`, 13 units; DeliverableID DEL-01-02)

- **Rows:** 51. Split rate 4 of 13 units (`#3` 14, `#4` 14, `#11` 8, `#13` 6).
- **SEE rows:** 14. Each Enforcement Matrix row `#4.n` points to `SEE:DOC:RELIANCE#3.n`.
- **Dispositions:**

  | Disposition | All rows | SEE rows excluded |
  |---|---|---|
  | IMPLEMENTED_DIFFERENTLY | 16 | 8 |
  | ALIGNED | 12 | 12 |
  | STALE_SPECIFICATION | 9 | 7 |
  | PARTIALLY_IMPLEMENTED | 9 | 6 |
  | DOCUMENTED_UNIMPLEMENTED | 2 | 1 |
  | STALE_VERIFICATION | 1 | 1 |
  | RETIRED_BY_RULING | 1 | 1 |
  | NOT_AUDITABLE | 1 | 1 |

- **Confidence:** LOW 5 (`#3.10`, `#4.10`, `#11.7`, `#11.8`, `#13.4`).
- **HumanDecisionNeeded:** R4-Q1 13, R4-Q5 6, R4-Q2 4, R4-Q3 4, R4-Q4 2, R4 2, NO 22.
- **Validator:** `RESULT PASS errors=0 warnings=0`.
- **SHA-256** `DOC-RELIANCE_claims.csv`: `4440b1d487566d21af4c0dd1319682a197e42e980b972b3ba79f77b1fc5306b8`

## RELEASE_PROCESS_NOT_RUN (for the manager's summary)

These tokens are negative evidence. They mean no record was found in the release AgentRuns records that were read: the `APP_V3_CODEX_HOST_REPLATFORM_20260912`, `APP_V3_USER_JOURNEYS_20260912` and `CODEX_MVP_PACKAGING_20260910` folders.

- **`DOC:VALSTRAT#4.7`: packaged Agent SDK proof.** It cannot pass on the A2 package.
- **`DOC:VALSTRAT#4.11`: network-policy proof for the v3.0.0 package.**
- **`DOC:VALSTRAT#7`: attestation.** Signing, notarization and publication did run: v3.0.0 was published on 2026-09-13.
- **Packaged S-6, S-8 and the renderer-disconnect repeat on the stapled App.** Rows `DOC:VALSTRAT#8` and `DOC:RELIANCE#11.1`. D-GOV-43 item 12 sets these as the post-build minimum. S-1..S-8 did pass from source.
- **`DOC:RELIANCE#3.2`: packaged offline Pi proof.**
- **`DOC:RELIANCE#8`: network-proof rerun for a release-significant review.**

## For the manager to resolve

1. **The Addendum 6 rule 3 edge case.** On the Codex path, several guarantees (containment, tool availability, shell posture) are met by the Codex sandbox and approvals. Repository code only selects that mechanism (`delegated.ts:324-329`).
   - I treated sandbox selection as not meeting the claim, so R4-Q1 is cited on RB-FILESYSTEM, RB-TOOL-SURFACE, RB-HOOKS, RB-SETTINGS and `#10`.
   - The other reading drops R4-Q1 on RB-FILESYSTEM and RB-TOOL-SURFACE. Please confirm which reading applies, or route the question to HELP_HUMAN.
2. **`DOC:RELIANCE#3.4` RB-PERMISSION is a possible AUTHORITY_CONFLICT.** The unamended K-PERM "deny-first" wording conflicts with D-GOV-43's user-chosen approval and sandbox policy. I recorded it as IMPLEMENTED_DIFFERENTLY with R4, not as a conflict.
3. **`DOC:RELIANCE#1`: REF-006 "currently MATCH" is false.** The PRD, CONTRACT and SPEC hashes all recompute NO for DEL-01-02. The DEL-01-02 `_REFERENCES` REGISTER row belongs to the PKG-01 ledger. This ledger does not add one.
4. **No `OTHER:` token** was used apart from the prescribed `OTHER:V3_ROLE_ADOPTION` (a `CAUSE2` on RB-SUBAGENT).
5. **Reading limits.** Neither PEC PRD nor Root export tooling was read, because both are outside the evidence roots. That limits `#11.7`, `#11.8` and `#12`.
