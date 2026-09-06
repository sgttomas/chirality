# Correlated RPC failure diagnostics

Driver source was handed to the parent immediately, before packaging. A PassThrough observes outbound numeric request IDs and method names only, then pipes the original bytes unchanged to the real App Server. It never persists request parameters, input text or full outbound messages. The bounded incoming observer records at most 32 errors: numeric ID, matching method, scrubbed code/message and whether data existed. Error data is not retained. Config-table diagnostics remain separately restricted; their four-record cap no longer prematurely disables later RPC error capture.

Production actor error sanitization and authority checks are unchanged. Existing two fixture/scrubber tests pass with the exact-vendor variable explicitly removed; one vendor test skips. This is syntax/local-fixture verification, not a claim that the diagnostic path was exercised against the vendor. Parent owns the next actual fresh-directory run. No own vendor execution, account or model access occurred.

Attribution: OpenAI GPT-6; exact model ID unavailable. Ephemeral Agent 2, role not mechanically enforced. Prior seals preserved.
