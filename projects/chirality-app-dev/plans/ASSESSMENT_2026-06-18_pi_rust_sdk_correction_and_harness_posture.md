# Assessment: Pi Rust SDK Correction And Agent Harness Posture

**Date:** 2026-06-18
**Status:** DERIVATIVE ASSESSMENT - session salvage note, not an implementation authorization
**Product:** Chirality desktop harness and bundled agent operating system
**Working root:** `projects/chirality-app-dev/`
**Prepared by:** Codex

## Purpose

This assessment records the useful findings from a session that briefly produced, then deleted, a draft plan for a "Pi agent SDK in Rust." The deleted plan used wording that could imply Pi already has a Rust SDK. The session established that this was not supported by the local evidence.

The durable value is the corrected framing: Chirality's harness architecture supports future provider/runtime adapters behind product-owned contracts, and Pi remains useful as an agent-harness pattern source. A future Rust-native adapter may be desirable, but it should be described as a Rust-native or small-core adapter inspired by Pi-like patterns, not as an existing Pi Rust SDK unless separately proven.

## Findings

1. **Pi is not evidenced as a Rust project in the local checkout.**

   A local file search over `/Users/ryan/ai-env/projects/pi` found no `Cargo.toml` or `*.rs` files, while the checkout contains `package.json` and `tsconfig.json` manifests. The existing Pi assessments also describe Pi packages in Node/TypeScript terms, including `@earendil-works/pi-ai`, `pi-ai`, and `pi-coding-agent` dependencies.

   Evidence: `plans/pi-assessment/05_license_maintenance.md:35-39`.

2. **Chirality's harness is already documented as provider-adapter-general.**

   Current governing and roadmap documents consistently say that external SDKs/providers are implementation substrates behind Chirality-owned contracts. Claude Agent SDK / Anthropic is the first concrete adapter, not the product identity or permanent strategy ceiling.

   Evidence: `docs/PLAN.md:56-60`, `docs/PRD.md:36-42`, `docs/DIRECTIVE.md:114-133`, `docs/CONTRACT.md:51-56`.

3. **Pi is currently authorized only as pattern corpus/reference material.**

   Existing app-dev plans and assessments rule out Pi adapter, fork, package import, sidecar, runtime-floor migration, and spike work under current scope unless a future human ruling explicitly reverses that boundary.

   Evidence: `docs/PLAN.md:456-478`, `docs/PRD.md:112`, `plans/pi-agent-harness-assessment.md:7-30`, `plans/pi-assessment/02_backend_adapter_feasibility.md:68-72`.

4. **The older Pi adapter shape still has useful architecture signal.**

   Historical notes considered a narrow future adapter behind `AgentEnginePort`, mapping Pi stream events into Chirality `UIEvent` and `HarnessEvent` records while keeping provider config, sessions, and terminal outcomes Chirality-owned. Those notes are superseded as authorization, but remain useful as pattern evidence.

   Evidence: `plans/pi-assessment/02_backend_adapter_feasibility.md:37-46`, `plans/pi-agent-harness-assessment.md:115-127`.

5. **Rust-native/small-core thinking exists elsewhere in the project ecosystem.**

   The agent-harness pattern assessment explicitly recommends a "Rust-shaped" smaller runtime approach for compaction and identifies a cleaner small-core structure to emulate: `Session`, `ConversationRuntime`, `PermissionPolicy`, `HookRunner`, `Compaction`, and `ToolRegistry`. Separately, the OpenPipeStress project contains Rust/Tauri crates and local-first deterministic domain-engine architecture.

   Evidence: `plans/agent-harness-patterns-from-claw-code-assessment.md:418-428`, `plans/agent-harness-patterns-from-claw-code-assessment.md:1142-1144`, `/Users/ryan/ai-env/projects/chirality/projects/chirality-piping/apps/desktop/src-tauri/Cargo.toml:1-24`, `/Users/ryan/ai-env/projects/chirality/docs/thesis/bigger-picture/Chirality_OpenPipeStress_Bigger_Picture_Development_Plan.md:1689-1696`.

## Corrected Framing

Do not describe the future feature as "the Pi agent SDK in Rust" unless a Rust Pi SDK is later located or created.

Preferred wording:

> A future Rust-native, small-core agent adapter inspired by Pi's agent-harness patterns, implemented behind Chirality's `AgentEnginePort`, complementary to the Claude Agent SDK / Anthropic adapter.

This wording preserves the useful intent:

- user choice between runtime substrates;
- no replacement of the Anthropic first-adapter path;
- smaller local runtime footprint as a future design goal;
- stronger local governance and fewer ambient dependency/config surfaces;
- resource measurements for constrained machines before claims are made.

It also preserves the current governance boundary:

- Pi remains pattern corpus/reference only;
- no Pi adapter or dependency is authorized by this assessment;
- any concrete adapter requires a future human ruling and bounded implementation tranche.

## Implications For A Future Plan

A future plan should be framed as a feasibility or design tranche, not an implementation tranche, unless the human ruling already exists. It should answer:

- whether the adapter is Pi-inspired, Pi-compatible, or a new Chirality-native Rust runtime;
- whether it targets hosted providers, local models, or both;
- what resource budget it is expected to improve, with repeatable benchmark criteria;
- how it passes the same engine conformance suite as Claude Agent SDK / Anthropic;
- how it prevents ambient config, provider registry, endpoint, credential, extension, and tool-policy leakage;
- how it keeps browser `UIEvent`, persisted `HarnessEvent`, session audit, permission semantics, redaction, and product identity Chirality-owned.

## Assessment Conclusion

The session's useful result is not that Pi is Rust. It is that Chirality already has the architectural space for a future native small-core adapter, and Pi remains a credible source of agent-harness design patterns. The next durable plan should use that corrected language and should explicitly separate direct evidence from inference.
