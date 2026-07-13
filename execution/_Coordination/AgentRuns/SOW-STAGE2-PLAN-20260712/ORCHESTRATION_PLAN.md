# D-GOV-16 Stage-2 Governed Orchestration Plan

Status: `PROPOSED EXECUTION PLAN — NO_STAGE2_DISPATCH`
Plan basis: synchronized `main@c9af689118e4e87f329e1ab4c6e71fea331b2674`
Authority: D-GOV-16 items 1–10, ruled exactly as proposed at
`7584718aa32b112e415331736d1a8e68c12ac176`
Parent at execution: `HELP_HUMAN` (Agent 0)

## 1. Outcome and execution gate

This plan converts the ruled architecture into a dependency-valid Stage-2
execution graph. It does not activate canon, dispatch a child, change a
deliverable, apply a patch, or perform Git integration.

The next lawful act is a human acceptance of this plan from synchronized
`main`. After acceptance, HELP_HUMAN creates a fresh Stage-2 execution run and
reconfirms that local `main`, local `origin/main`, and remote `main` are the
same commit. A mismatch, dirty in-scope basis, or changed census/caller state
halts before dispatch.

The plan uses a mixed graph:

- sequential phase boundaries where authority or accepted format changes;
- terminal fan-out/fan-in for disjoint package preparation and verification;
- supervised many-to-many coordination only for live drift, conflicts, shared
  consumer findings, or brief amendments; and
- one serialized CHANGE integration owner for every accepted-main mutation.

This is migration sequencing, not an engineering schedule or work-priority
assignment. No dependency claim is inferred from package numbering.

## 2. Frozen inputs

The execution run must bind these inputs before any write:

| Input | Bound identity |
|---|---|
| synchronized planning basis | `c9af689118e4e87f329e1ab4c6e71fea331b2674` |
| D-GOV-16 proposal snapshot | `31e5efd985db4cc7b25543e11a65933979e07e4f` |
| D-GOV-16 ruling publication | `7584718aa32b112e415331736d1a8e68c12ac176` |
| ruled successor standard | SHA-256 `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| ruled TYPES patch | SHA-256 `9614166c7db8340532d838768be2de52567862757fe0d5add3d3a90edea9d4b4` |
| ruled SPEC patch | SHA-256 `543200af8a617e2f5673db110eef2b0a5cf742c54e70ccda8bce0cad870d4b2e` |
| Stage-2 evidence index | SHA-256 `8a6e48ac8247fe5147afb4208d3e7c0b4f48cb1071b1e086b4f24a2ceeded806` |
| tracked population | 154 directories; sorted-path SHA-256 `b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31` |
| App pilot evidence | `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26` |
| Piping pilot evidence | `31c35ea9798c29cd0af16b7089186f3942dcfcb1` |

Stage-1 run records, pilot branches, claim maps, parity reports, checklist
outputs, and candidates are derivative evidence. They never replace current
decomposition or deliverable truth.

## 3. Universal execution contracts

### 3.1 Format and lifecycle

At every accepted commit, each affected deliverable resolves to exactly one
production format:

- `LEGACY_FOUR_DOC` before replacement; or
- `SOW_V1` after replacement.

`MIGRATION_DUAL` may exist only inside an exact, isolated conversion workspace
named in a sealed brief. It may never be integrated. Partial legacy, invalid
SOW, missing production content, or unauthorized dual format fails closed.

Migration must leave `_STATUS.md` byte-identical to its per-wave source basis.
It must not change lifecycle, acceptance, issuance, authentication, or
professional-reliance status. A content delta is `CONFLICT`, not a conversion
repair.

### 3.2 Deterministic-first conversion and review boundary

The registered converter, validator, map, parity, checklist, and renderer are
the authoritative mechanical path. Agentic work does not independently
re-extract acceptance criteria or rewrite mechanically preserved content.
TASK instances supervise bounded tool execution, classify failures, and return
evidence. REVIEW consumes deterministic checklist output and adds judgment
only at an actual human-gated review or conflict disposition.

### 3.3 Child and write scopes

Every child brief must declare parent, basis commit, read scope, exact write
targets, accepted inputs and hashes, tools, expected return, checks, and
dependants. Agent 2 does not delegate.

Package-parallel children may use registered deterministic tools and bounded
file operations only. If a child requires arbitrary Bash over a project root,
that child becomes the serialized integration owner for that stage and its
siblings do not write concurrently. Inability to provide bounded tools is
recorded as `SUBSTRATE_FALLBACK`; execution may serialize, but substrate status
does not imply schema/content PASS.

### 3.4 Snapshot and handoff rule

Each phase boundary writes a commit-bound immutable snapshot under the fresh
execution run, containing basis, manifest, outputs, checks, returns, conflicts,
failures, and rerun rules. Pointer updates occur only where the owning workflow
permits them. Every stopped package or phase writes a handoff naming accepted
upstream snapshots, derivative status, closure verdict, blockers, and required
reruns.

## 4. Phase graph

### Phase 0 — Execution bootstrap and manifest preflight

Owner: ORCHESTRATOR under HELP_HUMAN.

1. Start from synchronized `main` containing this presented plan and the
   D-GOV-16 ruling.
2. Reproduce `CENSUS_REFRESH.md` and `CALLER_REFRESH.md` read-only.
3. Freeze `CENSUS_MANIFEST.tsv` with one row per member: project, package,
   deliverable ID, path, four source hashes, `_STATUS.md` hash, lifecycle,
   pilot flag, and ISSUED flag.
4. Freeze `CALLER_MANIFEST.tsv` with every active caller classified
   `ACTIVATE`, `RETAIN_LEGACY`, `HISTORICAL`, `INDEPENDENT_SCHEMA`, or
   `DERIVATIVE_REGENERATE`.
5. Record the basis and manifests in snapshot `P0_BASIS`.

Gate G0 passes only at 154/10/144, 153 `IN_PROGRESS`, one named `ISSUED`, all
four companions complete, no SOW on accepted main, unchanged path digest, and
zero unclassified active callers. Any delta returns to the human; no child is
dispatched.

### Phase 1 — Exact canon activation

Owner: HELPS_HUMANS. Integration owner: CHANGE.

HELPS_HUMANS prepares one root-only tranche that:

1. replaces `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` byte-for-byte with
   the ruled proposed standard;
2. applies the ruled TYPES and SPEC patches with `--unidiff-zero` only after
   preflight checks pass;
3. leaves the proposal package and D-GOV records unchanged; and
4. emits before/after hashes and a patch-application receipt.

No consumer edit or project edit shares this tranche. EVALUATION validates
exact bytes, internal normative consistency, and scope. CHANGE integrates the
accepted result as a dedicated canon commit and records snapshot `P1_CANON`.

Gate G1 requires the exact standard hash, exact patch identities, expected
post-patch content, no unrelated path, and all applicable root governance and
path checks. A context mismatch or any proposed-byte change blocks Phase 2.

### Phase 2 — Consumer, tool, and runtime activation

Owners: HELPS_HUMANS for root instructions/skills/tools; one App Dev
WORKING_ITEMS manager for the frontend runtime. Integration owner: CHANGE.

After G1, two disjoint preparation lanes may run concurrently:

- **P2-R root lane:** update active agents, `scope-of-work` INIT/CONVERT/VERIFY
  contracts, deterministic format resolution, validators, semantic and
  consistency consumers, registries, new-initialization routing, legacy
  compatibility, and current explanatory canon. Regenerate governed exports.
- **P2-A App lane:** make the workspace scanner and document UI select
  `SOW_V1` or transitional `LEGACY_FOUR_DOC`, reject partial/ambiguous states,
  remove Stage-1-only feature/variance semantics, and preserve DOMAIN/control
  boundaries.

The lanes have disjoint writes. They do not edit project deliverable folders.
EVALUATION independently checks caller coverage and behavior; RECONCILIATION
fans in root and App results against the frozen caller manifest. One REVIEW
compatibility calibration confirms exact deterministic-checklist consumption;
it does not rederive criteria or repeat per-deliverable extraction.

CHANGE integrates root and App commits serially. Snapshot `P2_CONSUMERS`
contains final caller hashes, registered checks, export provenance, and the
refreshed classification.

Gate G2 requires:

- all active callers migrated or expressly retained;
- new PROJECT/SOFTWARE initialization routes to `SOW_V1`;
- legacy-only and SOW-only consumers green;
- missing, partial, ambiguous, and unauthorized dual states fail closed;
- four-documents and legacy readers still available for transition;
- deterministic checklist output byte-stable and REVIEW-compatible;
- root, agent, skill, tool, export, practitioner, App typecheck/build/test,
  runtime, scanner, API/MCP, and document-view checks PASS; and
- no project deliverable or lifecycle path changed.

Any unclassified caller or compatibility regression blocks Phase 3.

### Phase 3 — Post-activation census and execution-manifest freeze

Owner: ORCHESTRATOR. Independent fan-in: RECONCILIATION.

Reproduce the census on synchronized post-G2 main. Confirm consumer activation
did not change membership, sources, status, or lifecycle. Freeze an updated
execution manifest and compare it row-for-row with `P0_BASIS`. Record
snapshot `P3_MANIFEST`.

Gate G3 is the release point for conversion. Any source/status drift requires
a scoped manifest amendment and affected evidence rerun; membership,
lifecycle-population, or caller-classification drift returns to the human.

### Phase 4 — Atomic integration of the ten verified pilots

Owners: one App PKG-07 and one Piping PKG-13 WORKING_ITEMS manager. Children:
bounded TASK verify-only instances. Fan-in: RECONCILIATION. Integration owner:
CHANGE.

The two package lanes may prepare concurrently because their writes are
disjoint. They must not merge the pilot branches. For each of the ten members:

1. bind the current target's four source hashes and `_STATUS.md` hash;
2. compare them with the Stage-1 inventory;
3. extract only the hash-bound `ScopeOfWork.md` blob from the named evidence
   commit into an isolated replacement workspace;
4. independently reproduce validation, map, parity, checklist, and applicable
   deterministic HTML evidence on the current activation basis;
5. run project and consumer checks; and
6. prepare an atomic manifest entry that adds the exact SOW blob and removes
   all four legacy files without touching controls.

A changed source or candidate does not silently reuse Stage-1 evidence. It
blocks that pilot and triggers the D-GOV-16 material-change rerun rule.

RECONCILIATION validates all ten returns. CHANGE then integrates ten serial
replacement commits, one per deliverable, each leaving an accepted
single-format tree. Snapshot `P4_PILOTS` binds commit, preimage, postimage,
candidate hash, receipt, and rollback instruction for every pilot.

Gate G4 requires 10/10 `SOW_V1`, zero dual/partial states, 325/325 mapping rows,
3,466/3,466 source lines, unchanged controls/statuses, green callers/projects,
and an explicit single-format integration manifest. A failed pilot blocks its
dependants but not preparation of unrelated evidence; no failed pilot commit
integrates.

### Phase 5 — Remaining ordinary population in bounded package waves

Owners: one WORKING_ITEMS instance per package in the active wave. Children:
one author TASK and a separate verifier TASK per deliverable. Fan-in:
RECONCILIATION after every wave. Integration owner: CHANGE.

The ruled 143 ordinary remaining members execute in these bounded release
waves:

| Wave | Packages | Members |
|---|---|---:|
| A1 | App PKG-00–03 | 15 |
| A2 | App PKG-04–06 | 16 |
| A3 | App PKG-08–10 | 16 |
| P1 | Piping PKG-00–04, excluding `DEL-01-01` | 30 |
| P2 | Piping PKG-05–09 | 29 |
| P3 | Piping PKG-10–12 | 15 |
| P4 | Piping PKG-14–17 | 22 |
| **Total** | 27 non-pilot package scopes | **143** |

Within one wave, package managers may fan out using package-disjoint
worktrees. Within a package, deliverable children have disjoint target
directories. The author runs the deterministic converter and produces the
candidate, map, parity, checklist, render evidence, and receipt. The verifier
does not trust the author's derived results: it reproduces them read-only from
the bound source and candidate. Agentic semantic rewriting is prohibited.

For each wave:

1. ORCHESTRATOR reconfirms synchronized target main and source/status hashes.
2. Package managers prepare isolated `MIGRATION_DUAL` candidates.
3. Independent verifiers return PASS/FAILED with exact evidence.
4. RECONCILIATION checks coverage, conflicts, caller/project results,
   containment, and a proposed single-format manifest.
5. CHANGE integrates only the accepted release set, serially, one atomic
   deliverable replacement commit at a time.
6. Post-integration verification confirms no accepted dual/partial state and
   records an immutable wave snapshot and handoff before the next wave.

A failed deliverable is removed from the release set and receives a FAILED
handoff. Its declared dependants remain blocked; unrelated PASS deliverables
may form a formally closed release subset after RECONCILIATION confirms that
all applicable gates for that subset pass. Stage-2 corpus closure remains
blocked until every authorized ordinary member resolves.

No later wave begins integration until the prior wave snapshot is accepted.
Candidate preparation for a later disjoint wave may proceed only if main drift
is supervised and every candidate is rebound before release; the default is
sequential release waves.

### Phase 6 — Isolated ISSUED representation replacement

Owner: Piping PKG-01 WORKING_ITEMS manager. Children: separate author and
verifier TASK instances. Fan-in: RECONCILIATION. Decision owner: human.
Integration owner after approval: CHANGE.

This phase is serialized after P1 because the ordinary P1 scope and the ISSUED
scope share Piping PKG-01. It may prepare, but not integrate, Piping
`DEL-01-01`.

The preparation snapshot must bind:

- synchronized source commit;
- four source blobs and SHA-256 values;
- accepted/decomposition basis;
- exact `_STATUS.md` bytes and `ISSUED` state;
- deterministic conversion, 100% map/parity, checklist, containment, caller,
  and project checks; and
- independent RECONCILIATION preservation verdict.

Gate H-ISSUED is an explicit human administrative
representation-replacement approval citing that snapshot. Silence or approval
of this plan is not H-ISSUED approval. If approved, CHANGE performs one atomic
replacement commit and verifies that lifecycle remains `ISSUED`. Any semantic
difference is `CONFLICT` and routes to SCOPE_CHANGE or a new human ruling.

Snapshot `P6_ISSUED` records either the integrated replacement or a durable
prepared/blocked handoff.

### Phase 7 — Cross-wave closure and rollback window

Owners: RECONCILIATION and EVALUATION. Git evidence: CHANGE.

After all 154 replacements are integrated, independently verify:

- 154 valid `SOW_V1`, zero `LEGACY_FOUR_DOC`, zero dual/partial/invalid;
- per-wave source/control/status preservation and complete receipts;
- every active caller migrated or expressly retained;
- ISSUED administrative approval and exact lifecycle preservation;
- full root, export, instruction, skill, tool, practitioner, App, Piping,
  runtime, and containment checks;
- immutable evidence and historical surfaces unchanged; and
- every replacement commit has a non-history-rewriting rollback instruction
  bound to its preimage and manifest.

The rollback window begins with the first pilot replacement and remains open
through owner acceptance of the Stage-2 conversion-closure evidence. Before
integration, rollback is deletion of the isolated candidate. After
integration, rollback requires a human-authorized revert or replacement act;
no agent rewrites history or deletes receipts.

RECONCILIATION emits snapshot `P7_CLOSURE` and a handoff with verdict,
blockers, rerun rules, and rollback obligations. Failed closure checks block
only their declared dependants and preserve earlier valid snapshots.

### Phase 8 — Separate legacy-retirement decision request

Owner: RECONCILIATION prepares evidence; HELPS_HUMANS frames any exact
retirement proposal; human owns the decision.

This plan does not delete or deprecate `four-documents`, legacy readers,
legacy validators, or aliases. After P7 passes and the rollback obligations
are satisfied, prepare a distinct decision request naming exact retirement
targets, caller evidence, compatibility consequence, recovery plan, and
proposed bytes. Retirement occurs only under a later explicit owner act.

The Stage-2 execution run stops at
`CONVERSION_CLOSED — LEGACY_RETIREMENT_RULING_REQUIRED`, or earlier with a
durable blocked handoff.

## 5. Acceptance gates applied to every replacement

Every pilot, ordinary, and ISSUED replacement must provide:

1. bound source commit, source hashes, status hash, lifecycle, and authority;
2. 100% source-range disposition with complete merge/split provenance;
3. objective/output/requirement/claim/AC/VER/matrix closure;
4. deterministic checklist output containing every AC exactly once;
5. byte-identical control and lifecycle inputs relative to the release basis;
6. independent verifier return and RECONCILIATION acceptance;
7. legacy-only/SOW-only consumer checks and fail-closed negative cases;
8. deterministic bound offline HTML when rendered;
9. out-of-scope, history, DOMAIN/KTY, archive, fixture, and template
   containment;
10. applicable root/project/runtime/export tests;
11. separate schema, content/authority, preservation/containment, and
    execution-substrate classifications; and
12. a single-format replacement manifest and rollback instruction.

No waiver is inferred. A waived gate requires an explicit human ruling that
identifies the exact risk and affected scope.

## 6. Supervised coordination and amendments

Children report to their manager; managers report coordination notices to
HELP_HUMAN. Siblings do not exchange hidden authority. Informational relays
carry only minimum evidence and preserve claim status.

A new caller, source drift, lifecycle change, scope expansion, shared-write
conflict, altered acceptance criterion, or changed consequential risk requires
a versioned brief/graph amendment. Scope expansion, authority change,
unresolved shared-write ownership, ISSUED semantic change, or changed
acceptance/lifecycle criteria returns to the human.

## 7. Presentation stop

The current planning run ends at:

```text
PLAN_PRESENTED — NO_STAGE2_DISPATCH
```

No execution node in this document has been released. The next owner is the
human, through HELP_HUMAN, to accept, amend, defer, or reject this execution
plan.
