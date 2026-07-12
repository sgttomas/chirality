# R2 Wave-2 notes — DEL-03-02 Thin TurnEngine and Session Locking (PKG-03)

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source-state binding: `frontend/` at
`fac46e33f`, verified byte-identical through current HEAD `1625b396a` (`git diff
fac46e33f HEAD -- frontend` empty). All line anchors were re-read against the
live tree; INSP-03 (reviewed SHA `0e1ba9a1e`, 2026-06-20) line ranges drifted and
were re-derived. Requirement set re-derived from `Specification.md` (12 REQ-IDs,
matching the R1 REQUIREMENT_INDEX 12-ID checklist; no parser gap for this
deliverable).

## Census

- Total rows: 19
- By ClaimType: REQUIREMENT 12, EXCLUSION 4, REMAINING_WORK 1, REGISTER_DEFECT 2
- By Disposition: ALIGNED 15, PARTIALLY_IMPLEMENTED 2, REMAINING_STATE_MISMATCH 2
- AssessmentEvidence token distribution: STILL CURRENT 8, OVERTAKEN 2 (REQ-005,
  REQ-011), NOT APPLICABLE 6; each row carries exactly one token.
- SelectableUnderCurrentLoop=YES: only REM-001 (the concordance bootstrap).

## Scope / method notes (deviations and judgment calls)

- **No ACCEPTANCE rows emitted (MR-4).** Unlike sibling DEL-03-04, DEL-03-02's
  Datasheet "Conditions" table holds constraints/context (Source-state status,
  Route compatibility, Event separation, Session storage, Settings isolation,
  Implementation sequencing) that restate REQ rows rather than distinct
  acceptance scenarios; they were folded into the covering REQ rows. The one
  genuinely distinct condition — "Settings isolation" (shipped builds use SDK
  `settingSources: []`, K-SDK-1) — is context owned outside DEL-03-02 (SDK
  options / K-SDK deliverable); verified consistent anyway
  (`frontend/src/lib/harness/sdk-options-builder.ts:23-25`, default `[]`), so no
  ACC row was fabricated for a condition this deliverable does not own.
- **No IMPLEMENTED_UNMAPPED rows.** Material behaviors on the DEL-03-02 surface
  (`turn-engine.ts`) all map: attachment binding/warning-injection → REQ-006;
  unknown-tool rejection → REQ-012; locking → REQ-004/005; accepted/terminal
  persistence → REQ-008/009. Subagent-governance threading
  (`turn-engine.ts:277-289`) is documented DEL-08-04 (PKG-08) behavior physically
  located in the shared file — a cross-surface R3 observation, not an unmapped
  behavior. The sibling's UNMAPPED-1/2 (interrupt-time permission clear; additive
  event vocabulary) sit on the interrupt/adapter surface (DEL-03-04) and are not
  duplicated here.
- **`_REFERENCES.md` is current, not a defect.** Live SHA-256 of all six corpus
  docs (`docs/DIRECTIVE|CONTRACT|SPEC|TYPES|PLAN|PRD.md`) matches the Expected
  hashes recorded in `_REFERENCES.md` at `fac46e33f` (v6 corpus). No register row.
- **Register defects (MR-5):** REGISTER-1 (Dependencies.csv satisfaction
  metadata frozen at 2026-05-20 PENDING/TBD despite live upstream targets and a
  logged 2026-06-21 ADQ-05 run); REGISTER-2 (`_DEPENDENCIES.md` "Declared
  Upstream/Downstream: TBD — no edges extracted yet" contradicts its own 10-row
  Extracted Register + Dependencies.csv). Both REMAINING_STATE_MISMATCH,
  documentary/metadata-lag, no behavioral impact.

## Least-confident rows (self-flagged — fan-in should recheck these plus all
## non-ALIGNED rows)

1. **REQ-003 (ALIGNED, MEDIUM).** Alternative reading that would flip it:
   `Specification.md` REQ-003 lists "session lock acquisition" as a *route*
   responsibility, but the lock is now acquired inside `TurnEngine.runTurn`
   (`turn-engine.ts:220-229`), invoked by the route. A strict reading makes this
   IMPLEMENTED_DIFFERENTLY (or STALE_SPECIFICATION on the enumeration). Kept
   ALIGNED because the requirement's substance (thin route, lifecycle in engine)
   is fully met and the engine-side lock is corroborated by REQ-004/005 and
   DEL-03-04 EXC-002; logged only as an optional R5 doc-wording refresh.

2. **REQ-008 (ALIGNED, MEDIUM).** Alternative reading: INSP-03 rated this PARTIAL
   because accepted-turn persistence is adapter-owned (`turn.accepted` in
   `claude-agent-sdk-manager.ts:229-245`), not centralized in `TurnEngine` (which
   owns only `message.accepted` at `turn-engine.ts:301-312`). If the requirement
   is read as demanding TurnEngine ownership, this is PARTIALLY_IMPLEMENTED. Kept
   ALIGNED because REQ-008's wording only requires the accepted event to persist
   *before execution*, which both events do (proven by the engine-conformance
   replay ordering). The ownership question is surfaced as a NEW-PACKET decision,
   not a requirement failure.

3. **REQ-011 (ALIGNED, HIGH — corrected at fan-in).** Originally filed
   PARTIALLY_IMPLEMENTED on the claim that no dedicated legacy-session-format
   readability test existed at this slice; the fan-in verifier REFUTED that and
   re-verification confirms it was factually wrong: `session-manager.test.ts`
   'migrates legacy flat records to canonical folders on resume'
   (`frontend/src/__tests__/lib/session-manager.test.ts:72-104`) writes a legacy
   flat record and proves `FileSessionManager.resume` reads it, preserving
   `claudeSessionId`/`sdkTranscriptPath`/unknown extra fields — and `resume` is
   exactly the path TurnEngine uses (`turn-engine.ts:202`). Row flipped to
   ALIGNED with the INSP-03 PARTIAL marked OVERTAKEN (canonical-folder migration
   has since landed). Original discovery error: the test search covered only
   turn-engine/routes test files, not `session-manager.test.ts`.

4. **REQ-002 (PARTIALLY_IMPLEMENTED, MEDIUM).** Genuine named-port binding gap
   (TurnEngine depends on `IAgentSdkManager`, not the named `AgentEnginePort`).
   Alternative reading: if `IAgentSdkManager` is accepted as *the* product-owned
   port (the conformance suite already enforces SDK-name isolation), this is
   ALIGNED. Left as PARTIALLY_IMPLEMENTED with a NEW-PACKET because the named
   `AgentEnginePort`/`RuntimeEngineContract` type exists in the pinned
   harness-contract package yet is unused by TurnEngine.

5. **REQ-009 (PARTIALLY_IMPLEMENTED, HIGH).** High-confidence on the stub-path
   gap itself (grep confirms `agent-sdk-manager.ts` has no `appendHarnessEvent`);
   flagged only because the corrective NEW-PACKET is the *same* bounded stub
   terminal-persistence choice already raised at DEL-03-04-REQ-006 — R3/R4 must
   treat these as one packet, not two.

## Cross-reference / dependency duties discharged

- Re-verified the five EXECUTION dependency edges against the live tree: DEL-03-01
  (AgentEnginePort, harness-contract package present), DEL-05-02 (session-events
  JSONL writer present), DEL-03-03 (SSE compat), DEL-03-04 (interrupt/terminal —
  its R0 rows own that mapping), DEL-09-03 (test expansion). Satisfaction is real
  in the tree but the local register does not reflect it → REGISTER-1.
- MR-7 LatestDecision calls: D-APP-40 governs REQ-009 (terminal taxonomy incl.
  `turn.interrupted`); D-APP-40 (context) on REQ-005/EXC-002; D-APP-48 (context)
  on REQ-007/010 (harness-contract relocation); D-APP-25 (context) on REQ-008
  (manager-lifecycle bridging of `turn.accepted`); D-APP-53 (context) on
  REGISTER-1; D-APP-55 governs REM-001. No D-APP ruling directly governs the
  REQ-002 named-port gap or the REQ-008 ownership question → both NEW-PACKET.

## No agent-workflow (DEFERRED_AGENT_WORKFLOW) rows

Nothing in DEL-03-02's surface required judging an agent instruction, matrix, or
skill contract. `REF-007` points at `agents/AGENT_SOFTWARE_DECOMP.md` (frozen
process input, read-only), used only as decomposition-method provenance.
