# Verifier verdict 02 — DEL-00-01 ADRs and add-on P Scope of Work (`MODE=VERIFY`)

Reviewer: fresh read-only `pec-reviewer` TASK (agent `ac72f441847105e55`), `claude-opus-5-5`, high reasoning; brief `VERIFIER_BRIEF.md` (`2f7abd50…4af`). Reviewed at branch head `c4f9075b9` (observation `6c6cc1b00`). Transcribed by WORKING_ITEMS from the reviewer's hand-back (findings as given; the "checked" section condensed); the manager's dispositions follow.

---

**Verdict: FAIL.** Two BLOCKING findings, both about how the packet describes the DEL-00-01 contract (the add-on P candidate) and what that candidate changes. Neither affects byte identity, and every check passes. The ADR candidate has no blocking defect.

## Findings

1. **BLOCKING — the packet misstates inventory row INV-130 and skips the loci that row names.** Draft L172 ("inventory INV-130: CLM-005 L81, same premise in REQ-004") and `premise/DEL-00-01_SOW.json` P04 cause ("INV-130 note (same premise in REQ-004)"). The row (`IMPACT_INVENTORY_PEC_BASIS.csv`, `f0bba13a…e3bc`) Notes read: "Same premise in REQ-005/AC-003/AX-004 ("accepted v2 runtime/client ... boundary")." — no REQ-004. This is a false statement about a scope-binding source and hides that the inventory names REQ-005, AC-003 and AX-004; the packet leaves those unchanged (draft L129) without acknowledging the inventory's claim. REQ-004 does state "Root owns generic runtime semantics" word for word — amending it is right, but it was found by review, not by INV-130. On substance, keeping REQ-005, AC-003, AX-004 and OUT-002 is defensible (they echo register wording still verbatim at `189f205ff` — SOW-088 and the DEL-00-01 `Deliverables.csv` row read "accepted v2 runtime/client and human-only-act boundary"; they name no runtime owner; changing AC-003 would change the checklist). Repair: correct both citations; disposition INV-130's REQ-005/AC-003/AX-004 explicitly under "Loci examined"; label REQ-004 a review finding.
2. **BLOCKING — SOW hunks P01 and part of P02 fix text already stale since SCA-004.** `DRAFTER_BRIEF.md` rule 3 makes such text an "other finding". The DEL-00-01 SOW was last changed at `ea6b4b5d0` (2026-07-28); `_REFERENCES.md` was re-pinned to revision 1.4 at `1c6ecc6d9` (2026-08-03); from then "revision 1.3, the current successor basis" (objective warrant) and "`_REFERENCES.md` now names … revision 1.3 … SCA-003 establishes revision 1.3 as the current successor" (basis note) were false. The ledger records "first made false by SCA-004", the draft says "stale since revision 1.4", AX-008 says "made false again", yet the draft still calls add-on P "the premise-only correction" and question 2 lists "the currency paragraphs" without flagging the departure. Mitigation: P02's added "except where its premise amendment (AX-008) …" clause is a genuine consequence, and leaving "SCA-003 establishes revision 1.3 as the current successor" beside it would contradict it; SCA-005 §B4 names no housekeeping item for DEL-00-01. Repair, either: (a) drop P01, reduce P02 to the final clause, list the rest under "Other findings", adjust AX-008, re-render; or (b) keep and disclose as a departure made for coherence, as an explicit reading in question 4, and stop calling P strictly premise-only.
3. **NON-BLOCKING — DEL-01-05's "accepted ADR" wording is affected by the lapse, undisclosed.** DEL-01-05 (`IN_PROGRESS`) `ScopeOfWork.md` TBD-005 (L72) rests on "D-PEC-72 O-B and accepted `ADR-PEC-V2-001`" (the S1 candidate keeps it, `cbdb00934`, L90). Under ruling A the AC-007 acceptance lapses (in force only under R2), yet the draft says TBD-005 is "unchanged in meaning and text" and "any ruling order works". Repair: disclose as for DEL-01-01 CLM-009; route to DEL-01-05's own packet.
4. **NON-BLOCKING — AX-008 understates what changed and cites the wrong source for one list.** "in each, only the named runtime owner changes" — the owned scope also changes (from "generic runtime semantics" to an enumerated list "for each App instance"). AX-008 cites PRD v2.4 §4.2/§15 and C13 for "sessions, delegation, tools, turn locks, and interruption", which those sources state as "sessions, delegation, and turn admission"; the five-item list is K-RUNTIME-1 (`docs/CONTRACT.md` L168), not cited in AX-008. Repair: reword; cite K-RUNTIME-1.
5. **NON-BLOCKING — "PEC is an optional client" kept; defensible, reason weak.** "Optional" holds and posture 4 now says the seam is deferred; but no current source states PEC is a client (PRD §13: a per-application Runtime client is Deferred; PRD §8 casts the Runtime as a consumer of PEC). The draft's reason supports the boundary label, not "optional client". Repair: give the deferral reasoning in question 4(b).
6. **NON-BLOCKING — "D-PEC-56 behaviors 2, 4, and 7" still right, behavior 2 unanchored.** Behavior 2 (D-PEC-56 L19) is consistent with D-GOV-43 A2; 4 and 7 survive per D-PEC-58 behavior 8, PRD §15, C13; behavior 3 (now false) is correctly not cited; claim S15 anchors only 4 and 7. Repair: add a `contains` claim on D-PEC-56 L19.
7. **NON-BLOCKING — keeping ADR-002's "Sources: … PRD v2.2 §§4, 10, 13, and 15" is defensible** (dated record metadata; the note explains it; question 4(b) covers it).
8. **NON-BLOCKING — R1 gives only the with-P checklist hash.** Without P, a rerun uses the unchanged checklist `bb815439…3b84`. State that.
9. **NON-BLOCKING — `projects/pec/AGENTS.md` is stale on the client seam** (L175–176 "The client seam carries as a concept, reimplemented against v2 entities (PRD v2 §13)" vs PRD v2.4 §13 and SOW-087 OUT). Outside the targets; report only.
10. **NON-BLOCKING, cosmetic.** ADR hunk P02's daemon token is on L54, not L53 (SCA-005 §B5 says L54). "on that path" mirrors PRD §4.2 without an explicit antecedent. Pre-existing: the ADR never cites the path `projects/pec/docs/.archive/adr/ADR.md` literally, which REQ-005 asks for; an R1 rerun would meet this.

## What was checked (condensed)

- Byte identity: `render_candidates.py --only DEL-00-01_ADR DEL-00-01_SOW` exit 0; ADR `9e6961ac…8387` (6 hunks, 183 lines), SOW `61a31ff0…eb88` (5 hunks, 154 lines); preimages at `6c6cc1b00` and `189f205ff` match `_REVIEW.md` L65 and L82–83; `diff -u` shows only the hunks.
- ADR hunks: P02/P03 named by SCA-005 §B5; P04/P05 the runtime-ownership premise; P06 SOW-087 OUT, DEL-07-05 retired; P01 the uniform note. D-GOV-43 A2 content accurate (K-RUNTIME-1 L168; DIRECTIVE §7; `D-GOV-43_codex_host_replatform.md` L73; PRD §4.2/§15). Bridge/deferral facts accurate.
- Completeness: no daemon, cmux or Root-runtime premise remains in the ADRs; cited PRD rows byte-equal v2.2 → v2.4 except STR-002, still accurately invoked. ADR decision, D-PEC-72 selection, non-decisions and ADR-001 context byte-identical; AC-007's two confirmations still hold.
- SOW `MODE=VERIFY`: `PASS format=SOW_V1`; checklist twice `f363f7d9…1f1a`, no AC text change from `bb815439…`; boundary exit 0; DEL-00-01/REQ-006 and /AC-005 byte-identical; birth-basis decision sound.
- Coherence: with P the amended ADR satisfies REQ-003..006 and AC-001..007; without P, REQ-004/CLM-005 contradict posture 3 exactly as disclosed.
- Verifiers: quotes `RESULT PASS 29/29`; state claims `RESULT PASS 45/45`. `shasum -c SHA256SUMS` 95 OK. `pec_reliance_hold.py --operation candidate-validation` ALLOW ×2. No lifecycle/acceptance/CHECKING claim; no D-PEC-10x number in the candidates.

---

## Manager dispositions (WORKING_ITEMS)

1. **Accepted; repaired.** The draft and the ledger (P04 cause, now P02 after renumbering) cite INV-130 correctly; REQ-004 is labelled a review finding; "Loci examined" dispositions INV-130's REQ-005, AC-003 and AX-004 (and OUT-002) with the reason above.
2. **Accepted; repaired by option (a).** The DEL-00-01 SOW ledger drops the objective-warrant and basis-provenance hunks; both paragraphs stay as accepted and are listed under "Other findings". AX-008 now states that, apart from this amendment, the contract cites its revision-1.3 birth basis and that the SCA-004-era currency wording is left and reported. Candidate re-rendered and re-hashed; evidence regenerated.
3. **Accepted; repaired** (DEL-01-05 TBD-005 added to the downstream account, routed to DEL-01-05's own packet or to R1/R2).
4. **Accepted; repaired** (AX-008 reworded; K-RUNTIME-1 cited for the five-item list).
5. **Accepted; repaired** (question 4(b) gives the deferral reasoning).
6. **Accepted; repaired** (a `contains` claim anchors D-PEC-56 behavior 2 at `6c6cc1b00`).
7. **Noted; no change.**
8. **Accepted; repaired** (R1 names both checklist hashes).
9. **Accepted; added to "Other findings".**
10. **Accepted in part:** the ledger and draft loci now read L53–54; the other two are noted (the REQ-005 path point is added to "Other findings").
