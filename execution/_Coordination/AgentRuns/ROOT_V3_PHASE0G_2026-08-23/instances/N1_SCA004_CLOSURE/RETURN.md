# N1 return — SCA-004 R6 closure

Status: `PASS — CLOSED_CONFIRMED_PROPAGATION_PENDING`

Role evidence: bounded ephemeral Agent 2; role not mechanically enforced;
governed evidence instruction-asserted. Delegation was not used.

## Result

R6-A, R6-B, and R6-C are transcribed into the SCA decision log. The live
scope-change pointer now identifies SCA-004 revision 1.3 as the accepted
current basis. Its bytes are the candidate fenced block with exactly the
three R6-B-authorized slot fills. The Gate-5 application record has one
slot-only backfill line containing the recorded content commit, PR head,
merge, and R4-A/R4-B/R5-A/R6-A references. The SCA handoff is
`CLOSED_CONFIRMED_PROPAGATION_PENDING`.

Under owner ruling R6-D, the completed-state validator's sole stale pointer
expectation was updated from the pre-pointer SHA to the approved final pointer
SHA. R6-D is transcribed verbatim. The regenerated committed validation JSON
is PASS 65/65 with zero failures.

No decomposition byte, other SCA file, Task Management row, Root handoff, or
closeout receipt was changed by this instance.

## Pre-write fence

- Branch: `codex/root-v3-phase0g-2026-08-23`.
- HEAD and `origin/main`: `d279bad6a5903678822ac8b3b85aec76f7a0cfed`.
- PR #633 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`
  is an ancestor of `origin/main`.
- Phase-0g steer SHA-256:
  `40f746f2c7534df4b2290349b0fb8a952a8d9153c287d8bf3b725669955b60ba`.
- R6 ruling-record SHA-256:
  `4e39bf6df909d63b910db3d953db720d2bceb2d27f26ce7454c93551f2a822de`.
- Every basis-gate SHA and condition matched, including Receipt 119 as the
  last Root receipt.
- Fresh pre-write `validate_gate5_applied.py`: PASS 65/65, zero failures.
  Temporary-output SHA-256 and committed
  `Gate_5_Applied_Validation.json` SHA-256 were both
  `f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1`.
- The governed checkout contained only the parent-created Phase-0g control
  tree before substantive writes.

## Final pointer and exact three-slot proof

Final `execution/_ScopeChange/_LATEST.md` SHA-256:
`4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.

Deterministic reconstruction extracted the fenced block from
`Gate_5_Pointer_Candidate.md`, applied exactly these three replacements, and
matched the live pointer byte-for-byte:

```diff
- application-append approval reference `TBD`
+ application-append approval reference `R4-A (record SHA-256 5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a)`
- confirmation reference `TBD`
+ confirmation reference `R6-A (record SHA-256 4e39bf6df909d63b910db3d953db720d2bceb2d27f26ce7454c93551f2a822de)`
- Git effect `TBD` (filled by a later recorded act, never inferred)
+ Git effect `PR #633 merge 6d4438d8d3a580b65d6d50ad497dadfe07f177f2 (content 4ad3fea7ef9e397852913c08e533e1846e264134, PR head 17d3bc2af666005676a517c0a37e5ebd7b3a6614)`
```

The candidate block contained four literal `TBD` tokens. The final pointer
contains one: the untouched application-evidence sentence. The reduction of
exactly three is the named-slot proof; every other byte matched the candidate
block.

## Backfill diffs

`Gate_5_Application_Record.md` changed one line only:

```diff
-Git effect: `TBD` — filled only by a later recorded Git act; never inferred.
+Git effect: content commit `4ad3fea7ef9e397852913c08e533e1846e264134`; PR head `17d3bc2af666005676a517c0a37e5ebd7b3a6614`; PR #633 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`. References: append approval R4-A and execution authorization R4-B (R4 record SHA-256 `5916aa599bf5953324636b8c5e0b0a5e2b9e6a793fd6dd9b1cac1c7e19e0755a`); re-authorization R5-A (R5 record SHA-256 `1f0a3358602fdfb4dff70607ad631130db55dcfd62d71a6fe7a3a13e18f0f42a`); confirmation R6-A (R6 record SHA-256 `4e39bf6df909d63b910db3d953db720d2bceb2d27f26ce7454c93551f2a822de`).
```

`Decision_Log.md` changed the top-level and Gate-5 application status to
`CONFIRMED_BY_OWNER_R6-A`, appended the three ruled rows, and appended R6-A,
R6-B, and R6-C verbatim. Its recorded backfill row contains only this chain:

```diff
+content commit `4ad3fea7ef9e397852913c08e533e1846e264134`, PR head `17d3bc2af666005676a517c0a37e5ebd7b3a6614`, merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`; references R4-A, R4-B, R5-A, and R6-A
```

Byte comparison against the published R6 record: PASS 3/3 verbatim sections.

## R6-D widening repair

Before the widening, the completed-state validator returned FAIL 64/65 solely
because it still expected the pre-R6-B pointer SHA
`b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.
The observed pointer was the correct owner-approved final SHA
`4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
This was a stale-expectation defect, not a state defect.

R6-D authorized exactly this validator diff:

```diff
-    Path("execution/_ScopeChange/_LATEST.md"): "b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1",
+    Path("execution/_ScopeChange/_LATEST.md"): "4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c",
```

No other validator line changed. Old/new identities:

| Artifact | Before SHA-256 | After SHA-256 |
|---|---|---|
| `validate_gate5_applied.py` | `281cfa29f66cf73dc3ab28c85029386e940f3109807862fbb18ae4f86036f63b` | `41e4c522a49861b11ce69c2e2577db2f1c031564c42c42894ac9da3d065df7ae` |
| `Gate_5_Applied_Validation.json` | `f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1` | `756b347e613eaa64b440952b74b27f14194a41075de912cc0bab18154e0f021c` |

Updated completed-state run: PASS 65/65, zero failures. The pointer check
records observed=expected=
`4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
R6-D verbatim comparison against amendment V2: PASS.

## Changed paths and final identities

| Path | Final SHA-256 |
|---|---|
| `execution/_ScopeChange/_LATEST.md` | `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c` |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Application_Record.md` | `0d66859b98fe40c7e2b30278ea43760b9502e0ee6ffa821d24814a368753d19a` |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Decision_Log.md` | `e123d3000bb087d3939d8e05582fbd75df7817cb685cc160944ec107e491e092` |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Handoff_State.md` | `d7a63c8607e7b0f1b329da909d6aacc29e71a2cde5a1ff9cedff915172429644` |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py` | `41e4c522a49861b11ce69c2e2577db2f1c031564c42c42894ac9da3d065df7ae` |
| `execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_5_Applied_Validation.json` | `756b347e613eaa64b440952b74b27f14194a41075de912cc0bab18154e0f021c` |

Instance evidence additionally changes this `RETURN.md` and sibling
`STATUS.json`. The parent-owned orchestration plan, graph, and sealed brief
were not modified.

## Protected state

The seven live decomposition identities remain, in order:

1. `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986`
2. `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`
3. `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417`
4. `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f`
5. `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f`
6. `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438`
7. `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c`

Other protected identities remained unchanged:

- `Gate_5_Rehearsal_Record.md`: `ea5d90e88ebc7528f758664bf354f815deb8c50b638276ead19a5f49f9f92532`.
- pointer candidate: `5918e7bff305bfc0a22c4a4fd172a2ad7bf013a217a778d6ca3797ce773dfabf`.
- post-Gate5 backcheck: `70ed91a848c762d9afb778423220c53408e1e4d2273a4a8aa7d5d81fd25359e9`.
- Task Management register: `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518`.
- Root handoff: `6fa6c9f5b19b81ea6fc0a1f5abfc693b821abc8b46d1890c6efe662f0aa28db1`.

`git diff --name-only origin/main` listed exactly the original four project
targets plus the two R6-D-widened validator/JSON targets;
`git diff --check` passed. Fresh self-review found zero actionable findings.

## Remaining work and blockers

Later, separately gated propagation remains:

1. PREPARATION INIT ×7.
2. DEL-02-06 `_CONTEXT.md` edit list.
3. Dependency extraction.
4. Estimates and schedule.
5. `WORK_GRAPH.json` / `DAG.md` re-derivation.
6. `AUDIT_DEP_CLOSURE`.

TM-ROOT-106 and TM-ROOT-122 remain unchanged G1 blockers. All ten DEL-02-06
bindings remain `HELD_UNAVAILABLE`; no hold is lifted. No propagation,
implementation, release, reliance, or merge authority is inferred.

Task Management candidate for later triage, with no register write: phase
validators that pin post-state hashes should either scope themselves to their
phase or accept expected state as recorded input, so a later authorized state
change does not strand them red.
