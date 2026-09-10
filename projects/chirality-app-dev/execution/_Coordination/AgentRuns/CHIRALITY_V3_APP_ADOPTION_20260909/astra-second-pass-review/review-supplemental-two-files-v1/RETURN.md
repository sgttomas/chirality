# Supplemental independent review — two final-custody files v1

Verdict: **PASS — no actionable findings.** Reviewer: `/root/astra_app_second_pass`, user-requested independent GPT-6-Astra high TASK reviewer; no delegation and no subject edits. This bounded supplement closes two files absent from the earlier source-freeze scope. It does not amend or silently expand the immutable V7 return.

Base: `c16812685831a1cae3d44bf478d08b033c605c3a` in `/private/tmp/chirality-v3-adoption-20260909`.

| Exact subject | SHA-256 |
|---|---|
| `projects/chirality-app-dev/execution/_Reconciliation/References/test_reconcile_authority_corpus.py` | `d554422d5a221964e3279073aae6fef301516e1ebac360329415bcea3cda5ab1` |
| `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-shell.test.tsx` | `ac8f3938a45995c6a647bc16af28ab799b08f20b36607acbe1a3cbd3937021d0` |

Both expected hashes matched before and after validation. I inspected 100% of both postimages and their complete base/new-file diffs; snapshots and diffs accompany this return.

The new Python test imports the actual adjacent reconciler, removes the newly required domain-engine method-resource hash from a temporary copy of the current corpus, and invokes real status/apply/audit/bump commands. It asserts failure, the explicit invalid-corpus diagnostic and byte-for-byte preservation of the malformed corpus for every command. Adjacent production validation checks the configured twelve-member corpus before live hashing, reference rewriting or minting a new version. This is meaningful regression coverage for rejecting an incomplete adopted authority snapshot, without modifying real corpus or deliverable files. It is one missing-member fixture, not exhaustive coverage of every malformed input. Python ran with `-B` to avoid bytecode writes.

The shell-file diff adds the router mock, continuation props/callback handling in child test doubles, reset state and one V3 continuation regression. It removes no existing assertion. The real WovenDialogueShell is exercised: Continue requests the recorded role in the URL; the resume request remains withheld until that URL transition is reflected; then the recorded session ID reaches the primary chat and replay closes. These expectations match the production continuation callback and role/root gating at the ChatPanel boundary. Existing composition, preserved controller identity, resize/replay behavior, stale catalog rejection, title race/redaction, shortcuts and settings assertions remain in place and pass.

The ChatPanel and replay lens are mocked in this composition suite. The new test therefore proves shell routing/handoff, not actual provider continuation, persisted transcript recovery or native qualification; those were reviewed and tested separately in V7. Its title also mentions legacy read-only behavior, but the new case does not itself contain a real legacy-negative assertion. That claim rests on the separately reviewed real operator-projection/replay-lens tests and production admission guard, not this mock. The inherited mocked Legacy window link assertion similarly verifies the compatibility URL supplied to a test double, not a visible production legacy launch link. These limits do not weaken the meaningful V3 shell assertion or replace prior product evidence.

Commands executed:

- From App root: `python3 -B execution/_Reconciliation/References/test_reconcile_authority_corpus.py` — PASS, one test containing four command subcases. Log: `python-test.log`.
- From frontend: `./node_modules/.bin/vitest run src/__tests__/components/woven-dialogue-shell.test.tsx --reporter=verbose` — PASS, 18 tests / one file, no skips. Log: `vitest.log`.
- Read-only SHA-256, Git base/new-file diff and adjacent contract inspection; no broad suite, product mutation, provider, credential or browser process.

This is a derivative review evidence package. Exact two-file custody is PASS; any subject change requires a new hash-bound backcheck. Both test processes ended normally. The Runtime reviewer subsequently reported the previously routed native-history seam closed under its separate Runtime V4 review, with unchanged response shape; that report neither modifies these two subjects nor establishes native supplier qualification.
