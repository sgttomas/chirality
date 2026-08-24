# N1 HELPS_HUMANS Return — K-CONTROL-1 Design Amendment

- **Terminal status:** `COMPLETE`
- **Role:** HELPS_HUMANS (Agent 1); managed by HELP_HUMAN; no delegation
- **Basis:** `origin/main@162fa3be8d62b042177d4a256ef54bf15bd74a03`
- **Steer SHA-256:** `c0a9b1098fc9e36d1532dc1834424ee94f40b716d37f3c8b8c12dfb26a807c29`
- **Fresh review:** zero actionable findings

## Result

The ratified K-CONTROL-1 definition is amended in one row only. It preserves
the authenticated project-scoped HTTP/1.1 control socket, its exact path and
permissions, and the no-TCP rule. It adds exactly one private
daemon-to-Delegated-Harness Process Supervisor Unix-domain socket under the
same permission discipline, never renderer- or CLI-callable, grounded in
R7-A/DEL-02-07. The row calibrates current state explicitly: the supervisor
socket is accepted design but not implemented, one control socket is live
today, and the second socket becomes live only through the separately gated
DEL-02-07/WP-03 pathway. No third socket is permitted.

The enforcement cell retains socket-mode, authorization, stale-owner, and
listener tests and adds design-gated supervisor-socket tests that activate
with DEL-02-07 implementation. No amendment note was added because
`docs/CONTRACT.md` has no convention requiring one for a governed row change.

## Exact row pre-image

The following is the complete pre-image row byte sequence, followed by one
terminating LF byte:

```text
| **K-CONTROL-1** | Runtime control uses authenticated, project-scoped HTTP/1.1 over `{userData}/runtime/control.sock` beneath a `0700` directory with a `0600` socket. A TCP control listener is forbidden. | Socket-mode, authorization, stale-owner, and listener tests |
```

- Row SHA-256 including terminating LF:
  `bf5a41e23c95591c6de57e718158af6fede01e99d9cae688bd2fcfc68c285a71`
- Full-file pre-image SHA-256:
  `ed87eaff4e936bb76f94e1bf3018f708c54c23167e6b4884a7f17193c9dcf679`

## Exact row post-image

The following is the complete post-image row byte sequence, followed by one
terminating LF byte:

```text
| **K-CONTROL-1** | Runtime control uses authenticated, project-scoped HTTP/1.1 over `{userData}/runtime/control.sock` beneath a `0700` directory with a `0600` socket. The accepted design adds exactly one private Unix-domain socket between the daemon and the Delegated-Harness Process Supervisor, never renderer- or CLI-callable, with a `0700` parent directory and a `0600` socket, as accepted by R7-A through the DEL-02-07 scope contract (record SHA-256 `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53`). The supervisor socket is accepted design, not yet implemented: exactly one control socket is live today, and the second socket becomes live only through the separately gated DEL-02-07/WP-03 implementation pathway. No third socket and no TCP control listener are permitted under any configuration. | Socket-mode, authorization, stale-owner, and listener tests; design-gated supervisor-socket tests activating with DEL-02-07 implementation |
```

- Row SHA-256 including terminating LF:
  `2473b7eb8cadf4f8fb6e059bc593aa91585c21a1bc694c1a598d779196392a8a`
- Full-file post-image SHA-256:
  `ad0a4e6ae53853692205b34b2c4416e23d19dabb73079049e5acec09b5beeb83`

Programmatic reconstruction of the full pre-image with only the old row
replaced by the new row equals the post-image byte-for-byte.

## Manifest

- Path:
  `docs/governance_harness/tranche_manifests/ROOT-CONTRACT-KCONTROL1-DESIGN-2026-08-23.yaml`
- SHA-256:
  `2d3b988643b57c7bc2b5ed50e0ca2e730f37fa14a399f394f7d7e41163f9a5a3`
- Direct schema validation: `failures=[]`.
- The parsed `m2_gate.authorization` is byte-for-byte equal to the complete
  N1 section of the governing steer.
- Instruction-surface paths are exactly `docs/CONTRACT.md` and the manifest.
- Gate is `human-gated-pr`; `self_merge: false`; notice is pending with empty
  routing; public-export derivation is deferred.

## Checks

- Basis merge is present and is an ancestor of `HEAD`; `HEAD` and
  `origin/main` were both `162fa3be8d62b042177d4a256ef54bf15bd74a03`
  at node start.
- Receipt 125 is present on the basis.
- DEL-02-07 accepted SOW SHA-256 is
  `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5`.
- Task Management register SHA-256 remains
  `89ffd2ad3f85a97dd814e147c606ad3a6aef14a173678d65163445e7b096c518`.
- Contract diff is exactly one removed row and one added row at line 162;
  no other contract byte changed.
- Invariant-ID count remains exactly 40.
- Agent-instruction validator: 34 files, 0 errors, 0 warnings.
- Instruction-entrypoint validator: PASS.
- `git diff --check` passes for the N1 content outputs.
- Candidate-whitespace validation: PASS. Its first run found only terminal
  blank lines in four parent-created run/control files outside this instance's
  write scope; the parent normalized those files, and the fresh global rerun
  passed. No N1 contract or manifest finding was reported.

## Fresh review

Fresh review re-read the complete final row against each of the five steer
requirements and found zero actionable semantic, claim-calibration,
authority-boundary, invariant-count, manifest, containment, or scoped
whitespace findings. No implementation, activation, dispatch, App, pin, hold,
release, or reliance authority is claimed.

## Changed paths owned by this node

- `docs/CONTRACT.md`
- `docs/governance_harness/tranche_manifests/ROOT-CONTRACT-KCONTROL1-DESIGN-2026-08-23.yaml`
- `execution/_Coordination/AgentRuns/ROOT_KCONTROL1_DESIGN_2026-08-23/instances/N1_HELPS_HUMANS_KCONTROL1/RETURN.md`
- `execution/_Coordination/AgentRuns/ROOT_KCONTROL1_DESIGN_2026-08-23/instances/N1_HELPS_HUMANS_KCONTROL1/STATUS.json`

No scope widening was required. The owner's merge of the eventual PR remains
the ratification act.
