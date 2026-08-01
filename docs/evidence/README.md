# Root Evidence Register

Status: Root-service evidence surface. Non-normative. Not an agent
instruction surface.

## What this surface is

Dated, session-scoped records of agent-executed work: measured facts,
human rulings and their outcomes, failure logs, and — quarantined in a
clearly marked section of each record — the observations a model derived
from that evidence at the time.

This register exists because facts are not re-derivable (they decay if
uncaptured) while conclusions are (a current model re-derives better
ones from stored facts than any frozen list provides). Records here
preserve the facts and date-stamp the conclusions.

## Who reads this — and who must not

- **Humans**, when authoring or revising doctrine, standards, briefs,
  or workflow definitions.
- **Authoring sessions deliberately pointed here** by a human for that
  purpose.
- **Execution agents (Agent 0/1/2 instances working a live matter) do
  not load this surface.** It is not declared context in any
  `AGENT_*.md`, and it must not become ambient context: a listed
  observation biases pattern-matching on the matter at hand, which is
  exactly the failure mode the runtime's ad hoc composition avoids.
  Pattern selection for live work comes from the model against the
  situation, bounded by ratified doctrine — not from this register.

## Contract for records

- One file per session or bounded engagement, named
  `YYYY-MM-DD_<slug>.md`.
- Facts first (measurements, run IDs, PR references, ruling outcomes),
  repo-relative paths only.
- Derived observations, if included, sit in a terminal section that
  states its date, its origin (which model, which session), and that
  re-derivation from the facts supersedes it.
- No record here is authority for anything. Promotion of an observation
  into doctrine or enforcement follows the normal human-gated path, and
  its terminal form is executable (a guard, gate, profile, or brief
  clause) or ratified doctrine text — never advisory prose left here.
