# Chirality Program Architecture Tandem Review — Evaluation Report

## Basis

This report closes the review stage defined by the Tandem Review Charter; it does not accept or amend any product.

- Review freeze: `da31c19b5656dd74615e308c4215688971d33dc9`
- Product-basis commit: `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`
- Frozen basis: `FROZEN_BASIS_MANIFEST.json`, 776 Git blobs
- Frozen-basis SHA-256: `f569d994156f9585fd100286e43b325116ae473616b1d1bd4f169bd88d632386`
- Charter SHA-256: `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`
- Pass-1 freeze: `PASS1_FREEZE.json`

The manifest verifies that the charter is the only changed path between the product-basis commit and review freeze. Product evidence was read from Git objects at the freeze. Live filesystem bytes, mutable pointers, candidate documents, proposals, plans, and historical run material were not substituted for accepted authority.

The charter was used as procedure and challenge material only. Its candidate propositions—universal application profiles, App semantic parity, and optional resource governance—were not treated as accepted scope.

## Method

The manager applied the repository `evaluation-protocol` under the read-only `EVALUATION` contract:

1. frame and freeze the exact basis;
2. seal and concurrently dispatch Reviewer A and Reviewer B with no inherited conversation history and disjoint write targets;
3. preserve reviewer independence until both pass-1 packages were terminal;
4. deterministically validate both pass-1 returns;
5. hash-freeze both packages;
6. run reciprocal challenge against every sibling finding, exceeding the charter’s mandatory high-severity-plus-sample minimum;
7. validate both challenge returns;
8. fan in by evidence state, without averaging severity or forcing consensus;
9. stop at the human decision gate.

No scoring rubric was authorized, so no score was produced. No reviewed product, PRD, decomposition, ScopeOfWork, decision, status, pointer, or primary-checkout file was modified.

## Coverage

Both independent reviewers assessed Root, App, and PEC for depth and breadth.

| Return | Findings | Trace rows | Boundary rows | Manager validation |
| --- | ---: | ---: | ---: | --- |
| Reviewer A pass 1 | 18 | 208 | 19 | PASS, 0 failures |
| Reviewer B pass 1 | 15 | 88 | 22 | PASS, 0 failures |
| Reviewer A on B challenge | 15 targets (all B findings) | — | — | PASS, 0 failures |
| Reviewer B on A challenge | 18 targets (all A findings) | — | — | PASS, 0 failures |

The trace work covers all seven Root objectives and all 45 live Root SOWs; all ten App objectives and all 53 App SOWs, explicitly partitioned as 51 decomposition deliverables plus two PKG-00 controls; all eleven PEC invariants, all six PEC objectives, and all 64 deliverables, explicitly partitioned as 32 initialized SOWs plus 32 deliberate P2–P4 deferrals.

The boundary work covers Root authority and shared runtime; App client/work-surface semantics; PEC projection/presence and graceful absence; human judgment; domain truth; file/Git truth; delegation; permissions/tools; credentials/session state; notices/drift; application integration; migration/rollback; release/conformance; and candidate optional services.

### Disclosed conditions not elevated into defects

- Root post-candidate amendments are accepted through governing decisions; absence of a supplied convenience diff does not void them because exact Git comparison is reconstructible.
- Root `AGENTS.md` need not enumerate six packages or 45 deliverables; it is the runtime/agent index, not the decomposition register.
- Root PRD O-1’s stale six-member wording is lawfully superseded by the pointer and D-GOV-26/D-GOV-27 chain.
- Root’s unresolved initialization-tool conflicts remain routed work and limit claims of fully executable initialization, but do not erase the accepted decomposition or 45 initialized contracts.
- App’s missing semantic-parity instrument is candidate future work, not a current scope gap.
- The App orphan PKG-03 evidence tree remains excluded and does not create a 54th SOW.
- PEC’s 32 absent later-wave SOWs are deliberate sequencing, not omissions.
- Root and PEC validator-era results remain distinct; no current-tool rerun was used to invalidate historical acceptance.
- Resource governance remains optional candidate architecture, not accepted Root/App/PEC scope.

## Validated-return inventory

### Independent pass 1

- Reviewer A report: `returns/A_PASS1/REPORT.md`; SHA-256 `1a1c857fd8241c892f7a7009bc44da7313fb00d1f0fee049f73d96da4aa4aa82`
- Reviewer B report: `returns/B_PASS1/REPORT.md`; SHA-256 `4692e8bc2c05e0d0bf73e1a8dd9440f80166f77407aa36f5df98bcb4bdcc00f3`
- Both returns passed schema, evidence-anchor, product coverage, boundary coverage, population, high-severity completeness, return-hash, and independence checks.

### Reciprocal challenge

- Reviewer A challenge report: `challenges/A_ON_B/REPORT.md`; SHA-256 `a038c67e326021e143f88b3cdaeea7b467be5dcafde1c785d030a973fef9d132`
- Reviewer B challenge report: `challenges/B_ON_A/REPORT.md`; SHA-256 `6677c39d43813bbc72955cbefdc79eb00a9f09be33eede6b8e1e331bc4448f4b`
- Reviewer A challenged all 15 B findings: 10 CONFIRM, 3 NARROW, 1 REFUTE, 1 ADD-MISSING-EVIDENCE.
- Reviewer B challenged all 18 A findings: 13 CONFIRM, 5 NARROW.
- Both challenge packages passed schema, target, evidence, report-content, and output-hash checks.

## Findings

The authoritative fan-in register is `FINDINGS.csv`. It contains 19 issues classified under the charter’s non-averaging states:

- `AGREED`: 9
- `RESOLVED_BY_EVIDENCE`: 6
- `STANDING_DIVERGENCE`: 2
- `SHARED_BLIND_SPOT_RISK`: 1
- `STALE_INPUT`: 1

### Consequential architecture findings

1. `FAN-001` — Root shared-runtime ownership is under-decomposed. Both reviewers agree on the gap and Root SCOPE_CHANGE route. They do not agree on severity: A uses `BLOCK` only against a claim that decomposition ownership is complete; B uses `REVIEW` for remediation because the ruling and runtime remain valid.
2. `FAN-002` — App’s retained generic-runtime semantics conflict with the accepted Root-owner/App-client split. The correction must cover the App decomposition and affected runtime SOWs, not a SOW-only edit.
3. `FAN-003` — App’s self-required invariant-coverage register or explicit deferral is absent. This is a REVIEW prerequisite.
4. `FAN-004` — App’s exact current decomposition acceptance vehicle is not reconstructible from a ruling that binds current bytes and amendment lineage.
5. `FAN-006` and `FAN-007` — D-APP-48 is 12/12 stale and contains an additional ruling-versus-JSON source-commit conflict missed in both pass-1 reviews.
6. `FAN-008` — D-GOV-27’s applied-state SHA remains unbound.

### Record, trace, and coordination findings

- `FAN-005` narrows the stale App PRD reference to a WARN because frozen history resolves the delta to one KG-033 row.
- `FAN-009` retains the Root SHA-role conflict as WARN; D-GOV-25 and all 45 SOWs make the effective basis recoverable.
- `FAN-010` and `FAN-011` retain stale Root handoff/navigation and responsibility propagation as WARN without reopening accepted initialization or owner assignment.
- `FAN-012` narrows Root AC/VER machine opacity to an OBSERVATION/WARN because the current SOW standard does not require a dedicated field and no consumer failure was proved.
- `FAN-013` resolves App PR #333 as merged through reachable commit `612c35226b84c0d4fb042982065164c0d0e63419`; only stale coordination surfaces remain.
- `FAN-014` retains the three PEC residuals with terminal D-PEC-66 evidence.
- `FAN-015` narrows notice/drift concerns to stale derivative detection and specifically evidenced gaps; program-wide notice failure is not proved.
- `FAN-016` corrects the initiating manifest: only one of the six absent agent pins is active; five are retired.
- `FAN-017` and `FAN-018` retain App PRD citation ambiguity and the draft/operative overlay conflict.
- `FAN-019` preserves PEC profile status as INFO in the current v0.4-bound state and WARN before any profile-mediated v2 use.

## Conflicts and unknowns

### Standing divergences

- Runtime severity (`FAN-001`): `BLOCK` on claiming complete decomposition coverage versus `REVIEW` remediation priority. The core gap and route are not disputed.
- PEC profile severity (`FAN-019`): no current v2 defect is proved; the future-use gate is WARN while current state remains INFO/UNKNOWN.

### Resolved conflicts

- App daemon-service merge: Receipt 91 did not itself say “merged,” so Reviewer A correctly refuted B’s wording. Reviewer B then supplied stronger frozen evidence: merge commit `612c35226…` is reachable from the freeze. Fan-in therefore resolves the merge state and preserves only stale handoff/receipt representation.
- App PRD delta: the stale decomposition reference is real, but frozen history resolves its material delta to one KG-033 row rather than an unknown broad PRD change.
- PEC residual evidence: the earlier coverage package alone was insufficient for all three current residuals; the terminal D-PEC-66 closeout supplies the correct current anchor.

### Unknowns held visible

- Neither pass produced a function-by-function responsibility and release-gate matrix for every D-GOV-20 runtime function. This limits severity precision and is a rerun requirement after owner disposition; it does not create new scope.
- D-APP-48 hash drift proves stale byte identity, not symbol-level semantic incompatibility or actual current consumer failure. A consumer inventory and compatibility check remain missing evidence.
- Loop-by-loop consequences of notice gaps remain unknown without a per-change/per-receiver census.
- The exact future v2 PEC domain-engine profile remains intentionally undecided until the first profile-mediated v2 act.

## Optional scorecard

No scorecard was produced. No scoring rubric was requested or accepted.

## Recommendations

The smallest lawful sequence is:

1. Root owner gate: decide the `FAN-001` severity boundary and authorize a Root SCOPE_CHANGE that assigns continuing D-GOV-20 runtime semantics/conformance to explicit Root deliverable coverage.
2. App owner gate: after or in an explicitly coordinated sequence with Root, amend the App decomposition and affected runtime SOWs to retain only App client, adapter, presentation, packaging, compatibility, and acceptance duties.
3. App closure gate: create or explicitly defer the invariant register and bind exact current decomposition acceptance provenance.
4. App D-APP-48/49 gate: disposition the stale pull contract, resolve its internal source-commit conflict, and inventory current consumers before making semantic compatibility claims.
5. Root governance maintenance: bind D-GOV-27’s applied-state SHA, correct the SHA-role label, publish the missing phase handoff, repoint the completed plan, and close stale responsibility references.
6. Bounded repairs: refresh App PRD/decomposition trace metadata, annotate the terminal PR #333 merge state, carry the three PEC residuals to their affected gates, and reconcile/suspend stale derivative manifests loop by loop.

No recommendation authorizes implementation. Candidate semantic parity, universal application profiles, and resource governance remain outside accepted scope.

## Decision queue

| Decision | Human choice required | Consequence of no decision |
| --- | --- | --- |
| `DQ-01` Root runtime ownership | Whether to treat `FAN-001` as a release/complete-coverage blocker or a REVIEW remediation, and authorize the Root SCOPE_CHANGE boundary | Root authority remains clearer than deliverable ownership; complete-coverage claims stay blocked under Reviewer A’s bounded reading |
| `DQ-02` App runtime narrowing | Accept the Root-owner/App-client semantic split as the basis for an App SCOPE_CHANGE and affected SOW amendment | App can continue to carry divided generic-runtime semantics |
| `DQ-03` App review prerequisites | Create the invariant register versus explicitly defer it; bind prior acceptance provenance versus re-accept exact current bytes | App cannot lawfully claim the decomposition’s own REVIEW prerequisites are complete |
| `DQ-04` D-APP-48/49 disposition | Retire, supersede, or repin the pull; resolve ruling/JSON source identity; select compatibility evidence | The ruled compatibility path remains internally conflicted and 12/12 stale |
| `DQ-05` Record-repair tranches | Authorize the smallest Root/App/PEC governance and coordination repairs without reopening accepted topology | Navigation, SHA, handoff, citation, and derivative-detection debt persists |

## Handoff summary

- Review-stage verdict: `COMPLETE_PENDING_HUMAN_DISPOSITION`
- Product acceptance: not granted
- Derivative status: this evaluation package is derivative of the frozen Root/App/PEC basis and cannot replace decomposition truth
- Waivers: none
- Invalid returns: none
- Genuine review blocker: none; the full charter-prescribed review stage is complete
- Genuine product/owner gate: `FAN-001` blocks only the claim that Root decomposition completely allocates D-GOV-20 unless the human adopts Reviewer B’s REVIEW-only severity; App REVIEW prerequisites and runtime semantic narrowing also require owner action before their affected lifecycle claims
- Rerun posture: preserve both independent reports and challenges; after accepted changes, update the manifest and rerun only the affected trace/boundary rows

See `HANDOFF.md` for the decision-ready stop state.
