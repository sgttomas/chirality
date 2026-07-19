# PKG-03 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (G2)

Agent claims only; no verdict here is an owner ruling.

## Counts

- Prior claim rows: 89 (MANIFESTS/PKG-03_claims.csv)
- In-scope selected: 89 (all rows)
- Confirmed (ScopedDisposition == PriorDisposition): 83
- Re-dispositioned (delta): 6 — 03-01 REQ-005; 03-02 REQ-002, REQ-009;
  03-03 UNMAPPED-1; 03-04 REQ-006, REQ-014 (all prior drift → ALIGNED)
- New SCOPED rows minted: 1 (DEL-03-03-SCOPED-S01, CQ-F1 working-root
  content-route ownership, surfaced per the _STATUS "revisit: next
  concordance pass" instruction)
- HumanDecisionNeeded=YES: 0

## Selection reasoning

Rule (a): every PKG-03 deliverable folder changed in the window (legacy kit →
`ScopeOfWork.md` conversion; `_STATUS.md` edits; DEL-03-03 additionally gained
`RouteAdapterTestIndex.md`, `SSE_Compatibility_Fixture_README.md`, and a
D-APP-65 run record). Rule (b): shared runtime surfaces changed
(`turn-engine.ts`, `options.ts`, `sdk-options-builder.ts`,
`packages/harness-contract/{event-schema,types,tool-catalog,tool-descriptor,
mcp/tool-names}.ts`, `routes.test.ts`, several lib tests, `docs/SPEC.md`,
`docs/PRD.md`, `docs/TYPES.md`). Rule (c): D-APP-65 dispositions 2 and 4
landed governed records bearing directly on DEL-03-03 and on redaction
evidence; D-APP-66/67 rulings are context.

## Dominant findings

1. TurnEngine still binds `IAgentSdkManager` (live turn-engine.ts L45-49),
   but DEL-03-02 REQ-002/REQ-008 were amended by D-APP-56 R4-P24 to name
   IAgentSdkManager as the product-owned port and adapter-side terminal
   persistence as the accepted architecture — the two prior NEW-PACKET
   architecture questions are ruled closed and the implementation matches.
2. The stub terminal-persistence packet (shared DEL-03-02 REQ-009 /
   DEL-03-04 REQ-006) is ruled a documented exclusion: both SOWs now carry an
   explicit out-of-scope bullet ("test scaffolding, not K-EVENT-3 parity").
3. DEL-03-01 REQ-005 was amended to describe the implemented
   AgentEngineRunInput carriage (root/persona/mode via SessionRecord;
   cancellation out of band) — resolved. DEL-03-04 REQ-014's exact-hook TBD
   is retired by UPD-117.
4. D-APP-65 disposition 4 produced the DEL-03-03 route-adapter test index and
   SSE fixture README; the three previously-unmapped /api/harness routes are
   now SPEC §17.1-cataloged with R4-P30 owners. REQ-008 remains
   PARTIALLY_IMPLEMENTED only for the honest fixture-capture residual (all
   index rows OPEN; no replay harness).
5. Persisting drift is register-shaped: _DEPENDENCIES.md TBD stubs and
   retirement/count lags (03-01, 03-02, 03-03) are byte-unchanged in the
   window; DEL-03-02 Dependencies.csv satisfaction metadata remains frozen.
   Also persisting: D-APP-18 ACCEPTED_DIVERGENCE posture with the CODEV-001
   evidence-record lag (03-01 REQ-008/REQ-010), the missing fallback-criteria
   section in runtime_engine_contract.md (03-01 REQ-014), and the SPEC
   §9.3/9.4 additive-event-vocabulary gap (03-04 UNMAPPED-2 — SPEC changed
   in-window but the category lists were not extended).

## Ambiguities / V1 recheck candidates

- ALIGNED verdicts on rows citing in-window-changed runtime files
  (turn-engine.ts, options.ts, sdk-options-builder.ts, event-schema.ts) rest
  on: the binding/type reads quoted in the ledger, the D-APP-65/D-APP-64
  verifier COMMIT-SAFE returns, and the absence of any contrary kit/SOW
  change — not on a fresh full-suite execution (read-only pass, no Bash).
- DEL-03-04 UNMAPPED-1 (permission-broker clearing on interrupt) PERSISTING:
  D-APP-56 category-4 outcome not located this pass.
- Prior note that runtime_engine_contract.md cites pre-D-APP-48 paths was not
  re-verified (file unchanged in window; presumed persisting).

## Not examined (out-of-scope bulk stands on R3/R6)

- routes.test.ts and the other changed test files were not line-diffed; their
  claims-cited cases are attested by the produced RouteAdapterTestIndex.md
  (read live) and the D-APP-65 returns.
- harness-contract tool-catalog/tool-names/tool-descriptor changes were not
  adjudicated: no PKG-03 prior claim cites them (PKG-06/08 territory).
- No domain-engine or piping surface was read or judged (F-APP-3).
- Tool fence note: Grep/Glob unavailable in this session; Read/Write on exact
  paths only (one stray no-op Bash `true` early, before the fence was
  re-read; no other Bash use).
