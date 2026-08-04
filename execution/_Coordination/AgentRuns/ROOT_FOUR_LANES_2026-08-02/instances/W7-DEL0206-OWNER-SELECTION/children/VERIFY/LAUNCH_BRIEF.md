# W7 sealed child launch - fresh read-only decision-support verifier

- RequestedBy: `WORKING_ITEMS/W7-DEL0206-OWNER-SELECTION`.
- Node: `W7-VERIFY`; depends on manager-accepted `W7-AUTHOR` attempt 2.
- Parent runtime identity: `/root/w1_del0206`.
- Expected child form: genuinely fresh ephemeral Agent 2 generalist; delegation forbidden.
- Package/deliverable: `PKG-02` / `DEL-02-06` only.
- Governing W7 manager launch: SHA-256 `307598058d168361afa4b8ff3d8dd7273d502d631bab35768bdf301b7e635a13`.
- Governing plan/graph: `ORCHESTRATION_PLAN_V20.md` `6b8f471bccf1f4d1d7fcf50dd731176755b729dc3fe795ae5edd5d0ca11b6b0c`; `WORK_GRAPH_V20.json` `0c98f27efee591ebd3faa04f4883e1ca4c2cce23a7d7088716130243f78d5b4b`.
- Original author launch: SHA-256 `cc29413761180676154d702b58d6c92b04dbab4b7f008922689fd86dae092f9a`.
- Clean retry launch: SHA-256 `8c31a6db290be98052d834952cb50c02ec6134ff1ca9f5232da0629b65a21aab`.
- Clean retry manager status: SHA-256 `9fbee3ae3f4e919d5d08e34d9e5755fd5d4c5958f85b30f293c34484ea8a0378`.

## Objective

Independently attempt to refute the frozen attempt-2 owner-selection package.
Verify evidence grounding, row and option completeness, deterministic future
patch mapping, exact response grammar, and every authority/no-effect boundary.
This is a read-only semantic and static review. Do not repair, supplement,
reinterpret into adoption, or edit any candidate byte.

## Exact declared reads - 42/42

Read this launch in full at the manager-supplied post-closure SHA-256. Then
read in full and reproduce the hashes of the exact 34 accepted basis files
enumerated as items 1-34 in `children/AUTHOR/LAUNCH_BRIEF.md`, including the
W7 manager launch, V20 plan/graph, Scope of Work, accepted packet, N0-N6,
W6, and W6-R1 inputs. Read these additional seven exact files:

1. `children/AUTHOR/LAUNCH_BRIEF.md` `cc29413761180676154d702b58d6c92b04dbab4b7f008922689fd86dae092f9a`.
2. `children/AUTHOR/attempt-2/LAUNCH_BRIEF.md` `8c31a6db290be98052d834952cb50c02ec6134ff1ca9f5232da0629b65a21aab`.
3. `children/AUTHOR/attempt-2/OWNER_SELECTION_SLATE.md` `b8d7d7cbfd92a15ca4144967ce7aaf3ec5683aef7a91ae9ff872e7ad57a8f03d`.
4. `children/AUTHOR/attempt-2/OWNER_SELECTION_MATRIX.csv` `d13efba666bdf64c8b4687bfae49bcc474c07d845d2f698698873c7a37d3998b`.
5. `children/AUTHOR/attempt-2/SEMANTIC_PATCH_PLAN.md` `eefde51dce7a2e1a384a60ed152ff315365974d32cae64fdf1bf67cdf52849a1`.
6. `children/AUTHOR/attempt-2/AUTHOR_RETURN.md` `7beff43c1db6f92b6eff85b889f4dd11f4bcf59cafcd397f7f111c6b655d8769`.
7. `children/AUTHOR/attempt-2/STATUS.json` `9fbee3ae3f4e919d5d08e34d9e5755fd5d4c5958f85b30f293c34484ea8a0378`.

The 34-file basis list plus these seven files plus this launch totals 42/42.
Run-base paths resolve exactly as stated in the original author launch. W6
and W7 control paths resolve under
`execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/instances/`.
Do not discover or read any directory, attempt-1 semantic output, attempt-1
return/status, Git state, coordination register, or other file.

## Required refutation checks

1. Reproduce all 42 declared hashes and confirm the frozen author candidate
   is exactly its three semantic files plus terminal return/status; the
   rejected attempt 1 is not evidence.
2. Parse the CSV and verify its exact eleven-column header, exact ordered 27
   unique rows (`D1-D9`, `TBD-001..TBD-016`, `CENSUS`, `COMPAT-DELTA`), two
   stable unique named options per row, and one recommendation that names an
   exact listed option while explicitly saying non-authoritative decision
   support.
3. Check all 27 rationales against cited accepted evidence. Every evidence
   reference/hash pair must align, reproduce, and support the concern,
   options, recommendation, dependencies, and stated effect without claiming
   more than the source establishes. Record any unsupported or materially
   misleading recommendation as a material finding.
4. Verify the slate covers all D1-D9 families with recommendation,
   alternative, and consequences; summarizes all sixteen stable TBDs; gives
   exact placeholder-only response grammar for all 27 rows; contains no
   completed owner token; and explicitly makes silence non-acceptance.
5. Verify the patch plan maps all 54 option identifiers exactly once to
   deterministic future versioned-candidate paths, headings/placeholders,
   dependencies, validation/refutation reruns, and no-effect fences. No plan
   entry may direct a current accepted, candidate, integration, or handoff edit.
6. Verify the N2 census recommendation preserves the exact evidence-bounded
   affected-client census, and the compatibility-delta recommendation is
   conditional on future owner adoption of the recovery specification rather
   than a present policy change.
7. Verify foreign ownership throughout: App writes/conformance remain
   App-owned; PEC remains `UNRESOLVED` and Root can only retain/route it;
   Tier-0 relationship acts remain Tier-0-owned; Piping receives no work;
   silence, this review, and manager integration have no selection effect.
8. Verify derivative-package labeling and the full no-effect boundary: no
   semantic adoption, current authoritative/candidate edit, implementation,
   runtime/client/project/profile/check change, executable test, dependency
   act, SCA/decomposition/PRD or Task Management act, lifecycle/release/
   publication/issuance/reliance, Git, PR, merge, notice, or foreign-loop effect.
9. Check strict text/CSV shape: UTF-8-compatible text, LF endings, one terminal
   LF, no CRLF, no surplus terminal blank line, and valid eleven-field CSV rows.

Classify each finding as `MATERIAL`, `MINOR`, or `OBSERVATION`, with exact file,
row/section, claim, accepted evidence reference/hash, and required disposition.
Any material finding, missing declared byte, hash mismatch, ambiguous authority,
unsupported recommendation, incomplete row/map, forbidden current edit, or
tool/write-boundary failure requires terminal `RETURN_TO_MANAGER`. Minor issues
also return unless they are purely non-semantic observations that do not impair
selection, provenance, reproducibility, or boundaries. `ADMIT` is permitted only
with zero material and zero minor findings.

## Tools, exact write, and hard stops

- Tools: bounded non-shell file reads, SHA-256, UTF-8/CSV parsing, and
  `apply_patch` for the exact return only.
- Write exactly one regular non-symlink file in this `children/VERIFY/`
  directory: `VERIFIER_RETURN.md`. The manager alone writes `STATUS.json`.
- `VERIFIER_RETURN.md` must report runtime identity, 42/42 hash coverage,
  exact candidate identities, 27/27 rows, 54/54 mappings, per-check result,
  complete findings table (or explicit none), derivative/no-effect posture,
  tool/write containment, and one terminal verdict: `ADMIT` or
  `RETURN_TO_MANAGER`.
- No repair or edit to author, decision-support, accepted, candidate,
  integration, handoff, source, runtime/client/project, profile/check,
  decomposition/PRD/SCA, Task Management, lifecycle/release/reliance, or
  foreign-loop bytes.
- No shell or shell-backed command, network, executable/runtime/software
  check, delegation, Git, stage, commit, PR, merge, or notice.
