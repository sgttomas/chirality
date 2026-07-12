# Guidance: DEL-09-01 Section 8 Harness Validation Preservation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

DEL-09-01 exists to preserve the existing harness validation baseline while vNext runtime work proceeds. The deliverable should make it difficult for future changes to accidentally remove Section 8 coverage, rename the stable premerge artifact, reintroduce a retired legacy test ID, or let CI pass without the expected summary JSON.

## Principles

- Treat Section 8 as baseline preservation. New runtime behavior belongs in Section 9 validation unless the accepted sources explicitly amend Section 8.
- Keep the premerge wrapper strict about summary shape and required IDs. This is the current enforcement point for `docs/PRD.md` FR-066 and `docs/CONTRACT.md` K-VALIDATE-1.
- Preserve stable artifact location. CI and local workflows rely on `frontend/artifacts/harness/section8/latest/summary.json`.
- Prefer deterministic validation scripts over manual inspection wherever possible. This follows `docs/DIRECTIVE.md` deterministic validation guidance and the existing frontend scripts.
- Keep PRD hash status: MATCH visible but non-blocking for this run, per invoker instruction. (reconciled under D-APP-38).
- Do not treat a passing historical provenance summary as proof that current code still passes. It is useful evidence of the expected summary shape and ID set, not a substitute for rerunning validation.
- Keep DEL-09-01 limited to preserving Section 8 baseline behavior. Section 9 runtime validation IDs, broader runtime additions, and release workflow expansion belong to DEL-09-02 and related PKG-09 deliverables unless accepted sources move that scope here.

## Considerations

- The Section 8 script writes temporary run output under the platform temp directory and can stage the example project root when the requested project root is inside the instruction root. Preservation tests should account for that behavior rather than assuming a fixed absolute workroot.
- The premerge wrapper uses machine-readable stdout from the Section 8 script. Changes to `HARNESS_VALIDATION_SUMMARY_PATH` or `HARNESS_VALIDATION_STATUS` output would affect premerge behavior.
- The CI workflow starts the Next.js server, polls `/api/harness/session/list?projectRoot=/tmp`, runs the wrapper from `frontend/`, verifies the stable summary path, and uploads the artifact. A preservation change should cover this chain, not just the Node scripts.
- The current stable summary records eight passing rows. If future accepted Section 8 scope changes the row set, update `REQUIRED_TEST_IDS`, `REQUIRED_CHECK_ORDER`, SPEC/PRD text, and CI expectations together.
- ASSUMPTION: Unit tests or fixture tests for the wrapper may be preferable to relying solely on end-to-end CI runs, because they can exercise missing-ID and legacy-ID rejection deterministically. This is an implementation approach, not an accepted source requirement.
- Current acceptance should cite fresh command outcomes. Historical provenance summaries are suitable shape references, while release-significant acceptance needs current evidence for the local checks named by `docs/SPEC.md` Section 19.1 and `docs/CONTRACT.md` K-VALIDATE-1.

## Trade-offs

| Topic | Option | Trade-off |
|---|---|---|
| Required ID enforcement | Hard-code accepted Section 8 IDs in the wrapper | Strong regression protection, but source documents and script constants must be updated together if Section 8 scope changes. |
| Stable artifact path | Preserve `frontend/artifacts/harness/section8/latest/summary.json` | Supports CI upload and downstream tooling; requires care to avoid stale artifact confusion. |
| Historical summary evidence | Use provenance summary as shape evidence only | Avoids overstating stale evidence; requires reruns for current acceptance. |
| Section 9 additions | Keep out of DEL-09-01 except compatibility awareness | Keeps this deliverable focused; future runtime validation must be handled by DEL-09-02 and related packages. |

## Examples

- Supported preservation check: assert that `validate-harness-premerge.mjs` fails when a required Section 8 ID is absent from a summary fixture.
- Supported preservation check: assert that `validate-harness-premerge.mjs` fails if `regression.api_chat_reachability` appears in the summary.
- Supported preservation check: run `npm run harness:validate:premerge` and verify `frontend/artifacts/harness/section8/latest/summary.json` is readable.
- Not supported without amendment: broadening this deliverable into new Section 9 validation implementation.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; invoker instruction | N/A | Datasheet Conditions; Specification Requirements; run record | Treat PRD as accessible with warning for this run. | TBD — reconciled under D-APP-38 |

## Source Warnings

- `docs/PRD.md` expected SHA256 in `_REFERENCES.md` is `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`; observed SHA256 is `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`. The invoker instructed this run to treat the MATCH as a source status. (reconciled under D-APP-38).
