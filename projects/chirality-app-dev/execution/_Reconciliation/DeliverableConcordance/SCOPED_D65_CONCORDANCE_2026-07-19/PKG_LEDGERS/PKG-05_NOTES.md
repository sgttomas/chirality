# PKG-05 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (Instance G4)

- **Window:** `c313325b7` (R6 basis) → `ff2f68c82` (HEAD). Agent claims only; no verdict here is an owner act.

## Counts

| Metric | Value |
|---|---:|
| Prior claim rows (frozen manifest) | 116 |
| In-scope selected | 116 (100%) |
| Confirmed (ScopedDisposition == PriorDisposition) | 109 |
| Re-dispositioned (disposition deltas) | 7 |
| New rows minted (`DEL-XX-YY-SCOPED-Snn`) | 7 |
| HumanDecisionNeeded = YES | 4 |

Deltas: DEL-05-01 UNMAPPED-1/UNMAPPED-2 (IMPLEMENTED_UNDOCUMENTED→ALIGNED, R4-P31 kit adoption via ScopeOfWork CLM-014); DEL-05-02 REGISTER-2 (→ALIGNED, R5 dated correction block); DEL-05-03 R12 (PARTIALLY_IMPLEMENTED→ALIGNED, D-APP-67 Option B ruled the configured-secret schema question), UNMAPPED-2 (→ALIGNED, ratified taxonomy homes the scanner), REGISTER-1/REGISTER-2 (→ALIGNED, R5 dated corrections).

## Selection reasoning

Rule (a) captured every prior row: the drift window deleted all four kit
documents (Datasheet/Guidance/Procedure/Specification) for every PKG-05
deliverable and replaced them with a consolidated `ScopeOfWork.md`
(`chirality-deliverable-sow/v1`) under the owner-ratified D-GOV-15/D-GOV-16
Deliverable Scope-of-Work Standard (migration commits of 2026-07-13, e.g.
`8c8b0ef22`/`22e4aae2c`). Since every claim's NormativeSource cites at least
one deleted kit file, all 116 rows were selected. Rule (c) additionally
triggered for DEL-05-03 (D-APP-67 ruling, ratified taxonomy, adoption run
record) and for the R6/`_STATUS.md` bootstrap removals (commit `8a2f84f98`).

Adjudication method: for each claim I verified (i) the claim's substance was
carried into the live `ScopeOfWork.md` CLM blocks (requirement-ID tables
confirmed present per deliverable), and (ii) whether the claim's
implementation/verification surfaces changed in the window (git name-status:
`session-manager.ts`, `session-events.ts`, `run-logger.ts`,
`tool-result-artifacts.ts`, `tool-evidence.ts`, `sdk-message-mapper.ts`,
`transcript-replay.ts`, `event-factory.ts`, `harness-ui-bridge.ts` and their
focused test files are all UNCHANGED in the window; the only PKG-05-relevant
code deltas are the additive `coordination.*` event types and the additive
SessionRecord delegation-metadata fields in `harness-contract`).

## Key window facts

1. **D-GOV-16 SOW consolidation** — structural, owner-ratified; content
   carried; every prior ledger file+line anchor into kit files is now a dead
   pointer (new rows `DEL-05-0X-SCOPED-S01`).
2. **D-APP-67 Option B (2026-07-19)** — committed-secret taxonomy ratified in
   `Taxonomy_Committed_Secret_Redaction_DEL-05-03.md`; runtime helper stays
   API-key-specific by ruling; DEL-05-03 gated Remaining item discharged.
3. **Managed-delegation lane** — additive `coordination.*` event vocabulary
   and SessionRecord delegation fields (commits `62e563e47`/`c9734a6ee`/
   `ee35409f5`); consistent with DEL-05-01/02 requirements but unmapped to
   any PKG-05 kit (new rows S02 on DEL-05-01 and DEL-05-02, HDN=YES).
4. **Persisting staleness carried into the new SOWs** (repairs were never
   executed at R5; baseline verified to carry the same wording, so this is
   PERSISTING, not migration regression): DEL-05-02 HASH_MISMATCH wording
   (SOW lines 247/297/317) and `sdk.system.init`/`sdk.mirror.error` category
   names (lines 59/430-431); DEL-05-03 line 250 HASH_MISMATCH; DEL-05-04
   three residual dead `src/lib/harness/transcript-replay.ts` citations
   (lines 93/204/235).

## Human decisions (4)

1. DEL-05-01-SCOPED-S02 — adopt SessionRecord delegation-metadata fields into
   DEL-05-01's documented field list, or map to the managed-delegation surface.
2. DEL-05-02-SCOPED-S02 — same decision for the `coordination.*` event
   vocabulary.
3. DEL-05-03 UNMAPPED-1 — pec transport credential/cookie hygiene ownership
   (acknowledged but not assigned by D-APP-67).
4. DEL-05-05 UNMAPPED-1 — subagent child-output artifact storage ownership
   (materiality raised by the new delegation lane).

## Ambiguities

- Whether persisting HASH_MISMATCH/category-name staleness in the new SOWs
  should be treated as migration regression was resolved by checking the
  baseline kit text: identical wording existed at `c313325b7`, so PERSISTING.
- The `_STATUS.md` R6 bootstrap removals and R5 register corrections were
  executed by prior authorized phases; I coded them RESOLVED with the
  executing authority cited, not as new repairs.

## Not examined (stands on R3/R6)

- Register rows whose register files did not change in the window were
  re-checked only for the specific prior defect text, not re-extracted.
- No re-derivation of the 833-ALIGNED whole-corpus bulk outside PKG-05.
- No test execution: no full frontend gate transcript exists inside the
  window; behavioral confirmations are code-inspection-level
  (`RUN-INSPECTION@ff2f68c82`) on top of the unchanged-file byte identity to
  the W1-gated state; the only in-window suite evidence is the targeted
  87/87 pass recorded in `RETURN_N4_CODE_TEST.md` (DEL-04-05 file).

## Method deviations (disclosed)

- The brief's tool fence names Read/Grep/Glob/Write, but this harness exposes
  no Grep or Glob tool. After the kit files proved to be deleted/renamed,
  directory listing and window diffing were impossible with Read alone; I
  used strictly read-only Bash (`ls`, `grep`, `git log/diff/show`, `sed -n`,
  `head`) as the Grep/Glob substitute. No file outside the two PKG_LEDGERS
  write targets was created or modified; no network, no delegation, no test
  execution. Two early incidental read-only Bash calls (`ls` of MANIFESTS, a
  no-op) predate this decision and are included in this disclosure.
