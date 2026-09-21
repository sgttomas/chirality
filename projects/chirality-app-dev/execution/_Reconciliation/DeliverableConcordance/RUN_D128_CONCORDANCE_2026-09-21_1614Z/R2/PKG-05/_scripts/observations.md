## 8. Cross-package observations for R3 (hand-written; evidence, not rulings)

1. **No redaction before persistence on the live path (all five deliverables).** The Runtime `session-store.ts` writes events —
   including `codex.notification` with raw upstream `params` and full tool output — to `events.jsonl` unredacted; the redaction and
   artifact-offload stack (`session-events.ts`, `run-logger.ts` `redactJsonLike`, `tool-result-artifacts.ts`) is LEGACY_ONLY. Amended
   CONTRACT K-EVENT-6 requires redaction before every sink. Surfaces in DEL-05-02 (RQ-009/010), 05-03 (redaction), 05-04 (replay
   redaction; `Dependencies.csv` DEP-05-04-008 still SATISFIED), 05-05 (tool-result store). No App carrier names the Runtime owner of
   the missing structural redaction. Likely one owner decision, not five local repairs.
2. **R4-Q5 cluster.** Storing `codex.*` types and raw params follows amended K-EVENT-1/K-EVENT-6 but conflicts with unamended
   K-ENGINE-4/SPEC §10.3. Verifier refutations and contests in DEL-05-02, 05-04, 05-05 all sit here (VERIFICATION §4 pattern 1).
   Ledgers sealed before Addendum 7 (DEL-05-01, 05-02_A/B, 05-04) carry plain `R4`; R3 maps them.
3. **Canonical session store moved; SoW text did not.** Every SoW still names project-local `.chirality/sessions/<id>/events.jsonl`
   and D-APP-41 eager conversion; amended CONTRACT K-EVENT-4 (D-APP-127, building on D-APP-73) names the Runtime userData store with lazy
   migration. D-APP-127 names DEL-05-02, yet only its `_STATUS.md` was revised (D-APP-127 application map: the only `YES` in PKG-05).
   CARRIER_PROPAGATION cluster consistent with R0 §8 item 6.
4. **Legacy migration inert for bootstrapped projects.** `bootstrap-project.ts:43-53` writes manifests without `legacySessionRoots`, so v2
   session records are never read for App-bootstrapped projects; no SoW unit or Remaining item names who declares legacy roots
   (DEL-05-01 CLM-010.3, recorded UNRECORDED_JUDGMENT).
5. **"Continue this chat" (`0ed1a1a7f`)** lets a recorded session become the primary dialogue, contrary to DEL-05-04 REQ-014/015/019;
   no ruling covers it (plain `R4`). Its positive owner is unclear (DEL-02-02, DEL-08-02 or DEL-05-01).
6. **SCA-APP-005 not transcribed.** It cut DEL-05-05 back to App consumption of Runtime-owned tool results (2026-07-27), but the SoW
   (2026-07-14) is unchanged; similarly the decomposition gives DEL-05-03 no run-logger ownership while its SoW still assigns one.
   No live tool-result artifact producer exists although K-EVENT-7 / SPEC 9.2 still require one.
7. **Register hygiene (DOC_HYGIENE).** All 15 `_REFERENCES.md` MATCH hashes fail to reproduce; several `Dependencies.csv` rows are
   SATISFIED on those hashes or on legacy-only code; DEL-05-05 cites removed `Specification.md`/`Procedure.md`.

### Coverage gaps reported by workers (no forward row could own them; for R3)

| Deliverable | Gap | Likely owner / note |
|---|---|---|
| DEL-05-01 | Runtime deletion tombstones (`.deleted/<id>.json`, CAP-RTCORE-015) are live, product-visible state no text describes | DEL-05-01 |
| DEL-05-01 | Who declares `legacySessionRoots` for bootstrapped manifests / the packaged App's old cwd v2 store (CAP-RTCORE-009) | DEL-05-01 REM-1 or PKG-09 upgrade |
| DEL-05-01 | Operator CLI session commands (CAP-RTCORE-049) — boundary trace only | Runtime |
| DEL-05-02 | Live App normalized views of `codex.notification` (`harness-event-views.ts`, `native-progress.ts`, `turn-activity.ts`; CAP-SHELL-039, WOVEN-033) delivered but covered only by open REM-1 | DEL-05-02 V3-01 or DEL-05-04 |
| DEL-05-02 | Retained closed schema-v2 wire validator (CAP-RTCONTRACT-024) still ships though D-APP-127 retired the closed vocabulary | unowned |
| DEL-05-02 (B) | Non-event parts of the replay response; live `coordination.acknowledged` emit; replay panel MALFORMED notice (CAP-WOVEN-019) | DEL-05-04 |
| DEL-05-03 | Runtime-side structural redaction owner (CAP-RTCORE-029/017/013) | owner decision (observation 1) |
| DEL-05-03 | Sign-in ceremony data exclusion (CAP-RTCORE-006) has no SoW requirement | DEL-05-03 or credential deliverable |
| DEL-05-03 | Secret-evidence scanner named by amended K-KEY-1 (CAP-BUILD-028) | PKG-09 to confirm |
| DEL-05-04 | Continuing a recorded conversation (WOVEN-021, SHELL-031) | DEL-02-02 / DEL-08-02 / DEL-05-01 |
| DEL-05-04 | Instruction history and resolved bases in the replay payload (`runtime-daemon.ts:801-808`) | instruction-basis deliverable |
| DEL-05-04 | Chat titles and search depend on the transcript projection | answered NOT_MINE |
| DEL-05-05 | No live tool-result artifact producer (K-EVENT-7, SPEC 9.2) | Runtime/Root after SCA-APP-005 |
| DEL-05-05 | ToolStreamView artifact semantics assigned by D-APP-70 (CAP-SHELL-040) have no SoW unit | DEL-05-05 (anchored on STATE-1) |

### Method notes for later waves

- The Addendum 6 rule 3 wording ("rows met by LIVE code") is read two ways on partly-live PARTIALLY_IMPLEMENTED rows (VERIFICATION §4
  pattern 4); a one-line clarification would stabilise R4-Q1 counts.
- Workers asked for AuthorityTier guidance on D-APP-only restatements (DEL-05-05 used LOCAL_DESIGN) and for a LatestDecision value for
  accepted SCAs, which have no D-ID.
- Double-blind reverse passes were given the union of both workers' script-derived areas (A 9, B 8) so Responses are comparable.
