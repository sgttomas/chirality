# Discussion — open items after the owner's answers (2026-09-25)

Standing: **proposals (agent) for discussion.** Responses to the items the
owner opened for discussion (D-01, D-04, D-09, D-12). Nothing here is
decided until the owner says so in `DECISIONS.md`.

## 1. The working statement (Q-01, D-01)

What the correction changes:

- The standalone app is **the App for Creating Workflows**. It is the
  exemplar of what then lives "in various guises" in each application.
- Each application has **its own** workflows, skills and tools, made for its
  needs and uses — they are not all authored in one place.
- **The same four agents** apply across all applications; no additional
  roles are planned, though they may come.

With the owner's Q-05 words — "the harness for the model needs to be the
least of my concerns. I'm building agentic engineering applications. There's
plenty to do for getting a generic harness to know the specifics of how
agents should act within and for a particular application" — the product's
distinctive work comes into focus: **making a general agent harness act well
within and for a particular application.**

Three candidate statements, each emphasising something different:

**A. What Chirality does for an application**

> Chirality makes a capable general agent work within and for a particular
> application. Each application carries its own workflows, skills and tools;
> the same four agents use them to act on the application's objects with the
> means the professional has, and the professional directs the work and
> validates it to the degree the situation warrants. The Chirality App, for
> creating workflows, is the exemplar each application follows.

**B. What the professional experiences**

> In a Chirality application, a professional works with four agents that can
> do what the professional can do in that application — guided by workflows,
> skills and tools made for its work. The professional directs, checks and
> decides; what proves useful becomes a workflow to reuse and improve. The
> Chirality App is where workflows are created, and the pattern the other
> applications share.

**C. Short form**

> Chirality turns capable agent harnesses into agentic applications: four
> agents, application-specific workflows, skills and tools, and a
> professional who directs and validates the work.

The agent's preference is **A** as the PRD's opening statement, with C as the
one-line summary. A keeps the three things the owner has insisted on — the
harness is not the product, the application is where the work is, and the
human validates — and names the standalone app's role exactly.

## 2. Autonomy follow-ups (Q-04, D-04)

Option B is settled: the user and the agent work out how to work together;
outputs are validated "to the degree warranted by the situation". Two points
the words leave open, stated as proposals to confirm:

1. **Classifier approval modes are a user choice.** A harness's mode in which
   a model classifier approves routine requests (T7 §4) is one of the ways
   the user and agent may choose to work, like any other permission setting.
2. **One invariant holds everywhere.** An agent never originates or
   represents a human act — acceptance, a checked mark, an approval, an act
   of reliance — in the human's name. Agents may prepare, propose, perform
   within what the user allows, and record; the human's own acts stay the
   human's. (This is Root governance already, K-AUTH-1; stating it in the
   PRD keeps option B from being read as permission to blur it.)

SWBPIPE's row-by-row acceptance then becomes one mode the host offers, not
the only one.

## 3. The build method (Q-11, D-12)

The owner's proposal: keep the decomposition and execution folder structure
and the graph-traversal development loop (teams, subagents or solitary work);
guide the work graphs by having agents **follow the Project Management manual
according to the Agents User Manual**.

### What the proposal gains

- **The manuals get the use they were written for.** OD-08 asks for practices
  to be tried again, examined through use and improved through feedback. T2
  found no project record citing the manuals as a working basis since
  publication. The v4 build would be their first real field test.
- **One coherent method instead of accreted loop instruments.** The lessons
  (L-02, L-06, L-07) came largely from machinery added layer on layer. A
  published method with a stated route (the Field Book) replaces that with
  one source.
- **Symmetry with the product.** Option B for project management (D-09) puts
  coordination of an agent fleet into the product. If the v4 build is run
  by the same practices, the product's project-management capability is
  exercised in its own development — possibly part of the "more to it" the
  owner mentioned.

### Conditions it needs to work

1. **Standing.** The manuals say of themselves that reading them "does not
   amend those instructions or adopt a new execution basis." To make them the
   v4 method, the v4 project's own instructions must adopt them explicitly,
   with a precedence rule: Root governance, then v4 project instructions, then
   the accepted v4 basis (PRD) for *what* to build, then the manuals for
   *how* to organise the work. Creating those project instructions is an
   instruction change with its own scope — naturally part of the
   implementation session's setup, with the owner's approval.
2. **Selective loading.** The Consolidated manual is about 69,000 words. The
   Field Book (about 2,600 words) can be the always-present route; its
   section references into the full manual are loaded when a step needs the
   reasoning; the User Manual supplies the repository application.
3. **Pinned editions.** The User Manual moves with the Root workflow library —
   it changed today alongside workflow repairs on `main`. The v4 project
   should name the manual editions it follows and adopt new ones
   deliberately, not drift with every edit.
4. **Purposes over mechanisms.** The full manual still names some
   repository-specific mechanisms. Where it names one the v4 project does not
   use, the purpose governs and the project records what it does instead.
5. **A feedback loop someone reads.** Agents note, briefly and at the work
   graph node where it happened, where a practice helped, did not fit, or was
   ambiguous. Those notes are reviewed with the owner at each stage gate and
   become manual revisions or deliberate departures. Without a scheduled
   reader, this repeats L-06.
6. **Enforcement from the host, not prose.** Write boundaries and delegation
   limits come from the harness's actual permissions and worktrees; the
   manual describes intent, independent review checks it.

### Questions for the owner

- Does "follow the manual" replace the current loop instruction files for v4
  entirely, or sit beside a thin project loop file that points to it?
- Where the manuals are silent (estimation, schedule, risk — T2 found none),
  should agents improvise and record, or bring the gap to you?
- Who revises the manuals from the feedback: you directly, or agents proposing
  changes for your approval?

## 4. Project management — "more to it" (Q-08, D-09)

Option B is agreed for v4.0. The owner said there is more to it. Candidate
areas the agent would ask about: coordination across projects (PEC's
cross-loop "Waiting on you" slate), estimation and risk (absent from the
manuals), resource and cost tracking for agent work (model usage, time), and
project management inside host applications for engineering projects
themselves (option C). Which of these, or what else, does the owner have in
mind?
