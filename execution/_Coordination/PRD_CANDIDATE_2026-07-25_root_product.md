# Product Requirements Document — Chirality Root (the root product)

> **Status: `CANDIDATE — NOT ADOPTED`.**
>
> This document **binds nothing** (`docs/CONTRACT.md` §1.2, **K-AUTH-1**: only
> humans author binding approval records; no agent may claim to certify,
> approve, sign, seal, or issue work for reliance). Its existence, its
> validation, its commit, and its transport through Git are **not** approval
> (pattern of `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md` §Status banner).
>
> **Adoption is a separate future owner act on a separate instrument.**
> D-GOV-21 packet §11 item 3 expressly withholds the adoption instrument from
> that ruling and routes it to this track; packet §6 step 7 places PRD
> adoption after candidate development; the standing workplan
> (`execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`,
> §Gated downstream item 1) does **not** release it. Nothing in this document
> is adopted, accepted, ratified, or in force by virtue of appearing here.
>
> **Accepted basis:** `main@7ac718c7e` (merge of PR #339; D-GOV-21 sequence
> step 4 closed; Lanes A and B live).
> **Authored under run:** `ROOT-PRD-LANE-A-20260725`
> (`execution/_Coordination/AgentRuns/ROOT-PRD-LANE-A-20260725/`), Lane A of
> the standing workplan, D-GOV-21 packet §6 step 5, on the basis of D-GOV-21
> effect 5.
> **Authored by:** an ephemeral bounded Agent 2 generalist under the sealed
> brief `.../briefs/PRD-AUTHOR-BRIEF.md`, dispatched by `HELP_HUMAN`
> (Agent 0). Agent authorship confers no authority (`AGENTS.md`, Delegation
> and Entry Rules; K-AUTH-1).
> **Placement note:** this file sits on a non-exported coordination surface
> deliberately. Root `docs/` is in the public-export allowlist and root
> `execution/` is not (`exports/chirality-app/export_public.py`, `ROOT_DIRS`
> lines 34–42). The **adopted** PRD's placement is Reserved Decision **RD-4**
> and is not settled here.
> **Date:** 2026-07-25

---

## 1. How to read this document

Every requirement and every identity claim below carries exactly one
provenance label. The labels are defined in §2. Four owner decisions are
expressly **reserved** and are surfaced in §9 with options and consequences;
no agent resolves them. Conflicts between live sources are surfaced in §11
rather than harmonized (K-CONFLICT-1, `docs/CONTRACT.md` §1.9).

The neutral referents used throughout are **"the root product"** and
**"Chirality Root"**. The *genus* wording — the noun phrase that says what
kind of thing the root product is — is **not settled here**; both live
variants are presented in §3.2 and routed to **RD-1**.

---

## 2. Provenance key

| Label | Meaning | Reliance |
|---|---|---|
| **TRANSCRIBED** | Already accepted or ratified doctrine, cited to file and section/line. Verified against the live file at the accepted basis. | In force now, independent of this document |
| **OWNER_DECLARED** | Owner testimony or in-session direction, transcribed by the issuing Agent 0 during the 2026-07-25 root-PRD inquiry. The owner confirms or corrects at adoption. Not reworded. | Not in force as doctrine; awaits owner confirmation |
| **CLARIFIED** | An interpretation of existing accepted truth produced by the 2026-07-25 root-PRD inquiry (Agent 0 plus independent second-agent review, owner-mediated). It is interpretation, not new authority. | Reading aid only; the cited source governs |
| **PROPOSED** | A new commitment that takes effect **only if this PRD is adopted**. Until then it is inert. | None |

A label describes the *provenance* of the statement, not its truth. A
TRANSCRIBED requirement is in force because its source is in force, not
because this document repeats it. A PROPOSED requirement is inert until an
owner act adopts it (§10).

---

## 3. Product identity

### 3.1 What Chirality Root is

**ID-1 — Dual nature. [OWNER_DECLARED]**
Owner framing of record, transcribed in-session during the root-PRD inquiry,
2026-07-25 (Agent 0 transcription; owner confirms or corrects at adoption):

> The root is both an **operating system for governed professional knowledge
> work** and a **normative, self-applying instance of a generative development
> pattern** — it develops itself under the same governance it prescribes.

**ID-1a — The self-application half is independently TRANSCRIBED.
[TRANSCRIBED]**
D-GOV-21 (RULED 2026-07-25; owner ruling "I rule APPROVED for O-A against
candidate SHA `c038c493e871c95871823281b45890ba9404624b`";
AcceptedCandidateSHA `c038c493e871c95871823281b45890ba9404624b`;
PublicationSHA `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`;
EffectiveSHA `ee42157290618e3f84be0e0b651c041387ad6ee0`) makes the repository
root both the shared instruction root and the working root for development of
the root product (`docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
§Effects item 1; packet §2 item 1; `docs/DIRECTIVE.md` §2.6 as amended,
lines 199–204). The root product therefore develops itself inside the
governance it publishes. The owner's *characterization* of that fact as a
"generative development pattern" remains OWNER_DECLARED.

**ID-2 — Four constituting categories. [OWNER_DECLARED]**
Owner framing of record, transcribed in-session 2026-07-25:

> The root product is constituted by **four categories**: **Normative basis**
> (the ratified governance corpus and invariants), **Operative product** (the
> instruction surface, agents, skills, tools, harness, and runtime that do
> work), **Developmental machinery** (the governance harness, decision
> records, loops, and guards by which the product changes itself), and
> **Evidence** (receipts, run records, snapshots, audits — the record that
> makes reliance answerable).

These four categories are the organizing frame for §5.

**ID-3 — Human judgment is the governing hinge. [OWNER_DECLARED]**
Owner framing of record, transcribed in-session 2026-07-25:

> **Human judgment is the governing hinge**: only humans author binding
> approvals (K-AUTH-1); agent capability never confers authority; the
> permanent accountability gap (D-GOV-19) is why the hinge cannot be
> automated away.

**ID-3a — Supporting accepted doctrine. [TRANSCRIBED]**
K-AUTH-1 (`docs/CONTRACT.md` §1.2, line 64) restricts binding approval
authorship to humans. `AGENTS.md` (Delegation and Entry Rules, lines 87–91)
holds that "Delegation never implies capability inheritance" and that "A
child's capability does not become a parent capability"; `docs/DIRECTIVE.md`
§2 (praxiology, line 65) states capabilities "are explicit rather than
inherited". D-GOV-19 (RULED 2026-07-23; Ruling SHA
`981149df247fb6564768f8451e3b12dd591d9197`; AcceptedSourceSHA
`deab7a961c1a5c9fde771039497e50343b681d46`) rules that "the permanent
non-identity between externalizable information and accountable knowing is
the sole primary sense in which the project describes knowledge as chiral"
(§Ruled propositions item 5). D-GOV-17 (RULED 2026-07-18) records that
capability never confers authority regardless of steering content
(`docs/governance_harness/_DECISIONS/_REGISTER.md`, D-GOV-17 row).

**ID-4 — Historical lineage (owner testimony). [OWNER_DECLARED]**
The owner attests roughly three years of prior development lineage preceding
this repository. No in-repo source states this; it rests on owner testimony
and is recorded as such, unblended with the git fact below.

**ID-5 — In-repo history (git fact). [TRANSCRIBED]**
The repository's own git history begins with commit `7bee9ae41`, "Initial
migrated Chirality repository", authored and committed **2026-05-18**; no
commit in the history predates that month. `docs/DIRECTIVE.md` §2.2 ("Git Is
the Event Store", lines 163–167) establishes git as the development record of
record, which is what makes this a citable fact rather than recollection.
**Discrepancy surfaced, not resolved:** the sealed brief for this run states
that in-repo history begins 2026-02-18. That date is not observable in this
checkout's history and no in-repo file was found asserting it. See §11 C-4.
ID-4 and ID-5 are stated separately and are not blended.

### 3.2 Genus wording — two live variants, decision reserved

Two accepted surfaces name the root product with different genera. Both are
transcribed below; **neither is selected here**. The choice is Reserved
Decision **RD-1** (§9.1).

**ID-6 — Variant A (ratified governance). [TRANSCRIBED]**
`docs/DIRECTIVE.md` §1, line 13:

> "Chirality is a governed, filesystem-native agent operating system for
> deliverable-heavy professional work."

This sentence is in the RATIFIED root governance corpus (owner ratification
2026-07-11, D-GOV-09; `docs/DIRECTIVE.md` status banner, line 3). The
sentence's wording entered the tree at commit `b2a1e161f` (2026-06-15) and
was ratified 2026-07-11; the same line was amended by D-GOV-21 Annex A S2 to
admit the root's own working root, without changing the genus phrase.

**ID-7 — Variant B (non-binding surface). [TRANSCRIBED]**
`README.md`, line 3:

> "Chirality is a governed application environment for agent-assisted,
> deliverable-heavy professional work."

`README.md` is classified as a **non-binding / derivative surface** by the
D-GOV-21 packet §3b propagation table (line 125), which directs it to be
reworded to reflect the exception rather than treating it as a normative
clause. This wording entered the tree at commit `d3937edf3` (2026-07-02) —
later than Variant A's authorship, earlier than Variant A's ratification.

**Status of the conflict. [CLARIFIED]** These are not merely different
emphases: an "operating system" and an "application environment" name
different kinds of thing, and the repository's contents are consistent with
both readings (`README.md` lines 3–5 describes the tree as containing "a
filesystem-native agent operating system together with the governance layer,
deterministic tool layer, domain applications … governed project records, and
human gates"). Per K-CONFLICT-1 the disagreement is surfaced with both
citations and routed to RD-1; it is not harmonized here.

### 3.3 What the root product is *not*, structurally

**[TRANSCRIBED]** The root product is not an autonomous system and does not
hold professional authority. `docs/DIRECTIVE.md` §3.1 (lines 226–228) — "Agent
outputs are drafts and structured assistance, not authoritative engineering
judgment"; §3.4 (lines 246–256) — "Agent outputs carry no professional
authority"; K-AUTH-1; K-DOMAIN-4 (`docs/CONTRACT.md` §1.12, line 140) — a
green validation is "structural evidence only".

---

## 4. Problem and users

### 4.1 The problem the root product exists to solve

**[TRANSCRIBED]** `docs/DIRECTIVE.md` §1 (lines 17–21) states three purposes:

1. **Accelerate deliverable-heavy work** (EPC, design-build, software,
   domain-knowledge, proposals, and similar environments) by structuring
   agent workflows around production deliverables and decomposed knowledge.
2. **Make agentic work auditable and controllable** so that outputs can be
   relied upon in professional, regulated, and high-stakes contexts.
3. **Keep humans in charge** at every decision gate, while letting agents
   handle the mechanical work of drafting, extracting, reconciling,
   decomposing, and organizing.

**[TRANSCRIBED]** The underlying diagnosis is stated in `docs/DIRECTIVE.md`
§2 (epistemology, line 41): the problem "is not that they produce bad
outputs — it is that bad outputs are indistinguishable from good ones by
inspection." The system's response is to make epistemic status transparent
and auditable rather than to make the model more reliable.

**[TRANSCRIBED]** The load-bearing architectural commitment is
`docs/DIRECTIVE.md` §1 (line 15): "if the filesystem is the database,
architecture is a state-and-authority specification, not a service mesh."

### 4.2 Users

**[CLARIFIED]** No single accepted source enumerates the root product's
users. The following taxonomy is an interpretation produced by this inquiry
from the cited sources; it is a reading aid, and the cited sources govern.

| User class | Description | Grounding |
|---|---|---|
| **Practitioner-owners running governed loops** | The accountable humans who direct work, rule on decisions, and accept outputs for reliance. Presently one: `docs/governance_harness/human_actors.md` line 20 lists "Ryan Tufts — Owner / sole maintainer; sole author of binding rulings (K-AUTH-1)". | K-AUTH-1; D-GOV-04; `human_actors.md` |
| **Agents as bounded executors** | `agent = LLM + instructions + declared files/context + tools + permissions` (`AGENTS.md` line 17). Agents occupy runtime delegation positions (Agent 0 / 1 / 2), propose and draft, and never approve. | `AGENTS.md` line 17 and lines 46–50; `docs/DIRECTIVE.md` §2 praxiology |
| **Downstream working roots** | `projects/*` and `domains/*` workspaces served by the single shared instruction root, plus the desktop harness's user-selected folders. They consume the instruction surface and may extend — never weaken — the invariant catalog. | `docs/DIRECTIVE.md` §2.6 lines 201–204; `docs/CONTRACT.md` §1 line 11 |
| **Reviewers and auditors of reliance** | Whoever must later determine what may be relied upon, from the evidence trail alone. | `docs/DIRECTIVE.md` §2 (lines 41–61); `docs/TYPES.md` §10.4 |

**[TRANSCRIBED]** The system's scope of applicability is bounded:
`docs/DIRECTIVE.md` §3 (line 224) states that the professional
responsibility model "applies when the system is used in environments where
deliverables are safety-significant, contractually binding, subject to
codes/standards, or produced under professional responsibility."

---

## 5. Product requirements by category

The four categories are ID-2's owner framing. Within each, requirements are
enumerated with exactly one provenance label and a citation. TRANSCRIBED
requirements dominate by design: this PRD **integrates** what is already
ratified; it does not re-legislate it.

### 5.1 Normative basis

**R-N-0 — Category definition. [OWNER_DECLARED]** "**Normative basis** (the
ratified governance corpus and invariants)."

| ID | Requirement | Label | Citation |
|---|---|---|---|
| **R-N-1** | Authoritative project state lives entirely in git-tracked plain files. No external database, server state, or configuration holds authoritative truth. Rebuildable, gitignored projections are permitted, never citable as authority. | TRANSCRIBED | `docs/DIRECTIVE.md` §2.1 (lines 151–161), §5 constraint rows (lines 293–295); D-GOV-01 Option A, RULED 2026-07-01, Ruling SHA `82a35c545282889841ce789c3e24f2ca68991ba1` |
| **R-N-2** | Git is the event store. "If a decision is not in a versioned file, it does not exist for purposes of reliance." | TRANSCRIBED | `docs/DIRECTIVE.md` §2.2 (lines 163–167) |
| **R-N-3** | Only humans author binding approval records; no agent may certify, approve, sign, seal, or issue work for reliance. | TRANSCRIBED | `docs/CONTRACT.md` **K-AUTH-1** (§1.2, line 64); `docs/DIRECTIVE.md` §2.3 |
| **R-N-4** | Approvals bind to a specific git SHA; content change after approval voids the approval. | TRANSCRIBED | `docs/CONTRACT.md` **K-AUTH-2** (§1.2, line 65); `docs/DIRECTIVE.md` §2 (line 59) |
| **R-N-5** | Approvals are always binding and only binding; non-binding guidance is allowed outside approval records. | TRANSCRIBED | `docs/CONTRACT.md` **K-BIND-1** (§1.2, line 66) |
| **R-N-6** | Gates are dynamic per project instance; the minimum required gates are seal transition plus pipeline run approval. No machine BLOCK on the CHECKING→ISSUED judgment may be non-overridable. | TRANSCRIBED | `docs/CONTRACT.md` **K-GATE-1** (§1.7, line 100) and its D-GOV-02 note (line 102) |
| **R-N-7** | Every non-trivial governed claim cites a source path and best-effort section reference, or carries explicit `location TBD`. | TRANSCRIBED | `docs/CONTRACT.md` **K-PROV-1** (§1.9, line 114); `docs/DIRECTIVE.md` §2.4 |
| **R-N-8** | Unknown values become `TBD`, never guessed; agents do not invent scope, targets, parameters, or engineering content. | TRANSCRIBED | `docs/CONTRACT.md` **K-INVENT-1** (§1.9, line 115) |
| **R-N-9** | Conflicts between sources are surfaced with pointers, never silently resolved; the human owns the ruling. | TRANSCRIBED | `docs/CONTRACT.md` **K-CONFLICT-1** (§1.9, line 116); `docs/DIRECTIVE.md` §2 (line 49) |
| **R-N-10** | Claims must not overstate what the available warrant supports; necessity, sufficiency, universality, completeness, exclusivity, and regulatory-conclusiveness language is licensed only by the cited evidence. | TRANSCRIBED | `docs/CONTRACT.md` **K-CLAIM-1** (§1.9, line 117) |
| **R-N-11** | Every agent has an explicit declared write scope and writes nowhere outside it. | TRANSCRIBED | `docs/CONTRACT.md` **K-WRITE-1** (§1.10, line 123) |
| **R-N-12** | Every `ScopePath` and `AllowedWriteTarget` normalizes to an absolute path resolving under `git rev-parse --show-toplevel`; anything resolving outside — including via symlink or `..` — is rejected (`SCOPE_OUTSIDE_WORKTREE`) and the task stops. | TRANSCRIBED | `docs/CONTRACT.md` **K-WRITE-2** (§1.10, line 124); `docs/SPEC.md` §0.2.3 (lines 54–61) |
| **R-N-13** | Task agent outputs to tool roots are immutable snapshots; pointer files may be overwritten, snapshot folders must not. | TRANSCRIBED | `docs/CONTRACT.md` **K-SNAP-1** (§1.10, line 125) |
| **R-N-14** | A Chirality `AGENTS.md` is an authoritative governance surface, not merely an index; where live registries and narrative disagree, the live registry governs and the discrepancy is surfaced. | TRANSCRIBED | `docs/CONTRACT.md` **K-AGENTS-1** (§1.11, line 131) |
| **R-N-15** | Projects decompose as packages containing deliverables (flat, no nesting); deliverable IDs are stable and persist across path changes. | TRANSCRIBED | `docs/CONTRACT.md` **K-HIER-1**, **K-ID-1** (§1.1, lines 57–58) |
| **R-N-16** | `_STATUS.md` is the canonical lifecycle state file; upstream changes propagate staleness to transitive dependents; stale items are human-triaged; a deliverable is dirty if a governed input changed since its last approved SHA. | TRANSCRIBED | `docs/CONTRACT.md` **K-STATUS-1**, **K-STALE-1/2**, **K-VAL-1** (§§1.5–1.6, lines 86–94) |
| **R-N-17** | Deliverable-local dependency registers are authoritative; there is no central dependency graph; dependency references resolve to existing IDs or are marked `UNKNOWN`. | TRANSCRIBED | `docs/CONTRACT.md` **K-DEP-1**, **K-DEP-2** (§1.4, lines 79–80) |
| **R-N-18** | Merge to main is allowed only when branch HEAD equals the approved SHA for the relevant run. | TRANSCRIBED | `docs/CONTRACT.md` **K-MERGE-1** (§1.8, line 108) |
| **R-N-19** | No delegated child execution before context is sealed, the run is approved at the applicable human gate, and the launch cites that approval record; Agent 2 context is limited to declared read scopes — no ghost inputs. | TRANSCRIBED | `docs/CONTRACT.md` **K-SEAL-1**, **K-GHOST-1** (§1.3, lines 72–73) |
| **R-N-20** | Domain engines own authoritative domain truth; protected domain paths are write-quarantined; domain operations require an OperationProposal plus explicit human acceptance; domain-engine output is never professional approval. | TRANSCRIBED | `docs/CONTRACT.md` **K-DOMAIN-1..4** (§1.12, lines 137–140) |
| **R-N-21** | One opt-in per-user daemon exclusively owns engines, credentials, sessions, delegation, tools, turn locks, interruption, and residency; control is authenticated HTTP/1.1 over a protected Unix-domain socket with no TCP listener; tracked project manifests hold relative authority references only; runtime state never replaces checkout-contained governance truth; roles are model-independent; the public export excludes credentials, machine state, and private project adapters. | TRANSCRIBED | `docs/CONTRACT.md` §1.13 **K-RUNTIME-1**, **K-CONTROL-1**, **K-PROJECT-1**, **K-STORE-2**, **K-RESIDENCY-1**, **K-ROLE-2**, **K-EXPORT-1** (lines 148–154); `docs/DIRECTIVE.md` §7; D-GOV-20 |
| **R-N-22** | The authority chain is DIRECTIVE (why) → CONTRACT (binding invariants) → SPEC (physical structures and path anchoring) → TYPES (canonical vocabulary), with `AGENTS.md`/`agents/` as the live instruction surface. Where a candidate or lower document conflicts with ratified governance, ratified governance controls and the conflict is surfaced. | TRANSCRIBED | `docs/DIRECTIVE.md` §Authority chain (line 7) |
| **R-N-23** | The four pillars — ontology, epistemology, praxiology, axiology — are the system's accountability ontology; the ontology, praxiology, and axiology exist to serve the epistemology. | TRANSCRIBED | `docs/DIRECTIVE.md` §2 (lines 27–133), esp. §How the Pillars Relate (112–120) and §The Pillars as the Ontology of Professional Accountability (122–133) |
| **R-N-24** | The professional responsibility model holds: AI outputs are drafts; a licensed professional retains scope, code-selection, hazard-acceptance, adjudication, and issuance rights; competence includes tool competence; the hierarchy of authority runs laws → codes → project specifications → verified analysis → professional judgment. | TRANSCRIBED | `docs/DIRECTIVE.md` §3 (lines 222–256) |
| **R-N-25** | Out of scope, structurally: automated approval or issuance; financial transactions or binding commitments; safety-critical decisions without human review; replacing professional judgment in regulated practice; external systems as a source of authoritative project truth. | TRANSCRIBED | `docs/DIRECTIVE.md` §4.2 (lines 277–283) |
| **R-N-26** | The normative basis is a **constituent of the product**, not documentation *about* the product. A requirement of Chirality Root is therefore, in large part, the invariant catalog itself: the product must continue to satisfy K-\* rather than merely describe them. | CLARIFIED | Interpretation of `docs/CONTRACT.md` §2 (Enforcement Map, lines 165–178), which assigns each invariant a live enforcement point in the running system rather than a documentary one |

### 5.2 Operative product

**R-O-0 — Category definition. [OWNER_DECLARED]** "**Operative product** (the
instruction surface, agents, skills, tools, harness, and runtime that do
work)."

| ID | Requirement | Label | Citation |
|---|---|---|---|
| **R-O-1** | The shared instruction surface is exactly `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and `init/`; it is release-managed and read-mostly — changing it is a repo-wide governance action, not ordinary working-root execution. | TRANSCRIBED | `docs/DIRECTIVE.md` §2.6 (line 201); `docs/SPEC.md` §0.2.1 (line 44); `docs/TYPES.md` §1.4 (Instruction Root row) |
| **R-O-2** | An agent is `LLM + instructions + declared files/context + tools + permissions` — an operational definition, not a claim of personhood or professional responsibility. The human remains accountable for what is accepted or relied upon. | TRANSCRIBED | `AGENTS.md` §What Is an Agent? (line 17; operational-definition note, lines 20–23) |
| **R-O-3** | Three runtime delegation positions exist: Agent 0 Supervising Architect (sole canonical: HELP_HUMAN), Agent 1 Manager, Agent 2 Specialist. Human entry is untyped, Agent 0, or any Agent 1. Agent 0 delegates only to named Agent 1s; Agent 1 delegates to Agent 2 forms; **Agent 2 does not delegate**. | TRANSCRIBED | `AGENTS.md` §Good Agents and Great Workflows (table rows, lines 48–50) and §Delegation and Entry Rules (lines 82–86); `docs/DIRECTIVE.md` §2 praxiology (line 65); D-GOV-11 (RULED 2026-07-11) |
| **R-O-4** | Agent 2 may be instantiated as a TASK agent (shell + skill + sealed brief), an ephemeral bounded generalist (sealed purpose-specific brief, no persistent instruction file), or a human-approved dedicated specialist. A dedicated specialist requires a HELPS_HUMANS proposal and explicit human approval. | TRANSCRIBED | `AGENTS.md` §Agent 2 Construction Forms (lines 58–78); D-GOV-13 approved through D-GOV-14 item 4, published at `d22f80bf5d6c1190ce151df75d936bfcf4d38bc3` |
| **R-O-5** | Delegation never implies capability inheritance; a child's capability never becomes a parent capability; every child remains subject to sealed context, pipeline approval, path containment, enforced read/write scope, and durable evidence. | TRANSCRIBED | `AGENTS.md` lines 87–91 |
| **R-O-6** | Multi-agent execution may use terminal fan-out/fan-in, supervised parent-mediated many-to-many agency, or any dependency-valid mixture. Concurrent sibling writes must be disjoint; overlapping writes require serialization or one declared integration owner. Failed nodes block only their declared dependants; partial or invalid returns are not accepted at fan-in. | TRANSCRIBED | `AGENTS.md` §Multi-Agent Orchestration (lines 102–172); D-GOV-12 (RULED 2026-07-11) |
| **R-O-7** | `skills/` holds repo-native bounded method packs dispatched through TASK; the authoritative skill inventory is the live set of `skills/*/SKILL.md` folders governed by `skills/README.md`, not any narrative list. | TRANSCRIBED | `AGENTS.md` §TASK Skill Capabilities (lines 243–262) |
| **R-O-8** | `tools/` is the deterministic layer: a deterministic operation available to an agent, **never a substitute for semantic judgment**. | TRANSCRIBED | `AGENTS.md` line 33 (Tool row of the terminology table) |
| **R-O-9** | The path model defines two roots and one containment rule, with a closed `{*_ROOT}` token registry; an agent introducing a new token must declare its anchor and keep it consistent with the registry. | TRANSCRIBED | `docs/SPEC.md` §0.2 (lines 28–67), §0.3 (lines 71–91); `docs/TYPES.md` §1.4–§1.5 |
| **R-O-10** | Instruction-surface references resolve `REPO_ROOT`-relative; working-root references resolve `WORKING_ROOT`-relative; instruction, coordination, and plan files MUST NOT embed machine-absolute paths. Absolute paths appear only in run records and evidence, where they record what happened and are never re-executed. | TRANSCRIBED | `docs/SPEC.md` §0.2.4 (lines 63–67) |
| **R-O-11** | An execution instance is a self-contained workspace rooted at `{EXECUTION_ROOT}/`, containing `PKG-*` packages (with `0_References/`, `1_Working/`, `2_Checking/`, `3_Issued/`) and tool roots. | TRANSCRIBED | `docs/SPEC.md` §1 (lines 95–127) |
| **R-O-12** | The managed multi-agent runtime persists one durable record tree per orchestration run at `{EXECUTION_ROOT}/_Coordination/AgentRuns/<RunID>/`, with immutable/versioned plans, briefs, returns, notices, dispositions, amendments, and final handoff state; every work graph records RunID, plan version, selection authority, posture, accepted basis, nodes, edges, concurrency eligibility, read scopes, write ownership, expected returns, fan-in gates, and human decision points. | TRANSCRIBED | `docs/SPEC.md` §9.8 (lines 756–775) |
| **R-O-13** | The instruction root is separated from the working root, with **exactly one** governed exception: the root product's working root is the repository root. No other working root may be located inside the instruction root. | TRANSCRIBED | `docs/DIRECTIVE.md` §2.6 (lines 199–206); `docs/SPEC.md` §0.2.2 (lines 48–52); `docs/TYPES.md` §1.4; D-GOV-21 Annex A S1–S9 |
| **R-O-14** | Root `execution/` is the root product's lawful execution root, **eligible** for `PKG-*`/`DEL-*` structure only from an accepted root decomposition derived from an adopted root PRD and only while guards G0–G4 are registered and passing. Existing root coordination and evidence records remain valid historical state. | TRANSCRIBED | D-GOV-21 §Effects item 2; packet §2 item 2, §5.3, §6 step 9; `docs/SPEC.md` §1 (line 97); `execution/_Coordination/LOOP_INIT.md` §1 |
| **R-O-15** | The replacement containment contract M1–M7 is required for root development: fine-grained write ownership (M1); instruction-surface touches are governance actions requiring independent owner authorization, with the touching child serialized as sole integration owner and merge through a human-gated PR carrying a tranche manifest (M2 — the gate supplies containment and evidence conditions and does **not** itself grant authorization, per K-AUTH-1); frozen instruction basis per run (M3); worktree isolation for concurrent root children (M4); accepted snapshots at fan-in (M5); routed change notices per accepted tranche (M6); defined rollback posture (M7). | TRANSCRIBED | D-GOV-21 packet §5.2 (lines 169–208), ruled as effect 4. *Note:* within the packet's own labeling several M-items were PROPOSED; PROPOSED there means "effective only if this record is ruled" (packet §5.2 line 171), and the record **is** ruled — so they are in force now. |
| **R-O-16** | Deterministic guards G0–G4 are required with the §5.3 gate ordering: G0 materialization fence (shipped and wired into governance-harness CI), G1 root harness adapter, G2 static surface-ownership register plus validator, G3 pre-dispatch work-graph check, G4 instruction-surface tranche-manifest check. Guard **capability** exists before root Project Setup; root Project Setup **instantiates** guard state; G0 gates materialization on both. | TRANSCRIBED | D-GOV-21 packet §5.3 (lines 210–250); implementation handoff (`docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` lines 36–42) records G0 shipped as `tools/validation/validate_root_materialization_fence.py` with CI wiring |
| **R-O-17** | The same instruction surface is packaged as a desktop harness running agents against a user-selected working folder; in deployable desktop builds `agents/`, `skills/`, `tools/`, `docs/`, and `init/` are packaged as `instruction-root/`. | TRANSCRIBED | `docs/DIRECTIVE.md` §1 (line 13), §2.6 (line 201); `docs/SPEC.md` §0.2 (line 32) |
| **R-O-18** | Root `runtime/` is the generic executable agent-runtime workspace; desktop, the bundled CLI, and registered projects are clients of one opt-in per-user daemon over an authenticated Unix-domain socket. Generic runtime transport never grants project authority. The initial local pilot is deliberately narrow and authorizes no fallback, no local Agent 1, no production domain mutation, and no professional reliance. | TRANSCRIBED | `docs/DIRECTIVE.md` §7 (lines 316–335); `AGENTS.md` §Shared Runtime Doctrine (lines 264–277); D-GOV-20 |
| **R-O-19** | The in-scope capability set includes project/software/domain decomposition, workspace scaffolding, document-kit drafting, dependency extraction and reconciliation, semantic analysis, source extraction and cataloging (PDF/drawing/equation pipelines), cost estimation and schedule generation, publication assembly, aggregation/audit/evaluation, and change-management support. | TRANSCRIBED | `docs/DIRECTIVE.md` §4.1 (lines 262–275) |
| **R-O-20** | The operative product's boundary is the instruction surface (R-O-1) plus root `runtime/`. Everything the product "does" is expressed as either an instruction artifact or a deterministic tool; there is no third execution substrate. This is why an instruction-surface change is a governance act rather than a code change. | CLARIFIED | Interpretation of `docs/SPEC.md` §0.2.1 (line 44) with `docs/DIRECTIVE.md` §7 and D-GOV-21 M2 |

### 5.3 Developmental machinery

**R-D-0 — Category definition. [OWNER_DECLARED]** "**Developmental
machinery** (the governance harness, decision records, loops, and guards by
which the product changes itself)."

| ID | Requirement | Label | Citation |
|---|---|---|---|
| **R-D-1** | Consequential governance changes terminate in a published decision record under `docs/governance_harness/_DECISIONS/`, carrying status, verbatim owner ruling, SHAs, date, framing, accepted basis, decision key, and record convention; `_REGISTER.md` is a navigational summary and the per-decision records govern on disagreement. | TRANSCRIBED | `docs/governance_harness/_DECISIONS/_REGISTER.md` (lines 1–10); record header pattern, e.g. D-GOV-21 lines 3–13 |
| **R-D-2** | Decision records are **superseded, never edited**. A later correction to a ruled record is a superseding act, not an edit; amending a ruled candidate would void its AcceptedCandidateSHA. | TRANSCRIBED | D-GOV-21 record `RecordConvention` (line 12) and §Status note (lines 26–28); D-GOV-17 (line 168) recorded-exception protocol; `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` (lines 83–87) |
| **R-D-3** | Where a proposal contains substantial PROPOSED requirements, the ruling binds to an **exact candidate SHA**: commit the exact packet, record `AcceptedCandidateSHA`, record the owner ruling verbatim inside a ruling fence, publish the record, and record the merged implementation commit as `EffectiveSHA`. Any deviation from ruled exact prose returns for exact-prose re-acceptance before merge. | TRANSCRIBED | D-GOV-21 packet §14 (lines 369–391); D-GOV-18 and D-GOV-19 precedents (`_REGISTER.md` rows) |
| **R-D-4** | Identity attribution for `RuledBy`/`AdoptedBy`/`HumanRuling` matches an owner-curated allowlist; identity-dependent harness checks **REFUSE (exit 2)** when the file is absent or an actor does not match — refuse rather than guess. The list is owner-curated and must not be extended programmatically. | TRANSCRIBED | D-GOV-04 (RULED 2026-07-01, Ruling SHA `82a35c545282889841ce789c3e24f2ca68991ba1`); `docs/governance_harness/human_actors.md` (lines 3–14) |
| **R-D-5** | Deterministic validation uses the five-severity taxonomy with exit-code semantics: BLOCK (objective violation within the declared observation boundary; nonzero exit; human-only recorded override), REVIEW, WARN, INFO, NOT_APPLICABLE. "BLOCK" never means globally proven safe or unsafe. | TRANSCRIBED | D-GOV-02 (RULED 2026-07-01, Ruling SHA `82a35c545282889841ce789c3e24f2ca68991ba1`), severity table and caveats |
| **R-D-6** | A validator finding may never mechanically reject content the owner has adopted or ruled: where ruled text trips a validator, the validator is defective and is corrected under review — never the ruled text. | TRANSCRIBED | D-GOV-17 (RULED 2026-07-18), M2 floor-plus-corrections; `docs/CONTRACT.md` §1.7 note (line 102) |
| **R-D-7** | Seven governance integration rules bind phase-crossing work: derivative-package, snapshot, handoff-state, closure, sequencing, cycle-resolution, and agent-index change-notice. | TRANSCRIBED | `AGENTS.md` §Governance Integration Rules (heading line 174; rules, lines 176–182); `docs/DIRECTIVE.md` §2.7 (lines 208–218) |
| **R-D-8** | Root-product development runs through a governed loop: `LOOP_INIT.md` (session init, authority discipline, orchestration, stops and write fences, closeout), a deterministic standing-plan pointer `CURRENT_WORKPLAN.md` resolved by target rather than by mtime/filename/narrative, and an append-only `LOOP_RECEIPTS.md`. Coordination surfaces carry **no authority merely because they exist**; on disagreement with a live source, the live source governs and the delta is recorded. | TRANSCRIBED | `execution/_Coordination/LOOP_INIT.md` §§1–7; `execution/_Coordination/CURRENT_WORKPLAN.md`; `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md` §Authority basis (lines 20–27) |
| **R-D-9** | The governance-harness CI workflow runs the harness suite plus self-check on every PR and push to main, with the G0 materialization fence as a step; BLOCK exits fail the run per D-GOV-02, and REVIEW never gates. | TRANSCRIBED | `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` (lines 36–42); `_REGISTER.md` Completed item 10 addendum |
| **R-D-10** | Git closeout runs through CHANGE with human-gated PRs; **never self-merge**. Every lawful tranche appends one minimal receipt and emits an explicit handoff state. | TRANSCRIBED | `execution/_Coordination/LOOP_INIT.md` §7 (lines 115–127); standing workplan §Closeout (lines 266–273); `AGENTS.md` agent index (CHANGE row) |
| **R-D-11** | The decomposition pipeline is not waivable: `PKG-*`/`DEL-*` at root may come only from an accepted root decomposition. Nothing authorizes inventing packages from discussion. | TRANSCRIBED | D-GOV-21 packet §4 (lines 135–137); standing workplan §Gated downstream item 2 |
| **R-D-12** | The public-export boundary is maintained by an explicit allowlist profile that copies allowlisted files, sanitizes private absolute paths, writes a manifest and report, and fails on forbidden public paths or private absolute-path leaks. The export manifest is regenerated after changing any public-exported file. | TRANSCRIBED | `exports/chirality-app/export_public.py` (`ROOT_FILES` 21–28, `PUBLIC_ROOT_FILES` 30–32, `ROOT_DIRS` 34–42, `EXCLUDED_PUBLIC_PATHS`/`EXCLUDED_PUBLIC_PREFIXES` 44–51); `README.md` §Publishing Pipeline (lines 202–217); `docs/CONTRACT.md` **K-EXPORT-1** |
| **R-D-13** | A tranche that changes surfaces which downstream loops pin or mirror ships, in the same tranche, a routed coordination notice to each affected loop's coordination surface. The notice is coordination, not authority: the receiving loop adopts, amends, or declines under its own instruments. Detection must not depend on the downstream loop's own drift checks alone. | TRANSCRIBED | `AGENTS.md` §Agent-index change-notice rule (line 182); D-GOV-21 M6 (packet lines 202–207) and its §3b propagation table (lines 116–129) |
| **R-D-14** | The developmental machinery is **product scope**, not surrounding process. The harness, records, loops, and guards are things the root product must contain and keep working, and they are therefore legitimate targets of decomposition, deliverables, and acceptance — not exempt overhead. | CLARIFIED | Interpretation of ID-2 against D-GOV-21 packet §5.3 (guards are "preconditions, not future tooling", line 249–250) and `AGENTS.md` closure rule |
| **R-D-15** | Once adopted, this PRD is amended only by a superseding instrument bound to a git SHA, on the D-GOV-18/19/21 exact-candidate pattern. The adopted bytes are never edited in place. | **PROPOSED** | New commitment. Extends R-D-2 (whose ratified scope is D-GOV decision records) to the PRD artifact class. Inert unless adopted. |
| **R-D-16** | A standing concordance obligation binds the adopted PRD and `docs/DIRECTIVE.md` §1: any superseding amendment to either re-runs the concordance map and records the result. | **PROPOSED** | New commitment. D-GOV-21 packet §11 item 3 requires the concordance map **at adoption**; a standing post-adoption obligation is not established anywhere and is proposed here. Contingent on **RD-3**. Inert unless adopted. |
| **R-D-17** | The first root decomposition must demonstrate coverage across all four categories of ID-2 — every category either has decomposition coverage or a recorded, reasoned deferral. This constrains coverage demonstration only; it does **not** prescribe the decomposition's package partition. | **PROPOSED** | New commitment. Grounded in `AGENTS.md` closure rule (line 179) and the coverage-audit pattern (`AGENT_AUDIT_DECOMP`), but the four-category coverage obligation itself is new. Inert unless adopted. Strikeable without affecting any other requirement. |

### 5.4 Evidence

**R-E-0 — Category definition. [OWNER_DECLARED]** "**Evidence** (receipts,
run records, snapshots, audits — the record that makes reliance answerable)."

| ID | Requirement | Label | Citation |
|---|---|---|---|
| **R-E-1** | Every orchestration run persists a durable, versioned record tree under `_Coordination/AgentRuns/<RunID>/`. `<RunID>` is created only when a real run begins; placeholder runs and briefs represented as executed children are prohibited. | TRANSCRIBED | `docs/SPEC.md` §9.8 (lines 756–775); `execution/_Coordination/LOOP_INIT.md` §5 (lines 75–95) |
| **R-E-2** | Every phase-boundary decision that changes or validates governed state terminates in a new immutable snapshot; later phases consume accepted snapshots, not mutable working state. | TRANSCRIBED | `AGENTS.md` snapshot rule (line 177); `docs/DIRECTIVE.md` §2.7; **K-SNAP-1** |
| **R-E-3** | Any workflow stopping with work intended for another agent or phase emits an explicit handoff state naming accepted upstream snapshot(s), derivative-package status, closure verdict, rerun requirements, and remaining blockers. | TRANSCRIBED | `AGENTS.md` handoff-state rule (line 178); exemplar: `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` |
| **R-E-4** | Each lawful tranche appends one minimal receipt recording owner directions not recorded elsewhere, artifact pointers, gate outcomes, check summaries, and unresolved blockers. | TRANSCRIBED | `execution/_Coordination/LOOP_INIT.md` §7 (lines 115–127) |
| **R-E-5** | Rulings are SHA-bound: the publication commit binds the ruling, and the record carries the exact SHAs (`AcceptedCandidateSHA`, `PublicationSHA`, `EffectiveSHA` where applicable). Decisions are cited by ID plus SHA, never by recollection. | TRANSCRIBED | **K-AUTH-2**; `_REGISTER.md` (lines 1–10); D-GOV-21 header (lines 5–7) |
| **R-E-6** | Claims carry epistemic labels (FACT / ASSUMPTION / PROPOSAL / TBD) and progress through the warrant lifecycle `UNWARRANTED → CITED → REVIEWED → AUTHENTICATED`. AUTHENTICATED requires an accountable actor's scoped, purpose-specific, SHA-bound act. | TRANSCRIBED | `docs/DIRECTIVE.md` §2 (lines 51, 61); `docs/TYPES.md` §10.3–§10.4 (lines 431–460); D-GOV-19 ruled proposition 4; D-GOV-08 (Option B) |
| **R-E-7** | Read-only audit and evaluation surfaces exist and are governed: coverage, dependency-closure, hypergraph-closure, governance-consistency, epistemic-ontology, scope-closure, and agent-conformance audits, plus EVALUATION orchestration. | TRANSCRIBED | `AGENTS.md` agent index (Agent 2 audit rows); `docs/DIRECTIVE.md` §4.1 |
| **R-E-8** | Validation evidence is written only under declared generated paths, with the mutation-control contract; the harness never writes governed authority files, and governed-file mutation by a validation command is an unconditional BLOCK. | TRANSCRIBED | D-GOV-01 Option A; `_REGISTER.md` Completed item 9 (lines 116–133) |
| **R-E-9** | A scope unit or phase is not closed merely because files were written. Closure requires accepted authoritative truth, regenerated or explicitly deferred derivative packages, recorded audit status, and surfaced unresolved blockers. | TRANSCRIBED | `AGENTS.md` closure rule (line 179); `docs/DIRECTIVE.md` §2.7 |
| **R-E-10** | The D-GOV-21 falsifiers F1–F3 are under standing watch; observing one is recorded and raises packet §8 rollback consideration to the owner. | TRANSCRIBED | D-GOV-21 packet §9 (lines 305–320), §8 (lines 294–303); standing workplan §Stop state (lines 260–264) |
| **R-E-11** | Evidence completeness is not evidence sufficiency. The provenance ladder measures whether warrant is present, never whether it is adequate for a given reliance purpose; adequacy is a human judgment against scope and purpose. | CLARIFIED | Interpretation of D-GOV-08 Option B as implemented — "`evidence-check` applies the D-GOV-08 Option B provenance ladder (completeness, never sufficiency)" (`_REGISTER.md` Completed item 9); K-DOMAIN-4 ("Validation-passed is necessary, not sufficient"); K-CLAIM-1 |

---

## 6. Self-application

### 6.1 The claim

**[OWNER_DECLARED, per ID-1]** The root product is a normative, self-applying
instance of a generative development pattern: it develops itself under the
same governance it prescribes.

**[TRANSCRIBED]** The mechanism by which that claim is made operational is the
ruled D-GOV-21 sequence (packet §6, lines 252–273), of which this document is
step 5:

| Step | Act | Status at basis `main@7ac718c7e` |
|---|---|---|
| 1 | Inventory affected doctrine, assumptions, pins, coordination surfaces | Complete (packet §3, §3b, §5.1) |
| 2 | Rule D-GOV-21 per §14 mechanics | Complete — RULED 2026-07-25 |
| 3 | Implementation tranche (Annex A, §3b propagation, S10, G0, register row) | Complete at EffectiveSHA `ee42157290618e3f84be0e0b651c041387ad6ee0` |
| 4 | Reorient the root coordination loop | Complete (PR #339; standing workplan is the pointer target) |
| **5** | **Develop the candidate root PRD** | **This document** |
| 6 | Implement and validate guard capability G1–G4 | Live in parallel as Lane B |
| 7 | Adopt the root PRD (exact bytes, separate instrument) | **Gated — not released** |
| 8 | First root decomposition from the adopted PRD; root Project Setup instantiates the G2 register and first accepted work graph | Gated |
| 9 | Materialize `PKG-*`/`DEL-*` under root `execution/` from that accepted decomposition, with G0–G4 passing | Gated by §5.3 |

**[TRANSCRIBED]** The self-application therefore runs the root product
through its own pipeline — PRD → adoption → decomposition → Project Setup →
materialization under root `execution/` behind the §5.3 gate — with root
`execution/` holding control-plane records only until that gate closes
(`execution/_Coordination/LOOP_INIT.md` §1; standing workplan §Gated
downstream, line 187–188).

### 6.2 Falsifiers of the self-application claim

**Ruled falsifiers. [TRANSCRIBED]** D-GOV-21 packet §9 (lines 305–320)
defines three, which this PRD adopts as product-level falsifiers of ID-1:

- **F1 — Containment failure.** Root self-development corrupts a shared
  instruction surface out from under a situated loop (detected by that loop's
  corpus-drift or pin checks) in a way the superseded separation would have
  prevented, and M1–M6/G0–G4 did not detect or gate it first.
- **F2 — Loop bypass.** Root product development proceeds outside the root
  governed loop — work materialized at root `execution/` without a current
  workplan pointer, receipts, and the M2/G4/M6 machinery engaged.
- **F3 — Self-authorization.** A root node consumes a capability produced by
  root development before that capability was accepted through the basis or
  an explicitly accepted predecessor.

**PRD-level falsifiers. [PROPOSED]** These take effect only on adoption and
are inert until then:

- **F4 — Requirements drift.** At the close of the first root decomposition,
  an accepted scope unit cannot be traced to a requirement of the adopted
  PRD, or a requirement of the adopted PRD has neither decomposition coverage
  nor a recorded deferral. *(Falsifies the claim that the product develops
  itself* from *its own stated requirements.)*
- **F5 — Concordance failure.** The adopted PRD and `docs/DIRECTIVE.md` §1
  come to say incompatible things about what the root product is, without a
  recorded superseding act on one of them. *(Falsifies the claim that the
  self-application is* normative *rather than parallel.)*
- **F6 — Label decay.** A requirement's provenance label changes without a
  superseding instrument, or a PROPOSED item is relied upon as though
  adopted. *(Falsifies the claim that the product applies its own epistemic
  discipline — K-PROV-1, K-CLAIM-1 — to itself.)*

**[CLARIFIED]** F1–F3 test the *containment* of self-application; F4–F6 test
its *fidelity*. Neither set is a completeness claim: they are the conditions
whose observation would, on the cited sources, trigger rollback consideration
(packet §8) or amendment.

---

## 7. Non-goals

### 7.1 Restated from the ruled D-GOV-21 packet §4 (lines 130–145)

**[TRANSCRIBED]** These remain exactly as they were and constrain this PRD:

1. **No change to the public-export boundary.** Root `execution/` is not in
   the export allowlist and no record here adds it.
2. **No extension of the root working-root exception** to any `projects/*` or
   `domains/*` working root, nor to the desktop harness's user-selected
   working folders.
3. **No waiver of the decomposition pipeline.** `PKG-*`/`DEL-*` at root come
   only from an accepted root decomposition; nothing authorizes inventing
   packages from discussion.
4. **No blanket authority for future root-structure changes.** The D-GOV-21
   supersessions are closed-form (packet §3).
5. **No change to K-AUTH-1, K-AUTH-2, K-BIND-1, K-GATE-1, K-SEAL-1, or any
   invariant or clause not named in packet §3.** Ratification mechanics,
   human gates, lifecycle states, and the decision-record system are
   untouched.

### 7.2 Non-goals of this PRD specifically

| # | Non-goal | Label | Grounding |
|---|---|---|---|
| NG-1 | This document does not adopt, accept, or ratify anything, including itself. | TRANSCRIBED | K-AUTH-1; D-GOV-21 §Status note (lines 34–36); packet §11 |
| NG-2 | It does not settle the genus wording, the accountability model, the adoption instrument and concordance map, or the adopted PRD's placement. | TRANSCRIBED | D-GOV-21 packet §11 (lines 336–349); standing workplan Lane A (lines 105–119) |
| NG-3 | It creates no `PKG-*`/`DEL-*` structure anywhere and authorizes no materialization. | TRANSCRIBED | packet §5.3 gate, §10 (line 325); standing workplan (line 188) |
| NG-4 | It changes no instruction-surface file. Any instruction-surface change is an M2 governance tranche requiring independent owner authorization. | TRANSCRIBED | `docs/SPEC.md` §0.2.2 (line 52, second clause) and §0.2.1 (line 44); D-GOV-21 M2 |
| NG-5 | It does not re-litigate the philosophical framework or the thesis. Those are governed by D-GOV-19 and its exclusions; `docs/thesis/` is cited as basis and stands at CITED/REVIEWED, **not** AUTHENTICATED. | TRANSCRIBED | D-GOV-19 §Exclusions and limits; `docs/thesis/README.md` §Warrant Status |
| NG-6 | It is not a roadmap. The governed roadmap surface remains `docs/PLAN.md`; planning documents are not a substitute for a superseding record. | TRANSCRIBED | `docs/DIRECTIVE.md` §Authority chain (line 7); `_REGISTER.md` §Terminal-artifact rule (lines 192–195) |
| NG-7 | It does not resolve the conflicts in §11. Surfacing them is the act; ruling on them is the owner's. | TRANSCRIBED | K-CONFLICT-1 |

---

## 8. Relationship to variants

| Variant | Relationship to the root product | Label | Citation |
|---|---|---|---|
| **`projects/*` working roots** | Separate working roots served by the one shared instruction root. They may extend the invariant catalog in their own `docs/CONTRACT.md` (e.g. app-dev's runtime `K-PATH-*`/`K-ROOT-*` families, OpenPipeStress's `OPS-K-*` fork) but **MUST NOT weaken** a framework invariant. They do not inherit the root exception. Their `AGENTS.md` may overlay or specialize but must not weaken framework governance. | TRANSCRIBED | `docs/DIRECTIVE.md` §2.6 (lines 201–204); `docs/CONTRACT.md` §1 (line 11), **K-AGENTS-1**; D-GOV-21 packet §4 |
| **`domains/*` working roots** | Private/manual domain packs and corpus shells; also separate working roots. Domain engines own authoritative domain truth under K-DOMAIN-1..4 and are exempt from the rebuildable-cache rule per the D-GOV-01 scope note. | TRANSCRIBED | `docs/CONTRACT.md` §1.12 and its note (line 142); `README.md` §Private Project And Domain Workspaces |
| **Desktop harness** | The same instruction surface packaged as an app bundle (`instruction-root/`) running agents against a **user-selected working folder**. Its working folders are explicitly outside the D-GOV-21 exception. | TRANSCRIBED | `docs/DIRECTIVE.md` §2.6 (lines 201–202); `docs/SPEC.md` §0.2 (line 32), §0.3 `{INSTRUCTION_ROOT}` row; D-GOV-21 packet §4 |
| **Shared runtime (D-GOV-20)** | Root `runtime/` is the generic executable substrate; one opt-in per-user daemon is the exclusive owner of engines, credentials, sessions, delegation, tools, turn locks, interruption, and residency. Its user-data files are operational state, **not** project authority. Registered projects retain checkout-contained authority. | TRANSCRIBED | `AGENTS.md` §Shared Runtime Doctrine (lines 264–277); `docs/DIRECTIVE.md` §7; `docs/CONTRACT.md` §1.13 |
| **Public export (`exports/chirality-app`)** | A derivative publication surface built by an allowlist profile. Allowlist facts at this basis: `ROOT_FILES` = `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CHIRALITY_FRAMEWORK.md`, `PROFESSIONAL_ENGINEERING.md`, `LICENSE.md`; `PUBLIC_ROOT_FILES` maps `README.md` to the profile's `PUBLIC_README.md`; `ROOT_DIRS` = `.github`, `agents`, `skills`, `tools`, `docs`, `init`, `runtime`; exclusions include `.github/workflows/harness-premerge.yml`, `tools/practitioner_harness/BACKLOG.md`, and the prefix `docs/governance_harness/briefs/`. Root `execution/`, `projects/`, `domains/`, `plans/`, `exports/`, and `.archive/` are **not** exported. | TRANSCRIBED | `exports/chirality-app/export_public.py` lines 21–51; `README.md` §Public Export Boundary (lines 172–198); `docs/CONTRACT.md` **K-EXPORT-1** |
| **Export-staging currency** | Public-export staging regeneration is **DEFERRED** as of the D-GOV-21 implementation tranche: root `docs/` is in the allowlist, and the Annex A edits stale the exported copies and manifest hashes. Regenerate from the EffectiveSHA before any subsequent public-export apply; do not apply an export from a pre-D-GOV-21 staging. | TRANSCRIBED | `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` §Derivative-package status (lines 63–71); standing workplan §Closeout (lines 275–280) |

**[CLARIFIED]** The variants are not deployments of a single artifact: they
are different *bindings* of `{WORKING_ROOT}` against one instruction root
(`docs/SPEC.md` §0.3). The root product is distinguished from all of them by
being the only binding where `{WORKING_ROOT}` = `{INSTRUCTION_ROOT}` =
`REPO_ROOT`, which is precisely why it needed a replacement containment
contract (packet §5.1, lines 149–167).

---

## 9. Reserved owner decisions (decision slate)

These four decisions were **expressly not made** by D-GOV-21 and were routed
to the PRD development/adoption track (packet §11, lines 336–349). The
standing workplan requires this lane to surface each with options and
consequences and to **settle none** (Lane A, lines 105–119). Where an agent
recommendation is offered below it is labeled as such, and the decision
remains reserved to the owner.

### 9.1 RD-1 — Genus wording of the root product statement

**The question.** Which noun phrase names what kind of thing Chirality Root
is, and how is the other live surface brought into concordance?

| Option | Content | Consequences |
|---|---|---|
| **RD-1-A** | Retain `docs/DIRECTIVE.md` §1's ratified genus — "a governed, filesystem-native agent operating system for deliverable-heavy professional work" — and reword `README.md` as the derivative surface. | No amendment to ratified doctrine is required; `README.md` is already classified for propagation-style rewording (packet §3b, line 125). Cost: the genus arguably under-describes a tree that also holds a governance layer, tool layer, domain applications, project records, and a runtime (`README.md` lines 3–5). |
| **RD-1-B** | Adopt `README.md`'s genus — "a governed application environment for agent-assisted, deliverable-heavy professional work" — and amend `docs/DIRECTIVE.md` §1 accordingly. | Requires a superseding amendment to a RATIFIED clause, i.e. an act of the D-GOV-21 kind (enumerated supersession + exact candidate prose + exact-prose gate). Also touches `docs/SPEC.md`/`docs/TYPES.md`/`AGENTS.md` prose that leans on "operating system", plus the public export (root `docs/` is exported). |
| **RD-1-C** | Two-level formulation: one genus plus an explicit differentia, stated once and propagated to every surface that names the product. | Removes the ambiguity permanently and can subsume both current readings. Cost: it is *new prose*, so it requires exact-prose acceptance and a propagation tranche, and it is the largest single doctrine edit of the three options. |
| **RD-1-D** | Defer: adopt the PRD with the conflict recorded and both variants cited, ruling later. | Cheapest now. Cost: the PRD's own §3 remains unresolved on the product's genus, and F5 (concordance failure) stays live. |

**Agent recommendation:** none between A, B, and C — the genus is an identity
judgment reserved to the owner, and recommending one would settle what the
brief and packet §11 reserve. The recommendation is limited to a mechanical
point: **whichever option is chosen, the losing surface must be brought into
concordance in the same tranche**, because leaving both live is the condition
that F5 names. *(Labeled agent recommendation; decision expressly reserved.)*

### 9.2 RD-2 — Accountability model

**The question.** Is accountability scoped to *one accountable human per
consequential act*, or to *one owner per root*? Included in this decision:
**who may amend `docs/governance_harness/human_actors.md`**.

**Current state [TRANSCRIBED].** `human_actors.md` is ACTIVE, owner-curated,
with exactly one actor: "Ryan Tufts — Owner / sole maintainer; sole author of
binding rulings (K-AUTH-1)" (line 20). Its maintenance clause reads:
"owner-curated. Additions and removals are owner edits, published by CHANGE.
Do not extend this list programmatically" (lines 13–14). Identity-dependent
checks REFUSE (exit 2) on absence or mismatch (D-GOV-04). Packet §16 records
that the "apex" characterization of `human_actors.md` was deliberately
removed from packet §11.2 during review (line 416) — the file is an identity
allowlist, not an authority apex.

| Option | Content | Consequences |
|---|---|---|
| **RD-2-A** | **One accountable human per consequential act.** Accountability attaches to acts; the allowlist may hold several actors; each ruling names its accountable human. | Generalizes to more than one practitioner and to delegated professional responsibility across working roots. Matches the K-AUTH-1/K-AUTH-2 shape (approvals are acts bound to SHAs). Cost: needs an amendment policy for the allowlist, a per-act attribution discipline, and possibly a conflict rule when two actors touch one tranche. |
| **RD-2-B** | **One owner per root.** Accountability attaches to the root; the root has exactly one accountable owner who authors all binding rulings for it. | Matches the current live state exactly; no new machinery. Cost: couples the product's accountability model to a single person; provides no expressed path for a second practitioner, for succession, or for a working root whose accountable professional differs from the root owner. |
| **RD-2-C** | Both, layered: per-act accountability as the general rule; one owner per root as the current instantiation, recorded as a fact rather than a doctrine. | Keeps the general rule truthful and the present state simple. Cost: two things to keep concordant; the sub-decision below still has to be answered. |

**Sub-decision — who may amend `human_actors.md`:**

| Option | Content | Consequences |
|---|---|---|
| **RD-2-i** | Owner only (status quo, TRANSCRIBED from the file's maintenance clause). | No change. Single point of failure for succession. |
| **RD-2-ii** | Owner, plus a named delegate authorized by a recorded superseding instrument. | Adds a succession path. Requires the delegation instrument to be specified and itself gated. |
| **RD-2-iii** | Any actor already in the allowlist, under a two-party rule (two recorded actors for any addition or removal). | Removes the single point of failure. Meaningless while the list has one entry; needs a bootstrap rule for the second entry. |

**Agent recommendation:** RD-2-C with RD-2-i as the present instantiation —
the general rule and the current fact are not in tension (one owner per root
is the degenerate case of one accountable human per act when there is one
human), and stating both avoids writing a single-person assumption into the
product's requirements. This is an **agent recommendation only**; the
decision, including the sub-decision, is expressly reserved to the owner.

### 9.3 RD-3 — Adoption instrument and the required concordance map

**The question.** On what instrument is the root PRD adopted, and in what
form is the concordance map against `docs/DIRECTIVE.md` §1 produced? Packet
§11 item 3 reserves both.

| Option | Instrument | Consequences |
|---|---|---|
| **RD-3-A** | A **D-GOV-\* decision record** using the exact-candidate-SHA pattern (commit exact PRD bytes → `AcceptedCandidateSHA` → verbatim owner ruling in a fence → publish record → `EffectiveSHA`). | Reuses machinery already ruled and exercised three times (D-GOV-18, D-GOV-19, D-GOV-21). Inherits register visibility, self-check detection, and SHA binding for free. Cost: the D-GOV family becomes the home of a product-requirements act as well as governance acts. |
| **RD-3-B** | A **dedicated PRD adoption record class** (e.g. an `ADOPTION` instrument beside the PRD). | Keeps product-requirements acts distinct from governance decisions. Cost: new record convention, new validator surface, no existing detection; the harness would not recognize it without work. |
| **RD-3-C** | Ratify through the **corpus-ratification pattern** used for root `docs/` (D-GOV-09 style: an owner ratification act over a document set). | Familiar and simple. Cost: conflates a requirements act with governance ratification, and would imply the PRD joins the ratified governance corpus — which prejudges **RD-4**. |

**Concordance-map form (sub-decision):**

| Option | Form | Consequences |
|---|---|---|
| **RD-3-x** | One-directional table: each PRD requirement → the `docs/DIRECTIVE.md` §1 clause it derives from or extends. | Simple; shows derivation. Does not expose DIRECTIVE §1 content that the PRD failed to carry. |
| **RD-3-y** | Bidirectional coverage matrix: PRD → DIRECTIVE §1 **and** DIRECTIVE §1 → PRD, with uncovered items marked `TBD` (K-INVENT-1 discipline). | Exposes both drift directions; produces the artifact F5 would be checked against. Cost: more work at adoption. |

**Agent recommendation:** RD-3-A with RD-3-y — the exact-candidate pattern is
ruled, exercised, and mechanically detected, and the bidirectional matrix is
the only form that can later falsify F5. **Agent recommendation only;
decision expressly reserved.**

### 9.4 RD-4 — Placement of the adopted PRD relative to the public-export boundary

**The question.** Where does the *adopted* PRD live? Root `docs/` is in the
export allowlist (`ROOT_DIRS`, `export_public.py` line 39); root `execution/`
is not. Packet §11 item 4 records this as a **publication decision**.

| Option | Placement | Consequences |
|---|---|---|
| **RD-4-A** | Root `docs/` (exported). | The PRD becomes public through the existing allowlist — **no boundary change**, so packet §4 item 1 is not offended. It joins the instruction surface, so every future amendment becomes an M2 governance tranche with a tranche manifest and M6 notices, and each amendment triggers export-manifest regeneration (R-D-12). Doctrinally coherent: the PRD is normative basis and normative basis lives in `docs/`. |
| **RD-4-B** | Root `execution/` (not exported). | Stays private. Consistent with D-GOV-21's framing of root `execution/` as the root product's working root. Amendments are working-root acts, not instruction-surface acts — lighter process. Cost: a normative artifact sits on a surface whose own doctrine says coordination surfaces "carry no authority merely because they exist"; readers must be told explicitly that this one is different. |
| **RD-4-C** | Root `docs/` **with an export exclusion** (the profile already supports `EXCLUDED_PUBLIC_PATHS` and `EXCLUDED_PUBLIC_PREFIXES`, lines 44–51 — `docs/governance_harness/briefs/` is the precedent). | Doctrinal home plus privacy. Cost: edits the export profile — arguably not a *boundary* change in the packet §4 sense (the allowlist is unchanged; an exclusion narrows what is published), but it is a publication-policy change and should be ruled as one, not assumed. |
| **RD-4-D** | Split: adopted PRD in root `docs/`; candidates, evidence, and working revisions in root `execution/`. | Matches the existing candidate/ruled split used by `_PROPOSALS/` vs `_DECISIONS/`. Cost: two homes to keep concordant; the pointer discipline must be explicit. |

**Agent recommendation:** none between A, C, and D — this is a publication
judgment with commercial and disclosure dimensions the agent has no basis to
weigh. The recommendation is limited to two mechanical observations, offered
as **agent recommendation only**: (i) RD-4-A publishes through the existing
allowlist and therefore requires no boundary change, whereas RD-4-C does
require an export-profile edit; and (ii) whichever is chosen, the choice
determines whether future PRD amendments are M2 instruction-surface tranches
(A, C, D) or working-root acts (B) — that process consequence should be
decided deliberately, not inherited. **Decision expressly reserved.**

---

## 10. Adoption mechanics

**[TRANSCRIBED]** Adoption is a separate future owner act on a separate
instrument (D-GOV-21 packet §11, §6 step 7; standing workplan §Gated
downstream item 1). This lane's terminal act is presenting the candidate; the
lane stops at owner review and at each of the four reserved decisions
(standing workplan §Stop state, lines 242–248).

**[TRANSCRIBED]** What adoption requires, on the cited sources:

1. **Exact bytes.** Adoption binds to the exact committed bytes of the PRD at
   a named SHA, on the D-GOV-18/19/21 exact-candidate pattern — the specific
   instrument is **RD-3** and is not settled here (packet §14; §11 item 3).
2. **Concordance map against `docs/DIRECTIVE.md` §1** is required at adoption
   (packet §11 item 3). Its form is the RD-3 sub-decision.
3. **Owner ruling recorded verbatim**, attributed to an actor matching
   `docs/governance_harness/human_actors.md` (D-GOV-04; refuse rather than
   guess), and SHA-bound at publication (K-AUTH-2).
4. **Resolution of RD-1 through RD-4** (standing workplan Lane A, lines
   105–119) — the workplan requires the lane to surface them; adoption is
   where they are answered.
5. **No agent act substitutes for any of the above** (K-AUTH-1). Silence,
   file creation, validation, commit, and Git transport are not approval.

**[TRANSCRIBED]** Until an adoption act occurs, **every PROPOSED item in this
document is inert** — R-D-15, R-D-16, R-D-17, and falsifiers F4, F5, F6. The
TRANSCRIBED requirements remain in force regardless, because their authority
is their own source and not this document.

**[TRANSCRIBED]** What adoption would *not* do: it would not materialize
anything under root `execution/` (that is packet §6 step 9 behind the §5.3
gate), would not create a root decomposition (step 8), and would not change
the public-export boundary (packet §4).

---

## 11. Conflicts and open items surfaced (not resolved)

Per K-CONFLICT-1 these are recorded with pointers to the conflicting sources
and a `HumanRuling = TBD` disposition. None is resolved here.

| # | Conflict / open item | Sources | Disposition |
|---|---|---|---|
| **C-1** | **Genus wording.** `docs/DIRECTIVE.md` §1 line 13 names an "agent operating system"; `README.md` line 3 names an "application environment". | `docs/DIRECTIVE.md` §1 (RATIFIED); `README.md` (non-binding/derivative per packet §3b line 125) | Routed to **RD-1**. `HumanRuling = TBD` |
| **C-2** | **CONTRACT invariant-index arithmetic.** `docs/CONTRACT.md` §1 line 19 states "**27 stable invariants** across 12 subsections", and the index table lists 27 rows ending at K-DOMAIN-4. §1.13 (Shared Runtime, lines 144–154) then defines seven further invariants — K-RUNTIME-1, K-CONTROL-1, K-PROJECT-1, K-STORE-2, K-RESIDENCY-1, K-ROLE-2, K-EXPORT-1 — that are absent from the index. The live catalog therefore holds 34 invariants across 13 subsections. §2's enforcement map *does* reference K-ROLE-2 and K-EXPORT-1. | `docs/CONTRACT.md` lines 19–49 vs. lines 144–154 and 169–178 | **New find**, not previously recorded in the sources read for this run. Not amended here: `docs/CONTRACT.md` is ratified and root `docs/` is instruction surface (NG-4). Recommend routing as an M2 correction tranche. `HumanRuling = TBD` |
| **C-3** | **Export-profile description vs. profile code.** `README.md` §Public Export Boundary (lines 174–183) lists the export profile as root framing files, `.github/`, `AGENTS.md`, `agents/`, `skills/`, `tools/`, `docs/`, `init/` — omitting `runtime/`, which `export_public.py` `ROOT_DIRS` (line 41) includes. | `README.md` lines 174–183 vs. `exports/chirality-app/export_public.py` lines 34–42 | **New find.** Per K-AGENTS-1's live-registry principle and `README.md`'s own line 148, the live profile governs and the narrative is stale. Routed as a propagation item. `HumanRuling = TBD` |
| **C-4** | **Historical-note date.** The sealed brief for this run states in-repo history begins 2026-02-18; the repository's git history begins 2026-05-18 (`7bee9ae41`, "Initial migrated Chirality repository"), and no in-repo file asserting 2026-02-18 was found. | Sealed brief §Owner-declared framing item 4 vs. git history at `main@7ac718c7e` | §3.1 ID-5 records the verified git fact; the brief's date is surfaced, not adopted and not silently corrected. Owner confirms or corrects at adoption. `HumanRuling = TBD` |
| **C-5** | **K-WRITE-2 explanatory gloss (already-recorded debt, restated for completeness).** The gloss inside the K-WRITE-2 entry — "This confines a task's effects to its working root" — overstates the invariant's mechanical reach in a monorepo, where working-root containment has depended on narrower accepted scopes. | `docs/CONTRACT.md` line 124; D-GOV-21 packet §5.1 (lines 164–167); standing workplan §Parked lanes (lines 200–204) | Already routed as independent reconciliation debt (packet §7 class b). Not new; restated because it bears directly on R-N-12. `HumanRuling = TBD` |
| **C-6** | **Packet self-reference WARN (known, accepted, non-gating).** Self-check reports `UNRESOLVED_SOURCE_REF` at `PACKET.md:356` — the packet's declined option O-B names `projects/chirality-root/`, which deliberately does not exist. | `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` (lines 83–87); standing workplan Step 0 item 7 | Known accepted finding. The packet is the exact ruled candidate and must not be amended. No action. |

**Deliberately not included in this candidate [CLARIFIED]:**

- **No requirement numbering claim of completeness.** §5 enumerates the
  requirements this inquiry could ground in the declared read scope. It is
  not asserted to be exhaustive (K-CLAIM-1).
- **No acceptance criteria, verification methods, or priority ranking.**
  Those belong to decomposition and the Scope-of-Work contract (D-GOV-15,
  D-GOV-16), which run downstream of adoption; producing them here would
  prejudge packet §6 step 8.
- **No package or deliverable proposal.** Prohibited by packet §4 and NG-3.

---

## 12. Document control

| Field | Value |
|---|---|
| Status | `CANDIDATE — NOT ADOPTED` |
| Binds | Nothing (K-AUTH-1) |
| Accepted basis | `main@7ac718c7e` |
| Governing decision | D-GOV-21 (RULED 2026-07-25); AcceptedCandidateSHA `c038c493e871c95871823281b45890ba9404624b`; PublicationSHA `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`; EffectiveSHA `ee42157290618e3f84be0e0b651c041387ad6ee0` |
| Authorizing effect | D-GOV-21 effect 5 (PRD-development basis) |
| Run | `ROOT-PRD-LANE-A-20260725` |
| Standing workplan | `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`, Lane A |
| Reserved decisions | RD-1, RD-2 (+ sub-decision), RD-3 (+ sub-decision), RD-4 — all unresolved |
| Provenance counts | 78 labeled requirements: **67 TRANSCRIBED**, **4 OWNER_DECLARED**, **4 CLARIFIED**, **3 PROPOSED**; plus 3 PROPOSED falsifiers (F4–F6) and 3 TRANSCRIBED falsifiers (F1–F3) |
| PROPOSED inventory | R-D-15, R-D-16, R-D-17, F4, F5, F6 — inert unless adopted |
| Next act | Owner review. Adoption, if any, is a separate instrument (RD-3). |
