# Render-only job pair return

`renderRuntimeJobs(input)` supplies typed structured daemon/supervisor jobs plus plist strings using exact trusted executable paths and arguments. Labels and Unix socket paths must differ; sockets must lie inside a normalized absolute private runtime directory. No new switches or environment variables are invented. The existing launch-agent renderer always adds `--runtime-daemon`, so it is deliberately not used for the supervisor.

Security requirements are explicit: directory0700/socket0600 and runtime-only credential exchange. Plists include restrictive umask, separated job logs and no environment/credential fields. Unexpected fields and obvious secret/network argument forms reject; arbitrary executable semantics cannot be proven by a renderer. Caller-provided args must be reviewed as non-secret supported configuration. Paths are validated lexically; the eventual launcher must enforce physical ownership/modes and refuse symlink redirection.

Validation: `npm run typecheck` PASS; `npx vitest run packages/cli/test/runtime-jobs.test.ts` 5/5 PASS. Checks cover exact command preservation, XML escaping, distinct identities/sockets, private path confinement, absent invented switches, credentials/public exposure rejection. No files installed, launchctl called, job started or standalone runner availability asserted. Real deployment still requires supported launchers and private credential exchange; this artifact proves renderable topology only.

Author: bounded ephemeral Agent2, OpenAI GPT-6, serving model ID unavailable, role not mechanically enforced/instruction-asserted. No delegation.
