# W3 (PKG-08) — wave-local verification record

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; R2 Wave 3, PKG-08
  (DEL-08-01..05 — the product-runtime portions; agent-workflow surfaces are
  FROZEN_PROCESS_INPUT under plan §3 boundary 8).
- **Roster (Receipt 18 steer):** five `opus` discovery agents; fan-in by
  `fable` at high effort (package-scoped, read-only); verdicts composed here
  by the fable orchestrator. Refutations returned to owning agents; owners
  re-verified independently before editing. No judgment edited by anyone but
  its owner.
- **Source state:** frontend/ at `fac46e33f`, byte-identical through HEAD
  `74150b3a8` (orchestrator-verified at W3 dispatch; verifier re-confirmed).
  Behavioral evidence bound to `GATE-TRANSCRIPT(W1@fac46e33f)`.

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## 1. Deterministic structural validation

Final pass: 0 errors / 0 warnings; 98 rows (21+24+19+17+17). Row count
unchanged by fan-in (all corrections were in-place cell edits).

## 2. Fan-in recheck outcomes (28 rows rechecked)

| Deliverable | Rechecked | Confirmed | Refuted → resolution | Contested |
|---|---|---|---|---|
| DEL-08-01 | 5 | 4 | UNMAPPED-1 (packaged-SDK verification) → accepted sibling mapping exists: decomposition v3.2 line 363 + DEL-09-04 Specification line 32 (REQ-008, SDK subprocess packaging probe). Owner re-verified both sources and accepted → ALIGNED with the DEL-09-04 handle; NEW-PACKET withdrawn. Notes false-absence corrected: validate-route.test.ts and harness/routes.test.ts DO drive the inside-instruction-root rejection through real routes (REQ002 evidence strengthened, Confidence raised). | 0 |
| DEL-08-02 | 9 | 7 | — | **REQ-004 resolved by owner re-disposition** (STALE_SPECIFICATION → IMPLEMENTED_DIFFERENTLY, MEDIUM, NEW-PACKET): verifier's deciding fact — `agents/AGENT_RECONCILIATION.md` is Type-1 PERSONA since repo origin, so D-APP-24's Type-2 exclusion never governed the RECONCILING alias removal and D-APP-28 rules routing, not alias vocabulary. Owner re-verified (frontmatter + git history + grep of both ruling records), demoted both rulings to `(context)`, chose IMPLEMENTED_DIFFERENTLY over AUTHORITY_CONFLICT because precedence is explicit (AUTHORITY_MAP note 1; ADQ-12 is agent supersession, not a ruling), and flipped AssessmentEvidence to OVERTAKEN. **REQ-014 kept STALE_SPECIFICATION with the defect relocated:** verifier's deciding fact — Datasheet line 31 transcribes LIVE docs/SPEC.md §13.1 line 715 ("HELP_HUMAN or configured default"). Owner rejected the ALIGNED reading (live default is hardcoded WORKING_ITEMS — neither configured nor HELP_HUMAN), so the repair target is the corpus line itself; HumanDecisionNeeded NO → NEW-PACKET (D-APP-38 amendment family). Both resolutions carry full both-readings records in notes; R3/R4 should ratify the labels before the corpus-bump packet is drafted. |
| DEL-08-03 | 3 | 3 | — (IMPLEMENTED_DIFFERENTLY REQ-010 upheld: pipeline scan consumes `/api/project/deliverables`, not the spec-named `/api/working-root/scope`; both SPEC §17.2 active-root surfaces — intent holds, named endpoint differs.) | 0 |
| DEL-08-04 | 5 | 5 | — (UNMAPPED-1 conditional-Agent-exposure ALIGNED upheld on D-APP-10's affirmative ruling text; REGISTER-1 metadata lag confirmed.) | 0 |
| DEL-08-05 | 6 | 6 | — (UNMAPPED-1 hardcoded child-output limits upheld as genuinely unmapped threshold VALUES, cleanly distinct from DEL-05-05's `descriptor.resultBudget` — this resolves the W2 PKG-05 handle.) | 0 |

Net: 28 rechecked — 25 confirmed, 1 refuted (accepted by its owning agent
after independent re-verification), 2 contested (both resolved by their
owning agent with full contest records; the label questions escalate to
R3/R4). Final census: 98 rows — ALIGNED 82, STALE_SPECIFICATION 9,
IMPLEMENTED_UNDOCUMENTED 3, IMPLEMENTED_DIFFERENTLY 2,
REMAINING_STATE_MISMATCH 2; zero AUTHORITY_CONFLICT / UNKNOWN /
DEFERRED_AGENT_WORKFLOW.

## 3. Cross-checks and R3 flags

1. **FROZEN_PROCESS_INPUT conclusion verified for all five deliverables:**
   every rechecked row resolves on concordance facts about product-runtime
   surfaces or corpus/ruling precedence; reading a frozen agent file's
   AGENT_TYPE frontmatter is a permitted concordance fact, not workflow
   design judgment. No missed DEFERRED_AGENT_WORKFLOW rows.
2. **The MR-11 corpus-staleness block survived adversarial review 4-of-6
   intact** (REQ-003/008/009 on D-APP-28/24; ACC-001 on vocabulary
   completeness), with the two failures re-dispositioned by their owner
   (REQ-004) or relocated (REQ-014, defect moved from kit to corpus line).
   NEW-PACKET family now: DEL-08-02 REQ-003/004/008/009/014 + ACC-001 — six
   corpus-amendment packets for the D-APP-38 family; R4 input.
3. **Cross-deliverable handles verified consistent:** DEL-08-04 ↔ DEL-06-01
   (consumption vs declaration of the `subagent` permission class —
   compatible, no double-mapping); DEL-08-05 ↔ DEL-05-05 (hardcoded child
   limits vs descriptor resultBudget — cleanly separated; W2 handle
   resolved); DEL-08-01 ↔ DEL-08-04 (conformance vs implementation of the
   governance surface — compatible); DEL-08-01 ↔ DEL-09-04
   (packaged-SDK verification — W4 must verify DEL-09-04 claims it).
4. **Known double-count for R3 de-duplication:** DEL-08-03 UNMAPPED-1 and
   merged W1 DEL-02-02 UNMAPPED-1/2 record the same shared-file panels
   (pipeline-surface.tsx scaffold/contracts/lifecycle panels); both sides
   flag it; candidate owners DEL-07-02 (scaffold) / DEL-07-04 (transition).
5. **Kit/corpus factual errors recorded (not repaired — evidence-only run):**
   DEL-08-02 Datasheet line 26 ("former targets are not Type 0/1 loop
   personas") is false for RECONCILIATION; docs/SPEC.md §13.1 line 715
   misdescribes the live hardcoded WORKING_ITEMS default (the REQ-014
   packet); TYPES §4.3 line cites corrected 157/159 → 158/160.
6. **Cross-package handles for R3:** subagent permission-class ownership
   split (DEL-08-04/DEL-06-01) formalization; `isMatrixLaunchBlockedByStreaming`
   UI-guard ownership (DEL-08-02 UNMAPPED-001, no decomposition assignment
   found); child-output threshold values packet (DEL-08-05 UNMAPPED-1,
   NEW-PACKET); the DEL-08-03/DEL-02-02 panel double-count (item 4).
