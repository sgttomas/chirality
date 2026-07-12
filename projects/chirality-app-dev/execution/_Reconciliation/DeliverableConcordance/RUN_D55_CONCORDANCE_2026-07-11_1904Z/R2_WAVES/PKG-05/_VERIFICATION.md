# W2 (PKG-05) — wave-local verification record

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; R2 Wave 2, PKG-05
  (DEL-05-01..05).
- **Roster (Receipt 18 steer):** five `opus` discovery agents; fan-in by
  `fable` at high effort (package-scoped, read-only); verdicts composed here
  by the fable orchestrator. Refutations returned to owning agents; owners
  re-verified independently before editing. One deterministic-validation
  vocabulary error (DEL-05-01 UNMAPPED-2 Disposition `IMPLEMENTED_UNMAPPED`,
  a ClaimType not a §7 disposition) was owner-fixed to
  `IMPLEMENTED_UNDOCUMENTED` before fan-in.
- **Source state:** frontend/ at `fac46e33f` = HEAD byte-identical.

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## 1. Deterministic structural validation

Final pass: 0 errors / 0 warnings; 116 rows (28+25+24+18+21). DEL-05-02 grew
by one row at fan-in (ACC-002 added by its owner — see §2).

## 2. Fan-in recheck outcomes (39 rows rechecked)

| Deliverable | Rechecked | Confirmed | Refuted → resolution | Contested |
|---|---|---|---|---|
| DEL-05-01 | 6 | 3 | R009 → **ALIGNED**, ACC-004 → **ALIGNED**, R013 → **PARTIALLY_IMPLEMENTED**. One root cause: ACCEPTED_DIVERGENCE used without a permitting human decision — D-APP-41's "does not authorize…" clause is a withheld authorization, not a §7 permission (R013 additionally carried LatestDecision NONE_FOUND). Owner re-verified the ruling text and accepted all three; R013 keeps a session-metadata redaction-test residual (Spec Verification line 65). | 0 |
| DEL-05-02 | 8 | 8 | — (notes correction: the posed R3 check on `turn.cancelled` persistence is already answered — turn-engine.ts:327-353 persists it durably on the live cancel path; owner strengthened RQ-007, withdrew that self-flag, and added ACC-002 STALE_SPECIFICATION for the flat now-false Datasheet/Guidance event names, verifying the RATIFIED corpus already carries the provider-neutral names — kit-only staleness). | 0 |
| DEL-05-03 | 13 | 13 | — (load-bearing R3 "configured secret variants" reading upheld: the kit's own R12 keeps the configured-secret schema TBD by requirement, so no class exists yet for "variants" to reach; a PARTIAL would double-count the registry gap already at R12 + gated REMAINING-1). | 0 |
| DEL-05-04 | 4 | 4 | — (REQ-013 STALE_SPECIFICATION upheld against the ACCEPTED_DIVERGENCE flip: D-APP-48 authorizes the pinned-pull mechanism, not the kit's false path text; notes correction: the Section 9 runner DOES have gate coverage via validate-harness-section9.test.ts — owner strengthened REQ-010 with the precision that the gate binds manifest/runner content, not runner execution). | 0 |
| DEL-05-05 | 8 | 8 | — (REMAINING-1 is the package's §7-clean ACCEPTED_DIVERGENCE exemplar: D-APP-42 explicitly logs Option C as "a deferred future enhancement — not a correctness gap"). | 0 |

Net: 39 rechecked — 36 confirmed, 3 refuted (all accepted), 0 contested.
Final census: 116 rows — ALIGNED 93, PARTIALLY_IMPLEMENTED 8,
IMPLEMENTED_UNDOCUMENTED 5, STALE_SPECIFICATION 4,
REMAINING_STATE_MISMATCH 5, ACCEPTED_DIVERGENCE 1.

## 3. Cross-checks and R3 flags

1. **ACCEPTED_DIVERGENCE discipline (package lesson, wave-wide rule):** valid
   only on an affirmative permitting decision (D-APP-42 pattern); withheld
   authorizations (D-APP-41 pattern) do not qualify. Same rule drove PKG-03's
   REQ-008 flip the other way (D-APP-18's "accepted by this ruling" text IS
   affirmative).
2. **One underlying medium-preview/withheld gap**, not two: DEL-05-03 R13
   (verification side) and DEL-05-05 REQ-004/010/014 (owning policy side)
   agree and cross-reference; DEL-05-05 owns the eventual decision packet.
3. `session-events.ts` claimed by four siblings compatibly (distinct facets,
   cross-acknowledged exclusions).
4. D-APP-48 relocation handled at three severities (05-04 kit-normative path
   → STALE_SPECIFICATION; 05-05 citation → R5 note; 05-01/02 assessment
   pointers → noted). One R5 tranche can sweep all PKG-05 D-APP-48 path
   references.
5. DEL-05-02 REGISTER-1 belongs to the Declared-TBD register class under the
   **cross-package inter-verifier conflict recorded in
   `R2_WAVES/PKG-03/_VERIFICATION.md` §3.5** — stands pending R3
   harmonization. REGISTER-2 (retired-row count lag) is unaffected.
6. Register-defect de-minimis bar is inconsistent across siblings (05-01
   treated cosmetic label lag as non-defect; 05-05 emitted REGISTER-1 for a
   comparable lag) — harmonize at R3.
7. Cross-package handles: `/api/harness/session/[id]/events` route ownership
   (with DEL-03-03 UNMAPPED-1); DEL-05-01 UNMAPPED-2 instruction-root guard
   (PKG-03?); DEL-05-05 UNMAPPED-1 child-output artifacts (PKG-08, W3);
   DEL-05-03 UNMAPPED-1 domain-proposal hygiene (D-APP-52 lane).
