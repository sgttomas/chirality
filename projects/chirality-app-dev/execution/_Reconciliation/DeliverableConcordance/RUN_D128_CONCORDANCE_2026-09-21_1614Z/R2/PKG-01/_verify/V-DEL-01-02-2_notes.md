# V-DEL-01-02-2 — verifier shard notes (RUN_D128, R2, PKG-01, DEL-01-02)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a30 | 4 | 4 | 0 | 0 |
| b (ALIGNED) | 4 | 2 | 0 | 2 |
| c (reverse PARTIAL) | 14 | 14 | 0 | 0 |
| e (errata) | 17 | 16 | 1 | 0 |
| **Total** | **39** | **36** | **1** | **2** |

- **Verdict-field refutations (Addendum 3):** none. The one REFUTED item is on a non-verdict field (CLM-011.1 erratum, RemainingWork).
- **The two CONTESTED items are on Disposition** (CLM-006.5, CLM-007.6). Under grading key 2 they do not count as refutations.

## (ii) Patterns

1. **The symbol-level REACH errata hold.** I re-checked all 17 errata rows at the frozen tree. The LIVE tags in the sealed ledger came from the module-level pack map, which marks a whole module LIVE through a barrel import or through one live helper. At symbol level:
   - `engine-conformance.ts` is TEST_ONLY (CLM-006.1, 006.13).
   - `tool-descriptor.ts` is LEGACY_ONLY (CLM-006.10).
   - `redactJsonLike` is LEGACY_ONLY (CLM-006.12, 018.19).
   - `FileSessionManager` is LEGACY_ONLY (CLM-006.6, 018.7, 011.1).
   - The harness-contract shim is TEST_ONLY (STATE-2).
   - `agent1-run-coordinator.ts` is TEST_ONLY (CLM-006.8, 018.16). `app-owned-composition.ts:226` passes `undefined` into the `agent1Runs` constructor slot (`runtime-service.ts:119`), so `runAgent1` throws `REQUIRED_DELEGATION_MISSING` (`runtime-service.ts:664-670`).
   - For the 006.8/018.16 pair, the Disposition change to IMPLEMENTED_DIFFERENTLY and the addition of R4-Q1 both follow. They are consistent with the HELP_HUMAN clarification that TEST_ONLY code does not meet a product claim.
   - One drafting issue, not refuted: in the CLM-006.12 ProposedValue, the gloss "(used by chat-organization.ts:47 labels)" now follows `redactJsonLike`, but it belongs to `redactConfiguredApiKeys` (:81).
2. **Some guarantee rows are graded ALIGNED because their named surfaces exist, though the live control is weak.** This applies to CLM-006.5 and CLM-007.6 (human gate / lifecycle).
   - The live transition route requires `actor=HUMAN` and an approvalSha for CHECKING/ISSUED.
   - However, the actor is asserted by the caller, and the SHA is checked for format only.
   - The route has no live UI caller (CAP-WORKSPACE-022).
   - No live control stops a Codex agent under the default workspace-write sandbox from writing `_STATUS.md` directly. The legacy harness had no `_STATUS.md` write guard either.
   - The subject test reads "non-delegable" as a guarantee, which admits PARTIALLY_IMPLEMENTED. I graded both CONTESTED. The SEE target CLM-006.9 (another shard) would move with them.
3. **The CLM-011.1 RemainingWork erratum overstates its case.** The erratum says "all 13 exercise only LEGACY_ONLY modules". That is true of the manifest `evidenceFiles`, but two IDs' tests also import LIVE modules:
   - `instruction_root_protection_hook` → `lib/harness/instruction-root.ts`;
   - `chirality_mcp_status_dependencies` → `lib/dependencies/register-{reader,writer}.ts`.

   Also, the sealed "12 of 13" rested on `session-manager.ts`, which is the evidence file of `sdk_session_link_resume`, not one of the 13 implemented rows in the index. The Disposition is unaffected.
4. **Class c:** all 14 PARTIAL responses are genuine partial coverage by a register boundary row. I found no clearer owner key in the ledger. The register citations were confirmed, including `scan-secret-evidence.mjs` at `reliance_boundary_register.md:53` and the build-time integrity test at :94.
5. **Clean rows:**
   - REGISTER-1: the hash recompute matches the pack. CONTRACT changed after the v23 tranche (`7f1e9f387`, `95b342519`).
   - CLM-051: STALE_SPECIFICATION with R4-Q1.
   - CLM-010.3 and CLM-018.20: ALIGNED.
   - CLM-041 and CLM-059.1: NOT_AUDITABLE.
   - Line anchors are within 0–6 lines. The register test index is cited as 79-97; the table is at about 84-99.

## (iii) Effort

- **Read:** about 30 files or ranges in the frozen tree (SoW, `_REFERENCES`, MEMORY, the register doc, the Section 9 manifest and script, lifecycle and route code, Runtime composition, service, coordinator, supervisor and app-server client, run-logger callers, facade importers), plus the run inputs.
- **Git:** two read-only `git log` calls.
- **Not read:** Root `execution/`, `chirality-runtime/execution/`, R0 ledgers, other package folders and the other shard's output.
- The context budget was comfortable.
