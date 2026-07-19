**VERDICT: COMMIT-SAFE**

# RETURN — T4 Adversarial Governed-Diff Verifier (fresh context, refutation-only)

- **RunID:** `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Brief:** `VERIFIER_BRIEF_T4.md` (this folder)
- **Date:** 2026-07-19
- **Baseline verified:** `git rev-parse HEAD` = `2a753e3fdeeeed5741a22398b2070be82f3b074d` (matches the brief's `2a753e3fd`).
- **Posture:** all evidence recomputed independently from the staged index (`git show :<path>`) and live tree; no author-supplied values trusted without recomputation. Read-only except this file.

## Claim 1 — Whole-diff claim: NOT REFUTED

- `git diff --cached --name-status` returns exactly 12 files: the two new decision packets (A), `_REGISTER.md` (M), DEL-07-04 `_STATUS.md` (M) + new run record (A), DEL-05-03 taxonomy artifact (A) + `_STATUS.md` (M) + new run record (A), and the four run-directory files `LAUNCH_BRIEF_PACKETS_T4.md`, `LAUNCH_BRIEF_ON_RULING_T4.md`, `RETURN_N8_PACKETS.md`, `RETURN_N9_ON_RULING.md` (all A). 882 insertions, 2 deletions.
- `git diff --cached --stat -- frontend/` (and `projects/chirality-app-dev/frontend/`) is empty: no code file changed.
- Untracked files: only `VERIFIER_BRIEF_T4.md` (the declared addition) plus this return.

## Claim 2 — Ruling fidelity: NOT REFUTED

Computed with python3 over the **staged blobs** (`git show :<path>`), marker spans = bytes strictly between `<!-- BEGIN OWNER RULING VERBATIM -->` / `<!-- END OWNER RULING VERBATIM -->` excluding the marker lines and the delimiter newlines:

- D-APP-66 span: 1332 bytes, SHA-256 `766058c8a5831859df867519ed3a19c3a5d91f00b16318401150322a4d134955`.
- D-APP-67 span: byte-identical to D-APP-66's (`s66 == s67 → True`), same length and hash.
- Block R in `LAUNCH_BRIEF_ON_RULING_T4.md` (content of the single ``` fence, lines 18–24): byte-identical to both spans, same hash.
- Each packet contains exactly one BEGIN/END marker pair (`grep -c "OWNER RULING VERBATIM"` = 2 per packet).
- The recorded hash and byte count inside both packets match the recomputed values.
- D-APP-66 Status line: `RULED — Option C (status quo), owner ruling 2026-07-19 …`; the transcribed ruling's Question 1 owner selection is "C: Status quo"; the disposition paragraph authorizes no code and keeps content-change voiding a governance checklist concern. D-APP-67 Status line: `RULED — Option B (taxonomy document only) …`; Question 2 owner selection is "B: Taxonomy doc only"; the disposition ratifies the committed-file taxonomy + verifier-quoting rule and states the runtime helper stays API-key-specific with no `[REDACTED_SECRET]` token. Selections and dispositions are mutually consistent.

## Claim 3 — Register discipline: NOT REFUTED (one wording observation, non-blocking)

- `git diff --cached -U0 -- …/_REGISTER.md` shows a single hunk `@@ -80,0 +81,2 @@`: a pure 2-line insertion of the D-APP-66 and D-APP-67 rows after the D-APP-65 row. Every other row/byte is identical to HEAD (no other hunks exist).
- Both new rows have 6 columns (awk field count 8 with leading/trailing empties, matching the header `| ID | Decision | Blocks | State | Packet | Ruling record |`).
- State cells read `RULED (Option C status quo)` / `RULED (Option B taxonomy document only)`; Ruling-record cells carry the packet pointers and the canonical hash.
- **Observation (not a defect):** against HEAD the rows are net-new additions, not modifications — the AWAITING_RULING state existed only in the uncommitted T4 working sequence (N8 authored the rows AWAITING_RULING per `RETURN_N8_PACKETS.md`; N9 flipped them per `RETURN_N9_ON_RULING.md`; both landed in this one staged diff). The claim's substantive content — only these two rows differ from HEAD, shape preserved, all else byte-identical — holds exactly.

## Claim 4 — Status-surface rules: NOT REFUTED

For each of DEL-07-04 and DEL-05-03 `_STATUS.md`, the staged diff is exactly two lines:

- One removal: the HEAD line-10 deferred item (verified at HEAD line 10 by `sed -n '10p'`), each citing "D-APP-53 packet §3 Option C" — the exact D-APP-53-Option-C gated item named in the claim. The Remaining section is otherwise empty in both files at HEAD, so "every other Remaining item byte-intact" holds vacuously and exactly.
- One addition: a single dated `2026-07-19` History line citing D-APP-66 (Option C, no code) / D-APP-67 (Option B, taxonomy ratified) respectively, ending "No state or lifecycle change."
- Unchanged in both: `Current State: IN_PROGRESS`, `Last Updated: 2026-07-12`, `Checking Approval SHA: 8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, all lifecycle history.

## Claim 5 — Taxonomy grounding: NOT REFUTED

Spot-checked 8 citations (more than the required 4) against the live `projects/chirality-app-dev/frontend/scripts/scan-secret-evidence.mjs`:

1. Line 50: `const ANTHROPIC_KEY_PATTERN = /sk-ant-[A-Za-z0-9._=/-]{8,}/g` — matches Rule 1 bullet 1; scan loop confirmed at lines 320–334 with fixture-vs-blocked disposition.
2. Line 51: `URL_CREDENTIAL_PATTERN = /\bhttps?:\/\/[^\s/@:]+:[^\s/@]+@[^\s/]+/g` — matches Rule 1 bullet 2; scan loop at 336–350.
3. Lines 52–65: `FIXTURE_MARKERS` — exactly the 12 markers quoted (`ambient`…`ui-key`), in order.
4. Lines 141–148: `isFixtureToken` — marker-in-token OR path containing `__tests__`/`/test/`/`/tests/`, as Rule 1 states.
5. Lines 180–204: `collectEnvironmentSecrets` — `ANTHROPIC_API_KEY` + `CHIRALITY_ANTHROPIC_API_KEY`; `usable = present && value.length >= 8` at line 187; raw + `url_encoded` variant expansion at 194–200.
6. Lines 296–318: env-value hits pushed with `disposition: 'blocked'`, `reason: 'actual_environment_secret_value'`, and no `isFixtureToken` call in that loop — Rule 2's "no fixture-marker escape" is accurate.
7. Lines 166–178: `redactedFinding` records `valueSha256`/`valueLength` only, never the raw value — hash-only persistence confirmed. Fail path: `status: 'fail'` on any blocked finding (line 403), `process.exitCode = 1` at 431–433.
8. Rule 4 runtime citations: `readConfiguredApiKeyVariants` at `frontend/src/lib/harness/run-logger.ts:64–77` draws from exactly three API-key sources (`getUiApiKey()`, `ANTHROPIC_API_KEY`, `CHIRALITY_ANTHROPIC_API_KEY`); `[REDACTED_API_KEY]` replacement at line 90; `CHIRALITY_PEC_AGENT_PASSWORD` read only inside `pec-bridge-client.ts` login/envelope paths (lines 19, 184, 296). `grep -rn "REDACTED_SECRET" frontend/src/` in the app project returns nothing — Rule 4's "no `[REDACTED_SECRET]` token" and "helper remains API-key-specific" claims match the code; no rule claims runtime behavior that does not exist. `frontend/package.json:30` is `"proof:secret-scan": "node ./scripts/scan-secret-evidence.mjs"` as cited; `candidateFiles` begins at scanner line 242.

Secret-shape check of the artifact: the only `sk-ant-` occurrences are the regex pattern text itself (`sk-ant-[…]`), whose next character `[` is outside the pattern's character class — not a matchable continuation; no URL-embedded credential shape; the hex strings present are SHA-256 hashes (ruling hash, approval SHA), not secrets. The artifact's standing paragraph explicitly disclaims issuance/release-readiness/professional claims and states lifecycle is unchanged.

## Claim 6 — Consistency with the ruling: NOT REFUTED

- The staged diff contains zero code files, so no Option A of either packet is implemented: no `APPROVAL_SHA_STALE` in any source file (the token appears only as design-reference prose inside the packets/returns), no run-logger change, no env-var registry.
- `TASK_RUN_2026-07-19_DAPP66_ruling_closure.md` has an explicit "## No code landed" section: "No runtime source file was touched; the Option A design remains in the packet as reference only." The DEL-05-03 run record carries the equivalent section ("run-logger.ts unchanged, no [REDACTED_SECRET] token introduced").

## Claim 7 — Hygiene: NOT REFUTED

- Staged diff scans: `sk-ant-[A-Za-z0-9._=/-]{8,}` — zero matches on added lines (the pattern-as-text in the taxonomy does not match itself); URL-credential shape — zero matches; private-key blocks / AKIA / ghp_ / xox[baprs]- — zero matches.
- `python3 tools/practitioner_harness/harness.py self-check` exits 0 with summary exactly at the pinned baseline: **INFO=15, NOT_APPLICABLE=2, REVIEW=33, WARN=6**.

## Findings summary

No claim refuted. One non-blocking observation recorded under Claim 3: the register rows (and the packets' AWAITING_RULING phase generally) never existed at any commit — N8's authoring and N9's on-ruling writes land together in this single staged diff, so the diff shows net additions where the claims narrate a flip. All substantive invariants (row isolation, byte-identity of everything else, marker-span hashing, status-surface discipline, no-code posture, hygiene baseline) verified independently and hold.

**VERDICT: COMMIT-SAFE**
