# Deferred native discovery repair

Parent actual FILE_CHANGE_1 established primary apply_patch creation and foreign-patch denial but failed because native namespace was deferred. No overall pass claimed.

Provider now emits source-supported tool_search_call with execution client and arguments query/limit when actual spawn/wait tool is absent and actual client tool_search is advertised. Spawn query is exact source-test example "spawn agent", limit1. Wait query is source-shaped "wait agent", limit1. One search per required kind; failure after completed search remains fail-closed, no resend loop. Tools are consumed only from actual completed client tool_search_output with a call ID issued by this fixture, preserving namespace names and declared parameters. Existing directly advertised namespace path unchanged. No feature disabled and no absent tool invented.

Sources: pinned protocol/src/models.rs ToolSearchCall/Output; codex-api/src/sse/responses.rs parses_tool_search_call_items; core/tests/suite/search_tool.rs tool_search_returns_deferred_v1_multi_agent_tools; actual parent FILE_CHANGE_1 tool_search advertisement execution client/query+limit. Actual candidate execution pending parent. OpenAI GPT-6 exact serving ID unavailable, ephemeral Agent2 instruction-asserted, Agent0/2 not mechanically enforced. No delegation/vendor/network invocation.

Checks: JavaScript syntax PASS; explicit fixture typecheck PASS; four offline tests PASS including source-shaped search and rejecting unissued/non-client/pending search outputs. Five loopback/vendor tests skipped. File-change invocation unchanged. Network fixture files not touched.
