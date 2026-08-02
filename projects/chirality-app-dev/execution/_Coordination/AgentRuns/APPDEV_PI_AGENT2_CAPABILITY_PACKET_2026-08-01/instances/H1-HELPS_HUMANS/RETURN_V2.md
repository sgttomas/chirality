# HELPS_HUMANS Manager Return V2 — D-APP-84 Proposal Revision 2

Status: `COMPLETE / VALIDATED`

RunID: `APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01`

AcceptedBasis: `fc06b3388de17dcd5fc65eb29bf77c7f551a64cc`

ScopedDriftHead: `origin/main@23d15899fd0acf5d1d0513f3fe396438375c9e25`

CurrentProposalSHA256:
`59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9`

SupersededUnruledRevision1SHA256:
`0f4ddfb3c71b1862225ce35430fc18b275588b2dfafbca7d884aaef524a9830e`

## Result

Revision 2 is owner-presentable. It recommends a Pi-native-first architecture
behind Chirality contracts, a separate role/run-specific OS sandbox for every
tool-executing Agent 0/1/2 instance, Root-conditioned sandboxed Agent-2 Bash,
explicit version concordance, and strict replay/binding. It creates none of
those effects before later Root/App gates.

The manager repaired two substantive adversarial findings:

1. P1 now selects exactly one implementation family at accepted versioned
   profile/registration time. A selected primitive's failure rejects the
   operation; there is no runtime tool fallback or substitution. Changing
   implementation family requires renewed evidence and a new session.
2. §3 now identifies the all-agent worker layout as the X1 recommendation,
   not a requirement that contradicts X2/X3. Common non-bypass invariants remain
   mandatory for every sandboxed native or mutating tool.

## Exact decision interface

Recommended response:

```text
APPROVE D-APP-84 REVISION 2: B1 + V1 + P1 + X1 + H1 + R1.
```

Other valid B1 responses select exactly one V/P/X/H/R token and satisfy the
packet's compatibility rules. Standalone responses:

```text
HOLD D-APP-84 REVISION 2: B2.
ROUTE D-APP-84 REVISION 2 OWNERSHIP TRANSFER: B3.
DECLINE D-APP-84 REVISION 2: D.
```

The recommendation is non-binding. No omitted token is inferred.

## Authority and architecture conclusions

- Pi is still Agent-2-only. Native primitive reuse does not expose Pi native
  delegation, subagents, ambient resources, extensions, skills, prompts,
  settings, credentials, provider selection, or native permission authority.
- Chirality retains public tool identity/schema, versioned registration,
  exposure policy, pre-execution authorization, human gates, path/mount
  derivation, result bounds/redaction, canonical events, evidence,
  interruption, and audit.
- X1 recommends a fresh separate sandbox per tool-executing role/run instance,
  never a single shared sandbox. Profiles differ by sealed authority.
- H1 grants no Bash now. Until a separate Root ruling and implementation
  replaces current doctrine, a Bash-bearing managed child still requires
  project-root read/write scope and serialized integration ownership.
- No live App/Root OS agent/tool sandbox exists. Chromium's Electron renderer
  sandbox applies only to the GUI renderer, not the headless daemon, agent
  sessions, or tool execution.

## Drift and write containment

`origin/main` is four commits ahead of the accepted basis with merge-base equal
to the basis. A scoped `git diff --quiet` proves no intervening change to
`AGENTS.md`, `agents/**`, `runtime/**`, `projects/chirality-app-dev/**`,
`docs/WORKFLOW_COMPONENT_STANDARD.md`, or `docs/DECOMPOSITION_STANDARD.md`.
No rebase or merge was performed.

Changed paths remain limited to:

- Revision 1 and Revision 2 D-APP-84 proposal surfaces;
- the single D-APP-84 `AWAITING_RULING` register row; and
- this existing RunID's records.

No authority, runtime, frontend, decomposition, deliverable, SCOPE_CHANGE,
Task Management, receipt, parity, historical-UNKNOWN, lifecycle, release,
publication, commit, push, or merge effect occurred.

## Validation

- Revision 1 exact SHA-256: `PASS`.
- Revision 2 hash binding: `PASS`.
- Scoped origin/main drift: `PASS / DISJOINT`.
- D-APP-84 register uniqueness and Revision 2 linkage: `PASS`.
- AgentRuns JSON parse and acyclic v2 work graph: `PASS`.
- `git diff --check`: `PASS`.
- App loop receipt validator: `PASS`, frozen through Receipt-52; no receipt
  changed or was appended.
- Authority corpus v18 status/audit: `PASS`, all eight sources match and all
  deliverable reference rows remain reconciled.
- Fresh read-only adversarial review: `COMMIT-SAFE / OWNER-PRESENTABLE`; no
  remaining blocker, major, or repair-requiring minor.

Next lawful owner: `HELP_HUMAN` for independent fan-in and presentation to the
App owner. No ruling or implementation is inferred.
