# V-SHARD-DEL-08-04-1: verifier notes

Scope: 26 items from DEL-08-04, all under the shared PKG-08 grading key. That is 14 class a (11 errata, 3 REMAINING_WORK), 11 class a30 and 1 class b. Class-a errata rows were graded on the errata-applied row, and each errata row touching an item was rechecked against the frozen tree.

## (i) Counts

| Verdict | a | a30 | b | Total |
|---|---|---|---|---|
| CONFIRMED | 12 | 10 | 1 | 23 |
| CONTESTED | 2 | 0 | 0 | 2 |
| REFUTED | 0 | 1 | 0 | 1 |

- CONTESTED: `CLM-010.2` (Disposition) and `REM-3` (MechanicallyUnblocked).
- REFUTED: `REGISTER-3` (DirectionEvidence only; the Disposition holds).
- Disposition-level REFUTED keys: none in the graded, errata-applied ledger. Two errata change a sealed `ALIGNED` to `PARTIALLY_IMPLEMENTED`, at `SEC-2.3` and `CLM-016.4`, and both are confirmed. The sealed Disposition therefore did not hold for those two keys.
- Errata recheck: all 19 errata rows that touch this shard's keys were confirmed. That covers the ImplementationEvidence rows for SEC-1, SEC-2.1, CLM-003.2, CLM-033, CLM-010.2, CLM-016.2, CLM-016.3, CLM-016.7 and REM-2, the Notes rows for CLM-003.2 and CLM-010.1, and the four fields each of SEC-2.3 and CLM-016.4.

## (ii) Patterns

1. **The native-role-config reach retag is correct in substance but applied inconsistently.** At the frozen basis, `loadTrustedNativeRoleConfiguration` and `codexNativeRoleConfigOverrides` have no product caller; the only reference is the core `index.ts` re-export. The live path supplies `agents.<role>` config through `product-native-role-config.ts`, which `delegated-engine-adapter.ts:20` imports. So the sealed claim that maxDepth 2 is pinned on the live path was wrong. In the same way, `descendant-tracker.ts` is used only by `ProcessSupervisor`, which is never constructed in product. The errata retag both modules `TEST_ONLY` against the pack's static `LIVE`. That is accepted because the errata give a code-verified reason. The same ledger, however, keeps `agent1-run-coordinator.ts` at `REACH=LIVE` with a Notes caveat under the identical condition. Examples: SEC-1, CLM-010.2, CLM-016.2.
2. **Static LIVE is not the same as rendered.** The K-ROLE-2 labels live in `account-consent-settings.tsx`. That file is static-LIVE, but the panel never renders on the product path: `shell-frame.tsx:377` supplies a null port, and `settings-view.tsx:31` always takes the hosted branch. The persona picker also withholds Agent 2/TASK entry (`persona-picker.tsx:18-23`). This changes the Disposition, as SEC-2.3 and CLM-016.4 show, and the errata correct it. CLM-016.2 cites the same unrendered text, but there the Disposition does not change.
3. **Two cause and direction attributions need checking.**
   - `REGISTER-3` attributes the PRD hash drift to D-GOV-43. In fact, the recorded hash is PRD at the D-GOV-43 tranche commit `23b3879b3`, and the drift is the later `9eaddb596` (PR #778).
   - `CLM-010.2` gives the "sole executable path" statement a different Disposition from the verbatim CLM-003 row it repeats (MR-4).
   - `REM-3` reads the "DEL-02-02-V3-04 selected" gate as unmet without noting that both V3-04 prerequisites landed and that a V3-04 slice was implemented.

Other checks held:
- Line anchors: all within tolerance. The errata cite `shell-frame.tsx:377`, which is exact.
- PostReleaseBasis: the only cited file in TOUCHED_PATHS is `codex-supervisor.ts`, and lines 280-309 blame to `95b342519`.
- Test-case names: all exist.
- AssessmentEvidence tokens: MR-1 compliant.
- NONE_FOUND searches: spot-checked for CLM-006.

## (iii) Effort

- About 30 frozen-tree files were read in line ranges: the SoW, `_STATUS`, `_REFERENCES`, three other `_STATUS` files, CONTRACT, TYPES, PRD, the register and three rulings, and about 15 code files.
- Six read-only git calls against the frozen tree (log, show, blame).
- The context budget was comfortable. The ledger rows are very verbose, so they were extracted to scratch and read there.
