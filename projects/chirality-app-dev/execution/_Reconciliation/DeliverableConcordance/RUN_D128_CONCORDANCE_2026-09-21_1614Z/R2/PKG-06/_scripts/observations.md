## 8. Cross-package observations for R3 (hand-written; evidence, not rulings)

1. **R4-Q1 is the package's centre of gravity.**
   - About half of all PKG-06 rows cite R4-Q1 (§3). PKG-06's normative text describes the in-process
     Claude SDK harness: permission overlay, `canUseTool`, tool pool, write/edit hooks, Bash policy, and
     the hook and compaction mirror. At `00115c719` all of it is LEGACY_ONLY.
   - On the live Codex path the only bound is the user's Codex approval and sandbox choice. That includes
     "Full access" (bypass). The live **default** mode `workspaceWrite` maps to approval `never` with a
     workspace-write sandbox, so Codex runs shell commands and writes with no prompt (DEL-06-05 errata,
     verifier-confirmed; `chat-panel.tsx:136`, `delegated.ts:320-330`).
   - A legacy `dontAsk` request is silently mapped to `readOnly` (`runtime-daemon-harness-port.ts:205-207`),
     which is undocumented.
   - The same clauses (K-PATH, K-ROOT, K-HOOK, K-PERM, K-BASH, K-TOOL, K-MCP, SPEC §15.x) will recur in
     PKG-04, 08 and 10. One R4-Q1 ruling would settle 173 PKG-06 row citations.
2. **No live Chirality MCP tool surface.**
   - The Runtime fingerprint records `mcpServers: []` (DEL-06-03). The read tools, the coordination-tool
     composition and the seat for the unbuilt `propose` tool (DEL-06-03-V3-01, gated on DEL-02-02-V3-04)
     exist only on the legacy path.
   - This bears on PKG-02 (propose/dialogue), PKG-08 (delegation tools) and PKG-10 (domain tools).
3. **Event log redaction and translation (PKG-05 interface).**
   - The live Runtime store persists raw Codex notification `params` as `codex.notification`, with no
     redaction and no size cap (`session-store.ts` → `fs.ts` appendJsonLine). K-EVENT-6, as amended,
     still requires redaction before persistence. Redaction exists only on the legacy writer
     (DEL-06-06_RERUN CLM-004.4).
   - No `hook.*` or `context.compacted` event is ever produced live. Code emits `hook.failed`, which
     SPEC §9.4 does not list.
   - Amended K-EVENT-1/6 ("preserve") versus unamended SPEC §10.3 and K-ENGINE-4 ("translate") is a
     candidate AUTHORITY_CONFLICT for PKG-03 and PKG-05 (VERIFICATION §4.5).
4. **REGISTER cluster: one corpus-wide cause.**
   - All six PKG-06 `_REFERENCES.md` MATCH hashes fail to reproduce.
   - DEL-06-01_RERUN's verifier traced the cause. The hashes were refreshed correctly by the D-GOV-43
     tranche `23b3879b3`. Three later 2026-09-12 commits (`9eaddb596`, `95b342519`, `7f1e9f387`) then
     changed PRD, SPEC and CONTRACT without re-pinning.
   - This supports R0 §8 item 7: one corpus-wide repair.
   - No PKG-06 carrier cites D-APP-127 or D-GOV-43, and every `_CONTEXT.md` still names the Claude SDK
     and daemon path (CARRIER_PROPAGATION, mostly recorded as `CAUSE2:`).
5. **Undocumented post-release capability.** A Runtime application-tool catalog added in `da95ec194`
   rejects duplicate and unregistered tool names. It is the live counterpart of SOW-064's App/project
   tool catalog, but the App registers nothing into it and no deliverable records it (DEL-06-02 A and B
   both found it). This is relevant to the EXT SOW ledger and to PKG-05.
6. **Ownership overlap.** 14 capabilities are claimed or partly covered by more than one PKG-06
   deliverable (§5). Examples are the mode→Codex policy map (CAP-RTCONTRACT-019), the permission
   overlay (CAP-HARNESS-043) and the tool-descriptor registry (CAP-RTCONTRACT-042). R3 should assign a
   single owner. The mirror-only DEL-06-06 claims nothing outright, since everything it touches is owned
   in PKG-03, PKG-05, DEL-06-04 or DEL-09-02.
7. **Method signals.**
   - **Double-blind.** DEL-06-02's Disposition agreement was 54% exact (R0 DEL-03-01: 82%). The two main
     boundaries were STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH and IMPLEMENTED_DIFFERENTLY vs
     PARTIALLY_IMPLEMENTED. Reverse agreement was 99%.
   - **Named questions.** R4-Q2 and R4-Q3 appear only in DEL-06-04_RERUN (3 and 2 rows). 11 rows carry plain R4
     (DEL-06-01_RERUN 7, DEL-06-06_RERUN 3, DEL-06-04_RERUN 1); R3 should check whether a named question fits.
   - **Other tokens.** No `OTHER:` cause tokens were used. PKG-06 has one REMAINING_WORK row (DEL-06-03
     REM-1).
