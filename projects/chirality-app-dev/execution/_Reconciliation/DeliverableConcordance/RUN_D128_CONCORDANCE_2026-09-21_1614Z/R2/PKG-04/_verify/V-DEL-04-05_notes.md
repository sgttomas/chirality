# V-DEL-04-05 — verifier shard notes (R2, PKG-04)

Graded against the shared `GRADING_KEY.md` and `CONVENTIONS.md`, with all evidence read at the frozen basis `00115c719`.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (must-check) | 8 | 2 | 1 | 5 |
| n (30% non-ALIGNED) | 15 | 13 | 2 | 0 |
| b (15% ALIGNED) | 1 | 1 | 0 | 0 |
| c (reverse responses) | 4 | 4 | 0 | 0 |
| e (errata) | 8 | 8 | 0 | 0 |
| **Total** | **36** | **28** | **3** | **5** |

- **Disposition-level refutation:** one, `DEL-04-05#CLM-030`. The row says ALIGNED; the evidence supports PARTIALLY_IMPLEMENTED. Its DirectionEvidence, CauseTag and RemainingWork change with it.
- **Field-level refutations:** two, both on ImplementationEvidence.
  - `#CLM-004`: the cited `codex-supervisor.ts:104-108` is the sandbox `networkAccess` policy. It does not show that Codex is the default engine; `app-owned-composition.ts:214` does.
  - `#CLM-012`: the row tags the whole of `api-key-storage.ts` as REACH=LIVE. Its storage symbols are TEST_ONLY.
- **Method for class n rows that have errata.** I graded the row with its errata applied, and marked the reach defect the erratum repairs as `GRADING_KEY 1 (fixed by errata)`. I did not count it again as a refutation.

## (ii) Systematic patterns

1. **Reach of `api-key-storage.ts` taken at module level.** The evidence pack marks the module LIVE only because `api-key-ipc.ts:2` imports `isProviderCredentialId`. Every storage symbol, including `SafeStorageCredentialStore`, is imported only by `src/__tests__` files.
   - The worker's eight errata correct this, and all eight are CONFIRMED.
   - The errata miss `#CLM-012`, which is refuted here. `#CLM-020` also cites the module, but only through its test file, so its tag is not affected.
   - No Disposition changes, because the live credential port is a stub anyway (`app-owned-composition.ts:225`).
2. **A Codex-era ruling undercutting unamended GOVERNING clauses without naming them.** Four a-class rows turn on this: `#CLM-009.10`, `#CLM-009.14`, `#CLM-024` and `#CLM-026`.
   - `#CLM-024` is a clean AUTHORITY_CONFLICT and is CONFIRMED. App DIRECTIVE 2.8 is unamended, and App §0 ranks it above the CONTRACT/SPEC/PRD Codex-only preambles.
   - The other three are CONTESTED:
     - K-NET-1's "remote MCP/providers fail closed" against D-GOV-43 item 3, which says there is no effective-configuration veto (proposal lines 178 and 186);
     - unamended K-ENGINE-4 against K-EVENT-6 as amended, plus the live `codex.notification` event type (`v2-events.ts:22-25`);
     - the DIRECTIVE 2.8 ownership list against D-GOV-43 custody and transport.
3. **LOW rows judged without tracing the live path.**
   - `#CLM-030`: the worker's own least-confident note already names PARTIALLY_IMPLEMENTED as the alternative, and the live-path search confirms it.
   - `#CLM-009.9` stays CONTESTED between IMPLEMENTED_DIFFERENTLY and ALIGNED, the same split as R0 VERIFICATION §3 #52.
4. **A dated History entry graded as a current-state assertion.** `#STATE-3` restates a 2026-09-03 `_STATUS` History entry. Under MR-8 (iv), a claim true only of its snapshot is a register row, so the Disposition is CONTESTED.

Checks that held, grouped by field:

- **PostReleaseBasis = NO:** held everywhere. The touched lines in `app-owned-composition.ts` (180, 214, 225) and `codex-supervisor.ts` (104-108) blame to `95364569ae` or `95b3425195`, which are not among the four post-release commits.
- **MechanicallyUnblocked:** `NO` with `MOOT:D-APP-127` on `#REM-1` is correct under D-APP-127 lines 62-64 and 98-109.
- **R0 repairs** are in place:
  - `#CLM-028` no longer contradicts `#CLM-009.6`/`.7`.
  - `#CLM-010` and `#CLM-012` are now REQUIREMENT rows, so their AuthorityTier is consistent.

## (iii) Capability-file accuracy

- **CAP-ELECTRON-019, -032, -033, -034 and CAP-HARNESS-031:** the REACH and STATE tags hold at the frozen tree.
- **CAP-ELECTRON-034:** it correctly records symbol-level TEST_ONLY for the store, while the pack says the module is LIVE.
- **CAP-ELECTRON-032:** its mention of a legacy mount at `shell-frame.tsx:302` was not verified. Line 404 passes `hosted`, which I confirmed.
- No inaccuracy found.

## (iv) Effort

- **Reading:** about 30 file reads or greps at the frozen tree. These covered:
  - the deliverable's ScopeOfWork, `_STATUS`, `_REFERENCES`, INSP-03 and `_CONTEXT`;
  - App DIRECTIVE §0/§2.8 and CONTRACT K-NET-1, K-KEY-1, K-ENGINE-4 and K-EVENT-6;
  - D-APP-127 and D-GOV-43 (record and proposal);
  - the code: api-key-storage, api-key-ipc, app-owned-composition, codex-supervisor, v2-events, delegated-engine-adapter, the anthropic and claude SDK managers, sdk-options-builder, settings-view, shell-frame, preload and main.
- **Git:** five read-only `blame -L` calls against the frozen tree.
- **Context budget:** comfortable.
