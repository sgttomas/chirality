# HUMAN-GATE HANDOFF — Tandem review (charter protocol step 7)

Date: 2026-07-26. Manager: Agent 0 (HELP_HUMAN posture, EVALUATION-manager
role). Status: **STEPS 1–6 COMPLETE — AWAITING OWNER DISPOSITIONS.** The
review edited no PRD, decomposition, SOW, governance, or product file; the
only git-state change across all stages is the read-only frozen worktree.
Step 8 (route smallest governed actions) begins only from the dispositions
below; per the charter, review closure is not product acceptance.

## Frozen artifact chain (integrity anchors)

| Artifact | sha256 |
|---|---|
| `FROZEN_BASIS_MANIFEST.md` | `b4a0ceb4b51b9a…` |
| `BRIEF_REVIEWER_A.md` / `BRIEF_REVIEWER_B.md` | `66e2e22a3625…` / `6fbf8317d9ed…` |
| `REVIEWER_A_REPORT.md` (pass 1, frozen) | `ee39da9fc11d9e56d9c7db8ab5bd458252519a1acd66e8504ec9c52fe650ee3e` |
| `REVIEWER_B_REPORT.md` (pass 1, frozen) | `5c20315e9ad7829afff0cfc021bf928a4ee05fbce8a7d2a10f1e63d69ba61cbf` |
| `VALIDATION_RECORD.md` (step 4) | `5d832a007a40…` |
| `CHALLENGE_BRIEF_A.md` / `CHALLENGE_BRIEF_B.md` | `b1aeac525b64…` / `1b2ed0e424c5…` |
| `CHALLENGE_A_ON_B.md` (step 5, frozen) | `c2b8beab30ce344f97e906095252c37c7f2a9ec97ab3991d9d2b676ec9f67ad6` |
| `CHALLENGE_B_ON_A.md` (step 5, frozen) | `f3d68abb9524d4a98adbd4929c2a50b6997ecc4fc18e7a77e50f53fba151d9de` |
| `FANIN_CLASSIFICATION.md` (step 6, refutation-corrected) | `c95d359c76eb05e02d97338a9974ab76c5b19f8932afe4d649b2dafc6b27c9f7` |
| Corpus | `/Users/ryan/dev/chirality-review-frozen-da31c19` @ `da31c19b5…`; charter `1756b844…` |

Challenge-stage validation (step 5→6 gate): both pass-1 reports byte-identical
after challenge; both challenges hash-verified their input report and brief
before reliance; coverage complete (every BLOCK+REVIEW challenged; WARN/INFO
samples recorded with rationale and omissions explained); verdict vocabulary
conforming; independence attested and mechanically confirmed (the only
cross-filename mentions are non-access attestations); corpus clean throughout.

Manager fan-in refutation (standing owner steer, supplementing the charter
protocol): one sealed adversarial refuter (opus-5, read-only) attacked the
step-6/7 synthesis against all four frozen inputs before this gate was
presented. Verdict: **0 CRIT / 4 MAJ / 5 MIN — all nine accepted and applied**
(FI-02's falsely-"identical" joint action re-separated and its F3 limb
relabeled NARROWED_TO_UNPROVEN; FI-04's discharge re-routed FI-08→FI-16;
FI-17's PEC-side act and RB-014's OI-009 note restored to D7/D6; D10's
"identical under either grade" claim corrected; plus five precision fixes).
The refuter verified all 33 findings dispositioned exactly once, both
challenge tallies exact, no averaging at either standing divergence, and six
load-bearing factual claims reproduced at the corpus.

## Headline

33 findings, 20 fan-in issues, **zero refutations in either direction** after
full reciprocal challenge. Every load-bearing quantitative claim in both
reports reproduced exactly under independently written parsers. Two NARROWs
trimmed one inference (F3 — carried forward as flagged-unproven, not
resolved) and one urgency characterization (pec.yaml blast radius); three
ADD-MISSING-EVIDENCE verdicts strengthened the findings they challenged. The corpus's central defect cluster is singular and consistent:
**the shared runtime's ownership is ruled but nowhere executable** — and its
surrounding basis, register, and propagation defects are specific, small, and
individually correctable.

## Decisions requiring owner judgment (rank order)

**D1 — Runtime ownership route (FI-02; RA-002≡RB-002, agreed-on-fact).**
Choose: (a) Root PRD amendment adding one operative runtime-ownership
commitment (M2 tranche under D-13/D-16), then Root SCOPE_CHANGE (B's
specific shape: split SOW-027 by maintenance locus with `runtime/` as a
declared write locus; A's shape: extend the decomposition); or (b) an
explicit recorded deferral on the OI-013 pattern naming where the work is
carried meanwhile — **terminal for v1 on A's routing; an acceptable interim
only on B's.** Both reviewers independently rejected any decomposition-only
fix as unlawful (D-9). Until one lands, the runtime has no Root deliverable,
no write locus, and no M2 gate — no lawful change path at all.

**D2 — App §13 semantic-ownership sentence (FI-01; RB-001≡RA-003, agreed-on-fact).**
Authorize the App SCOPE_CHANGE one-sentence clarification (deliverable
accountability vs runtime semantic ownership), with routed notices to Tier-0
and PEC. B expressly prefers A's smaller routing. Related same-tranche
candidates: FI-03 (SOW-037/DEL-03-01 rescope-or-defer), FI-05 (repin or
retire the D-APP-48 mirror — its target depends on this ruling).

**D3 — App basis repair (FI-06 unanimous BLOCK + FI-07).** Authorize one
bounded App tranche: re-pin the six unresolvable `decomposition_basis` fields
(deterministic defect, no scope change) and, at SCA-APP-004 implementation
closeout, re-pin all 51 contracts to one post-SCA-APP-004 basis
(single-pin pattern; optional fold-ins: six stale folder labels, RA-009).

**D4 — PEC-description staleness pair (FI-13 + FI-14).** Authorize the
Tier-0 residual row for D-T0-23, and rule the pec.yaml interim disposition
on the D-GOV-06 pattern (demote grant-bearing fields or mark
SUPERSEDED_PENDING_V2). Note the challenge narrowing: the profile's grant
reaches only the retired scratch/demo prototype — real authority defect,
lower urgency than B's pass-1 ranking asserted. Timing is yours.

**D5 — App register/coverage repairs (FI-08 + FI-09 + FI-10).** One App
SCOPE_CHANGE lane: SOW-064 coverage (or reasoned R6 deferral); the seven
§8↔§9 rows + authoritative-surface declaration (DL-15 precedent); the
invariant-coverage register create-or-defer (include §1.13 families if
created); the PKG-00 control-overlay ruling (retirement disposition
available — its SCC is closed).

**D6 — Root propagation repairs (FI-11 + FI-12 + RA-015 + RB-014).** Root
deliverable remediation for DEL-02-01 (cite SPEC §0.2.1 + D-GOV-26/27; no
new instrument needed); the O-1 clause-gap record or SOW-026 split; the
D-GOV-27 EffectiveSHA backfill + SOW-pin disposition already owed under
Receipt 52; and RB-014's OI-009/SOW-094 inheritance note (record that the
future RD-2 attribution referent must start from PEC-K-02 / PEC PRD §4.2 —
a register note, no commitment created; owner: Root decomposition companion
registers). Optional: commission the clause-granularity sweep (blind-spot 5).

**D7 — Cross-loop routing (FI-15 + FI-16 + FI-17 + FI-18).** Ship the
overdue D-GOV-26/27 notices to PEC and Piping; notice the RB-PEC-ADAPTER row
to PEC; open the Tier-0 coupling row for event-contract home / daemon feed /
auth-token reuse (D-T0-19 precedent); and authorize FI-17's consumer-side
half — the PEC open-issue-register annotation recording that PEC-K-03 /
PEC-K-11 have consumer-side obligations owned outside PEC, naming the owning
surface (owner: PEC loop; register annotation, no scope change).

**D8 — App acceptance-criteria posture (FI-20).** Judgment call the
reviewers deliberately did not make: is the conversion-fidelity AC pattern
(1.1 AC/contract; 0/53 in-contract human gates vs 41/45 Root, 28/32 PEC) an
accepted consequence of the D-APP-54 rebaseline, or a defect? If defect:
remediate the five P0 reliance-boundary deliverables first, on PEC's
in-corpus pattern. Note the open factor: App's SOW validation era is UNKNOWN.

**D9 — Method-layer tranche (FI-19 + RA-016).** One optional-field M2 tranche
against the D-GOV-16 instrument: `interfaces:`/`consumers:` element (making
producer/consumer relations deterministically checkable — the structural
mechanism behind the whole runtime cluster) + `acceptance_status:` field
(machine-readable candidate status). In-corpus shape precedent: the D-APP-48
`boundaries` object.

**D10 — Severity-calibration divergence (standing).**
The one standing divergence: whether "accepted instrument contradicted /
accepted commitment with no executable coverage" is BLOCK (B) or REVIEW (A).
The D2–D9 actions do not change with the grade; at D1 the grade tracks a
real difference — whether the recorded deferral closes the question (A) or
merely parks it as an interim (B) — so ruling D1's route also effectively
dispositions this. Rule it separately only if you want a corpus-wide
severity convention.

## Blind-spot register (from fan-in; candidates for targeted checks)

(1) whether any governed run has actually consumed the daemon (settles the
F3 limb); (2) SOW heading-set conformance (three App contracts carry a
seventh L2 heading); (3) App SOW validation era; (4) PEC PKG-07 seam depth —
structurally unavailable until P3/P4 SOWs; (5) clause-granularity sweep over
the remaining root scope items.

## What this review does NOT ask

No product acceptance; no severity averaging; no candidate architecture
(application profile, reusable work surface, resource governance) introduced
as scope — all three were correctly absent from every decomposition and
remain owner-held open questions (both reports' §5/§6 preserve the
alternatives and decision criteria). The three PEC REVIEW residuals
(manifest PEC-3) were assessed in context and generated no new findings.
