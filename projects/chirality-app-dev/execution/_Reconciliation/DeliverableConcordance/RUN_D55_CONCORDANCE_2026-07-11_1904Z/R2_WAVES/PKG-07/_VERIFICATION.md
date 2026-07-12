# W3 (PKG-07) — wave-local verification record

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; R2 Wave 3, PKG-07
  (DEL-07-01..06).
- **Roster (Receipt 18 steer):** six `opus` discovery agents; fan-in by
  `fable` at high effort (package-scoped, read-only); verdicts composed here
  by the fable orchestrator. Refutations returned to owning agents; owners
  re-verified independently before editing. No judgment edited by anyone but
  its owner.
- **Source state:** frontend/ at `fac46e33f`, byte-identical through HEAD
  `74150b3a8` (orchestrator-verified at W3 dispatch; verifier re-confirmed).
  Behavioral evidence bound to `GATE-TRANSCRIPT(W1@fac46e33f)`.

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## 1. Deterministic structural validation

Final pass: 0 errors / 0 warnings; 125 rows (18+21+17+26+22+21). Row count
unchanged by fan-in (all corrections were in-place cell edits).

## 2. Fan-in recheck outcomes (46 rows rechecked)

| Deliverable | Rechecked | Confirmed | Refuted → resolution | Contested |
|---|---|---|---|---|
| DEL-07-01 | 7 | 7 | — | 0 |
| DEL-07-02 | 8 | 7 | UNMAPPED-1 (scaffold preview/dry-run) → accepted sibling mapping exists: decomposition v3.2 line 330 assigns scaffold preview to DEL-06-03. Owner accepted; row re-dispositioned ALIGNED with the DEL-06-03 cross-deliverable handle; NEW-PACKET withdrawn. | 0 |
| DEL-07-03 | 12 | 3 | REQ-001..007 + REQ-009 (8-row STALE_ASSESSMENT class) → refuted on MR-1's reserve condition: the assessment's ADQ-07 Superseding Note (lines 15-24) recasts the FAIL/PARTIAL matrix cells as a recorded historical gap, so no surface presents the stale conclusion as current truth; the cited precedents (R0 DEL-02-01, W2 DEL-04-03) are noteless and distinguishable; sibling DEL-07-02 treated the identical ADQ-06 note as ALIGNED+OVERTAKEN. Owner re-verified (grep: exactly two assessments corpus-wide carry superseding notes — DEL-07-02, DEL-07-03) and accepted; all eight rows → ALIGNED, AssessmentEvidence stays OVERTAKEN, R5 matrix-annotation repair retained in RemainingWork. | 0 |
| DEL-07-04 | 9 | 7 | REMAINING-1 → refuted: no §7 REMAINING_STATE_MISMATCH prong holds — the _STATUS.md item is genuinely open, accurately recorded, and its verbatim gate suffix exactly matches the D-APP-53 ruling record; an accurately recorded, correctly gated open item is concordant. Owner accepted → ALIGNED (HumanDecisionNeeded=NEW-PACKET and Selectable=NO retained; the implementation gap stays carried on REQ-014). | **REQ-017 stands explicitly CONTESTED** (owner kept PARTIALLY_IMPLEMENTED): Reading A — the SHALL clause (explicit actor mapping + fail-closed) is met and the requirement's own "exact enum … remains TBD" defers enumeration → ALIGNED. Reading B (owner) — on re-verification the live mechanism is a prefix wildcard (`normalized.startsWith('HUMAN')`, transition.ts:69), so any HUMAN*-prefixed actor authorizes human-gate transitions; heuristic prefix matching independently falls short of "explicit" mapping regardless of the enum question. Deciding facts recorded in the owner's notes. R3/R4 input. |
| DEL-07-05 | 7 | 6 | — | **UNMAPPED-001 resolved-with-standing-contest:** verifier surfaced docs/TYPES.md §6.2 line 211 ("IMPLEMENTS_NODE … normally one per deliverable") as the corpus mapping for the anchor-count warning. Owner adopted Reading B → ALIGNED (spec-refresh residual under REQ-006), Confidence kept MEDIUM, with the full both-readings contest record in notes. Open R3 classification question: does TYPES.md descriptive-normative vocabulary-table wording count as an "accepted mapping" under the W3 corpus-wide test? |
| DEL-07-06 | 3 | 3 | — | 0 |

Net: 46 rechecked — 34 confirmed, 10 refuted (ALL accepted by their owning
agents after independent re-verification), 2 contested (1 standing on the
recorded disposition: DEL-07-04 REQ-017; 1 resolved by owner adoption with
the classification question escalated: DEL-07-05 UNMAPPED-001). Final census:
125 rows — ALIGNED 101, PARTIALLY_IMPLEMENTED 9, REMAINING_STATE_MISMATCH 8,
STALE_SPECIFICATION 6, IMPLEMENTED_DIFFERENTLY 1; zero AUTHORITY_CONFLICT /
UNKNOWN / DEFERRED_AGENT_WORKFLOW.

## 3. Cross-checks and R3 flags

1. **STALE_ASSESSMENT boundary (adjudicated intra-package, open run-wide):**
   the superseding-note test decided the DEL-07-03 class here (note present →
   ALIGNED+OVERTAKEN; noteless → STALE_ASSESSMENT stands, per R0 DEL-02-01
   and W2 DEL-04-03). R3 should ratify this boundary run-wide so PKG-07's
   uniform treatment and the two noteless precedents stay consistent.
2. **REF-006 (docs/PRD.md) staleness family — verified once, applied six
   times:** live shasum `ac35fba4…c30bfd` equals Expected==Actual in all six
   deliverables' `_REFERENCES.md` (Status MATCH); D-APP-35 (refresh accepted)
   and D-APP-38 (corpus v6) confirmed. Kit assertions of HASH_MISMATCH →
   STALE_SPECIFICATION (6 rows); register rows carrying the stale warning →
   REMAINING_STATE_MISMATCH (6 REGISTER rows). One bounded package-wide R5
   doc-repair tranche under the existing D-APP-35 authorization.
3. **No incompatible sibling surface claims** — scope boundaries interlock
   (DEL-07-02 EXC-002/003 ↔ DEL-07-04/05; DEL-07-04 EXC-001 ↔ DEL-07-05;
   DEL-07-03 EXC-002/003 ↔ DEL-07-04/05). DEL-07-02 REQ-011's residual names
   a delegation question to DEL-07-01 (SOW-027) rather than claiming the
   surface.
4. **Cross-package handles for R3:** (a) scaffold-preview ownership → verify
   DEL-06-03's merged W2 ledger claims the surface (from the accepted
   DEL-07-02 UNMAPPED-1 refutation); (b) DEL-07-05 REQ-017 possible mapping
   to the shared harness-options owner (PKG-03/04 surface); (c)
   DECISION_INDEX.csv under-links D-APP-35 to PRD-grounded PKG-07
   deliverables (verified: zero PKG-07 rows) — index-gap note; (d) the
   TYPES.md §6.2 "accepted mapping" classification question (item in §2).
5. **Notes factual corrections applied by owners:** DEL-07-04 (the W3
   anti-ACCEPTED_DIVERGENCE rule does not force REMAINING_STATE_MISMATCH);
   DEL-07-05 (code does not strictly foreclose a literal location-TBD string;
   divergence still material). All "no test exists" assertions in this
   package were re-searched by the verifier and hold.
