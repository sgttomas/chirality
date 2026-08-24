# Sealed Launch Brief — N1_HELPS_HUMANS_KCONTROL1

Role: HELPS_HUMANS (Agent 1)
Parent: HELP_HUMAN
Delegation: no child delegation is needed for this bounded single-row act
Basis: `origin/main@162fa3be8d62b042177d4a256ef54bf15bd74a03`

## Objective

Implement the exact N1 design-amendment tranche directed by
`plans/steers/chirality_app_v3_kcontrol1_amendment_steer_root_2026-08-23.md`
at SHA-256
`c0a9b1098fc9e36d1532dc1834424ee94f40b716d37f3c8b8c12dfb26a807c29`.

## Required reads

- `AGENTS.md`
- `agents/AGENT_HELPS_HUMANS.md`
- the complete governing steer above
- A4 and A5 companion records named by the steer
- canonical R7 record
  `plans/steers/chirality_app_v3_root_ruling_record_r7_2026-08-23.md`
- `docs/CONTRACT.md`, especially subsection 1.13
- one current schema-v1 manifest as a formatting model

## Write scope — exact

- `docs/CONTRACT.md`: replace only the K-CONTROL-1 table row. Do not add an
  amendment note unless the document convention strictly requires it.
- `docs/governance_harness/tranche_manifests/ROOT-CONTRACT-KCONTROL1-DESIGN-2026-08-23.yaml`: new live manifest exactly as the steer specifies.
- This instance's `RETURN.md` and `STATUS.json` only.

No other write is authorized.

## Row requirements

Preserve the current authenticated project-scoped HTTP/1.1 control socket at
`{userData}/runtime/control.sock`, `0700` directory, `0600` socket, and no-TCP
rule. Add exactly one private daemon-to-Delegated-Harness Process Supervisor
Unix-domain socket, never renderer- or CLI-callable, under the same permission
discipline, grounded in R7-A/DEL-02-07. State that it is accepted design but
not implemented: one control socket is live today, and the second becomes live
only through the separately gated DEL-02-07/WP-03 implementation pathway. No
third socket. Extend verification with design-gated supervisor-socket tests
while retaining the existing socket-mode, authorization, stale-owner, and
listener tests.

## Manifest requirements

Schema v1; tranche ID and filename correspond to
`ROOT-CONTRACT-KCONTROL1-DESIGN-2026-08-23`; basis is the current main SHA;
instruction-surface paths are only `docs/CONTRACT.md` and the manifest;
human-gated PR; `self_merge: false`; authorization is the governing steer's
N1 section verbatim; pending notice with empty routing; derivative export
disposition deferred. Scope limits must make the design-only and no-foreign-
authority boundaries explicit.

## Acceptance checks and return

Record the exact pre/post row bytes, full-file pre/post SHA-256, manifest SHA,
changed-path containment, invariant-ID count (40), and fresh review findings.
If any required semantic cannot fit in the single row or any other file would
need to change, stop and return the blocker without widening.
