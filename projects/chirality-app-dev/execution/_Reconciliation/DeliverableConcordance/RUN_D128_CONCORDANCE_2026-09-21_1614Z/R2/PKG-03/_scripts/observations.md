## 7. Cross-package observations for R3 (hand-written by the PKG-03 manager; evidence, not rulings)

1. **Event-contract conflict is corpus-wide and needs framing.** Every PKG-03 ledger records the same
   GOVERNING tension: amended K-EVENT-1/6, SPEC §11 and TYPES §7.4 (preserve upstream Codex methods and
   payloads, which the live Codex adapter does) against unamended K-ENGINE-4, SPEC §10.3 and TYPES §7.1
   (translate; no provider-shaped events). 15 AUTHORITY_CONFLICT rows here carry plain `R4`, because no
   named question fits. The same tension appears in R0 §8 item 3 (DEL-03-01) and PKG-06 wave 1
   (DEL-06-06). Verifiers keep it CONTESTED on DEL-03-01 because D-APP-127 names the deliverable and could
   carry MR-11. A named R4 question would let R3 cluster these rows consistently.
2. **R4-Q2 is concentrated in DEL-03-01** (14 of 15 rows): the K-ENGINE-2 conformance suite has run only
   against scripted stub and Claude SDK subjects, and the Codex engine (production default) never. Its
   V3-01 Remaining item (REM-2) is REMAINING_STATE_MISMATCH with MechanicallyUnblocked `YES`: the gate is
   met in App code at the frozen basis, yet `_STATUS.md` still marks the item not selectable. DEL-03-03
   V3-01 (transport repair) is in the same state: the repair landed in live code but is recorded as not
   selectable.
3. **The turn lifecycle moved to the Runtime service; the SoWs did not.** DEL-03-02 and DEL-03-04 find the
   live lock, turn persistence, interrupt and terminal handling in the Runtime `TurnCoordinator` /
   `TurnRegistry`, reached from `electron/main.ts` through the App-owned composition; the App
   `turn-engine.ts` is reached by nothing (LEGACY_ONLY, UNREACHED). Unamended SPEC §10.4 still says the
   route takes the lock and forwards to TurnEngine, and the package grades it three different ways
   (VERIFICATION §4 item 2). R3 should treat SPEC §10.4 once, under the Addendum 6 subject test.
4. **Carrier propagation is uniform.** In all four deliverables D-APP-127/D-GOV-43 reached `_STATUS.md`
   only; `ScopeOfWork.md`, `_CONTEXT.md`, `Dependencies.csv` and `_REFERENCES.md` are unrevised (pack item
   5). DEL-03-01's SoW was recorded by SCA-APP-005 as `FROZEN_STALE_REPAIR_REQUIRED` and never rewritten.
   STALE_SPECIFICATION is the largest Disposition (109 of 285 rows), and CARRIER_PROPAGATION is the most
   common `CAUSE2:` secondary (32). All 12 `_REFERENCES.md` MATCH hashes fail to reproduce (one
   REGISTER row per deliverable).
5. **Live-path secret redaction gap (candidate cross-package finding).** DEL-03-01 CLM-018.7 and DEL-03-04
   CLM-004.6 / CLM-009.13 find no structural redaction of secrets before canonical events are persisted or
   streamed on the live Runtime path, as amended K-EVENT-6 requires. The only redaction found is stderr
   redaction in the Codex app-server client. The reverse pass found no capability for it in any
   surface file. This is relevant to the event-store and credential-custody deliverables in other packages.
6. **Unlisted live routes.** Turn re-attach and turn state (CAP-ROUTES-008/009) are live, but appear in
   neither the DEL-03-03 SoW nor the SPEC §17.1 route catalog; they are covered only through DEL-03-03
   REM-1 (coverage gap recorded in reverse notes, not an erratum).
7. **Ownership overlaps.** CAP-ROUTES-007 (turn route) is CLAIMED_BY both DEL-03-02 and DEL-03-03, and 20
   capabilities are claimed or partly covered by more than one PKG-03 deliverable (mostly Runtime lock,
   persistence and turn-state behaviour). The shutdown-settles-as-`turn.interrupted` behaviour
   (CAP-RTCORE-018, DEL-03-04) conflicts with D-APP-40's reservation of `turn.cancelled` for system
   cancellation (DEL-03-04 CLM-009.7, R4).
8. **Convention friction for R3.** (a) The tie-break (Addendum 5) still leaves dated history notes open
   (VERIFICATION §4 item 3). (b) Workers cited the deliverable's own `_STATUS.md` as `CTX:`, but RUN_BASIS
   §5 classes it as declared state (5 corrections). (c) A SoW that declares its own older clauses
   "compatibility history" under a GOVERNING SCA makes ACCEPTED_DIVERGENCE and IMPLEMENTED_DIFFERENTLY
   both available (DEL-03-02 CLM-008). (d) All PKG-03 ledgers sealed before Addendum 6. R3's scripted
   re-derivation of R4-Q1 affects the 46 rows that mix LEGACY_ONLY and LIVE evidence.
