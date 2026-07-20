# W3 D-APP-50 Result-Contract Repair Return

## Terminal result

`REPAIRED_AWAITING_G1_COMMIT`

V1 findings F-001 and F-002 are repaired within the released scope. There are
no blockers, unknowns, conflicts, or waivers. Git, D-APP-48 repin, status,
receipt, descriptor, registry, documentation, and lifecycle closeout remain
held for their downstream gates.

## Basis and write containment

- Branch: `codex/app-dev-dapp50-headless-live-20260720`
- Required and reproduced HEAD:
  `f67d44706f4b2b5495833f809cb0bc714d2bbc18`
- Role: WORKING_ITEMS, sole serialized repair owner
- Delegation: none
- Git action: none
- Implementation write population: exactly two tracked files:
  1. `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts`
  2. `projects/chirality-app-dev/frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts`
- Terminal-control writes: this `RETURN.md`, sibling `HANDOFF.md`, and terminal
  `STATUS.json` only.

No descriptor, tool catalog, registry version, runtime documentation,
read-tools wiring, pull contract, deliverable status/run record, receipt,
decision state, piping, tier-0, pec, release, lifecycle, or unrelated source
was edited by W3.

## F-001 repair

The adapter now fails closed on the complete app-facing DEC-065 `solve` result
transport shape:

- exact required and allowed CLI-output keys, fixed artifact/schema/package/
  deliverable/command/operation identities, and unknown-key rejection;
- the exact 10-key DEC-065 local-process policy and all settled values;
- exact validation-object shape and full diagnostic-record validation with
  allowed class/severity tokens;
- the full 11-key runner-result contract, including run/job progress and
  cancellation fields, analysis-status vocabulary, result-envelope reference,
  result and audit references, checksums, privacy, provenance, professional
  boundary, and diagnostics;
- top-level, request-validation, result-validation, and runner-result
  diagnostic participation in exit correlation;
- exit 0 requires a completed runner result, non-null result validation and
  mechanics envelope, and no blocking diagnostic; exit 1 requires a blocking
  diagnostic; schema defects retain
  `HEADLESS_RUNNER_RESULT_SCHEMA_MISMATCH`.

The positive fixture is now structurally complete and invented, following the
committed piping solve-witness shape field-for-field. Negative coverage includes
missing/wrong package and deliverable identities; incomplete, contradictory,
ill-typed, and extra policy fields; missing/ill-typed/extra validation members;
missing/incomplete/extra runner-result members; bad nested job, analysis,
reference, checksum, privacy, professional-boundary, and diagnostic fields;
extra top-level `padding`; and exit/result mismatches. Oversized valid-result
coverage now uses contract-valid result references rather than an unknown
padding member.

### Final repair hashes

| Path | Basis SHA-256 | Repaired SHA-256 |
|---|---|---|
| `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` | `eac51da403aa5f91c1bf9fcf0ab5c62efcc46a7e1b526ca097213fdf617dfc57` | `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109` |
| `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` | `12ea34a53611bb0a5a2c5010d1d7f0525960c783753e7f4b162b2b2c6116ba94` | `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41` |

## F-002 exact cleanup

Immediately before deletion W3 revalidated the exact absolute target:

- path and realpath:
  `/Users/ryan/.codex/worktrees/2d6d/chirality/projects/chirality-app-dev/frontend/dist`;
- non-symlink directory, one device (`16777230`), no mount boundary;
- top-level members exactly `builder-debug.yml` and `mac-arm64/`;
- `mac-arm64/` member exactly `Chirality.app/`;
- `builder-debug.yml`: 948 bytes;
- `Chirality.app/**`: 163 regular files / 839,495,218 bytes;
- total: 164 regular files / 839,496,166 bytes;
- 14 bundle-internal symlinks, all resolving inside the exact `dist/` root;
- 497 enumerated files/directories/symlinks all ignored by
  `frontend/.gitignore:4:dist/`; tracked 0; staged 0;
- packaging-output mtimes in the V1 `2026-07-20 11:13:44–49 -0600` interval,
  with the V1-noted older copied-resource birth metadata retained only inside
  the newly born bundle root.

W3 recursively deleted only that exact absolute directory after the final
predicate pass. The path is absent after all builds/checks, and no relevant
builder, `desktop:pack`, Next, Vitest, or runner process remains. `.next` and
`dist-electron` were not cleanup targets; they remain separate ignored normal-
build outputs. The removed ignored packaging output is reproducible only by
rerunning packaging and is not Git-restorable.

## Validation

- Focused headless transport Vitest: PASS, 48/48 after final formatting.
- Adjacent transport/registry/descriptor/evidence Vitest: PASS, 89/89 across
  six files.
- Full frontend Vitest: PASS, 776 passed / 4 skipped across 98 passed and one
  skipped test file.
- Frontend TypeScript typecheck: PASS, including a final post-format rerun.
- Production Next/Electron build without packaging: PASS.
- Registered managed-service frontend premerge: PASS; check exit 0 in 14.543s,
  isolated loopback service reached READY and was stopped after the run.
- D-APP-48 pull-contract validator: PASS; its exported contract bytes were not
  changed by these two non-export repair paths.
- Harness-contract dependency lint: PASS.
- App-dev receipt validator: PASS; no receipt was changed.
- Authority corpus v9: PASS, 8/8 match, no drift.
- Repository practitioner self-check: exit 0 at the existing 3 REVIEW / 6 WARN
  baseline.
- `tools/validation` pytest: PASS, 123/123.
- `tools/practitioner_harness` pytest: PASS, 311/311.
- Final tracked whitespace, staged-path, protected-scope, exact-hash, cleanup-
  absence, and process-containment checks: PASS; staged paths are empty.

Packaging, network proof, and instruction-root bundle proof were not run, as
the sealed W3 brief prohibited them.

## Retained boundaries and next gate

The W2 closeout surfaces remain byte-identical:

- D-APP-48 pull contract:
  `bfe99e17541b2840795cde054f29ddad9fa390610fb58accaafc133c8a22204b`
- DEL-10-01 `_STATUS.md`:
  `028fd7b16e1306e1e6977636cf3f924475990c7d9550750d3cf05d10e141aacb`
- Receipt ledger:
  `397fb8ddceef25efe56fa146463c47e34b6a5ab0937a6e418bd163006d45f4db`

No apply/proposal capability, protected-path write, piping/tier-0/pec edit,
network/provider expansion, packaging/publication/distribution act, lifecycle
transition, or professional/certification/sealing/authentication/code-
compliance/solver-truth claim occurred.

The only next gate requested is G1 CHANGE commit-only publication of the exact
two repaired tracked files. D-APP-48 repin and a fresh independent EVALUATION
remain downstream and unreleased by W3.
