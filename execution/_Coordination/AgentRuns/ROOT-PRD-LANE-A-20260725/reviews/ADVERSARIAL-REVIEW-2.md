# Adversarial Review 2 — PRD Candidate Rev 2 (ROOT-PRD-LANE-A-20260725)

Reviewer: same independent second agent, routed by the owner in-session,
2026-07-25. Subject: Rev 2 at `a72c2cd06` (PR #340).
Verdict: **"Rev 2 resolves most of the prior review and is now recognizably
a product PRD. I recommend one more revision before owner decisions or
adoption. The remaining issues are mostly precise contradictions, not
architectural disagreements."** Explicitly to preserve: objectives + v1
boundary; overlapping functional categories; downward-specialization /
upward-evidence relationship; users/actors/contexts separation; three SHA
roles; two-axis accountability decision; companion-annex strategy.

Agent 0 dispositions: all items ACCEPTED — see
`../briefs/PRD-AUTHOR-BRIEF-AMENDMENT-2.md`. Line references below are to
Rev 2 at `a72c2cd06`.

## Review items (verbatim in substance, as routed by the owner)

1. **ID-1 prematurely settles RD-1** (PRD:53). ID-1 calls Chirality Root an
   "operating system," while §1.2 says the genus is unresolved. Use
   genus-neutral wording in ID-1 until RD-1 is decided, or incorporate the
   selected wording into the final candidate.
2. **N-1 omits the domain-engine exception** (PRD:279). It says no external
   database or server holds authoritative truth, but K-DOMAIN-1 expressly
   allows engine-owned authoritative domain truth. The annex notices the
   exception, but the annex will never be adopted; the exception must
   appear in N-1 itself. Limit N-1 to authoritative governance and
   project-coordination state, then preserve domain-engine ownership
   explicitly.
3. **O-10 contradicts the human-authority model** (PRD:302). "Nothing
   outside those layers holds project authority" excludes the human, who
   necessarily exists outside the three machine layers. Suggested
   correction: "No fourth machine execution substrate is claimed; none of
   the three operative layers holds or grants project authority, which
   remains with attributable human acts under the governed record."
4. **OBJ-2 makes every gate human-performed** (PRD:197). Chirality also has
   deterministic guards, fan-in gates, and structural validation gates.
   Require human performance of consequential acceptance, reliance, and
   issuance judgments — not every gate. Also make clear that Chirality
   carries work to an issuance decision; the accountable human issues it.
5. **The human-user taxonomy still mixes distinct authorities** (PRD:158).
   Root governance, professional accountability, review, and product
   maintenance are different capacities that may be held by different
   people. A professional practitioner does not thereby obtain
   root-governance authority, and a root owner does not thereby become the
   accountable professional for situated work. Secondary users also need
   not be purely passive. Make the role distinctions explicit.
6. **RD-5 reintroduces the applicability narrowing Rev 2 removed**
   (PRD:590). Option B targets "licensed or accountable practitioners in
   the target domains," whereas §2.2 says the product addresses
   professional knowledge work generally with responsibility provisions
   activating in higher-stakes circumstances. Option B should be
   "individual professional knowledge workers generally," with the
   responsibility model activating where applicable.
7. **Preserve the two human-judgment loops explicitly** (PRD:225).
   Operative work produces evidence; evidence informs human evaluation.
   Developmental machinery produces candidate changes and iteration
   evidence; these inform human iteration judgment. Either judgment may
   accept, reject, or redirect, but neither is delegated to machinery.
   Central enough to state directly rather than leave implicit in one
   combined loop.
8. **OBJ-6 needs an explicit coordination boundary** (PRD:201).
   "`_Coordination/` state alone" could mean root-product development
   runs, every run across all situated working roots, or a future
   aggregated coordination layer. Only the first is presently supported
   without adding a new product function. State the intended population
   and observation boundary. Replace "at any point in time" with a
   checkable lifecycle condition that accommodates interrupted or
   crashing runs.
9. **D-2's label does not solve its normative gap** (PRD:309). A CLARIFIED
   interpretation cannot establish a product-wide supersede-never-edit
   commitment. Either narrow D-2 to the record classes where that
   convention already governs, or label the generalized rule PROPOSED.
10. **The annex is not yet mechanically regenerable** (PRD:635; Annex:176).
    It supplies a manual regeneration method, but no generator, schema, or
    executable check. Several purportedly mechanical checks also require
    semantic judgment — especially whether changed invariant text still
    supports a commitment. Change the present-tense claim to "specified
    for regeneration and proposed for checking," or supply the actual
    checking capability before adoption.
11. **Clarify the final adoption transformation** (PRD:3; PRD:659). The
    exact bytes currently say `CANDIDATE — NOT ADOPTED`, "binds nothing,"
    and contain five unresolved option sets; D-13 then forbids editing
    adopted bytes. Before owner adoption, produce final adoption-ready
    bytes containing the selected RD dispositions and a status model that
    remains truthful after the external adoption act. Preserve Rev 2 as
    historical candidate evidence rather than adopting its unresolved
    bytes as-is.

Lower-level refinements:

- **OBJ-3** "bounded time" needs a threshold, or a requirement that the
  threshold and sample be fixed before evaluation.
- **OBJ-5** should avoid forcing an artificial promotion merely to pass
  v1. Demonstrating a complete promotion disposition — accepted, rejected,
  or deferred with evidence — tests the pathway without prejudging that a
  candidate deserves promotion.
