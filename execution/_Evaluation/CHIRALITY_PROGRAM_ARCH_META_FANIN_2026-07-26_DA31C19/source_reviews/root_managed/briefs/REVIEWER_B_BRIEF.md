# SEALED BRIEF — Reviewer B (horizontal lens: architecture, boundaries, and adversarial concordance)

Run: TANDEM-REVIEW-20260726 · Pass 1 (independent)
Dispatcher: HELP_HUMAN (Agent 0), acting as supervising review manager per owner direction
of 2026-07-26. You are a bounded, read-only Agent 2 reviewer. You do not delegate.

## 1. Identity and basis (frozen — verify before relying)

- Review corpus: the Chirality monorepo at commit
  `da31c19b5656dd74615e308c4215688971d33dc9` (the review freeze).
- Product-basis commit: `aeadf5304435e1a4d8b4a26306da9ad4d4519eb6`. Only the charter
  changed between the two.
- Your working copy: the detached read-only worktree at
  `/private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-chirality-root-prd-inquiry-799a78/2f009cef-c385-4df3-8ea0-196308681f90/scratchpad/frozen-da31c19b5`
  — its HEAD is the freeze commit. All repository paths in this brief resolve from that
  worktree root. If you ever doubt a file's currency, resolve it with
  `git show da31c19b5656dd74615e308c4215688971d33dc9:<path>`; the frozen commit governs
  over any live filesystem bytes anywhere else.
- Do NOT read, cd into, or cite `/Users/ryan/dev/chirality` (the primary checkout) or any
  other worktree. Do not fetch, pull, checkout, or otherwise alter Git state.

## 2. Required reading, in order, before any finding

1. The charter, in full:
   `plans/chirality_program_architecture_and_tandem_review_2026-07-25.html`
   (in your worktree; SHA-256 `1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f`).
   It is **non-governing reviewer guidance**: procedural instruction and challenge
   material. Its architectural propositions are questions to test, not facts to presume,
   and never citable as evidence.
2. The frozen-basis manifest, in full:
   `../TANDEM_REVIEW_2026-07-26/FROZEN_BASIS_MANIFEST.md` (absolute path:
   `/private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-chirality-root-prd-inquiry-799a78/2f009cef-c385-4df3-8ea0-196308681f90/scratchpad/TANDEM_REVIEW_2026-07-26/FROZEN_BASIS_MANIFEST.md`).
   It identifies the accepted basis per product, the not-basis surfaces, and 20 disclosed
   basis-wide conditions.
3. Then orient from the governed records themselves (PRDs, decompositions, registers,
   decisions, SOWs) per the charter's Orient guidance: form your own account of each
   product from the frozen repository basis FIRST; only then use the charter as a
   challenge set against your account.

## 3. Scope

All three products — Chirality Root, Chirality App, PEC — plus the shared method and
runtime layers and the cross-product control surfaces (Tier-0 register). Both depth and
breadth for every product:

- Depth: intent → PRD → decomposition → deliverable → ScopeOfWork traceability,
  authority, acceptance, and fitness.
- Breadth: boundaries, ownership, integration, optionality, runtime composition,
  coordination, downstream effects, and program coherence.

Domain packs (`domains/chirality`, `domains/chirality-app-dev`, `domains/chirality-piping`,
`domains/piping-design`) are consulted-only context: not reviewed products, but their
pins, notices, and drift are admissible evidence about Root/App/PEC architecture effects.
Piping is a situated-product exemplar for notice/inheritance coverage only. Resource
governance is optional candidate architecture described only by the charter — absence of
it is never a scope gap. The proposed App semantic-parity work is not accepted basis.

## 4. Your assigned lens (emphasis, not exclusive jurisdiction)

**Horizontal: architecture, boundaries, and adversarial concordance.** Your report must
give primary weight to:

- Ownership across Root / App / PEC / shared runtime / domain engines: for every shared
  function, one semantic owner, one accepted record, an explicit compatibility
  obligation, and a routed change path. "Shared" describes use — test every place where
  it has quietly become divided ownership.
- Producer, consumer, fallback, and degraded-mode relations: what breaks, and what is
  supposed to happen, when an optional service (PEC; candidate resource governance) is
  absent; whether governed work remains intelligible and recoverable without PEC; whether
  any optionality claim is contradicted by an actual dependency.
- Duplicated truth: the same fact owned or restated in two places with independent update
  paths (pins vs sources, mirrors vs originals, registers vs prose, exhibits vs live
  registers). Identify which copy governs and whether that is recorded.
- Circular dependency and self-authorization: any surface that authorizes itself, any
  loop granting itself capability, any validator or runtime state functioning as
  authority, any machine gate that has absorbed a human judgment.
- Cross-product gaps and scope migration: functions the corpus relies on that no product
  owns (e.g., reusable work-surface contracts, application-integration/composition
  contracts, notice routing); scope that has migrated to the wrong product (e.g., runtime
  semantics retained by a client; domain truth absorbed by generic infrastructure).
- Runtime composition under D-GOV-20 / D-T0-23: whether App and PEC are genuinely
  distinct clients with explicit seams (PEC PKG-07/PKG-08; App runtime-client seams);
  whether ownership and integration seams are explicit enough to prevent silent
  absorption of one another's responsibilities.
- Notice and inheritance effectiveness, using the consulted-only domain packs and Piping
  as the exemplar: does the routed-notice architecture actually reach and get
  dispositioned downstream, and does downstream detection work without it?

You must still cover the vertical territory (authority chains, trace, acceptance
provenance) at assessment depth — the lens sets emphasis, not jurisdiction.

## 5. Evidence rules

- Every finding cites exact evidence: file path (repo-relative), section/heading or line,
  row, stable ID, SHA, or a validated tool output — all resolved at the freeze commit.
- Mutable pointers (`_LATEST.md`, `CURRENT_WORKPLAN.md`, register tables that describe
  themselves as non-governing) are navigation, not authority — cite the instrument they
  point to.
- If you run any validator or script from the frozen tree, you MUST state the tool basis
  (the freeze commit and tool path) alongside any PASS/FAIL you rely on. Note the
  disclosed version-skew condition: Root's 45 SOWs passed under the pre-v6 method; a
  current-tool rerun that flags them shows tool drift, not that the accepted historical
  validation was false. Never run tools that write into the worktree; read-only execution
  (validators writing to stdout) is fine. If a validator insists on writing, skip it and
  say so.
- The 20 disclosed basis-wide conditions (manifest §5) and the per-product "conditions
  reviewers should assess" lists are already known: assess their consequences (severity,
  reach, compounding risk, smallest correction) — do not present them as new discoveries.
  You may still criticize them, deepen them, or show interactions between them; genuinely
  new aspects of a disclosed condition are new findings.
- Permissible treatment follows assertion status (charter §5): accepted basis →
  conformance findings; clarified framing → concordance questions/risks, never a failure
  for not instantiating the framing; candidate architecture (including resource
  governance) → proposals/owner-decision requests only, absence is not a gap; open design
  questions → preserve alternatives and decision criteria, do not close by preference.
- A review may expose a candidate requirement; it cannot create one. Route new
  commitments as owner-decision requests in your findings — never as assumed scope.

## 6. Read-only boundary and independence

- You write EXACTLY ONE artifact: your report (path in §8). No other file anywhere. No
  modification of the worktree, the primary checkout, or Git state.
- You work alone. Do not communicate with, look for, or read the work of any other
  reviewer or agent. There is a second, independent reviewer whose existence you know of
  but whose identity, lens, and output are sealed from you until after your report is
  frozen. Do not attempt to anticipate or coordinate with it.
- Your report is a pass-1 return. It will be frozen (hashed) on receipt; there is no
  post-hoc editing. Completeness before submission is your responsibility.

## 7. Required output schema

Write a single Markdown report with these sections, in order:

1. **Reviewed-basis statement** — freeze SHA, charter SHA-256, manifest read
   confirmation, every tool basis used, and any deviation from this brief (should be
   none).
2. **Product accounts** (Root, App, PEC — one each): your independent account of what the
   product is, its authority chain, and its current governed state, formed from the
   frozen records. Concise — this grounds your findings.
3. **Coverage matrices** (one per product): every admitted PRD commitment/objective with
   its trace disposition — COVERED (with the carrying scope items/deliverables),
   DEFERRED (with the recording instrument), or GAP (a finding). Full coverage, not
   anecdotes. Where a product's commitments are too numerous to row-enumerate, enumerate
   objectives and commitment groups completely and state your grouping rule explicitly.
4. **Boundary and ownership matrix** (cross-product): for each shared function (at
   minimum: shared runtime, work-surface/UI, coordination projection, dependency truth,
   SOW method layer, authority-corpus pinning, notice routing, domain-engine profiles,
   resource governance (candidate)): semantic owner, producers, consumers, authoritative
   record, compatibility obligation, fallback/degraded behavior, routed change path —
   each cell evidenced or marked UNKNOWN.
5. **Findings register** — a table (or per-finding blocks) with EXACTLY these fields per
   the charter: `FindingID` (B-001, B-002, … stable, never reused), `Product/Surface`
   (ROOT | APP | PEC | CROSS_PRODUCT | specific SOW/deliverable), `Assertion` (one
   checkable claim), `EvidenceRefs`, `Class` (authority conflict | trace gap | ownership
   gap | semantic conflict | omission | overreach | observation), `Severity`
   (BLOCK | REVIEW | WARN | INFO) with a declared observation boundary stated once at the
   top of the register, `Consequence`, `SmallestAction/Owner` (least expansive lawful
   correction + owning instrument/workflow), `Confidence` (HIGH/MEDIUM/LOW, with UNKNOWN
   visible where the basis cannot decide).
6. **Disclosed-conditions assessment** — all 20 manifest §5 conditions plus the
   per-product condition lists: for each, consequence assessment and whether your review
   found the condition accurately described, worse than described, or immaterial.
7. **Open questions and UNKNOWNs** — including any owner-decision requests and preserved
   open design questions with decision criteria.

Order findings most-severe-first within each product. Prefer many precise findings over
few broad ones. Do not average away internal tension — if two governed records conflict,
that conflict is itself a finding.

## 8. Output location

Write your report to:
`/private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-chirality-root-prd-inquiry-799a78/2f009cef-c385-4df3-8ea0-196308681f90/scratchpad/TANDEM_REVIEW_2026-07-26/reviewer_b/REPORT_B.md`

Your terminal return message to the dispatcher: a short structural summary only (section
list, finding count by severity, coverage totals, any brief deviations). The report file
is the deliverable; do not paste it into the return.
