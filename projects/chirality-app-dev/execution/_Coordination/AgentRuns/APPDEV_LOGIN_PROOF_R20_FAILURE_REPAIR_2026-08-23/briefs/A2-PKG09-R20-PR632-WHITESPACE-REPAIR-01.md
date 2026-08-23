# Sealed brief — PR #632 record-only whitespace repair and validation

- RequestedBy: `WORKING_ITEMS` instance `/root/node3_pkg09` under HELP_HUMAN.
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-REPAIR-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-WHITESPACE-REPAIR-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role and non-delegation are instruction-asserted. Do not delegate.
- PackageID/DeliverableID: `PKG-09` / `DEL-09-04`, record-only integration scope.
- Objective: repair exactly the 12 paths enumerated in `PR632_WHITESPACE_DIAGNOSTIC.md`, freeze lossless lineage, and run the authorized non-product pre-push gates.
- AcceptedBasis: clean branch/tip `codex/app-login-proof-r20-repair` / `85caafd4882a2ffff204ed87334171608ce462be`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`; exact owner authority in `CHAT_TRANSCRIPTION.md` and `AMENDMENT_06_PR632_RECORD_ONLY_WHITESPACE_REPAIR.md`.
- Dependencies: controlling diagnostic exit 1 and 12-path inventory frozen before dispatch.
- DeclaredReads: root/App instructions and standing plan; owner transcription/amendment/v8 plan/graph/diagnostic; the exact 12 preimages; candidate whitespace validator; receipt validator; committed PR/pre-push workflows and non-product validation docs/scripts; accepted instruction-root evidence.
- AllowedTools: read-only shell/git/hash/stat/gzip inspection; deterministic `gzip -n -9`; exact targeted Markdown whitespace normalization; authorized validators/checks. No network, product test, build, package, daemon, GUI, proof, launchd, operator, signing, or release tool.
- AllowedWriteTargets: the exact 12 diagnostic paths (11 raw logs replaced by same-name `.gz`, and only lines 23–25 of the one RETURN); `instances/A2-PKG09-R20-PR632-WHITESPACE-REPAIR-01/`. No other shared or frontend path.
- Repair method: freeze exact preimage byte count/SHA-256; remove only one U+0020 from each RETURN line 23–25; for each raw log create deterministic same-name `.gz` using gzip header normalization (`-n`) and maximum compression (`-9`), verify `gzip -cd` output byte count/SHA-256 equals its raw preimage, then delete only that raw file. Record each raw deletion/addition explicitly.
- Validation: exact `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main` must PASS after repair; receipt validator; `git diff --check`; exact App-only containment and empty index; frontend tree must remain `b4c73edda1fe3346815ce75449b2327c80c79bf8` and `git diff --stat cb008dc5d6aa9b249639c91f3453a18609530d0f..HEAD -- projects/chirality-app-dev/frontend` must remain empty; instruction-root accepted current-byte identity; every non-product pre-push gate required by the committed loop/PR workflow, including authority corpus, repo self-check, practitioner harness, and App hold if applicable. Record exact commands/exits. Do not rerun product tests/build/package/proof.
- ExpectedOutputs: `ACTIVATION.md`, `REPAIR_LINEAGE.md`, `VALIDATION.md`, and `RETURN.md` in the unique instance; exact inventory/hashes; pass/fail matrix; retained-evidence classification; scope/index/frontend proof; blockers and rerun requirements.
- AcceptanceCriteria: all 12 repairs exactly bounded and lossless; 11 deterministic gzip files recover exact raw bytes; controlling whitespace validator and every authorized gate PASS; no frontend or non-App dirt; no semantic/proof/claim upgrade; index empty.
- Escalation: stop on any extra validator finding, inability to reproduce a preimage, decompression mismatch, frontend/hash drift, out-of-scope need, missing gate authority, or failed gate. Do not repair beyond this brief.
- Git fence: do not stage, commit, fetch, push, open/alter PR, rebase, force-push, or merge.
