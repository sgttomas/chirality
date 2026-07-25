# Concordance Annex — Chirality Root candidate PRD (Rev 3)

> **Package role: `derived publication artifact` / DERIVATIVE PACKAGE.**
> **Status: NOT ADOPTED, and never adoptable.**
>
> This annex is the companion source-concordance artifact for
> `execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md` (Rev 3).
> It carries the detailed transcription inventory that Rev 1 held inline, so
> the main PRD can hold stable commitments and incorporate dynamic registries
> by reference.
>
> **What that status means, bindingly:**
>
> - **Derivative package** under the `AGENTS.md` derivative-package rule:
>   assembled from accepted upstream truth, citing its accepted upstream
>   snapshot, and **never a substitute for that truth**. On any disagreement
>   between this annex and a live source, **the live source governs** and the
>   delta is recorded.
> - **Derived publication artifact** under `docs/DECOMPOSITION_STANDARD.md`
>   §Package Architecture: **not the amendment surface**, explicitly labelled
>   derived and non-authoritative.
> - **Never itself adopted.** Adoption of the root PRD, if it occurs, **binds
>   the exact bytes of the main PRD only** (D-GOV-21 packet §11 item 3;
>   K-AUTH-1). Nothing in this annex can be adopted, ratified, or relied upon
>   as authority.
> - **Specified for regeneration; proposed for checking.** §6 gives a
>   regeneration *method* and §4 *specifies* the D-14 check classes.
>   **Neither is built.** At this basis there is **no generator, no schema,
>   and no executable check** — regeneration is a documented manual procedure
>   and D-14 is a PROPOSED obligation whose capability does not yet exist.
>   Two of the six check classes additionally require **semantic judgment**
>   and are not mechanizable as specified (§4). Do not describe this annex as
>   mechanically regenerable or mechanically checked.
>   *(Rev 3 correction: Rev 2 claimed present-tense mechanical regenerability
>   and checking. It had neither.)*
>
> **Accepted upstream snapshot:** `main@7ac718c7e`. Every anchor below was
> read and verified against the live file at that basis during run
> `ROOT-PRD-LANE-A-20260725` (Rev 1 authoring; carried through Rev 2 and
> Rev 3, with Rev 3's new and changed anchors verified in that revision).
> **Governing decision:** D-GOV-21, RULED 2026-07-25 — candidate
> `c038c493e871c95871823281b45890ba9404624b`, publication
> `75b7aa6d1fb019846ac76fb775df2fc1652ab8a8`, effective
> `ee42157290618e3f84be0e0b651c041387ad6ee0`.
> **Date:** 2026-07-25

---

## 1. How to read this annex

Section 2 maps every stable commitment in the main PRD §5 to its verified
source anchors. Section 3 lists the live registries the PRD incorporates by
reference — the things this annex deliberately does **not** enumerate.
Section 4 **specifies** what a D-14 currency check would inspect, marking each
class MECHANICAL or SEMANTIC (the capability is unbuilt). Section 5 carries
previously-recorded items that Rev 1 listed as conflicts C-5 and C-6 but which
were already recorded elsewhere and are not new finds, plus the durable
correction history for **Rev 1 → Rev 2** (§5.3) and **Rev 2 → Rev 3** (§5.4).
Section 6 records the regeneration contract and what building it would take.

Line numbers are given where they were directly verified; they are the most
fragile element of this annex and are the primary trigger for a D-14 anchor
check. **Section references govern over line numbers** where the two diverge.

---

## 2. Commitment-to-source concordance

### 2.1 Normative basis (main PRD §5.1)

| Commitment | Source anchors (verified at `main@7ac718c7e`) |
|---|---|
| **N-1** | `docs/DIRECTIVE.md` §2.1 Filesystem Is the Database (lines 151–161); §2.2 Git Is the Event Store (163–167); §5 constraint rows (293–295). D-GOV-01 Substrate authority — RULED Option A 2026-07-01, Ruling SHA `82a35c545282889841ce789c3e24f2ca68991ba1`. **Exception now carried in N-1 itself (Rev 3):** K-DOMAIN-1 (`docs/CONTRACT.md` §1.12, line 137) — domain engines own authoritative domain truth, and "Chirality governs the work around it … it is not the solver and is never the source of accepted engineering truth"; plus the §1.12 note (line 142) recording that engine-owned domain stores are "sanctioned authoritative domain truth under K-DOMAIN-1 and are exempt from the governance rebuildable-cache rule". `docs/DIRECTIVE.md` §2.1 itself points to the K-DOMAIN family for engine-owned stores. |
| **N-2** | `docs/CONTRACT.md` §1 Invariant Catalog (index at line 19; definitions lines 57–154). K-AGENTS-1 live-registry principle (line 131): "Where live registries … and narrative disagree, the live registry governs and the discrepancy is surfaced." |
| **N-3** | K-AUTH-1 (`docs/CONTRACT.md` §1.2, line 64); K-AUTH-2 (line 65); K-BIND-1 (line 66); K-GATE-1 (§1.7, line 100) and its D-GOV-02 note (line 102). `docs/DIRECTIVE.md` §2.3 Human Authority at Every Gate (169–175); §2 (line 59, content-addressed approval). |
| **N-4** | K-PROV-1 (line 114); K-INVENT-1 (line 115); K-CONFLICT-1 (line 116); K-CLAIM-1 (line 117). `docs/DIRECTIVE.md` §2.4 Evidence Over Plausibility (177–185); §2 epistemology mechanisms (43–53). |
| **N-5** | K-WRITE-1 (line 123); K-WRITE-2 (line 124); K-SNAP-1 (line 125). `docs/SPEC.md` §0.2.3 ScopePath containment (54–61) — normalization, resolution under `REPO_ROOT`, `SCOPE_OUTSIDE_WORKTREE` rejection. |
| **N-6** | `docs/DIRECTIVE.md` §Authority chain (line 7): DIRECTIVE → CONTRACT → SPEC → TYPES; `AGENTS.md`/`agents/` as live instruction surface; ratified governance controls on conflict. |
| **N-7** | `docs/DIRECTIVE.md` §2 The Four Pillars (27–133); §How the Pillars Relate (112–120); §The Pillars as the Ontology of Professional Accountability (122–133); §The Fractal Property (88–108). |
| **N-8** | `docs/DIRECTIVE.md` §3 Professional Responsibility Model (222–256): §3.1 AI Outputs Are Drafts (226–228); §3.2 Engineer-of-Record (230–240); §3.3 Tool competence (242–244); §3.4 Hierarchy of Authority (246–256). Activation-boundary clause at line 224 — see §5.3 of this annex for the Rev 2 correction. |
| **N-9** | Interpretation. Grounding: `docs/CONTRACT.md` §2 Enforcement Map Summary (165–178), which assigns every invariant a live enforcement point (agent instructions, TASK shell, human review, governance audit, runtime) rather than a documentary one. |

### 2.2 Operative product (main PRD §5.2)

| Commitment | Source anchors (verified at `main@7ac718c7e`) |
|---|---|
| **O-1** | `docs/DIRECTIVE.md` §2.6 (line 201, instruction-root membership); `docs/SPEC.md` §0.2.1 (line 44, "The instruction surface is read-mostly: changing it is a repo-wide governance action, not ordinary working-root execution"); `docs/TYPES.md` §1.4 Instruction Root row (lines 43–53). |
| **O-2** | Layer (a): `docs/SPEC.md` §9 (agent instruction structure); `AGENTS.md` §What Is an Agent? (line 17; operational-definition note 20–23). Layer (b): `AGENTS.md` terminology table, Tool row (line 33) — "a deterministic operation available to an agent; never a substitute for semantic judgment". Layer (c): `AGENTS.md` §Shared Runtime Doctrine (264–277), esp. "Generic runtime transport never grants project authority" (274–275); `docs/DIRECTIVE.md` §7 (316–335); `docs/CONTRACT.md` §1.13 (144–161), esp. the closing paragraph that the daemon's user-data files "do not grant an agent permission to write outside its checkout scope" (156–161). |
| **O-3** | `AGENTS.md` §Good Agents and Great Workflows, hierarchy table rows (48–50); §Agent 2 Construction Forms (58–78); §Delegation and Entry Rules (80–100). `docs/DIRECTIVE.md` §2 praxiology (line 65). D-GOV-11 (hierarchy, RULED 2026-07-11); D-GOV-12 (orchestration, RULED 2026-07-11); D-GOV-13 (dedicated Agent 2 requalification, approved through D-GOV-14 item 4, published `d22f80bf5d6c1190ce151df75d936bfcf4d38bc3`). |
| **O-4** | `AGENTS.md` §Delegation and Entry Rules (87–91). K-SEAL-1 and K-GHOST-1 (`docs/CONTRACT.md` §1.3, lines 72–73). D-GOV-17 (RULED 2026-07-18) — capability never confers authority regardless of steering content. |
| **O-5** | `AGENTS.md` §TASK Skill Capabilities (243–262), esp. "This file is not the complete skill registry" and "treat the live skill folder plus `skills/README.md` as the current skill registry". K-AGENTS-1 (line 131). Registries: `skills/README.md`, `tools/REGISTRY.md`. |
| **O-6** | `docs/SPEC.md` §0.2 Root Model and Path Anchoring (28–67): §0.2.1 `REPO_ROOT` (34–44), §0.2.2 `WORKING_ROOT` (46–52), §0.2.3 containment (54–61), §0.2.4 path reference discipline (63–67, machine-absolute-path prohibition). §0.3 Path Token Registry (71–91). `docs/TYPES.md` §1.4–§1.5. |
| **O-7** | `docs/SPEC.md` §1 Execution Root Layout (95–127); §3 `_STATUS.md` Lifecycle State (242 ff.), §3.3 Transition Rules (275 ff.). K-HIER-1, K-ID-1 (lines 57–58); K-STATUS-1 (86); K-STALE-1/2, K-VAL-1 (92–94). |
| **O-8** | K-DEP-1 (`docs/CONTRACT.md` §1.4, line 79) — deliverable-local registers authoritative; "There is no central dependency graph; generic read-only aggregation is on-demand via `_Evaluation/`; a calibrated corpus-concordance run may also inventory dependencies under `_Reconciliation/DeliverableConcordance/`." K-DEP-2 (line 80). `agents/AGENT_PROJECT_SETUP.md` line 155 — "`FULL_GRAPH` — dependency declarations are intended to form a complete DAG; compute blockers only from the declared graph"; also lines 218, 500, 620. **The invariant's own text provides for derived aggregation; Rev 1's flat "no central dependency graph" dropped that clause.** |
| **O-9** | D-GOV-21 §Effects items 1–4; packet §2 (57–78), §5 Replacement containment contract (147–250) — §5.1 why mandatory (149–167), §5.2 mechanisms M1–M7 (169–208), §5.3 guards G0–G4 and gate ordering (210–250). `docs/DIRECTIVE.md` §2.6 as amended (199–206); `docs/SPEC.md` §0.2.2 (48, 52) and §1 (97); `docs/TYPES.md` §1.4 (Working Root and Execution Root rows). Annex A application record: `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md` (25–28). **Packet-internal labelling note:** several M-items and all guards are labelled PROPOSED inside the packet, where PROPOSED means "new commitment, effective only if this record is ruled" (packet §5.2 label block, lines 171–172). The record is RULED, so they are in force. |
| **O-10** | Interpretation of O-1 and O-2 with the D-GOV-21 M2 gate (packet 180–190) and `docs/SPEC.md` §0.2.2 line 52 (second clause, as amended). |

### 2.3 Developmental machinery (main PRD §5.3)

| Commitment | Source anchors (verified at `main@7ac718c7e`) |
|---|---|
| **D-1** | `docs/governance_harness/_DECISIONS/` — 21 per-decision records plus `_REGISTER.md`. Register framing (lines 1–10): "this register is a navigational summary — on any disagreement the records govern." Record header pattern: D-GOV-21 lines 3–13. |
| **D-2** | D-GOV-21 `RecordConvention` field (line 12: "D-GOV-18/19 exact candidate-SHA ruling pattern; supersede-never-edit") and §Status note (26–28: "Any later correction to the transcription is a superseding act, not an edit"). D-GOV-17 line 168 (recorded supersede-never-edit exception entries). `D-GOV-21_IMPLEMENTATION_HANDOFF.md` (83–87: "amendment would void the AcceptedCandidateSHA"). **No root-wide clause states the absolute formulation.** Rev 2 kept the general rule under a CLARIFIED label; **Rev 3 narrows D-2 to exactly the two classes these anchors govern** — published D-GOV records carrying the convention, and ruled candidate packets bound to an `AcceptedCandidateSHA` — and moves the generalization to **D-16 (PROPOSED)**, so no CLARIFIED label does normative work. |
| **D-3** | D-GOV-21 packet §14 Ruling mechanics (369–391); D-GOV-21 record §Implementation gates (69–79). Precedents: D-GOV-18 (`_REGISTER.md` row — "I APPROVE D-GOV-18 items 1–8 at commit 9a900b3b76dda415cc4d41185350eb2e5a436302"); D-GOV-19 (Ruling SHA `981149df247fb6564768f8451e3b12dd591d9197`, AcceptedSourceSHA `deab7a961c1a5c9fde771039497e50343b681d46`). |
| **D-4** | D-GOV-04 (RULED 2026-07-01, Ruling SHA `82a35c545282889841ce789c3e24f2ca68991ba1`). `docs/governance_harness/human_actors.md` lines 3–14 (status, refuse-exit-2 behaviour, owner-curated maintenance clause) and line 20 (the single registered actor row). |
| **D-5** | D-GOV-02 (RULED 2026-07-01) severity table and caveats — five severities with exit-code semantics; "BLOCK means mechanically blocked within the declared observation boundary, never globally proven safe/unsafe"; human-only recorded override. D-GOV-17 M2 floor-plus-corrections. `docs/CONTRACT.md` §1.7 note (line 102). |
| **D-6** | `AGENTS.md` §Governance Integration Rules (heading line 174; the seven rules at lines 176–182). `docs/DIRECTIVE.md` §2.7 Governed State and Multi-Phase Closure (208–218). |
| **D-7** | `execution/_Coordination/LOOP_INIT.md` §1 Bootstrap (12–25), §2 Hand off to the standing plan (26 ff.), §4 Authority and evidence discipline (55 ff.), §5 Multi-agent orchestration (67–95), §6 Stops and write fences (96–114), §7 Closeout (115–129). `execution/_Coordination/CURRENT_WORKPLAN.md` (deterministic pointer; "Do not select a workplan by modification time, filename sorting, or narrative claims"). Standing workplan §Authority basis (20–27): "It carries no authority merely because it exists." |
| **D-8** | `execution/_Coordination/LOOP_INIT.md` §7 (115–127); standing workplan §Closeout (266–273); K-MERGE-1 (`docs/CONTRACT.md` §1.8, line 108); `AGENTS.md` agent index, CHANGE row. |
| **D-9** | D-GOV-21 packet §4 (135–137): "No waiver of the decomposition pipeline … Nothing in this record authorizes inventing packages from discussion." Standing workplan §Gated downstream item 2. |
| **D-10** | `exports/chirality-app/export_public.py` — profile mechanics at lines 21–51 and the boundary checks. `README.md` §Publishing Pipeline (202–217); §Public Export Boundary (172–198). K-EXPORT-1 (`docs/CONTRACT.md` §1.13). **Membership is deliberately not enumerated here** — see §3. |
| **D-11** | `AGENTS.md` agent-index change-notice rule (line 182). D-GOV-21 M6 (packet 202–207) and §3b propagation table (116–129). Live instances: the two routed notices recorded in `D-GOV-21_IMPLEMENTATION_HANDOFF.md` (48–51). |
| **D-12** | Interpretation. Grounding: D-GOV-21 packet §5.3 closing (249–250) — "these guards are preconditions, not future tooling"; `AGENTS.md` closure rule (line 179). |
| **D-13** | PROPOSED. No source; a new commitment extending D-2's convention to the PRD artifact class. |
| **D-14** | PROPOSED. Partial grounding: D-GOV-21 packet §11 item 3 requires the concordance map **at adoption** only. The standing obligation and its five additional check classes are new. Severity routing grounded in D-GOV-02 (REVIEW never gates) and K-AUTH-1 (no automatic amendment). **Rev 3: scoped honestly — the capability is unbuilt and two check classes are semantic (§4).** |
| **D-15** | PROPOSED. Partial grounding: `AGENTS.md` closure rule (line 179); the coverage-audit pattern (`agents/AGENT_AUDIT_DECOMP.md`); `docs/DECOMPOSITION_STANDARD.md` completeness requirements. The four-category coverage obligation itself is new. |
| **D-16** *(new in Rev 3)* | PROPOSED. Pattern basis only, not authority for the generalization: D-2's two record classes (D-GOV-21 `RecordConvention` and §Status note; the AcceptedCandidateSHA-voiding rule in `D-GOV-21_IMPLEMENTATION_HANDOFF.md` 83–87) plus K-SNAP-1 (`docs/CONTRACT.md` line 125 — "Pointer files may be overwritten; snapshot folders must not"). **Extending this to every ruled or adopted governed artifact is new and has no source.** Carried as PROPOSED precisely because a CLARIFIED label cannot establish it. |

### 2.4 Evidence (main PRD §5.4)

| Commitment | Source anchors (verified at `main@7ac718c7e`) |
|---|---|
| **E-1** | `docs/SPEC.md` §9.8 Managed Multi-Agent Runtime Record (756–775) — record tree contents, immutability/versioning, work-graph required fields. `execution/_Coordination/LOOP_INIT.md` §5 (75–95): "The runtime creates `<RunID>` only when a real run begins. Do not create placeholder runs or represent briefs as executed children." |
| **E-2** | `AGENTS.md` snapshot rule (line 177) and handoff-state rule (line 178); K-SNAP-1 (line 125); `LOOP_INIT.md` §7 (115–127); `docs/DIRECTIVE.md` §2.7. Exemplar handoff: `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`. |
| **E-3** | K-AUTH-2 (line 65). D-GOV-21 record header (lines 5–7) distinguishing `AcceptedCandidateSHA` (the content the owner act approved), `PublicationSHA` (this record's publication commit), and `EffectiveSHA` (the merge that applied the change). `_REGISTER.md` lines 1–10 on SHA binding by publication commit. |
| **E-4** | `docs/TYPES.md` §10.3 Epistemic Labels (431 ff.), §10.4 Warrant Lifecycle (442–460, ladder at line 447). `docs/DIRECTIVE.md` §2 (lines 51, 61). D-GOV-19 ruled proposition 4 (relational, attributable authentication). D-GOV-08 (Option B). |
| **E-5** | `AGENTS.md` agent index, Agent 2 audit rows (AUDIT_DECOMP, AUDIT_DEP_CLOSURE, AUDIT_HYPERGRAPH_CLOSURE, AUDIT_GOVERNANCE, AUDIT_EPISTEMIC, AUDIT_SCOPE_CLOSURE, AUDIT_AGENTS, EVALUATION_*) and the EVALUATION Agent 1 row. `docs/DIRECTIVE.md` §4.1. **Membership by reference; not enumerated as a commitment.** |
| **E-6** | D-GOV-01 Option A (harness never writes governed authority files; labelled generated artifacts under declared generated paths). `_REGISTER.md` Completed item 9 (116–133) — mutation-control contract, `practitioner-harness-evidence/v1`, the two BLOCK conditions. |
| **E-7** | `AGENTS.md` closure rule (line 179); `docs/DIRECTIVE.md` §2.7 (215). |
| **E-8** | Interpretation. Grounding: `_REGISTER.md` Completed item 9 — "`evidence-check` applies the D-GOV-08 Option B provenance ladder (completeness, never sufficiency)"; K-DOMAIN-4 (line 140) — "Validation-passed is necessary, not sufficient, for engineering correctness"; K-CLAIM-1 (line 117). |

### 2.5 Sections outside §5

| Main PRD element | Source anchors |
|---|---|
| Banner / candidate status | K-AUTH-1; D-GOV-21 §Status note (34–36); packet §11; standing workplan §Gated downstream item 1; packet §Status banner (3–7) as the non-approval pattern. |
| ID-1a verbatim ruling | `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`, ruling fence lines 43–45; header SHAs lines 5–7. |
| ID-4 git fact | `git log --reverse` at `main@7ac718c7e`: first commit `7bee9ae41`, "Initial migrated Chirality repository", author and commit date 2026-05-18. `docs/DIRECTIVE.md` §2.2 as the basis for treating git as the development record. |
| §1.2 genus variants | `docs/DIRECTIVE.md` line 13 (Variant A; wording introduced at commit `b2a1e161f`, 2026-06-15; ratified 2026-07-11 per the file's status banner, line 3, and D-GOV-09). `README.md` line 3 (Variant B; wording introduced at commit `d3937edf3`, 2026-07-02). Non-binding classification: D-GOV-21 packet §3b table, README row (line 125). |
| §2.1 problem | `docs/DIRECTIVE.md` §1 (17–21 the three purposes; line 15 the core insight); §2 line 41 (the diagnosis). |
| §2.2 applicability | `docs/DIRECTIVE.md` §3 line 224 (activation clause). |
| §2.3 human capacities *(new in Rev 3)* | Root-governance authority: K-AUTH-1; D-GOV-04 and `docs/governance_harness/human_actors.md` (which registers *permitted authors of binding governance records*, per packet §16's removal of the "apex" characterization). Professional accountability for situated work: `docs/DIRECTIVE.md` §3.2 (230–240). Review: `docs/DIRECTIVE.md` §2 (43–61); the REVIEW gate role in the `AGENTS.md` agent index. Product maintenance: D-GOV-21 M2 (180–190); `docs/SPEC.md` §0.2.1 (line 44), §0.2.2 (line 52). **The separability claim is CLARIFIED** — no single source states it; it follows from the sources' distinct grants. |
| §2.3 user strata | `docs/CONTRACT.md` §1 line 11 (working roots may extend, not weaken); `AGENTS.md` lines 17–23; `docs/governance_harness/human_actors.md`; `docs/SPEC.md` §0.3 (`{WORKING_ROOT}` binding). |
| §3 objectives rationale | `docs/DECOMPOSITION_STANDARD.md` §Non-negotiable invariants, **I7** (line 54): "Objective mapping is best-effort. Objectives are derived from the source material. Unmapped objectives MUST be surfaced as open issues." §SPEC — Validity Requirements, Completeness requirements row: "Objectives derived — Objectives list exists and is human-confirmed." Also §Package Architecture (79–134) for the annex's own package-role classification. |
| §6.1 sequence | D-GOV-21 packet §6 (252–273); standing workplan §Live lanes and §Gated downstream; `D-GOV-21_IMPLEMENTATION_HANDOFF.md` §Remaining blockers (89–107). |
| §6.2 discipline | Packet §9 F3 (317–320); M2 (180–190, "the M2 gate does not itself grant authorization"). |
| §6.3 concurrency | Packet M1 (174–179), M3 (191–196), M4 (197–199), G3 (230–234); `AGENTS.md` §Mixed work graphs and safety (146–172). |
| §7.1 downward | `docs/DIRECTIVE.md` §2.6 (201–204); `docs/CONTRACT.md` §1 (line 11), K-AGENTS-1, K-DOMAIN-1..4; packet §4 (140–141). |
| §7.2 upward | PROPOSED — no source. New commitment. |
| §8.1 non-goals | Packet §4 (130–145); D-GOV-19 §Exclusions and limits; `docs/thesis/README.md` §Warrant Status; `docs/DIRECTIVE.md` §Authority chain (PLAN.md as roadmap surface); `_REGISTER.md` §Terminal-artifact rule (192–195). |
| §8.2 F1–F3 | Packet §9 (305–320); rollback posture §8 (294–303); standing workplan §Stop state falsifier watch (260–264). |
| §8.3 release authority | PROPOSED. Supporting: K-AUTH-1; D-GOV-02 observation-boundary caveat; `docs/DIRECTIVE.md` §7 (line 335, "release, publication, issuance, or professional reliance" not authorized); K-DOMAIN-4 (line 140). |
| §9 RD-1..RD-4 | Packet §11 (336–349) items 1–4; standing workplan Lane A (105–119). Packet §16 Rev 2 note (line 416) recording removal of the `human_actors.md` "apex" characterization. |
| §9.5 RD-5 | Raised by the first independent adversarial review (2026-07-25); not present in packet §11. New reserved decision. Option B reworded in Rev 3 to match §2.2 (review 2 item 6). |
| §4.2 two judgment loops *(new in Rev 3)* | OWNER_DECLARED synthesis, elaborated at review 2 item 7. Non-delegation grounded in K-AUTH-1; D-GOV-02 (observation-boundary caveat); D-GOV-17 (a validator finding may never mechanically reject owner-ruled content); `AGENTS.md` Tool row (line 33). |
| §10.3 adoption transformation *(new in Rev 3)* | CLARIFIED. Grounded in the interaction of D-13/D-16 (adopted bytes not edited) with this document's own candidate status and the five open reserved decisions; pattern from the `_PROPOSALS/` → `_DECISIONS/` candidate/ruled split and D-GOV-21 packet §14's exact-candidate mechanics. Prior-revision immutability: Rev 1 `f15d51277`, Rev 2 `a72c2cd06`. |

---

## 3. Registries incorporated by reference (deliberately not enumerated)

The main PRD cites these registries rather than their members. Enumerating
them in an adopted document is the drift mechanism this restructure exists to
avoid — the failure already observed in `docs/CONTRACT.md`'s invariant index
and `README.md`'s export description.

| Registry | Live location | Governing rule |
|---|---|---|
| Invariant catalog | `docs/CONTRACT.md` §1 | The catalog governs its own membership; working roots may extend, never weaken (`docs/CONTRACT.md` line 11) |
| Agent index and role membership | `AGENTS.md` §Agent Index; `agents/AGENT_*.md` | K-AGENTS-1 — live registry governs over narrative |
| Skill registry | `skills/README.md` plus immediate `skills/*/SKILL.md` folders | `AGENTS.md` §TASK Skill Capabilities — "This file is not the complete skill registry" |
| Tool registry | `tools/REGISTRY.md` | `README.md` §Agents, Skills, Tools, And Tests — curated contract/index surface |
| Public-export profile | `exports/chirality-app/export_public.py` | K-EXPORT-1; the profile is the boundary contract; `README.md` line 198 — "Do not infer the public package contents from the root directory listing" |
| Decision register | `docs/governance_harness/_DECISIONS/_REGISTER.md` + per-decision records | The records govern; the register is navigational |
| Standing workplan pointer | `execution/_Coordination/CURRENT_WORKPLAN.md` | Deterministic target resolution; never by mtime, filename, or narrative |

**Snapshot note (informational, not a commitment).** At the accepted basis the
export profile's root-directory allowlist contained `.github`, `agents`,
`skills`, `tools`, `docs`, `init`, and `runtime`, with root files
`.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CHIRALITY_FRAMEWORK.md`,
`PROFESSIONAL_ENGINEERING.md`, `LICENSE.md`, a substituted public `README.md`,
and two path exclusions plus one prefix exclusion. Root `execution/`,
`projects/`, `domains/`, `plans/`, `exports/`, and `.archive/` were not
exported. **This snapshot is evidence of what was true at
`main@7ac718c7e`; it is not a commitment and must never be cited as the
boundary.** The profile is the boundary.

---

## 4. D-14 source-currency check specification

D-14 in the main PRD is **PROPOSED and inert until adoption**, and **the
capability specified below does not exist at this basis** — there is no
generator, no schema, and no executable check. This section is a
specification of what would be checked, not a description of a running check.
If D-14 is adopted, building the capability is a precondition of relying on
it. Each finding would be a **REVIEW** disposition routed to the owner —
never an automatic amendment (D-GOV-02; K-AUTH-1).

Each class is marked **MECHANICAL** (decidable by comparison against the live
tree) or **SEMANTIC** (requires human or agent judgment about meaning, and
cannot be settled by a diff).

| Class | Kind | What would be checked | Failure signal |
|---|---|---|---|
| **(a1) Invariant IDs exist** | **MECHANICAL** | Every `K-*` ID cited in §2 still exists in `docs/CONTRACT.md` and is not listed in §3 Retired Invariants. | Missing or retired ID |
| **(a2) Invariant text still supports the commitment** | **SEMANTIC** | Where an invariant's text has changed, whether it still supports the commitment citing it. **This is a judgment about meaning, not a diff**: text can change without changing what it warrants, and can keep its wording while a note or ruling changes its effect. A diff can only *flag* the class for judgment. | Changed invariant text whose effect on the citing commitment is undetermined |
| **(b) Live registries** | **MECHANICAL** for existence and location; **SEMANTIC** for "still carries the governing rule" | The registries in §3 still exist at their cited locations; whether each still carries the governing rule the PRD relies on is a reading judgment. | Moved, renamed, or removed registry (mechanical); changed governing rule (semantic) |
| **(c) Source anchors** | **MECHANICAL** | Section references in §2 still resolve. Line numbers are advisory and re-derived; section references govern. | Section heading removed or renumbered (material); line drift alone (informational) |
| **(d) Repeated enumerations** | **MECHANICAL** | Any list the main PRD or this annex repeats from a registry — notably the §3 snapshot note — still matches its registry, or is still correctly labelled a non-binding snapshot. | Snapshot diverged from registry and is not labelled historical |
| **(e) Provenance labels and counts** | **MECHANICAL** | The main PRD's §10.4 counts match the labels present in its tables; no label changed without a superseding instrument (F6). | Count mismatch; label changed in place |
| **(f) DIRECTIVE §1 concordance** | **SEMANTIC** | Whether the adopted PRD and `docs/DIRECTIVE.md` §1 assert incompatible things about what the root product is (F5). Incompatibility is a judgment about claims, not about strings. | Divergence without a recorded superseding act on one of them |

**What a passing check would and would not mean.** Even fully built, the
D-GOV-02 observation-boundary caveat applies: a pass means "no divergence
detected within the declared observation boundary", never "the PRD is
current". The two SEMANTIC classes cannot be discharged by tooling alone —
tooling can route them for judgment, which is the same division of labour the
product asserts everywhere else (D-5; O-2 layer (b): deterministic tools are
never a substitute for semantic judgment).

**Live demonstration of class (e).** During Rev 2 authoring, the §10.4
provenance counts stated 31 TRANSCRIBED / 8 CLARIFIED against tables actually
holding 34 / 5 — a hand-maintained count drifted within a single authoring
session and was caught by manual recount, not by tooling. This is the failure
mode class (e) exists to catch, and it is evidence that the class is worth
building.

---

## 5. Previously-recorded items carried forward

Rev 1 listed these as conflicts C-5 and C-6. They are **not new finds** — both
were already recorded in accepted sources before this run — so Rev 2 carries
them here rather than in the main PRD's conflict register.

### 5.1 K-WRITE-2 explanatory gloss (routed debt)

The gloss inside the K-WRITE-2 entry (`docs/CONTRACT.md` line 124) — "This
confines a task's effects to its working root" — overstates the invariant's
mechanical reach in a monorepo, where working-root containment has always
depended on narrower accepted scopes (briefs, declared write targets, agent
permissions, the SPEC §0.2.2 prohibition), not on K-WRITE-2 alone.

Recorded at: D-GOV-21 packet §5.1 (164–167, "Routed debt (not amended
here)"); standing workplan §Parked lanes, packet §7 class (b) (200–204).
Status: routed for independent reconciliation; not amended by D-GOV-21.
Bears directly on main PRD commitment **N-5**.

### 5.2 Accepted packet WARN (non-gating)

Harness self-check reports `UNRESOLVED_SOURCE_REF` at `PACKET.md:356` — the
packet's declined option O-B names `projects/chirality-root/`, a path that
deliberately does not exist.

Recorded at: `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`
(83–87); standing workplan Step 0 item 7 (83–85). Status: known accepted
finding, non-gating. The packet is the exact ruled candidate and **must not be
amended** — amendment would void the AcceptedCandidateSHA. No action.

### 5.3 Rev 1 corrections recorded for traceability

Four Rev 1 statements were corrected in Rev 2 following the adversarial
review. Recorded here so the correction history is durable without editing
Rev 1 (which remains immutable at `f15d51277`).

| Rev 1 item | Defect | Rev 2 disposition |
|---|---|---|
| R-O-20 | Claimed no third execution substrate exists beyond instruction artifacts and deterministic tools. Root `runtime/` is exactly such a substrate. | Rewritten as **O-2** — three layers with distinct authority boundaries |
| R-N-17 | "There is no central dependency graph" — dropped K-DEP-1's own on-demand-aggregation clause and ignored `FULL_GRAPH` mode. | Rewritten as **O-8** — no central graph is *authoritative*; derived graphs are lawful coordination state |
| Applicability (Rev 1 §4.2) | Cited `docs/DIRECTIVE.md` §3's activation clause as the product's applicability boundary. | Corrected in main PRD **§2.2** — activation boundary of the responsibility model, not of the product |
| R-D-2 | Labelled TRANSCRIBED an absolute supersede-never-edit rule generalized from per-record conventions. | Relabelled **CLARIFIED** as **D-2** — further corrected in Rev 3, see §5.4 |
| R-E-5 | Conflated the candidate, publication, and effective SHA roles. | Corrected in **E-3** — three distinct roles, recorded distinctly |
| ID-1/ID-2/ID-3 presentation | Presented Agent 0 syntheses in verbatim-style blockquotes under an OWNER_DECLARED key that said "not reworded". | OWNER_DECLARED key redefined; blockquote presentation removed from all non-verbatim items; only the D-GOV-21 ruling text remains quote-fenced |

### 5.4 Rev 2 corrections recorded for traceability

Eleven items plus two refinements were corrected in Rev 3 following the second
adversarial review. Recorded here so the correction history stays durable
without editing Rev 2 (immutable at `a72c2cd06`).

| Rev 2 item | Defect | Rev 3 disposition |
|---|---|---|
| ID-1 | Called the product an "operating system", prematurely settling RD-1 in body text while §1.2 said the genus was open. | Reworded genus-neutrally ("governs the production of professional knowledge work"); the genus noun now appears only in RD-1's options and the cited variants |
| N-1 | Asserted no external substrate holds authoritative truth, omitting K-DOMAIN-1's engine-owned domain truth. The annex noted it, but the annex is never adopted. | Scoped to authoritative **governance and project-coordination** state, with the K-DOMAIN-1 exception stated in **N-1 itself** |
| O-10 | "Nothing outside those layers holds project authority" excluded the human, who necessarily sits outside the machine layers. | Replaced with the reviewer's corrected formulation — no fourth *machine* substrate; authority remains with attributable human acts |
| OBJ-2 | Required "every gate human-performed", contradicting the product's lawful deterministic guards, fan-in gates, and structural validation gates. | Narrowed to consequential **acceptance, reliance, and issuance judgments**; non-human gates named as lawful; product carries work *to* an issuance decision |
| §2.3 users | Mixed root governance, professional accountability, review, and maintenance into two strata; implied secondary users are passive. | Added an explicit **four-capacity** table with separability stated; secondary users act (reviewers gate, maintainers change the surface) |
| RD-5 option B | "Licensed or accountable practitioner in the target domains" reintroduced the applicability narrowing §2.2 had removed. | Reworded to **individual professional knowledge workers generally**, responsibility model activating where applicable |
| §4.2 loop | One combined "human judgment" step left the two distinct judgments implicit. | Added explicit **evaluation judgment** vs **iteration judgment** table with inputs, questions, and the non-delegation rule |
| OBJ-6 | "`_Coordination/` state alone" had an ambiguous population; "at any point in time" was not checkable against interrupted runs. | Population fixed to root-product development runs (aggregated cross-root coordination named as a *new product function*, not implied); condition made lifecycle-checkable with stale/orphaned-run detectability |
| D-2 | A CLARIFIED label was doing normative work — a product-wide rule an interpretation cannot establish. | **Option (a) taken:** D-2 narrowed to the two record classes where the convention already governs (stays CLARIFIED, classes cited); the generalization carried separately as **D-16, PROPOSED** |
| Annex regenerability | Claimed present-tense mechanical regenerability and checking with no generator, schema, or executable check. | Changed to **specified for regeneration, proposed for checking**; §4 now marks each class MECHANICAL or SEMANTIC; §6 states what building the capability would require. Main PRD §10.1, its banner, and D-14 aligned |
| Adoption transformation | Exact bytes said `NOT ADOPTED` / "binds nothing" with five open option sets, which D-13 would then forbid correcting. | Main PRD §10.3 now specifies **two-step terminal mechanics**: candidate revisions, then a final adoption-ready revision after RD rulings, with a status model that stays truthful post-adoption; prior revisions remain immutable evidence |
| OBJ-3 *(refinement)* | "Bounded time" had no threshold. | Threshold and tranche sample must be **fixed and recorded before** the evaluation runs |
| OBJ-5 *(refinement)* | Required an actual promotion, which could force an artificial one to pass v1. | Success is a complete promotion **disposition** — accepted, rejected, or deferred with evidence |

---

## 6. Regeneration contract

**What this annex is derived from.** Accepted upstream snapshot
`main@7ac718c7e`, plus the main PRD Rev 3 at the same basis. Every anchor was
read against the live file during run `ROOT-PRD-LANE-A-20260725`.

**Regeneration is a specified manual procedure, not an implemented one.**
There is no generator and no schema at this basis. What follows is the
*method* a future generator would implement, and the method a human or agent
follows in the meantime.

**How it is regenerated.** By re-reading the cited sources at a stated basis
and re-deriving §2 from the main PRD's commitment IDs. Section references are
the stable key; line numbers are re-derived each time and are advisory.

**Building the capability.** Mechanizing this would require, at minimum: a
stable machine-readable key linking each commitment ID to its source anchors
(§2 is presently prose tables); a resolver for section references; and a
report format carrying the MECHANICAL/SEMANTIC split of §4. **None of this
exists.** Until it does, neither this annex nor the main PRD may be described
as mechanically checked, and D-14 remains a PROPOSED obligation without a
capability behind it.

**What regeneration does not do.** It does not amend the main PRD, does not
change any commitment's provenance label, and does not resolve any conflict or
reserved decision. A regeneration that surfaces divergence produces a REVIEW
finding for the owner (§4), not an edit.

**Closure and handoff note.** This annex is a derivative package under the
`AGENTS.md` derivative-package rule and cites its accepted upstream snapshot
above. Per the closure rule, its existence closes nothing: the Lane A closure
verdict, rerun requirements, and remaining blockers belong to the run's
handoff state, not to this file.
