# SCA-APP-002 Amendment Preview

**Package Role:** accepted amendment snapshot
**Gate:** 3 — Amendment Approval
**Status:** `ACCEPTED_EXECUTED_VALIDATED`
**Authority:** D-APP-72

This file records the exact amendment accepted by the owner in the instruction to implement the Pi + oMLX second-engine plan. The accepted amendment has been executed and independently backchecked; `Handoff_State.md` and `RUN_SUMMARY.md` record closure.

## Accepted amendment

- Upgrade Electron to `43.1.1`, electron-builder to `26.15.3`, and the project Node floor to `>=22.19.0` before enabling Pi behavior.
- Pin in-process `@earendil-works/pi-coding-agent` `0.80.10`.
- Keep Claude as the default engine and supervisor.
- Add provider-neutral engine selection, session attribution, typed failures, tool representation, and canonical events while preserving current routes and compatibility fields.
- Permit Pi only with oMLX at an authenticated literal-loopback endpoint, exact discovered model IDs, explicit per-child selection, and no automatic fallback.
- Disable Pi built-in tools and ambient resource, credential, settings, extension, skill, prompt, and model discovery.
- Initially expose Pi only to a governed Agent 2 child with one Chirality-owned `read_file` tool.
- Persist parentage, adapter, provider, actual model, sealed brief, permissions, evidence, interruption, and terminal state under Chirality authority.

## Explicit exclusions

The amendment does not authorize a Pi fork or sidecar, Pi-native tools or delegation, extensions or skills, ambient configuration, remote providers, non-loopback oMLX, automatic engine fallback, model aliases, direct Pi supervisor sessions, graphical engine selection, or Pi write, shell, or network access.

It also does not change package or deliverable topology, lifecycle state, release status, publication status, issuance status, or professional-reliance authority.

## Supersession boundary

D-APP-72 prospectively supersedes only the Pi/provider implementation restrictions identified in `Supersession_Delta.csv`. D-APP-01, D-APP-02, D-APP-03, and SCA-APP-001 remain unchanged as historical records. Every restriction not explicitly replaced remains effective.
