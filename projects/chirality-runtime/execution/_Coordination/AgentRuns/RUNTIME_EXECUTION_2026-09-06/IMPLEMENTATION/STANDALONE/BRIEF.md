# Standalone jobs brief

Parent WORKING_ITEMS AMENDMENT3 release. Executor: ephemeral Agent 2, OpenAI GPT-6, exact serving model ID unavailable; instruction-asserted role, not mechanically enforced. No delegation.

Implement actual daemon and supervisor executable composition from existing runtime classes. Allowed files: packages/daemon/src/standalone.ts, standalone-bin.ts, tests/standalone.test.ts, daemon/package.json bin metadata, package-lock.json corresponding bin metadata, and this evidence directory. No dependencies, installation, launchctl, accounts, actual production configuration or foreign writes.

Trusted private JSON selects fixed controlled worker configuration; public clients cannot select executable commands or receive supervisor credentials. Unix-only endpoints and private app-owned directories/files. Atomically rotate supervisor credentials each process generation; daemon verifies the current credential on startup and uses the private client. Use pre-existing explicit ProjectRegistry registration only. Empty engine inventory and explicit unsupported offline service operations. Tests run actual two-job child processes and client consent/turn/termination in disposable roots. Preserve controlled evidence label and no production containment claim.
