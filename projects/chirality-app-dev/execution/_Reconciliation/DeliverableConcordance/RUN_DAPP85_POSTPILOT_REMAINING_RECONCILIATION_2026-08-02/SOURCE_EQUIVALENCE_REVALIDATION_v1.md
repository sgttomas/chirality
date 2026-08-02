# Source-Equivalence Revalidation v1

Status: `PASS / EXACT MANIFEST REMAINS SELECTABLE`

Frozen basis: `556ae59a34ac2f06ef924d367843a72ea00d1f37`
Latest-origin basis: `ccd9a2178ffd8029fdd1cd779910e954e0612e21`

The frozen basis is an ancestor of latest origin. The intervening path census
contains 38 files: 14 under `_DomainEngines/**` and 24 under `projects/pec/**`.
There are zero changes under app-dev, root `runtime/**`, the shared method or
agent file, or the standing plan.

Direct Git-object comparison across both trees proves byte identity for:

- all 18 C01-C18 status files and accepted before-block hashes;
- all 30 preservation blocks and their status-file hashes;
- all 53 app-dev lifecycle states and Checking Approval SHA values; normalized
  aggregate SHA-256
  `7c31869d66bc268a41a3dafeeb332b1477e9a8e01a93f5caa4ea84e2527e6d53`;
- `AGENT_RECONCILIATION`, the shared concordance method, standing plan,
  decomposition, dependency pointer, scope pointer, DIRECTIVE, CONTRACT,
  SPEC, TYPES, and PRD; and
- every D-APP-85 repair preimage. No configured worktree has a pending change
  on an enumerated target path.

## C18 external-authority assessment

Latest-origin D-T0-27 is `EFFECTIVE / ADOPTED / READ_ONLY` and expressly
declares no runtime or adapter-client tool or invocation. D-T0-28 changes only
a conscious test pin and creates no runtime effect. PEC `AGENTS.md` repeats
that the profile declares no runtime store, service, transport,
adapter-client, mutation, proposal, external-result, or instance-content lane.
PEC `docs/STATUS.md` and `software-workflow.json` show DEL-01-06 as a local
typed loop-registry/config slice with deterministic registered checks; it
remains `INITIALIZED`. Future DEL-07-05 decomposition scope is not current
runtime-client authority. C18 therefore remains `NO_CHANGE` with its fences
attached.

## Transparent derivative correction

Gate-1 `RUN_BASIS.md` transcribed the decision-register hash incorrectly as
`175d8f4a235c14327069146f27d4a39e27c300654417560bc50573fd58c8b550`.
The live register is byte-identical to the frozen Git object and hashes
`175d8f8e96c5cf9f67ddfe022bac8184deafe330f985bd8f762e0861af2ab550`.
Only the derivative transcription was corrected. `RUN_BASIS.md` changed from
SHA-256 `3a26d5a989d3b2afd7cdb382187f890cefa16ce8800a73344fa438c3d127fdc3`
to `414e0777d4492969892f78363e6b8913eeb109ecf95c4e7e24c361d0d12741e2`.
The live register and accepted manifest did not change.

Fresh sealed Agent-2 verification returned `PASS`: the unchanged manifest may
be applied without a new owner ruling; C18 remains open; and the derivative
hash correction is non-material.
