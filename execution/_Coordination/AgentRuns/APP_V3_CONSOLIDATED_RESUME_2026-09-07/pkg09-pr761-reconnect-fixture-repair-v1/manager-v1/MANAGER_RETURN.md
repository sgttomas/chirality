# PR761 reconnect fixture repair — manager return

Verdict: **PASS_READY_FOR_CHANGE_CI_REQUIRED**

At `f8c9b22cfbc9192c14ee2b6b142371d5bb69f7a5`, the exact one-path successor changes only `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx`: `b21c16a91694a4524d97ffc5a75737a415385372cc8a10de8b1ff955c8d4e879` (11,860 bytes) to `26046c6a127e7496341c05181e0131840cf713ec1324ccbae1d6691c28283fd4` (12,383 bytes).

The partial chat-organization mock retains real `deriveChatTitle` and `visibleActiveChatSessions`, while giving the background title reader an independent no-op four-method interface. All existing replay/reconnect assertions are byte-preserved. This closes the shared-spy fixture collision without changing or masking product behavior.

Final patch: `aa3689fcc53a0692e536031b45434af26074c8f228300a641cfa9775d6b0a9c1` (1265 bytes). Independent review PASS manifest: `2ef0d3d87e982b14abb5a28dd5b0182845d249c55ee8a76e062487397829a797`.

Manager rehashed the exact pre/postimages, confirmed one-path scope, reverse patch applicability, and `git diff --check`: PASS. Matching dependencies are absent; focused tests, related tests, typecheck, full App suite, and Harness remain **CI_REQUIRED_NOT_RUN_LOCAL**. No setup, build, native, package, staging, commit, or release action occurred. CHANGE retains Git custody.
