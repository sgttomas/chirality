# Owner Intent of Record — Product delivery direction: domain-specific applications with a Chirality control plane (2026-08-02)

Status: `OWNER INTENT OF RECORD — COORDINATION, NOT AUTHORITY`

This record preserves the owner's product-delivery direction, given in the
root governance session of 2026-08-02 and recorded at the owner's
direction. Its purpose is direction recorded durably enough that project
loops can re-plan against it. It ratifies nothing: it is not a PRD, not
scope, not decomposition input, and not a reliance or lifecycle act. No
design principle is fixed by this record; design principles for the
surfaces named below are to be worked out and proven within the owning
loops. Each loop adopts, amends, defers, or declines any response through
its own instruments and cadence. The surrounding discussion, including
all commercial aspects, remains deliberately unrecorded by owner
direction; only the excerpts below are preserved.

## 1. Primary delivery vehicle

Owner statement, verbatim excerpts:

<!-- BEGIN OWNER INTENT VERBATIM (excerpts) -->
While there is still some value in a user-facing general agent harness,
the agents I'm building will primarily be access through domain-specific
applications, with the Chirality runtime and harness and governance and
coordination and task management all bundled.

So that means I want to focus on the agent harness and runtime as it
pertains to getting the `chirality/projects/chirality-piping/` published
and working as I want to see it, with a robust and user-friendly UI
(we're far from that presently) and the semantic equivalent for agents
through their API
<!-- END OWNER INTENT VERBATIM -->

Restatement (non-authoritative): domain-specific applications are the
primary delivery vehicle for the agents being built. The first instance
is publication of the Chirality Piping application (OpenPipeStress) from
`projects/chirality-piping/`, working as intended, with a robust
user-facing UI and a semantically equivalent agent-facing API surface.

## 2. Standing of Chirality App

Owner statement, verbatim:

<!-- BEGIN OWNER INTENT VERBATIM -->
Chirality App will also remain and be published as an app for your
"desktop". The control plane interface version uses all the same code
except the UI is tied to the needs of that domain-specific app. It's
just focusing the user into typed agent interactions, structured
information, workflows, and decision gates towards outcomes.
<!-- END OWNER INTENT VERBATIM -->

Restatement (non-authoritative): Chirality App continues as a published
standalone desktop application. The same codebase also serves, lightly
skinned, as the control-plane interface for a domain-specific
application — the UI focused into typed agent interactions, structured
information, workflows, and decision gates toward outcomes.

## 3. The domain application's own agent surface

Owner statement, verbatim excerpt:

<!-- BEGIN OWNER INTENT VERBATIM (excerpt) -->
Piping needs its own operative agent surface and therefore maintains its
own version of the available runtime services and agent harnesses
specially tailored to its needs.
<!-- END OWNER INTENT VERBATIM -->

Restatement (non-authoritative): the domain application owns its
operative agent surface — its own tailored version of the runtime
services and agent harness. The lightly-skinned control-plane version of
Chirality App (item 2) is the orchestration plane and user interface for
scaling agentic workflows within that particular application.

## What this record does not do

- It fixes no design principles, architecture decisions, package
  priorities, or sequencing for either loop.
- It performs no product-basis act. Any effect on a PRD, decomposition,
  or scope requires a separate owner-initiated act through the owning
  loop's instruments.
- It adds nothing to required agent reading and is not normative text.
  The owner is separately intent on auditing and reducing governance
  statements, including by converting mature, stable patterns into
  harness tooling; this record must not accrete into such a statement.

## Consumption

Routed for coordination on 2026-08-02 to:

- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`
- `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-02_PRODUCT_DELIVERY_DIRECTION.md`

On any disagreement between a restatement and its verbatim block, the
verbatim governs.
