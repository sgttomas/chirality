# DEL-04-02 R2 concordance notes — RUN_D55_CONCORDANCE_2026-07-11_1904Z

Wave: W2 (PKG-04). Source state: frontend/ at `fac46e33f` (byte-identical through
HEAD `1625b396a`, orchestrator-verified; HEAD re-confirmed this run). docs/kit
inspected at `1625b396a`. Claim set re-derived from `Specification.md`: 14
requirement rows (DEL-04-02-REQ-001..014), matching the R1 REQUIREMENT_INDEX
14-ID checklist exactly. No parser gap for this deliverable — the R1 index
carried both the full `DEL-04-02-REQ-nnn` IDs and 14 duplicate bare `REQ-nnn`
forms; both resolve to the same 14 spec requirements.

Package-local dedup (per dispatch): sibling DEL-04-01's W2 D-APP-18 key-aware
default-provider cutover (its UNMAPPED-1, ACCEPTED_DIVERGENCE) is NOT restated
here; runtime.ts provider selection is a DEL-04-05/PKG-03 surface, out of this
builder's rows.

## Census

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 14 |
| EXCLUSION | 5 |
| ACCEPTANCE | 2 |
| REMAINING_WORK | 1 |
| REGISTER_DEFECT | 1 |
| **Total** | **23** |

| Disposition | Rows |
|---|---:|
| ALIGNED | 16 |
| PARTIALLY_IMPLEMENTED | 4 |
| STALE_SPECIFICATION | 2 |
| REMAINING_STATE_MISMATCH | 1 |

Fan-in correction accepted (former UNMAPPED-1, REFUTED at verification): the
executable subagent bridge + delegated Agent exposure I initially raised as
IMPLEMENTED_UNDOCUMENTED is mapped corpus-wide — decomposition v3.2 line 353
assigns DEL-08-04 "Type 2 Subagent Governance Bridge" (SOW-063) with
anticipated artifacts "`evaluateSubagentGovernance` bridge; SDK agent
definitions; `Agent` hook tests" (re-verified directly this run). The row was
dropped and its evidence folded into REQ-013 (the builder's lines 93-109
attachment is the required adjacent-contract consumption) and EXC-004 (bridge
ownership sits in PKG-08, so the exclusion boundary is respected; confidence
raised to HIGH). The NEW-PACKET flag was removed. Cross-package handle for R3:
DEL-08-04's PKG-08 wave (W3) claims the bridge side (subagent-bridge.ts, the
Agent hook tests). Dependencies.csv carries no explicit DEL-04-02→DEL-08-04
row (subagent posture rides the package-level DEP-04-02-009 PKG-06 row) — a
register-granularity observation for R3, not scored as a defect.

MR-4 note: Datasheet Attribute/Condition restatements (Fallback chains,
Settings posture, Tool mapping posture, Permission boundary posture, Max-turn
guard, Visible metadata) are folded into REQ-001/003+004/005/007/008/010. The
two ACCEPTANCE rows are kit-distinct conditions: the PRD source-state warning
cluster (ACC-001) and the setup-era TBD wording cluster covering dependency
extraction / module path / test command (ACC-002).

MR-8 tie-break applied on both STALE_SPECIFICATION rows: the kit text flatly
asserts a now-false state (PRD HASH_MISMATCH; "no dependency edges extracted";
"module path TBD"), so STALE_SPECIFICATION (repair-shaped), not
ACCEPTED_DIVERGENCE — no ruling acknowledges these as a bounded difference.

Domain MCP tool attachment (D-APP-50 tranche-1 read tools; D-APP-52 pec
proposal tools) flows through the same builder tool-mapping mechanism the
Specification requires (REQ-005/006) and is exercised by
sdk-options-builder.test.ts lines 216-307. The domain tool ROSTER is owned by
DEL-06-02 / PKG-10 descriptor deliverables and rulings D-APP-50/52, so it is
cited as `(context)` on REQ-005/006 rather than raised as a separate
IMPLEMENTED_UNMAPPED row (the builder's map-registered-names behavior is
required, not unmapped). The dev/test-only `spawnClaudeCodeProcess` scripted
proof (builder lines 105, 155-157; test lines 330-368) is DEL-04-01/ADQ-15
packaging-proof scope, gated to NODE_ENV test/development + env flag, and not
shipped behavior — folded into that sibling scope, not a row here.

## Least-confident rows (mandatory self-flagging)

1. **DEL-04-02-REQ-005 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative reading:
   ALIGNED. The requirement's two clauses (map only to registered names; unknown
   names MUST produce structured validation errors) are both satisfied at the
   runtime boundary — the builder maps deterministically via resolveHarnessToolPool
   and TurnEngine.assertKnownAgentSdkTools throws a structured
   `HarnessError('INVALID_REQUEST',400,{category:'UNKNOWN_TOOLS'})` before
   streaming. I kept PARTIALLY_IMPLEMENTED because the ERROR is not emitted by
   the builder itself (the builder silently drops unknown names from its allowed
   set), which is exactly the split-ownership INSP-03 flagged (Gap 1) and which
   persists at fac46e33f. If the fan-in reads "the builder MUST map … unknown
   names MUST produce errors" as satisfied by any point in the DEL-04-02 call
   path, the row flips to ALIGNED.
2. **DEL-04-02-REQ-010 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative reading:
   ALIGNED. REQ-010 is SHOULD-level with a "where available" qualifier; most
   listed fields (SDK version, permission mode, visible tool list, MCP names,
   session/resume) are present in renderToolSurface + the turn.accepted event,
   and transcript/store linkage is legitimately deferred to PKG-05. I kept
   PARTIALLY_IMPLEMENTED because (a) INSP-03 rated it PARTIAL and (b) the
   settings-source posture field named in Specification.md line 37 and Guidance
   Example Settings Posture is not actually surfaced in visible metadata. A
   reviewer treating SHOULD + "where available" as fully satisfied would flip it.
3. **DEL-04-02-REQ-012 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative readings:
   (a) STALE_SPECIFICATION — the code now imports concrete SDK Options/
   PermissionMode/SettingSource types that compile against the pinned SDK, so
   the Specification "exact SDK option property names … remain TBD" wording is
   arguably flatly stale; (b) ALIGNED — the property names are confirmed by the
   probe/typecheck. I kept PARTIALLY_IMPLEMENTED to match INSP-03 and because
   the formal version-pinned ADOPTION verdict is still open in sibling
   DEL-04-01 (DEL-04-01-REQ-013 PARTIALLY_IMPLEMENTED), so the epistemic TBD is
   not fully closed even though the code-level property names are concrete.
4. **DEL-04-02-REQ-014 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative reading:
   ALIGNED. The enumerated fail-closed cases (unknown tools, denied/parked tools,
   undelegated Agent, ungated bypass) all fail closed today. I kept
   PARTIALLY_IMPLEMENTED because the requirement's broader "when required
   governed policy inputs for settings, tools, permission, hooks, MCP, or
   subagents are absent or explicitly unresolved" clause has no explicit
   builder-level guard for absent settings/hook/MCP policy — the builder
   constructs from whatever ResolvedOpts/SessionRecord supply — and INSP-03
   scoped that closure to PKG-06/PKG-08.
5. *(Withdrawn.)* The former UNMAPPED-1 self-flag (executable subagent bridge)
   was refuted at fan-in exactly along the alternative reading anticipated
   here: decomposition v3.2 line 353 maps the surface to DEL-08-04, so it is
   the sibling deliverable's row, not an unmapped one. See the fan-in
   correction note under the census above.

The fan-in verifier should also recheck all non-ALIGNED rows per the brief. The
two STALE_SPECIFICATION rows (ACC-001, ACC-002) are HIGH-confidence: the PRD
hash was recomputed live this run (`shasum -a 256 docs/PRD.md` reproduces
`ac35fba4…c30bfd`, matching `_REFERENCES.md` REF-006 MATCH), and the
11-row register / landed builder module / landed test suite were re-read
directly.

## Register-defect summary

One defect (REGISTER-1): `_DEPENDENCIES.md` "Declared Upstream" (line 14) and
"Declared Downstream" (line 18) narrative sections still assert "TBD - no
accepted dependency edges have been extracted yet" while the same file records
the 11-row Extracted Dependency Register (lines 22-44) and the 2026-05-20
extraction run (Run History lines 63-65). Same defect class as sibling
DEL-04-01 REGISTER-1 (the D-APP-53/DRQ-04 sync corrected summary/metric tables
but left these narrative sections stale). `Dependencies.csv` itself is
internally consistent with `_DEPENDENCIES.md`'s tables (11 rows; ACTIVE=11;
SATISFIED=5 / TBD=6) — no defect there. No defect in `_REFERENCES.md`: all
seven rows MATCH, REF-006 re-verified by live hash recomputation.

## Remaining-item handling

One `## Remaining` item (concordance bootstrap, UNGATED, D-APP-55) → one
REMAINING_WORK row (REMAINING-1), SelectableUnderCurrentLoop YES; this run is
its in-progress execution. No gated residuals; no cross-project gate, so no
`UNKNOWN` gate value needed (MR-6). DEP-04-02-011 (DOWNSTREAM HANDOVER to the
UNKNOWN/TBD runtime/event max-turn consumer) remains ACTIVE/TBD but is a
legitimate open dependency edge, not a `## Remaining` item and not a register
defect — noted in REQ-008 RemainingWork.

## Method deviations

None. Test line anchors for suites I read directly this run
(sdk-options-builder.test.ts; harness-options.test.ts; options.ts;
sdk-options-builder.ts; tool-pool.ts; turn-engine.ts; persona-manager
renderToolSurface; claude-agent-sdk-manager metadata) are stated without
attribution. Anchors I did not open this run (persona-manager.test.ts;
turn-engine.test.ts; sdk-message-mapper.test.ts; claude-agent-sdk-manager.test.ts)
are attributed to INSP-03's citations with the referenced surfaces' presence
re-confirmed at fac46e33f. No tests executed; no dependencies installed; no
files outside the two wave artifacts written.
