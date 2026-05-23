# Guidance: DEL-09-05 CI Artifact and Release Verification Workflow

## Purpose

This deliverable gives release operators and implementers a stable validation workflow for CI artifacts and manual release verification. It exists to connect required local checks, Section 8/9 validation surfaces, stable summary artifact handling, and macOS DMG release verification into one reviewable workflow for PKG-09.

Source basis: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` `DEL-09-05`; `docs/PRD.md` Sections 12.2, 12.7, and 12.8; `docs/SPEC.md` Sections 19.1 through 19.4.

## Principles

- Treat the local command sequence as the release-significant baseline: `test`, `typecheck`, `harness:validate:premerge`, `instruction-root:integrity`, and `desktop:dist` are the named commands in the accepted source slices.
- Keep CI evidence stable and reviewable. The stable summary artifact path is `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`.
- Separate CI automation from human release judgment. CI can run checks and upload artifacts, but it does not issue, certify, or professionally approve the work.
- Preserve current release boundaries. The accepted target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended.
- Keep security posture visible during release verification: network scope and key handling are release constraints, not optional implementation details.
- Prefer `TBD` over invented implementation detail when workflow filename, artifact retention, or evidence format is not source-defined.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| PRD source warning | The PRD hash mismatch is not a blocker for this run because the dispatch brief explicitly downgrades it to a source warning. Do not treat the mismatch as resolved. | `_REFERENCES.md`; dispatch brief |
| CI workflow location | ASSUMPTION: Use GitHub Actions because the PRD names a GitHub workflow. Exact file path remains TBD. | `docs/PRD.md` Section 12.7 |
| Stable artifact path | Use the source-defined path exactly when verifying or uploading the instruction-root integrity summary. | `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1 |
| Section 8/9 scope | This deliverable should wire or verify the workflow; sibling deliverables own detailed validation additions and tests. | Decomposition PKG-09 rows |
| Manual verification | The runbook should record pass/fail/TBD per checklist item, not collapse all DMG checks into one overall statement. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |
| Secret handling | Release logs and artifacts should be checked for accidental key material. API keys are non-project convenience state and must not enter project files or tool artifacts. | `docs/CONTRACT.md` K-KEY-1 |
| Network posture | CI and packaged-app verification should not broaden network policy beyond loopback plus Anthropic API path without governed scope change. | `docs/CONTRACT.md` K-NET-1 |

## Trade-offs

| Decision Area | Trade-off | Recommendation |
|---|---|---|
| CI breadth vs runtime ownership | A broad CI job can catch release blockers, but Section 8/9 validation implementation belongs to sibling test deliverables. | Keep this deliverable focused on orchestration, artifact stability, and release checklist coverage. |
| Artifact path stability vs historical retention | `latest/summary.json` gives a stable pointer, but release evidence may need immutable history. | Use the stable path for CI acceptance; add immutable release evidence only if a governing source or human ruling specifies it. |
| Manual checklist vs automated packaging probes | Manual checks preserve release judgment, while automated probes reduce missed packaging issues. | Automate source-defined checks where practical, but keep a manual release verification checklist as required. |
| PRD mismatch handling | Blocking on the mismatch would preserve strict source fidelity, but the dispatch brief gives an explicit ruling for this run. | Proceed with a recorded source warning and avoid treating the mismatch as fixed. |

## Examples

Example local verification command block:

```bash
cd frontend
npm run test
npm run typecheck
npm run harness:validate:premerge
npm run instruction-root:integrity
npm run desktop:dist
```

Example CI acceptance checklist:

| Step | Expected Evidence |
|---|---|
| Checkout and Node setup | CI log shows repository checkout and Node.js 20 setup. |
| Dependency install | CI log shows `npm ci` completed. |
| Instruction-root assets | CI log or validation output confirms required assets are present. |
| Premerge validation | CI log shows `npm run harness:validate:premerge` completed. |
| Stable summary artifact | CI verifies `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json`. |
| Artifact upload | CI uploads the summary artifact. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONFLICT-09-05-001 | PRD hash mismatch exists, but dispatcher instructs this run to treat it as source warning only. | `_REFERENCES.md` REF-006 hash mismatch | Dispatch brief PRD mismatch ruling | All PRD-grounded sections | Proceed for P1/P2 with explicit warning; do not mark mismatch resolved. | TBD |

## Open Items

- TBD: Exact CI workflow path.
- TBD: Stable upload artifact name and retention period.
- TBD: Release verification runbook filename and final evidence storage location.
- TBD: Human assignment for `ResponsibleParty`.
- TBD: Whether immutable release evidence snapshots are required in addition to the stable `latest/summary.json` pointer.
