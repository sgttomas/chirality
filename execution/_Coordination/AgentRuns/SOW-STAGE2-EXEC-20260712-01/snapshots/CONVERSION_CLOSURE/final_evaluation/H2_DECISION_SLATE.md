# H2 Legacy-Retirement Decision Slate

Decision basis: exact
`origin/main@79de30d83b91a2ab468a3f17536a5233c2f85fe7`, with final independent
conversion-closure evaluation `PASS`.

The options below are mutually exclusive. Selecting one does not authorize
writes outside its stated boundary. **Silence performs no retirement and
leaves every current compatibility surface supported.**

## H2-R — Retain compatibility; no retirement — RECOMMENDED

Keep the eight ruled PKG-00 legacy contracts, the compatibility-only
`four-documents` skill, the legacy validator, all active format-aware callers,
and all rollback/historical evidence unchanged.

- Permitted writes: the H2 ruling record, closure pointer, work graph, and
  receipt only; no project, skill, tool, caller, lifecycle, rollback, or
  historical-evidence write.
- Required checks: exact-basis and ruling-hash binding; no implementation
  suite is triggered because live behavior is unchanged.
- Consequence: current PKG-00 maintenance and the full human-gated rollback
  path remain supported. Maintenance cost and dual-format compatibility code
  remain.
- Rollback posture: unchanged and complete at 730 bound inverse rows.

## H2-P — Prepare bounded partial retirement

Authorize a fresh design/evidence lane to remove compatibility authoring while
retaining legacy read/resolve/validate behavior for the eight PKG-00 contracts
and for human-authorized rollback. This knowingly proposes making current
legacy contracts and rollback-restored kits read-only to TASK production
maintenance unless a replacement maintenance method is accepted.

- Permitted writes before a second integration gate: a new H2-P run under
  `execution/_Coordination/AgentRuns/**`, isolated candidates for the four
  `skills/four-documents/*` files, and candidate-only edits to direct registry,
  dispatcher, and test callers selected from `LEGACY_SURFACES.tsv`. No live
  project, lifecycle, evidence-history, rollback-manifest, or accepted caller
  integration is permitted.
- Required checks: exact changed/caller manifest; proof the eight PKG-00
  contracts still resolve, validate, render/read, audit, and review; negative
  new-initialization tests; rollback simulation through restored-format
  validation; root/App/Piping suites; independent EVALUATION and
  RECONCILIATION; explicit human acceptance of lost maintenance capability;
  CHANGE for any later integration.
- Consequence: smaller authoring surface, but supported semantic maintenance
  of the only eight live legacy contracts is removed unless replaced.
- Rollback posture: content restoration remains possible; post-restore
  maintenance becomes unsupported unless the design supplies a replacement.

## H2-F — Prepare full legacy retirement

Authorize only a consequential prerequisite lane: amend the active PKG-00
human ruling, convert or otherwise lawfully replace all eight live PKG-00
contracts, close their caller and lifecycle effects, and define a replacement
for the accepted inverse rollback before proposing deletion of any legacy
reader, validator, skill, alias, or compatibility branch.

- Permitted writes before a second integration gate: a new H2-F
  decision/design run and isolated candidates only. No current project,
  lifecycle, skill, tool, caller, rollback, or evidence-history write is
  authorized by this option alone.
- Required checks: new human-approved PKG-00 amendment; eight-member
  preservation and lifecycle proof; fresh global legacy-kit census at zero;
  exact caller removal manifest; replacement rollback design; root/App/Piping
  suites; independent evaluation/reconciliation; CHANGE integration gates.
- Consequence: eventual single-format runtime is possible, but this option
  changes the ruled PKG-00 basis and the accepted rollback contract. Immediate
  full deletion at the current basis is non-conformant.
- Rollback posture: the current 730-row legacy inverse cannot be retired until
  an explicitly accepted replacement provides equivalent recovery.
