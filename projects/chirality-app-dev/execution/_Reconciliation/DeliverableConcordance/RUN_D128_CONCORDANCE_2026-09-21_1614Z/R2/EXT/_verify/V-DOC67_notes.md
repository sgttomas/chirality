# V-DOC67 verifier shard notes (RUN_D128 R2 EXT, item 6/7 ledgers, audit-only)

Output: `V-DOC67.csv`, 19 verdict lines covering 18 selected items. SHA-256
`274b9f1d0d2532be95c57ec75309c23e5fad24d08dc8f380ed704bb64a285ba8`.

## (i) Counts

Items checked: 18 (class a 3, class b 9, class c 6; no class e).

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 3 | 2 (README#0, RUNTIME_ENGINE_CONTRACT#4) | 1 (ADDING_A_TOOL#3) | 0 |
| b | 9 | 8 | 0 | 1 item (TOOL_CATALOG#1). ADDING_A_TOOL#1 is CONFIRMED on Disposition and CONTESTED on Notes |
| c | 6 | 6 | 0 | 0 |

Verdict lines by Field: Disposition: 1 REFUTED (ADDING_A_TOOL#3 → IMPLEMENTED_DIFFERENTLY), 1 CONTESTED
(TOOL_CATALOG#1). Notes: 1 CONTESTED (ADDING_A_TOOL#1, ALSO_MODULE missing). 16 CONFIRMED lines.
Verdict-field refutations: 1 of 18 distinct items (5.6%), which is under the Addendum 3 10% threshold.

## (ii) Patterns

1. **ACCEPTED_DIVERGENCE on the strength of a document banner (ADDING_A_TOOL#3).** The row restates
   CONTRACT hook and permission controls that only LEGACY_ONLY code meets. The file's own D-GOV-43 line
   calls the SDK path compatibility history. D-GOV-43 does not rule on K-HOOK or K-PATH, and those
   questions remain open as R4-Q1, which the row itself cites. No GOVERNING ruling therefore permits
   the difference. The same situation in RUNTIME_ENGINE_CONTRACT#4 was disposed
   IMPLEMENTED_DIFFERENTLY, so the worker applied the rule inconsistently across the two ledgers.
   ACCEPTED_DIVERGENCE does hold in RUNTIME_ENGINE_CONTRACT#1, because the Codex sole-engine rule
   directly governs the retired provider set.
2. **Upstream-preserving event representation disposed PARTIALLY_IMPLEMENTED with
   ALSO:STALE_SPECIFICATION (README#0, RUNTIME_ENGINE_CONTRACT#0, TRACEABILITY#2).** Upstream method and
   params do travel, but only nested in `harness:event` `codex.notification` inside the eight-name
   UIEvent envelope (delegated-engine-adapter.ts:209,282,289; agent-engine-port.ts:84,97). The
   `sdk_native_stream` check that the docs call history is a REQUIRED premerge ID run on the live route.
   The disposition is applied consistently and the alternative is recorded, so I confirmed all three.
3. **The legacy-only tool surface: DOCUMENTED_UNIMPLEMENTED versus IMPLEMENTED_DIFFERENTLY
   (TOOL_CATALOG#1), and Addendum 6 rule 4 (ADDING_A_TOOL#1).** The live path has no `mcp__chirality__`
   tool and the App registers no application-tool catalog, so the §2.3 "lacks it" branch is arguable.
   ADDING_A_TOOL#1 cites R4-Q1 because its product-path exposure steps are met only by legacy code, but
   it records no `ALSO_MODULE:`.

Minor slips recorded in ConventionIssue, not refuted: in RUNTIME_ENGINE_CONTRACT#1, Codex's sole-engine
registration is at app-owned-composition.ts:214, not :226. All REACH tags matched REACHABILITY.csv.
PostReleaseBasis NO held on every row: the codex-supervisor.ts:705-710 and app-owned-composition.ts:214/226
citations fall outside the TOUCHED_PATHS ranges, and no docs/harness or instructions file is listed.
AUDIT-ONLY is present on every non-ALIGNED, non-NOT_AUDITABLE row; NOT_AUDITABLE is non-divergent per
validator NON_DIVERGENT. No Q-01..Q-13 misuse and no OTHER: tokens.

## (iii) Effort

About 30 file reads or greps: the five harness docs and the product AGENTS.md, runtime contracts and core
adapter lines, app scripts, the register rows D-APP-47/89/127, D-GOV-43, the evidence pack, the gate
transcript, and two blames (README.md:104, run-network-policy-proof.mjs:13-17,72-78). No Root
`execution/**`, runtime execution, other R2 folders or R0 ledgers were read. The context budget was
comfortable.
