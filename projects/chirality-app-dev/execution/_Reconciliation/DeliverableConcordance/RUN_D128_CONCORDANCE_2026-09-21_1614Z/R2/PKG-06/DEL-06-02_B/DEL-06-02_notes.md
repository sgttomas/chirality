# DEL-06-02 — forward-pass notes (worker B, double-blind)

Deliverable: `DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation` (PKG-06), lifecycle `IN_PROGRESS`,
no Remaining items. Basis: frozen tree `00115c719`. Ledger: `DEL-06-02_claims.csv` (56 rows).

## 1. Census

**Rows:** 56 in total.
- 48 rows cover the 35 indexed units.
- 4 are `REGISTER-n` rows and 4 are `STATE-n` rows.

**Split rate:** 2 of 35 units (5.7%).
- `CLM-010` is split into `.1`–`.13`, one row per DEL-06-02-REQ-001..013. These items are separately numbered but are not listed in `SubItems`.
- `CLM-035` is split into `.1` (AC-002) and `.2` (VER-002), as `V-SUBITEMS` requires.
- `CLM-015` (AC-001) and `CLM-021` (VER-001) each hold a single item and get one row each.

**By Disposition** (SEE rows are included here and also counted separately below):

| Disposition | Rows |
|---|---:|
| IMPLEMENTED_DIFFERENTLY | 16 |
| STALE_SPECIFICATION | 12 |
| PARTIALLY_IMPLEMENTED | 8 |
| NOT_AUDITABLE | 7 |
| REMAINING_STATE_MISMATCH | 6 |
| AUTHORITY_CONFLICT | 4 |
| ALIGNED | 3 |

**By ClaimType:**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 22 |
| STATE_ASSERTION | 14 |
| CONTEXT_CLAIM | 9 |
| ACCEPTANCE | 7 |
| REGISTER_DEFECT | 4 |

**SEE rows (MR-4), 7 in total:**
- `CLM-008`, `CLM-016`, `CLM-022` and `CLM-029` point to `CLM-001` (REMAINING_STATE_MISMATCH).
- `CLM-013` and `CLM-014` point to `CLM-006` (STALE_SPECIFICATION).
- `CLM-027` points to `CLM-010.7` (IMPLEMENTED_DIFFERENTLY).

**Without SEE rows:** 49 rows, as follows:

| Disposition | Rows |
|---|---:|
| IMPLEMENTED_DIFFERENTLY | 15 |
| STALE_SPECIFICATION | 10 |
| PARTIALLY_IMPLEMENTED | 8 |
| NOT_AUDITABLE | 7 |
| AUTHORITY_CONFLICT | 4 |
| ALIGNED | 3 |
| REMAINING_STATE_MISMATCH | 2 |

**Errata:** none (forward pass only).

## 2. Least-confident rows

- **`CLM-010.3`** (REQ-003, SDK built-in names), LOW, `IMPLEMENTED_DIFFERENTLY`.
  - Alternative reading: SPEC §14.1 is worded for the "first-adapter SDK". The retained registry models
    `Read`/`LS`/`Glob`/`Grep`/`Write`/`Edit`/`Bash` in `tool-descriptor.ts:13-25`, so a module-level
    reading would give `ALIGNED`.
- **`CLM-010.9`** (REQ-009, `allowedTools` is not a boundary), MEDIUM, `IMPLEMENTED_DIFFERENTLY`.
  - Alternative reading: `ALIGNED`. The live path has no `allowedTools`. Restriction comes from the
    mode mapped to a Codex sandbox and approval policy, and "mode policy" is one of K-PERM-3's listed
    mechanisms.
- **`CLM-010.5`, `.6` and `.10`, and `CLM-024`** (`AUTHORITY_CONFLICT`).
  - Alternative reading: `DOCUMENTED_UNIMPLEMENTED` on the live path.
  - I chose the conflict reading because K-TOOL-1, K-TOOL-2 and SPEC §14.3 are unamended, while
    D-GOV-43 makes the stock Codex tool surface and the user's configuration authoritative without
    naming these clauses.
  - These clauses are not among R4-Q1's listed clauses (K-PATH, K-ROOT, K-HOOK, SPEC §15.2). R4-Q1 is
    still the nearest framed question.
- **`CLM-035.1`** (AC-002), `IMPLEMENTED_DIFFERENTLY` / `RUNTIME_EXTRACTION`.
  - Alternative reading: `ALIGNED` at module level. The four names and descriptors exist,
    collision-checked. The divergence I recorded is that the surface now lives in the Runtime-owned
    `runtime-contracts` package, and the SoW's cited App files are deprecated facades.
- **`CLM-032`** (Examples), `STALE_SPECIFICATION`.
  - Four of the five examples track `CLM-010.x` (legacy-only). Only the `domain_*` example is stale
    under D-APP-50 and D-APP-56.
  - Alternative reading: `IMPLEMENTED_DIFFERENTLY`.

## 3. Register-defect summary

- **REGISTER-1:** `_REFERENCES.md` REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record MATCH
  hashes that do not reproduce (`HASH-RECOMPUTE@00115c719`).
  - The hashes were repinned mechanically in the D-GOV-43 tranche commit `23b3879b3`, without revising
    the SoW or `_CONTEXT.md`.
  - Later edits were not repinned: CONTRACT in `95b342519` and `7f1e9f387`; SPEC and PRD in `9eaddb596`.
  - REF-001, REF-004, REF-005 and REF-007 still reproduce; I recomputed DIRECTIVE, TYPES and PLAN myself.
  - REF-008 is missing from the numbering.
  - Rows that restate it: `CLM-001`/`008`/`016`/`022`/`029` (D-APP-56 notes), `CLM-007`, `CLM-018`,
    `CLM-033`, and the MATCH fragments in `CLM-003`/`004`/`019`/`020`.
- **REGISTER-2:** `_DEPENDENCIES.md` still declares "TBD — no accepted dependency edges" upstream and
  downstream. The same file, and `Dependencies.csv`, list 11 ACTIVE rows.
- **REGISTER-3:** `Dependencies.csv` marks `DEP-06-02-011` SATISFIED on the premise that REF-006 is
  MATCH. That premise no longer holds.
- **REGISTER-4:** `_STATUS.md` shows "Last Updated 2026-07-12", but its History has entries dated
  2026-07-19 and 2026-07-20, and the History is not in chronological order.
- **Stale TBD sets (`CLM-006`, `013`, `014`, `021`):** implementation, registry, test and fingerprint
  paths are still marked TBD. They existed by 2026-06-21 (INSP-03, ADQ-11).
- **Stale conflict table (`CLM-033`):** it still says "no direct source conflict".
- **Stale evidence paths (`STATE-3`):** `Evidence_ADQ-11` cites `frontend/src/lib/harness/sdk-version.ts`
  and `mcp/tool-names.ts`, which are absent at the frozen basis.

## 4. Direction and cause

**Primary CauseTag: `CODEX_SOLE_ENGINE` (29 rows).**
- The SoW specifies a Claude-SDK read-tool resolver.
- On the live path (App → Runtime → Codex):
  - The operator's `opts.tools` (`toolkit.ts:137-146`, LIVE) reach Runtime `restrictRequestedTools`
    (`runtime-method-service.ts:507-519`). That function filters names by role, method and mode, and
    rejects names it does not admit with a structured 422 error. It keeps no registry of known names.
  - The admitted list is never forwarded to Codex: `delegated-engine-adapter.ts:231` passes `[]`, and
    `delegated-runtime.ts:289` ignores its `_runtimeTools` argument.
  - Codex exposes its native tools under a sandbox and approval policy derived from the mode
    (`delegated.ts:322-330`, `codex-supervisor.ts:104-106`).
- The descriptor registry, `resolveHarnessToolPool`, the SDK options builder and the ADQ-11
  fingerprint are LEGACY_ONLY. The registry module in `runtime-contracts` is LIVE only through the
  barrel export.
- The live boot fingerprint has placeholder tool fields (`runtime-service.ts:559-583`).
- DirectionEvidence: `GOV:D-GOV-43` on these rows.

**Other CauseTags:**
- `DOC_HYGIENE` (11): hash and register drift.
- `PRE_V3_DRIFT` (5): TBD paths and the missing canonical sort. The legacy pool keeps request order
  after deduplication; no permuted-order fixture exists.
- `RUNTIME_EXTRACTION` (1): `CLM-035.1`, with `GOV:D-APP-73` and `GOV:D-APP-89`.

**CAUSE2 secondaries:** `RUNTIME_EXTRACTION`, `PRE_V3_DRIFT`, `DOC_HYGIENE`, `CARRIER_PROPAGATION`,
`A2_TOPOLOGY`, `FACADE_DEPRECATION`.

**Carrier propagation:**
- No DEL-06-02 carrier cites D-GOV-43 or D-APP-127; the D-APP-127 application map shows every carrier
  `NO`.
- `_CONTEXT.md` still names the Claude Agent SDK as the "first concrete/current path" and speaks of
  "daemon" exposure and conformance (`STATE-1`).
- The Runtime application-tool catalog is the live analogue of the `_CONTEXT`/D-APP-80 "App/project
  catalog, collision prevention" scope (`STATE-2`, `CLM-009`, PostReleaseBasis `YES`).
  - It arrived post-release in `da95ec194`; I verified this by blame on `application-tools.ts:48-66`
    and `codex-supervisor.ts:219` and `653-657`.
  - It has no DEL-06-02 carrier record, and the App registers no tools into it.
  - `codex-supervisor.ts:104-106` blames to `95364569ae`, so PostReleaseBasis is `NO` there.

**MR-11:** applied to `CLM-032` only, where D-APP-56 R4-P27 explicitly reconciles the domain-tool
wording.

**`NONE_FOUND` searches:**
- `_DECISIONS/_REGISTER.md`, searched for `DEL-06-02`, "tool surface", `opts.tools`, "dynamic tool",
  "application tool", `runtime-contracts` and `harness-contract`. The only hits were D-APP-43, 55, 56,
  68, 70, 80, 89 and 127; none addresses the live tool surface.
- `APPDEV_V3_NODE_*` AgentRuns and `plans/steers`: no DEL-06-02 or tool-surface direction. The only
  NODE_E hit is a generic "read-first set".
- R4 questions: every live-path divergence cites `R4-Q1`. Done-declaration questions are not cited.

## 5. Method friction

- **MR-8(iv) versus the CONTEXT_CLAIM rule.** A CONTEXT_CLAIM references table that restates a
  snapshot MATCH (`CLM-007`) may only take `STALE_SPECIFICATION` or `NOT_AUDITABLE`, yet MR-8(iv) says
  snapshot claims are not STALE_SPECIFICATION.
  - I used `STALE_SPECIFICATION` citing REGISTER-1 for `CLM-007`, and `REMAINING_STATE_MISMATCH` for
    the STATE_ASSERTION restatements.
  - Proposal: state explicitly which disposition SoW restatements of a REGISTER hash row take.
- **R4-Q1's clause list.** It names K-PATH, K-ROOT, K-HOOK and SPEC §15.2 only. This deliverable's
  conflicts are with K-TOOL-1, K-TOOL-2, K-PERM-3/4 and SPEC §14.3.
  - Proposal: widen R4-Q1 to "any CONTRACT §1.6 / SPEC §14–15 tool-surface clause", or frame a new
    question.
- **Barrel-only reach.** `REACHABILITY.csv` marks `runtime-contracts` `tool-descriptor.ts` and
  `tool-names.ts` LIVE through the contracts barrel, while their functional consumers are LEGACY_ONLY.
  I tagged them LIVE and explained the split in Notes. Symbol-level reach would help.
- **Numbered REQs not in `SubItems`.** `DEL-06-02-REQ-nnn` items are not in `SubItems`, because the
  index only lists bare REQ-/AC-/VER- ids. I split them anyway under the "separately numbered" rule.

## 6. Effort

- About 45 files and slices read:
  - deliverable: 9 files;
  - evidence pack and R1: 7;
  - App frontend: about 12;
  - Runtime packages: about 12;
  - tests: 6;
  - decisions: 4.
- Git use: read-only `blame -L`, `log` and `show` on the frozen tree.
- Context budget: moderate, not tight.
