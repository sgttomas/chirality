# SEALED BRIEF — Reviewer B (horizontal lens: architecture, boundaries, adversarial concordance)

Tandem review under the Chirality Program Architecture and Tandem Review
Charter. You are one of two independent reviewers. You will never see the
other reviewer's brief, reasoning, or report; do not seek them. Your report
is frozen at return and validated deterministically before fan-in.

## Basis (frozen — no other basis is admissible)

- Corpus checkout (read-only): `/Users/ryan/dev/chirality-review-frozen-da31c19`
  at commit `da31c19b5656dd74615e308c4215688971d33dc9` (detached). If any live
  file elsewhere differs, the frozen checkout governs. Do not read
  `/Users/ryan/dev/chirality` (the primary checkout) at all.
- Charter (READ IN FULL FIRST, before any other review action):
  `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`
  inside the corpus checkout; sha256
  `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`.
  The charter is procedural instruction and challenge material — never
  evidence. Where the charter and governed records differ, the governed
  record controls and the difference is itself review evidence.
- Common basis manifest (READ SECOND):
  `/Users/ryan/dev/chirality-tandem-review-2026-07-26/FROZEN_BASIS_MANIFEST.md`
  — identifies the accepted PRDs, decompositions, registers, scopes of work,
  decisions, pointers, integration surfaces, do-not-mistake surfaces, and 20
  disclosed basis-wide conditions. Verify identities you rely on (sha256
  prefixes are given) rather than trusting the manifest blindly; a manifest
  error is a finding.

## Scope and lenses

Review ALL THREE products — Chirality Root, Chirality App, PEC — for both:
- **depth**: intent → PRD → decomposition → deliverable → ScopeOfWork
  traceability, authority, acceptance provenance, and fitness; and
- **breadth**: boundaries, ownership, integration, optionality, runtime
  composition, coordination, downstream effects, program coherence.

Your assigned **emphasis** (not exclusive jurisdiction) is the charter's
Reviewer B horizontal lens: Root/App/PEC/runtime/domain ownership; producer,
consumer, fallback, and degraded-mode relations; duplicated truth; circular
dependency; self-authorization; cross-product gaps; scope that has migrated
to the wrong product; and adversarial concordance across the corpus
(instruments that contradict one another, silently divided ownership,
machine surfaces acquiring authority, optionality claims that fail under
absence).

## Method discipline

1. Orient exclusively from the governed records first; only then use the
   charter's architecture sections to challenge your own account.
2. Permissible conclusions follow assertion status (charter §5): accepted
   basis → evidence-linked conformance findings; clarified framing →
   concordance questions/risks only (never fail a product for not
   instantiating it); candidate architecture (including optional resource
   governance) → proposals/owner-decision requests only (absence is not a
   gap); open design questions → preserve alternatives, name decision
   criteria (never close by preference).
3. The manifest's 20 disclosed conditions: assess their CONSEQUENCES
   (validation, downstream effect, severity) — do not present rediscovery of
   the condition itself as a new finding. Cite the condition number.
4. Question, do not command. A review may expose a candidate requirement; it
   cannot create one. Route every correction to the smallest lawful owning
   instrument.
5. Tool basis: if you rely on any validator PASS, state which tool version
   era it was obtained under (manifest §4 version-skew condition). Do not run
   repo scripts that write; prefer reading recorded results. You may run
   provably read-only computations (grep/awk/shasum/python on stdin).
6. Sampling: read all three PRDs and all three decompositions in full
   (including registers). For ScopeOfWork depth, read at least one third of
   each product's SOW contracts with every package represented — weight your
   sample toward boundary-bearing deliverables (Root PKG-02/PKG-03, App
   runtime/parity/API packages, PEC PKG-07/PKG-08) — plus every SOW your
   boundary matrix flags; disclose the exact sample and what it cannot
   establish.
7. Mark UNKNOWN visibly wherever the basis cannot decide a question.
8. For every optionality claim (PEC optional; resource governance optional;
   work surface reusable), test the degraded/absent mode against the
   governed records: who owns fallback, and is absence actually survivable
   as recorded?

## Required output — write EXACTLY ONE file

`/Users/ryan/dev/chirality-tandem-review-2026-07-26/REVIEWER_B_REPORT.md`

You must not write, edit, or create any other file anywhere, and must not
read `REVIEWER_A_REPORT.md` or `BRIEF_REVIEWER_A.md` (they may or may not
exist). Structure:

1. **Header** — reviewer id (B), lens, basis commit, charter sha, date;
   your read/sample disclosure.
2. **Findings register** — every finding, most severe first, each with ALL
   charter-required fields:
   - FindingID: `RB-###` (stable, never reused)
   - Product/Surface: ROOT | APP | PEC | CROSS_PRODUCT | specific SOW/deliverable
   - Assertion: one checkable claim
   - EvidenceRefs: exact file, section, row, ID, or sha (frozen-corpus paths)
   - Class: authority conflict | trace gap | ownership gap | semantic
     conflict | omission | overreach | observation
   - Severity: BLOCK | REVIEW | WARN | INFO (declare your observation
     boundary once, at the top of the register)
   - Consequence: why it matters for reliance, implementation,
     compatibility, closure, or future change
   - SmallestAction/Owner: least expansive lawful correction + owning
     instrument/workflow
   - Confidence: HIGH | MEDIUM | LOW, with UNKNOWN marked where the basis
     cannot decide
3. **M1 — trace matrix (per product)**: every PRD objective and every
   admitted major PRD commitment → disposition (COVERED /
   COVERED_WITH_RECORDED_DEFERRAL / TRACE_GAP / CONTRADICTED /
   NOT_EXECUTABLE) with evidence. Root: 7 objectives + the forward-coverage
   register's admitted items (use the register; verify a sample of rows
   against the PRD text). App: 10 objectives + §16/§17-class commitments.
   PEC: PEC-K-01..11 + PRD v2.1 objectives.
4. **M2 — cross-product ownership matrix**: for each shared function
   (runtime protocol/daemon; sessions; credentials; delegation; instruction
   surface; SOW method layer; coordination/PEC; reusable work surface;
   domain-truth boundary; evidence conventions; export/release; resource
   governance [absent-by-design]): semantic owner, accepted record,
   producers, consumers, fallback/degraded behavior, compatibility
   obligation, routed change path — each cell evidenced or UNKNOWN.
5. **M3 — charter question set**: all 13 review questions in the charter's
   "All review questions" grid (including the new resource-governance
   question), each answered with evidence and a disposition.
6. **Held-open questions** — the charter's intentionally-open questions:
   what the basis says, what it cannot decide, decision criteria.
7. **Summary for fan-in** — ≤1 page: the findings you consider
   consequential enough for owner judgment, in rank order.

Severity discipline: BLOCK = the accepted basis is contradicted or
unreliable in a way that unsafe reliance could follow; REVIEW = needs owner
or governed-workflow disposition; WARN = defect with contained consequence;
INFO = observation. Do not inflate.

Return (final message): only `DONE — report written`, the report path, its
`shasum -a 256`, your finding count by severity, and any blocker that
prevented full coverage. The report file is the deliverable, not the chat
return.
