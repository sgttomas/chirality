# DEL-07-04 concordance notes — Status Transition API and MCP Tool (PKG-07, W3)

Source state: `frontend/` at `fac46e33f` (byte-identical through HEAD `74150b3a8` per the W3 brief).
Behavioral evidence binds to `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped) plus named tests. No tests executed this run.

## Census

Total rows: 26.

By ClaimType:
- REQUIREMENT: 18 (DEL-07-04-REQ-001 .. REQ-018)
- EXCLUSION: 4 (EXC-001 .. EXC-004, from Specification "Out of scope" bullets)
- REMAINING_WORK: 2 (REMAINING-1 gated, REMAINING-2 ungated)
- REGISTER_DEFECT: 2 (REGISTER-1, REGISTER-2)
- ACCEPTANCE: 0 — Datasheet conditions restate REQ rows; the only datasheet-distinct condition (the PRD hash warning) is stale and captured by REQ-018 + REGISTER-1 (MR-4 fold).
- IMPLEMENTED_UNMAPPED: 0 — the status parse/transition/API/MCP surface is fully covered by REQ-001..018; sibling surfaces (deps_read/deps_write → DEL-07-05; scope_scan/scaffold_preview; domain_* → PKG-10) are not this deliverable's surface. Checked read-tools.ts tool set explicitly.

By Disposition (post fan-in correction; see "Fan-in corrections" below):
- ALIGNED: 20 (REQ-001..013, REQ-015, EXC-001..004, REMAINING-1, REMAINING-2)
- PARTIALLY_IMPLEMENTED: 3 (REQ-014, REQ-016, REQ-017 — REQ-017 stands as a CONTESTED row)
- STALE_SPECIFICATION: 1 (REQ-018)
- REMAINING_STATE_MISMATCH: 2 (REGISTER-1, REGISTER-2)

Confidence: HIGH 21, MEDIUM 5 (REQ-016, REQ-017, REGISTER-2, and the two are self-flagged below).

## Key finding — REF-006 (docs/PRD.md) reconciliation is landed but the kit is stale

The whole kit (Specification Source Warning, Datasheet Conditions line 38, Guidance, Procedure, REQ-018, and `Dependencies.csv` DEP-07-04-005) still declares `docs/PRD.md` as `HASH_MISMATCH`. But the deliverable's own `_REFERENCES.md` REF-006 (line 12) now records `ExpectedSHA256 == ActualSHA256 == ac35fba4...` with Status **MATCH**, and a live `shasum -a 256 docs/PRD.md` this run reproduces `ac35fba4...`. D-APP-35 (2026-06-21) ruled "Refresh accepted hash" and authorized the downstream reference-refresh, which has landed in `_REFERENCES.md`. Parallel to the R0 exemplar's DEL-02-01-ACC-001. Consequences:
- REQ-018 → STALE_SPECIFICATION (its blocking premise — an open mismatch — is now false; D-APP-35 governs). HIGH.
- REGISTER-1 → REMAINING_STATE_MISMATCH for the internal register inconsistency (Dependencies.csv vs _REFERENCES.md within the same deliverable). HIGH.

## Assessment-citation drift (REQ-009, REQ-010) — behavior intact

INSP-03 cited `frontend/src/lib/harness/mcp/tool-names.ts` (REQ-009) and `frontend/src/lib/harness/tool-descriptor.ts` (REQ-010). Both were refactored into the pinned `frontend/packages/harness-contract/**` package (`src/mcp/tool-names.ts`, `src/tool-descriptor.ts`) per D-APP-48. The tool names and mode-gated descriptor behavior are intact and still tested, so the PASS conclusions remain STILL CURRENT; rows cite the current package paths. This is citation drift, not a behavior change — flagged so the fan-in verifier can confirm the relocation.

## Least-confident rows (mandatory self-flag, with the flipping alternative)

- **REQ-017 (PARTIALLY_IMPLEMENTED, MEDIUM).** `normalizeActor` is explicit and fail-closed for unmapped actors (transition.ts 67-73, 170-177), which is exactly the SHALL clause; the requirement then *explicitly defers* the exact enum ("remains TBD"). Alternative reading that flips it to **ALIGNED**: the mandatory clause (explicit + fail-closed) is fully met and the un-enumerated runtime identity set is the deferred part the requirement itself leaves TBD, so there is no live scope gap. Kept at PARTIALLY_IMPLEMENTED; adjudicated CONTESTED at fan-in — see "Fan-in corrections" for the full contest record and deciding fact.
- **REQ-016 (PARTIALLY_IMPLEMENTED, MEDIUM).** Response/request schemas exist in the harness-contract descriptors (tool-descriptor.ts 505-520, 585-619) and route handlers and are exercised inline by the API tests, but no *accepted standalone schema-fixture pack* was found. Alternative reading that flips it to **ALIGNED**: the descriptor schemas plus inline golden-shape test assertions effectively satisfy the "captured schema" intent and the "TBD until accepted" clause is a soft gate that inline coverage discharges.
- **REGISTER-2 (REMAINING_STATE_MISMATCH, MEDIUM).** DEP-07-04-008 records the implementation module location as UNKNOWN/TBD while the modules demonstrably exist and are mapped by INSP-03. Alternative reading that flips it to **not a defect**: the extracted row reflects the allowed-evidence-set (four-documents) scaffold-time truth, and the kit deliberately preserves `ResponsibleParty: TBD` / module-adoption as a human-owned act (`_CONTEXT.md` Source Authority); under that reading it is an un-adopted-but-implemented state better left as a note than a REGISTER_DEFECT. Would demote to a notes-only observation.

Also flagged for recheck (non-ALIGNED, already surfaced above): REQ-014, REQ-018, REGISTER-1 (REMAINING-1 was rechecked at fan-in and corrected to ALIGNED).

## REQ-014 / REMAINING-1 — gated, not accepted-divergence

REQ-014 (approval evidence binds to content; content changes void approval until review) is PARTIALLY_IMPLEMENTED: approval SHA is persisted (transition.ts 120-135; status-writer.ts) but there is no automatic content-change revalidation (confirmed by a real search — no content-hash void logic on the transition surface; the absence of a test is correct). This is the recorded **gated** remaining item (REMAINING-1). Per the W3 rule, D-APP-53 ruled "Option A only" and thereby *withheld* authorization for the Option C content-change item — a withholding, not an affirmative permit — so ACCEPTED_DIVERGENCE is barred; the facts dictate PARTIALLY_IMPLEMENTED on REQ-014 and ALIGNED on the REMAINING-1 row itself (see "Fan-in corrections"). `HumanDecisionNeeded = NEW-PACKET` (the needed new owner ruling has no register row yet). `SelectableUnderCurrentLoop = NO` (gate unsatisfied).

## Fan-in corrections (W3 fan-in verification round-trip)

- **REMAINING-1: REMAINING_STATE_MISMATCH → ALIGNED (verifier REFUTED; accepted after independent recheck).** I re-tested the row against each §7 REMAINING_STATE_MISMATCH prong: (a) the item is neither landed (no content-change revalidation exists at fac46e33f) nor ruled shut (D-APP-53 left it open behind a gate); (b) no residual is omitted; (c) the recorded verbatim gate suffix "(gated: new owner ruling required — D-APP-53 2026-07-10 ruled Option A only)" exactly matches the D-APP-53 ruling record (line 58) and the packet §7 gate mechanism — metadata agrees with current authority and implementation. An accurately recorded, correctly gated, genuinely open item is concordant. My original reasoning erred by treating "not ACCEPTED_DIVERGENCE" (the W3 withheld-authorization rule) as forcing a mismatch disposition; the rule says "as the facts dictate," and the facts dictate ALIGNED. HumanDecisionNeeded=NEW-PACKET and SelectableUnderCurrentLoop=NO are unchanged. The underlying implementation gap remains carried on REQ-014 (PARTIALLY_IMPLEMENTED, CONFIRMED at fan-in).
- **REQ-017: kept PARTIALLY_IMPLEMENTED — standing CONTESTED row for R3.** Verifier verdict CONTESTED; both readings recorded:
  - *Reading A (ALIGNED):* the SHALL clause — explicit actor mapping plus fail-closed rejection of unmapped actors — is fully met (transition.ts normalizeActor lines 67-73; UNAUTHORIZED_ACTOR lines 170-177, tested at lifecycle-status.test.ts 115-137), and the requirement's own text removes the exact enum from the current claim surface ("exact enum or mapping remains TBD"), analogous to the Declared-TBD non-defect rule.
  - *Reading B (PARTIALLY_IMPLEMENTED, retained):* the partial satisfaction lies in the SHALL clause itself, not only the deferred enum — `normalizeActor` uses a prefix wildcard, `normalized.startsWith('HUMAN')` (transition.ts line 69), so ANY actor string beginning with "HUMAN" (e.g. `HUMANOID`, `HUMAN_RESOURCES`) normalizes to `HUMAN` and is thereby authorized for human-gate transitions. Heuristic prefix matching is not an *explicit* mapping, and it is the live mechanism behind INSP-03's still-current "runtime actor identity mapping is narrow" PARTIAL.
  - *Deciding fact:* whether the requirement-internal "exact enum ... remains TBD" clause removes enumeration from the current claim surface. Reading B holds that even granting that removal, the `startsWith('HUMAN')` wildcard independently falls short of "explicit," so the row stays PARTIALLY_IMPLEMENTED. Recorded as a standing contested row for R3.

## Register-defect summary

- REGISTER-1: `Dependencies.csv` DEP-07-04-005 (and kit Source Warnings) assert REF-006 `HASH_MISMATCH`/TBD, contradicting the same deliverable's `_REFERENCES.md` REF-006 MATCH. Internal register inconsistency + metadata lag against the D-APP-35 reconciliation. HIGH.
- REGISTER-2: DEP-07-04-008 records implementation-module-location TBD/UNKNOWN/ACTIVE while the modules now exist in the live tree. Metadata lag against the live implementation. MEDIUM (self-flagged above).

Per the W3 brief, the bare Declared-Upstream/Downstream "TBD" sections in `_DEPENDENCIES.md` (lines 12-18) are human-owned by design (SPEC §5.2) and are NOT emitted as register defects. Observation only: they remain TBD while the Extracted register holds 8 ACTIVE rows.

## Method notes / deviations

- No method deviations. 19-column header copied verbatim from the R0 exemplar; MR-1 (single AssessmentEvidence token), MR-2 (SelectableUnderCurrentLoop=YES only on the one ungated REMAINING row), MR-5 (bare `REGISTER-n` IDs), MR-6 (verbatim gate suffix on REMAINING-1) all satisfied.
- REQUIREMENT_INDEX.csv listed both prefixed (`DEL-07-04-REQ-0nn`) and bare (`REQ-0nn`) IDs for this deliverable — a duplication in the R1 index, not a real doubling of requirements. The claim set was re-derived from Specification.md (18 requirements); no parser-gap zero-scan applied here.
- Kit-wide stale documentation observation (not separately rowed): Datasheet "Existing implementation path: TBD" (line 42), Procedure prerequisite "Implementation module location TBD" (line 16), and `ResponsibleParty: TBD` persist even though the implementation is substantially complete and mapped. Captured via REGISTER-2 and the REQ rows' implementation evidence.
