# Verifier verdict 01 — MODE=VERIFY, DEL-08-06 candidate (K2, provisional D-PEC-103)

- **Reviewer:** a fresh read-only `pec-reviewer` TASK (`claude-opus-5-5`, high), dispatched by WORKING_ITEMS. It authored nothing in the packet.
- **Reviewed:** candidate `31d0aa6e9d77e345b1c7178acde16fbb099d510500130e58aafdbdd60212d036` at branch commit `3ed3b31aa`.
- **Transcription:** the report below is the reviewer's hand-back message as delivered, with the harness's indentation removed. The manager's dispositions follow it.

## Report

**Verdict: FAILED.** There is one blocking finding: the failure behaviour contradicts the output pass-through rule, and that is part of the shape the K3 profile act would copy. It is a small repair. Everything else passes or has only non-blocking notes. After the repair, a targeted backcheck should give PASS WITH NOTES.

I did not modify anything. The worktree is clean at `3ed3b31aa` (`origin/main` was `ce99bc256` after fetch). The scratch directory I created with `mktemp -d` has been deleted.

**Candidate reviewed**
- Path: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-k2-sows-prep/projects/pec/execution/_Coordination/PEC_FIRST_SOWS_K2_PREP_2026-09-26/candidates/projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/ScopeOfWork.md`
- SHA-256 `31d0aa6e9d77e345b1c7178acde16fbb099d510500130e58aafdbdd60212d036` (recomputed, matches). 249 lines, no tabs, no trailing whitespace, ends with a newline.
- Reliance-hold preflight (`candidate-validation`): `ALLOW`.

## 1. Checks from checks.md (MODE=VERIFY, INIT discipline)

All tools ran on a `git archive HEAD` export with the candidate copied into its production path, using Python 3.13.7 with `PYTHONDONTWRITEBYTECODE=1`.

- **Item 1 — PASS.** The standard (`docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` §7) says new deliverables use `SOW_V1`. The validator resolves the folder as `SOW_V1`.
- **Item 3 — PASS.** `_STATUS.md` hash is `73e21846…2511` and reads `OPEN` at `125cfacc1`, at HEAD and at `origin/main`. The candidate is not in the production folder.
- **Item 4 — PASS.** `validate_scope_of_work.py` gives `PASS format=SOW_V1`, exit 0.
- **Item 8 — PASS.** All 17 matrix rows cite `SOW-099 OBJ-001`.
- **Item 9 — PASS.** AC-001..016 each map to VER-001..016. AC-017 is `HUMAN_REVIEW`.
- **Item 13 — PASS.** `derive_review_checklist.py` exits 0 and produces 17 items, in source order, with exact text. It is bound to the `31d0aa6e…` hash.
- **Item 16** — The findings below are tagged schema, content or substrate.
- **Item 18 — PASS.**
  - Two derivations are byte-identical (`d9eae773…4c21`).
  - An invalid matrix reference (`VER-099`) fails with exit 1 and writes no output.
  - A dual-format (AMBIGUOUS) folder fails with exit 1 and writes no output.
- **Item 19 — PASS.** Every local-ID token in the candidate is defined in the candidate. No upstream local IDs are cited. `check_cited_ids.py` reports `RESULT PASS 0/0`.
- **Item 20 — PASS.** There is one AC per row, and each row has a single VER.
- **Item 21 — PASS, with note NB-2.** `check_boundary_owner_resolution.py --show-not-checkable` exits 0: 1 requirement checked (REQ-014), 0 not checkable, 0 without a cited claim, no failures.
  - **REQ-014 → CLM-011, by hand.** All 19 excluded acts resolve to named owners. I checked each owner against the `ScopeLedger.csv` `DeliverableIDs` column at `125cfacc1`:
    - socket and access-class logic: DEL-08-01 (SOW-040/003)
    - schema: DEL-08-02 (042)
    - format and budgets: DEL-08-03 (043/098)
    - latency: DEL-08-04 (041)
    - SSE: DEL-08-05 (044)
    - orientation: DEL-04-01 (004)
    - delta: DEL-04-02 (005)
    - citation, stamp and envelope: DEL-04-03 (006/007/097)
    - scope: DEL-04-04 (008)
    - limitations: DEL-04-05 (009)
    - gate: DEL-05-01 (022/023)
    - slate: DEL-05-02 (024)
    - presence, scan, correlation, TTL and overlap: DEL-06-01/02/03/05/06 (026/027/028/030+032/031)
    - ingest guard: DEL-01-03 (056)
    - locality and dependencies: DEL-01-05 (052/053)
    - no-ruling-write: DEL-10-03 (025)
    - kill test: DEL-10-02 (055)
    - uptake: DEL-10-12 (060)
    - reliance gate: DEL-10-13 (100)
  - **REQ-015 → CLM-012 and CLM-013, by hand.**
    - Token mechanism → §16.6 owner ruling (quoted from the PRD).
    - Tier-0 entry → tier-0 owner (§B6 "The tier-0 owner rules it").
    - Enabling → the consumer (PEC-API-007).
    - Schema field → the §B8 source packet (quoted).
    - Reliance advertisement → "human release act". This owner is asserted but no source for it is quoted (NB-2).
  - The tool silently skips REQ-015 because it contains no `DEL-` token (NOTE N-6).
- Items 2, 5–7, 10–12, 14, 17 and 22 are `NOT_APPLICABLE` (CONVERT or REVISE only). Item 15 is not applicable because no HTML was requested.

## 2. Prep verifiers (rerun)

- `verify_k2_quotes.py --observation 125cfacc1 --only DEL-08-06`: `RESULT PASS 61/61`, exit 0. That is 59 quotes plus the forbidden-phrase and observation-commit checks. It found 0 DEP rows citing the contract.
- `verify_k2_state_claims.py --only DEL-08-06`: `RESULT PASS 147/147`, exit 0.
- `check_cited_ids.py --commit 125cfacc1`: `RESULT PASS 0/0`, exit 0.
- `scan_old_s2_text.py --prior ce934ac33 --current 125cfacc1`: `RESULT PASS stale=0 current=43`, exit 0. The 43 CURRENT lines are the OBJ-001 quote plus shared boilerplate.

**Are the verifiers sound?** Yes, within limits I closed by hand.
- Both the quote and claim verifiers are two-sided. Every quote entry carries `commit: 125cfacc1` and is read with `git show`.
- The DEP check's `execution/...` path format matches the corpus `EvidenceFile` convention.
- Limits (substrate notes, N-7), and what I did about each:
  - `verify_k2_quotes.py` L88–98 checks only a substring of the whole file, not the locus, and does not check that every quotation is registered. I listed every quoted span and blockquote in the candidate: all are registered. I checked every attributed locus (PEC-API-007/006, ORI-007, K-03/01/11, §8, §12, §16.6, C12, OI-006, DL-21, §B6/§B8, pec.yaml L81/L104, K3, D-PEC-101 finding 3, D-PEC-90, the CP1 register row, IA §13.1).
  - `verify_k2_state_claims.py` L112 anchors `candidate_text` only loosely. Some claims are weak proxies (S32 "six rows" via not-contains `-007`; S93; S136–S138 "two tools"), and S30 duplicates S29. I confirmed each directly:
    - `Dependencies.csv` has exactly 6 rows.
    - The DEL-08-01 contract has no `agent` class (REQ-003 L107).
    - `pec.yaml` declares exactly two tools and no query tool.
    - All hash suffixes match.
  - `scan_old_s2_text.py` looks only at quoted spans. My own 10-word n-gram scan against the prior S2 contracts found only boilerplate phrasing (AX-012/AX-013 style, the VER-013 wording), with no quoted old S2 content.

## 3. Semantics

**Confirmed:**
- Pin `189f205ff` and `125cfacc1` have identical bytes for SOFTWARE_DECOMP (`9374c21f…8eb1`), Deliverables (`94ee5d18…9805`), ScopeLedger (`1d24a4b8…916e`), ContextBudgetQA (`93b0bb07…4c7c`) and PRD (`ae49b806…3fbe`). These paths are unchanged on `origin/main` too.
- The pin is an ancestor of `125cfacc1`. `_LATEST.md` supports the checkpoint-3 statement.
- The ledger and register rows are quoted in full and accurately.
- DL-21, the OBJ-001 row and IA §13.1 are accurate. The OBJ-001 attribution ("packaging, not derivation") is no stronger than DL-21 and §3 support.
- Token mechanism: kept open as TBD-002 / OI-006.
- Tier-0 act: not performed. TBD-007 records its content as not made. The contract only supplies a shape the act "may transcribe".
- Enabling stays with the consumer (REQ-007, REQ-015).
- The S4 contracts are used only as observations with hash prefixes (CLM-010, CON-001).
- DEL-08-02's CHECKING state is not mentioned.
- There is no `## Remaining` section. There is no readiness, CHECKING, ISSUED or acceptance claim. The contract is lifecycle-neutral.
- CON-003 (dependency coverage) and CON-004 (envelope on reads other than orientation) are honest records of open matters.

**BLOCKING**

**B-1 (content): the failure behaviour contradicts the pass-through rule.**
- REQ-005 (L149) and AC-005 (L166) require "the file-fallback signal and **no claim**" when PEC is "degraded, failing its own checks".
- In those states PEC still returns an API response. PEC-ORI-007 puts the fallback signal inside the response envelope.
- REQ-002 (L146), AC-002 (L163: "equals the versioned API response … field for field; nothing … dropped") and AX-005 (L219) require that response to pass through unchanged.
- So for a degraded response that carries claims, AC-002 and AC-005 cannot both be met. REQ-005 would make the tool strip claims, which no source supports: PEC-ORI-007 requires a signal, not removal of claims, and PEC-K-03 puts the fallback with the consumer. It would also decide envelope semantics that belong to DEL-04-03 (compare TBD-006 and CON-004).
- REQ-005's last sentence ("carry it unchanged") already leans toward pass-through, so the text is at best ambiguous.
- **Repair:** limit "file-fallback signal and no claim" to cases where no API response exists (PEC absent or unreachable, service stopped, request refused before a response). State that any API response, including a degraded or check-failing one, passes through unchanged with its envelope and signal. Update AC-005 and VER-005 (L200) to match, and keep CON-004/TBD-006 as the home of envelope questions.

**NON-BLOCKING**

- **NB-1 (content): REQ-008 overstates independence from the token mechanism.** REQ-008 (L152) says "The binding shall not depend on the choice of token mechanism". The sources say the "Token mechanism follows OI-006", and DEL-08-01's envelope note says the "auth half may be reworked on ruling", so the ruling could change how the credential is presented. AC-008 (L169, "contains no token-mechanism choice") is the right strength. **Repair:** reword REQ-008 to "embeds no token-mechanism choice; credential handling follows the OI-006 ruling through DEL-08-01's access path".
- **NB-2 (content): the owner of the reliance advertisement is not grounded.** CLM-012 (L110), REQ-015 (L159) and AX-009 (L223) name "a separate human release act" as the owner of the reliance advertisement. The quoted §12 text does not name an actor. The supporting source is `pec.yaml` L82, "separate owner act for artifact fitness, lifecycle, release, or professional reliance", and it is not quoted. **Repair:** quote L82 in CLM-013 or CLM-012 and add a claim for it. Optionally add CLM-013 to the REQ-015 matrix row (L247, which cites only CLM-012).
- **NB-3 (content): "declared" is used in two senses.** REQ-001 (L145, "shall be declared only for a query kind…"), AC-001 (L162), AC-002 (L163), VER-002 (L197) and the Praxeology line (L187, "tool-shape declaration") use "declared" to mean authoring a definition. That is the same word CON-002 (L181) leaves open in its tier-0 sense, so the wording could be read as presuming the CON-002 answer. **Repair:** use "defined" or "definition" in those places, and keep "declare" only for fields inside a definition (for example REQ-004's declared mode).

**NOTES**

- **N-1 (content):** AC-016 (L177) says "The test suite implements VER-001 through VER-015". VER-009 and VER-015 are review methods, and VER-016 (L211) correctly says "test or review record". Align AC-016 with VER-016.
- **N-2 (content):** AX-010 (L224) says INITIALIZED "makes the upstream *contracts* the reliable inputs". That sits awkwardly beside CON-001's "relies on none of their current wording". Suggested wording: "makes the upstream contracts the inputs the edges name".
- **N-3 (content):** REQ-011 (L155) cites PEC-K-03 for pull-only behaviour. The relevant PEC-K-03 clause ("never self-polls, schedules a consumer, injects into an agent, or claims an external cadence") is not quoted: CLM-014 quotes only the reliance half. CLM-015 (L128) introduces one-sentence excerpts of PEC-K-01 and PEC-K-11 with "reads", which suggests the full row. Suggest "states" and adding the pull-only clause.
- **N-4 (§B6 sufficiency, item 4 of the brief):** The contract fixes the shape adequately:
  - inputs: REQ-001, with exact operations left to the owners in TBD-004
  - outputs with envelope and budgets: REQ-002
  - paths: REQ-003
  - mode `read_only` and no side effects: REQ-004
  - failure behaviour: REQ-005, subject to B-1
  - result schema: REQ-006
  - human gates: REQ-007
  - access class: REQ-008

  It does not decide format, harness, token mechanism or transport (TBD-003, TBD-002, TBD-008). The K3 act will still have to set profile-entry fields the contract rightly leaves alone (`impl`, `requires_human_confirmation`). That is K3's decision, not a gap here.
- **N-5 (content):** The Praxeology "so that the tier-0 act can transcribe it" (L189) and AX-008 are slightly firmer than CLM-013's "may transcribe". This is acceptable because §B6 says the act comes after the contract "fixes the tool's shape"; the softer verb is optional.
- **N-6 (substrate):** `tools/scope_of_work/check_boundary_owner_resolution.py` (L180–195, the no-owner path) does not route an exclusion whose owners are instruments with no `DEL-` token (REQ-015) to NOT_CHECKABLE. Such requirements pass silently. I carried REQ-015 by hand above.
- **N-7 (substrate):** The verifier limits described in section 2. None hides a defect in this candidate.

## Suggested backcheck after repair

Rerun validate, the checklist derivation twice, the boundary check, and both prep verifiers. Rehash the candidate and update the quote and claim JSON if any quoted or claimed text moves. Then do a targeted reread of REQ-002, REQ-005, REQ-008 and REQ-015 with their ACs and VERs.

## Dispositions (WORKING_ITEMS)

Pending. Repairs are routed to the DEL-08-06 drafter, followed by a backcheck; this section is completed after the backcheck.
