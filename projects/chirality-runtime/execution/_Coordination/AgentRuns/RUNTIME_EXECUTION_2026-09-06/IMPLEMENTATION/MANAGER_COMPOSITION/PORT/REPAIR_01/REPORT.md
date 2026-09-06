# Port timeout repair support

OpenAI GPT-6; exact serving model ID unavailable. Ephemeral Agent 2, instruction-asserted role. Derivative evidence package under Am11; earlier evidence remains sealed.

Independent reviewer confirmed actual port/coordinator repro in REVIEW/ACCUMULATED/review-repro.test.ts: timeout produced failed terminal while child remained active; subsequent child hook completion overwrote failed run evidence with running state. Cancellation ownership is core coordinator, because the current hook contract does not expose an abort operation to the port.

Port changes: trusted constructor callbackTimeoutMs, integer 1..120000, defaults unchanged. Added actual 10ms timeout regression proving failure propagation and supervisor actor retirement; added invalid timeout bound checks. No claim that manager actor retirement cancels a governed child. Core must separately abort and drain all outstanding hook work before final terminal/persistence, including early manager return and ordinary external cancellation. Parent and reviewer were notified; this agent did not edit core.

Validation: tests/codex-manager.test.ts 9/9 PASS using approved local Unix sockets, no provider/account use. Workspace tsc -b PASS.

Handoff: port support complete. Overall lifecycle defect remains open until parent-serialized core repair and independent repro backcheck pass. Parent owns final acceptance and manifest fan-in. Tools: shell/Python edits, Vitest, TypeScript. Exact output hashes in MANIFEST.json; preimages preserved.
