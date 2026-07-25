# Sealed Brief — N1: Author the candidate root PRD (ROOT-PRD-LANE-A-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25
Executor: ephemeral bounded Agent 2 generalist, model `opus-5`
Basis: `main@7ac718c7e` (D-GOV-21 step 4 closed; Lane A live)

## Purpose

Author the **candidate** Product Requirements Document for the root product
("Chirality Root") — the first integrated PRD for the monorepo root itself —
as authorized by D-GOV-21 effect 5. The candidate binds nothing. Adoption is
a separate future owner act on a separate instrument (packet §11.3); nothing
you write may present itself as adopted, and the document must say so.

## Single write target

`execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md` — new
file; the ONLY file you may create or modify. It is deliberately placed on a
non-exported coordination surface: root `docs/` is in the public-export
allowlist and `execution/` is not, and the adopted PRD's placement is one of
the reserved owner decisions you must surface, not settle.

## Declared context (read scope; read before writing)

- `docs/DIRECTIVE.md` (esp. §1 Founding Intent, §2, §2.6 as amended, §5)
- `docs/CONTRACT.md` (K-* invariants; esp. K-AUTH-1, K-AUTH-2, K-WRITE-2)
- `docs/SPEC.md` §0.2–§0.3, §1 (as amended); `docs/TYPES.md` §1.4
- `AGENTS.md` (runtime doctrine; agent hierarchy; governance rules)
- `README.md` (note: describes the product as a "governed application
  environment" — a live genus variant)
- `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
  and the ruled packet
  `docs/governance_harness/_PROPOSALS/D-GOV-21_root-working-root-exception/PACKET.md`
  (§§2, 4, 5, 6, 9, 10, 11 govern what you may claim)
- `docs/governance_harness/D-GOV-21_IMPLEMENTATION_HANDOFF.md`
- `docs/governance_harness/_DECISIONS/_REGISTER.md` (decision history)
- `docs/governance_harness/human_actors.md`
- `execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md`
  (Lane A definition; your constraints restate its)
- `docs/thesis/` (read-only; philosophical basis — cite, never re-litigate)
- `exports/chirality-app/export_public.py` (ROOT_DIRS allowlist facts only)

## Provenance discipline (mandatory)

Label every requirement and every identity claim with exactly one of:

- **TRANSCRIBED** — already accepted/ratified doctrine; cite file and
  section/line. Verify each citation against the live file before writing it.
- **OWNER_DECLARED** — owner testimony or in-session direction transcribed
  by the issuing Agent 0 (sources quoted below); the owner confirms or
  corrects at adoption. Never silently reword these.
- **CLARIFIED** — an interpretation of existing accepted truth produced by
  the 2026-07-25 root-PRD inquiry (Agent 0 + independent second-agent
  review, owner-mediated); mark as interpretation.
- **PROPOSED** — a new commitment that takes effect only if the PRD is
  adopted.

## Owner-declared framing of record (transcribe; do not reword)

The following owner framing was given in-session during the root-PRD
inquiry, 2026-07-25 (Agent 0 transcription; owner confirms at adoption):

1. The root is both an **operating system for governed professional
   knowledge work** and a **normative, self-applying instance of a
   generative development pattern** — it develops itself under the same
   governance it prescribes. (The self-application half is now also
   TRANSCRIBED via D-GOV-21.)
2. The root product is constituted by **four categories**: **Normative
   basis** (the ratified governance corpus and invariants), **Operative
   product** (the instruction surface, agents, skills, tools, harness, and
   runtime that do work), **Developmental machinery** (the governance
   harness, decision records, loops, and guards by which the product
   changes itself), and **Evidence** (receipts, run records, snapshots,
   audits — the record that makes reliance answerable).
3. **Human judgment is the governing hinge**: only humans author binding
   approvals (K-AUTH-1); agent capability never confers authority; the
   permanent accountability gap (D-GOV-19) is why the hinge cannot be
   automated away.
4. Historical note: the owner attests roughly three years of prior
   development lineage; in-repo history begins 2026-02-18. State both facts
   with their provenance (owner testimony vs. git history); do not blend
   them.

## Required document structure

1. **Candidate banner** — Status `CANDIDATE — NOT ADOPTED`; binds nothing
   (K-AUTH-1); adoption is a separate owner instrument; basis
   `main@7ac718c7e`; authored under run `ROOT-PRD-LANE-A-20260725`.
2. **Provenance key** — the four labels above, defined.
3. **Product identity** — what Chirality Root is, using the neutral referent
   "the root product"/"Chirality Root" in body text. Present the dual nature
   (item 1 above) and the four categories (item 2) as the organizing frame.
   **Do not settle the genus wording**: present the live variants —
   DIRECTIVE §1's ratified "governed, filesystem-native agent operating
   system" (TRANSCRIBED, ratified, older) and README's "governed application
   environment" (TRANSCRIBED from a non-binding surface, newer) — and route
   the choice to Reserved Decision 1.
4. **Problem and users** — from DIRECTIVE §1 intents (TRANSCRIBED):
   deliverable-heavy professional work; auditability and controllability for
   professional/regulated reliance; who uses it (practitioner-owners running
   governed loops; agents as bounded executors; downstream working roots).
5. **Product requirements by category** — for each of the four categories,
   enumerate the requirements the root product must satisfy, each labeled
   and cited. TRANSCRIBED requirements dominate (this PRD integrates what is
   already ratified); CLARIFIED where the inquiry sharpened meaning;
   PROPOSED only where a genuine new commitment is needed, kept minimal.
   Include as requirements (not exhaustive): filesystem-as-database and
   git-tracked plain-file authority (D-GOV-01, DIRECTIVE); human-gated
   consequential decisions (K-AUTH-1/K-GATE-1); SHA-bound approvals
   (K-AUTH-2); checkout containment (K-WRITE-2); instruction/working-root
   separation with the single D-GOV-21 exception and its replacement
   containment contract (M1–M7, G0–G4); the agent hierarchy and construction
   forms (AGENTS.md); decision-record system with supersede-never-edit;
   deterministic validation with D-GOV-02 severity semantics; the
   public-export boundary.
6. **Self-application** — the root develops itself through its own
   pipeline: PRD → adoption → decomposition → Project Setup →
   materialization under root `execution/` behind the §5.3 gate. State the
   D-GOV-21 falsifiers F1–F3 as product-level falsifiers of the
   self-application claim, and add any PRD-level falsifiers you can ground
   (label PROPOSED).
7. **Non-goals** — at minimum, restate packet §4's exclusions as PRD
   non-goals (no export-boundary change; no extension of the root exception
   to other working roots; no waiver of the decomposition pipeline; no
   blanket authority for future root-structure changes) plus any inquiry
   non-goals you can ground in cited sources.
8. **Relationship to variants** — the monorepo's other working roots
   (`projects/*`, `domains/*`), the desktop harness (user-selected working
   folders; instruction root as app bundle), the shared runtime (D-GOV-20),
   and the public export (`exports/chirality-app`; allowlist facts). Each
   TRANSCRIBED with citations.
9. **Reserved owner decisions (decision slate)** — the four packet §11
   decisions, each presented with options, consequences, and NO
   recommendation-as-resolution (a recommendation may be offered but must be
   labeled as agent recommendation, decision expressly reserved):
   RD-1 genus wording; RD-2 accountability model (one accountable human per
   consequential act vs. one owner per root — including who may amend
   `docs/governance_harness/human_actors.md`); RD-3 adoption instrument and
   the required concordance map against DIRECTIVE §1; RD-4 adopted-PRD
   placement relative to the public-export boundary.
10. **Adoption mechanics** — exact-bytes adoption on a separate instrument;
    concordance map against `docs/DIRECTIVE.md` §1 required at adoption
    (packet §11.3); until then every PROPOSED item is inert.

## Constraints

- ONE write target (above). No instruction-surface writes (`AGENTS.md`,
  `agents/`, `skills/`, `tools/`, root `docs/`, `init/`), no
  `projects/*`/`domains/*` writes, no `PKG-*`/`DEL-*` creation anywhere.
- No adoption, acceptance, or ratification claims for the PRD itself.
- No machine-absolute paths (SPEC §0.2.4). Repo-relative citations.
- Cite decisions by ID + SHA where SHAs are recorded; never by recollection.
- Where sources conflict (e.g., genus variants), present the conflict with
  both citations; never harmonize silently.
- If you find a contradiction between this brief and a governing source,
  stop writing that section and return the conflict.

## Terminal return (structured; your final text is a data return to Agent 0)

1. The file path written and its section outline.
2. Provenance-label counts (how many TRANSCRIBED / OWNER_DECLARED /
   CLARIFIED / PROPOSED requirements) and the complete list of PROPOSED
   items (these need the closest owner attention).
3. Confirmation of each constraint (only file touched; no absolute paths;
   citations verified; reserved decisions unresolved).
4. Anything you could not ground, chose not to include, or left for Agent 0
   disposition.
