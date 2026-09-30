# A1 closure — implementation questions, evidence and decisions

This is a conditional impact inventory for the unselected P/C/U alternatives.
No source edit, test execution, new case, resource measurement or repair is
authorized by this document. Aliases and source basis are in
`A1_CLOSURE_OPTIONS.md`.

## Exact loci to carry into a future bounded brief

| Source locus | Present responsibility | Consequence to resolve |
|---|---|---|
| `FK/src/structural/retained/adaptive.rs:276–309` | Binary64 body extent and coupled scales | Reuse exact operation order and zero-extent behavior; both multiply/divide directions and finite results need coverage. |
| `adaptive.rs:341–424` | Threshold, upward b, A1 row bound and classification | Constants and formulas stay fixed for P/C. U changes the scale operand and requires an explicit public contract. |
| `adaptive.rs:950–1016` | Exact prescribed publication versus P-bit prescribed values | Early scale eligibility excludes these rows, but D2 lower-bound sums include them. Preserve exact-sum/one-rounding custody and range semantics. |
| `adaptive.rs:1904–1949` | Verification scales and O9 eligibility | C retains these; P still needs old behavior for excluded rows unless its removal is separately proved. Avoid deleting implicit finite-extent checks. |
| `adaptive.rs:2020–2145` | Stop numerator, M selection, Phi and normalized trackers | Use the selected X rule for covered rows, unchanged V/W-plus/magnitude charges and exact comparison. Define summary denominator semantics. |
| `adaptive.rs:2188–2249` | Certified-bound checks and charge (d) | Keep uc/theta/g and low-p charge unchanged. Covered p512 charge must be tied to the same publication budget or a separately checked additional cap. |
| `adaptive.rs:2293`, `:2378` | Candidate publication conversion and typed pair dispatch | A helper must cover every candidate/verification width without private-state substitution or double rounding. |
| `adaptive.rs:2598–2658` | Final scale/class construction | Share or verify tentative/final scale bits, raw row eligibility and Phi. Do not materialize an entire second Publication merely for its scales without accounting for it. |
| `adaptive.rs:3196–3235` | Compare decision, work charge and acceptance | Rejected-p work and new checks must be charged under the actual work contract. No test-only uncharged fast path in production. |
| `adaptive.rs:3295–3360` | Final publication/evidence and bound encoding | Ensure the proved y/S survives finalization; define handling of unencodable scales and any new evidence. |
| `FK/src/structural/retained/verify.rs:321–379` | Shared e_hat and Phi bit rules | Preserve the single-source floor and its precision condition; do not silently substitute a newly rounded E or Phi. |
| `verify.rs:1113–1181` | t1/t3 and W-plus/charge formation | The proposal changes their allowance, not their certified derivation. Preserve A2's available-certified-bound semantics. |
| `R7:318–353`, `:563–583`, `:694–701` | Acceptance, corollary and receipt summary | Amend only by a new selected addendum after verification; retain hash-bound text as history. A sufficient new lemma is not an adopted amendment. |
| `R7:817–850` | D2 G5a lower bound, summaries and floor reconstruction | Close the explicit absolute-error/unit-conversion obligation; do not repeat the disproved relative scale-transfer premise. |
| `T3/DESIGN_NUMERICS/DESIGN.md:422–446` | Product stress propagation and relative floor | Carry pre-transformation subnormal error through each multiplier/divisor. Existing covered/not-covered and propagation factors remain protected. |
| `T3/DESIGN_STANDING/DESIGN.md:531–604`, `:638–742` | G5a/b/c, row standing and interval binding | Maintain raw-scale recomputation for P/C; assess U's changed evidence. Reconcile A1 bound meaning and existing publication factors with eventual S-I endpoints. |

Line numbers are source locators, not evidence that every surrounding module
was re-reviewed. Runtime input, solver arithmetic and the represented physical
model are not changed by the proposed acceptance-scale alternatives.

## Work and allocation questions for DELIVERY / K6c

Let N be the quantity count and B the body count. Current comparison holds a
candidate skip mask, Wide verification scales, report/state data, hats/floors
and bounded trackers; finalization later builds published values, classes and
evidence clones. An early publication projection changes overlap even if the
solver matrices are untouched.

| Question | What must be established before calling an impact zero |
|---|---|
| Early conversion | Can eligible candidate values be streamed into B sets of four f64 maxima using the existing conversion, or is a new N-element `Vec<Binary64Outcome>` retained? Is final conversion repeated or safely reused? |
| P versus C | P may still require Sv for excluded rows. C needs both paths or equivalent dual checks. Count actual vector length/capacity and Wide-width costs; do not assume the old scale allocation disappears. |
| Handoff to finalization | Are tentative scale bits stored in StopDecision, recomputed with an equality assertion, or borrowed from a shared immutable projection? Determine lifetime through accepted/rejected returns and every encoding failure. |
| Cache identity | Publication scales depend on the case/load state, not stiffness identity alone. A verification reused as the next candidate needs that pair's eligibility and new verification-derived Phi; do not cache the prior pair's floored scale as shared stiffness data. |
| U receipt evidence | Any additional per-body evidence, outward conversion and refusal state changes both the live-allocation table and encoded output sizes. |
| Work definition | Wide arithmetic and ExactWideSum work are metered today; binary64 conversion is documented as an uncounted value method. Identify actual removed/added operations and their governing definition rather than calling all new work free. |
| Rejected candidates and cache | Changes in accepted precision can alter solved-state retention, shared verification caches, number of attempts and peak overlaps. A local helper-size comparison alone cannot establish the final E_max or work bound. |
| Trackers/summaries | Reusing existing trackers, adding a second set or recording both denominators have different heap/work effects. Specify zero-budget/zero-numerator entries without forming 0/0; omission versus a recorded zero can change receipt inventory. Keep bounded tracking, refusal propagation and exact count reconciliation. |
| Integration order | K6c's final estimate and measurements must cover the chosen final kernel or an independently checked no-impact argument. No final admission or W1 limit can be established from this draft. |

No byte/LME delta is asserted without an implementation. Source locations are
exclusive implementation candidates, not a blanket write grant to FK, H or VR.
Shared consumer edits require ROOT's ownership assignment before fan-in.

## Proof and evidence gate

1. Freeze a complete chosen proposal, including exceptional rows, finite
   scale handling, summary meanings and D2 consequences, for fresh independent
   DESIGN-VERIFY. The sufficient X<=S lemma must be checked against all
   consumers and actual selected widths.
2. Incorporate remaining A0 findings. B01 establishes one clean selected
   driver; B02's forensic escalation emphasizes complete-layout gates. The
   unrun B boundaries and C hypotheses cannot be marked satisfied. A realized
   false claim raises the existing BLOCKING criterion; a failed C construction
   does not close the general proof gap.
3. Preserve existing controls/oracles and rejection evidence. A future repair
   needs discriminating controls and a reverted-change check under an exact
   frozen candidate; do not change expected outcomes merely to make it pass.
   Any changed precision/class/availability needs its derivation and impact
   account. This draft creates no new case or test assignment.
4. If source or reader changes are selected, follow the existing exact-head
   review, applicable registered checks, native evidence and PR gates. Source
   integration, numerical evidence, project acceptance and release stay distinct.

## Decision ownership, with concrete boundaries

The response graph's decision rule at lines 238–242 reserves narrowing the
guaranteed domain, published-contract/standing changes, accepted-criterion
changes, scope expansion and unresolved ownership conflicts to the human.
ROOT handles routine implementation choices within the authorized brief.
This draft does not add a human checkpoint merely because an existing test
or proof needs repair.

| Potential decision | Owning route and why |
|---|---|
| Internal P/C arithmetic, shared helper/storage, exact comparison and work charging | ROOT's D1 selection after independent verification can resolve an in-scope implementation choice **if** it preserves the accepted public guarantee/criteria and does not cross a reserved consequence below. |
| C as extra acceptance caps with original summary meanings | A concrete way to consider preserving existing public fields: retain original (a)/(d) summaries as their original tests and specify the additional publication guards separately. ROOT/verifier must establish the semantics and replay behavior; no hidden relabeling is permitted. |
| Replacing receipt denominator semantics, adding private-scale evidence, or U changing S/class/b meaning | Prepare a precise public-contract proposal for the human under the graph. Identical field names or constants do not make a changed attestation meaning immaterial. |
| Tightening a gate changes selected precision or refuses a previously selected case | Measure/disclose it and compare with explicit availability/retirement commitments. A numerical repair is not automatically a human decision; crossing an adopted availability criterion or narrowing the guaranteed domain is. Do not infer either outcome in advance. |
| New range exclusion to make the proof true | If it narrows the guaranteed/admitted domain, it requires the owning human decision. A pre-existing enforced exclusion may instead be proved and documented. |
| G5a criterion, propagation coverage or stated interval assurance needs change | Preserve current checks now; prepare the concrete contract/criterion delta and its consequence evidence for the owner. A failing proof does not authorize a relaxed reader check. |
| Changing epsilon, R, Q, A1 b, publication factors, lambda, charge constants or protected comparison limits | Not granted by this draft. Do not adjust them to obtain a pass. |
| KF3-B1, dense-screen policy, owner-held ceilings, final W1 limits, F2a implementation/release | Retain their existing owners and holds; none is selected or expanded here. |

No owner question is ready or required from this drafting checkpoint. The next
reviewable decision package needs the remaining evidence and independent
verification. ROOT may continue bounded preparation without pretending that
an alternative or public contract has already been accepted.

## Evidence continuity note

ROOT's later coordination commit is
`84843dbf9b74c4c3fdb727610998910b740a48ea`; numerical source remains 3bddc2b.
ROOT reports B02's latch resolved after fresh PID/group absence checks; its
numerical result remains guard-failed. No further B/C grant is inferred.
`Run/PORTABLE_EXPORT_REISSUE_01.json` maps the explicitly preserved original
timeout/build export seals to path-only portable views before their first
commit. Prior manager-return hashes remain dated original seals; B01/B02
packets and numerical inputs were not changed by that export correction.
