# Runtime extension review

Verdict: PASS for exact-byte verification, render-only jobs and bounded offline protocol probing. No production release, hosted-turn or actual positive vendor-run claim.

Reviewer: OpenAI GPT-6, exact model ID unavailable; ephemeral Agent 2, role not mechanically enforced. No delegation. Source read-only; outputs restricted to REVIEW. The original sealed review is preserved.

## Review

Exact supply pins the accepted 0.149.0 App Server digest and uses regular-file, canonical-path, descriptor/identity and streamed SHA checks. Revalidation rejects replaced inode, aliases, altered bytes and unissued/forged descriptors. Fixture issuance is separate and cannot satisfy accepted-supply verification. Historical R14 identifies this digest as codex-app-server 0.149.0; R16 repeats the accepted digest. Invalid vendor signature remains explicitly unresolved. Verification is not execution authorization; path-based launch retains the explicitly documented post-check race.

Jobs are pure XML rendering. Exact executable/arguments are preserved with escaping, distinct socket/label checks, private-mode requirements and no invented runner switches. Obvious secret/public-network fields are rejected, but arbitrary trusted runner behavior is not proved. No launchd installation, executable implementation or topology enforcement follows from rendering.

Offline probe uses a fresh private home/work/tmp tree, no ambient credential env, fixed observed initialize/config/features/account-read methods, no refresh/login/turn, exact supply verification before actual mode, and a macOS network/write restrictive sandbox profile. Controlled fixtures are distinctly labelled. Output and time are bounded, unexpected protocol responses fail closed, descendants are killed on leader exit, and scratch cleanup is in finally. Returned evidence omits account content and raw stderr. No positive exact binary was executed by this reviewer.

## Checks and calibration

Independent combined run passed 31 tests: 9 supply, 5 jobs, 5 offline probe and 12 delegated integration. checks.log is the exact output. The 19 extension cases exercise actual controlled files/processes, rejection paths, output floods, timeout and cleanup; they do not validate the real vendor protocol or kernel sandbox with a positive exact-supply execution.

Protocol check status passed means the RPC returned result instead of error; config response semantics/enforcement are not validated. Network denial is configured in the profile, but returned evidence does not establish zero attempted egress. Neither a successful fixed-method probe nor the unresolved signature finding permits hosted worker execution. Supply fixture cannot be relabelled into production. No new actionable finding within these explicit boundaries.
