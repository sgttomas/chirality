# Independent shell fixture v2 backcheck

**NEEDS_REPAIR — one final bounded error-latch correction.** Reviewed fixture v2 SHA256 `36857fb82ea15b6629ca09a9cd5b32cbf286d4b3916f012c0e5a482ed3d5222f`. V1 findings remain preserved in REVIEW_FIXTURE.md. Independent TASK / Type 2, no delegation or fixture/supplier execution. Permitted Node 24.18.0 `--check` passed.

The three original findings are substantially resolved:

- Each issued exec call gets a recorded call_id; only its unique custom_tool_call_output supplies evidence. String and input_text-array output forms are decoded. Each turn terminal is matched to its thread and accepted turn identity. After interruption, a new call must supply fresh exit0 and README output; prior history cannot satisfy it.
- HTTP/stdout/stderr/evidence buffers have limits, ps has timeout/status/signal checks, sockets have inactivity limits and bounded destruction, and failure cleanup censuses and signals identified fixture-owned processes. Forced cleanup retains FAIL. Successful completion requires clean supplier exit and empty process census.
- Direct and pair denial cases now require ordinary exit1, expected marker/denial text and unchanged protected/read-only files. Pair checks reject running/timeout/crash indicators and demand one terminal exit. The output markers match pinned supplier formatters (`core/src/tools/mod.rs:114`, `core/src/tools/context.rs:453`).

**Remaining P2:** late stdout/stderr cap violations or protocol errors set `serverError`, but after the last completed() call the success path never checks it before assigning PASS. An overflow/error during final shutdown can therefore coexist with a passing result. Check the latch immediately before assigning PASS and ensure any error arriving during final shutdown downgrades the result before evidence is saved. This is a local fail-closed correction, not an additional capability or owner approval gate.

Generated policy, synthetic nested file-backed home, thread/turn profile selection and readback remain as previously reviewed. Source/dist binding and account-free/native qualification limits are unchanged. Parent may release within the approved scope after this narrow backcheck; this report makes no execution or qualification success claim.
