# CI repair manager return

Source frozen for parent publication checks. Only tests/codex-immutable-file.test.ts and tests/delegated-runtime.test.ts changed; production source and admission fences remain unchanged.

The three immutable-file drift checks require actual macOS Seatbelt and now run only on Darwin. A separate non-Darwin test requires the existing unsupported-platform rejection before macOS file access. Local macOS check: three passed, one skipped. Linux execution remains pending remote CI.

The approval test previously relied on a worker terminating after 900ms. It now keeps the actual supervised worker alive until the host explicitly releases it after all authorization and generation assertions. It verifies the turn remains unsettled before release and completes afterward; failure cleanup releases, interrupts or closes as necessary, and joins the turn. The 10s worker watchdog is only a cleanup bound. Focused real-process/socket check: one passed, 33 unselected, 282ms. No production validity window was relaxed.

Manager inspected both final diffs and specialist return. Evidence is in IMMUTABLE_PLATFORM/ and APPROVAL_LIFETIME/; parent owns combined checks, Linux rerun, lossless evidence presentation packaging, commit and push. No supplier/canary stream was reopened. No child remains running for this repair.

OpenAI GPT-6; exact serving model ID unavailable. WORKING_ITEMS role is instruction-asserted and not mechanically enforced; Agent 0 role likewise is not mechanically enforced.
