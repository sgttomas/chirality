# EVALUATION Report — D-APP-50 Headless Preview Repair Backcheck

## Verdict

`BLOCK`

V1 F-002 is cured, and most of F-001's structural repair is effective, but one
deterministic nested-reference correlation remains fail-open. The adapter
accepts an exit-0 result whose declared result envelope has no matching
checksum. The final piping validator would emit a blocking diagnostic for the
same result. Final CHANGE publication must remain held.

## Basis and coverage

The evaluated subject is branch
`codex/app-dev-dapp50-headless-live-20260720` at
`fcf152bdae1e1764b11dfabf3f87d50c5680213d`, plus the uncommitted W2/W4
closeout. G0 has the required single parent
`bc35e3b0049d990f494dd3610603be285c7aa9ed`; G1 has G0 as its single parent.
All nine released V2 questions were inspected. No child was dispatched and no
score was requested.

## Commit and transport findings

- G0 contains exactly the frozen 14 implementation paths, and all 14 committed
  SHA-256 values reproduce. G1 contains exactly the two repair paths at
  `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109`
  and `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41`.
  The frontend is clean against G1; no frontend source byte changed outside
  those commits.
- The original configured-local transport controls remain present: explicit
  absolute runner path and lowercase SHA-256; realpath, regular-file, `X_OK`,
  and byte-hash verification immediately before a direct `solve` spawn;
  `shell: false`; minimal environment; exact stdin; stdout-only JSON; timeout,
  reaping, and separate 2 MiB caps; stable sanitized errors; and contained
  regular-file `runnerInputRef` resolution.
- Profile, registry, and descriptor gates remain exact to registered
  `open_pipe_stress`. The tool stays read-only, `project-root-read`,
  input-dependent, exclusive, and non-confirming. `pec`, unknown, missing,
  mismatch, outside-root, symlink-escape, and non-file cases refuse.
- The normal read-MCP permission, event, redaction, result-budget, evidence,
  and artifact pipeline remains in use. No proposal/apply/accept, provider or
  network, output-path or sidecar, piping implementation, lifecycle, release,
  professional, or solver-truth expansion was found.

## V1 F-001 repair assessment

The repaired assertion now enforces exact top-level identity/allowed keys, the
full ten-key DEC-065 process policy, typed validation objects, exact diagnostic
record shapes, the 11-key runner result, nested job/status/reference/privacy/
provenance/professional-boundary structures, unknown-key rejection, and basic
exit/diagnostic correlation. The focused suite exercises the reported V1
missing/extra/type/token cases and passes 48/48.

The examined `TBD` diagnostic-class token is not an overacceptance: the frozen
`schemas/headless_runner.schema.yaml` diagnostic enum explicitly includes it.
The current Rust `DiagnosticClass` enum cannot emit it, but the schema-first
basis authorizes the token.

One remaining fail-open correlation is directly demonstrated by the repaired
positive fixture. It declares
`result_envelope_ref.envelope_ref.ref_id = result-envelope:invented-app-transport`
but supplies only one checksum, whose payload reference is
`runner_request/request-1`. `isRunnerResult` checks merely that the checksum
array is non-empty and every member has an individually valid shape. It does
not require a checksum for the declared result envelope.

Piping's final `validate_result` explicitly calls
`has_result_envelope_checksum` and emits the blocking
`HEADLESS_RUNNER_RESULT_ENVELOPE_CHECKSUM_MISSING` diagnostic when that
cross-reference is absent. The committed TP-RUNNER-015 exit-0 witness contains
the matching result-envelope checksum. Nevertheless the app's focused
exit-0 test passes this malformed fixture through the real configured process
transport. This contradicts W3's required full nested checksum/correlation
repair and V2's fail-closed decision criterion. It is a transport-contract
finding only, not an assertion that the app exhaustively validates solver
semantics.

## V1 F-002 and distribution state

F-002 is cured. `projects/chirality-app-dev/frontend/dist` is absent. No
`.app`, DMG, PKG, ZIP, AppImage, electron-builder/packaging process, running
Next server, Vitest process, or `openpipestress-runner` process remains.
`.next` and `dist-electron` exist as ignored normal-build outputs and are
distinct from the deleted packaging target. Required V2 validation refreshed
those ordinary generated outputs and ignored harness summaries; it did not
run packaging or create `frontend/dist`.

## D-APP-48, DEL-10-01, and receipt history

- D-APP-48 parses with strict duplicate-key rejection and hashes to
  `e01120ad843578813a558a2f9bffbf6a7504dc8d294eff983f27482dc201caa6`.
  Its source pin is reachable G1, registry version is v14, all exports are
  byte-current, and all six boundary flags remain false. Replacing only the G1
  pin with G0 reconstructs W2's exact
  `bfe99e17541b2840795cde054f29ddad9fa390610fb58accaafc133c8a22204b`
  contract, proving W4 changed no other byte.
- DEL-10-01 remains `IN_PROGRESS`; Checking Approval SHA
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec` and the complete single
  Remaining item are preserved. Its W2 and W4 history lines and distinct run
  records correctly distinguish initial closeout from V1 repair. The run
  records hash to `c64c03604ef2b043180ac2d01caa264f18be00d386aee84929d8f4aaf020b387`
  and `51365d34990e055c9ad9e8042fe845d2807d5728cbd6f002a6f2da1f85ce103a`.
- Receipt-83's prefix is byte-identical to the W2 ledger hash
  `397fb8ddceef25efe56fa146463c47e34b6a5ab0937a6e418bd163006d45f4db`.
  Receipt-84 is unique, parents Receipt-83, and examines through G1. The full
  ledger hashes to
  `819be78ee30629d5ef1b54814d6d4f849cd5816e675b8fc79899bb97cb12e2e8`.
- The decision register remains
  `af1a6dec6f30e81fc19a1aab4ecf2f99874c35c97e8d83aafadeb18ebcb33920`.
  Git-visible changes name only the three expected tracked closeout surfaces
  and the expected untracked two run records, control run, and V1 package.
  No unrelated deliverable change was found.

## Deterministic reruns

- Focused repaired transport: PASS, 48/48.
- Generated tool catalog: PASS, 2/2.
- Frontend typecheck: PASS.
- Full frontend Vitest: PASS, 776 passed / 4 skipped.
- Production Next/Electron build: PASS.
- Managed premerge: PASS, Section 8 8/8; Section 9 16/16 report-only. The
  evaluator-owned server was stopped. An initial no-server attempt reported
  the expected operational failure with zero tests before the managed rerun.
- D-APP-48 pull-contract validation and dependency lint: PASS.
- Receipt validator: PASS.
- Authority corpus: v9, 8/8 match, no drift.
- Repository self-check: exit 0 at the existing 3 REVIEW / 6 WARN baseline.
- `tools/validation` pytest: PASS, 123/123.
- `tools/practitioner_harness` pytest: PASS, 311/311.
- Tracked/no-index/cached/staged/whitespace/write-scope checks: PASS. Index is
  empty; the Git-visible subject state is unchanged from V2 entry.

## Conflicts, unknowns, waivers, and reruns

- Findings/blockers: 1.
- Conflicts: 0.
- Unknowns: 0.
- Waivers: 0.
- Required rerun: repair V2-F-001, add matching and mismatched checksum-reference
  tests, create a new reachable repair commit, repin and append correction
  history without rewriting prior evidence, then run a fresh independent
  EVALUATION. Final CHANGE remains held.

## Subject preservation

EVALUATION made no source, contract, decision, receipt, deliverable, Git,
packaging, or cleanup change. Its durable writes are quarantined to this
evaluation root and the V2 terminal instance. Required build/premerge commands
refreshed only already-ignored ordinary build and harness evidence outputs;
`frontend/dist` remains absent. The only server started by V2 was stopped.
