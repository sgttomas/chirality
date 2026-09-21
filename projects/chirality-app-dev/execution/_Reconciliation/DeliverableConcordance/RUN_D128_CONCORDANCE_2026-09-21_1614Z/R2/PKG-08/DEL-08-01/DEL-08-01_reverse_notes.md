# DEL-08-01 — reverse-pass notes (RUN_D128 R2 PKG-08, rerun)

## Inputs

- **Areas:** BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT and RTCORE, from `R2/SURFACES/<AREA>_capabilities.csv` and `<AREA>_notes.md`.
- **Validator input:** `REVERSE_INPUT_capabilities.csv`, 283 rows.
- **Sealed ledger SHA-256:** `dee44036769cc35a59e79d5181e2de584270f2d3591533b28e30f6d1c4492790`. Re-checked after this pass and unchanged.

## Responses

| Response | Rows | Capabilities |
|---|---:|---|
| CLAIMED_BY | 2 | CAP-BUILD-007 (integrity verifier) → CLM-005.2; CAP-HARNESS-041 (agent conformance validator) → CLM-005.1 |
| PARTIAL | 14 | See the list below |
| NOT_MINE | 267 | Everything else |

The 14 PARTIAL capabilities are:

- BUILD-006 and 013;
- ELECTRON-006;
- HARNESS-025, 026, 045, 047 and 058;
- ROUTES-026, 034 and 035;
- RTCORE-010, 035 and 042.

Each PARTIAL capability implements behaviour that DEL-08-01 *verifies* but does not own: packaging, separation, path policy, the governance bridge, or registry and role loading. DEL-08-01 is a TEST_SUITE deliverable, so it claims only the checks themselves.

## Errata (2 rows, Field = ImplementationEvidence)

**CLM-009.12 and CLM-009.14.** The sealed rows tagged `native-role-config.ts` (`loadTrustedNativeRoleConfiguration` / `readRole`) `REACH=LIVE`.

- `REACHABILITY.csv` marks that module LIVE, but only through the core barrel.
- CAP-RTCORE-042 and a grep confirm the functions have no product caller. The only product path is `product-native-role-config.ts` `materializeProductNativeRoles`, reached through `delegated-engine-adapter.ts:213`.
- The proposed values re-tag the loader `REACH=TEST_ONLY` and add the live module.
- Dispositions are unchanged: IMPLEMENTED_DIFFERENTLY in both cases. The live path is still Codex-native delegation that parses no frontmatter.
- The CLM-009.12 VerificationEvidence cites `tests/native-role-config.test.ts`. That test exercises the non-product loader, so it is weaker live-path evidence than the row implies. I raised no separate erratum, because the token and the file are accurate.

## Coverage gaps (no forward row missing)

No capability exposes a DEL-08-01 obligation that lacks a forward row.

Two observations for the manager:

1. **CAP-RTCORE-016 (cross-deliverable).**
   - Runtime `RuntimeService.listAgents` (`runtime-service.ts:587-620`) still derives agent type and class by regex from the SPEC §7 `AGENT_TYPE` / Agent Type table text in `agents/AGENT_*.md`.
   - The shipped v3 role files carry neither, so this route would return all four roles untyped. With `directChat=1` it would return an empty list.
   - The App roster no longer calls it. `runtime-daemon-harness-port.ts:449-466` projects `listRoles` instead, so there is no product impact at the frozen basis.
   - It is a live Runtime consumer of the unamended SPEC §7 format. It supports the CLM-009.7/009.8 finding and the `R4` question, and belongs to the roster-owning PKG-08 deliverable.
2. **CAP-ELECTRON-006.**
   - The Electron main process resolves the instruction root itself: `CHIRALITY_INSTRUCTION_ROOT`, the packaged Resources path, or an ancestor search for agents/, AGENTS.md and docs/DIRECTIVE.md. It exports the result to the Next routes.
   - So the `docs/PLAN.md` entry in `lib/harness/instruction-root.ts:6-14` (noted in CLM-009.3) applies only when that env variable is absent. In the packaged product it does not gate resolution.
   - The CLM-009.3 note is accurate as written, but should not be read as a live runtime requirement for PLAN.md.

## Validation

- `reverse`: `RULES errors none | warnings none`; `RESULT PASS errors=0 warnings=0`.
- `errata`: `RULES errors none | warnings none`; `RESULT PASS errors=0 warnings=0`.
