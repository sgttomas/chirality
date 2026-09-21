# V-DEL-10-03 — verifier shard notes (PKG-10, R2)

Unit: DEL-10-03. Basis: frozen tree at `00115c719`. Grading key: `BRIEFS/VERIFIER_BRIEF.md`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / AUTHORITY_CONFLICT / REMAINING_WORK) | 2 | 2 | 0 | 0 |
| a30 (30% of other non-ALIGNED) | 9 | 7 | 0 | 2 |
| b (15% of ALIGNED) | 4 | 4 | 0 | 0 |
| c (reverse PARTIAL) | 2 | 2 | 0 | 0 |
| e (errata) | 0 | — | — | — |
| **Total** | **17** | **15** | **0** | **2** |

Verdict-field refutations (Addendum 3): 0. No field-only refutations either.

## (ii) Patterns

1. **Future-boundary REQ rows measured against the live path.** The worker's two-axis measure
   (documentary artifact plus whether the forbidden outcome is reachable on the live Codex path)
   is applied consistently. It is the source of both CONTESTED items:
   - `CLM-003.2`: PARTIALLY_IMPLEMENTED || ALIGNED. PRD §8.17 (`docs/PRD.md:835`) keeps
     protected-path writes and hooks "future and gated", and REQ-10-03-008 is verified by a
     review checklist. The row's `R4-Q1` is also a weak fit: no retained-harness quarantine
     exists, so the retained-harness question does not decide it (NO, or plain R4 on D-GOV-43's
     no-pinning, are the alternatives).
   - `CLM-010.10`: STALE_SPECIFICATION || ALIGNED. REQ-10-03-010 says the artifacts stay TBD
     "until accepted", so it can be read as a rule that the adopted profiles and bound schema
     refs satisfy. The now-false TBD state text is carried separately by CLM-018 and CLM-005.
2. **Status-constancy finding (CLM-004 / CLM-011) holds.** Persona `@77a327727` lines 406–407
   say `proposal_only` covers only `draft` and `ready_for_review`. TYPES:641 makes it constant.
   DIRECTIVE §0 ranks TYPES above `agents/AGENT_*`, so the worker correctly rejected
   AUTHORITY_CONFLICT. The only false part is the SoW's conformance claim.
3. **Line anchors are exact or within 1–3 lines.** For example, `resolvePecTransportProfile`
   is at 137–150 against the cited 133–150, which includes its doc comment. Every date checked
   with `git blame` falls before 2026-08-22 (SoW 7bb70be83 2026-07-14; CONTRACT/TYPES
   fbd8e29fd 2026-06-21), which supports PRE_V3_DRIFT. The REGISTER-1 hashes blame to
   23b3879b3 (2026-09-12); DOC_HYGIENE is correct there. No cited path is in
   `TOUCHED_PATHS.csv`, so PostReleaseBasis = NO holds.
4. **Grading key 3.** `CLM-003.1` and `CLM-010.7` rely on `contracts/src/harness/*.ts` REACH=LIVE,
   taken from the module map. The RTCONTRACT capability notes say TEST_ONLY (no product consumer),
   and the worker notes the module is inert. Both are shape/future requirements, so the
   difference does not change the Disposition. Not contested.
5. **REM-1.** The gate is piping-side, so MechanicallyUnblocked `UNKNOWN` is correct (no App
   carrier). The D-APP-127 ruling does not name D-APP-50 or PKG-10, so MR-11 does not apply and
   AUTHORITY_CONFLICT + `R4-Q1` fits. PRD §8.17 still calls the pec tools "live" although they
   are LEGACY_ONLY, which is more support for R4-Q1.

## (iii) Effort

About 20 file reads or range reads: SoW, `_STATUS`, `_REFERENCES`, `Dependencies.csv`,
`_DEPENDENCIES.md`, TYPES/CONTRACT/PRD/DIRECTIVE ranges, the persona at `77a327727`, two contract
modules, two legacy MCP modules, the profile YAML, the D-APP-127 ruling, and evidence-pack CSVs.
There were also 6 read-only git blame/log calls. The context budget was not tight.
