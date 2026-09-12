# Public release update source and workflow label

Executor: bounded TASK Type 2, gpt-6-astra medium, no delegation. Parent is
HELP_HUMAN. Work only in the fresh chirality-ui-refinement-packaged-20260912
checkout; baseline ce6f3ade0. Read Root/App AGENTS.md and TASK instructions.
This is direct owner-authorized product refinement, not a held deliverable
activation. Parent owns governance text, instruction work, integration and
independent review. Do not write those surfaces or commit.

The owner named https://github.com/sgttomas/chirality-app/releases as the
public update source and requested `Turn into workflow` instead of
`Save as workflow in chat`. Read-only public API inspection returned v2.0.0
as latest published stable release, with a Chirality-2.0.0-arm64.dmg asset.
Our installed candidate is 3.0.0-rc.1 and must not offer a downgrade.

Implement the existing manual check against the repository's public GitHub
Releases API, without authentication. Use published stable releases (GitHub
latest semantics); do not include drafts or prereleases as normal updates.
Keep the existing browser-mediated download/install UX. Validate the exact
repository source and returned release/download URLs, reject credentials,
redirects and foreign destinations, compare semver correctly, and bound an
unresponsive fetch. Use a suitable asset for the current platform/architecture
or the exact validated release page where asset selection is unavailable;
never imply unsupported architecture installation. Handle network/rate-limit,
no-release, malformed response, equal/newer/older version outcomes truthfully.
Do not add background scheduling, an installer, auto-restart or publishing.

Write scope: frontend/electron/app-update.ts, app-update-source.ts,
app-update-ipc-contract.ts if needed; associated maintained update tests;
frontend/src/components/shell/native-plan-panel.tsx and tests containing the
old exact button label. Paths are relative to projects/chirality-app-dev.
Do not edit electron/main.ts because the parent may need it for instruction
settings. Return any needed main.ts adjustment as a patch recommendation.
Keep other UI wording/design and the action behind the renamed button intact.

Use primary GitHub documentation if protocol facts require external lookup.
Run focused behavioral tests and relevant typechecks after your changes. Do
not repeat full suites, build/sign/launch Apps or access live APIs with private
state. Never read identity/auth/token/binding/keychain/Codex-home/session files,
run security, enter credentials, touch R17 state or access intro-rehearsal.
Filter log lines containing @ before recording. Return changed files, tests,
meaningful limits and required parent integration. Parent validates return,
records it and dispatches a separate reviewer over the final candidate.
