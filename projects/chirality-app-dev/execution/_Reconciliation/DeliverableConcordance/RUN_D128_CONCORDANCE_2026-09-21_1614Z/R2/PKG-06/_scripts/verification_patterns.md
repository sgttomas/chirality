## §4 Patterns (hand-written by the PKG-06 manager from the shard notes; evidence, not rulings)

1. **The AUTHORITY_CONFLICT + R4-Q1 cluster holds in every shard.** The unamended engine-neutral or
   SDK-named clauses K-PATH-2/3, K-ROOT-2, K-HOOK-1, K-PERM-1/3/4/5/6, K-BASH-1, K-TOOL-1/2, K-MCP-1,
   SPEC §15.1/§15.2, TYPES §8.5 and PRD FR-119 sit at the CONTRACT/SPEC tier. D-GOV-43 (item 4:
   approval and sandbox are the user's choice) and the amended K-RUNTIME-1 undercut them without naming
   them, so DIRECTIVE §0 cannot resolve the tension. Shards confirmed this on 01_RERUN, 03, 04_RERUN, 05
   and 06_RERUN. The boundary cases are:
   - **Where DIRECTIVE §0 does resolve it** (a decomposition or SCA restatement against amended
     CONTRACT/SPEC), AUTHORITY_CONFLICT is wrong. These are the two verdict-field refutations in
     ledgers of record: DEL-06-04#STATE-2 and DEL-06-06#STATE-1 (→ STALE_SPECIFICATION).
   - **Mechanism-neutral clauses.** K-PERM-4 / FR-091 (DEL-06-03#CLM-010.9) and K-PERM-3 in Claude SDK
     wording (DEL-06-05#CLM-009.4) are CONTESTED toward DOCUMENTED_UNIMPLEMENTED on the live path.
   - **Uneven application within one ledger.** DEL-06-02#CLM-003 folds its K-TOOL-2 and K-PERM-3 rows
     into IMPLEMENTED_DIFFERENTLY, and DEL-06-02#CLM-010.7 reads either way.
2. **MR-8 (iv) / grading key 5 is the dominant CONTESTED class.** The dated "REF-006 MATCH (D-APP-56
   current-state note, 2026-07-12)" rows and their SEE rows are STALE_SPECIFICATION in the ledgers, but
   register-lag REMAINING_STATE_MISMATCH fits equally. Affected: DEL-06-01 CLM-001/007/023 and
   REGISTER-1, DEL-06-02 CLM-001/008, DEL-06-04 CLM-001/004.1/004.7, DEL-06-05 CLM-004.1/027, and
   DEL-06-06 CLM-001/004/007/008 in the first attempt. The same boundary produced 6 of the 16
   Disposition disagreements in the DEL-06-02 double-blind. The undated MATCH assertions are confirmed
   as STALE_SPECIFICATION. **Convention question for R3:** a rule for dated carrier notes that restate a
   register value.
3. **Module-level versus symbol-level reach (grading key 3).** `REACHABILITY.csv` marks
   `runtime-contracts` `tool-descriptor.ts` and `tool-names.ts` LIVE, but only through the package
   barrel. CAP-RTCONTRACT-042/044 mark their symbols LEGACY_ONLY, and CAP-HARNESS-060 disagrees on
   `runtime-fingerprint.ts`. DEL-06-03 CLM-003/010.1/010.4 are CONTESTED between PARTIALLY_IMPLEMENTED
   and DOCUMENTED_UNIMPLEMENTED on this point alone. Workers followed the rulebook, which names the pack
   map, so these rows are not errors. See the pack manifest's known limit 1.
4. **Field-level precision errors (all in CORRECTIONS.csv or superseded attempts).**
   - **DirectionEvidence propagated through SEE chains.** In DEL-06-01_RERUN, one wrong gloss ("no
     register refresh followed D-GOV-43") repeats on 6 rows. At the frozen tree the refresh happened at
     `23b3879b3`; the drift comes from `9eaddb596`, `95b342519` and `7f1e9f387` on 2026-09-12.
   - **PostReleaseBasis.** The R0 pattern recurred in DEL-06-01_RERUN CLM-003 and CLM-009.2: the cited
     range `codex-supervisor.ts:694-717` includes line 695, which blames to `da95ec194`. The first
     attempt of DEL-06-01 cited that file correctly.
   - **First attempts (superseded).** DEL-06-01 had 3 truncated or untagged `delegated.ts` citations and
     DirectionEvidence NONE_FOUND against D-APP-89. DEL-06-04 had 2 anchors that pointed at the
     coordination gate instead of the write gate, and 2 rows with LatestDecision NONE_FOUND beside
     `GOV:D-GOV-43`.
   - **AssessmentEvidence.** DEL-06-02#CLM-010.9 names the wrong INSP-03 anchor, but OVERTAKEN holds.
5. **Event-contract tension, a candidate new conflict.** DEL-06-06_RERUN CLM-004.2, 010.8 and 010.12
   are CONTESTED. Amended K-EVENT-1/6 preserve upstream payloads, while unamended SPEC §10.3 and
   K-ENGINE-4 still say "translate". The live path persists `thread/compacted` and hook notifications
   only as generic `codex.notification`. This parallels the R0 `codex.*` event-type question (R0 §8
   item 3).
6. **Reverse pass.** 34 class-c items with 33 CONFIRMED, 1 CONTESTED (DEL-06-01 first attempt: CLM-004
   vs CLM-027 as owner of CAP-RTCONTRACT-019) and no REFUTED. Errata: 15 items, all CONFIRMED, of which
   12 are in the superseded DEL-06-01 attempt.

## §5 Rerun and acceptance record

| Deliverable | Attempts | Ledger of record | Why |
|---|---|---|---|
| DEL-06-01 | `DEL-06-01/` (first), `DEL-06-01_RERUN/` | `DEL-06-01_RERUN` | The first attempt was rerun under the original rule (12.9% of distinct rows REFUTED, all field-level). The rerun has 0 verdict-field refutations. Its 8 field-level refutations are in CORRECTIONS.csv. Under Addendum 3 no third attempt was started. |
| DEL-06-02 | `_A`, `_B` (double-blind) | `DEL-06-02_A` | Brief step 4. B was not verified; it is compared in `DOUBLE_BLIND_DEL-06-02.md`. |
| DEL-06-03 | one | `DEL-06-03` | 0 REFUTED. |
| DEL-06-04 | first, `_RERUN` | `DEL-06-04_RERUN` | First attempt 12.1% (field-level only), rerun under the original rule. The rerun has 1 verdict refutation of 35 items (2.9%). |
| DEL-06-05 | one | `DEL-06-05` | 0 REFUTED; 3 errata confirmed. |
| DEL-06-06 | first, `_RERUN` | `DEL-06-06_RERUN` | First attempt 10.5% (1 Disposition, CLM-010.11, and 1 DirectionEvidence), rerun under the original rule. The rerun has 1 verdict refutation of 28 items (3.6%). The rerun re-judged the redaction requirement at the store (CLM-004.4, DOCUMENTED_UNIMPLEMENTED). |

The rerun prompts named the defect classes found by the first verifiers, such as per-path REACH tags,
anchor accuracy and judging redaction at the store. They did not name dispositions, and the rerun
workers were barred from the first attempts and `_verify/`. That guidance means the reruns are not fully
blind to the first verification. STATE.jsonl records each prompt's note.
