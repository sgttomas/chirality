# V-DEL-06-01 — verifier shard notes (DEL-06-01)

Evidence-only verification against the frozen tree at `00115c719`, graded with the shared key in
`R2/PKG-06/BRIEFS/VERIFIER_BRIEF.md` and `CONVENTIONS.md`. The shard edited no ledger, worker or pack file.
Class `a` rows are graded on their errata-applied values: where an erratum already fixes a sealed
gloss, the defect is recorded once, on the class `e` line.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT, LOW/self-flag) | 13 | 7 | 4 | 2 |
| a30 (30% of other non-ALIGNED) | 13 | 10 | 0 | 3 |
| b (ALIGNED sample) | 2 | 1 | 0 | 1 |
| c (reverse) | 5 | 4 | 0 | 1 |
| e (errata) | 12 | 12 | 0 | 0 |
| **Total** | **45** | **34** | **4** | **7** |

SELECTION has 45 items for this shard: 12 errata items, plus 33 in the other classes.

## (ii) Systematic patterns

1. **Truncated `delegated.ts` gloss with no REACH tag** (REFUTED on ImplementationEvidence: CLM-009.4,
   CLM-009.8, CLM-025).
   - The worker's template text `policySelectionFromPermissionMode (readOnly->on-request/read-only` was
     cut off mid-parenthesis. When it is the last entry in the cell (009.4, 025), or is followed only by a
     LEGACY_ONLY entry (009.8), the LIVE path is left untagged. In 009.8 it even reads as sharing the
     LEGACY_ONLY tag.
   - The same fragment appears inside the cells of CLM-009.5, 009.11 and 024. There a following entry's
     `REACH=LIVE` covers it, so it was not refuted.
   - The errata for 009.4 and 025 carry the defect forward.
2. **The AUTHORITY_CONFLICT family is mostly sound.**
   - D-GOV-43 item 4 (`D-GOV-43.proposed.md:187-195`, adopted verbatim by the ruling) makes approval and
     sandbox the user's choice and expressly allows Full access. The unamended App CONTRACT
     K-PERM-1..6 and SPEC §15.1/§15.2 are not named by it. So bypass-bearing rows (CLM-004, 009.9, 027,
     031) and overlay/Chirality-owned-policy rows (CLM-003, 009.3, 009.4, 024, 025) hold.
   - R4-Q1 fits, because the CONTRACT enforcement column assigns K-PERM to the retained permission
     overlay and options builder.
   - **CONTESTED:** CLM-009.5 (readOnly) and CLM-009.6 (dontAsk). The divergence comes from Chirality's
     own fixed mapping in `delegated.ts:322-331` (readOnly → on-request; legacy dontAsk → readOnly, which
     prompts). The ruling does not force it: approval `never` with a read-only sandbox would satisfy
     K-PERM-4/5 under D-GOV-43. So IMPLEMENTED_DIFFERENTLY or DOCUMENTED_UNIMPLEMENTED is an equally
     available reading.
   - For dontAsk, the App CONTRACT's Codex-only preamble (line 17) calling SDK-specific wording
     compatibility history adds a possible DIRECTIVE §0 resolution.
3. **MR-8 (iv) on the dated REF-006 note.**
   - CLM-001 and its SEE rows CLM-007 and CLM-023 are graded CONTESTED. The "D-APP-56 R5 P40
     current-state note (2026-07-12)" is dated and was true of that snapshot, and the row's own Notes cite
     MR-8 (iv). Yet the row takes STALE_SPECIFICATION rather than register-class
     REMAINING_STATE_MISMATCH.
   - The undated MATCH tables (CLM-006, CLM-033) and REGISTER-1 are correctly STALE_SPECIFICATION.
4. **Missed register row.**
   - For CLM-034.1, DirectionEvidence `NONE_FOUND` is REFUTED. `_REGISTER.md:104` D-APP-89 (RULED
     2026-08-02, Option B) governs exactly the deprecated `@chirality/harness-contract` facade and keeps
     it as tested rollback.
   - This also makes ALIGNED at module level a live alternative to STALE_SPECIFICATION.
5. **The errata are correct.**
   - The runtime-tool-list discard is verified: `delegated-engine-adapter.ts:231` passes `[]`, and
     `DelegatedRuntime.turn` ignores `_runtimeTools` (`delegated-runtime.ts:289`).
   - The legacy `dontAsk` → `readOnly` mapping is verified (`runtime-daemon-harness-port.ts:205-207`,
     LIVE).
   - Minor additions that do not change a verdict:
     - Host-side application dynamic tools (codex-supervisor `item/tool/call`) are also live, which makes
       "governed only by sandbox/approval" approximate.
     - "TYPES §12 PolicySelection" is correct for Root TYPES. In App TYPES the term sits under the
       duplicated second "§13 Shared Runtime Vocabulary" (line 728).
6. **Other contested items.**
   - Class `b`, CLM-022.2 (VER-001) is CONTESTED: ALIGNED at module level, or STALE_VERIFICATION because
     it verifies DEL-06-01's requirements only through a LEGACY_ONLY module (grading key 3). The row also
     carries R4-Q1 on an ALIGNED row.
   - Class `c`, CAP-RTCONTRACT-019 is CONTESTED between CLM-004 and CLM-027 ("Mode Mapping").

Line anchors were checked at the frozen tree. The drifts found are within 1–2 lines, which is immaterial:
`delegated.ts:320-330` is at 322-331, `turn-coordinator.ts:289` is at 290, and `runtime-method-service.ts:509` is at 510.
PostReleaseBasis NO on CLM-009.2 was confirmed with `git blame -L 718,731`: the lines blame to
95364569a, 0ed1a1a7f and 2f825f180. Touched ranges in `codex-supervisor.ts` end at 695.

## (iii) Effort

About 30 file reads or greps on the frozen tree covered:

- the deliverable SoW and `_REFERENCES.md`;
- CONTRACT §1.6 and the preamble, SPEC §14.3/§15, and App and Root TYPES;
- the D-GOV-43 ruling and its proposal item 4, and the register row for D-APP-89;
- the runtime sources: `delegated.ts`, `delegated-runtime`, `delegated-engine-adapter`,
  `runtime-method-service`, `turn-coordinator`, `runtime-service`, `codex-supervisor` and
  `application-tools`;
- the App sources: `chat-panel`, `permission-requests`, the permission route, `request-card`,
  `server-request-answer`, `runtime-daemon-harness-port`, `permission-overlay`,
  `sdk-options-builder` and the facade;
- three test files.

Git was used once, read-only (`blame -L`). The context budget was adequate.
