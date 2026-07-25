# Product Requirements Document — Chirality Root (the root product)

> **Status: `CANDIDATE — NOT ADOPTED`. Revision 2.**
>
> This document **binds nothing** (`docs/CONTRACT.md` §1.2, **K-AUTH-1**: only
> humans author binding approval records; no agent may certify, approve, sign,
> seal, or issue work for reliance). Existence, validation, commit, and Git
> transport are **not** approval.
>
> **Adoption is a separate future owner act on a separate instrument**
> (D-GOV-21 packet §11 item 3; §6 step 7; standing workplan §Gated downstream
> item 1). Nothing here is adopted, accepted, ratified, or in force by virtue
> of appearing in this file.
>
> **Accepted basis:** `main@7ac718c7e`. **Run:** `ROOT-PRD-LANE-A-20260725`
> (Lane A; D-GOV-21 packet §6 step 5, on the basis of D-GOV-21 effect 5).
> **Revision history:** Rev 1 committed at `f15d51277` (PR #340); Rev 2
> incorporates the owner-routed independent adversarial review of 2026-07-25
> under brief amendment 1
> (`execution/_Coordination/AgentRuns/ROOT-PRD-LANE-A-20260725/briefs/PRD-AUTHOR-BRIEF-AMENDMENT-1.md`;
> review verbatim in the same run's `reviews/ADVERSARIAL-REVIEW-1.md`).
> **Authored by:** an ephemeral bounded Agent 2 generalist under sealed brief,
> dispatched by `HELP_HUMAN` (Agent 0). Agent authorship confers no authority.
> **Companion:** `execution/_Coordination/PRD_CANDIDATE_2026-07-25_concordance_annex.md`
> — a **derivative package**, regenerable and never itself adopted (§10.1).
> **Adoption, if it occurs, binds the exact bytes of this file only.**
> **Placement** of the adopted PRD is reserved (**RD-4**); this candidate sits
> on a non-exported coordination surface deliberately.
> **Date:** 2026-07-25

---

## Provenance key

Every requirement, objective, and identity claim carries exactly one label.

| Label | Meaning | Reliance |
|---|---|---|
| **TRANSCRIBED** | Accepted or ratified doctrine, cited to its governing clause and verified against the live file at the accepted basis. | In force now, because its source is in force — not because this document repeats it |
| **OWNER_DECLARED** | Owner-endorsed framing **as transcribed or synthesized by Agent 0 in-session**. Exact wording is subject to owner confirmation or correction at adoption. **Not claimed verbatim unless quote-fenced.** | Not in force as doctrine; awaits owner confirmation |
| **CLARIFIED** | An interpretation of accepted truth produced by the 2026-07-25 root-PRD inquiry (Agent 0 plus independent second-agent review, owner-mediated). Interpretation, not new authority. | Reading aid; the cited source governs |
| **PROPOSED** | A new commitment taking effect **only if this PRD is adopted**. Inert until then. | None |

Quote fences (`>`) appear **only** around text warranted as verbatim, with its
record cited. Synthesized owner framing is presented as ordinary prose.

---

## 1. Product identity and genus

### 1.1 What Chirality Root is

**ID-1 — Dual nature. [OWNER_DECLARED]** The root product is both an operating
system for governed professional knowledge work and a normative, self-applying
instance of a generative development pattern: it develops itself under the
same governance it prescribes. *(Agent 0 synthesis of in-session owner framing
carried through a context compaction; not warranted verbatim. Owner confirms
or corrects at adoption.)*

**ID-1a — The self-application half is independently accepted. [TRANSCRIBED]**
D-GOV-21 (RULED 2026-07-25) makes the repository root both the shared
instruction root and the working root for development of the root product
(D-GOV-21 §Effects item 1; packet §2 item 1; `docs/DIRECTIVE.md` §2.6 as
amended). The owner ruling of record, verbatim from the decision record's
ruling fence:

> I rule APPROVED for O-A against candidate SHA c038c493e871c95871823281b45890ba9404624b

AcceptedCandidateSHA `c038c493e871c95871823281b45890ba9404624b`;
PublicationSHA `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`;
EffectiveSHA `ee42157290618e3f84be0e0b651c041387ad6ee0`. The owner's
*characterization* of this as a "generative development pattern" remains
OWNER_DECLARED.

**ID-2 — Human judgment is the governing hinge. [OWNER_DECLARED]** Only humans
author binding approvals; agent capability never confers authority; the
permanent accountability gap is why the hinge cannot be automated away.
*(Agent 0 synthesis; not verbatim.)* Supporting accepted doctrine
**[TRANSCRIBED]**: K-AUTH-1 (`docs/CONTRACT.md` §1.2); `AGENTS.md` §Delegation
and Entry Rules ("Delegation never implies capability inheritance … A child's
capability does not become a parent capability"); D-GOV-19 ruled proposition 5
(the permanent non-identity between externalizable information and accountable
knowing); D-GOV-17 (capability never confers authority regardless of steering).

**ID-3 — Historical lineage (owner testimony). [OWNER_DECLARED]** The owner
attests roughly three years of prior development lineage preceding this
repository. No in-repo source states this.

**ID-4 — In-repo history (git fact). [TRANSCRIBED]** This repository's git
history begins at commit `7bee9ae41`, "Initial migrated Chirality repository",
2026-05-18; no commit predates that month. `docs/DIRECTIVE.md` §2.2 ("Git Is
the Event Store") makes git the development record of record. ID-3 and ID-4
are stated separately and are **not** blended. See conflict **C-3**.

### 1.2 Genus wording — reserved, not settled

Two accepted surfaces name the product with different genera. Both are
transcribed; **neither is selected here**. The choice is **RD-1** (§9.1).

- **Variant A [TRANSCRIBED]** — `docs/DIRECTIVE.md` §1: "a governed,
  filesystem-native agent operating system for deliverable-heavy professional
  work." In the RATIFIED root governance corpus (D-GOV-09, owner ratification
  2026-07-11).
- **Variant B [TRANSCRIBED]** — `README.md`: "a governed application
  environment for agent-assisted, deliverable-heavy professional work."
  `README.md` is classified a **non-binding / derivative surface** by D-GOV-21
  packet §3b.

**[CLARIFIED]** These name different kinds of thing, and the tree's contents
are consistent with both readings. Per K-CONFLICT-1 the disagreement is
surfaced with both citations and routed to RD-1 (which now carries a concrete
reviewer-recommended third formulation); it is **not** harmonized here.

### 1.3 What the root product structurally is not

**[TRANSCRIBED]** It holds no professional authority. Agent outputs are drafts
and structured assistance (`docs/DIRECTIVE.md` §3.1); "Agent outputs carry no
professional authority" (§3.4); a green validation is structural evidence only
and never certification (K-DOMAIN-4; D-GOV-02 — BLOCK never means globally
proven safe or unsafe).

---

## 2. Problem and human users

### 2.1 The problem

**[TRANSCRIBED]** `docs/DIRECTIVE.md` §1 states three purposes: accelerate
deliverable-heavy work by structuring agent workflows around production
deliverables and decomposed knowledge; make agentic work auditable and
controllable so outputs can be relied upon in professional, regulated, and
high-stakes contexts; and keep humans in charge at every decision gate while
agents handle drafting, extracting, reconciling, decomposing, and organizing.

**[TRANSCRIBED]** The diagnosis (§2, epistemology): the problem "is not that
they produce bad outputs — it is that bad outputs are indistinguishable from
good ones by inspection." The response is to make epistemic status transparent
and auditable rather than to make the model more reliable. The load-bearing
architectural commitment (§1): "if the filesystem is the database,
architecture is a state-and-authority specification, not a service mesh."

### 2.2 Applicability

**[TRANSCRIBED, corrected in Rev 2]** Chirality Root is for **governed
professional knowledge work generally**. The clause at `docs/DIRECTIVE.md` §3
("This section applies when the system is used in environments where
deliverables are safety-significant, contractually binding, subject to
codes/standards, or produced under professional responsibility") states the
**activation boundary of the professional-responsibility model** — the point
at which §3's additional provisions become load-bearing — **not** the
applicability boundary of the product. Rev 1 conflated the two.

### 2.3 Users, actors, and consuming contexts

Agents and working roots are **not users** in the product sense. The four
strata below are distinguished per the adversarial review.

| Stratum | Who / what | Notes | Label |
|---|---|---|---|
| **Primary human users** | Accountable practitioners directing governed work — the people who rule, approve, adjudicate conflicts, accept residual risk, and issue for reliance. | The only actors who can perform the acts K-AUTH-1 reserves. Presently one person is registered as a permitted author of binding governance records (`docs/governance_harness/human_actors.md`). | CLARIFIED |
| **Secondary human users** | Reviewers, auditors, maintainers, and people assessing whether work may be relied upon. | They consume the evidence trail without directing the work. Their needs drive the epistemic architecture (`docs/DIRECTIVE.md` §2). | CLARIFIED |
| **System actors** (not users) | Agent 0 / Agent 1 / Agent 2 instances; deterministic tools; the runtime daemon and its clients. | `agent = LLM + instructions + declared files/context + tools + permissions` (`AGENTS.md`) — "an operational definition, not a claim of personhood or professional responsibility". They execute within permission boundaries and never hold authority. | TRANSCRIBED |
| **Consuming contexts** (not users) | `projects/*` and `domains/*` working roots; desktop-harness user-selected folders; other situated working roots; the public export. | They bind `{WORKING_ROOT}` against the one instruction root. They may extend the invariant catalog but MUST NOT weaken it (`docs/CONTRACT.md` §1). | TRANSCRIBED |

**Whom v1 is *for* is reserved as RD-5** (§9.5) — present owner-practitioner,
accountable professional practitioners generally, or multi-practitioner
organizations. **RD-2 does not answer this**: RD-2 concerns governance
jurisdiction and act-level accountability, not product user scope.

---

## 3. Objectives and v1 success conditions

**Why this section exists.** `docs/DECOMPOSITION_STANDARD.md` requires a
conforming decomposition to derive **objectives from its source** (invariant
I7; Completeness requirements — "Objectives derived"). If this PRD becomes
that source, it must state objectives, or decomposition will have to infer the
product's direction from constitutional statements.

**v1 boundary. [PROPOSED]** Chirality Root **v1** is the state in which
(a) the D-GOV-21 §6 sequence has closed through step 9 — root packages
materialized from an accepted root decomposition with G0–G4 registered and
passing; (b) the root product's own governed loop has carried at least one
complete deliverable stream end to end; and (c) at least one situated working
root operates on the same instruction basis with a recorded convergence path.
**Completeness is claimed only for this boundary** — not for every future
Chirality possibility. If the owner defines v1 differently at adoption, the
success conditions below re-scope accordingly.

All seven objectives are **PROPOSED**: they are new commitments, which is the
point. Detailed acceptance tests remain downstream (D-GOV-15 / D-GOV-16
machinery); what success *means* lives here.

| # | Objective | v1 success condition (testable) |
|---|---|---|
| **OBJ-1** | **Coherent and discoverable normative authority.** A reader can determine what governs, from the repository alone. | For every governance surface in the instruction root, a reader can determine without asking a person: which document is authoritative for a given question, whether it is ratified, and what superseded it. No ratified clause has an unrecorded conflicting live variant. *(C-1 is the current open instance; C-2 is a current index defect.)* |
| **OBJ-2** | **Governed production of professional knowledge work.** The product actually produces deliverables under its own governance. | At least one complete deliverable stream runs end to end through the pipeline — decomposition → package/deliverable → checking → issuance — with every gate human-performed and every governed claim carrying provenance sufficient for a reviewer to determine reliance. Demonstrated at root and in at least one situated working root. |
| **OBJ-3** | **The human iteration and evaluation loop closes.** Humans can evaluate and redirect on evidence. | For any accepted change, a human can retrieve from files alone, in bounded time: the evidence that informed it, the ruling that accepted it, and the state it changed. Verified as a retrieval exercise over a sample of accepted tranches. |
| **OBJ-4** | **Safe self-application without self-authorization.** The root develops itself without granting itself authority. | Through v1: falsifiers F1–F3 unobserved; every root capability consumed by root development was accepted through the basis or an explicitly accepted predecessor; G0–G4 registered and passing at every materialization. |
| **OBJ-5** | **Situated specialization with governed convergence.** Variants specialize; useful patterns come back lawfully. | At least one pattern originating in a situated working root is promoted to root through the developmental machinery with its evidence linkage intact, and no variant change reaches root by any other path. |
| **OBJ-6** | **Coordination remains intelligible as concurrent activity grows.** Concurrency does not outrun legibility. | At any point in time the set of active runs, their declared write ownership, their dependencies, and their pending gates is reconstructible from `_Coordination/` state alone. Concurrent sibling write targets are disjoint or serialized. No run's effect is discoverable only from chat history. |
| **OBJ-7** | **File-native continuity and recoverability.** Nothing load-bearing lives outside the checkout. | The full governed state — decisions, approvals, scope, evidence, and each loop's current position — survives loss of every non-file substrate (chat context, model memory, daemon state, local caches) and is recoverable from the checkout alone. |

**[CLARIFIED]** OBJ-1 through OBJ-7 are objectives of the *product*, not of any
single tranche. They are the intended source for the objective derivation
that `docs/DECOMPOSITION_STANDARD.md` I7 requires; unmapped objectives at
decomposition time are surfaced as open issues, never silently dropped.

---

## 4. The four functional categories and their human-governed loop

### 4.1 The categories

**[OWNER_DECLARED]** The root product is constituted by four categories
*(Agent 0 synthesis of in-session owner framing; not verbatim)*:

| Category | What it is |
|---|---|
| **Normative basis** | The ratified governance corpus and invariants |
| **Operative product** | The instruction surface, agents, skills, tools, harness, and runtime that do work |
| **Developmental machinery** | The governance harness, decision records, loops, and guards by which the product changes itself |
| **Evidence** | Receipts, run records, snapshots, audits — the record that makes reliance answerable |

### 4.2 The generative loop

**[OWNER_DECLARED]** The categories are related by a loop, not a partition
*(Agent 0 synthesis; not verbatim)*:

```text
normative basis        ──constrains──▶  operative work
operative work         ──produces────▶  artifacts and evidence
evidence               ──informs─────▶  human evaluation
developmental machinery──produces────▶  candidate changes + iteration evidence
human judgment         ──accepts / rejects / redirects──▶
accepted acts          ──change──────▶  normative or operative state ──▶ (loop)
```

The hinge is human judgment (ID-2): the loop has no closing step that an agent
can perform.

### 4.3 What the categories are and are not

**[CLARIFIED]**

- They classify **functions and authority relationships**, not filesystem
  buckets.
- They are **non-exclusive**. One artifact may participate in several.
  `AGENTS.md` is normative basis (K-AGENTS-1 makes it an authoritative
  governance surface), operative product (it is the live index agents execute
  against), and — through its change-notice rule — developmental machinery. A
  decision record is developmental machinery and evidence, and its ruling
  becomes normative basis.
- They **do not prescribe four packages.** Nothing in this PRD determines the
  decomposition's partition; that is `docs/DECOMPOSITION_STANDARD.md` work at
  a later, human-gated stage. See D-15 for the only coverage obligation this
  PRD proposes.

---

## 5. Stable product requirements

**Registry discipline (anti-rot).** This section states **stable product
commitments** and incorporates **dynamic registries by reference**. It cites
registries, not their members: the invariant catalog (`docs/CONTRACT.md` §1),
the live agent index (`AGENTS.md`), the live skill registry
(`skills/README.md` plus `skills/*/SKILL.md`), the tool registry
(`tools/REGISTRY.md`), and the export profile
(`exports/chirality-app/export_public.py`). Where live registry and narrative
disagree, **the live registry governs and the discrepancy is surfaced**
(K-AGENTS-1). The full transcription inventory — every clause, anchor, and
verified line reference behind these commitments — lives in the concordance
annex (§10.1) and is regenerable from it.

### 5.1 Normative basis

| ID | Commitment | Label and source |
|---|---|---|
| **N-1** | Authoritative state is git-tracked plain files. No external database, server state, or configuration holds authoritative truth; rebuildable gitignored projections are permitted and never citable as authority. If a decision is not in a versioned file, it does not exist for purposes of reliance. | TRANSCRIBED — `docs/DIRECTIVE.md` §2.1, §2.2, §5; D-GOV-01 (Option A) |
| **N-2** | The invariant catalog is the binding constraint set the root product must continue to satisfy. **Incorporated by reference**: the catalog governs its own membership; this PRD maintains no parallel list of `K-*` IDs. | TRANSCRIBED — `docs/CONTRACT.md` §1; K-AGENTS-1 live-registry principle |
| **N-3** | Human authority at every consequential gate: only humans author binding approvals; approvals bind to a specific git SHA and are voided by content change; approvals are always binding and only binding; gates are dynamic per project with a stated minimum, and no machine BLOCK on the issuance judgment may be non-overridable. | TRANSCRIBED — K-AUTH-1, K-AUTH-2, K-BIND-1, K-GATE-1; `docs/DIRECTIVE.md` §2.3 |
| **N-4** | Epistemic discipline is architectural, not advisory: mandatory provenance; unknowns become `TBD` rather than guesses; conflicts are surfaced with pointers, never silently resolved; claims are calibrated to their warrant. | TRANSCRIBED — K-PROV-1, K-INVENT-1, K-CONFLICT-1, K-CLAIM-1; `docs/DIRECTIVE.md` §2.4 |
| **N-5** | Write containment is architectural: every agent has an explicit declared write scope; every scope path and write target resolves under the active checkout or the task stops; task outputs to tool roots are immutable snapshots. | TRANSCRIBED — K-WRITE-1, K-WRITE-2, K-SNAP-1; `docs/SPEC.md` §0.2.3 |
| **N-6** | The authority chain is DIRECTIVE (why) → CONTRACT (binding invariants) → SPEC (structures and path anchoring) → TYPES (vocabulary), with `AGENTS.md` and `agents/` as the live instruction surface. Where a lower or candidate document conflicts with ratified governance, ratified governance controls and the conflict is surfaced. | TRANSCRIBED — `docs/DIRECTIVE.md` §Authority chain |
| **N-7** | The four pillars — ontology, epistemology, praxiology, axiology — are the system's accountability ontology; ontology, praxiology, and axiology exist to serve the epistemology. | TRANSCRIBED — `docs/DIRECTIVE.md` §2 |
| **N-8** | The professional-responsibility model holds where it activates (§2.2): AI outputs are drafts; the licensed professional retains scope, code selection, hazard acceptance, adjudication, and issuance rights; competence includes tool competence; the hierarchy of authority runs laws → codes → project specifications → verified analysis → professional judgment. | TRANSCRIBED — `docs/DIRECTIVE.md` §3 |
| **N-9** | The normative basis is a **constituent of the product**, not documentation about it: the requirement is that the running system continue to satisfy the invariants, not that it describe them. | CLARIFIED — interpretation of `docs/CONTRACT.md` §2 (every invariant has a live enforcement point) |

### 5.2 Operative product

| ID | Commitment | Label and source |
|---|---|---|
| **O-1** | The shared instruction surface is `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and `init/`. It is release-managed and read-mostly; changing it is a repo-wide governance action, not ordinary working-root execution. | TRANSCRIBED — `docs/DIRECTIVE.md` §2.6; `docs/SPEC.md` §0.2.1; `docs/TYPES.md` §1.4 |
| **O-2** | The product operates through **three layers**, each with a distinct authority boundary: **(a) instruction artifacts** — agent instruction packages, skills, and governance documents carrying semantic authority contracts, constraining behaviour by declared scope; **(b) deterministic tools** — computed, repeatable operations producing facts and findings, *never a substitute for semantic judgment*; **(c) the root `runtime/` executable substrate** — daemon, clients, adapters, sessions, and transport, which executes and carries work but whose **transport never grants project authority** and whose user-data state is operational, not project truth. | TRANSCRIBED — `AGENTS.md` (Tool row; §Shared Runtime Doctrine); `docs/DIRECTIVE.md` §7; `docs/CONTRACT.md` §1.13. *(Rev 2 correction: Rev 1's R-O-20 wrongly denied a third execution substrate.)* |
| **O-3** | The runtime delegation hierarchy is Agent 0 Supervising Architect → Agent 1 Manager → Agent 2 Specialist, with declared entry rules and no delegation below Agent 2; Agent 2 exists in three construction forms. **The live index and role membership are incorporated by reference** to `AGENTS.md`; this PRD enumerates no agents. | TRANSCRIBED — `AGENTS.md`; `docs/DIRECTIVE.md` §2 (praxiology); D-GOV-11, D-GOV-12, D-GOV-13 |
| **O-4** | Capability never confers authority. Delegation implies no capability inheritance; a child's capability never becomes its parent's; every child remains subject to sealed context, gate approval, path containment, enforced read/write scope, and durable evidence. | TRANSCRIBED — `AGENTS.md` §Delegation and Entry Rules; K-SEAL-1, K-GHOST-1; D-GOV-17 |
| **O-5** | Method packs (`skills/`) and deterministic operations (`tools/`) are maintained as **live registries**, and the live registry is authoritative over any narrative list. Membership is incorporated by reference to `skills/README.md` and `tools/REGISTRY.md`. | TRANSCRIBED — `AGENTS.md` §TASK Skill Capabilities; K-AGENTS-1 |
| **O-6** | The path model defines two roots (`REPO_ROOT`, `WORKING_ROOT`), one containment rule, and a closed `{*_ROOT}` token registry; instruction, coordination, and plan files MUST NOT embed machine-absolute paths. | TRANSCRIBED — `docs/SPEC.md` §0.2–§0.3 |
| **O-7** | Governed work is structured as execution instances containing flat packages and deliverables with stable IDs, a canonical lifecycle state file, and human-triaged staleness propagation. | TRANSCRIBED — `docs/SPEC.md` §1, §3; K-HIER-1, K-ID-1, K-STATUS-1, K-STALE-1/2, K-VAL-1 |
| **O-8** | Deliverable-local dependency registers are authoritative. **No central dependency graph is *authoritative*** — but derived and aggregated graphs are lawful coordination state: on-demand read-only aggregation is provided for, and `FULL_GRAPH` dependency mode computes blockers from the declared graph. | TRANSCRIBED — K-DEP-1 (which itself provides for on-demand aggregation), K-DEP-2; `agents/AGENT_PROJECT_SETUP.md` (`FULL_GRAPH` mode). *(Rev 2 correction: Rev 1's R-N-17 overstated this as "no central dependency graph".)* |
| **O-9** | The instruction root is separated from the working root, with **exactly one** governed exception — the root product's working root is the repository root, and root `execution/` is its execution root, **eligible** for `PKG-*`/`DEL-*` only from an accepted root decomposition derived from an adopted PRD and only while the guards pass. The replacement containment contract (mechanisms M1–M7 and guards G0–G4 with the §5.3 gate ordering) is required and **incorporated by reference** to D-GOV-21 §5. | TRANSCRIBED — D-GOV-21 §Effects 1–4; packet §5; `docs/DIRECTIVE.md` §2.6; `docs/SPEC.md` §0.2.2, §1; `docs/TYPES.md` §1.4 |
| **O-10** | The operative product's boundary is exactly the three layers of O-2. There is no fourth execution substrate, and nothing outside those layers holds project authority — which is why an instruction-surface change is a governance act rather than a code change. | CLARIFIED — interpretation of O-1, O-2 and the D-GOV-21 M2 gate |

### 5.3 Developmental machinery

| ID | Commitment | Label and source |
|---|---|---|
| **D-1** | Consequential governance change terminates in a published decision record carrying status, verbatim owner ruling, SHAs, date, framing, accepted basis, and record convention. The register is navigational; the per-decision records govern. | TRANSCRIBED — `docs/governance_harness/_DECISIONS/` (records + `_REGISTER.md`) |
| **D-2** | Corrections to ruled content are **superseding acts, not edits**: a later correction supersedes; amending a ruled candidate would void its accepted SHA. | CLARIFIED — the record-level convention (`RecordConvention: … supersede-never-edit`, D-GOV-21; D-GOV-17's recorded-exception protocol) generalized to a product commitment. *(Rev 2 correction: Rev 1 labelled this TRANSCRIBED; no root-wide rule states the absolute formulation, so the generalization is marked as interpretation.)* |
| **D-3** | Where a proposal contains substantial PROPOSED requirements, the ruling binds to an **exact candidate SHA**: commit the exact candidate, record it, record the owner ruling verbatim in a fence, publish the record, and record the merged implementation commit. Deviation from ruled exact prose returns for exact-prose re-acceptance before merge. | TRANSCRIBED — D-GOV-21 packet §14; D-GOV-18 and D-GOV-19 precedents |
| **D-4** | Attribution of rulings and adoptions matches an owner-curated identity allowlist; identity-dependent checks **refuse rather than guess**. The list is owner-curated and not extended programmatically. | TRANSCRIBED — D-GOV-04; `docs/governance_harness/human_actors.md` |
| **D-5** | Validation is deterministic and severity-typed (BLOCK / REVIEW / WARN / INFO / NOT_APPLICABLE, with exit-code semantics and human-only recorded BLOCK override); "BLOCK" never means globally proven safe or unsafe; and a validator finding may **never** mechanically reject content the owner has ruled — where ruled text trips a validator, the validator is defective. | TRANSCRIBED — D-GOV-02; D-GOV-17; `docs/CONTRACT.md` §1.7 note |
| **D-6** | Phase-crossing work is bound by the governance integration rules — derivative-package, snapshot, handoff-state, closure, sequencing, cycle-resolution, and change-notice routing. **Incorporated by reference** to `AGENTS.md` §Governance Integration Rules. | TRANSCRIBED — `AGENTS.md`; `docs/DIRECTIVE.md` §2.7 |
| **D-7** | Root-product development runs through a governed loop with a session-init contract, a deterministic standing-plan pointer, and an append-only receipts log. **Coordination surfaces carry no authority merely because they exist**; on disagreement with a live source, the live source governs and the delta is recorded. | TRANSCRIBED — `execution/_Coordination/LOOP_INIT.md`; `CURRENT_WORKPLAN.md`; standing workplan §Authority basis |
| **D-8** | Git closeout runs through the change-management role with human-gated PRs; **never self-merge**. | TRANSCRIBED — `execution/_Coordination/LOOP_INIT.md` §7; standing workplan §Closeout; K-MERGE-1 |
| **D-9** | The decomposition pipeline is not waivable: packages and deliverables come only from an accepted decomposition. Nothing authorizes inventing packages from discussion. | TRANSCRIBED — D-GOV-21 packet §4 |
| **D-10** | The public-export boundary is an explicit allowlist profile that copies allowlisted content, sanitizes private absolute paths, writes a manifest and report, and fails on forbidden paths or leaks. **The profile is the boundary contract and is incorporated by reference**; membership is not restated here. | TRANSCRIBED — `exports/chirality-app/export_public.py`; K-EXPORT-1 |
| **D-11** | A tranche changing surfaces that downstream loops pin or mirror ships a routed coordination notice to each affected loop in the same tranche. The notice is coordination, not authority: the receiving loop adopts, amends, or declines under its own instruments. | TRANSCRIBED — `AGENTS.md` change-notice rule; D-GOV-21 M6 |
| **D-12** | Developmental machinery is **product scope**, not surrounding process — a legitimate target of decomposition, deliverables, and acceptance rather than exempt overhead. | CLARIFIED — interpretation of §4.1 against D-GOV-21 packet §5.3 ("these guards are preconditions, not future tooling") |
| **D-13** | Once adopted, this PRD is amended only by a superseding instrument bound to a git SHA. The adopted bytes are never edited in place. | **PROPOSED** |
| **D-14** | **Source-currency obligation.** An adopted PRD that incorporates accepted doctrine carries a standing currency check covering: (a) referenced invariant IDs still exist and still say what is cited; (b) the live agent and skill registries still support the by-reference commitments; (c) source anchors that have changed; (d) repeated enumerations that have drifted from their registries; (e) provenance labels and counts; and (f) concordance with `docs/DIRECTIVE.md` §1. The check runs against the concordance annex (§10.1). **A currency failure is a REVIEW finding routed to the owner — never an automatic amendment** (K-AUTH-1; D-GOV-02). | **PROPOSED** — expands Rev 1's R-D-16 beyond DIRECTIVE §1 concordance per the review |
| **D-15** | The first root decomposition demonstrates **coverage across all four categories** of §4.1 — each category has decomposition coverage or a recorded, reasoned deferral. This constrains coverage demonstration only; it does **not** prescribe the partition (§4.3). | **PROPOSED** — strikeable without affecting any other commitment |

### 5.4 Evidence

| ID | Commitment | Label and source |
|---|---|---|
| **E-1** | Every orchestration run persists a durable, versioned record tree under `_Coordination/AgentRuns/<RunID>/` capturing plan, work graph, briefs, returns, notices, dispositions, amendments, and final handoff state. Run IDs are created only when a real run begins; placeholder runs and briefs presented as executed children are prohibited. | TRANSCRIBED — `docs/SPEC.md` §9.8; `execution/_Coordination/LOOP_INIT.md` §5 |
| **E-2** | Phase-boundary decisions terminate in immutable snapshots; stopping work emits an explicit handoff state; each lawful tranche appends a minimal receipt. | TRANSCRIBED — `AGENTS.md` snapshot and handoff-state rules; K-SNAP-1; `LOOP_INIT.md` §7 |
| **E-3** | The three SHA roles are distinct and recorded distinctly: the **owner act binds approved content to its candidate SHA**; the **publication SHA identifies the durable ruling record**; the **EffectiveSHA identifies applied state**. | TRANSCRIBED — K-AUTH-2; D-GOV-21 record header. *(Rev 2 correction: Rev 1's R-E-5 conflated these.)* |
| **E-4** | Claims carry epistemic labels and progress through the warrant lifecycle `UNWARRANTED → CITED → REVIEWED → AUTHENTICATED`; authentication is an accountable actor's scoped, purpose-specific, SHA-bound act that neither creates knowledge nor establishes truth. | TRANSCRIBED — `docs/TYPES.md` §10.3–§10.4; D-GOV-19 ruled proposition 4; D-GOV-08 |
| **E-5** | Read-only audit and evaluation surfaces exist and are governed; **membership is incorporated by reference** to the live agent index. | TRANSCRIBED — `AGENTS.md` agent index; `docs/DIRECTIVE.md` §4.1 |
| **E-6** | Validation evidence is written only under declared generated paths under the mutation-control contract; the harness never writes governed authority files, and governed-file mutation by a validation command is an unconditional BLOCK. | TRANSCRIBED — D-GOV-01; harness phase-4 record in `_REGISTER.md` |
| **E-7** | A scope unit or phase is not closed because files were written: closure requires accepted authoritative truth, regenerated or explicitly deferred derivatives, recorded audit status, and surfaced unresolved blockers. | TRANSCRIBED — `AGENTS.md` closure rule; `docs/DIRECTIVE.md` §2.7 |
| **E-8** | **Evidence completeness is not evidence sufficiency.** The provenance ladder measures whether warrant is present, never whether it is adequate for a given reliance purpose; adequacy is a human judgment against scope and purpose. | CLARIFIED — D-GOV-08 Option B as implemented ("completeness, never sufficiency"); K-DOMAIN-4; K-CLAIM-1 |

---

## 6. Self-application and concurrency direction

### 6.1 The ruled sequence

**[TRANSCRIBED]** Self-application is operationalized by the D-GOV-21 §6
sequence, of which this document is step 5. Steps 1–4 are closed at the
accepted basis; step 5 is this candidate; step 6 (guard capability G1–G4) runs
in parallel as Lane B; **steps 7–9 — PRD adoption, first root decomposition
with Project Setup, and materialization behind the §5.3 gate — are gated and
not released**. Until that gate closes, root `execution/` holds control-plane
records only.

### 6.2 Self-application discipline

**[TRANSCRIBED]** What makes self-application safe rather than circular is
that a root node may not consume a capability produced by root development
before that capability was accepted through the basis or an explicitly
accepted predecessor (falsifier F3). Deterministic guards and human gates
supply containment; **neither supplies authorization** — the M2 gate "does not
itself grant authorization" (K-AUTH-1).

### 6.3 Concurrency direction

**[TRANSCRIBED]** Four accepted mechanisms make concurrent root development
safe: fine-grained write ownership with disjoint or serialized targets (M1);
a frozen instruction basis per run, so an in-flight run never consumes a
sibling's candidate instruction change (M3); worktree isolation for concurrent
children (M4); and a pre-dispatch work-graph check validating declared and
disjoint write targets before dispatch (G3).

**[CLARIFIED]** These four are what make OBJ-6 achievable rather than
aspirational: legibility of concurrent work is a property of declared,
file-recorded write ownership — not of coordination held in conversation. As
concurrent Agent 0 activity grows, the binding constraint is that every active
run's ownership and gates remain reconstructible from `_Coordination/` state,
which is why work graphs are recorded **before** dispatch rather than after.

---

## 7. Variant specialization and governed promotion

### 7.1 Downward: root serves variants

**[TRANSCRIBED]** One instruction root serves many working roots —
`projects/*`, `domains/*`, and desktop-harness user-selected folders — without
per-workspace instruction drift. A working root may extend the invariant
catalog and may overlay or specialize the agent suite, but **MUST NOT weaken**
framework governance. No variant inherits the D-GOV-21 root exception, and the
exception extends to no other working root. Domain engines own authoritative
domain truth; the root governs the work around them without becoming the
solver. Variant and export membership are incorporated by reference (§5,
registry discipline); the detailed inventory is in the annex.

### 7.2 Upward: governed promotion (the reciprocal half)

**[PROPOSED]** The reciprocal relationship — how the product has actually
grown — is stated as a new commitment:

1. Variants **specialize** root patterns for particular forms of knowledge
   work.
2. Their observed friction and successful patterns **may return as
   evidence-linked root candidates**.
3. **No variant automatically changes or weakens root.** A pattern's success
   in a working root is evidence, not authority.
4. **Promotion occurs only through the root's human-governed developmental
   machinery** — a candidate, a ruling, and an accepted tranche (§5.3).

**[CLARIFIED]** §7.1 and §7.2 together are what "generative operating form"
would mean operationally: specialization downward, evidence upward, authority
only through the human hinge. OBJ-5's success condition tests whether the
upward half actually works.

---

## 8. Non-goals, falsifiers, and release authority

### 8.1 Non-goals

**[TRANSCRIBED — restated from D-GOV-21 packet §4, in force and constraining
this PRD]** No change to the public-export boundary; no extension of the root
working-root exception to any other working root or to desktop-selected
folders; no waiver of the decomposition pipeline; no blanket authority for
future root-structure changes; no change to K-AUTH-1, K-AUTH-2, K-BIND-1,
K-GATE-1, K-SEAL-1, or any invariant or clause not named in packet §3.

**[TRANSCRIBED] Non-goals of this document specifically:** it adopts, accepts,
and ratifies nothing including itself (K-AUTH-1); it settles none of
RD-1..RD-5; it creates no `PKG-*`/`DEL-*` and authorizes no materialization;
it changes no instruction-surface file (any such change is an M2 governance
tranche requiring independent owner authorization); it does not re-litigate
the philosophical framework or thesis (governed by D-GOV-19; `docs/thesis/`
stands at CITED/REVIEWED, **not** AUTHENTICATED); it is not a roadmap
(`docs/PLAN.md` remains the roadmap surface); and it resolves none of the
conflicts in §10.2 — surfacing them is the act, ruling on them is the owner's.

**[CLARIFIED] Not decomposition.** This revision adds direction, not
partition. No packages, deliverables, acceptance tests, or priority rankings
are introduced; those are downstream, human-gated work under
`docs/DECOMPOSITION_STANDARD.md` and D-GOV-15/16.

### 8.2 Falsifiers

**[TRANSCRIBED — D-GOV-21 packet §9]** Falsifiers of the *containment* of
self-application, adopted here as product-level falsifiers of ID-1:

- **F1 — Containment failure.** Root self-development corrupts a shared
  instruction surface out from under a situated loop in a way the superseded
  separation would have prevented, and M1–M6/G0–G4 did not detect or gate it.
- **F2 — Loop bypass.** Root development proceeds outside the root governed
  loop — work materialized without a current workplan pointer, receipts, and
  the M2/G4/M6 machinery engaged.
- **F3 — Self-authorization.** A root node consumes a capability produced by
  root development before that capability was accepted.

**[PROPOSED]** Falsifiers of the *fidelity* of self-application, inert until
adoption:

- **F4 — Requirements drift.** At the close of the first root decomposition,
  an accepted scope unit cannot be traced to a PRD requirement or objective,
  or a PRD requirement or objective has neither coverage nor a recorded
  deferral.
- **F5 — Concordance failure.** The adopted PRD and `docs/DIRECTIVE.md` §1
  come to say incompatible things about what the root product is, without a
  recorded superseding act on one of them.
- **F6 — Label decay.** A provenance label changes without a superseding
  instrument, or a PROPOSED item is relied upon as though adopted.

### 8.3 Release authority

**[PROPOSED]** Evidence, validation results, decomposition coverage, and guard
state **inform** release judgment. **None of them releases Chirality Root
mechanically.** Release occurs only when the owner performs the applicable
explicit release act.

**[TRANSCRIBED] Supporting basis:** K-AUTH-1 (only humans author binding
approvals; no agent may issue work for reliance); D-GOV-02 (a BLOCK is
mechanically bounded to its declared observation boundary and never a global
safety verdict); `docs/DIRECTIVE.md` §7 (the runtime pilot "does not authorize
… release, publication, issuance, or professional reliance"); K-DOMAIN-4
(validation-passed is necessary, not sufficient).

---

## 9. Reserved owner decisions (RD-1 .. RD-5)

D-GOV-21 packet §11 expressly withheld four decisions and routed them here;
the adversarial review identified a fifth. Each is presented with options and
consequences. **None is settled.** Where an agent or reviewer recommendation
appears it is attributed as such, and the decision remains reserved.

### 9.1 RD-1 — Genus wording

| Option | Content | Consequence |
|---|---|---|
| **A** | Retain `docs/DIRECTIVE.md` §1's ratified genus; reword `README.md` as the derivative surface. | No amendment to ratified doctrine; `README.md` is already slated for propagation-style rewording. Cost: the genus arguably under-describes a tree that also holds a governance layer, tool layer, domain applications, project records, and a runtime. |
| **B** | Adopt `README.md`'s genus; amend `docs/DIRECTIVE.md` §1. | Requires a superseding amendment to a RATIFIED clause (a D-GOV-21-class act with exact candidate prose), plus propagation to SPEC/TYPES/AGENTS prose and to the public export. |
| **C** | A two-level formulation: genus plus explicit differentia, stated once and propagated. | Removes the ambiguity permanently and can subsume both readings. Cost: new prose requiring exact-prose acceptance and a propagation tranche. |
| **D** | Defer: adopt with the conflict recorded and both variants cited. | Cheapest now. Cost: §1.2 stays unresolved and F5 remains live. |

**Concrete candidate for option C — reviewer-recommended, decision expressly
reserved.** The independent reviewer proposed this exact formulation
(reproduced verbatim from the run's `reviews/ADVERSARIAL-REVIEW-1.md`):

> "Chirality Root is the canonical human-governed application environment and
> generative operating form for governed professional knowledge work. It
> contains a filesystem-native agent operating system together with the
> normative basis, developmental machinery, evidence, and human judgment by
> which that operating system is formed and governed."

*Attribution: a reviewer recommendation — not an agent recommendation and not
an owner statement. It is offered so option C can be ruled on as text rather
than as an abstraction. Adopting it would require the option-C propagation
tranche above.*

**Agent recommendation:** none among A–D — this is an identity judgment
reserved to the owner. The only agent observation: **whichever option is
chosen, the losing surface must be brought into concordance in the same
tranche**, because leaving both live is exactly the condition F5 names.

### 9.2 RD-2 — Jurisdiction and accountability (two axes)

**Reframed in Rev 2** per the review: this is not one binary but **two axes**.

**Axis 1 — Jurisdiction: who holds authority to govern the root?**

| Option | Content | Consequence |
|---|---|---|
| **A1** | Single root owner (present state). | Matches the live registry exactly; no new machinery. Cost: no expressed succession or delegation path. |
| **A2** | Owner plus named delegates authorized by a recorded superseding instrument. | Adds succession. Requires the delegation instrument to be specified and itself gated. |
| **A3** | A governing body with a recorded quorum rule. | Removes the single point of failure. Requires a bootstrap rule and substantially more machinery than v1 needs. |

**Axis 2 — Accountability: who answers for each consequential professional or
reliance act?**

| Option | Content | Consequence |
|---|---|---|
| **B1** | One accountable human per consequential act, named on the act. | Matches the K-AUTH-1/K-AUTH-2 shape (approvals are acts bound to SHAs) and generalizes to situated professional work in variants where the accountable professional is not the root owner. |
| **B2** | One accountable owner per root, inherited by all acts within it. | Simplest; matches the present single-practitioner state. Cost: writes a single-person assumption into the product and cannot express a variant whose accountable professional differs from the root owner. |

**[TRANSCRIBED] Clarification the review supplies.**
`docs/governance_harness/human_actors.md` identifies **permitted authors of
binding governance records** (D-GOV-04 identity matching). It need not be, and
is not, a registry of every person accountable for situated professional work.
Rev 1 blurred these. The sub-question of **who may amend that file** belongs
to Axis 1: presently owner-curated, owner edits only, not extended
programmatically.

**Agent recommendation:** treat the axes independently — A1 (present state)
with B1 (per-act accountability) is coherent and writes no single-person
assumption into the product, since one owner per root is the degenerate case
of per-act accountability when there is one human. **Agent recommendation
only; both axes expressly reserved.**

### 9.3 RD-3 — Adoption instrument and concordance map

| Option | Instrument | Consequence |
|---|---|---|
| **A** | A **D-GOV-\*** record on the exact-candidate-SHA pattern. | Reuses machinery ruled and exercised three times (D-GOV-18/19/21); inherits register visibility, self-check detection, and SHA binding. Cost: the D-GOV family hosts a product-requirements act as well as governance acts. |
| **B** | A **dedicated PRD adoption record class**. | Keeps requirements acts distinct from governance decisions. Cost: new convention, new validator surface, no existing detection. |
| **C** | The **corpus-ratification pattern** (D-GOV-09 style). | Familiar. Cost: conflates a requirements act with governance ratification and prejudges RD-4 by implying the PRD joins the ratified corpus. |

**Concordance-map form:** (**x**) one-directional — each PRD requirement to
the `docs/DIRECTIVE.md` §1 clause it derives from; simple, but does not expose
DIRECTIVE §1 content the PRD failed to carry. (**y**) bidirectional coverage
matrix with uncovered items marked `TBD`; exposes both drift directions and
produces the artifact F5 is checked against.

**Agent recommendation:** A with y — the exact-candidate pattern is ruled,
exercised, and mechanically detected, and only the bidirectional matrix can
later falsify F5. **Agent recommendation only; decision expressly reserved.**

### 9.4 RD-4 — Placement relative to the public-export boundary

Root `docs/` is in the export allowlist; root `execution/` is not. Packet §11
item 4 records this as a **publication decision**.

| Option | Placement | Consequence |
|---|---|---|
| **A** | Root `docs/` (exported). | Publishes through the **existing** allowlist — no boundary change, so packet §4 is not offended. The PRD joins the instruction surface, so every amendment becomes an M2 tranche and triggers export-manifest regeneration. Doctrinally coherent: normative basis lives in `docs/`. |
| **B** | Root `execution/` (not exported). | Stays private; consistent with root `execution/` as the root product's working root; amendments are working-root acts. Cost: a normative artifact sits on a surface whose own doctrine says coordination surfaces carry no authority merely by existing — readers must be told this one is different. |
| **C** | Root `docs/` **with an export exclusion** (the profile already supports path and prefix exclusions; the governance-harness briefs prefix is the precedent). | Doctrinal home plus privacy. Cost: edits the export profile — an allowlist-narrowing publication-policy change that should be ruled, not assumed. |
| **D** | Split: adopted PRD in root `docs/`; candidates and evidence in root `execution/`. | Mirrors the existing `_PROPOSALS/` vs `_DECISIONS/` split. **Corrected in Rev 2:** this imposes **no two-way concordance burden** — the `execution/` candidate remains immutable historical evidence while a pointer identifies the adopted exact bytes in `docs/`. Rev 1 overstated the cost as "two homes to keep concordant". |

**Agent recommendation:** none among A, C, D — this is a publication judgment
with disclosure dimensions the agent cannot weigh. Two mechanical
observations only: (i) A publishes through the existing allowlist and needs no
boundary change, whereas C requires an export-profile edit; and (ii) the
choice determines whether future PRD amendments are M2 instruction-surface
tranches (A, C, D) or working-root acts (B) — a process consequence worth
deciding deliberately rather than inheriting. **Decision expressly reserved.**

### 9.5 RD-5 — v1 user scope *(new in Rev 2)*

**The question.** Who is Chirality Root **v1** for? RD-2 does not answer this:
RD-2 concerns governance jurisdiction and act-level accountability, not
product user scope.

| Option | Scope | Consequence |
|---|---|---|
| **A** | **The present owner-practitioner.** v1 targets one accountable practitioner running governed loops. | Smallest honest claim; matches the live state and demands no multi-user machinery. Cost: OBJ-2's situated-working-root condition is satisfied by the owner's own variants only, and multi-practitioner needs (concurrent human review, per-act attribution across people, delegation) go undesigned — becoming v2 rework rather than v1 constraint. |
| **B** | **Accountable professional practitioners generally.** v1 targets any single licensed or accountable practitioner in the target domains. | Aligns with `docs/DIRECTIVE.md` §3's engineer-of-record framing and makes the professional-responsibility model do real work. Cost: raises the bar for onboarding, documentation, and OBJ-1's discoverability condition; implies the product must be intelligible to someone who did not build it. |
| **C** | **Multi-practitioner organizations.** v1 targets teams with several accountable humans. | Largest reach. Cost: requires answering RD-2 Axis 1 with A2 or A3 and Axis 2 with B1, plus concurrent-human-review machinery, per-act attribution across people, and inter-practitioner conflict resolution — none of which exists at the accepted basis. |

**Consequences that cut across.** The choice sets the meaning of "user" in
OBJ-1 (discoverability *by whom*), OBJ-2 (whose deliverable stream), and OBJ-3
(whose retrieval, in whose bounded time). It also determines whether §2.3's
primary-user stratum is one person or a class.

**Agent recommendation:** none — this is a product-scope judgment for the
owner. One observation: **B is the smallest scope under which OBJ-1's
discoverability condition has independent content**, because a product built
for its own author can satisfy "discoverable" trivially. **Decision expressly
reserved.**

---

## 10. Source concordance and document control

### 10.1 The concordance annex (derivative package)

The detailed transcription inventory — every clause, section anchor, and
verified line reference behind the commitments in §5, plus the registry
reference index and the previously-recorded items carried forward from Rev 1 —
lives in:

`execution/_Coordination/PRD_CANDIDATE_2026-07-25_concordance_annex.md`

**Its status is binding on how it may be used:**

- It is a **derivative package** under the `AGENTS.md` derivative-package
  rule: assembled from accepted upstream truth, citing its source SHAs, and
  **never a substitute** for that truth.
- It is a **derived publication artifact** in
  `docs/DECOMPOSITION_STANDARD.md` terms: not the amendment surface,
  deterministically regenerable, explicitly labelled derived and
  non-authoritative.
- It is **mechanically regenerable and checked** — it is the surface the D-14
  source-currency obligation runs against.
- **It is never itself adopted. Adoption, if it occurs, binds the exact bytes
  of this main PRD only.**

Rev 2 moved the inventory out of the main document to prevent the PRD from
becoming another drifting registry — the failure mode already observed in
`docs/CONTRACT.md`'s invariant index (C-2) and `README.md`'s export
description (C-4).

### 10.2 Conflicts surfaced, not resolved

Per K-CONFLICT-1, each carries `HumanRuling = TBD`. Two previously-recorded,
non-new items (the K-WRITE-2 explanatory-gloss debt and the accepted packet
`UNRESOLVED_SOURCE_REF` WARN) are carried in the annex rather than restated
here.

| # | Conflict | Sources | Disposition |
|---|---|---|---|
| **C-1** | **Genus wording.** `docs/DIRECTIVE.md` §1 names an "agent operating system"; `README.md` names an "application environment". | Ratified governance vs. a non-binding/derivative surface (D-GOV-21 packet §3b) | Routed to **RD-1**. `HumanRuling = TBD` |
| **C-2** | **Invariant-index arithmetic.** `docs/CONTRACT.md` §1 states "27 stable invariants across 12 subsections" and its index table ends at K-DOMAIN-4, but §1.13 defines seven further invariants absent from that index; the §2 enforcement map does reference two of them. The live catalog holds 34 across 13. | `docs/CONTRACT.md` §1 index vs. §1.13 and §2 | **New find** (Rev 1). Not amended here — ratified instruction surface. Recommend an M2 correction tranche. `HumanRuling = TBD` |
| **C-3** | **Historical-note date.** The sealed brief states in-repo history begins 2026-02-18; git shows the first commit is 2026-05-18 and no in-repo file asserts the earlier date. | Sealed brief vs. git history at the accepted basis | §1.1 ID-4 records the verified git fact; the brief's date is surfaced, not adopted and not silently corrected. Owner confirms or corrects at adoption. `HumanRuling = TBD` |
| **C-4** | **Export description vs. export profile.** `README.md`'s public-export section omits `runtime/`, which the export profile's root-directory allowlist includes. | `README.md` vs. `exports/chirality-app/export_public.py` | **New find** (Rev 1). Live profile governs (K-AGENTS-1 principle; `README.md`'s own guidance). Routed as propagation. `HumanRuling = TBD` |

### 10.3 Adoption mechanics

**[TRANSCRIBED]** Adoption is a separate future owner act on a separate
instrument. What it requires, on the cited sources: **exact bytes** of this
file bound at a named SHA (instrument reserved as RD-3); the **concordance map
against `docs/DIRECTIVE.md` §1** required at adoption (packet §11 item 3; form
reserved as RD-3); the **owner ruling recorded verbatim** and attributed to a
matching registered actor (D-GOV-04), SHA-bound at publication (K-AUTH-2); and
**resolution of RD-1 through RD-5**. No agent act substitutes for any of these
(K-AUTH-1).

**[TRANSCRIBED]** Until adoption, **every PROPOSED item here is inert** — the
v1 boundary, OBJ-1..OBJ-7, D-13, D-14, D-15, §7.2 governed promotion, §8.3
release authority, and F4–F6. TRANSCRIBED commitments remain in force
regardless, because their authority is their own source.

**[TRANSCRIBED]** What adoption would **not** do: materialize anything under
root `execution/` (packet §6 step 9, behind the §5.3 gate), create a root
decomposition (step 8), or change the public-export boundary (packet §4).

### 10.4 Document control

| Field | Value |
|---|---|
| Status | `CANDIDATE — NOT ADOPTED`, Revision 2 |
| Binds | Nothing (K-AUTH-1) |
| Accepted basis | `main@7ac718c7e` |
| Rev 1 | `f15d51277` (PR #340) — superseded by this revision, not edited |
| Governing decision | D-GOV-21 (RULED 2026-07-25); candidate `c038c493e871c95871823281b45890ba9404624b`; publication `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`; effective `ee42157290618e3f84be0e0b651c041387ad6ee0` |
| Authorizing effect | D-GOV-21 effect 5 (PRD-development basis) |
| Run | `ROOT-PRD-LANE-A-20260725` (Lane A) |
| Companion | Concordance annex — derivative package, never adopted (§10.1) |
| Reserved decisions | RD-1 .. RD-5, all unresolved |
| Provenance counts | **§5 stable commitments — 42 total: 34 TRANSCRIBED (N-1..N-8, O-1..O-9, D-1, D-3..D-11, E-1..E-7), 5 CLARIFIED (N-9, O-10, D-2, D-12, E-8), 3 PROPOSED (D-13, D-14, D-15).** Elsewhere: **5 OWNER_DECLARED** framing claims (ID-1, ID-2, ID-3, §4.1 categories, §4.2 loop); **1 TRANSCRIBED** identity fact (ID-4) plus ID-1a; **3 TRANSCRIBED** falsifiers (F1–F3); **13 further PROPOSED** items (v1 boundary, OBJ-1..OBJ-7, §7.2 promotion relationship, §8.3 release authority, F4, F5, F6). |
| PROPOSED inventory | **16 items, all inert unless adopted:** D-13; D-14; D-15; the v1 boundary (§3); OBJ-1; OBJ-2; OBJ-3; OBJ-4; OBJ-5; OBJ-6; OBJ-7; §7.2 governed-promotion relationship (items 1–4, one commitment); §8.3 release authority; F4; F5; F6. |
| Next act | Owner review. Adoption, if any, is a separate instrument (RD-3). |
