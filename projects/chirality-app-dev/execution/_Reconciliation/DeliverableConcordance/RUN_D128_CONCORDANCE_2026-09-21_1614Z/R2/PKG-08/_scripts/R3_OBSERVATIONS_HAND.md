## §8 Cross-package observations for R3 (hand-written by the PKG-08 manager; evidence, not rulings)

1. **R4-Q1 dominates PKG-08.** 78 of 310 rows turn on legacy harness versus the live Codex path.
   Every App `delegate_agent` admission module, `ChildRunRecord` / `subagent.*` / `artifacts/subagents`
   writer and 16/512 KiB cap is LEGACY_ONLY. On the live path children come from Codex-native `[agents]`
   descent, recorded only as `tool.*` / `codex.notification` events. The one governed live-side runner
   (`GovernedAgent1RunCoordinator`) is never composed: the runs route throws
   REQUIRED_DELEGATION_MISSING. The same question sits in PKG-04, PKG-06 and PKG-10 (R0 §8.1), so R3
   should frame it once.
2. **An unframed owner question behind plain `R4` (45 rows, 32 in DEL-08-02).** The 2026-09-09 v3
   role adoption (`9b005c23a`; CONTEXT `CHIRALITY_V3_APP_ADOPTION_20260909`) changed the alias map and
   default role, retired the agent matrix and the Pipeline surface, and replaced the SPEC §7 agent-file
   header format. App PRD/SPEC/CONTRACT were not amended. DEL-08-01 carries this as
   `OTHER:V3_ROLE_ADOPTION` (18 rows), and its conformance validator checks only fixtures and would
   fail the four shipped role files. Candidate R4-Q4: "Is the v3 four-role adoption a governing
   amendment of SPEC §7 and §13 and the persona and matrix contracts?"
3. **The static reachability map overstates LIVE.** It is import-based, so surfaces the product
   imports but never renders or constructs read as LIVE. Other waves (PKG-02/07 shell, PKG-03/05
   runtime) will meet the same modules (`pipeline-surface.tsx`, the consent-port panel,
   `agent1-run-coordinator.ts`, `native-role-config.ts`). An "executed on product path" annotation,
   or a module- versus function-level rule, would reduce errata and CONTESTED items.
4. **Authority conflicts that remain after the DIRECTIVE §0 order.** (a) TYPES §10 v2
   `ChildRunRecord` (`childInstanceId`) against D-APP-40 and D-APP-56 (`childRunId`); no ruling names
   TYPES §10 (DEL-08-05, 3 rows). (b) CONTRACT K-SUBAGENT-1 "0→1 or 1→2" against the code and Root
   AGENTS admitting Agent 0 → TASK (R0 §8.5; DEL-08-04 rows citing K-SUBAGENT-1 mostly carry R4-Q1, e.g. SEC-1, CLM-003.2, CLM-010.1).
5. **Corpus-wide hygiene, confirmed again.** All 15 PKG-08 `_REFERENCES.md` MATCH hashes fail to
   reproduce (25 REGISTER_DEFECT rows across the package, not all of them hash rows). The PRD drift dates from `9eaddb596`, not from the
   D-GOV-43 tranche (DEL-08-04 REGISTER-3 correction). This supports the R0 §8.7 suggestion of one
   corpus-wide repair.
6. **Cross-deliverable ownership.** PKG-08 claims no capability twice. `CAP-HARNESS-056` (child
   lifecycle and records) belongs to DEL-08-05, not DEL-08-04. The runtime `listAgents` roster still
   parses SPEC §7 `AGENT_TYPE` headers, so it would list the v3 role files untyped (CAP-RTCORE-016). The
   App does not call it; this is for the roster owner (likely PKG-03/05).
7. **Post-release coverage gap.** `da95ec194` added child-thread tool-call cancellation to
   `codex-supervisor.ts` (lines 526, 535-544, 570-573). No PKG-08 row cites it, though it bears on
   DEL-08-05 CLM-018.2 (REQ-002 cleanup). Recorded in reverse_notes only; R3 decides where it lands.
