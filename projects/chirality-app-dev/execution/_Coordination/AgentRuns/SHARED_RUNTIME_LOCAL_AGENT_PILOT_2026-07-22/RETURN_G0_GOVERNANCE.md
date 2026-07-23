# G0 Return — Shared Runtime Governance Reconciliation

## Outcome

`G0` completed with integration-owner remediation of the root downstream
surfaces after the bounded writer stopped responding during its final pass.
No runtime, Desktop, PEC implementation source, package manifest, or lockfile
was changed.

## Rulings and snapshot

- Root: `D-GOV-20`
- App: `D-APP-73`
- Domain convergence: `D-T0-23`
- PEC: `D-PEC-56`
- App scope snapshot: `SCA-APP-003`
- Owner approval: 2026-07-22 instruction to implement the accepted Shared
  Runtime and Local-Agent Pilot.

The rulings preserve historical decisions and open gates. In particular,
`D-PEC-49` remains `AWAITING_RULING`; production PEC, automatic or forced
model switching, multiple resident primary local models, durable model-role
defaults, local Agent 1, direct Pi supervision, Pi write/shell/network,
automatic LaunchAgent installation, release, publication, and issuance remain
outside authority.

## Reconciled surfaces

- Root Agent doctrine; DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN; README and
  framework explanation; public-export policy and allowlist.
- App AGENTS; six authority documents; build, validation, and release gates;
  reliance boundary; decomposition; affected status Remaining records;
  D-APP-73 and complete SCA-APP-003.
- Tier-0 domain-engine register, profile, index, standing workplan, receipts,
  and active bridge-design brief.
- PEC AGENTS, register, SPEC, TRACEABILITY, STATUS, README, ADR, sidecar
  boundary, and pilot runbook.

## Validation

- D-APP-38 corpus initially bumped from v12 to v13, then to v14 after the
  independent G0A audit required the accepted LaunchAgent lifecycle and full
  CLI contract to be restored to app authority.
- Corpus status: all eight registered authority sources match.
- Corpus audit: all generated deliverable reference rows reconcile to v14.
- SCA-APP-003 artifact inventory: 13 required snapshot files present.
- Supersession accumulator: 11 cumulative rows, zero findings, zero blockers.
- `git diff --check`: pass after integration-owner whitespace remediation.

`tools/validation/validate_scope_change_packet.py` targets the unrelated
PKG-00 consumable-packet schema and is not applicable to the accepted
SCA-APP snapshot format; its expected missing-file report was not treated as
SCA validation.

## Attribution

- Bounded governance writer: Codex child, actual model `gpt-5.6-sol`
  (inherited parent configuration).
- Integration owner/remediation: HELP_HUMAN Codex session, actual model
  `gpt-5.6-sol`, high reasoning effort.
- No model substitution occurred.

## Fan-in gate

Implementation remains blocked until the independent read-only `G0A`
authority audit accepts this return and the resulting diff.
