# Perspective for the implementing session (owner's note)

Orientation first: read Root `AGENTS.md`, then `HANDOFF.md` in this
directory, then the governing records it names. The text below is the
owner's perspective, drafted with the independent reviewer on 2026-09-12 and
reproduced verbatim. It explains intent; the accepted D-GOV-43 record and its
A2 supplement define the scope.

---

You are implementing a deliberate simplification of Chirality, not merely replacing one transport with another.

Chirality helps people direct and validate knowledge work. Its core experience should be simple: plan your work, execute it, save useful methods as workflows, reuse them, and iterate. Mastery comes from learning to direct and validate increasingly demanding work while remaining able to take responsibility for the results.

Codex should provide the agent capabilities. Chirality contributes the conversational interface, four role relationships, reusable workflows, inspectable plans and useful access to artifacts. Its instructions guide how agents participate; they supplement Codex's base instructions. Agents should retain initiative in choosing tools, discovering methods, delegating and adapting within the human's directions and actual permissions.

The previous implementation accumulated a custom daemon, patched Codex binaries, private authentication/admission protocols, fixed configuration restrictions and a narrow event translation layer. These were intended to provide control and evidence, but collectively they restricted useful Codex behavior and made ordinary work fragile. A concrete example: tool activity was discarded, a quiet stream timed out, and the disconnect interrupted legitimate work. Repeated packaging and qualification procedures then made repairs expensive.

The new direction removes that accumulated machinery. Host stock Codex App Server through its supported protocol, preserve its capabilities, and build a reliable Chirality experience around it. Keep Chirality's Codex-managed sign-in separate from other Codex clients while sharing appropriate configuration and resources through the agreed T3-style overlay.

Governance simplification is equally important. Remove requirements and tests whose purpose disappears with the old architecture. Do not recreate them under new names. Preserve ordinary application security, dependency integrity, meaningful independent review and truthful evidence. Preserve historical records without rewriting them. Use concise explanations and reviewed Git changes; do not create another elaborate reporting system to prove that you simplified the first one.

Preserve the established visual direction, but refine or redesign interactions where needed to present Codex's capabilities clearly. The current UI is a good foundation, not a fixed constraint. It does not yet provide everything needed to convey the agents' work and support the user's participation.

Add the presentation and controls needed for tool activity and results, approvals, questions, delegation, plans, interruptions and recovery. Practical improvements that make these interactions more familiar and useful are welcome within the release objective. Reuse existing components where they serve the intended behavior; change them where they do not.

Keep primary surfaces concise, with deeper information available through deliberate inspection. Minimalism means showing what helps the user understand and direct the work. It must not hide useful capabilities or force every interaction into a generic card. Prefer a coherent conversation experience over accumulating panels, controls and technical labels.

Workflows deserve prominence. Skills operate mostly in the background, with less prominent read-only inspection. Activity should make work understandable without flooding the user with protocol metadata. The four roles and one continuing conversation should be sufficient for ordinary use.

This tranche does not include a workflow execution engine, a separate workflow editor, or local-model integration. Workflows are created and revised through conversation. UI refinements that support the agreed experience are implementation work; substantial new product capabilities remain scope decisions.

Judge success by the complete production experience: real planning and revision, substantive tool use, appropriate delegation, saving and reusing a workflow, iteration, interruption, approval handling, and continuation after restart. A demonstration that works only when the agent avoids reading files or doing substantial work is not success.

Build the spike on the production path. Use a separate independent source reviewer before the consolidated signed build. Reuse valid test evidence; repeat affected checks when source, configuration or packaging changes invalidate it. Do not repeat unaffected tests merely because another stage has begun.

Exercise judgment. Routine implementation and UI decisions are yours. Escalate consequential departures from the agreed behavior, substantial product-scope changes or departures from the established visual direction—not every uncertainty or repair. The accepted D-GOV-43 decision defines the implementation scope; this note explains its intent.

The objective is a reliable App the owner can try, followed by the system-prompt discussion and explicit publishing approval.

---

Selected topology (A2, recorded 2026-09-12): the Runtime host is retained
as a simplified service that the App starts, owns and stops as a child
process, speaking its existing socket API, with stock Codex inside it. The
host stays independent of Electron and Next so later Chirality applications
can run it as a sidecar; only the Chirality App is implemented and
qualified in this tranche.
