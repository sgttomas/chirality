# DEL-01-02 — S2 notes (SoW Praxeology + Axiology, CLM-024..CLM-060)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, frozen basis `00115c719`, PKG-01 wave 4, split S2.
Ledger: `DEL-01-02_claims.csv` (44 rows, forward pass, sealed on return). No run-local rows were
needed in this half (none numbered from 51).

## 1. Census

Rows: 44, covering 37 indexed units (CLM-024..CLM-060).

| Disposition | Rows |
|---|---:|
| NOT_AUDITABLE | 19 |
| STALE_SPECIFICATION | 11 (of which 3 SEE rows) |
| PARTIALLY_IMPLEMENTED | 6 |
| ALIGNED | 4 |
| AUTHORITY_CONFLICT | 2 |
| REMAINING_STATE_MISMATCH | 2 |

| ClaimType × Disposition | Rows |
|---|---:|
| CONTEXT_CLAIM × NOT_AUDITABLE | 19 |
| CONTEXT_CLAIM × STALE_SPECIFICATION | 1 (CLM-032) |
| STATE_ASSERTION × STALE_SPECIFICATION | 8 |
| STATE_ASSERTION × REMAINING_STATE_MISMATCH | 2 (CLM-059.3, CLM-059.5) |
| STATE_ASSERTION × ALIGNED | 1 (CLM-058) |
| REQUIREMENT × PARTIALLY_IMPLEMENTED | 4 (CLM-043, 047, 050, 052) |
| REQUIREMENT × ALIGNED | 3 (CLM-042, 045, 046) |
| REQUIREMENT × AUTHORITY_CONFLICT | 2 (CLM-040, 044) |
| REQUIREMENT × STALE_SPECIFICATION | 2 (CLM-049, 051) |
| ACCEPTANCE × PARTIALLY_IMPLEMENTED | 2 (CLM-036, CLM-038.4 VER-001) |

- **SEE rows (counted separately):** 3. CLM-057 → CLM-026; CLM-059.2 → CLM-051; CLM-059.4 → CLM-032.
  All are STALE_SPECIFICATION. Excluding them, the non-SEE census is 41 rows, 8 of them STALE_SPECIFICATION.
- **Split rate:** 2 of 37 units split (5.4%). CLM-038 → 4 rows (BLK-RBR-001..003 plus VER-001, its only
  SubItem). CLM-059 → 5 rows (ASSUMPTION-RBR-001, TBD-RBR-001..004). Both are tables of independently
  dispositionable rows. CLM-036 (a 9-item verification table) and CLM-051 (a 7-row surface table) are
  kept as single rows, with the failing items named in Notes.
- **HumanDecisionNeeded:** NO 36; `R4-Q1` 7; `R4; R4-Q1` 1 (CLM-040).
- **Confidence:** HIGH 25, MEDIUM 15, LOW 4.
- **PostReleaseBasis YES:** 3 (CLM-038.3, CLM-044 via `codex-supervisor.ts:219` → `da95ec194`; CLM-040 via
  `app-owned-composition.ts:170-171` → `da95ec194`).
- No errata file (pass 1).

Classification choice: the Procedure steps (CLM-025..CLM-035, CLM-037) are method notes, so they are
`CONTEXT_CLAIM`. They are `NOT_AUDITABLE` unless they make a checkable now-false assertion. CLM-026 is
reclassified as `STATE_ASSERTION`, and CLM-032 stays a CONTEXT_CLAIM with STALE_SPECIFICATION.
Guidance principles (CLM-040, 042–047) and the normative considerations (CLM-049–052) are REQUIREMENT
rows.

## 2. Least-confident rows

- **CLM-038.2 (BLK-RBR-002), LOW, STALE_SPECIFICATION.** Alternative reading: the blocker is still open
  in substance, because the register names no live Codex-path surfaces. On that reading the text is
  accurate (ALIGNED). I chose STALE because the blocker's stated closure route (downstream filling of
  paths) has happened, and the SoW itself marks TBD-RBR-001 RESOLVED.
- **CLM-038.3 (BLK-RBR-003), LOW, STALE_SPECIFICATION.** Alternatives:
  - ALIGNED at module level, if the retained Claude adapter still carries the probe obligation (R4-Q1).
  - AUTHORITY_CONFLICT between unamended K-SDK-1/K-SDK-3 and amended K-ENGINE-3.
  I rejected AUTHORITY_CONFLICT because K-SDK-1 is conditional on the Claude adapter.
- **CLM-059.3 (TBD-RBR-002), LOW, REMAINING_STATE_MISMATCH.** Alternative: the TBD is still open for the
  legacy Claude SDK transcripts (ALIGNED). The Codex-path storage decision exists in amended K-EVENT-4
  and D-GOV-43 item 5.
- **CLM-059.5 (TBD-RBR-004), LOW, REMAINING_STATE_MISMATCH.** Alternative: ALIGNED, because schema and
  inventory validator automation is still absent. The register test checks only path existence and PEC
  wording, while register line 87 overstates it (an S1-domain observation).
- **Also borderline (MEDIUM):**
  - CLM-042 ALIGNED: RB-SETTINGS' ProductSemantic names Claude Code settings, which is arguably vendor
    wording; K-SDK-1 uses the same wording.
  - CLM-046 ALIGNED: the live transition route takes a caller-asserted `actor`, which is a live analogue
    of R4-Q3. I did not cite R4-Q3 because no live Codex tool reaches the route.

## 3. Register-defect summary

This half has no REGISTER rows (S1 owns them from REGISTER-1). The S2 units that restate the
`_REFERENCES.md` hash drift are each dispositioned in full, with `cf. DEL-01-02#REGISTER-1` in Notes:

- CLM-026, CLM-038.1, CLM-049 and CLM-057 (SEE → CLM-026) restate REF-006 `MATCH` as current. The
  recorded PRD hash `8649ccba…` recomputes to `17ca3f3c…` at `00115c719`; CONTRACT and SPEC also fail
  to match (`REFERENCE_HASHES.csv`).
- CLM-029, CLM-036, CLM-047 and CLM-052 mention the drift as part of a wider finding.

Other register-like staleness found in this half:

- The SoW Procedure (CLM-032) and TBD-RBR-003 still call `section9.reliance_boundary_register` and
  `section9.sdk_session_link_resume` future IDs. Both are at `validate-harness-section9.mjs:34,36` and
  manifest `:38,:52`.
- The CLM-051 surface table gives a wrong path for `RuntimeEngineContract`. The symbol is defined at
  `projects/chirality-runtime/packages/contracts/src/harness/agent-engine-port.ts:90`, not in
  `frontend/src/lib/harness/agent-runtime-contract.ts`.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE, 9 rows: the SoW and register describe the in-process Claude SDK harness, but the
    live product runs Codex App Server in the App-owned Runtime service.
  - DOC_HYGIENE, 6 rows: reference-hash drift and TBD lag.
  - CARRIER_PROPAGATION, 4 rows: D-APP-56 annotations appended without revising the tables; the A2
    tranche revised only the SCA-APP-003 register rows.
  - PRE_V3_DRIFT, 2 rows: VER-001 checks, and the addendum reduced schema.
- **CAUSE2 secondaries:** CARRIER_PROPAGATION (most CODEX_SOLE_ENGINE and DOC_HYGIENE rows);
  CODEX_SOLE_ENGINE (CLM-047, CLM-052); FACADE_DEPRECATION (CLM-051, CLM-059.2); DOC_HYGIENE (CLM-032).
- **GOVERNING records used (`GOV:`):**
  - D-GOV-43 proposal packet (the ruling-record basis):
    - `D-GOV-43.proposed.md:20-28`: the Codex sole-engine rule is preserved.
    - Item 4 (`:187-195`): chosen approval and sandbox policy.
    - Item 5 (`:196-207`): continuity from Codex.
    - Item 8 (`:222-229`): upstream tool behaviour preserved.
    - `IMPACT.md:124`: the register revision is limited to RB-DAEMON, RB-CONTROL-SOCKET and RB-ROLE-MODEL.
    - `IMPACT.md` corpus-hashed docs row: "one corpus re-hash".
  - D-APP-56 (UPD-100/101/102, UPD-097).
  - D-APP-89 (facade retained as rollback).
- **CONTEXT records used (`CTX:`):**
  - `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_DOCS_RETURN.md:12-17`:
    the A2 register revision scope.
  - `…/APP_EXECUTION_RETURN.md:113-115`: a corpus re-hash by another session was observed.
- **NONE_FOUND searches:**
  - CLM-038.4 (VER-001) and CLM-050 (addendum schema). I searched
    `execution/_Coordination/_DECISIONS/_REGISTER.md` for `DEL-01-02`, `reliance` and `Reliance`. Hits
    were D-APP-38, 55, 56, 74, 75, 77 and 127, and I read the rows for D-APP-38, 56, 73/74, 77, 89
    and 127.
  - I grepped the CONTEXT sources (`plans/steers`, the v3 release plan, `AgentRuns/APP_V3_*`,
    `APPDEV_V3_NODE_*`, `CHIRALITY_V3_APP_ADOPTION_20260909`) for `DEL-01-02` and
    `reliance_boundary_register`. Only the A2 tranche returns and the 2026-09-06 integration
    decision-source copies were hit, and neither explains the VER-001 checks or the reduced addendum
    schema.
- **Authority routes on governance-invariant rows:**
  - CLM-040 and CLM-044 took AUTHORITY_CONFLICT (a ruling undercuts an unamended GOVERNING clause
    without naming it).
    - CLM-040: App DIRECTIVE §2.8 (unamended; the Claude Agent SDK is the key-aware default) against the
      Codex sole-engine rule that D-GOV-43 preserved. That rule is transcribed in amended CONTRACT
      K-ENGINE-3 and the PRD preamble. D-GOV-43 and D-APP-127 name neither App DIRECTIVE §2.8 nor
      DEL-01-02, and IMPACT.md:56 lists only Root DIRECTIVE §5/§7. The DIRECTIVE §0 order alone would
      favour the SoW text. I did not apply it, because doing so would set aside a ruled rule without a
      ruling.
    - CLM-044: D-GOV-43 item 4 (user-chosen approval and sandbox; `permissionMode` grants nothing)
      against unamended K-PERM-1 (hard-deny override) and K-PERM-6 (bypass never shipped). The live
      mapping `bypass → never/danger-full-access` is at `contracts/src/delegated.ts:326`. I cited the
      matching named question, R4-Q1.
  - The "no authority question" route applies to CLM-036, 042, 043, 045, 046 and 052: the invariants
    they restate are unamended and consistent with the live path.
  - I did not use the DIRECTIVE §0 route to resolve any row.
- **R4-Q1 (subject test):**
  - Cited by evidence on CLM-038.2, 038.3, 040, 043, 044, 051, 059.2 and 060.
  - Product-behaviour rows met only by legacy code carry `ALSO_MODULE:` (CLM-043, 044, 060).
  - Reachability caveat: REACHABILITY.csv reaches `core/src/{session-store,runtime-service,delegated-runtime}.ts`
    through `electron/main.ts>attachment-picker.ts>core/index.ts`, which is a re-export chain. I confirmed
    the symbols relied on are live through the packaged runtime-service entry:
    `daemon/src/standalone-bin.ts>standalone.ts>app-owned-composition.ts:161-171`, which constructs
    SessionStore, CodexSupervisor and DelegatedRuntime.
  - I tagged the FE `harness-contract` shim `TEST_ONLY`: only a test and a packaged-proof script import
    it, and the pack has no REACH row for it.

## 5. Method friction

- **Procedure steps as CONTEXT_CLAIM.** Imperative method steps fall under "method notes", but some of
  them carry embedded state (for example "future IDs" in CLM-032). The literal rule sends them to
  NOT_AUDITABLE unless a now-false fact can be isolated.
  - Proposal: say explicitly whether SoW Procedure sections are CONTEXT_CLAIM or LOCAL_DESIGN
    REQUIREMENT. Otherwise split workers may diverge on a large block of rows.
- **Blocker and TBD tables outside `## Remaining`.** The tie-break confines REMAINING_STATE_MISMATCH to
  `## Remaining` items or REMAINING_WORK rows. SoW "Remaining Blockers" tables therefore fall to
  STALE_SPECIFICATION, while TBD rows use rule 2(b) as "TBD placeholders".
  - Proposal: name SoW blocker tables explicitly in rule 2.
- **Validator REACH tag parsing.** The validator rejects `REACH=LIVE.` followed by a period; tags must be
  followed by whitespace, `;`, `,` or `)`. This is worth one line in CONVENTIONS §2.3.
- **Scripts and manifests.** `frontend/scripts/*.mjs|json` match the validator's code-path pattern but
  have no REACH row. I tagged them `TEST_ONLY`, meaning validation tooling with no product entry.
  CONVENTIONS could name a tag for tooling.

## 6. Effort

- About 30 files or excerpts read:
  - the SoW (lines 1–20 and 330–775), `_STATUS.md`, `_REFERENCES.md`, `_CONTEXT.md` (grep) and the
    INSP-03 assessment;
  - the register (193 lines);
  - evidence-pack filters, App DIRECTIVE §0/§2.8–2.10 and CONTRACT rows;
  - the D-GOV-43 packet (README, proposed.md excerpts, IMPACT.md excerpts) and D-APP-127 (grep);
  - the decision register (grep), and about 12 code files by line range;
  - both gate transcripts;
  - read-only blame for 5 ranges.
- Context budget was adequate, not tight.

## Coverage gaps

- **Live Codex-path boundaries have no SoW scope and no register row.** User-chosen approval and
  sandbox policy (`contracts/src/delegated.ts:322-331`, `codex-supervisor.ts:219`), Codex approval
  request answering (`codex-supervisor.ts:40,:477`), dynamic application tools
  (`daemon/src/application-tools.ts`) and the Codex effective home have no row. The SoW Procedure's
  inventory (CLM-030) and owner classes (CLM-031) are SDK-era. The owning scope looks like DEL-01-02
  itself, but no indexed unit asks for these rows, so they are recorded here rather than as a forward
  row.
- **The SoW "Output and Evaluation Matrix" (`ScopeOfWork.md:770-774`, OUT-001) is not an indexed
  unit.** It maps OUT-001 to CLM-014, AC-001 and VER-001. I left it to the manager to decide whether
  S1 or neither half owns it; its VER-001 content is dispositioned on CLM-038.4.
