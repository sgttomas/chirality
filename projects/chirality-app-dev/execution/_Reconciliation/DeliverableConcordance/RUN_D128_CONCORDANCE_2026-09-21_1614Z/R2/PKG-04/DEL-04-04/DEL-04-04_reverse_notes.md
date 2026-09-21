# DEL-04-04 — reverse-pass notes

These notes cover the reverse pass for `DEL-04-04`.

- **Sealed forward ledger:** SHA-256
  `d077fd3845dd72f192ad773113ca9d0cbc491cc6e29ae5a89213d89c0e5bba85`. I re-checked it after this
  pass and it is unchanged.
- **Capability input:** `_reverse_inputs/DEL-04-04_capabilities.csv`, 328 rows across 8 areas:
  BUILD, ELECTRON, HARNESS, INSTRUCTIONS, RTCORE, SETTINGS, SHELL, WORKSPACE.
- **Validator:** the reverse file and the errata file each end with
  `RESULT PASS errors=0 warnings=0`.

## Response counts

| Response | Rows |
|---|---|
| CLAIMED_BY | 2 |
| PARTIAL | 8 |
| NOT_MINE | 318 |

- **CLAIMED_BY:**
  - CAP-HARNESS-040 → `CLM-005`: the legacy PersonaComposer.
  - CAP-INSTRUCTIONS-003 → `CLM-010.6`: common guidance plus the active role, rendered into
    Codex `developerInstructions`.
- **PARTIAL:**

  | Capability | Forward row |
  |---|---|
  | CAP-RTCORE-038 | SEC-1 |
  | CAP-RTCORE-025 | CLM-010.6 |
  | CAP-RTCORE-041 | CLM-010.10 |
  | CAP-RTCORE-042 | CLM-010.4 |
  | CAP-HARNESS-041 | CLM-010.4 |
  | CAP-SHELL-036 | CLM-010.5 |
  | CAP-HARNESS-025 | CLM-010.1 |
  | CAP-RTCORE-039 | CLM-010.8 |

## Errata

The errata file has 3 rows, all in the `ImplementationEvidence` field. No Disposition,
CauseTag or REACH tag changes.

- **CLM-010.3 and CLM-010.6: the project `AGENTS.md` citation is wrong for the live path.**
  - The sealed evidence cites `project:AGENTS` as a supplied entry of kind project.
  - At `app-owned-composition.ts:226` the App composition sets `nativeProjectDiscovery: true`.
    Because of that, `runtime-method-service.ts:563` never adds `project:AGENTS`; Codex
    discovers the project file natively.
  - The active role enters as `role:<id>` at `runtime-method-service.ts:570`.
    `native-role:*` entries are filtered out of `developerInstructions`
    (`delegated-engine-adapter.ts:39`).
  - Separation and content inclusion still hold, so both dispositions stand.
- **CLM-010.8: the cited enforcement point is disabled for Codex.**
  - The sealed evidence cites `restrictRuntimeTools` as live enforcement. CAP-RTCORE-039
    shows its result is discarded for Codex (`delegated-runtime.ts:289`, `_runtimeTools`).
  - Live enforcement is instead:
    - tool admission at `turn-coordinator.ts:161` (`restrictRequestedTools`);
    - the Codex sandbox and approval policy at `codex-supervisor.ts:104-112`. Those lines are
      not in any TOUCHED_PATHS range, so PostReleaseBasis stays `NO`.
  - ALIGNED stands.
- **Same imprecision on four more rows, not raised as errata.** SEC-1, CLM-009, CLM-016 and
  CLM-023 use a shared evidence string that lists `project:AGENTS` among the supplied entries.
  On the live path that entry is conditionally skipped. It does not bear on those rows'
  dispositions, so I did not write errata for them. The CLM-010.6 erratum shows the
  corrected wording.
- **REACH tags I cited all agree with the import graph.** I did not cite
  `native-role-config.ts`, which CAP-RTCORE-042 says is TEST_ONLY and appears LIVE only
  through the core barrel.

## Census: sealed vs errata-applied

The errata change only evidence text, so the census is identical both ways.

| Figure | Sealed | Errata-applied |
|---|---|---|
| Rows | 50 | 50 |
| IMPLEMENTED_DIFFERENTLY | 11 | 11 |
| STALE_SPECIFICATION | 10 | 10 |
| ALIGNED | 9 | 9 |
| PARTIALLY_IMPLEMENTED | 7 | 7 |
| REMAINING_STATE_MISMATCH | 6 | 6 |
| NOT_AUDITABLE | 4 | 4 |
| DOCUMENTED_UNIMPLEMENTED | 2 | 2 |
| STALE_VERIFICATION | 1 | 1 |
| HumanDecisionNeeded ≠ NO | 21 | 21 |

## Coverage gaps

There are none that need a new forward row. Every capability I answered CLAIMED_BY or PARTIAL
maps to an existing row.

One observation is worth a verifier's attention. CAP-INSTRUCTIONS-003 notes that
`rootVersion` (`runtime-method-service.ts:650`) hashes the packaged `instructionRoot/AGENTS.md`,
not the user-edited copy that is actually supplied. The per-entry sha256 still covers the
supplied bytes. However, this is relevant to the organisation-layer pin work: if the pin is
built on `rootVersion`, it would verify the wrong file. The sealed ledger raises the
fingerprint and pin gap at SEC-2, CLM-010.10 and REM-1, but no row names this specific point.

## Capabilities that look owned elsewhere

| Capability | Likely owner |
|---|---|
| CAP-WORKSPACE-038 (governed-workflow grammar) | DEL-07-03; this deliverable only consumes it through the pending roadmap seam |
| CAP-ELECTRON-027 (product instructions store) | settings/instructions deliverable; the organisation-layer pins are DEL-07-01 |
| CAP-INSTRUCTIONS-002 (product instructions store) | settings/instructions deliverable; the organisation-layer pins are DEL-07-01 |
| CAP-BUILD-006, CAP-BUILD-007 (instruction-root packaging and integrity) | DEL-08-01 / DEL-09-04 |
| CAP-HARNESS-031 (legacy SDK prompt wiring) | DEL-04-01 / DEL-04-02 |
| CAP-RTCORE-028 (Codex supervisor lifecycle and instruction adoption) | engine adapter (DEL-04-01 / DEL-04-03 area) |
| CAP-INSTRUCTIONS-014 (instruction adoption at a safe boundary) | engine adapter (DEL-04-01 / DEL-04-03 area) |
| CAP-RTCORE-037 (method selection) | workflow/method slice |

## Capability-file accuracy

- **CAP-RTCORE-038 is accurate.** It correctly records that project `AGENTS.md` is left to
  native discovery.
- **CAP-HARNESS-060 is accurate.** It correctly flags `runtime-fingerprint.ts` as TEST_ONLY,
  whereas the pack says LEGACY_ONLY. I did not cite that module.
- **No REACH/STATE tag I checked is contradicted by code.** I checked: product-native-role-config,
  delegated-engine-adapter, codex-supervisor, turn-coordinator, app-owned-composition,
  persona-resolution, persona-manager and governed-workflow.

## Effort

- I read the capability rows for all 8 areas, in full for about 18 relevant rows.
- I re-read these frozen-tree lines: `app-owned-composition.ts:210-228`,
  `runtime-method-service.ts:561-570`, `delegated-engine-adapter.ts:39`,
  `turn-coordinator.ts:161`, `delegated-runtime.ts:286-292` and `codex-supervisor.ts:104-112`.
- The context budget was adequate.
