## §8 Cross-package observations for R3 (hand-written by the PKG-02 manager; evidence, not rulings)

**Reading the figures.** No errata were filed, so sealed = errata-applied everywhere.
`CORRECTIONS.csv` holds 5 non-verdict rows (Notes, DirectionEvidence, LatestDecision); none is a census
field, so the corrected figures in §2 equal the sealed ones. The 4 verdict-field refutations are
not applied to any census, because Addendum 3 does not route them into a file. They are:
- DEL-02-01 CLM-017 (ACCEPTED_DIVERGENCE → IMPLEMENTED_DIFFERENTLY + R4-Q4);
- DEL-02-01 CLM-023.2 (→ ALIGNED; the manager treats this as CONTESTED because the evidence sits in Root
  `execution/**`, outside the RUN_BASIS §3 roots; VERIFICATION §4);
- DEL-02-04 CLM-003.4 and CLM-005.5 (DOCUMENTED_UNIMPLEMENTED → PARTIALLY_IMPLEMENTED).
R3 should apply them when it clusters.

1. **The v3 four-role adoption (`9b005c23a`) is PKG-02's dominant unruled change (R4-Q4: 53 rows).**
   - The commit removed the 3×4 agent matrix, the PORTAL/loop-first shell and the composer
     delegation/rung fields, and left Workbench/Pipeline as imports that are never rendered.
   - The texts that still keep these surfaces were not amended: App TYPES §4, PRD FR-001/FR-007,
     DIRECTIVE §4.1, D-APP-74 ("until separately retired"), SPEC §7/§13.
   - Only D-APP-108 Q3 (the Workbench/Pipeline unmount) is a governing retirement. DEL-02-02 relied on it
     for 25 `RETIRED_BY_RULING` rows, and the verifier confirmed them, with one caveat: the D-APP-108
     record never names DEL-02-02, and PRD FR-011/FR-012 (P0) are unamended.
   - Workers coined `OTHER:V3_ROLE_ADOPTION`: 35 rows in DEL-02-01, and 2 more in DEL-02-05 as
     `OTHER:V3_FOUR_ROLE_ADOPTION` for the same mechanism.
   - Proposal for R3: normalise both to one vocabulary tag paired with R4-Q4. Other packages touched by
     the role adoption (PKG-07/08 persona and matrix) may show the same.
2. **Split-halves divergence on DEL-02-01 is a reproducibility signal.**
   - Half B rated as `ACCEPTED_DIVERGENCE` (CLM-017, CLM-020.1/.3/.4/.5/.8, CLM-025) what half A rated
     as R4-Q4 divergence on the same evidence.
   - The verifier backed half A. R3 should re-examine the unsampled half-B rows under MR-8.
3. **Module-LIVE / symbol-unreached and the not-found page.**
   - Every route renders only `WovenDialogueShell`, and `void legacy` discards the older shells.
   - `app/not-found.tsx` still renders the legacy shell: the Toolkit panel, the API-key panel, the
     working-root bar and the deliverables list. It is therefore the only product path to several
     "retained" UIs.
   - This bears on any package citing those components as LIVE: DEL-04-xx provider UI, and DEL-07-03
     scope scan.
4. **Anthropic API-key UI: AUTHORITY_CONFLICT confirmed under DIRECTIVE §0 (DEL-02-05, 15 rows, plain
   `R4`).**
   - The App DIRECTIVE §2.8/§4.1 was never amended for D-GOV-43, and it outranks the Codex-only
     preambles.
   - This candidate for a named question recurs across PKG-02 and PKG-04 (DEL-04-05) and R0 §8.9. A
     single owner ruling (amend DIRECTIVE §2.8/§4.1, or retire the key UI) would resolve the cluster.
5. **R4-Q5 in UI deliverables.** DEL-02-05 has 7 R4-Q5 rows and DEL-02-02 has 1. They concern the UI's
   SSE event names (`turn:error`, `process:exit`). Verifiers CONTESTED all four sampled rows
   (AUTHORITY_CONFLICT || STALE_SPECIFICATION), so the question reaches beyond PKG-03/05.
6. **D-APP-127 carrier propagation.** Every PKG-02 carrier is `Revised = NO` except DEL-02-05 `_STATUS.md`
   (pack item 5). The live Codex account surface (`HostedBootstrapView`, runtime `codex-login.ts`)
   has no current SoW requirement anywhere in PKG-02.
7. **Reference hashes.** All 15 `_REFERENCES.md` MATCH verdicts are stale (REGISTER rows in every
   ledger). This matches the corpus-wide DOC_HYGIENE cluster.
8. **Coverage gaps (indexed work with no forward row the worker could own; from notes §5 and
   reverse_notes).**
   - **DEL-02-01:**
     - runtime connectivity/reconnect control (CAP-SHELL-010/011; `_STATUS` history records it as
       DEL-02-01 work);
     - theme control;
     - chat continuity and new-chat/resume;
     - the SoW OUT-001 line and SCA preambles, which are unindexed;
     - an internal contradiction: CLM-007/014 say UPD-106 is "implemented", CLM-023 says "withheld".
   - **DEL-02-02:**
     - the v3 method library and workflow-draft registration (live in the Workflows tab; owner
       probably DEL-07-03, DEL-08-02 or Runtime);
     - composer role picker ownership (vs DEL-02-05 and DEL-08-04);
     - Plan tab;
     - recorded-session panel menu;
     - composer workflow selection;
     - skills browsing;
     - Navigator surface groups;
     - a capability-file error: CAP-ROUTES-042 says `/pipeline` and `/workbench` open a named surface,
       but they render the dialogue only.
   - **DEL-02-03:**
     - the document viewer and `/api/working-root/file`;
     - the right-panel view switcher and Quick Look;
     - ChatMarkdown/ANSI consumer (D-APP-70);
     - `selectDirectory` retention (D-APP-71);
     - per-chat folder features outside SOW-002;
     - `/api/working-root/scope`, which has no rendered consumer.
   - **DEL-02-04:**
     - workspace fields `chatIndex`, `foldersCollapsed`, `chatDocuments`, `lastActiveChat` and the
       `knownRoots` seed have no unit;
     - theme persistence appears only in the Remaining preamble;
     - toolkit storage warning;
     - SPEC §13.1 unknown-key warning ownership on the Runtime path (DEP-02-04-014 `TBD`);
     - fields with no producer (`chatRung`/`declined` → DEL-02-02-V3-04; `contextReferences`,
       `focusedArtifact`, `dialogueAnchorId` → DEL-02-03-V3-02);
     - `_SEMANTIC*`/`MEMORY.md` are unindexed.
   - **DEL-02-05:**
     - the live Codex account surface (only via REM-1 and retired REQ-001; sits between DEL-02-05 and
       DEL-04-05);
     - `preload.ts` coordination lead (D-APP-71);
     - attachment picker and chips (only via AC-002);
     - Settings Runtime and Agent-instructions groups;
     - `MEMORY.md` has no D-APP-127 entry;
     - `_STATUS.md:11` "command-network postures retired" versus amended K-NET-1.
   - Two capabilities are CLAIMED_BY two PKG-02 deliverables: CAP-ROUTES-042 (02-01, 02-02) and
     CAP-SHELL-035 (02-01, 02-03).
9. **Convention friction for R3.**
   - Numbered SCA Gate-5 acceptance-obligation lists and mixed attribute tables cannot be split under
     §2.2 (DEL-02-01 CLM-003/005, DEL-02-02 SEC-2/SEC-4).
   - The REGISTER_DEFECT verdict pair does not fit a duplicate-RefID collision (DEL-02-01 REGISTER-4).
   - MechanicallyUnblocked is undefined for untyped `Depends` lines or standing disciplines.
   - `STATE-n` is not allowed for a false sentence embedded in a REMAINING_WORK unit (DEL-02-02 REM-1,
     recorded as `ALSO:`).
