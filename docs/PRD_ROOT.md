<!-- RD-4-D ADOPTED PLACEMENT — pointer block added at placement; everything below the horizontal rule is byte-identical to the adopted candidate bytes. -->

> **Adopted root PRD (placement copy).** Adopted by **D-GOV-22**
> (`docs/governance_harness/_DECISIONS/D-GOV-22_root_prd_adoption.md`), owner
> ruling 2026-07-25 against candidate SHA
> `90fae458bf485412e9c3a6295df193eb323c9774`. The adopted exact bytes are
> `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md` at
> `d9ea86f88504cb8d859a4cf3f042bac00d38fe57`
> (sha256 `d85ac3f941ee6808c9a62888bc488cec2198c2814b4f14641094cf0e0f1d04cb`);
> this file is those bytes plus this pointer block, placed in root `docs/`
> per RD-4-D. Candidates and revision evidence remain immutable in
> `execution/_Coordination/`. Future amendments to the adopted PRD are M2
> instruction-surface tranches, never edits to the candidate history.

---

# Product Requirements Document — Chirality Root (the root product)

> **Status: `ADOPTION-READY — adopted only by the instrument named below`.
> Revision 5 — the final adoption-ready revision specified at §10.3.**
>
> **The adopting instrument** is a `D-GOV-*` decision record using the
> exact-candidate-SHA pattern over the exact bytes of this file — the form the
> owner ruled at **RD-3** (§9.3). **That record, not this file, carries the
> adopted status**: it records the owner's verbatim ruling, binds it to a SHA
> (K-AUTH-2), and is where adoption happens. This file states its own status by
> pointing outward, so nothing in it becomes false when that record is
> published.
>
> **All five reserved owner decisions are RULED** (§9): RD-1 genus, RD-2
> jurisdiction and accountability, RD-3 adoption instrument and concordance
> map, RD-4 placement, RD-5 v1 user scope. The concordance obligations the RD-1
> ruling creates are routed to the adoption/implementation tranche and are
> **not performed here** (§9.1).
>
> **This file confers no authority of its own.** Authorship by an agent confers
> none (`docs/CONTRACT.md` §1.2, **K-AUTH-1**: only humans author binding
> approval records; no agent may certify, approve, sign, seal, or issue work
> for reliance), and existence, validation, commit, and Git transport are
> **not** approval. **Until the named instrument's owner ruling, every
> PROPOSED item here is inert** (§10.3).
>
> **Adoption is an act on a separate instrument** (D-GOV-21 packet §11 item 3;
> §6 step 7; standing workplan §Gated downstream item 1), and **it binds the
> exact bytes of this file only**.
>
> **SourceCorpusBasis:** `main@7ac718c7e` — the state of the cited governance
> corpus. This revision's own bytes live in the commit that contains them,
> recorded by Agent 0 in the run record and receipt; this file does not assert
> its own SHA (no self-referential backfill).
> **Run:** `ROOT-PRD-LANE-A-20260725` (Lane A; D-GOV-21 packet §6 step 5, on
> the basis of D-GOV-21 effect 5).
> **Revision history:** Rev 1 `f15d51277`; Rev 2 `a72c2cd06`; Rev 3
> `f9d33fcd9`; Rev 4 `ae5a476f4` — each immutable historical candidate
> evidence, superseded by this revision and not edited (§10.3). Revs 2–5
> incorporate the four owner-routed independent adversarial reviews under brief
> amendments 1–4; Rev 4 additionally incorporates the owner's **RD-1** ruling
> and Rev 5 the owner's **RD-2..RD-5** rulings. All amendments and reviews are
> in this run's `briefs/` and `reviews/` directories under
> `execution/_Coordination/AgentRuns/ROOT-PRD-LANE-A-20260725/`.
> **Authored by:** an ephemeral bounded Agent 2 generalist under sealed brief,
> dispatched by `HELP_HUMAN` (Agent 0). Agent authorship confers no authority.
> **Companion:** `execution/_Coordination/PRD_CANDIDATE_2026-07-25_concordance_annex.md`
> — a **derivative package**, specified for regeneration and never itself
> adopted (§10.1).
> **Placement (RD-4, RULED — split with pointer):** the adopted exact bytes are
> placed in root `docs/` by the adoption tranche; **this file stays on the
> non-exported coordination surface as immutable revision evidence**, and a
> pointer identifies the adopted bytes (§9.4). **The `PRD_CANDIDATE_` filename
> is retained deliberately**: this path is the candidate/evidence surface, and
> renaming it would break the prior revisions' history at a stable path. The
> status is the banner's, not the filename's.
> **Date:** 2026-07-25

---

## Provenance key

Every requirement, objective, and identity claim carries exactly one label.

| Label | Meaning | Reliance |
|---|---|---|
| **TRANSCRIBED** | Accepted or ratified doctrine, cited to its governing clause and verified against the live file at the SourceCorpusBasis. | In force now, because its source is in force — not because this document repeats it |
| **OWNER_DECLARED** | Owner-endorsed framing or an owner ruling **as transcribed or synthesized by Agent 0 in-session**. Exact wording is subject to owner confirmation or correction at adoption. **Not claimed verbatim unless quote-fenced.** | Not in force as doctrine; an in-session ruling is an owner act of record that becomes SHA-bound at the adoption instrument |
| **OBSERVED** | A **verifiable repository fact** — what a non-binding live surface says, or what git history shows — cited to file and line, carrying **no** doctrinal force. Distinguishes "this text exists in the tree" from "this text governs". | None. An OBSERVED item may be true and still bind nothing; it supports no reliance claim |
| **CLARIFIED** | An interpretation of accepted truth produced by the 2026-07-25 root-PRD inquiry (Agent 0 plus independent second-agent review, owner-mediated). Interpretation, not new authority. | Reading aid; the cited source governs |
| **PROPOSED** | A new commitment taking effect **only if this PRD is adopted**. Inert until then. | None |

Quote fences (`>`) appear **only** around text warranted as verbatim, with its
record cited. Synthesized owner framing is presented as ordinary prose.

---

## 1. Product identity and genus

### 1.1 What Chirality Root is

**ID-0 — Ruled genus. [OWNER_DECLARED — owner ruling of record]** The owner
ruled **RD-1** in-session on 2026-07-25, selecting the two-level formulation.
The ruled genus text:

> "Chirality Root is the canonical human-governed application environment
> and generative operating form for governed professional knowledge work.
> It contains a filesystem-native agent operating system together with the
> normative basis, developmental machinery, evidence, and human judgment
> by which that operating system is formed and governed."

*Ruled in-session; recorded in Receipt 37; SHA-bound at the adoption
instrument (RD-3). Selection and ruling mechanics are at §9.1.*

**What this ruling does and does not do [CLARIFIED].** It settles the genus
**for this PRD**. It does **not** amend `docs/DIRECTIVE.md` §1 — that clause
is ratified governance and remains **in force as written** until a separate
exact-prose, human-gated concordance act supersedes it (§9.1, follow-on
obligation (a)). Until then this document records the ruling and the
divergence honestly rather than claiming DIRECTIVE has been amended.

**ID-1 — Dual nature. [OWNER_DECLARED]** The root product both **governs the
production of professional knowledge work** and is a **normative,
self-applying instance of a generative development pattern**: it develops
itself under the same governance it prescribes. This is the same duality the
ruled genus expresses as "application environment **and** generative
operating form". *(Agent 0 synthesis of in-session owner framing carried
through a context compaction; not warranted verbatim. Owner confirms or
corrects at adoption.)*

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

### 1.2 Genus wording — ruled, concordance pending

**The genus is ruled** (ID-0, §9.1). This section now records the ruling
against the two live surfaces it supersedes **in principle**, and states
exactly what is still true of each pending the concordance act.

| Surface | Wording | Label | Status after the RD-1 ruling |
|---|---|---|---|
| **`docs/DIRECTIVE.md` §1** | "a governed, filesystem-native agent operating system for deliverable-heavy professional work" | **TRANSCRIBED** | **Still in force as ratified doctrine.** It is in the RATIFIED root governance corpus (D-GOV-09, owner ratification 2026-07-11) and the RD-1 ruling does not amend it. Superseded **in principle** by the ruled genus; superseded **in fact** only when the concordance act lands (§9.1 obligation (a)). |
| **`README.md`** | "a governed application environment for agent-assisted, deliverable-heavy professional work" | **OBSERVED** | A verifiable repository fact, not doctrine: `README.md` is a **non-binding / derivative surface** per D-GOV-21 packet §3b. It carries no doctrinal force either before or after the ruling, and is scheduled for reword under §9.1 obligation (b). |

**[CLARIFIED]** These are **two live surfaces**, not two accepted authorities:
only the DIRECTIVE clause is doctrine, which is why only it carries
TRANSCRIBED. The ruled genus is closest in shape to the README wording and subsumes the
DIRECTIVE wording as its second level ("It contains a filesystem-native agent
operating system…"), which is why the two-level formulation can resolve the
conflict rather than merely pick a side.

**Divergence of record, pending concordance [CLARIFIED].** Until obligation
(a) lands, the repository contains a ratified genus clause that differs from
the genus this PRD carries. That is a **known, recorded divergence**, not a
silent inconsistency: it is tracked as **C-1** (§10.2) at status
`RESOLVED-IN-PRINCIPLE — concordance pending`, and it is precisely what
falsifier **F5** exists to catch if it is left unclosed.

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
applicability boundary of the product.

### 2.3 Users, actors, and consuming contexts

Agents and working roots are **not users** in the product sense. Two
distinctions are drawn below: **strata** (who or what interacts with the
product) and, first, **capacities** (which authority a person is exercising).

#### Human capacities are separable [CLARIFIED]

Four distinct capacities may be held by four different people. **Holding one
confers none of the others.**

| Capacity | What it authorizes | Governing source |
|---|---|---|
| **Root-governance authority** | Ruling on the root product's own governance: authoring binding governance records, ratifying, superseding. | K-AUTH-1; D-GOV-04 identity matching against `docs/governance_harness/human_actors.md` |
| **Professional accountability for situated work** | Accepting scope and design basis, adjudicating technical conflicts, accepting residual risk, and issuing situated deliverables for reliance. | `docs/DIRECTIVE.md` §3.2 engineer-of-record principle |
| **Review** | Assessing whether work may be relied upon; gating a lifecycle transition; returning findings that stop or redirect work. | `docs/DIRECTIVE.md` §2 (epistemic architecture); the REVIEW gate role |
| **Product maintenance** | Changing the instruction surface, tools, skills, and harness under governance. | D-GOV-21 M2; `docs/SPEC.md` §0.2.1–§0.2.2 |

**Explicitly:** a professional practitioner does **not** thereby obtain
root-governance authority, and the root owner does **not** thereby become the
accountable professional for situated work in a variant. At the accepted basis
all four capacities happen to be held by one person; **that is a fact about
the present instantiation, not a property of the product.**

**[CLARIFIED] What the rulings settle here.** Under **RD-2** (RULED — A1+B2,
§9.2) v1 scopes jurisdiction to a single root owner and accountability to one
accountable owner per root; under **RD-5** (RULED — A with a staged
trajectory, §9.5) v1 targets the present owner-practitioner. **v1 therefore
need not support the four capacities being held by four different people** —
but the separability above is a property of the capacities themselves, not of
the v1 configuration, and it is what the B and C stages of the RD-5 trajectory
would exercise.

#### Strata

| Stratum | Who / what | Notes | Label |
|---|---|---|---|
| **Primary human users** | People exercising root-governance authority or professional accountability for situated work — directing governed work, ruling, approving, adjudicating, accepting residual risk, issuing for reliance. | The only actors who can perform the acts K-AUTH-1 reserves. Presently one person is registered as a permitted author of binding governance records (`docs/governance_harness/human_actors.md`) — which registers *that* capacity only, not the others. | CLARIFIED |
| **Secondary human users** | People exercising review or product-maintenance capacity: reviewers, auditors, maintainers, and people assessing whether work may be relied upon. | **They act, they do not merely observe** — a reviewer may gate a lifecycle transition or return findings that stop work, and a maintainer changes the instruction surface under governance. They do not thereby acquire root-governance authority. Their needs drive the epistemic architecture (`docs/DIRECTIVE.md` §2). | CLARIFIED |
| **System actors** (not users) | Agent 0 / Agent 1 / Agent 2 instances; deterministic tools; the runtime daemon and its clients. | `agent = LLM + instructions + declared files/context + tools + permissions` (`AGENTS.md`) — "an operational definition, not a claim of personhood or professional responsibility". They execute within permission boundaries and never hold authority. | TRANSCRIBED |
| **Consuming contexts** (not users) | `projects/*` and `domains/*` working roots; desktop-harness user-selected folders; other situated working roots; the public export. | They bind `{WORKING_ROOT}` against the one instruction root. They may extend the invariant catalog but MUST NOT weaken it (`docs/CONTRACT.md` §1). | TRANSCRIBED |

**Whom v1 is *for* is RULED as RD-5** (§9.5): **v1 = the present
owner-practitioner**, on a staged trajectory toward individual professional
knowledge workers generally and then multi-practitioner organizations. RD-2
(§9.2) is a separate question and answers a different one: governance
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
| **OBJ-2** | **Governed production of professional knowledge work.** The product carries work **to** an issuance decision; the accountable human issues it. | At least one complete deliverable stream runs end to end — decomposition → package/deliverable → checking → issuance decision — where **every consequential acceptance, reliance, and issuance judgment is performed by an accountable human**, and every governed claim carries provenance sufficient for a reviewer to determine reliance. Deterministic guards, fan-in gates, and structural validation gates remain lawful **non-human** gates: they gate on objective preconditions and hygiene and never make the acceptance or issuance judgment (K-GATE-1 with its D-GOV-02 note; K-AUTH-1). Demonstrated at root and in at least one situated working root. |
| **OBJ-3** | **The human evaluation and iteration loops close.** Humans can evaluate and redirect on evidence. | **Two conditions, one universal and one sampled.** **(i) Structural completeness — universal:** *every* accepted change has a retrievable linkage from files alone between the evidence that informed it, the ruling that accepted it, and the state it changed. A missing link is a defect regardless of sampling. **(ii) Retrieval usability — sampled:** the linkage can be *followed* within a bounded time, verified as a retrieval exercise where **the time threshold and the tranche sample are fixed and recorded before the evaluation runs** — not chosen after seeing results. Completeness is a property of the record; usability is measured, not asserted. |
| **OBJ-4** | **Safe self-application without self-authorization.** The root develops itself without granting itself authority. | Through v1: falsifiers F1–F3 unobserved; every root capability consumed by root development was accepted through the basis or an explicitly accepted predecessor; G0–G4 registered and passing at every materialization. |
| **OBJ-5** | **Situated specialization with governed convergence.** Variants specialize; useful patterns come back lawfully. | **(i)** At least one candidate pattern originating in a situated working root reaches a **complete promotion disposition — accepted, rejected, or deferred with its evidence recorded** — through the developmental machinery with its evidence linkage intact. **A rejection or reasoned deferral satisfies this**: the objective tests that the pathway works, not that any candidate deserves promotion; no promotion is forced to pass v1. **(ii)** **Every root change that claims variant-derived provenance used the governed promotion path.** *(Stated positively and checkably against changes that make the claim — rather than as an unprovable negative about all changes by every possible route.)* |
| **OBJ-6** | **Coordination remains intelligible as concurrent activity grows.** Concurrency does not outrun legibility. | **Population and observation boundary:** root-product development runs — the run records under this loop's `execution/_Coordination/`. Situated working roots' coordination remains their own surface and is out of scope here; **any future aggregated cross-root coordination layer would be a new product function, not implied by this objective.** **Condition:** for every run record present in that population, its declared write ownership, dependencies, and pending gates are reconstructible from the recorded state, and runs that were interrupted, abandoned, or crashed are **detectable as stale or orphaned** rather than silently indistinguishable from live ones. Concurrent sibling write targets are disjoint or serialized. No run's effect is discoverable only from chat history. |
| **OBJ-7** | **File-native continuity and recoverability.** Nothing load-bearing lives outside the checkout. | The full governed state — decisions, approvals, scope, evidence, and each loop's current position — survives loss of every non-file substrate (chat context, model memory, daemon state, local caches) and is recoverable from the checkout alone. |

**[CLARIFIED]** OBJ-1 through OBJ-7 are objectives of the *product*, not of any
single tranche. They are the intended source for the objective derivation
that `docs/DECOMPOSITION_STANDARD.md` I7 requires; unmapped objectives at
decomposition time are surfaced as open issues, never silently dropped.

**[CLARIFIED] Reading the objectives under the ruled v1 user scope.** RD-5 is
RULED at **A** — the present owner-practitioner (§9.5) — so "user" in OBJ-1,
OBJ-2, and OBJ-3 means that practitioner for v1. **OBJ-1's discoverability
condition still has independent content under A**, because the ruled scope is
not a terminus: the owner ruled a **staged trajectory** in which learning from
A produces a version for B (individual professional knowledge workers
generally) and then C (multi-practitioner organizations, the stated target
maturity). A product built only for its own author could satisfy
"discoverable" trivially; a product expressly built *toward* B and C cannot,
because the B stage is what a reader who did not build it must survive. The
trajectory is the reason OBJ-1 is tested rather than assumed at v1.

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

#### Three distinct human judgments [OWNER_DECLARED]

The single "human judgment" step above resolves into **three judgments that
must not be collapsed** *(Agent 0 synthesis; not verbatim)*. The first two are
loops in the diagram; the third is a lifecycle judgment that draws on both:

| Judgment | Input | Decides | Question it answers |
|---|---|---|---|
| **Evaluation judgment** *(loop)* | Operative evidence — the artifacts, claims, and records that operative work produced. | Accept, reject, or redirect **the work**. | Is this work good enough, and for what reliance? |
| **Iteration judgment** *(loop)* | Developmental candidates plus iteration evidence — proposed changes to the product itself and the record of how prior changes fared. | Accept, reject, or redirect **the change to the product**. | Should the product itself change, and in this way? |
| **Release judgment** *(lifecycle gate)* | **Both** operative evidence and developmental evidence, plus validation results, decomposition coverage, and guard state. | Whether **the current product state may be released**. | Is what exists now fit to be released, as it stands? |

**Release is not iteration.** It asks whether the present state may go out, not
whether the product should change; a release judgment may be "no" with no
change proposed, or "yes" with changes pending. It is **separately
human-gated** (§8.3).

**None is delegated to machinery.** Deterministic tools, guards, and validators
supply findings to all three and gate objective preconditions; they never
perform any of the judgments (K-AUTH-1; D-GOV-02's observation-boundary caveat;
D-GOV-17 — a validator finding may never mechanically reject owner-ruled
content).

**Why the distinctions matter here.** They have different inputs, failure
modes, and evidence needs. Conflating evaluation and iteration would let a
product-level change ride in on deliverable-level evidence, or block a sound
deliverable because the machinery that produced it is under revision. Folding
release into iteration would imply that nothing can be released without
changing something, and that a decision to change is a decision to ship.
OBJ-3 tests that the two loops close; §8.3 governs the release gate.

### 4.3 What the categories are and are not

**[CLARIFIED]**

- They classify **functions and authority relationships**, not filesystem
  buckets.
- They are **non-exclusive**. One artifact may participate in several.
  `AGENTS.md` is normative basis (K-AGENTS-1 makes it an authoritative
  governance surface), operative product (it is the live index agents execute
  against), and — through its change-notice rule — developmental machinery. A
  decision record is developmental machinery and evidence, and its ruling
  **establishes normative or operative accepted state according to its scope**
  — a ruling may settle a governance rule, an operative arrangement, or both,
  and does not invariably become normative basis.
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
| **N-1** | **For authoritative governance and project-coordination state**, the substrate is git-tracked plain files: no external database, server state, or configuration holds that truth; rebuildable gitignored projections are permitted and never citable as authority; if a decision is not in a versioned file it does not exist for purposes of reliance. **Stated exception (K-DOMAIN-1): domain engines own authoritative domain truth** — canonical model files, model states, analysis runs, comparisons, solver outputs, and handoff internals are engine-owned, are sanctioned authoritative domain truth, and are exempt from the rebuildable-projection rule. Chirality governs the work *around* the engine (profiles, manifests, proposals, review notes, gates); it is not the solver and is never the source of accepted engineering truth. | TRANSCRIBED — `docs/DIRECTIVE.md` §2.1, §2.2, §5; D-GOV-01 (Option A) **and its scope note**; K-DOMAIN-1 (`docs/CONTRACT.md` §1.12) and the §1.12 note exempting engine-owned stores. **The exception is stated here, not only in the annex, because the annex is never adopted.** |
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
| **O-2** | The product operates through **three layers**, each with a distinct authority boundary: **(a) instruction artifacts** — agent instruction packages, skills, and governance documents carrying semantic authority contracts, constraining behaviour by declared scope; **(b) deterministic tools** — computed, repeatable operations producing facts and findings, *never a substitute for semantic judgment*; **(c) the root `runtime/` executable substrate** — daemon, clients, adapters, sessions, and transport, which executes and carries work but whose **transport never grants project authority** and whose user-data state is operational, not project truth. | TRANSCRIBED — `AGENTS.md` (Tool row; §Shared Runtime Doctrine); `docs/DIRECTIVE.md` §7; `docs/CONTRACT.md` §1.13. |
| **O-3** | The runtime delegation hierarchy is Agent 0 Supervising Architect → Agent 1 Manager → Agent 2 Specialist, with declared entry rules and no delegation below Agent 2; Agent 2 exists in three construction forms. **The live index and role membership are incorporated by reference** to `AGENTS.md`; this PRD enumerates no agents. | TRANSCRIBED — `AGENTS.md`; `docs/DIRECTIVE.md` §2 (praxiology); D-GOV-11, D-GOV-12, D-GOV-13 |
| **O-4** | Capability never confers authority. Delegation implies no capability inheritance; a child's capability never becomes its parent's; every child remains subject to sealed context, gate approval, path containment, enforced read/write scope, and durable evidence. | TRANSCRIBED — `AGENTS.md` §Delegation and Entry Rules; K-SEAL-1, K-GHOST-1; D-GOV-17 |
| **O-5** | Method packs (`skills/`) and deterministic operations (`tools/`) are maintained as **live registries**, and the live registry is authoritative over any narrative list. Membership is incorporated by reference to `skills/README.md` and `tools/REGISTRY.md`. | TRANSCRIBED — `AGENTS.md` §TASK Skill Capabilities; K-AGENTS-1 |
| **O-6** | The path model defines two roots (`REPO_ROOT`, `WORKING_ROOT`), one containment rule, and a closed `{*_ROOT}` token registry; instruction, coordination, and plan files MUST NOT embed machine-absolute paths. | TRANSCRIBED — `docs/SPEC.md` §0.2–§0.3 |
| **O-7** | Governed work is structured as execution instances containing flat packages and deliverables with stable IDs, a canonical lifecycle state file, and human-triaged staleness propagation. | TRANSCRIBED — `docs/SPEC.md` §1, §3; K-HIER-1, K-ID-1, K-STATUS-1, K-STALE-1/2, K-VAL-1 |
| **O-8** | Deliverable-local dependency registers are authoritative. **No central dependency graph is *authoritative*** — but derived and aggregated graphs are lawful coordination state: on-demand read-only aggregation is provided for, and `FULL_GRAPH` dependency mode computes blockers from the declared graph. | TRANSCRIBED — K-DEP-1 (which itself provides for on-demand aggregation), K-DEP-2; `agents/AGENT_PROJECT_SETUP.md` (`FULL_GRAPH` mode). |
| **O-9** | The instruction root is separated from the working root, with **exactly one** governed exception — the root product's working root is the repository root, and root `execution/` is its execution root, **eligible** for `PKG-*`/`DEL-*` only from an accepted root decomposition derived from an adopted PRD and only while the guards pass. The replacement containment contract (mechanisms M1–M7 and guards G0–G4 with the §5.3 gate ordering) is required and **incorporated by reference** to D-GOV-21 §5. | TRANSCRIBED — D-GOV-21 §Effects 1–4; packet §5; `docs/DIRECTIVE.md` §2.6; `docs/SPEC.md` §0.2.2, §1; `docs/TYPES.md` §1.4 |
| **O-10** | The operative product's boundary is exactly the three layers of O-2. **No fourth machine execution substrate is claimed; none of the three operative layers holds or grants project authority, which remains with attributable human acts under the governed record.** This is why an instruction-surface change is a governance act rather than a code change. | CLARIFIED — interpretation of O-1, O-2 and the D-GOV-21 M2 gate, with K-AUTH-1. |

### 5.3 Developmental machinery

| ID | Commitment | Label and source |
|---|---|---|
| **D-1** | **A design change is carried by one of two terminal artifacts: it supersedes a `D-GOV-*` record, or it arrives as PR review — never a new plan document.** Where the vehicle is a decision record, that record carries status, verbatim owner ruling, SHAs, date, framing, accepted basis, and record convention; the register is navigational and the per-decision records govern. | TRANSCRIBED **at that scope** — the terminal-artifact rule as stated in `docs/governance_harness/_DECISIONS/_REGISTER.md` (§Terminal-artifact rule, restated in §Now actionable): "Design changes from here supersede a `D-GOV-*` record or arrive as PR review — never a new plan document." Record structure: the `_DECISIONS/` records themselves |
| **D-2** | **Within the two record classes where the convention already governs**, corrections to ruled content are superseding acts, not edits: **(i)** published D-GOV decision records carrying the `supersede-never-edit` record convention — a later correction to a ruled record supersedes it; and **(ii)** ruled candidate packets bound to an `AcceptedCandidateSHA` — amending the candidate would void the SHA the owner's ruling approved. **This commitment asserts nothing beyond those two classes.** | CLARIFIED — reads the convention as it stands in its own scope: D-GOV-21 `RecordConvention` field and §Status note ("Any later correction to the transcription is a superseding act, not an edit"); D-GOV-17's recorded-exception protocol; the implementation handoff's "amendment would void the AcceptedCandidateSHA". **The broader change-control rule is carried separately at D-16 (PROPOSED)** — a CLARIFIED label cannot establish it. |
| **D-4** | Attribution of rulings and adoptions matches an owner-curated identity allowlist; identity-dependent checks **refuse rather than guess**. The list is owner-curated and not extended programmatically. | TRANSCRIBED — D-GOV-04; `docs/governance_harness/human_actors.md` |
| **D-5** | Validation is deterministic and severity-typed (BLOCK / REVIEW / WARN / INFO / NOT_APPLICABLE, with exit-code semantics and human-only recorded BLOCK override); "BLOCK" never means globally proven safe or unsafe; and a validator finding may **never** mechanically reject content the owner has ruled — where ruled text trips a validator, the validator is defective. | TRANSCRIBED — D-GOV-02; D-GOV-17; `docs/CONTRACT.md` §1.7 note |
| **D-6** | Phase-crossing work is bound by the governance integration rules — derivative-package, snapshot, handoff-state, closure, sequencing, cycle-resolution, and change-notice routing. **Incorporated by reference** to `AGENTS.md` §Governance Integration Rules. | TRANSCRIBED — `AGENTS.md`; `docs/DIRECTIVE.md` §2.7 |
| **D-7** | Root-product development runs through a governed loop with a session-init contract, a deterministic standing-plan pointer, and an append-only receipts log. **Coordination surfaces carry no authority merely because they exist**; on disagreement with a live source, the live source governs and the delta is recorded. | TRANSCRIBED — `execution/_Coordination/LOOP_INIT.md`; `CURRENT_WORKPLAN.md`; standing workplan §Authority basis |
| **D-8** | Git closeout runs through the change-management role with human-gated PRs; **never self-merge**. | TRANSCRIBED — `execution/_Coordination/LOOP_INIT.md` §7; standing workplan §Closeout; K-MERGE-1 |
| **D-9** | The decomposition pipeline is not waivable: packages and deliverables come only from an accepted decomposition. Nothing authorizes inventing packages from discussion. | TRANSCRIBED — D-GOV-21 packet §4 |
| **D-10** | The public-export boundary is an explicit allowlist profile that copies allowlisted content, sanitizes private absolute paths, writes a manifest and report, and fails on forbidden paths or leaks. **The profile is the boundary contract and is incorporated by reference**; membership is not restated here. | TRANSCRIBED — `exports/chirality-app/export_public.py`; K-EXPORT-1 |
| **D-11** | A tranche changing surfaces that downstream loops pin or mirror ships a routed coordination notice to each affected loop in the same tranche. The notice is coordination, not authority: the receiving loop adopts, amends, or declines under its own instruments. | TRANSCRIBED — `AGENTS.md` change-notice rule; D-GOV-21 M6 |
| **D-12** | Developmental machinery is **product scope**, not surrounding process — a legitimate target of decomposition, deliverables, and acceptance rather than exempt overhead. | CLARIFIED — interpretation of §4.1 against D-GOV-21 packet §5.3 ("these guards are preconditions, not future tooling") |
| **D-13** | Once adopted, this PRD is amended only by a superseding instrument bound to a git SHA. **This commitment is the explicit immutability declaration for the adopted PRD** in D-16's sense: the adopted bytes are never overwritten at their path, and each revision is a new attributable act. | **PROPOSED** |
| **D-14** | **Source-currency obligation.** An adopted PRD that incorporates accepted doctrine carries a standing currency check over **nine classes** — invariant IDs still exist and still support what cites them; live registries still exist and still carry the relied-on rule; source anchors still resolve; repeated enumerations still match their registries; provenance labels and counts still reconcile and any change is linked to a valid superseding instrument; and concordance with `docs/DIRECTIVE.md` §1 holds. The classes are enumerated in annex §4, where **five are mechanical and four require semantic judgment**. It pairs the **SourceCorpusBasis** (the sources) with the **containing commit** of the adopted bytes (the candidate). **The check is not built** — no generator, schema, or executable check exists at this basis; building it is a precondition of relying on it. **A currency failure is a REVIEW finding routed to the owner — never an automatic amendment** (K-AUTH-1; D-GOV-02). | **PROPOSED** |
| **D-15** | The first root decomposition demonstrates **coverage across all four categories** of §4.1 — each category has decomposition coverage or a recorded, reasoned deferral. This constrains coverage demonstration only; it does **not** prescribe the partition (§4.3). | **PROPOSED** — strikeable without affecting any other commitment |
| **D-16** | **Attributable change control over approved content.** Any change to previously approved content requires a **new attributable act bound to the resulting SHA**, and prior approved bytes **remain recoverable in Git**. Only artifact classes **explicitly declared immutable** — decision records, accepted candidate packets, and snapshots — are never overwritten at their path. **Living authoritative surfaces amend in place through accepted commits**: `AGENTS.md`, `docs/DIRECTIVE.md`, `docs/SPEC.md`, `docs/TYPES.md`, status files, and other current-state surfaces are meant to be edited, and freezing their pathnames would break the product rather than protect it. | **PROPOSED** — pattern basis: D-2's two immutable record classes; K-SNAP-1 (pointer files may be overwritten, snapshot folders must not); K-AUTH-2 (approvals bind to a SHA). Stating it as a general change-control commitment is new and takes effect only on adoption |

**Retired identifier — D-3.** `D-3` is deliberately absent. The
exact-candidate-SHA procedure it once carried is **not a product requirement**;
it is an **OBSERVED practice statement** at §6.2, which makes no authority
claim. **The identifier is retired and never reassigned** — D-4 through D-16
keep their IDs so that every cross-reference in the annex, the prior revisions,
and this run's record stays valid, and no future commitment may reuse `D-3`.

### 5.4 Evidence

| ID | Commitment | Label and source |
|---|---|---|
| **E-1** | Every orchestration run persists a durable, versioned record tree under `_Coordination/AgentRuns/<RunID>/` capturing plan, work graph, briefs, returns, notices, dispositions, amendments, and final handoff state. Run IDs are created only when a real run begins; placeholder runs and briefs presented as executed children are prohibited. | TRANSCRIBED — `docs/SPEC.md` §9.8; `execution/_Coordination/LOOP_INIT.md` §5 |
| **E-2** | Phase-boundary decisions terminate in immutable snapshots; stopping work emits an explicit handoff state; each lawful tranche appends a minimal receipt. | TRANSCRIBED — `AGENTS.md` snapshot and handoff-state rules; K-SNAP-1; `LOOP_INIT.md` §7 |
| **E-3** | The three SHA roles are distinct and recorded distinctly: the **owner act binds approved content to its candidate SHA**; the **publication SHA identifies the durable ruling record**; the **EffectiveSHA identifies applied state**. | TRANSCRIBED — K-AUTH-2; D-GOV-21 record header. |
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

#### The exact-candidate-SHA procedure — an observed practice, not a rule

**[OBSERVED]** A five-step procedure has been exercised three times on
substantial governance proposals: **commit the exact candidate**; **record its
SHA**; **have the owner rule on that exact commit, recorded verbatim in a
fence**; **publish the ruling as a separate durable record**; **record the
merged implementation commit**, returning for exact-prose re-acceptance if
implementation would change approved prose. The instances of record are
**D-GOV-18** (approval at an exact commit), **D-GOV-19** (candidate SHA plus a
separate exact-prose ruling), and **D-GOV-21** (packet §14 mechanics;
`AcceptedCandidateSHA` / publication / `EffectiveSHA`).

**This states what the record shows and claims nothing more.** The actual
invariant is **K-AUTH-2** — every approval binds to a specific git SHA and is
voided by content change — and K-AUTH-2 **admits other vehicles**: a PR
approval against branch HEAD satisfies it differently. No governing clause
requires this particular multi-SHA packet procedure of every substantial
proposal, and **this document asserts none**. The procedure is available when
consequence warrants it, and professional judgment selects the vehicle.

**[CLARIFIED]** Promotion of the pattern into a PROPOSED requirement remains
available if evidence later shows that selecting among approval vehicles
causes ambiguity or failure — as a governed default with stated criteria, or
as a mandatory rule with "substantial" defined. Leaving it OBSERVED is the
product's own movement applied to itself: practice supplies evidence, evidence
informs judgment, and judgment alone makes the rule.

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
and ratifies nothing including itself — adoption is the named instrument's act,
performed by the owner (K-AUTH-1); it **records** the five owner rulings of §9
but performs none of the follow-on obligations they create, including the §9.1
concordance obligations; it creates no `PKG-*`/`DEL-*` and authorizes no
materialization;
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

**[PROPOSED]** Release is a **separately human-gated lifecycle judgment** over
whether the current product state may be released — the third judgment of
§4.2. It draws on **both** operative evidence and developmental evidence, and
is informed by validation results, decomposition coverage, and guard state.
**None of those releases Chirality Root mechanically**, and none of them
constitutes the judgment. Release occurs only when the owner performs the
applicable explicit release act.

**It is not an iteration decision.** Release asks whether what exists may go
out, not whether the product should change. A release judgment may be negative
with no change proposed, or positive with changes pending; neither outcome is
a decision to change the product.

**[TRANSCRIBED] Supporting basis:** K-AUTH-1 (only humans author binding
approvals; no agent may issue work for reliance); D-GOV-02 (a BLOCK is
mechanically bounded to its declared observation boundary and never a global
safety verdict); `docs/DIRECTIVE.md` §7 (the runtime pilot "does not authorize
… release, publication, issuance, or professional reliance"); K-DOMAIN-4
(validation-passed is necessary, not sufficient).

---

## 9. Owner decisions — all five RULED

D-GOV-21 packet §11 expressly withheld four decisions and routed them here;
the first adversarial review identified a fifth. **All five are now ruled by
the owner, in-session, 2026-07-25.** This section is the **record of what was
decided** — the option slates are compressed to what was offered and what was
selected; the full slates as presented, with their consequences, remain in the
immutable prior revisions and in this run's briefs and reviews.

**Status of these rulings.** Each is an **owner act of record**. Recorded here
with its verbatim selection; **SHA-binding occurs at the adoption instrument**
(RD-3, §9.3), not in this file. Receipts of record: **Receipt 37** (RD-1) and
**Receipt 38** (RD-2..RD-5) in `execution/_Coordination/LOOP_RECEIPTS.md`.
Where a ruling diverges from an agent or reviewer recommendation, that is
recorded rather than smoothed over.

| # | Question | Ruling | Recorded at |
|---|---|---|---|
| **RD-1** | Genus wording | **C — two-level formulation** | §9.1 |
| **RD-2** | Jurisdiction and accountability | **A1 + B2**, with a declared evolution path | §9.2 |
| **RD-3** | Adoption instrument and concordance map | **A + y** | §9.3 |
| **RD-4** | Placement vs. the export boundary | **D — split with pointer** | §9.4 |
| **RD-5** | v1 user scope | **A**, on a staged A → B → C trajectory | §9.5 |

### 9.1 RD-1 — Genus wording · **RULED**

**Status: RULED** — owner, in-session, 2026-07-25. Recorded in Receipt 37.
**SHA-binding occurs at the adoption instrument** (RD-3), not here; this
section is the record of the act, not the act's binding surface.

**Selection, verbatim as recorded from the selection interface:**

> "C — Two-level formulation"

**Ruled genus text** — option C's formulation, originating in the first
independent adversarial review and reproduced exactly:

> "Chirality Root is the canonical human-governed application environment
> and generative operating form for governed professional knowledge work.
> It contains a filesystem-native agent operating system together with the
> normative basis, developmental machinery, evidence, and human judgment
> by which that operating system is formed and governed."

**The slate as presented** (retained so the ruling is legible against what was
offered):

| Option | Content | Disposition |
|---|---|---|
| **A** | Retain `docs/DIRECTIVE.md` §1's ratified genus; reword `README.md`. | Not selected |
| **B** | Adopt `README.md`'s genus; amend `docs/DIRECTIVE.md` §1. | Not selected |
| **C** | A two-level formulation: genus plus explicit differentia, stated once and propagated. | **SELECTED** |
| **D** | Defer: adopt with the conflict recorded and both variants cited. | Not selected |

#### Follow-on concordance obligations created by this ruling

The ruling settles the genus **for this PRD**. It does **not** by itself change
any governance surface. Three obligations follow; **none is performed in this
candidate**, and each is routed to the adoption/implementation tranche:

| # | Obligation | Nature |
|---|---|---|
| **(a)** | **Supersede the ratified `docs/DIRECTIVE.md` §1 genus clause** through an exact-prose, human-gated act on the D-GOV-21 pattern (enumerated supersession, exact candidate prose, exact-prose gate, human-gated merge). | Required. Until it lands, the ratified clause **remains in force as written** and this PRD claims no amendment to it. |
| **(b)** | **Reword `README.md`** to the ruled genus. | Required. `README.md` is a non-binding derivative surface (D-GOV-21 packet §3b), so this is propagation, not supersession. |
| **(c)** | **Survey SPEC / TYPES / `AGENTS.md` prose** that leans on "operating system" and propagate where the ruled two-level formulation changes the sense. | Required as a **survey** — its scope is an output of the survey, not assumed here. |

**Sequencing note [CLARIFIED].** Obligation (a) touches ratified root `docs/`
— the instruction surface — so it is an **M2 governance tranche** requiring
independent owner authorization, a single serialized integration owner, a
tranche manifest, and routed notices (D-GOV-21 M2/G4/M6). It is not a
side-effect of adopting this PRD. Whether it runs before, with, or after
adoption is itself sequencing the owner controls; **C-1 does not close until
it lands**.

### 9.2 RD-2 — Jurisdiction and accountability · **RULED**

**Status: RULED** — owner, in-session, 2026-07-25; Receipt 38. Two axes were
offered: **jurisdiction** (A1 single root owner / A2 owner plus named delegates
/ A3 governing body with a quorum rule) and **accountability** (B1 one
accountable human per consequential act / B2 one accountable owner per root).

**Ruling: A1 + B2**, with a declared evolution path. Owner verbatim:

> "A1+B2 could seemingly be scaled up to multi-practitioner using the PEC
> interface and a database, and attribution can be done more securely that
> way. If you agree I would go that way. And that database and PEC interface
> are not current scope. That can be something that may be incorporated as
> Chirality morphs and responds to usage with ongoing development and
> refinement."

**Agent 0 concurrence, recorded because the ruling was conditioned on it
[OWNER_DECLARED — Agent 0 act of record]:** Agent 0 agrees. The prior agent
recommendation in Rev 4 was A1+B1; the owner ruled **B2** with a scaling path,
and that is the ruling. The recommendation is recorded as not followed.

**What v1 carries [OWNER_DECLARED]:**

| Axis | Ruled for v1 | Effect on this document |
|---|---|---|
| **Jurisdiction** | **A1** — a single root owner governs the root. | Matches the live registry exactly (`docs/governance_harness/human_actors.md`, one registered actor); no delegation or quorum machinery is introduced. |
| **Accountability** | **B2** — one accountable owner per root, inherited by acts within it. | v1 does not require per-act accountability across multiple people; the four §2.3 capacities need not be separately held (§2.3). |
| **Sub-decision: who may amend `human_actors.md`** | **Status quo** — owner-curated; additions and removals are owner edits published by CHANGE; **not extended programmatically**. | TRANSCRIBED as it stands: D-GOV-04; `docs/governance_harness/human_actors.md` §Maintenance. Under B2 this follows from jurisdiction A1. |

**Evolution path [OWNER_DECLARED, expressly not current scope].** A1+B2 is
ruled as scalable toward multi-practitioner attribution mediated by the **PEC
interface with database backing**, which the owner states would also make
attribution more secure. **The database and PEC interface are not current
scope**; they may be incorporated as the product responds to usage through
ongoing development. A PEC-mediated future would also revisit the
`human_actors.md` sub-decision. *The referent of "the PEC interface" is not
resolved in this document; it is `TBD` rather than guessed (K-INVENT-1), and
the owner fixes it if and when that scope is opened.*

**Reconciliation with the substrate ruling [CLARIFIED].** Under **D-GOV-01**
(Option A, RULED 2026-07-01) git-tracked authored plain files are the **sole
authority** for Chirality governance state, and any database is a rebuildable
projection **never citable as authority**. A future PEC/database layer
therefore supplies the attribution **mechanism** while the authoritative
**record** stays file-native — unless a future ruling consciously amends
D-GOV-01. That amendment is not proposed here and would be its own governance
act.

**[TRANSCRIBED] Standing clarification, unchanged by the ruling.**
`docs/governance_harness/human_actors.md` identifies **permitted authors of
binding governance records** (D-GOV-04 identity matching). It is not a registry
of every person accountable for situated professional work, and B2 does not
make it one.

### 9.3 RD-3 — Adoption instrument and concordance map · **RULED**

**Status: RULED** — owner, in-session, 2026-07-25; Receipt 38. Three
instruments were offered (**A** a `D-GOV-*` record on the exact-candidate-SHA
pattern; **B** a dedicated PRD adoption record class; **C** the
corpus-ratification pattern) and two map forms (**x** one-directional,
requirement → DIRECTIVE §1; **y** bidirectional coverage matrix with uncovered
items marked `TBD`). Both carried the agent recommendation A+y.

**Selection, verbatim as recorded from the selection interface:**

> "A+y (Recommended)"

**What this fixes [OWNER_DECLARED]:**

| Element | Ruled |
|---|---|
| **Instrument** | A **`D-GOV-*` decision record** using the **exact-candidate-SHA pattern** over the exact bytes of this adoption-ready revision. It reuses machinery exercised three times (D-GOV-18/19/21 — see the §6.2 practice statement) and inherits register visibility and SHA binding (K-AUTH-2). |
| **Concordance map** | **Bidirectional** (form y): PRD ↔ `docs/DIRECTIVE.md` §1, with uncovered items on either side marked `TBD`. This is the artifact **F5** is checked against, and only the bidirectional form exposes drift in both directions. |
| **Sequencing** | Absent contrary owner direction, the map is drawn against **`docs/DIRECTIVE.md` §1 as it stands**, recording the RD-1 divergence as a known open item. **§9.1 obligation (a) — the exact-prose supersession of that clause — lands in the adoption/implementation tranche**, not before the map. Stated also at §10.3. |

**[CLARIFIED]** Choosing the D-GOV family means a product-requirements act is
hosted alongside governance acts. That was the offered cost of option A and is
accepted by the ruling; it is recorded here so the register's later readers
know the choice was deliberate.

### 9.4 RD-4 — Placement relative to the public-export boundary · **RULED**

**Status: RULED** — owner, in-session, 2026-07-25; Receipt 38. Packet §11 item
4 records this as a **publication decision**. Four placements were offered:
**A** root `docs/` (exported); **B** root `execution/` (not exported); **C**
root `docs/` with an export exclusion; **D** a split. No agent recommendation
was offered among A, C, and D — the disclosure dimension was the owner's to
weigh.

**Selection, verbatim as recorded from the selection interface:**

> "D — Split with pointer"

**What this fixes [OWNER_DECLARED]:**

| Element | Ruled |
|---|---|
| **Adopted bytes** | Placed in **root `docs/`**, publishing through the **existing** export allowlist — `docs` is already a root directory in the export profile, so **no boundary change occurs** and packet §4's non-goal is not offended. |
| **Candidates and revision evidence** | **Remain in root `execution/`** as immutable history, including this file and every prior revision. |
| **Pointer** | A pointer **identifies the adopted exact bytes**. This imposes **no two-way concordance burden**: the `execution/` candidates are historical evidence, not a maintained parallel copy. |
| **Future amendments** | The adopted PRD joins the instruction surface, so **every amendment is an M2 instruction-surface tranche** requiring independent owner authorization, a tranche manifest, routed notices, and export-manifest regeneration (D-GOV-21 M2/G4/M6). |

**[CLARIFIED]** The split mirrors the existing `_PROPOSALS/` vs `_DECISIONS/`
separation: the candidate surface holds what was proposed and how it changed;
the doctrinal surface holds what was adopted. **Placement is performed by the
adoption tranche, not by this file** — nothing here writes to root `docs/`.

### 9.5 RD-5 — v1 user scope · **RULED**

**Status: RULED** — owner, in-session, 2026-07-25; Receipt 38. Three scopes
were offered: **A** the present owner-practitioner; **B** individual
professional knowledge workers generally; **C** multi-practitioner
organizations. No agent recommendation was offered.

**Ruling: A for v1, on a staged progression A → B → C.** Owner verbatim:

> "It's for all of those, but I see it progressing over time as we start with
> A and learn from my use to make a better version for B which I can test out
> locally with multiple computers with multiple Agent 0 instances on each and
> learn from that and make a better C which is the target level of maturity
> for the platform."

**What this fixes [OWNER_DECLARED]:**

| Stage | Scope | Standing |
|---|---|---|
| **A** | The present owner-practitioner. | **v1 scope.** "User" in OBJ-1, OBJ-2, and OBJ-3 means this practitioner for v1 (§3). |
| **B** | Individual professional knowledge workers generally, with §2.2's responsibility model activating where applicable. | **Declared trajectory.** Informed by learning from A; **tested locally across multiple computers with multiple Agent 0 instances on each.** |
| **C** | Multi-practitioner organizations. | **Declared trajectory and the stated target level of maturity for the platform.** Informed by learning from B. |

**[CLARIFIED] Why the trajectory is load-bearing rather than aspirational.**
It is what keeps OBJ-1's discoverability condition from being trivially
satisfiable at v1 (§3), and it is the reason the §2.3 capacities are stated as
separable even though v1 does not require them to be separately held (§2.3).

**[CLARIFIED] Where the B-stage test intent already connects.** Multiple
computers each running multiple Agent 0 instances is exactly the population
**OBJ-6** and **§6.3** speak to — declared write ownership and reconstructible
run state as concurrent Agent 0 activity grows — and it is the kind of
deployment the shared runtime pilot (**D-GOV-20**: one opt-in per-user daemon
owning engines, sessions, delegation, and turn locks, with checkout-contained
project authority) already anticipates. **This states a connection, not a new
commitment**: no objective, requirement, or runtime obligation is added here.

**[CLARIFIED] Interaction with RD-2.** The RD-5 trajectory and the RD-2
evolution path point the same direction and are governed separately: RD-5
stages *who the product is for*; RD-2 (§9.2) stages *how attribution and
jurisdiction would scale*, and its B/C-stage machinery — the PEC interface and
database — is expressly not current scope.

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
  explicitly labelled derived and non-authoritative.
- It is **specified for regeneration and proposed for checking** — annex §6
  gives the regeneration method and annex §4 specifies the D-14 check classes.
  **No generator, schema, or executable check exists at this basis**, and
  **four of the nine check classes require semantic judgment** rather than
  mechanical comparison. The annex is the surface D-14 *would* run against;
  D-14 is PROPOSED and its capability is unbuilt.
- **It is never itself adopted. Adoption, if it occurs, binds the exact bytes
  of this main PRD only.**

The inventory sits in the annex rather than here to prevent the PRD from
becoming another drifting registry — the failure mode already observed in
`docs/CONTRACT.md`'s invariant index (C-2) and `README.md`'s export
description (C-4).

### 10.2 Conflicts surfaced

**These are not reserved decisions and none was ruled by the §9 rulings.** One
is resolved in principle pending concordance; **C-2, C-3, and C-4 remain open**
and carry `HumanRuling = TBD` into the adoption instrument. **C-3 is expressly
flagged for owner confirmation at that instrument**, because it concerns owner
testimony this document could not verify. Two previously-recorded, non-new
items (the K-WRITE-2 explanatory-gloss debt and the accepted packet
`UNRESOLVED_SOURCE_REF` WARN) are carried in the annex rather than restated
here.

| # | Conflict | Sources | Disposition |
|---|---|---|---|
| **C-1** | **Genus wording.** `docs/DIRECTIVE.md` §1 names an "agent operating system"; `README.md` names an "application environment"; the ruled genus (ID-0) is a two-level formulation differing from both. | Ratified governance vs. a non-binding/derivative surface (D-GOV-21 packet §3b) vs. the RD-1 ruling | **`RESOLVED-IN-PRINCIPLE — concordance pending`.** RD-1 is RULED (§9.1) and settles the genus for this PRD. **It stays listed** because the ratified DIRECTIVE §1 clause remains in force until obligation (a) lands, and `README.md` until (b). **Closes fully only when the concordance tranche lands.** |
| **C-2** | **Invariant-index arithmetic.** `docs/CONTRACT.md` §1 states "27 stable invariants across 12 subsections" and its index table ends at K-DOMAIN-4, but §1.13 defines seven further invariants absent from that index; the §2 enforcement map does reference two of them. The live catalog holds 34 across 13. | `docs/CONTRACT.md` §1 index vs. §1.13 and §2 | **New find** (Rev 1). Not amended here — ratified instruction surface. Recommend an M2 correction tranche. `HumanRuling = TBD` |
| **C-3** | **Historical-note date.** The sealed brief states in-repo history begins 2026-02-18; git shows the first commit is 2026-05-18 and no in-repo file asserts the earlier date. | Sealed brief vs. git history at the accepted basis | §1.1 ID-4 records the verified git fact; the brief's date is surfaced, not adopted and not silently corrected. **Expressly flagged for owner confirmation at the adoption instrument** — it bears on ID-3 owner testimony, which no in-repo source can settle. `HumanRuling = TBD` |
| **C-4** | **Export description vs. export profile.** `README.md`'s public-export section omits `runtime/`, which the export profile's root-directory allowlist includes. | `README.md` vs. `exports/chirality-app/export_public.py` | **New find** (Rev 1). Live profile governs (K-AGENTS-1 principle; `README.md`'s own guidance). Routed as propagation. `HumanRuling = TBD` |

### 10.3 Adoption mechanics

**[TRANSCRIBED]** Adoption is an owner act on a separate instrument. What it
requires, on the cited sources: **exact bytes** of this revision bound at a
named SHA; the **concordance map against `docs/DIRECTIVE.md` §1** (packet §11
item 3); and the **owner ruling recorded verbatim** and attributed to a
matching registered actor (D-GOV-04), SHA-bound at publication (K-AUTH-2). No
agent act substitutes for any of these (K-AUTH-1).

**[OWNER_DECLARED] What RD-3 fixed** (§9.3): the instrument is a **`D-GOV-*`
record on the exact-candidate-SHA pattern**; the map is **bidirectional**, with
uncovered items on either side marked `TBD`.

**[OWNER_DECLARED] Sequencing of the map against the RD-1 divergence.** The map
is drawn against **`docs/DIRECTIVE.md` §1 as it stands**, recording the RD-1
divergence as a known open item (**C-1**, §10.2). **§9.1 obligation (a) — the
exact-prose, human-gated M2 supersession of that clause — lands in the
adoption/implementation tranche**, after and separately from adoption. The map
drawn at adoption therefore records a divergence it does not close; **F5**
tests that the divergence does not become permanent and unrecorded.

**[TRANSCRIBED] Carried into the instrument as open items:** conflicts **C-2**,
**C-3**, and **C-4** (§10.2), none of which the §9 rulings addressed, with C-3
expressly flagged for owner confirmation.

**[TRANSCRIBED]** Until adoption, **every PROPOSED item here is inert** — the
v1 boundary, OBJ-1..OBJ-7, D-13, D-14, D-15, D-16, §7.2 governed promotion,
§8.3 release authority, and F4–F6. TRANSCRIBED commitments remain in force
regardless, because their authority is their own source.

#### The final adoption transformation — step 2, completed here [CLARIFIED]

The terminal mechanics specified in Rev 3 have two steps, and **this revision
is step 2**.

**Step 1 — candidate revisions (closed).** Candidate revisions iterated under
independent adversarial review: Rev 1 → Rev 2 → Rev 3 → Rev 4. Each remains
**immutable historical candidate evidence** at its own SHA (Rev 1
`f15d51277`; Rev 2 `a72c2cd06`; Rev 3 `f9d33fcd9`; Rev 4 `ae5a476f4`) and is
superseded by this revision rather than edited. Revising a candidate was not
editing an adopted artifact, so D-13 and D-16 did not apply to them.

**Step 2 — the final adoption-ready revision (this document).** All five owner
rulings are incorporated: the ruled genus (RD-1, §1.1/§9.1), the jurisdiction
and accountability model with its declared evolution path (RD-2, §9.2), the
adoption instrument and concordance-map form (RD-3, §9.3), the placement
(RD-4, §9.4), and the v1 user scope with its staged trajectory (RD-5, §9.5).
**§9 is now a record of what was decided and by which act, not an open
slate.** These are the bytes the adoption instrument binds.

**Normalization performed.** Requirement bodies carry the resulting commitment
and its provenance — **not the drafting history that produced them**. That
history is not lost: it lives in the annex §5 correction tables (Rev 1 → 2,
Rev 2 → 3, Rev 3 → 4, Rev 4 → 5) and in this run's record of briefs, reviews,
amendments, and receipts. In-body notes survive **only where they state a live
constraint** — why N-1 carries the domain-engine exception locally rather than
only in the never-adopted annex; that D-16 carries the general rule D-2
deliberately does not; that D-3's identifier is retired and not reassigned.
**This document does not carry its own drafting conversation.**

**Status model.** The banner states this file's status by **pointing outward**:
the named instrument carries the adopted status, and this file asserts no state
that the adoption act would falsify. Bytes asserting `NOT ADOPTED` or `binds
nothing` were rejected for exactly that reason — correcting them after adoption
would require a fresh attributable act under D-13/D-16 rather than an edit.
What the banner does assert stays true afterward: that agent authorship confers
no authority, that existence and commit are not approval, and that adoption
binds these exact bytes only.

**[TRANSCRIBED]** What adoption would **not** do: materialize anything under
root `execution/` (packet §6 step 9, behind the §5.3 gate), create a root
decomposition (step 8), or change the public-export boundary (packet §4).

### 10.4 Document control

| Field | Value |
|---|---|
| Status | `ADOPTION-READY — adopted only by the instrument named below`, Revision 5 — the **final adoption-ready revision** (§10.3) |
| Adopting instrument | A `D-GOV-*` decision record on the exact-candidate-SHA pattern over this file's exact bytes (RD-3, §9.3), to be staged after this revision commits. **That record carries the adopted status; this file does not.** |
| Authority of this file itself | None of its own. Agent authorship confers none (K-AUTH-1); existence, validation, commit, and Git transport are not approval. PROPOSED items are inert until the instrument's owner ruling. |
| SourceCorpusBasis | `main@7ac718c7e` (the cited governance corpus) |
| This revision's bytes | The containing commit, recorded by Agent 0 in the run record and receipt. This file asserts no SHA for itself. |
| Prior revisions | Rev 1 `f15d51277`; Rev 2 `a72c2cd06`; Rev 3 `f9d33fcd9`; Rev 4 `ae5a476f4` — immutable historical candidate evidence, superseded by this revision, not edited |
| Governing decision | D-GOV-21 (RULED 2026-07-25); candidate `c038c493e871c95871823281b45890ba9404624b`; publication `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`; effective `ee42157290618e3f84be0e0b651c041387ad6ee0` |
| Authorizing effect | D-GOV-21 effect 5 (PRD-development basis) |
| Run | `ROOT-PRD-LANE-A-20260725` (Lane A) |
| Companion | Concordance annex — derivative package, specified for regeneration, never adopted (§10.1) |
| Owner decisions | **All five RULED**, in-session 2026-07-25 — RD-1 (Receipt 37); RD-2, RD-3, RD-4, RD-5 (Receipt 38). SHA-binding at the adoption instrument. §9.1's three concordance obligations are routed downstream and **unperformed**. |
| Placement | **RD-4-D**: adopted bytes to root `docs/` (existing allowlist, no boundary change); this file and all prior revisions stay in root `execution/` as immutable evidence; a pointer identifies the adopted bytes. Performed by the adoption tranche. |
| Provenance counts | **§5 stable commitments — 42 total: 33 TRANSCRIBED (N-1..N-8, O-1..O-9, D-1, D-4..D-11, E-1..E-7), 5 CLARIFIED (N-9, O-10, D-2, D-12, E-8), 4 PROPOSED (D-13, D-14, D-15, D-16).** D-3 was withdrawn in Rev 5 (43 → 42; TRANSCRIBED 34 → 33) and its identifier retired, not reassigned (§5.3). Elsewhere: **5 OWNER_DECLARED owner acts of record** (the five §9 rulings, four carrying verbatim owner text and one — RD-2 — carrying a recorded Agent 0 concurrence); **5 OWNER_DECLARED** framing claims (ID-1, ID-2, ID-3, §4.1 categories, §4.2 loop) plus the §4.2 three-judgments statement; **TRANSCRIBED** identity items ID-1a and ID-4; **2 OBSERVED** items (the `README.md` genus wording, §1.2; the exact-candidate practice statement, §6.2); **3 TRANSCRIBED** falsifiers (F1–F3); **13 further PROPOSED** items (v1 boundary, OBJ-1..OBJ-7, §7.2 promotion relationship, §8.3 release authority, F4, F5, F6). |
| PROPOSED inventory | **17 items, all inert until the adoption instrument's owner ruling:** D-13; D-14; D-15; D-16; the v1 boundary (§3); OBJ-1; OBJ-2; OBJ-3; OBJ-4; OBJ-5; OBJ-6; OBJ-7; §7.2 governed-promotion relationship (items 1–4, one commitment); §8.3 release authority; F4; F5; F6. Membership unchanged from Rev 4. |
| Open, not ruled | Conflicts **C-2**, **C-3**, **C-4** (§10.2) — carried into the adoption instrument; C-3 expressly flagged for owner confirmation. |
| Next act | Stage the **adoption instrument** (RD-3-A) over these exact bytes, with the bidirectional concordance map (RD-3-y) drawn against `docs/DIRECTIVE.md` §1 as it stands. Then, separately sequenced: §9.1 obligations (a) supersession, (b) `README.md` reword, (c) SPEC/TYPES/`AGENTS.md` survey; and the RD-4-D placement with its pointer. |
