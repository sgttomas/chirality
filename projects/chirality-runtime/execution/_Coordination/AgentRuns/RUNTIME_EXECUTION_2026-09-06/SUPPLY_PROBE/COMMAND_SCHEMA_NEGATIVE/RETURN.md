# Standalone command negative schema probe

OpenAI GPT-6 ephemeral Agent 2, serving ID unavailable; role instruction-asserted and not mechanically enforced; no delegation. Parent-authorized exact-pin schema inspection only.

Current official App Server docs https://learn.chatgpt.com/docs/app-server document command/exec as a standalone argv command under server sandbox without creating a thread. Current docs document command array, cwd, sandboxPolicy and timeoutMs; these are discovery candidates, not exact-pin proof. They separately describe process/spawn and thread/shellCommand as outside the internal sandbox; neither was invoked.

On the retained exact original 0.149.0 payload, initialized under the same hard network/home-read/Keychain/write-deny bounds and isolated no-account HOME, command/exec with params:{} returns the exact error in command-negative.json. No command array or executable was submitted, no command ran, no thread/turn/login/provider request occurred. The error supports only this parser reachability and named required field; it does not establish the complete command schema or actual subprocess sandbox behavior. Those are separate bounded probes if parent authorizes them. Original binary retained for aggregate diagnostic.
