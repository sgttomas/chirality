# Workflow author return

RUN_STATUS: SUCCESS (bounded implementation; acceptance remains with parent)
ControlSurface: MERGED — LAUNCH_BRIEF.md plus AMENDMENT_01.md and parent focused-test authorization.
TaskProfile: NONE
TaskSkill: software-bounded-implementation
ToolPolicyCompliance: PASS
WriteAuthorization: ALLOWED_WRITE_TARGETS
ResolvedSkillVersion: 1
ResolvedTaskProfileRequirement: NONE
CompanionFiles: BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)
AllowedTools: repository-native reads/edits/local exec; declared software-workflow validator; exact parent-authorized focused Vitest command.
RuntimeOverrides: manager binds CHIRALITY_INSTRUCTION_ROOT=REPO_ROOT for native TASK hydration; no product environment change.

## Outputs / AppliedChanges
- frontend/src/lib/workspace/governed-workflow.ts — new pure typed parser, runtime validator, canonical serializer, gate advance, bind, source currency and lexical folder helpers.
- frontend/src/__tests__/lib/governed-workflow.test.ts — 59 passing fixtures.
- Own record subtree: source identities, test evidence, scope validation, return and TASK record.

## Acceptance mapping and downstream API
- OUT-001 / AC-001 / VER-001: all seven required front matter keys; nested roadmapSource identity/sha256; strict consecutive numbered roadmap with optional leading [gate]; initial position 1 and attribution null; stored advanced position must follow a human gate. Unknown/missing fields rejected by both parser and runtime serializer validation, including nested source and roadmap objects. Status/approval/evidence fields have no storage slot.
- parseGovernedWorkflow(content, vocabulary), serializeGovernedWorkflow(workflow, vocabulary), validateGovernedWorkflow(value, vocabulary): vocabulary is REQUIRED and comes from caller's live Agent 1 role and permission/delegation/destination registries. No production enum or provider activation is invented here; test tokens are fixtures only.
- Grammar deliberately is not general YAML: front matter strings are plain restricted or JSON quoted; roadmapSource has two indented scalar keys. Scalar quoting in canonical serialization permits Unicode/punctuation to round trip without comments, aliases, duplicate keys or implicit conversions. acceptedAt is exact UTC ISO milliseconds and survives Bind as source acceptance metadata, never an approval record.
- nextWorkflowGate returns the first gate at or beyond current. advanceWorkflowAtGate accepts only that gate and a nonempty human identity, advancing to gate+1. This permits completing the ordinary work segment before its human decision while refusing ordinary-step progress writes, gate skipping and rewind. The last gate permits current=roadmap.length+1. A roadmap with no remaining gate cannot advance stored position.
- bindWorkflowContent rewrites folder, resets current/advancedBy, retains roadmapSource/hash/acceptedAt, and returns content only. No file IO or automatic approval.
- workflowSourceCurrency compares caller-computed hashes and identity, returning current/changed/unavailable without mutation. Case-insensitive digest comparison preserves original stored digest spelling.
- isCanonicalWorkflowFolder checks lexical absolute POSIX paths only. No slug/file-write helper is exposed; downstream must resolve canonical roots/symlinks and enforce write containment.

## Tests and checks
Authorized focused command: `node node_modules/vitest/vitest.mjs run src/__tests__/lib/governed-workflow.test.ts` from frontend. PASS 59/59; Node v24.18.0 and Vitest v4.1.10. See FOCUSED_TEST.txt.
Explicit-path validate_change_scope.py PASS; shared unrelated edits excluded by declared author path inventory. See SCOPE_VALIDATION.json.
Global frontend-test/typecheck/build/premerge and harness checks NOT RUN by author; parent owns them serially after fresh review.

## Accepted basis and handoff
Accepted upstream: SCA-APP-010 decomposition dbd812a52d5ed0cb3ed173f3aaaa68703a914291; D-APP-108 Q16; target spec §5.10 hash d1643e3cf8156b7084b370aa8624bd5e87a75bfb4c0cd7b3a2552a4cbef82b45; accepted closure CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034 PASS with carried warnings. Exact input/postimage hashes in SOURCE_IDENTITIES.json. Parent dispatch PREFLIGHT.json ALLOW preserved; own reliance check ALLOW persisted.
Derivative-package status: implementation and evidence are derivative, not decomposition truth. Closure verdict: AUTHOR COMPLETE, REVIEW AND PARENT VALIDATION PENDING. No lifecycle promotion or acceptance.

## Risks / Missing / Dependency Notes
Concurrent editing unsupported, documented in module: caller must check exact current content before applying a human-accepted transformation. Human identity authentication, acceptance evidence, prerequisite checking, canonical filesystem resolution, write gate and persistence all remain caller responsibilities and are intentionally absent from this pure contract. Vocabulary correctness is caller-owned, not mechanically inferred from AGENTS.md. Strict grammar choices are explicit local implementation details; no existing workflow files migrated. A1 frontend restage/fresh owner proof remains parent-owned. Fresh independent review and parent checks required before closure. No other blockers and no human ruling requested.
