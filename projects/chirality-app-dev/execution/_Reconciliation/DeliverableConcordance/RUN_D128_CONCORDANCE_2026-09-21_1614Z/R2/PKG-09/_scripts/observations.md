## 8. OWNER_CHECK candidates (RUN_BASIS Addendum 10; hand-written)

Addendum 10 (owner direction: "a lack of evidence is not evidence of lack") arrived after every PKG-09 ledger
had sealed and every verifier shard had returned, so no row carries `OWNER_CHECK:` and no verifier graded
against it. Sealed ledgers are not edited. The rows below have a non-ALIGNED verdict that rests wholly or partly
on the absence, inside the evidence roots, of a record of an out-of-code event. Under Addendum 10 their
event-dependent part would be `UNKNOWN` pending the owner's answer; code-presence parts of the same rows stand.
Screened by `_scripts/owner_check_scan.py` (keyword screen, 99 hits) and curated by hand. The owner has already
stated that **v3.0.1 was notarized, as v3.0.0 was**, which answers the notarization half of the first group.

| Row(s) | Sealed Disposition | OWNER_CHECK question |
|---|---|---|
| DEL-09-04#CLM-005, #CLM-011.1, #CLM-011.2, #CLM-011.3, #CLM-011.7, #CLM-012.1, #CLM-018 | PARTIALLY_IMPLEMENTED | Was a `desktop:dist` build of the current version (3.0.1) produced, signed and notarized, and where is its build record (transcript, DMG checksum, integrity summary)? |
| DEL-09-04#CLM-011.5 | PARTIALLY_IMPLEMENTED | Was the candidate bundle's binary architecture (arm64) inspected for 3.0.0 or 3.0.1? |
| DEL-09-04#CLM-009.8, #CLM-011.8 | PARTIALLY_IMPLEMENTED | Was the packaged App run so that the Runtime service spawned the pinned `codex app-server`, with secret and network checks, for 3.0.0 or 3.0.1? |
| DEL-09-04#CLM-017 | PARTIALLY_IMPLEMENTED | Was a packaged network-guardrail check run for the Codex-engine build? (Code part stands: the proof scripts target `api.anthropic.com`.) |
| DEL-09-04#REM-1 | REMAINING_STATE_MISMATCH | Was the V3-01 Return (offline network-denied package evidence, nested signature inventory) produced for the landed package? |
| DEL-09-05#CLM-010.8 | PARTIALLY_IMPLEMENTED | Did the full K-VALIDATE-1 set, including `desktop:dist`, pass before release-significant acceptance of 3.0.0/3.0.1? |
| DEL-09-05#CLM-010.9, #CLM-010.15 | PARTIALLY_IMPLEMENTED | Was a secret-redaction and network-scope inspection run over the v3 CI logs, the 2026-09-12 build record or the packaged App? (Code part stands: the scanner does not cover Codex/OAuth material.) |
| DEL-09-05#CLM-016.5 | DOCUMENTED_UNIMPLEMENTED | Was the ten-step CI review, the manual checklist or a requirement-to-evidence matrix carried out anywhere outside the deliverable? |
| DEL-09-05#CLM-016.6, #CLM-021, #CLM-022, #CLM-023.1 | PARTIALLY_IMPLEMENTED | Was the WP-11/V3-05 release execution (and VER-001 against the executed workflow) performed and recorded for 3.0.0/3.0.1, and where? |
| DEL-09-05#CLM-016.3, #CLM-026; DEL-09-04#CLM-022, #CLM-023.3 | AUTHORITY_CONFLICT | Which act, if any, was the owner's release act for the published 3.0.0/3.0.1 DMG (done-declaration Q-02)? The authority question itself stays with R3/R4. |
| DEL-09-01#CLM-011, #CLM-009.8, #REM-1 | PARTIALLY_IMPLEMENTED / REMAINING_STATE_MISMATCH | Has a Section 8 premerge run passed against the Codex-hosted Runtime since the re-platform (repository-root CI or local)? |
| DEL-09-02#CLM-020.2 | PARTIALLY_IMPLEMENTED | Has a premerge run with the full 16-ID Section 9 manifest been executed and its summary kept? |
| DEL-09-06#CLM-016, #CLM-021 | PARTIALLY_IMPLEMENTED | Was a packaged security/network proof run after the A2 (Codex-hosted) topology landed? (Code part stands: the proofs are legacy-provider shaped.) |
| DEL-09-06#CLM-014 | PARTIALLY_IMPLEMENTED | Was a packaged built-in PDF proof run? (Legacy-only code parts stand.) |

## 9. Cross-package observations for R3 (hand-written; evidence, not rulings)

1. **The v3 release happened in the records, not in the deliverables.** AgentRuns records (read in root) show a
   Developer ID-signed 3.0.0-rc.1 build on 2026-09-12 and a signed, notarized, published 3.0.0 on 2026-09-13; the
   owner states 3.0.1 was notarized too. Every PKG-09 SoW still describes an unsigned/unnotarized target, a
   Claude/Anthropic engine or the retired LaunchAgent/two-job topology, and D-APP-127 reached only `_STATUS.md`
   (DEL-09-03..07) or no carrier at all (DEL-09-01, 09-02). This is the same CARRIER_PROPAGATION pattern R0 §8.6
   found, now on the release surface.
2. **Release-signing posture needs one R3 cluster.** Four rows split between STALE_SPECIFICATION (MR-11 via the
   amended CONTRACT preamble naming K-RELEASE-1) and AUTHORITY_CONFLICT (unamended K-RELEASE-1 row text, PRD §6.2,
   D-APP-97's F-APP-2 fence); see VERIFICATION §5.1. The G6a gate (DEL-09-05 CLM-016.3 vs REGISTER-52) belongs
   in the same cluster. Done-declaration Q-02 is the CONTEXT for both.
3. **Validation proves the legacy harness, not the shipped path.** DEL-09-01's Section 8 and DEL-09-02's 16
   Section 9 IDs run against the retained in-process Claude-SDK harness (`controlled-ci-runtime.ts` imports the
   legacy stub engine); none exercises `projects/chirality-runtime`. DEL-09-03's route tests reach live routes
   through a test-only fake port fed by legacy events. This bears on R4-Q1 and R4-Q2 and on any claim that
   validation evidence covers v3.
4. **Build/validation script reach needs a rule.** R1b tags validation and `proof:*` scripts TEST_ONLY; PKG-09
   workers mostly tagged them LIVE (package.json entry). R3 should fix one reading before scripting R4-Q1 from
   REACH tags (VERIFICATION §5.3).
5. **R4-Q6 reaches PKG-09** through K-PERM-1 hard-deny precedence in DEL-09-03 (CLM-005.8, 009.9, 011, 017, 023)
   and DEL-09-02_A CLM-010.6 (sealed before Addendum 9; maps).
6. **Double-blind (DEL-09-02).** Disposition agreement 23/29 (79%) against DEL-05-02 24/33 and DEL-06-02 19/35;
   no pure STALE_SPECIFICATION/REMAINING_STATE_MISMATCH splits (the Addendum 5 tie-break held). HumanDecisionNeeded
   agreed on 24/29 keys, but where either worker cited an R4 token the token sets agreed on only 1/6, all on
   R4-Q1: rows about validation *scope* met by live scripts that exercise legacy harness modules still split under
   the Addendum 6/8 subject test.

### Coverage gaps (indexed scope or SoW text with no forward row a worker could own)

- DEL-09-07: decomposition SOW-080, OI-003/OI-007 still list the retired installer (outside the preserved set;
  for the EXT `SOW:SOW-080` unit).
- DEL-09-04: unindexed SoW OUT-001 (line 22) and the frontmatter decomposition pin; BUILD capabilities
  CAP-BUILD-001/002 (Next/Electron build before packaging) and CAP-BUILD-010 (Electron fuses) have no owning row.
- DEL-09-05: unindexed Purpose OUT-001 (recorded as STATE-1) and the Output and Evaluation Matrix, which still
  carries the G6a premise; the out-of-root desktop-release workflow's retired LaunchAgent proof steps have no carrier.
- DEL-09-01 / DEL-09-05: nothing owns retiring or replacing `frontend/scripts/controlled-ci-runtime.ts`
  (LEGACY_ONLY; recorded as broken against the A2 core).
- DEL-09-02: no Section 9 ID covers the live Runtime surfaces (event journal/replay, application tools, Codex
  notification pass-through, native child tracking, effective Codex home).
- DEL-09-03: `routes.test.ts:1270` still expects a stream disconnect to cancel the turn, contrary to amended SPEC
  §11; no row owns fixing or retiring it.
