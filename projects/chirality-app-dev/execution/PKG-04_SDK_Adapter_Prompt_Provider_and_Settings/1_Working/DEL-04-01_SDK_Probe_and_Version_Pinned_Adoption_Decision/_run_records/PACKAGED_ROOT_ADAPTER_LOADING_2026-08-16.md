# Packaged Root adapter loading — 2026-08-16

- RunID: `APPDEV_PACKAGED_ADAPTER_LOADING_2026-08-16`
- Basis: `65735390590e500dbbea6b63a4a79ba42944bf6d`
- Authority: D-APP-72, D-APP-73, accepted SCA-APP-003, and the live
  DEL-04-01 packaged-runtime Remaining item. APP-HOLD-1 dispatch and final scan
  allow the work.

## Product result

`frontend/electron/runtime-host.ts` now registers the promoted Root Claude and
Pi factories around the existing App turn-runtime implementations. SafeStorage
credential ownership, prior capability descriptors, interrupt propagation,
Pi Agent-2/tool restrictions, and residency behavior are preserved. The
Electron build resolves Root `engine-claude`; package/lock and Electron
TypeScript resolution include the Root package.

The shared-daemon integration executes Desktop and CLI traffic through the
Root Pi wrapper and checks emitted selected-model attribution. Runtime-host
coverage checks exact package/provider/version and capability attribution:

- `anthropic-direct` / Anthropic / `@anthropic-ai/sdk@0.93.0`;
- `claude-agent-sdk` / Anthropic /
  `@anthropic-ai/claude-agent-sdk@0.3.150`;
- `pi` / oMLX / `@earendil-works/pi-coding-agent@0.82.0`.

The packaged dependency verifier reads the Desktop source map from the actual
`app.asar`, proves Root client, daemon, Claude, and Pi wrapper sources are in
the packaged Desktop host, proves Root CLI/client sources are in the packaged
CLI, and rejects daemon, engine, or App-host sources in that client-only CLI.

## Evidence and review

- Focused Vitest: 11 pass.
- Full Vitest: 1,124 pass / 4 skip across 144 passing files / 1 skipped file.
- Typecheck: pass; production build: pass.
- Local unsigned macOS arm64 `desktop:pack`: pass. Packaged verifier: pass,
  zero monorepo-only package entries, Root source proof pass with 182 Desktop
  and 15 CLI sources; instruction-root integrity exits pass at its existing
  source-completeness label.
- Practitioner pytest: 349 pass; repository self-check exit 0; APP-HOLD scan
  pass with register agreement.
- Fresh read-only `TASK + software-code-review`: PASS, no actionable findings,
  all nine frozen path hashes matched.
- Registered local premerge ran with an owned Next service and stopped it; its
  eight Section 8 rows returned the established isolated-profile 503 advisory
  because the profile supplies no shared-runtime socket/token/project binding
  after daemon-client migration. Receipts 110–112 classify this as a
  non-blocking PR-CI/live-runtime rerun advisory. No waiver or passing product
  inference is asserted.
- D-APP-36: not applicable because no UI behavior or rendering changed.

The first clean dependency run exposed unbuilt Root file-link packages. Checks
were rerun against a compiled read-only `/private/tmp` Root copy with transient
frontend links; Root `runtime/**` remained byte-unchanged. All dependency,
build, package, and temporary-copy artifacts were then removed.

## Disposition

The exact packaged-root GUI/daemon/CLI proof item is complete and removed from
`Remaining`. DEL-04-01 stays `IN_PROGRESS`; its Checking Approval SHA and
historical evidence are unchanged. No provider/network expansion, Root runtime
write, lifecycle act, release-readiness claim, distribution, waiver, or owner
decision occurred. The run artifacts are derivative evidence tied to the basis
above; owner-gated CHANGE/PR-CI closeout remains.
