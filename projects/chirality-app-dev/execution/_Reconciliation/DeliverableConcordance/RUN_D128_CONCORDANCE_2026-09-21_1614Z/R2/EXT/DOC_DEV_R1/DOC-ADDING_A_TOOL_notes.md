# DOC-ADDING_A_TOOL — notes (item 7 rerun, fresh worker)

Source: `projects/chirality-app-dev/frontend/docs/harness/adding_a_tool.md` at `00115c719`.
Ledger: `DOC-ADDING_A_TOOL_claims.csv` (8 rows, sealed, SHA-256
`655604ed7d20dc6c00070e1fd6f13340b644f1c225fe4851e0973890de9c8f26`). Audit-only (item 7).
The earlier attempt (`R2/EXT/DOC_DEV/`) and `_verify/` were not read.

## 1. Census

| ClaimType | Rows |
|---|---|
| CONTEXT_CLAIM | 1 (#0) |
| REQUIREMENT | 7 (#1–#7) |

| Disposition | Rows | Keys |
|---|---|---|
| ALIGNED | 2 | #2, #7 |
| IMPLEMENTED_DIFFERENTLY | 3 | #1, #3, #6 |
| DOCUMENTED_UNIMPLEMENTED | 2 | #4, #5 |
| STALE_SPECIFICATION | 1 | #0 |

- Split rate: 0/8. No section holds numbered REQ/AC/VER items or a table of independently
  dispositionable rows; the numbered steps in #1 and #3 are one procedure each.
- SEE rows: 0. Run-local rows: 0. No errata.
- HumanDecisionNeeded: `R4-Q1` on 5 rows (#1, #3, #4, #5, #6); `NO` on 3.
- ACCEPTED_DIVERGENCE: 0. The preamble's D-GOV-43 banner calls the SDK path
  "compatibility history". That is the document's own note, not a GOVERNING ruling that
  permits this difference, so the live path was judged by the normal vocabulary.

## 2. Least-confident rows (with alternative readings)

No row is LOW. MEDIUM rows and their alternatives:

- **#1 Required Sequence.** Read as product behaviour, because step 4 states a control on
  tool exposure (K-TOOL-2; rules 1–2). Alternative: a module-level developer procedure,
  giving `STALE_SPECIFICATION` (steps 1–2 name removed files) without R4-Q1. Recorded as
  `ALSO_MODULE:STALE_SPECIFICATION`.
- **#4 In-Process MCP Path.** `DOCUMENTED_UNIMPLEMENTED` because the live path has no
  Chirality MCP server. Alternative: `IMPLEMENTED_DIFFERENTLY`, treating Codex's approvals as
  "another mechanism". Module reading `PARTIALLY_IMPLEMENTED`: the coordination tools
  (`delegate_agent`, `report_coordination_notice`, `send_agent_update`) have `mutating`
  descriptors but do not use the handler-level wrapper. They are mode-gated only at pool
  resolution. Whether they "mutate project state" (the doc's K-MCP-1 bypass test) or only
  runtime control-plane records is open.
- **#5 Reserved Names.** Alternative: a module contract for the named tools, giving
  `ALIGNED` without R4-Q1.
- **#6 Agent Tool Exception.** CauseTag `NATIVE_DELEGATION` (primary), with
  `CAUSE2:CODEX_SOLE_ENGINE`. The two could be swapped.
- **#7 Catalog and Test Gates.** `ALIGNED`, but the guide leaves out that the generator
  and tests import the *built* `@chirality/runtime-contracts` dist. After a descriptor edit,
  the Runtime contracts must be rebuilt before the catalog is regenerated. Read as a missing
  step, not a false statement. A stricter reader might give `PARTIALLY_IMPLEMENTED`.

## 3. Register-defect summary

None. This is a developer document with no `_STATUS`, `_REFERENCES` or register carrier.

## 4. Direction and cause

- CauseTags: `CODEX_SOLE_ENGINE` ×4 (#1, #3, #4, #5), `NATIVE_DELEGATION` ×1 (#6),
  `PRE_V3_DRIFT` ×1 (#0). Secondaries: `CAUSE2:FACADE_DEPRECATION` (#0),
  `CAUSE2:PRE_V3_DRIFT` (#1), `CAUSE2:CODEX_SOLE_ENGINE` (#6). No `OTHER:` tokens.
- GOVERNING records used in DirectionEvidence:
  - `GOV:D-GOV-43`: Codex is the sole engine, so the legacy SDK/MCP path is not the product
    path.
  - `GOV:D-APP-47`: shim-importer migration and shim retirement. `git show ee290e22a`
    (2026-07-04) removed `frontend/src/lib/harness/tool-descriptor.ts` (renamed to
    `tool-pool.ts`) and the `mcp/tool-names.ts` shim. The registry now lives in
    `projects/chirality-runtime/packages/contracts/src/harness/`.
- `LatestDecision = NONE_FOUND` (#2, #7): I searched the App `_DECISIONS/_REGISTER.md` for
  `tool-descriptor`, `runtime-contracts`, `harness-contract`, `adding_a_tool`,
  `tool_catalog` and `docs/harness`. Only D-APP-46/47/48/49/89 matched, and each concerns
  package extraction or facade posture, not descriptor fields or catalog gates. No
  DirectionEvidence `NONE_FOUND` was needed.
- R4-Q1 by rule 3 and the Addendum 8 reading. On #1 and #3–#6, the only code meeting the
  claim on the product path is `REACH=LEGACY_ONLY`: `sdk-options-builder`, `tool-pool`,
  `chirality-hooks`, `mcp/read-tools`, the domain runner, `subagent-*` and
  `permission-overlay`. All are UNREACHED from product entries (HARNESS CAP-031/040/050–058
  `STATE=DISABLED`). The runtime `tool-descriptor.ts` is `REACH=LIVE` in the pack only
  through the contracts barrel (CAP-RTCONTRACT-042 says its consumers are legacy). So #2, a
  claim about the registry alone, does not cite R4-Q1.
- R4-Q6 is not cited. No row turns on whether DIRECTIVE §2.8/§2.10/§4.1/§4.2 or
  K-PERM-1/K-PERM-6 bind. R4-Q3 (`status_transition` actor) is not the subject of #4.
- PostReleaseBasis `YES` only on #4. It cites
  `chirality-runtime/packages/daemon/src/application-tools.ts:24`, and `TOUCHED_PATHS.csv`
  lists lines 1–155 of that file under `da95ec194`. No other cited file is on the list.
- Done-declaration questions: none relied on.

## 5. Method friction

- Build and validation scripts are outside `REACHABILITY.csv`: `generate-tool-catalog.mjs`
  and `validate-harness-premerge.mjs`. I tagged them by use (npm developer/CI scripts, no
  product entry), following BUILD CAP-036/025, and said so in Notes.
- `LifecycleState` has no `_STATUS` source for a harness developer document, so I wrote
  `NOT_APPLICABLE`. Proposal: give extension DOC rows a fixed value in CONVENTIONS §8.
- Static REACH for runtime contracts modules (LIVE through the barrel) differs from their
  effective reach (legacy consumers). Rule 3 keys on the tag, so a registry-only claim
  escapes R4-Q1 while claims about its consumers cite it. Proposal: a pack note that marks
  barrel-only LIVE rows.

## 6. Effort

About 20 files or ranges read: the source document, the runtime tool descriptor, the
harness modules `sdk-options-builder`, `read-tools`, `coordination-tools`, `subagent-*`,
`tool-path-policy` and `permission-overlay`, the domain runner, the generator script, two
test files, `package.json`, register rows, capability files and the gate transcript. The
context budget was not tight.
