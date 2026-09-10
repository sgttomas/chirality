# Independent integration custody review V1

Verdict: HOLD for exact current-postimage attribution. This is a read-only source/manifest audit, not a repeat semantic review or test qualification.

Reviewer: `/root/integration_custody_review`, TASK, delegated-harness-native. Parent `/root`; integration manager `/root/root_adoption`. Scope and permissions were the parent's sealed task brief: inspect the named lane subjects and final integration manifest; write evidence only here; no delegation, product edits, staging, Git mutations, network, supplier, credential, or native actions.

Compared base `c16812685831a1cae3d44bf478d08b033c605c3a` in `/private/tmp/chirality-v3-adoption-20260909`. Active instruction origins/hashes are in UNION_CHECK.json. Historical subjects were retained as historical: later overlays replace hashes only for explicitly listed paths, preserving predecessor-only implementation.

## Verified

- Independently reconstructed 294 unique lane-subject paths, including unchanged context and in-run metadata. Latest Runtime V5 binds 44 members plus two shared Root fixtures; App V7 binds 48; distribution V10 binds 19.
- Independently enumerated 267 changed files outside AgentRuns. STAGING_MANIFEST_V1.json includes all 267 exactly once; zero missing changed product files and zero duplicate source rows.
- All 267 source rows, 59 evidence rows, and nine subject-file hashes physically match current files. Source/evidence sets do not overlap.
- Current npm package-lock is explicitly owned; unrelated pnpm locks are absent. Exclusion policy preserves duplicate source captures, fixtures, and generated outputs on disk.
- Governed acceptance, future integrated commit binding, merge, publication, release, native adapter and supplier qualification remain separate. Original distribution V10 pending-review prose describes its creation time and must not be rewritten as if reviews were then complete.

## Open findings

1. Two App backend test files have changed postimages absent from effective reviewed freezes: `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` and `frontend/src/__tests__/lib/harness-anthropic-agent-sdk-manager.test.ts`. V1 binds current bytes to APP_SUBJECT.sha256, but that subject records different historical hashes. The exact expected and actual hashes are in UNION_CHECK.json. Parent has routed a bounded supplemental review.
2. App `AGENTS.md` and `execution/_Coordination/_COORDINATION.md` are assigned to CORPUS_V21_FREEZE_v2.md in V1 although that freeze and its exact independent review inventory contain only five core artifacts plus 52 deliverable references. Bind their actual instruction/coordination review or an explicit current documentary supplement; do not imply the corpus freeze contains them.
3. Terminal documentary evidence selection should include the Runtime source manifest and compact final probe source/configuration/results needed to inspect or reproduce its findings. V1 selects the Runtime evidence manifest while excluding all those members. Retaining intermediate/duplicate captures locally is appropriate, but terminal reproducibility evidence and historical-only local exclusions need an explicit distinction.

The integration inventory also still describes pending lanes and Runtime V4 as effective; a terminal inventory must state V5 plus its exact engine supplement and current verdicts. No historical record needs in-place rewriting.

## Handoff

Accepted upstream design authorization is the parent-supplied approved Chirality v3 adoption plan. All lane records here remain derivative review evidence, not authoritative decomposition truth or human acceptance. Closure is open only for exact attribution and final evidence selection. No broad tests or semantic lane review were rerun. Rehash and recheck the final successor manifest after the supplements and evidence selection settle; preserve this V1 review as historical.
