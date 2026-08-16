# WORKING_ITEMS manager return

- RunID / InstanceID: `APPDEV_PACKAGED_ADAPTER_LOADING_2026-08-16` /
  `WI-PKG04-DEL0401`
- Package / deliverable: PKG-04 / DEL-04-01
- Verdict: `CHANGE_READY_WITH_PR_CI_ADVISORY`.

## Product fan-in

The App daemon composition now registers Root `engine-claude` and
`engine-pi-omlx` factories around the existing App turn runtimes. Prior
capability, credential, interrupt, governed-tool, and residency behavior is
preserved. Exact package/provider versions and selected-model attribution are
covered in runtime-host and shared Desktop/CLI daemon tests. Build/package
resolution includes Root engine-claude.

The packaged verifier reads the actual `app.asar` source map. Final unsigned
packaging proves Root client/daemon/Claude/Pi sources in Desktop and a
client-only Root CLI; zero monorepo-only package entries or forbidden
development packages are present.

Exact product/test files are the nine frozen paths in the reviewer brief. Root
`runtime/**` was never edited. DEL-04-01's sole packaged-runtime Remaining item
is removed; lifecycle and Checking Approval SHA remain unchanged.

## Validation and fan-in

- Fresh independent review: PASS, zero actionable findings, all nine frozen
  hashes matched.
- Focused Vitest: 11 pass; full Vitest: 1,124 pass / 4 skip.
- Typecheck and production build: pass.
- Final unsigned `desktop:pack`, packaged Root source/package boundary, and
  instruction-root integrity: pass.
- Practitioner pytest: 349 pass; self-check exit 0 at baseline; APP-HOLD pass;
  corpus v18 eight MATCH/no drift; receipt, whitespace, diff, and containment
  checks pass.
- Local registered premerge ran with its owned Next service. Its eight Section
  8 rows retain the known post-daemon-migration 503 advisory because the local
  profile supplies no socket/token/project binding. Receipts 110–112 assign
  the authoritative rerun to PR CI/live runtime. This is not a waiver and no
  product-pass inference relies on it.
- D-APP-36: not applicable; UI behavior/rendering unchanged.

Reruns: clean file links initially resolved to unbuilt Root packages; the
registered suite was rerun against a compiled read-only `/private/tmp` copy.
The packaged verifier was rerun after its asar-CLI extraction remediation.
Both passed and all transient links, dependencies, copies, and build/package
outputs were removed.

Blockers: none to CHANGE handoff. Waivers: none. Owner decisions: none.
Derivative evidence is bound to base
`65735390590e500dbbea6b63a4a79ba42944bf6d`; no release-readiness claim.
