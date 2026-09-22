# T2B: subject test on rows that lost every LIVE tag under reach calls (a)/(b)

Task T2B, R3. Input `R3/_work/CAND_SUBJECT.csv` (99 rows). Consistency calls, not rulings.
Outputs: `R3/_work/T2B_VERDICTS.csv` (99 rows), `R3/_work/T2B_REMAPS.csv` (3 rows, 1 key).
Script: `R3/_work/T2B_scripts/t2b_build.py` (the verdicts are recorded in it; it only assembles).
## Counts
- KEEP_OTHER 67 (PKG-09 34, PKG-10 29, PKG-06 3, EXT 1). KEEP_MODULE 30 (PKG-10 21, EXT 6, PKG-06 3).
- REDISPOSITION 1: DEL-06-01#CLM-034.2 (ALIGNED to IMPLEMENTED_DIFFERENTLY; CauseTag NONE to NATIVE_DELEGATION).
- UNDECIDED 1: DEL-06-03#CLM-010.4. HumanDecisionNeeded is not changed on any row.
## Patterns
- PKG-09 (call b, 34 rows): every row is about validation, CI or release tooling or its records. TEST_ONLY
  is the tooling's own reach, so the Disposition judges the tooling (as T4A reads it).
- PKG-10 contract shapes (call a): DomainEngineProfile and OperationProposal field sets, enums and guards
  name a type and state only its contract (rule 1). Sealed notes already call the types inert with no
  product caller, so those ALIGNED verdicts were module-level from the start.
- PKG-10 copy, principles, procedures and check definitions are deliverable text. Documentary evidence
  meets them; the re-tagged type was corroboration only.
- Staged-surface rows (DEL-10-01#CLM-004.1, 012.2; DEL-10-04#CLM-004.1, 010.1) were already live-path
  PARTIALLY_IMPLEMENTED. The gated half (no endpoints, apply or protected-path hooks) still holds live.
- Rows resting on absence on every path (no domain output, apply, endpoint or protected write), and the two
  ACCEPTED_DIVERGENCE rows, do not rest on the re-tagged code.
- DEL-10-04#CLM-004.6, 010.4, 028 concern where OpenPipeStress concepts sit. The descriptor is still in the
  public runtime-contracts package. Their notes call it "LIVE"; it is now LEGACY_ONLY by symbol, but the
  location finding is unchanged.
- DEL-06-02#CLM-035.1 and DEL-10-01#CLM-016.1 (IMPLEMENTED_DIFFERENTLY) are module-level readings (moved module).
## Redisposition
- DEL-06-01#CLM-034.2: "hard-denied outside workspaceWrite" is a permission control (rule 1). The sealed
  ALIGNED judged the LEGACY_ONLY overlay at module level; after call a the descriptor text is LEGACY_ONLY
  too. Live operator modes map to Codex sandbox policy (`codex-supervisor.ts:104-109`,
  `chat-panel.tsx:123-136`), with no Chirality coordination class; delegation is Codex-native.
  IMPLEMENTED_DIFFERENTLY, ALSO_MODULE:ALIGNED, as sibling DEL-06-03#CLM-035.1. Other reading:
  DOCUMENTED_UNIMPLEMENTED if the Codex sandbox is not counted as the mechanism.
## Undecided
- DEL-06-03#CLM-010.4 ("Tool definitions declare schema, permissions, ..."). A (rule 1, module): fields exist
  (`tool-descriptor.ts:84-106`), so ALIGNED. B (sealed live-path reading): no LIVE code declares Chirality
  tool metadata and the Runtime records `mcpServers: []` (SEE DEL-06-03#CLM-003), so
  DOCUMENTED_UNIMPLEMENTED with ALSO_MODULE:ALIGNED. Neither reading keeps the sealed PARTIALLY_IMPLEMENTED.
## Least-confident KEEP
- DEL-10-04#CLM-010.3: the partial rests on the registry and the Root validator. The alternative is
  DOCUMENTED_UNIMPLEMENTED on the live path: no validation step runs there, and no domain surface is exposed.
