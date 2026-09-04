# REVIEW — D2_REVIEWER — APPDEV_V3_NODE_D_2026-09-03 (DEL-05-01-V3-01)

**FINDINGS — 0 blocking / 1 major / 2 minor** (plus 4 notes, none actionable on their own)

Reviewer: fresh read-only `software-code-review` instance (Claude Fable 5.1, `claude-fable-5-1`), not the implementer's context. Scope reviewed: 100% of `git diff 0c683fb1657706316272951e4c3a0f7781b46009 3b6b4758bca7cd0e4ac84f9685052a0548c4ca2e` (25 files, +2037/−78), read in a detached scratch worktree at `3b6b4758b`; no file modified, no branch changed, no commit made. Paths below are relative to `projects/chirality-app-dev/` unless prefixed with `runtime/` or `tools/`.

Basis context read: `AGENTS.md` (independent-review path), `loop/WORKPLAN_2026-09-03_app_dev_loop.md` (fences, evidence contract), DEL-05-01 `_STATUS.md` `## Remaining` at `0c683fb16`, `ScopeOfWork.md` (OUT-001, R003/R004/R010/R015/R016, CLM-012), decomposition row L322, D-APP-41 packet + ruling, `docs/SPEC.md` §8.1/§8.2/§25.4, the full AgentRuns record, `runtime/packages/contracts/src/harness/errors.ts` and `ISessionManager` in `types.ts`.

---

## Findings (most severe first)

### F1 — MAJOR — Accepted requirement R010 (flat-record removal) is violated and its verification test replaced without the conflict being surfaced as an owner decision

**Where.** `frontend/src/lib/harness/session-manager.ts:480-555` (`resolveSessionRecord`; the basis `rm(legacyFilePath, { force: true })` at basis lines 271-273 is removed with no replacement); `frontend/src/__tests__/lib/session-manager.test.ts:122, 274, 300, 324` (four `access(...).rejects` assertions became byte-identity assertions); records `AgentRuns/.../STEP0_DISCOVERY.md` "Delta 1", `RETURN.md` "Stale-map / instruction deltas", `_run_records/TASK_RUN_2026-09-03_V3-01_v2_lazy_access.md` latitude item 1.

**What.** The accepted Scope of Work (re-pinned 2026-09-03 to the applied v3_2 decomposition at `d6f6cadb`) carries, as MUSTs, not only R003/R004 (cited by the implementer) but also:

- **R010**: "If both canonical folder and legacy flat records exist for the same `sessionId`, resolution MUST prefer defined canonical values, preserve legacy-only fields, write the merged canonical `session.json`, **and remove the flat record**." (source: D-APP-41; SPEC §8.1)
- **CLM-012 verification row** for R003/R004/R005/R010/R016: "duplicate fixture tests proving merge precedence, legacy-only field preservation, **and flat-file removal**."
- **D-APP-41 ruling** (owner-ratified 2026-06-21, Option D "eager legacy conversion"): "resolve the duplicate shape by migrating, archiving, or removing the flat record according to the migration implementation"; packet Option D text: "remove or archive the flat JSON record".

The change retains the flat file indefinitely and deletes the only tests that proved removal. Neither R010 nor the CLM-012 row is cited anywhere in STEP0, RETURN, the TASK run record, or `BYTE_IDENTITY_PROOF.md`. The implementer classified the choice as a stale-map delta ("live tree wins") plus D-APP-60/64 agent latitude. That classification is wrong in kind: this is not a map that disagrees with the tree — the basis tree *removed* the file — it is two sets of **accepted authority** disagreeing (R010 + CLM-012 + D-APP-41 versus seated row L322 "non-destructive" + SPEC §25.4 "no ... destructive source move" + the sealed brief's explicit "never ... deletes the legacy file"). Under the loop's own doctrine such a conflict is a human-review item (the harness self-check labels exactly this pattern "sources conflict — human review required"), and a change to on-disk product behaviour of every user's session store is a material, owner-shaped fork, not ordinary latitude.

**Why it matters.** (a) A closeout that records DEL-05-01-V3-01 as landed "with review PASS" would silently leave R010 unsatisfied and its verification removed; a later G5 fan-in or concordance pass will flag it. (b) The owner explicitly ratified Option D after a mis-attribution incident recorded in the ruling itself; departing from it without an owner-visible decision repeats the pattern that ruling corrects. (c) The direction chosen is the *reversible* one (bytes retained), so this does not need to block the code.

**Exact remediation (record-only; no code change required by this finding).**
1. In `STEP0_DISCOVERY.md` Delta 1, `RETURN.md` (stale-map section and residual risks), and the TASK run record latitude item 1: quote R010 and the CLM-012 row verbatim; state plainly that **R010 is not satisfied by this tranche and its removal-proving assertions were replaced**; re-label the disposition from "stale-map delta / agent latitude" to **`OWNER_DECISION_REQUIRED`** with the two options stated — (i) ratify retention (amend D-APP-41 / SCA on R010, R004 wording and CLM-012 row; S-4 backup concern becomes moot), or (ii) reinstate removal after successful materialization (bounded code delta: re-add `rm(legacyFilePath, { force: true })` after `writeCanonicalSession` in both `ok` branches of `resolveSessionRecord`, revert the four assertions, drop the retention-specific evaluator assertions).
2. At fan-in, HELP_HUMAN presents that decision to the owner before Receipt 208 / `_STATUS.md` History claims the item closed; the `_STATUS.md` History line must not state R010 satisfied.
3. `BYTE_IDENTITY_PROOF.md` §1 "Epistemic status" already says the SoW governs on disagreement — add one line naming the R010 disagreement so the evidence packet is self-consistent.

### F2 — MINOR — With retention, the flat file remains a standing *read* input on every access (latent field-resurrection), and the record mischaracterizes this

**Where.** `frontend/src/lib/harness/session-manager.ts:522-541` (canonical-ok branch merges legacy on every call and re-materializes whenever `stableSerialize(merged) !== stableSerialize(canonical.record)`); `RETURN.md` / STEP0 wording "the flat file is an untouched source, not a written shape".

**What.** Because the flat file is never consumed/marked, every `getById`/`resume`/`save`/`list`/`delete` re-reads it and merges it under canonical. Consequences: (a) any field later removed from canonical by a writer reappears from legacy on the next read and is written back (resurrection); (b) an external edit to the flat file after materialization changes the live record; (c) R004's "MUST NOT keep flat records as a standing parallel storage shape" is only honoured on the write side — the flat record is a standing parallel *read* shape. No current caller clears fields (`turn-engine.ts:375`, `mcp/coordination-tools.ts:52/203/220/290` all set values), so the hazard is latent today.

**Exact remediation.** Correct the record wording now (part of F1's amendment). Code follow-up, owner-dependent: if retention is ratified, mark consumption in canonical (e.g., `legacySource: { sha256, materializedAt }`) and merge legacy only when absent/mismatched; if removal is reinstated, this finding closes itself. Add a regression test either way: materialize, delete a legacy-only field from canonical, read again, assert it does not return.

### F3 — MINOR — `listWithDiagnostics` now aborts the whole listing on a single candidate's non-record I/O failure (basis skipped it)

**Where.** `frontend/src/lib/harness/session-manager.ts:645-657` — the `catch` only swallows `HarnessError` with `type === 'SESSION_NOT_FOUND'` (unsafe ids) and rethrows everything else. Basis `list` (`0c683fb16` lines 338-346) swallowed all errors per candidate.

**What.** A materialization write failure for one legacy-only candidate — read-only session root (`EROFS`/`EACCES`), or a stray *file* occupying the `{sessionRoot}/{id}` path (`ENOTDIR`/`EEXIST` from `mkdir`) — now rejects the entire list with a raw Node error, which `asHarnessError` maps to `SDK_FAILURE` 500. Basis still returned every other session. This is the "list must not crash on a sibling" property the brief names, applied to I/O rather than content; it is disclosed in `RETURN.md` residual risks but it is a regression of "preserve list behavior", not a neutral change.

**Exact remediation.** Per candidate, catch non-`HarnessError` errors from `resolveSessionRecord`: if the record content was readable, still push the session (unmaterialized) and record a diagnostic; otherwise push a failure entry (reason `record could not be materialized (<code>)`) and continue. Test: seed `sess_x.json` plus an empty regular file named `sess_x`; assert `list` returns the other fixtures and reports `sess_x`.

### N1 — NOTE — Read-permission/IO errors are typed `malformed`

`session-manager.ts:238-249`: `EACCES`/`EISDIR`/`EIO` become `kind: 'malformed'` (reason text does carry the code), and `delete` then refuses with 422. Observable and non-destructive, so acceptable for this item; fold into the future error-type proposal (N2).

### N2 — NOTE — `SessionRecordAccessError` = `SESSION_NOT_FOUND` + HTTP 422 (finding 4)

`session-manager.ts:92-119`. `HarnessErrorType` is a closed Root-owned union (`runtime/packages/contracts/src/harness/errors.ts`); `ISessionManager` is unchanged (`git diff ... -- runtime/` is empty); new exports are additive and `list()`'s signature is unchanged. `errorResponse` (`lib/harness/http.ts:29-41`) serializes `details`, so `details.kind/shape/filePath/reason` are on the wire. Exposure is limited: the session HTTP routes (`app/api/harness/session/[id]/route.ts:18,31`, `list/route.ts:13`) call `getDaemonHarnessPort()`, not `FileSessionManager`; the new error reaches consumers only on in-process paths (`turn-engine.ts:169 resume`, `mcp/coordination-tools.ts:36,277 getById`). Where it does reach the UI, `lib/harness/error-display.ts:37` renders every `SESSION_NOT_FOUND` as "Session Not Found — The active harness session no longer exists. Start a new session", which is wrong for a record that exists but is unreadable. Verdict: acceptable and honestly disclosed for this item; a `SESSION_RECORD_UNREADABLE` (or similar) `HarnessErrorType` should be routed to Root with the V3-02 schema work, and `error-display` should consult `details.kind` in the interim (outside this locus).

### N3 — NOTE — Other intended behaviour changes, disclosed and judged correct

- `list(projectA)` no longer materializes canonical folders for records bound to project B (`materializeOnlyFor`, lines 491-505, 648-650). Basis wrote into other projects' folders during list — the new behaviour is an improvement.
- Corrupt canonical + readable legacy now fails closed (422) on `getById`/`save`/`delete` (lines 518-520); basis silently rebuilt canonical from legacy and deleted legacy. Correct under "non-destructive" and disclosed (latitude 3).
- `delete` of an unreadable record now refuses; basis returned 404 for a malformed record and left it. Disclosed; consistent with the open-first contract.
- Malformed records moved from silent 404 to typed 422 — the item's objective.

### N4 — NOTE — Evidence contract

`Evidence/V3-01_v2_lazy_access_2026-09-03/` carries fixture bytes, sorted SHA-256 inventory (independently recomputed: match), focused-run stdout and JSON (35/35), environment, versions, cwd, exit status, cleanup proof, and a bounded rerun method; `CHECKS.json` records exact commands/cwd/exit for every registered check. Full `npm test`/`typecheck` stdout are summarized rather than preserved as bytes — adequate because the item's own claim is carried by the focused evaluator. `MANIFEST.sha256`, `HANDOFF_STATE.md`, `_STATUS.md` and Receipt 208 are deferred to closeout per the brief; F1 must be settled before those are written.

---

## Finding-3 recommendation (semantic delta: legacy flat file retained vs. deleted on first touch)

**Recommendation: accept with an owner-visible note — do not accept as conforming; do not require a code change at this stage.**

Reasoning:

1. **Does the seated contract require retention, or only non-destructive access?** The seated item (`_STATUS.md` `## Remaining`, V3-01) requires "lazy non-destructive access ... (no destructive bulk rewrite)" and AT-035 "representative v2 data opens without destructive rewrite"; row L322 says "lazy non-destructive access to and migration of legacy project-local session records while preserving list, resume, and delete behavior"; SPEC §25.4 says "read lazily and migrated non-destructively on access. No bulk rewrite or **destructive source move** is permitted." Deleting the source after copying it is a destructive source move, so the plain reading of §25.4 and the seated row does require source retention, and the sealed brief said so explicitly ("first-touch access never rewrites, truncates, or deletes the legacy file"). On that authority the implementation conforms. Note, however, that §25.4's subject is the *central* (daemon) store; applying it to the project-local canonical folder is an extension the seated row makes, not something §25.4 itself states.
2. **Is retention a product-behaviour change the owner must rule on?** Yes. It reverses an owner-ratified ruling (D-APP-41 Option D, whose packet text is "remove or archive the flat JSON record"), violates the accepted SoW MUST R010 verbatim, and removes the CLM-012 "flat-file removal" verification. D-APP-41's ruling wording ("migrating, archiving, or removing ... according to the migration implementation") is loose enough that retention is not a *literal* breach of the ruling, but R010 is unambiguous. Two accepted instruments disagree; only the owner can resolve which one is amended.
3. **Does retention create read ambiguity?** Precedence is deterministic — canonical wins field-by-field, legacy-only fields preserved, corrupt canonical fails closed and is never overwritten from legacy (`session-manager.ts:518-541`, proven by tests at `session-manager-v2-legacy-access.test.ts:420-487`). What retention does create is the standing-read-shape / resurrection hazard in F2, which the record understates.
4. **Why not require reinstating removal now?** The retained-bytes direction is the reversible one and is what the parent's sealed brief instructed; a reviewer requiring the opposite would substitute its judgment for the owner's on a fork that belongs to the owner. The correct outcome is that the fork is *visible* at fan-in with both bounded options (F1 remediation) and the code lands only after the owner picks.

Net: conforming to the seated item and sealed brief; non-conforming to R010/CLM-012/D-APP-41 as written; the return may proceed to fan-in only with F1's record amendment so the owner sees the fork.

---

## Check table (reviewer reruns, scratch worktree at `3b6b4758b`, macOS darwin 25.6.0, Node v24.18.0, npm 11.16.0)

Prerequisite (per the evidence packet's rerun method): `cd runtime && npm ci && npm run build` (exit 0; emits ignored `dist/`) then `cd projects/chirality-app-dev/frontend && npm ci` (exit 0). Before the runtime build, `npm run typecheck` fails with `TS2307 Cannot find module '@chirality/runtime-contracts/...'` and `npm test` reports 71 failed files — the documented prerequisite class, not a defect in this change.

| Check | cwd | Command | Reviewer result | Implementer's CHECKS.json |
|---|---|---|---|---|
| Typecheck | `frontend` | `npm run typecheck` | exit 0, no errors (app + electron) | PASS |
| Full Vitest | `frontend` | `npm test` | exit 0 — Test Files 156 passed, 1 skipped (157); Tests 1300 passed, 4 skipped (1304) | PASS, same totals |
| Focused | `frontend` | `npx vitest run src/__tests__/lib/session-manager.test.ts src/__tests__/lib/session-manager-v2-legacy-access.test.ts` | exit 0 — 2 files, 35/35 passed | PASS 35/35 |
| Whitespace | repo root | `git diff --check 0c683fb16 3b6b4758b` | exit 0, clean | PASS |
| Write scope | repo root | `python3 tools/software_workflow/validate_change_scope.py . --base 0c683fb16… --head 3b6b4758b… --allowed <5 declared roots>` | `PASS`, 0 violations, 25 paths (= diff) | PASS; `WRITE_SCOPE_VALIDATION.json` matches |
| Harness self-check | repo root | `python3 tools/practitioner_harness/harness.py self-check` | exit 0; INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=43 — all pre-existing, none in App paths | PASS, identical counts |
| Fixture inventory | fixture dir | `find . -type f \| sed … \| LC_ALL=C sort \| xargs shasum -a 256 \| diff - FIXTURE_INVENTORY.sha256` | identical (9 files) | — |
| Scratch tree | scratch root | `git status --porcelain` after all builds/tests | clean | — |
| Premerge (not rerun) | — | `PREMERGE_RESULTS.json` read | `next dev` READY; `harness:validate:premerge` 8/8 fail, every route HTTP 503 `ENGINE_UNAVAILABLE "Chirality runtime daemon client is not configured"` (`lib/runtime-client/daemon-harness-port.ts:113`); the session routes call the daemon port, not `FileSessionManager`, so this change cannot be the cause. Class matches receipts precedent `LOOP_RECEIPTS.md:5183,5313` (absent runtime-daemon bindings → PR-CI-owed, no inferred pass). | FAIL_DEFERRED_TO_PR_CI — truthfully classed |

Dimension coverage:

| # | Dimension | Result |
|---|---|---|
| 1 | Correctness / regressions | Typed reader, `inspect`, `listWithDiagnostics`, canonical precedence, idempotent materialization (`stableSerialize`, tested at `…legacy-access.test.ts:264-275, 333-343, 454-459`), corrupt-canonical fail-closed, unsafe-id guard, 404 for absent, delete contract (open first; removes both shapes; siblings byte-identical) all verified by reading and by test rerun. Callers traced: `turn-engine.ts:169/375`, `mcp/coordination-tools.ts:36/52/203/220/277/290`, `app/api/working-root/validate/route.ts:3` (`assertProjectRootAccessible` only), `runtime.ts:158` wiring, `__tests__/api/harness/fake-daemon-harness-port.ts:11`. Regressions: F3 (list aborts on sibling I/O failure); F2 latent. |
| 2 | Scope compliance | No backup/rollback, no bulk migration, no `runtime/**`, no `events.jsonl`/`HarnessEvent` change, no dependency added, no layout change. All 25 paths inside the declared locus. Scope exceedance is F1's authority conflict, not a file-locus breach. |
| 3 | Semantic delta | See recommendation section. |
| 4 | Contract stability | `ISessionManager` unchanged; additive exports only; N2 on 422/`SESSION_NOT_FOUND`. |
| 5 | Tests / fixtures | 23 new tests genuinely assert `Buffer.equals` before/after `inspect`/`list`/`resume`/`getById`/`save`/`delete` for every legacy flat file plus `events.jsonl`, and file-set equality (`listFilesRecursively`) proving the only new path is the accessed session's `session.json`. Malformed fixture is a real truncation; unsupported-version fixture declares `chirality.session/v9`; missing-fields fixture lacks `projectRoot`/`createdAt`. Fixtures use placeholder roots and contain no secrets or user paths (asserted at `…legacy-access.test.ts:155-168`). The four assertion changes in `session-manager.test.ts` are the ones F1 governs; no other test weakened; the pre-existing delete test (`session-manager.test.ts:333-354`) is untouched. |
| 6 | Evidence contract | Satisfied for the item's claim (N4); `WRITE_SCOPE_VALIDATION.json` independently reproduced; premerge failure truthfully classed. |
| 7 | Incident | Stray `PREMERGE_RESULTS.json` under Root `execution/_Coordination/AgentRuns/` disclosed in `RETURN.md` ("Incident"). Verified absent: `git ls-tree -r 3b6b4758b -- execution/_Coordination/AgentRuns` has no `NODE_D` entry; implementer worktree `wt-nodeD` and the parent worktree both report empty `git status --porcelain --untracked-files=all`. |

---

## Residual risk and fan-in validity

- **Residual risk (code):** F3 list-abort on sibling I/O failure; F2 resurrection hazard is latent until a writer clears a field; N1/N2 error typing rides on a Root-owned closed union and the UI copy for `SESSION_NOT_FOUND` will mislabel unreadable records on in-process paths. Retained flat files accumulate with no cleanup path (S-4 unseated) — by design, but only if the owner ratifies retention.
- **Residual risk (process):** Receipt 208, `_STATUS.md`, `HANDOFF_STATE.md`, and `MANIFEST.sha256` are not yet written; premerge is PR-CI-owed; A1 re-stage rule is triggered and declared.
- **Validity for fan-in:** The return is **valid for manager fan-in as a frozen implementation with findings**, not as a PASS. The registered deterministic gates reproduce exactly. The single MAJOR is a record/decision-routing defect, remediable inside the declared locus without touching product source: amend the three record surfaces per F1, mark the retention fork `OWNER_DECISION_REQUIRED`, and re-freeze; a code change is owed only if the owner elects removal. F3 is a small bounded code fix that can ride the same re-freeze. This review does not perform lifecycle acceptance.
