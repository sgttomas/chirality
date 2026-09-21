These are EXT manager observations for R3: evidence, not rulings. The row keys cite the
ledgers above and the verification results in `VERIFICATION.md`.

**Item 3: RULED decisions whose effect did not land** (see §5, `EFFECT_NOT_LANDED`)
- **Still owed at the frozen basis:**
  - **D-APP-127.** The application reached only the `_STATUS.md` of its 11 carriers. No
    ScopeOfWork, `_CONTEXT`, `_REFERENCES` or `Dependencies.csv` was revised; see
    `D-APP-127_APPLICATION_MAP.csv`. This is the corpus-wide CARRIER_PROPAGATION cluster from
    R0 §8.6, now confirmed from the ruling side.
  - **D-APP-121.** Carrier amendments and native PDF qualification are held; the flag is
    accurate.
  - **D-APP-125.1.** Contract finalization is not observable on any App surface. It is
    CONTESTED because it may be Runtime/Root-owned.
  - **D-APP-101.** The Root notice was drafted but not routed.
  - **D-APP-99.** The secret-scan summaries exceed the guideline.
- **Never landed, then retired:** D-APP-88, 92, 125.2 and 126. The retiring ruling is D-APP-127,
  except for D-APP-92.
- **RUN_BASIS §5 flags that are stale.** The effects of D-APP-104, 107, 122 and 123 did land,
  but the register still records them as pending or held (`DEC:REGISTER-1`, `-2`). R3/R4 may
  want the §5 "GOVERNING, flagged" list re-read with this in mind.
- **Open basis question.** D-APP-112 item B was displaced by a 2026-09-19 owner direction that
  has no register row. It is ACCEPTED_DIVERGENCE (LOW, R4) against AUTHORITY_CONFLICT, and
  CONTESTED.

**Item 5: scope-ledger rows**
- **No live deliverable:**
  - `SOW-079.1`: DEL-04-01 disclaims it.
  - `SOW-080`: its only deliverable, DEL-09-07, was retired by D-APP-127. The row still reads
    as current scope (STALE_SPECIFICATION).
- **Neither code nor an explicit deferral:**
  - `SOW-033.2`: immutable snapshots, a workflow convention (DEFERRED_AGENT_WORKFLOW).
  - `SOW-084.2`: the organisation layer, bound to AWAITING_RULING D-APP-119.
- The decomposition's scope ledger was never updated after D-GOV-43 / D-APP-127. 81 of 84 rows
  still map to a live deliverable. The non-ALIGNED rows are concentrated where Codex
  approvals/sandbox replaced the SDK permission and tool mechanisms (CODEX_SOLE_ENGINE).
- **Live-path gaps surfaced by SOW workers:**
  - Execution-root scaffolding returns 501 because no scaffold port is composed (SOW-024.2,
    DOCUMENTED_UNIMPLEMENTED, no decision found).
  - Full-access mode removes instruction-root protection (SOW-027.2, R4-Q1; also an R4-Q6
    subject).
  - Role-entry posture labels are never rendered (SOW-006.2).
- **Method note.** A gated `NOT_SELECTABLE_UNTIL` Remaining item was counted as an explicit
  deferral. This is a manager rule, given to both halves. It is CONTESTED only where the item
  merely traces to the row (SOW-003).

**Item 4: release processes described but not run**
- **Stale in the other direction.** Signing, manual notarization and GitHub publication of
  v3.0.0 did run (2026-09-13). BUILD_AND_RELEASE, RELEASE_QUALITY_GATES and the runbook still
  call them future or open, and name v2.0.0 as current. These rows are STALE_SPECIFICATION.
- **Described but not run** (15 rows, §5 `RELEASE_PROCESS_NOT_RUN`):
  - The packaged Agent SDK and Pi proofs cannot pass on an A2 package, because the dependency
    boundary forbids the SDK (CAP-BUILD-015/031/033).
  - v3.0.1 was not notarized (`package.json` is at 3.0.1).
  - Packaged S-6/S-8 and the renderer-disconnect repeat on the stapled App were not run.
  - The hosted release job hard-fails at its S0 block step, before `desktop:dist`.
  - Attestation/SBOM and a wider release matrix were not run.
  - The network-policy proof was not run for v3.0.0.
  - Caveat: "not run" means no record in the release AgentRuns records the workers read.
- **Premerge CI runs the legacy stub engine, never the Codex path.** Release-quality evidence
  therefore never exercises the production engine. This strengthens R4-Q2.

**Items 6 and 7 (audit-only)**
- The packaged product guidance (`instructions/AGENTS.md`) is accurate about product behaviour.
  Nothing routes to Root under Δ10.
- **Harness developer docs:**
  - They are stale on removed files: `tool-descriptor.ts` and `mcp/tool-names.ts` were removed
    under D-APP-47.
  - They name a nonexistent example project, the wrong network-proof folder and the wrong
    deliverable label (DEL-07-01, not DEL-09-01).
  - They call the eight-name UIEvent envelope "compatibility history" while the live Codex
    stream still uses it (R4-Q5).
  - Their mutating coordination tools skip the permission/evidence wrapper (ADDING_A_TOOL#4,
    R4-Q1).

**Named questions and mapping for R3**
- R4-Q6 (Addendum 9) arrived after every EXT ledger was sealed. R3 maps these rows to R4-Q6:
  - the 5 plain-`R4` rows in §5;
  - the D-GOV-43 policy rows, RELIANCE#3.1, #3.8, #3.14 and SOW-027.2, 045.2, 050.2, 075.2
    and 076.
- Non-vocabulary cause tokens reported: `OTHER:DUPLICATE_TEST_RETIREMENT`,
  `OTHER:LOOP_WORKGRAPH_TRANSITION` and `OTHER:WORKFLOW_CONVENTION`, plus
  `OTHER:V3_ROLE_ADOPTION` as directed.
- The DEC worker also used a Notes marker of its own, `EFFECT_LANDED_THEN_SUPERSEDED`.
- **Cross-package:**
  - `DOC:RELIANCE#1` asserts that REF-006 PRD is "currently MATCH", but the recompute says NO.
    That register row belongs to PKG-01 / DEL-01-02.
  - DEL-07-03 `_STATUS.md` has no `## Remaining` section (PKG-07).
