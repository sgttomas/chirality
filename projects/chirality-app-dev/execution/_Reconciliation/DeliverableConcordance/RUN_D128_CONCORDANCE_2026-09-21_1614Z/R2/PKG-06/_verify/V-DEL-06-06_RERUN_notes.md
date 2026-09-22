# V-DEL-06-06_RERUN verifier notes

Shard `V-DEL-06-06_RERUN`, unit `DEL-06-06_RERUN`, frozen basis `00115c719`. Graded against
`CONVENTIONS.md` and the shared grading key in `BRIEFS/VERIFIER_BRIEF.md`. The original DEL-06-06
folder and other shards' files were not read. There is no errata file (pass 1 had no errata), so
the shard has no class `e` items.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT) | 8 | 7 | 1 | 0 |
| a30 (30% of other non-ALIGNED) | 15 | 12 | 0 | 3 |
| b (ALIGNED sample) | 2 | 2 | 0 | 0 |
| c (reverse PARTIAL) | 3 | 3 | 0 | 0 |
| **Total** | **28** | **24** | **1** | **3** |

## (ii) Systematic patterns

1. **The K-HOOK-1 / SPEC 15.2 / TYPES 8.5 AUTHORITY_CONFLICT set holds.** This covers CLM-003.2,
   003.3, 009, 010.5, 010.6, 024 and 025.3.
   - K-HOOK-1 (CONTRACT.md:99) and the SPEC 15.2 fail-closed sentence (SPEC.md:860) are
     unamended at the frozen basis.
   - D-GOV-43 (proposal, ruling candidate and IMPACT.md) never mentions hooks or K-HOOK.
   - Both conflicting texts sit at the same tier, so DIRECTIVE §0 does not resolve the conflict.
   - The rulebook's own R4-Q1 definition names exactly these clauses, so `R4-Q1` is the right
     citation.
   - Minor: CLM-003.3 merges two Attributes table rows. Its PreCompact/Stop half is D-APP-43 2B
     (MR-11) territory, and the row's Notes correctly route that half elsewhere.
2. **Refuted: STATE-1 (daemon and "Claude Agent SDK first/current path" in `_CONTEXT.md`).** The
   worker marked this AUTHORITY_CONFLICT. DIRECTIVE §0 resolves it, so AUTHORITY_CONFLICT is wrong
   (grading key 4). CONTRACT is tier 2 and outranks the tier 7 decomposition and scope-change
   records. CONTRACT states:
   - Codex is the sole MVP engine, and Claude/Anthropic is compatibility history (CONTRACT.md:15,
     K-ENGINE-3);
   - K-RUNTIME-1 is re-expressed without a daemon (CONTRACT.md:224).

   The correct reading is STALE_SPECIFICATION with HumanDecisionNeeded `NO`, and D-GOV-43 as a
   governing (not `(context)`) decision.
3. **Contested: the wrap-and-preserve representation versus "translate".** This covers CLM-004.2
   and its SEE row CLM-010.12, plus CLM-010.8.
   - Amended K-EVENT-1 and K-EVENT-6 explicitly preserve upstream method names and payloads.
     Unamended SPEC 10.3 and K-ENGINE-4 still say "translate" and "adapter metadata only". Either
     reading is defensible.
   - For CLM-010.8, the supervisor forwards every notification (codex-supervisor.ts:546). The
     D-GOV-43 proposal (finding 6) names the upstream `thread/compacted` notification. On that
     reading the compaction boundary is persisted as a generic `codex.notification`, which is
     IMPLEMENTED_DIFFERENTLY. The ledger itself uses that reading for CLM-010.7.
   - If that reading is taken, CLM-010.8's `NONE_FOUND` DirectionEvidence would become
     `GOV:D-GOV-43 item 2/5`. This also resolves the worker's stated uncertainty about the
     upstream compaction method name.
4. **Checks that held.**
   - **Line anchors.** Every cited code anchor showed the claimed content, with drift of at most
     one line (for example the `sdk-message-mapper.ts` compaction block at 1034–1056, and
     `session-store.ts` sessions root at 1113).
   - **PostReleaseBasis `NO`.** `git blame -L` on the relied-on ranges of `codex-supervisor.ts`
     (584–600, 729–735) and `session-store.ts` (654–669, 813–823, 1111–1127) returns only
     95364569a, 9eaddb596, 8b3643e6c, 9b005c23a, 5c43b3a20 and 25818258a. None of these is one of
     the four touched commits.
   - **REACH tags.** All tags match `REACHABILITY.csv`.
   - **Named test cases.** All exist at the cited files.
   - **Redaction gap.** No redaction exists in `chirality-runtime/packages/*/src`: the word
     appears only in tool-catalog prose and conformance codes. The gap in CLM-004.4 and 010.11 is
     therefore confirmed.

## (iii) Effort

- **Ledger and rulebook.** Read the full rulebook, RUN_BASIS §3, §5 and the addenda, the unit
  notes and reverse notes, the 28 selected rows (by script), and the pack files (REFERENCE_HASHES,
  D-APP-127 map, REACHABILITY and TOUCHED_PATHS, the last two grepped).
- **Frozen tree, deliverable and governance files.** The SoW (Attributes, Conditions, REQ table
  and Principles), `_CONTEXT`, `_STATUS`, MEMORY, `_REFERENCES`, the decomposition L227–231 and
  L351, CONTRACT K-rows, SPEC §9 and §15.2, TYPES §8.5, and DIRECTIVE §0.
- **Frozen tree, rulings.** The D-GOV-43 proposal (findings and items 1–14) and its IMPACT.md
  grep, the D-APP-43 ruling grep, and DONE-10 in the done-declaration candidate.
- **Frozen tree, code line ranges.** About 9 code files (adapter, supervisor, session-store, fs,
  event-schema, turn-coordinator, and the legacy hooks, mapper, session-events and
  tool-result-artifacts), plus test-name greps in 6 test files.
- **Git.** `git log -1` and `git show` on 16f7ed612, and `git blame -L` on the decomposition and
  on the two touched runtime files.
- **Context budget.** Moderate; not tight.
