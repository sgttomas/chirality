# DEL-09-05 concordance notes (R2 Wave-4)

Deliverable: DEL-09-05 CI Artifact and Release Verification Workflow (PKG-09).
Source state: frontend/ at `fac46e33f`, byte-identical through HEAD `6f7c06814` (this
worktree). Workflow files (repo-root and project-local `.github/`) sit outside frontend/;
inspected at HEAD `6f7c06814` and bound to `fac46e33f` through the passing frontend test
`harness-premerge-workflow.test.ts`, which reads the repo-root YAML.

## Census (post fan-in revision 2026-07-12)

Total rows: 23 (15 REQUIREMENT, 5 EXCLUSION, 1 ACCEPTANCE, 1 REMAINING_WORK, 0
IMPLEMENTED_UNMAPPED, 1 REGISTER_DEFECT).

Disposition counts:
- ALIGNED 14 (REQ-001, REQ-002, REQ-005, REQ-007, REQ-008, REQ-009, REQ-010,
  REQ-011, EXC-001, EXC-002, EXC-003, EXC-004, EXC-005, REMAINING-1)
- IMPLEMENTED_DIFFERENTLY 1 (REQ-004)
- PARTIALLY_IMPLEMENTED 3 (REQ-003, REQ-006, REQ-015)
- DOCUMENTED_UNIMPLEMENTED 2 (REQ-013, REQ-014)
- STALE_SPECIFICATION 2 (REQ-012, ACC-001)
- REMAINING_STATE_MISMATCH 1 (REGISTER-1)

AssessmentEvidence: OVERTAKEN 8, STILL CURRENT 13, NOT APPLICABLE 2 (REMAINING-1,
REGISTER-1).

## Fan-in re-verification record (2026-07-12)

Three verifier items were independently re-verified; edits confined to my two files. The
verifier's verdicts were treated as agent judgments, not rulings.

1. **REQ-003 — ACCEPTED (ALIGNED -> PARTIALLY_IMPLEMENTED; token OVERTAKEN -> STILL
   CURRENT).** Re-verified: `frontend/dist/` and `frontend/artifacts/` do not exist at
   `6f7c06814` and are gitignored (frontend/.gitignore lines 4-15); Spec line 29 is a MUST
   on the outputs themselves; sibling DEL-09-04 records the identical packaging-output
   surface (its REQ-003/004/005) as PARTIALLY_IMPLEMENTED / STILL CURRENT. Plan §6 denies
   PASS-equivalence without verification evidence — config-verified with artifacts absent
   is exactly a bounded portion. The INSP-03 FAIL's artifact-absence state persists
   unchanged, so STILL CURRENT is the truthful token; my original OVERTAKEN conflated "not
   a config defect" (true) with "assessment conclusion overtaken" (false).
2. **REQ-008 — STANDS CONTESTED (remains ALIGNED, MEDIUM).** Re-verified both sources:
   docs/CONTRACT.md K-VALIDATE-1 (line 128) lists `desktop:dist` in its Enforcement
   column, while docs/SPEC.md Section 19.1 structurally separates the four required checks
   from a distinct "Packaging:" block and RELEASE_QUALITY_RUNBOOK §6 keeps packaging
   evidence separate; the deliverable's own Spec mirrors that split (REQ-09-05-001 names
   four commands, REQ-09-05-002 is a separate packaging requirement). I read
   K-VALIDATE-1's Enforcement column as naming the invariant's enforcement surfaces, with
   SPEC 19.1 defining which checks bind which change class — code-change acceptance is
   enforced by the premerge CI + wrapper; packaging binds packaging-significant changes.
   Reading B (all five commands bind every release-significant acceptance ->
   PARTIALLY_IMPLEMENTED) is defensible; the deciding normative-interpretation question is
   recorded on the row's RemainingWork and routed to R3 per the verifier's recommendation.
3. **Notes factual error — ACCEPTED (notes corrected; REGISTER-1 added).** Re-verified:
   `_DEPENDENCIES.md` line 69 carries an unannotated `[WARNING] PRD_HASH_MISMATCH`
   run-note presenting REF-006 as an open mismatch, lagging the live `_REFERENCES.md`
   MATCH state. My original claim that the staleness lives only in the four-document kit
   was factually wrong. DEL-09-02 and DEL-09-04 ledgered the same class as REGISTER-1 /
   REMAINING_STATE_MISMATCH; I added the matching REGISTER-1 row (harmonization at R3).
   The register-defect summary below is corrected accordingly.

## Cross-deliverable CI-ownership handle (recorded from my side)

The DEL-09-01 sibling agent recorded that the kit-described project-local workflow
`projects/chirality-app-dev/.github/workflows/harness-premerge.yml` is NOT an executed
GitHub Actions workflow (Actions runs only repo-root `.github/workflows`) and assigned live
CI ownership to DEL-09-05 (decomposition line 364; SOW-035/036/072 map DEL-09-05 in;
DEL-09-01 notes finding 1). **My ledger addresses the LIVE repo-root
`.github/workflows/harness-premerge.yml` as DEL-09-05's CI surface.** Concordance of that
executed workflow against the DEL-09-05 kit:
- REQ-09-05-004 (ten-step CI baseline): IMPLEMENTED_DIFFERENTLY. The executed repo-root
  workflow (ORN-01 reshape) runs the substance and MORE (typecheck + full Vitest +
  instruction-root:integrity + `validate:release-quality` which invokes the premerge
  wrapper indirectly + verifies three summaries + uploads `harness-validation-summaries`).
  The kit's literal step list (Spec REQ-09-05-004, Datasheet CI baseline) matches only the
  non-executed project-local duplicate.
- REQ-09-05-005 (Section 8 summary verify/upload; instruction-root separate;
  release-quality wrapper summary): ALIGNED. The executed workflow verifies all three
  summaries `status==pass` and uploads all three (harness-premerge.yml lines 127-142),
  matching the ADQ-14-reshaped requirement exactly.
- REQ-09-05-012 (workflow path "TBD"): STALE_SPECIFICATION. The path is concrete
  (repo-root harness-premerge.yml); the kit's TBD wording is overtaken.
I mirror the sibling's decision attribution: REQ-004/REQ-008/REQ-012 cite `D-APP-53
(context)` (the ORN/inspection-orphan queue whose closeout reshaped the workflow); no
governing ruling reassigns the surface, and the decomposition assignment to DEL-09-05 is
unambiguous, so no AUTHORITY_CONFLICT arises between DEL-09-01 REQ-007 and DEL-09-05
REQ-09-05-004.

## Least-confident rows (self-flagged; alternative reading that would flip them)

- **REQ-004 (IMPLEMENTED_DIFFERENTLY, MEDIUM).** Alternative -> **STALE_SPECIFICATION**:
  if one treats REQ-09-05-004's substance (CI validates a release-significant change and
  uploads the stable summary) as fully satisfied and only the kit's step wording/citation as
  wrong, this is a pure documentation-staleness repair. I chose IMPLEMENTED_DIFFERENTLY
  because the executed mechanism differs materially (indirect premerge via
  `validate:release-quality`, added typecheck+Vitest+instruction-root gates, different
  upload bundle) and the kit describes the non-executed project-local workflow. Mirrors the
  DEL-09-01 REQ-007 call.
- **REQ-003 (PARTIALLY_IMPLEMENTED, HIGH — revised at fan-in; see re-verification record).**
  Originally ALIGNED (config-verified reading); refuted at fan-in and accepted: the MUST on
  outputs is only partially supported when none of the three outputs exists at the source
  state. Residual alternative -> **DOCUMENTED_UNIMPLEMENTED** if the electron-builder config
  and policy test are given no partial credit at all; PARTIALLY_IMPLEMENTED matches the
  sibling DEL-09-04 treatment of the same surface. No build was run (discovery is read-only).
- **REQ-006 (PARTIALLY_IMPLEMENTED, MEDIUM).** Alternative -> **DOCUMENTED_UNIMPLEMENTED**:
  no manual DMG checklist/run-record artifact exists at all. I chose PARTIALLY_IMPLEMENTED
  because most checklist items ARE covered by automated policy tests (dmg-packaging-policy,
  build-network-policy, verify-packaged-agent-sdk-runtime); the missing piece is the
  consolidated manual checklist artifact with per-item pass/fail/TBD rows. If the deliverable
  output "manual release verification checklist" is treated as wholly absent, flip to
  DOCUMENTED_UNIMPLEMENTED.
- **REQ-008 (ALIGNED, MEDIUM).** Alternative -> **PARTIALLY_IMPLEMENTED**: the premerge CI
  gate does not include `desktop:dist` packaging. I read packaging as intentionally separate
  (RELEASE_QUALITY_RUNBOOK Section 6) and the required LOCAL checks for release-significant
  code changes as enforced by the premerge CI + wrapper, so ALIGNED. If K-VALIDATE-1 is read
  to require packaging in the same gate, flip to PARTIALLY_IMPLEMENTED.
- **REQ-009 / REQ-010 (ALIGNED, MEDIUM).** Alternative -> **PARTIALLY_IMPLEMENTED**: the
  key-absence and network-scope guarantees are enforced by the executed workflow (provider
  stub, no secret) and by proof scripts/tests, but no secret/network inspection RECORD tied
  to an actual CI log or release run exists (REQ-015 captures that residual separately). If
  the requirement is read to demand a live-run inspection artifact rather than design +
  automated proof, flip to PARTIALLY_IMPLEMENTED.
- **EXC-005 (ALIGNED, MEDIUM).** Alternative -> a **cross-deliverable finding for R3**: the
  repo-root `desktop-release-template.yml` build-windows job (lines 113-152) DOES build
  Windows NSIS artifacts, which touches K-RELEASE-1's macOS-only posture. I kept EXC-005
  ALIGNED because DEL-09-05's own surfaces produce no Windows/Linux packaging and the release
  template is DEL-09-04/packaging territory; I route the Windows-build-vs-K-RELEASE-1
  observation to R3/DEL-09-04 rather than judging it on DEL-09-05's ledger (write-scope and
  ownership discipline).

## "No test exists" / test-presence search (performed)

Grep of `frontend/src/**` test trees (VERIFICATION_INDEX has no DEL-09-05 rows — see method
notes) returned real coverage, so no false-absence claim was made:
- `harness-premerge-workflow.test.ts` asserts the executed repo-root workflow YAML
  (typecheck, test, instruction-root:integrity, validate:release-quality, three summary
  paths, absence of `secrets.ANTHROPIC_API_KEY`, provider stub) — binds REQ-004/005/008/009/012.
- `dmg-packaging-policy.test.ts` asserts unsigned forcing, macOS min>=15, arm64 dmg target,
  instruction-root bundling, SDK unpacked outside app.asar — binds REQ-002/006/007.
- `build-network-policy.test.ts` asserts the renderer egress allowlist
  (api.anthropic.com/localhost/127.0.0.1), loopback/allowlisted-only proof mode, redacted
  secret-scan proof command — binds REQ-009/010.
- `run-live-packaged-agent-sdk-read-tool-proof.test.ts` / `verify-packaged-agent-sdk-runtime.test.ts`
  — packaged-SDK key-absence and startup (REQ-006/009).
True gaps confirmed (not asserted falsely): no completed manual DMG checklist artifact
(REQ-006), no product-owned release-evidence manifest (REQ-013), no standalone CI ten-step
review table (REQ-014), no CI-log/release-record secret/network inspection record (REQ-015).

## Register-defect summary (corrected at fan-in)

One REGISTER row emitted. Cross-referenced the three registers against the live tree:
- **REGISTER-1 (REMAINING_STATE_MISMATCH):** `_DEPENDENCIES.md` Run Notes (line 69) still
  present REF-006 `docs/PRD.md` as an open `[WARNING] PRD_HASH_MISMATCH` without a
  superseding annotation, lagging the live `_REFERENCES.md` register which records REF-006
  MATCH (ac35fba40..., reproduced by live hash recomputation) after D-APP-35/D-APP-38.
  Same class as DEL-09-02 REGISTER-1 and DEL-09-04 REGISTER-1; harmonization at R3.
- `Dependencies.csv` (14 rows) — all `SatisfactionStatus=TBD`; this is the disclosed
  open-closure state (INSP-03 Dependency Closure Note; DepClosure baseline), not an
  inconsistency. DEP-09-05-011 ("CI provider and workflow path", TargetLocation TBD) is now
  resolvable to repo-root `.github/workflows/harness-premerge.yml`, but a bare TBD extracted
  row that is now resolvable is treated as open-closure (consistent with the DEL-09-01
  sibling not flagging its TBD dep rows), not metadata lag. No dep row carries a concrete
  wrong artifact/workflow citation (unlike DEL-09-01 DEP-09-01-010), because the DEL-09-05
  kit keeps the workflow path/upload-artifact name deliberately TBD.
- `_DEPENDENCIES.md` Declared Upstream/Downstream are bare TBD by design (docs/SPEC.md §5.2
  human-owned sections) — no REGISTER_DEFECT per the Wave-4 rule.
- `_REFERENCES.md` is internally consistent (REF-006 now MATCH). The kit-document PRD-hash
  staleness (Datasheet/Guidance/Spec/Procedure) is modeled as ACC-001 STALE_SPECIFICATION
  (same pattern as R0 exemplar DEL-02-01 ACC-001 and DEL-09-01 REQ-010); the register-side
  lag is REGISTER-1 above.

## Method notes / deviations

- No test suites executed, no dependencies installed, no mutating git, no secret/key VALUES
  copied (the executed repo-root workflow deliberately omits `secrets.ANTHROPIC_API_KEY`; the
  non-executing project-local duplicate references the secret NAME only, described without
  reproducing any value).
- **Parser gap (recorded per brief):** `REQUIREMENT_INDEX.csv` line 543 captured only
  `DEL-09-05,REQ-09` (truncated) and `VERIFICATION_INDEX.csv` / `IMPLEMENTATION_SURFACES.csv`
  have ZERO DEL-09-05 rows. I re-derived the full claim set (REQ-09-05-001..015 + 5
  exclusions + the ACC/REMAINING rows) directly from `Specification.md`.
- Behavioral verification cites `GATE-TRANSCRIPT(W1@fac46e33f)` + the named test file with
  line anchors. Workflow-YAML content (outside frontend/) cites `RUN-INSPECTION@6f7c06814`
  anchored to `fac46e33f` via the passing `harness-premerge-workflow.test.ts`. Non-behavioral
  rows use the MR-10 vocabulary (`DOC-BASIS(D-APP-38)`, `RULING-RECORD(D-APP-35/38)`).
- MR-7: REQ-004/008/012 cite `D-APP-53 (context)`; ACC-001 cites `D-APP-35; D-APP-38`
  (governing the PRD-hash refresh); all other rows `NONE_FOUND`. ADQ-14 is implementation
  evidence (an assessment-driven tranche), not a D-APP ruling, so it appears in
  NormativeSource/ImplementationEvidence, never in LatestDecision.
- MR-9: REQ-005's Specification was rewritten by ADQ-14 after INSP-03 (2026-06-21); its
  AssessmentEvidence names the old-REQ005 mapping and marks OVERTAKEN.
- EXC-004 distinction from the R0 exemplar: DEL-02-01 EXC-004 was STALE_SPECIFICATION because
  its kit flatly claimed "Dependencies.csv not produced." DEL-09-05's exclusion is
  run-scoped ("Direct creation of Dependencies.csv in this run") and remains accurate, so it
  is ALIGNED — the extracted register was produced by a separate dependency-extract run.
- No IMPLEMENTED_UNMAPPED row: the executed workflow's added gates map to REQ-001/008
  substance; the three-summary verify/upload maps to REQ-005; the instruction-root fixture
  prep maps to REQ-004 — no material live behavior on DEL-09-05's surface lacks a mapping.
- No AUTHORITY_CONFLICT, DEFERRED_AGENT_WORKFLOW, or UNKNOWN rows arose. The repo-root
  `governance-harness.yml` workflow is root-governance/cross-project scope
  (FROZEN_PROCESS_INPUT), not DEL-09-05's CI surface; noted, not judged.
