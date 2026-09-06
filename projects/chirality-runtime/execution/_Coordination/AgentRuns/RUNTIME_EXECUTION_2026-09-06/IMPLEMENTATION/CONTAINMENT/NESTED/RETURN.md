# Nested sandbox and broker control follow-up

OpenAI GPT-6, exact serving ID unavailable; ephemeral Agent 2, instruction-asserted. Parent re-dispatch authorized the same two source/test paths and this evidence extension. Original OUTPUTS.json and tests.log remain historical and unchanged.

No production profile relaxation was needed or made. Added real subprocess read/write denials for a synthetic broker credential in a control directory sibling of the worker-private directory. Those checks pass; the credential stays unchanged. Standalone must enforce the worker-private subtree is disjoint from its control directory. This helper cannot infer control paths from its existing options.

Actual nested `/usr/bin/sandbox-exec -p '(version 1)(allow default)(deny network*)' /usr/bin/true` inside the generated outer profile fails at sandbox_apply, exit 71. Actual nested sandbox using the exact generated outer profile succeeds, exit 0. This rules out a blanket inability to nest macOS sandboxes and does not establish a missing filesystem resource.

Isolation matrix: network-only outer profile allows the minimal inner profile. Independent outer file-write denial, securityd lookup denial, and system read allowlist each reject the minimal inner profile. For each of those same restrictions, identical inner and outer profiles succeed. This is consistent with rejection of an inner profile requesting rights missing from the outer profile; it is an inference from the matrix, not an audited OS implementation claim.

The launch caller must prove compatibility of the actual generated Codex child profile under this concrete outer profile. Passing the matching-profile test does not establish that Codex's independently generated workspace profile is compatible. Do not broaden unrelated file or broker/account access merely to get that child to start. No hosted network or account operation was run.

Focused final tests: two test cases passed with actual compatible nested process, incompatible nested denial, sibling control-file denial, outside read/write denial, symlink escape denial and offline socket denial. Initial getcwd warning came from a test inheriting an outside current directory and was corrected by explicitly spawning at canonicalRoot.
