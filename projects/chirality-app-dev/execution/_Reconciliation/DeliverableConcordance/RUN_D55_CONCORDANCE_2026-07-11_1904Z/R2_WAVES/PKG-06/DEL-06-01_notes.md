# R2 notes — DEL-06-01 ChiralityPermissionOverlay and Mode Mapping (PKG-06, Wave 2)

Run: RUN_D55_CONCORDANCE_2026-07-11_1904Z. Source state: frontend/ at `fac46e33f`
(byte-identical through HEAD `1625b396a`). Behavioral verification bound to
`GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped).

## Census

Total rows: 22 (initially 23; REGISTER-2 dropped after fan-in REFUTED verdict —
see the fan-in addendum at the end of this file).

By ClaimType:
- REQUIREMENT: 15 (REQ-001..015, re-derived from Specification.md — the R1
  REQUIREMENT_INDEX 15 canonical IDs match; the six bare `REQ-00n` rows in that
  index are the INSP-03 matrix duplicates, not extra requirements)
- EXCLUSION: 3 (EXC-001..003, from Specification "Out of scope" lines 17-19)
- ACCEPTANCE: 1 (ACC-001, Datasheet PRD source-state condition — MR-4 distinct)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-1, subagent/Agent permission class)
- REMAINING_WORK: 1 (REMAINING-1, the concordance bootstrap)
- REGISTER_DEFECT: 1 (REGISTER-1)

By Disposition:
- ALIGNED: 19 (all 15 REQ + all 3 EXC + REMAINING-1)
- STALE_SPECIFICATION: 1 (ACC-001)
- IMPLEMENTED_UNDOCUMENTED: 1 (UNMAPPED-1)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

All 15 requirements are implemented, tested, and gate-green; INSP-03 (2026-06-21,
SHA `09c840be20`) rated all 15 PASS and those conclusions are STILL CURRENT at
`fac46e33f`. This deliverable is substantively aligned; the material findings are
one stale source-state warning (ACC-001), one register-metadata lag (REGISTER-1),
one unmapped capability class, and two doc-pointer refreshes folded into
REQ-014/REQ-015 RemainingWork.

## Least-confident rows (self-flagged; alternative reading that would flip them)

- **REGISTER-2 (LOW) — since REFUTED at fan-in and dropped; entry preserved for
  the record.** Read the `D-APP-38 authority corpus v2` label in
  `_DEPENDENCIES.md`/Dependencies.csv as stale vs the current v6 snapshot
  (AUTHORITY_MAP). Alternative reading (the one that prevailed): "v2" is accurate
  historical provenance — the corpus version at which REF-006 was reconciled —
  not a current-state assertion, so it is not a defect at all. The REF-006 MATCH
  fact it accompanied is verified correct regardless.
- **REGISTER-1 (MEDIUM).** Treats DEP-06-01-014 (`UNKNOWN`/`TBD`/`PENDING`/`LOW`)
  as overtaken because the event-writer call path is now concrete
  (`session-events.ts` `appendHarnessEvent`). Alternative reading: the register's
  `UNKNOWN` is specifically about the *owning upstream deliverable*, which is still
  genuinely unnamed; only the call path resolved, so the row is arguably still
  accurate and this is not a mismatch. Kept as REMAINING_STATE_MISMATCH because the
  cell text "exact call path is TBD" is now literally false.
- **REQ-008 (MEDIUM, ALIGNED).** Rated ALIGNED because both `canUseTool` and hooks
  are structurally attached in `buildSdkOptions` and hook enforcement is tested.
  Alternative reading: no test asserts the *invariant* that both are attached on
  every write/shell-exposing path (INSP-03 Medium gap + Forward Recommendation);
  a stricter reviewer could rate PARTIALLY_IMPLEMENTED on verification coverage.
  Flagged as additive-test RemainingWork, not a _STATUS residual.
- **REQ-011 (MEDIUM, ALIGNED).** The prompt-is-not-a-boundary property is enforced
  structurally (decisions derive from descriptor/path/shell, never prompt) but no
  dedicated negative test names the prompt-injection claim. Alternative reading:
  STALE_VERIFICATION on the assessment's cited persona-manager evidence. Kept
  ALIGNED on the structural guarantee.
- **UNMAPPED-1 (MEDIUM).** The subagent/Agent permission class is ruling-governed
  (D-APP-10) and lives on the overlay surface but is unmapped in this kit.
  Alternative reading: it belongs wholly to the D-APP-10 executable-subagent-bridge
  deliverable and should not be an UNMAPPED row against DEL-06-01 at all — hence
  HumanDecisionNeeded=NEW-PACKET rather than an adoption recommendation.

Per the brief, the fan-in verifier should recheck these plus every non-ALIGNED row
(ACC-001, UNMAPPED-1, REGISTER-1; REGISTER-2 already adjudicated — see addendum).

## Register-defect summary

- **REGISTER-1** — Dependencies.csv DEP-06-01-014 (event-writer/session-JSONL
  interface) still carries `TargetType=UNKNOWN`, `Target=TBD`, `PENDING`, `LOW`,
  and "exact call path is TBD"; the call path is now concrete
  (`permission-overlay.ts` -> `session-events.ts appendHarnessEvent`).

A second candidate (REGISTER-2, the "corpus v2" version label) was initially
emitted and withdrawn after the fan-in REFUTED verdict; see the addendum.

No count/lifecycle inconsistency found in `_DEPENDENCIES.md`: 14 rows, 11 ACTIVE /
3 RETIRED, SATISFIED 6 / PENDING 5 / NOT_APPLICABLE 3 all reconcile against
Dependencies.csv. The Datasheet References table listing REF-006 as "HASH_MISMATCH
warning" (line 63) is a kit-doc staleness captured under ACC-001
(STALE_SPECIFICATION), not a register-file internal inconsistency.

## Notable observations / method notes

- **Implementation relocation (D-APP-48).** The assessment cited the tool
  descriptor taxonomy at `frontend/src/lib/harness/tool-descriptor.ts`; it has been
  relocated to `frontend/packages/harness-contract/src/tool-descriptor.ts` under the
  D-APP-48 SHA-pinned intra-repo pull (AUTHORITY_MAP lists that path as in-scope
  implementation evidence). The assessment's PASS conclusion for REQ-005 remains
  current; only the file path drifted. INSP-03 line anchors are all from
  `09c840be20` and shift by ~1 line at `fac46e33f`; rows cite current anchors.
- **Cross-package overlap (declared).** The Chirality->SDK posture mapping
  (`mapPermissionMode` in `sdk-options-builder.ts`) and the allowedTools/hooks
  wiring are shared with DEL-04-02's options-builder side per the dispatch's
  cross-package context. This deliverable's rows claim the mode-mapping and
  restriction *semantics*; they do not re-litigate the options-builder mechanics.
  W1's DEL-02-04 recorded the missing operator mode/persona UI control (a Toolkit
  surface) — that UI gap is out of this overlay's scope and not re-raised here.
- **Extra hard-deny classes.** The overlay implements `danger` and `reserved`
  capability-class hard-denies beyond the spec's enumerated write/edit/bash/network
  set (REQ-005). These broaden denial (safe direction) and are folded into REQ-005
  evidence rather than emitted as separate unmapped rows; only the subagent class
  (which also adds Agent tool exposure and is ruling-governed) is flagged
  (UNMAPPED-1).
- **No DOCUMENTED_UNIMPLEMENTED, AUTHORITY_CONFLICT, or DEFERRED_AGENT_WORKFLOW
  rows.** All 15 requirements have adequate implementation; no live normative
  surfaces conflict on this deliverable's claims; no finding required agent-workflow
  redesign.
- No method deviations. Write scope limited to the two authorized files. No tests
  executed; verification bound to the W1 gate transcript per MR-3.

## Fan-in addendum — REGISTER-2 REFUTED and dropped

Fan-in verification rechecked 6 rows: 5 CONFIRMED (ACC-001, UNMAPPED-1 including
the NEW-PACKET routing, REGISTER-1, REQ-008, REQ-011); REGISTER-2 REFUTED.
Verifier basis: every cited "corpus v2" occurrence (`_DEPENDENCIES.md` lines 24
and 74; Dependencies.csv DEP-06-01-010 Notes) sits inside sentences describing
the ADQ-11-era reconciliation event, when the corpus was in fact v2 — accurate
provenance, not a false current-state assertion; line 74 is explicitly tagged
`[HISTORICAL WARNING]`; the current-state claims (REF-006 MATCH, DEP-06-01-010
SATISFIED, warning retired) are true.

Discovery-agent action: independently re-verified before editing — confirmed the
`[HISTORICAL WARNING]` tag on `_DEPENDENCIES.md` line 74 and the event-narrative
framing of all "corpus v2" occurrences (also line 81 Run History and INSP-03
lines 45/50, same historical framing). Accepted the refutation (it matches this
file's own pre-flagged LOW-confidence alternative reading), dropped the
REGISTER-2 row from `DEL-06-01_claims.csv` without renumbering, and updated the
census above (total 23 -> 22; REGISTER_DEFECT 2 -> 1;
REMAINING_STATE_MISMATCH 2 -> 1). No other row changed.
