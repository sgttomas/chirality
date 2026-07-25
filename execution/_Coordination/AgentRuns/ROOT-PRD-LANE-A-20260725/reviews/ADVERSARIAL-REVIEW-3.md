# Adversarial Review 3 — PRD Candidate Rev 3 (ROOT-PRD-LANE-A-20260725)

Reviewer: same independent second agent, routed by the owner in-session,
2026-07-25. Subject: Rev 3 at `f9d33fcd9` (PR #340).
Verdict: **"converged substantially… one final precision revision before
the owner rules RD-1 through RD-5. The architecture no longer needs
reopening; the remaining issues concern authority, provenance, and
document mechanics."** Named strong: dual human loops, separable
capacities, root/variant reciprocity, self-application boundary, v1
objectives, honest unbuilt-checker treatment.

Agent 0 dispositions: all items ACCEPTED — see
`../briefs/PRD-AUTHOR-BRIEF-AMENDMENT-3.md`. Line references are to Rev 3
at `f9d33fcd9`.

## Review items (verbatim in substance)

1. **D-16 is materially overbroad** (PRD:384). "Every ruled or adopted
   governed artifact … never edited in place" conflates immutable approved
   bytes with living authoritative files. Chirality routinely amends
   `AGENTS.md`, DIRECTIVE, SPEC, status files, and other current surfaces
   through new accepted commits; Git preserves prior bytes; the pathname
   need not be frozen. Recommended replacement: any change to previously
   approved content requires a new attributable act bound to the resulting
   SHA, while prior approved bytes remain recoverable in Git. Only artifact
   classes explicitly declared immutable — decision records, accepted
   packets, snapshots — must never be overwritten at their path.
2. **D-1 and D-3 still generalize practice as existing doctrine**
   (PRD:369, :371). D-1: the accepted terminal-artifact rule permits either
   a decision record or PR review, not only decision records. D-3: the
   D-GOV-18/19/21 exact-candidate pattern is an exercised pattern, not a
   root-wide rule for every substantial proposal. Narrow each to its
   evidenced scope, label the generalization PROPOSED, or cite an actual
   universal governing clause.
3. **The genus conflict still violates the provenance key** (PRD:110).
   "Two accepted surfaces" + TRANSCRIBED label on README wording, while
   acknowledging README is non-binding. Say "two live surfaces"; retain
   TRANSCRIBED for DIRECTIVE; classify README as an observed repository
   fact / non-binding live wording; add an OBSERVED provenance category if
   necessary.
4. **Record the pair's two bases separately** (Annex:37, :300). Source
   corpus is `main@7ac718c7e`; PRD Rev 3 and annex are at `f9d33fcd9`; the
   annex cannot be "PRD Rev 3 at the same basis." Record SourceCorpusBasis,
   CandidatePRDSHA, CompanionAnnexSHA (or same containing commit) so D-14
   has an unambiguous source/candidate pairing.
5. **D-14 mechanical/semantic accounting is internally inconsistent**
   (Annex:26, :204). Header/main PRD say two classes are semantic; the
   table shows semantic work in (a2), (b), and (f); class (e) is only
   partly mechanical (recounting labels vs. deciding valid superseding
   linkage). Split (e); align all summaries and counts.
6. **Do not force root-product release into the iteration loop**
   (PRD:296). Release judgment evaluates whether the current product state
   may be released; informed by both operative and developmental evidence;
   not necessarily a decision to change the product. State it as a
   separately human-gated lifecycle judgment drawing from both loops.
7. **Tighten two objective quantifiers** (PRD:236, :238). OBJ-3: separate
   universal structural completeness from sampled retrieval usability.
   OBJ-5: "no variant change reaches root by any other path" is hard to
   prove — require instead that every root change claiming variant-derived
   provenance use the governed promotion path.
8. **Normalize the final adoption-ready PRD.** The final adopted document
   should not preserve extensive Rev-N correction commentary inside
   requirements; that history belongs in the annex and run evidence. The
   final PRD carries resulting identity, objectives, requirements,
   decisions, durable provenance pointers — not its drafting conversation.

Wording corrections: a decision record's ruling does not invariably
"become normative basis" — it may establish normative or operative
accepted state per its scope (PRD:309). The annex cannot make its own
status binding — its use is constrained by the already-binding upstream
derivative-package rule (Annex:12).
