# T1 terminal return — thesis foundation (verbatim)

FAN-IN DELTA (supervising session, recorded per LOOP_INIT stance): T1's
claim that "wheel / five governed representations / composition thesis"
occurs NOWHERE in the repo is overbroad — the phrase originates in the
derivative 07-28 tandem review's own section heading
(`plans/chirality_program_architecture_tandem_comparison_2026-07-28.html`,
"An interpretive seven-spoke wheel: five governed representations, with
rim behavior unproven"). T1 is correct that the THESIS corpus does not
contain it; the metaphor is review-coined, not thesis-grounded, which
makes T1's substantive finding (the thesis ontology actively resists
multi-representation synchronization in the governed record) stand and
sharpen. Live sources win over both returns on any further disagreement.

All investigation complete. Here is the structured return.

## Corpus map

`docs/thesis/` is a 16-file draft thesis plus a planning subfolder, titled **"Systems Engineering of LLM Agent Governance for Regulated Professional Engineering Practice — The Chirality Thesis"** (Ryan Tufts, P.Eng., 2026). Reading order and roles (per `docs/thesis/README.md` status table and `00_front_matter.md` ToC):

| File | Role |
|---|---|
| `00_front_matter.md` | Abstract, Author's Note, ToC. States the research question and the five novel contributions |
| `01_introduction.md` | Problem (LLM output carries no intrinsic epistemic warrant), approach, five contributions, whole-system category ("governed application environment") |
| `02_literature_review.md` | Five literature domains: agent architectures, hallucination, formal methods/safety-critical SE, professional regulation, epistemic frameworks (Sowa, BWW, provenance) |
| `03_philosophical_framework.md` | Four pillars (ontology/epistemology/praxiology/axiology); §3.6 chirality of knowledge, accountability gap, configurational multiplicity, six philosophical precedents (Bohr, Polanyi, Smith, Sellars, Brandom, +) |
| `04_architecture.md` | Filesystem-as-state, entity model, dual-graph model, lifecycle, Agent 0/1/2 hierarchy, write-scope quarantine, invariants, control loop |
| `05_epistemic_architecture.md` | Core novelty: six primitives (claim/warrant/status/gap/conflict/ruling), four enforcement mechanisms, warrant lifecycle UNWARRANTED→CITED→REVIEWED→AUTHENTICATED |
| `06_professional_practice.md` | APEGA "Relying on the Work of Others" mapping; AI agents as "others" |
| `07_se_design_analysis.md` | Eight SE disciplines as the implementation mechanism; control-theory reading of the runtime |
| `08_implementation.md` | Implementation evidence; §8.6 honest gap assessment incl. §8.6.2 soft enforcement |
| `09_discussion.md` | Limitations (incl. §9.2.4 instruction-level enforcement, §9.2.6 over-proceduralization), generalizability, §9.3.6 alignment ("align the system of use, not the model") |
| `10_conclusion.md` | Restates the five contributions |
| `appendix_a_invariant_catalog.md` | R1–R17, I1–I10, K-* catalog, regenerated 2026-07-02 from live `docs/CONTRACT.md` |
| `appendix_c_apega_mapping.md` | Clause-by-clause APEGA mapping table |
| `appendix_d_framework_s.md` | The existential conjecture (modal-notation "double commitment"), explicitly non-foundational; §D.8 records the origin |
| `references.md`, `glossary.md` | Verified references; glossary |
| `bigger-picture/` | Explicitly **not** thesis chapters: three draft planning artifacts (domain-engine PRD amendment, OpenPipeStress integration/development plans), preserved as "historical seeds" of the domain-engine and piping tracks |

There is no Appendix B — the agent index is the live root `AGENTS.md`. Critical status fact (`README.md` "Warrant Status"): every chapter is agent-drafted under owner direction; the thesis sits at **CITED/REVIEWED, never AUTHENTICATED**, and "per K-CLAIM-1 the thesis therefore binds nothing and is not a governance surface; on any disagreement, the governed record... governs."

## The nine domains: origin and derivation

**The nine domains do not appear anywhere in `docs/thesis/`.** Zero hits for "nine domains", "3×3", "Prioritization", or "Action Item" across the corpus. They are a **separate, older intellectual stream**: three owner-authored Word documents from **October 2025** (predating most of the repo's governance corpus), preserved byte-for-byte at `plans/chirality-task-management/sources/` under `SOURCE_MANIFEST.md` (status `NON_AUTHORITATIVE_SOURCE_CORPUS`, SHA-256 pinned):

- `9_domains_task_management.4.1.docx` (v4.1, 2025-10-29) — the matrix and its concentric expansions
- `9_domains_task_management_explained.3.1.docx` (v3.1, 2025-10-19) — the professional argument
- `9_rules_task_management_deliverables.1.docx` (v1.0, 2025-10-19) — operating rules

**Axes: there are none. The matrix is asserted as a mnemonic, not derived.** The "explained" document is explicit (I extracted the docx text; quoting the derivation-refusing passage):

> "Knowledge work doesn't progress in straight lines... the path along that sequence looks more like a bee's flight path rather than a straight line... **That's why I present task management as a matrix. This acts like a mnemonic device to recall the domains where our attention is required but not locking into a mental model of a particular sequence of events or actions.**"

and: "Together, these nine domains form a complete scanning framework. It is a simple 3x3 matrix that acts as a diagnostic scanning tool... **It is a tool for thinking, not a rigid workflow**."

The only structural claim is **positional, not axial**: laid out row-wise as (Action Item, Assignment, Prioritization / Deliverables, **Work**, Planning / Approval, Checking, Decisions), with "Notice that 'Work' sits at the center — task coordinators don't manage work execution itself, they manage the coordination boundaries." The matrix then expands concentrically: Workers (gold) at center → Task Management (green) "coordination membrane" → Project Controls (blue) → Project Management (purple), with role-responsibility overlays (Project Manager/Engineer/Controller/Document Controller). Note the nine-domain cells are grouped by color, not by row/column semantics — green domains (Action Item, Assignment, Deliverables, Approval) generate logged tasks; gold (Work) does not.

**It is NOT derived from the Chirality semantic algebra.** The canonical semantic matrices (`skills/semantic-matrix-build/SKILL.md` §"Matrix construction rules") are Matrix A "Orientation" (3×4: normative/operative/evaluative × guiding/applying/judging/reviewing) and Matrix B "Conceptualization" (4×4: data/information/knowledge/wisdom × necessity/sufficiency/completeness/consistency) — no dimensional or vocabulary overlap with the nine domains. Two independent 3×N matrix habits from the same mind, not one derivation.

The live normative statement is `plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md` §4: the nine domains are "a 3×3 scanning matrix: a mnemonic and diagnostic lens," with the owner quote "the nine domains are scanning lenses for agents to coordinate their work on, not any kind of sequence or specific workflow," plus a per-domain ownership table (Task Management **owns** only Action Item; all eight others are cited-by-reference to their existing owners). Adopted via D-GOV-32 (commit 19359de39) into `agents/AGENT_TASK_MANAGEMENT.md`.

## The wheel and the composition thesis

**NOT FOUND — anywhere.** The literal terms "wheel," "rim," "hub" (in this sense), "five governed representations," and "composition thesis" occur nowhere in `docs/thesis/`, nowhere in root governance, and nowhere in the repo or its git history except the requesting run's own manifest (`execution/_Coordination/AgentRuns/GOV-EXPLORE-FIVE-20260801/RUN_MANIFEST.md:16`). The metaphor is the supervising session's coinage, not the program's recorded vocabulary. I will not guess which structure it names, but here is the complete inventory of candidate referents, and — the substantive finding — the thesis's own position, which is *anti*-wheel:

1. **The thesis's representation doctrine is single-hub with no rim at all.** `04_architecture.md` §4.2.1: "the project graph has no representation other than the filesystem itself. There is no translation layer, no secondary index, and no remote service." §4.2.3 explicitly *precludes* "Centralised dependency graphs that must be kept synchronized with deliverable-local registers." `03_philosophical_framework.md` (¶ near line 28): "There is no separate representation, no translation layer, no synchronization discipline." A wheel of five synchronized representations is precisely what the thesis forbids inside the governed record.
2. **The closest hub/rim structure in live doctrine is the derivative-package rule** (`AGENTS.md` §Governance Integration Rules): accepted decomposition truth is the hub; "regenerated KTY-local artifacts, `_Aggregation` outputs, hypergraph snapshots, audit snapshots, concordance packages, and publication packages" (six, not five) are derivative and "must never be treated as a substitute for decomposition truth." Under this reading, "rim proof" would mean demonstrating that a derivative-to-derivative relation can be relied on without re-deriving through the accepted hub snapshot — which the doctrine currently prohibits rather than proves.
3. **The piping export architecture is an explicit hub-and-adapter wheel** (`domains/piping-design/plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md`): "Keep a clean internal model that is richer than any one vendor format"; "Convert canonical model to target representation" (line 585); "The core application should not know CAEPIPE syntax. It should know only the canonical model and the adapter contract" (line 604). The unproven part: the import-and-analysis validation harness against CAEPIPE MBF is planned, not run. Similarly `projects/chirality-piping/docs/PRD.md` §5.2 "Schema-Backed Physical Model Is the Source of Truth" with physical→analytical transformation (PKG-13 DEL-13-04) and downstream 3D/stress representations.
4. **Exactly-five candidates**: DRAWING_EXTRACT's five `(drawing_type)` targets — DRAWING_SET, PFD, P_AND_ID implemented; **ISOMETRIC/GA "stubbed fail-fast"** (`AGENTS.md` agent index) — five governed drawing representations with an unproven arc; the five-file minimum viable fileset `_STATUS/_CONTEXT/_DEPENDENCIES/_REFERENCES/_SEMANTIC` (`04_architecture.md` §4.3.3); the five control variables (`07_se_design_analysis.md` line 291).
5. The nearest thing to a "composition thesis" *inside* the thesis is the **dual-graph model** (`04_architecture.md` §4.3.4): ANCHOR tree × EXECUTION DAG "together form a knowledge graph" answering vertical and horizontal questions — a claim that two representations compose because both are projections of the same files, never a synchronization proof.

Recommend the supervisor state which referent the metaphor intends; the thesis basis differs sharply between readings 2 and 3 (governance rule vs. product architecture), and reading 1 means the wheel is a post-thesis development the thesis's ontology actively resists.

## The core formal idea

Two distinct formal ideas share the name; the thesis deliberately ranks them.

**Primary (the name's meaning of record):** *Chirality = the permanent accountability gap.* `CHIRALITY_FRAMEWORK.md` §2.4 (Rev 3, D-GOV-19): "The framework is named for the permanent **accountability gap** between externalizable information and accountable knowing... This is the sole primary sense in which the framework calls knowledge *chiral*. The term marks an irreducible orientation: information can be presented, organized, and warranted, while knowing remains situated in the person who knows." Appendix D §D.7 supplies the bounded chemistry analogy (non-superposable mirror configurations; "one substrate can admit more than one configuration") and declares it deletable without loss. Appendix D's conjecture compresses the authentication act to one line: **S ⊢ (S ⊢ (M ∧ N)) → G** — the "double commitment": inner affirmation of meaning-as-necessary, outer affirmation of oneself as bound to that stance (interpretive analogue of REVIEWED→AUTHENTICATED, explicitly "analogue, not definition"). §D.8 records the pre-project origin: the insight, formed in the author's first LLM work in reflection on Ayat al-Kursi (Qur'an 2:255), "that meaning is not self-grounding," which "explains the architecture's most consistent refusal: at every level, the system declines to let computation manufacture warrant. That refusal was a commitment before it was a design."

**Secondary (the operational calculus):** the semantic algebra, now living only in `skills/semantic-matrix-build/SKILL.md`: *semantic multiplication* `*` "combines two semantic units into their intersection" (`sufficient * reason = justification`), semantic addition `+` groups, and interpretation `I(r,c,L)` collapses list cells via axis-anchor → projected contributors → centroid. Canonical matrices A (Orientation) and B (Conceptualization) generate C (Formulation), F (Requirements), D (Objectives), K, G, X (Verification), T, E (Evaluation) by matrix-product-shaped compositions, e.g. `L_C(i,j) = Σ_k (A(i,k) * B(k,j))`. The thesis demotes this explicitly (`03_philosophical_framework.md` §3.6.3): "The semantic algebra organizes a work product for a stated purpose; **it does not legislate the limits of knowledge**" — semantic lenses are "scaffolding rather than exhaustive categorizations" (configurational multiplicity).

## Thesis-to-practice mapping and divergences

**Direct mappings (thesis → live doctrine):**
- Agent 0/1/2 (`04_architecture.md` §4.5, three authority invariants: Type 2 cannot escalate; managers cannot override standards; human gates reserved against every agent type) → `AGENTS.md` runtime hierarchy verbatim in structure, with HELP_HUMAN as sole Agent 0.
- K-* invariants: Appendix A was **regenerated from live `docs/CONTRACT.md`** (27 K-* invariants, revision note 2026-07-02) — the thesis mirrors the registry, not vice versa; K-AGENTS-1 codifies "registry governs on disagreement," which was applied *to the thesis itself* (2026-07-18 R1–R12→R1–R17 drift correction, "narrative had drifted behind the live registry").
- "Instruction-text enforcement is soft": `08_implementation.md` §8.6.2 reproduces the CONTRACT §2 enforcement map, states "Instruction-layer constraints still depend on model conformance," names the five future-tooling invariants (K-STALE-1, K-VAL-1, K-MERGE-1, K-AUTH-2, K-DEP-2) as "the most significant gap," and `09_discussion.md` §9.2.4 gives the honest form: "a soft constraint, not a hard one... The system does not claim that instruction-level enforcement is sufficient alone. It claims that the multi-layer enforcement model contains failures to manageable scope." This is now standing doctrine (echoed in Task Management PRD reasoning about why emission-without-consumption fails).

**Divergences / outgrowths:**
- **Orchestration pattern.** The thesis's control loop (§4.8.3) is ORCHESTRATOR→WORKING_ITEMS→TASK→EVALUATION→CHANGE with `NEXT_INSTANCE_STATE.md` handoffs, "not continuous — human-triggered at each session." Live doctrine has outgrown this into `delegate_agent` managed children with sealed briefs, terminal fan-out/fan-in *and* supervised many-to-many agency, coordination notices, versioned brief amendments (`AGENTS.md` §Multi-Agent Orchestration) — none of which the thesis describes. §8.6.2's paragraph about the "managed runtime" mechanical enforcement was patched in later and sits awkwardly against Ch4.
- **The 3×4 UI matrix** (§8.2.3) is explicitly legacy: "retained as a desktop navigation view... Agent authority and delegation follow Agent 0/1/2; the matrix" is a routing view — the thesis documents its own superseded taxonomy.
- **Naming recalibration**: D-GOV-19 (2026-07-23) forced Revision 3 — knowledge relocated into a situated knower, authentication made relational, and the accountability gap made "the **sole** primary chirality," retiring earlier readings where multiple dualities were chiral. The four-document kit's recursion was renamed a "fractal property... not a claim that one chiral duality recurs at every level."
- **Unproven empirics remain unproven**: §8.6.4 still carries "[TODO: Characterize the actual error rates observed in practice...]"; §9.2.1 concedes no controlled empirical validation. The governance-economics question (sibling task T4) is a live gap the thesis names but never fills.
- **The thesis's own status is the sharpest divergence**: the system's warrant lifecycle applied to itself leaves the program's intellectual foundation permanently CITED/REVIEWED and non-binding — the founding text is, by the founder's own invariant, not authority.

## Predictions and tensions vs recent developments

- **Task Management was predicted by the invariant catalog, not the nine-domains corpus.** Appendix A K-STALE-2 lists its enforcement point as "**Human triage queue**" — and the PRD candidate (§1) builds on exactly this: "K-STALE-2's declared enforcement point is a 'Human triage queue' (`docs/CONTRACT.md:100`) that exists nowhere in `docs/SPEC.md` or `docs/TYPES.md`. This product is that instrument." A three-word cell in the 2026-07-02 catalog is the thesis-side seed of D-GOV-32.
- **The 2025 rules docx predicted agentic adoption**: rule 9 — "Tools must serve the framework, not dictate it... Simpler tools that align with the framework... will enable agentic workflows with AI more easily" — written before the register/scanner design that now implements exactly that (deterministic scanner, no agent, no LLM).
- **Agent-driven loops strain §4.8.3.** "The architecture does not run agents autonomously between human interactions" is still formally true (loops are human-triggered), but the development-loop pattern, self-pacing project loops, and the D-GOV-20 daemon push far past the thesis's session-scoped picture; the thesis contains no account of standing loops, loop receipts, or parked lanes.
- **The Piping design-tool boundary is a faithful application, anticipated in outline.** `01_introduction.md` (§1.2, ¶40) already names "domain applications where a discipline requires deterministic computation (the domain-engine boundary, governed by invariants K-DOMAIN-1 through K-DOMAIN-4)," and the `bigger-picture/` seeds grew into the ruled records. The chirality-piping PRD's "full analytical engine, non-authoritative result" ("They are design-engine results... not professional reliance results," `projects/chirality-piping/docs/PRD.md` §3/§5.1) is the thesis's Central Distinction (`CHIRALITY_FRAMEWORK.md` §5) transposed into product scope: the boundary "is defined by claim authority," not solver capability.
- **Tension to watch:** the design tool's canonical-model-plus-representations architecture (and any "wheel" framing of multi-representation consistency) reintroduces exactly the translation layers and synchronization disciplines the thesis's ontology pillar prohibits for the *governed record*. The reconciliation is that the model lives behind the domain-engine boundary (engine store ≠ governed truth), but no thesis text yet argues why multi-representation synchronization is acceptable inside an engine while forbidden in the record. That argument is currently NOT WRITTEN anywhere.
- `09_discussion.md` §9.2.6 (over-proceduralization as displaced attention — "process artifacts become what the practitioner looks *at*") reads as a pre-registered warning about precisely the failure mode the Task Management evidence base then measured (29/30 notices never closed; emission enforced, consumption not).

## Reading list (owner's own eyes)

1. **`docs/thesis/appendix_d_framework_s.md` §D.8 "Origin"** (~15 lines) — the pre-project conviction, Ayat al-Kursi, and "the system declines to let computation manufacture warrant. That refusal was a commitment before it was a design." The whole program in one paragraph.
2. **`CHIRALITY_FRAMEWORK.md` §2.4 + §6–§7** — the sole-primary-chirality statement and the axiom "to know what you know, why you know it, and why you know why." (Root doc, but it is the thesis's declared primary source for Ch. 1/3/5/10.)
3. **`docs/thesis/09_discussion.md` §9.2.6** — the Polanyi-grounded over-proceduralization warning; the most self-critical passage in the corpus and the one most predictive of the notice-ledger failure data.
4. **`plans/chirality-task-management/sources/9_domains_task_management_explained.3.1.docx`**, section "The 9 Domains" (mise-en-place through "tool for thinking, not a rigid workflow") — the actual origin text of the nine domains; confirms the matrix is a mnemonic with Work at the hub, no derived axes.
5. **`docs/thesis/08_implementation.md` §8.6.2–8.6.4** — the enforcement map, the five soft invariants, and the standing `[TODO]` on empirical conformance rates; the exact edge of what the program has and has not proven about itself.

One caution for the fan-in: everything above from `docs/thesis/` carries the corpus's own label — CITED/REVIEWED, not AUTHENTICATED, binding nothing (README "Warrant Status"); where it disagrees with `AGENTS.md`/`docs/CONTRACT.md`, the registries govern.
