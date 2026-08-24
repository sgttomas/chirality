# Root v3 Phase 4 orchestration plan

- **Run ID:** `ROOT_V3_PHASE4_2026-08-23`
- **Plan version:** 1 (frozen before dispatch)
- **Selection authority:** HUMAN — Ryan Tufts Phase 4 owner-carried steer
- **Basis:** `origin/main@7974f2d4a456777f2132fb5726a67a042137ca78`
- **Posture:** ordered terminal fan-out/fan-in
- **Objective:** produce an hours-only, provenance-first estimate candidate for the seven SCA-004 carriers and the incremental DEL-02-06 fan-in work, then independently review and seal one immutable derivative snapshot for owner acceptance.

## Ordered nodes

1. `N1_CARRIER_ESTIMATES` — define the package estimate method and draft seven carrier estimates.
2. `N2_DEL0206_REASSESSMENT` — independently draft the DEL-02-06 incremental fan-in reassessment; depends on N1 only for the shared estimate-method definitions.
3. `N3_SNAPSHOT_REVIEW` — independently review and repair the eight estimates, assemble summary and provenance pins, and seal the snapshot; depends on N1 and N2.

Writes are serialized. N1 and N2 write disjoint estimate files. N3 may repair any file inside the new snapshot folder under the unlimited-repair/fresh-review rule and must disclose every repair. Each node owns only its sealed brief's snapshot targets and its own instance return/status. HELP_HUMAN owns the run-level control records, Receipt 124, Root handoff append, validation, Git commits, push, and PR creation.

## Method disposition

The repo-native `estimate-snapshot` TASK method supplies provenance, no-invention, confidence/uncertainty, immutability, and human-acceptance discipline. Its generic commercial-pricing interface (`BASIS_OF_ESTIMATE` cost enum, currency, price sources, `_Estimates/` destination) does not describe this owner-directed hours-only snapshot. The Phase 4 steer therefore controls the exact path, inputs, hours unit, output form, and absence of currency, cost, or schedule computation.

## Fan-in gates

- N1: seven estimates cover accepted SOW outputs; every work element has base hours, uncertainty class, range, and accepted-source citations; exclusions and sequencing risks are explicit.
- N2: only incremental integration/fan-in work currently estimable is priced in hours; all held work remains excluded.
- N3: candidate-whitespace precheck already passed before any pinning artifact; input pins reproduce; totals and ranges recalculate; independent review has zero actionable findings after disclosed repairs; `RETURN.md` closes `AWAITING_OWNER_ACCEPTANCE`.

## Human gates and stops

Stop for drift, an out-of-scope write, an estimate element not groundable in accepted truth, an implied schedule, acceptance, seating, implementation, activation, pin assumption, App authority, hold lift, or foreign write. Estimate acceptance, scheduling, later evidence reruns, and implementation remain outside authority.
