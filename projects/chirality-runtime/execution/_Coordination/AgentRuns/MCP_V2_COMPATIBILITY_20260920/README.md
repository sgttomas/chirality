# Desktop Codex MCP stateless compatibility observation

One bounded historical probe, executed 2026-09-20T19:58:54Z–19:58:55Z. This Runtime-owned directory is the canonical retained evidence. Consumers should cite these Git bytes instead of copying the packet. Original scratch: `/private/var/folders/96/1_3ww0012pv5ptwwsd1990yw0000gn/T/chirality-mcp-v2-2ajwqpg0`.

## Result and limits

The tested desktop-bundled Codex `0.155.0-alpha.9.2` initiated MCP `initialize` with protocolVersion `2025-06-18`. The fixture rejected that legacy handshake, and required MCP startup failed. No modern `2026-07-28` request, tool call, cross-workspace test, reconnect or cancellation test was reached. Those unperformed checks are not passes. Recorder/process exit 0 indicates orderly completion of the negative observation, not MCP compatibility.

This establishes incompatibility of this exact transient stdio configuration with a modern-only server. It does not establish that all Codex versions/configurations/transports lack modern support, or qualify hot installation into an existing desktop task. Codex App Server initialization in app-server-wire.json is a separate outer protocol; the decisive MCP exchange is mcp-wire.jsonl. The result makes no claim about Runtime dynamic-tool implementation or Piping live integration.

## Method

Target executable `/Applications/ChatGPT.app/Contents/Resources/codex`, SHA-256 `9280c0754e8f1f6b72f495d30c8c82a006dbc4995bf0492916fa0901f6bfd1f9`; the different PATH CLI was not used. Generated experimental App Server types established the available direct MCP methods before the probe. Their large generated tree is retained only in original scratch; no call method was reached in this negative result.

The child had fresh scratch HOME/CODEX_HOME/cwd, an allowlisted environment, per-run `-c` configuration pointing only to the harmless recorder/server, and the attached sandbox profile denying network and access to real Codex, keychain and Application Support paths. No model turn, login/account request, persistent configuration, token extraction, native UI/VM/CAEPIPE action or Piping resource slot was used. Child processes were stopped on completion. Helper-alias warnings in stderr were retained and did not prevent the observed MCP handshake.

The scripts are original one-off recorder/fixture source, not maintained product commands or a test suite. Do not execute them to consume this evidence. Raw files below were copied byte-for-byte from the original observation; no probe was repeated for preservation. Local paths and the original sandbox profile deliberately remain historical. The single at-sign in probe.py is its log-filter expression, not an account address.

Owner authority in task `dev - app`: conditional acceptance only of stateless MCP V2, followed by “pass on what you learn, not just my statement.” The Piping peer requested an isolated harmless compatibility witness and later this canonical preservation. No integration activation or protocol downgrade is inferred. Agent: HELP_HUMAN / Agent 0, OpenAI GPT-6; no model inference was used by the probe.

## References

- https://modelcontextprotocol.io/specification/2026-07-28/basic/index
- https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning
- https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio
- https://modelcontextprotocol.io/specification/2026-07-28/server/discover

## Original byte identities

| File | Bytes | SHA-256 |
|---|---:|---|
| `result.json` | 1620 | `efe9f5f9084ea8cc9826c1ece3327baff886466d9d3dcd0a499c2f158b7da418` |
| `mcp-wire.jsonl` | 658 | `9e214cc66a68103c3c6ef1b5d8945372091aeee5c1c9eed0fe462ff8005da9a8` |
| `app-server-wire.json` | 2198 | `146fa6e67e1d0045151c7e0e639181d61d1b7a9b78346fd40a9d66a1071d3c16` |
| `probe.py` | 5193 | `64b59d042e39ec945f51e4b85c98730c562d6dcf492fdb7c96aa62a43f000c4d` |
| `server.py` | 2703 | `20ce605ee895b85a56e7a15459ddfe1fd823486ac58f44ef0de2f7e9d03eaa2a` |
| `stderr.log` | 828 | `3e1a73b16b71970945e4a830933a07c763c7eee8dbe094d36ef6bc55f68eee72` |
| `isolation.sb` | 259 | `3b53ac2bd2e8560ab029e55ca5f04b375c88ac38f79870304a7e14a6f514e184` |
