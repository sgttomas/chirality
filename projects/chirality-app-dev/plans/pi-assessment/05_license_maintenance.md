# Pi License And Maintenance Assessment

Date: 2026-06-13

Pi source baseline: `/Users/ryan/ai-env/projects/pi` at commit `9e9fc7947871a913946f727854ae0a57fbce1863`.

## Scope

Assess legal, package, runtime, and maintenance implications for borrowing from or depending on Pi.

Primary sources:

- `/Users/ryan/ai-env/projects/pi/LICENSE`
- `/Users/ryan/ai-env/projects/pi/package.json`
- `/Users/ryan/ai-env/projects/pi/packages/agent/package.json`
- `/Users/ryan/ai-env/projects/pi/packages/ai/package.json`
- `/Users/ryan/ai-env/projects/pi/packages/coding-agent/package.json`
- `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/package.json`

## License

Pi is MIT licensed. The license permits use, copy, modification, merge, publish, distribution, sublicensing, and sale (`/Users/ryan/ai-env/projects/pi/LICENSE:5`). It requires inclusion of the copyright and permission notice in all copies or substantial portions (`/Users/ryan/ai-env/projects/pi/LICENSE:12`).

Implications:

- Pattern borrowing does not require code attribution, but the assessment and any ADR should cite Pi as the source of inspiration.
- Copying code or substantial structure requires preserving Pi's MIT notice, including `Copyright (c) 2025 Mario Zechner`.
- Bundling Pi npm packages should include Pi in third-party notices.
- Forking is legally allowed but would create a large maintenance obligation.

## Package Fit

Pi package versions inspected are `0.79.3`. The generic core package depends on `@earendil-works/pi-ai`, `ignore`, `typebox`, and `yaml` (`/Users/ryan/ai-env/projects/pi/packages/agent/package.json:31`). `pi-ai` depends on several provider SDKs, including Anthropic, AWS Bedrock, Google GenAI, Mistral, OpenAI, proxy agents, partial-json, and TypeBox (`/Users/ryan/ai-env/projects/pi/packages/ai/package.json:69`). `pi-coding-agent` brings the full CLI/TUI/coding surface and dependencies such as `pi-tui`, photon, chalk, cross-spawn, diff, glob, hosted-git-info, proper-lockfile, undici, and yaml (`/Users/ryan/ai-env/projects/pi/packages/coding-agent/package.json:38`).

Chirality currently targets Node `>=20` (`/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/package.json:44`). Pi requires Node `>=22.19.0` at the repo and package level (`/Users/ryan/ai-env/projects/pi/package.json:51`, `/Users/ryan/ai-env/projects/pi/packages/agent/package.json:51`, `/Users/ryan/ai-env/projects/pi/packages/ai/package.json:98`, and `/Users/ryan/ai-env/projects/pi/packages/coding-agent/package.json:92`).

This is the main direct-dependency blocker. Chirality should not add a Pi package dependency until it either raises its runtime floor or isolates Pi behind a Node 22 sidecar process.

## Maintenance Risk

Pi appears actively maintained and fast-moving. That is good for a standalone coding harness but risky as a production embedded dependency. Frequent provider updates, model changes, and platform changes mean Chirality must pin exact versions and avoid loose `^0.x` behavior if it ever depends on Pi.

The current lowest-risk uses are:

1. Reference-only design borrowing.
2. Small code excerpts with MIT notice where a strong practical advantage exists.
3. A sidecar spike pinned to an exact Pi version.
4. A direct package dependency only after Chirality's Node/runtime/packaging strategy is revised.

## Recommendation

| Option | Legal fit | Maintenance fit | Recommendation |
| --- | --- | --- | --- |
| Reference only | Clean | Low cost | Preferred now |
| Borrow selected code | Allowed with MIT notice | Medium; keep small | Use only when necessary |
| Depend on `pi-ai` | Allowed | Node/provider breadth risk | Later spike only |
| Depend on `pi-agent-core` | Allowed | Node/runtime risk | Later spike only |
| Depend on `pi-coding-agent` | Allowed | High risk | Avoid for production |
| Fork Pi | Allowed | High ongoing burden | Do not pursue |

Verdict: **do not add Pi as a Chirality dependency now.** Keep it cloned as a reference, cite it in assessment/ADR material, and revisit an exact-version sidecar adapter only after the current Claude SDK runtime boundary is generalized.
