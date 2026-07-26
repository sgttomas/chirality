# FAN-IN CLASSIFICATION — Tandem review (charter protocol step 6)

Manager: Agent 0 (HELP_HUMAN posture, EVALUATION-manager role). Date: 2026-07-26.
Inputs (all frozen, hashes in `VALIDATION_RECORD.md` and below): Reviewer A pass-1
(`ee39da9fc11d…`, RA-001..018), Reviewer B pass-1 (`5c20315e9ad7…`, RB-001..015),
Challenge A-on-B (`c2b8beab30ce…`), Challenge B-on-A (`f3d68abb9524…`).
Method: per charter — each issue classified as AGREED / RESOLVED_BY_EVIDENCE /
STANDING_DIVERGENCE / SHARED_BLIND_SPOT_RISK / STALE_INPUT. Agreement is not
proof; disagreement is not failure; nothing is averaged. Where a reviewer
conceded a point in challenge, the concession is quoted-in-substance, not
imposed. All 33 findings are dispositioned below; none is dropped or merged
away — grouping into issues preserves each finding's identity. Vocabulary
note: where a heading pairs AGREED with "RESOLVED_BY_EVIDENCE (…)" on FI-05,
FI-14, FI-15, the phrase marks a *challenge outcome that changed the
evidence state* (a confidence upgrade, an urgency narrowing, a corrected
supporting scan) — not the resolution of a reviewer divergence; no
divergence existed on those issues.

Challenge outcome summary: A-on-B — 9 CONFIRM / 0 REFUTE / 2 NARROW (RB-002,
RB-004) / 2 ADD-MISSING-EVIDENCE (RB-006, RB-013), 13 challenged (all 9
BLOCK+REVIEW + 4 sampled). B-on-A — 12 CONFIRM / 0 REFUTE / 0 NARROW / 1
ADD-MISSING-EVIDENCE (RA-001), 13 challenged (all 8 BLOCK+REVIEW + 5 sampled).
Zero refutations in either direction. Unsampled WARN/INFO findings (RA-009,
RA-010, RA-014, RA-015, RA-018 / RB-012, RB-014) stand as pass-1 findings,
unchallenged by recorded omission (reasoned for all but RA-009 and RA-018, which B listed without stated grounds).

---

## Cluster 1 — Shared-runtime ownership

### FI-01 · AGREED (fact) + STANDING_DIVERGENCE (severity) — App decomposition §13 asserts app-dev "retain[s] semantic ownership" of the runtime, contradicting D-GOV-20, CONTRACT K-RUNTIME-1, and App PRD §17
- Members: **RB-001 (BLOCK)** ≡ **RA-003 (REVIEW)**. Cross-confirmed: A CONFIRMed RB-001; B CONFIRMed RA-003. Every quote and line number verified by both.
- Fact state: AGREED and jointly re-verified from opposite lenses. A's challenge weakened one of B's three limbs (K-RUNTIME-1 speaks to *competing runtimes*, not ownership wording) — B's conclusion survives on D-GOV-20 + PRD §17 without it. B's challenge added that App's own conflict-surfacing duties (decomposition §2.1; PRD §16) were never exercised on this sentence, weakening the loose-drafting reading without settling it.
- New joint evidence (A's challenge, out-of-scope §4a, admissibility caveated as text-artifact): the shipped facade `frontend/packages/harness-contract/src/index.ts` states "Runtime contract ownership moved to the repository-root workspace" — the §13 sentence is now the sole artifact in the corpus asserting the contrary. A recorded this moves A toward B's severity.
- Severity: STANDING_DIVERGENCE, boundary-definition difference, both internally consistent (B: accepted-instrument contradiction = BLOCK; A: required unsafe-reliance path = REVIEW). Not resolved; not averaged.
- Smallest action (both reviewers converge; B expressly prefers A's routing as smaller): App SCOPE_CHANGE one-sentence clarification of §13 within OI-007's existing scope — deliverable accountability (app-dev) vs runtime semantic ownership (Root) — plus routed notice to Tier-0 and PEC per the change-notice rule. Owner: App loop + D-APP record.

### FI-02 · AGREED (fact) + STANDING_DIVERGENCE (severity) + one limb NARROWED_TO_UNPROVEN — Root `runtime/` has no owning package, deliverable, write locus, SOW, or M2 gate in accepted Root scope
- Members: **RB-002 (BLOCK)** ≡ **RA-002 (REVIEW)**. A's challenge NARROWed RB-002; B's challenge CONFIRMed RA-002 with every census reproduced (0/103 scope items; 0/45 deliverables; 0 `runtime/` write loci; `runtime/` outside SPEC §0.2.1 so no M2 gate; seven K-* runtime invariants bound with no Root owner).
- NARROWED_TO_UNPROVEN (one limb of RB-002, per A's NARROW — not resolved, and B did not concede): B's "F3 (self-authorization) is tripped" inference carries forward only as flagged-unproven — it requires facts about how root development actually executes (excluded by B's own observation boundary; A searched and found no record either way), and the record *indicates* App-extraction provenance rather than root-development production. The settling fact is blind-spot 1 below. The ownership gap itself carries at full strength.
- Strengthening evidence both directions: B's challenge added that D-GOV-20 is absent even from the decomposition's §2.3 interpretive-context list (the ruling was not weighed-and-excluded; it was not enumerated at all), supporting A's UNKNOWN-on-intent. A adopted B's two strongest structural points (K-* invariant binding; no-M2-gate) as established by B.
- Severity: STANDING_DIVERGENCE, same boundary difference as FI-01. Both recorded it identically and independently as "agreed-on-fact, divergent-on-severity."
- Smallest action (convergent on the routing constraint, distinct on shape — preserved): **A** frames (a) PRD amendment then SCOPE_CHANGE extension and (b) explicit recorded deferral (OI-013/§12.1 pattern) as alternative *terminal* routes — "execute only that one." **B** frames one sequence — (1) PRD amendment adding an operative runtime-ownership commitment (M2 tranche, D-13/D-16), then (2) Root SCOPE_CHANGE splitting SOW-027 by maintenance locus with `runtime/` as declared write locus — with the recorded deferral as an *acceptable interim only*. The SOW-027-split specificity is B's alone. Both independently hold that a decomposition edit alone is unlawful (D-9). Owner: Root PRD instrument / Root loop.

### FI-03 · AGREED — The App contract layer never received the rehoming; `DEL-03-01` still delivers a "product-owned" runtime engine contract
- Members: **RB-005 (REVIEW)**, CONFIRMed by A with a softening nuance A supplied: the rehoming *is* recorded as open work in `DEL-03-01`'s `_STATUS.md` Remaining — so a layer-propagation gap, not a total omission. 1/53 App contracts mentions the daemon; SOW-037 still reads "product-owned."
- Smallest action: App SCOPE_CHANGE amending SOW-037 / DEL-03-01 OUT-001 to client-conformance scope against the Root-owned contract, or explicit recorded deferral until Root's package exists. Owner: App loop.

### FI-04 · AGREED — The runtime↔client seam has no ScopeOfWork contract in any product (conjunction finding)
- Members: **RB-011 (WARN)**, CONFIRMed by A exactly (PEC PKG-05/06/07/09 = 0 contracts; one correction: PKG-07 has 5 deliverables, not 6 — conclusion unaffected). Explicitly does not contest PEC's deliberate sequencing (manifest conditions PEC-2/14). Discharged via FI-02 + FI-16 (per RB-011's own routing to RB-002 + RB-007); recorded so the conjunction is not lost if either is deferred.

### FI-05 · AGREED + RESOLVED_BY_EVIDENCE (confidence upgraded) — App's D-APP-48 pinned contract mirror is 12/12 stale; App has no working runtime-drift detection in either direction
- Members: **RB-013 (WARN, MEDIUM confidence, load-bearing count UNKNOWN)**. A's challenge located the pin contract, recomputed all 12 sha256s (12 stale / 0 matching), and verified the deprecation-shim rewrite — confidence upgraded MEDIUM→HIGH by evidence. A flagged that WARN "sits at the boundary" given the detection path is gone (one-cycle facade), not degraded, and combined with FI-02 there is no producer-side obligation either.
- Smallest action: repin or formally retire the mirror in the same tranche that dispositions FI-01, since the repin target depends on the ownership answer. Owner: D-APP / App SCOPE_CHANGE.

## Cluster 2 — Basis and register integrity

### FI-06 · AGREED (unanimous BLOCK after challenge) — Six App contracts pin a `decomposition_basis` object that does not exist in the repository
- Members: **RA-001 (BLOCK)**. B's challenge: ADD-MISSING-EVIDENCE — every core check reproduced independently (object absent, not shallow, 9-hex prefix coincidence, same six contracts, other four pins resolve, 53-pin census exact); B corrected A's mitigating count ("five of six" Gate-5 sections → actually three; the propagation conclusion holds 6/6 via row-level citations) and **agreed with BLOCK**. B disclosed its own pass-1 never tested pin resolvability — a lens-caught gap, recorded not absorbed.
- Smallest action (A, endorsed by B): re-pin the six fields to a resolvable commit in one bounded App tranche; no scope change. Owner: App loop CHANGE/closeout.

### FI-07 · AGREED — App's SOW layer declares five bases, all ≤2026-07-13, all superseded by SCA-APP-003/004; PEC is the only product whose SOW basis is byte-current
- Members: **RA-008 (REVIEW)**, CONFIRMed to the digit (blob comparisons included). B added: the staleness concentrates exactly where change is fastest (the runtime/UI amendments) — the same region as FI-01/FI-03.
- Smallest action: re-pin all 51 to one post-SCA-APP-004 commit at SCA-APP-004 implementation closeout, single-pin pattern per Root/PEC. Owner: App loop under SCA-APP-004's pointer. Fold-in candidates: FI-06's six contracts; RA-009's six stale folder labels (WARN, unchallenged-by-recorded-omission).

### FI-08 · AGREED — SOW-064 has no executing contract while telemetry certifies zero unmapped items; seven §8↔§9 register disagreements; no companion register to arbitrate
- Members: **RA-004 (REVIEW)** + **RA-005 (REVIEW)**, both CONFIRMed with independent parsers (7 mismatches item-for-item; Root 0 / PEC 0 controls reproduced). B refined: three of seven are OUT boundary items, so residual IN-item exposure is SOW-064 + three benign-covered items; and B proved A's mechanism by construction (contract frontmatter reproduces §8 with 0/51 mismatches — so §9-only items can never reach a contract). B's severity note: telemetry is true *of the ledger*; the defect is metric-computed-on-the-wrong-surface.
- Smallest action: add SOW-064 to DEL-06-02/-03 coverage + contract refs (or reasoned R6 deferral); reconcile the seven rows; declare which surface is authoritative (PEC DL-15 precedent). Owner: App SCOPE_CHANGE.

### FI-09 · AGREED (severity resolved by challenge concession, not averaging) — App PKG-00 control contracts pin a README as `decomposition_basis` and mint a `CONTROL-*` namespace outside any accepted decomposition
- Members: **RB-009 (REVIEW)** ≡ **RA-010 (WARN)**. A's challenge CONFIRMed RB-009 and conceded B's REVIEW is better calibrated (A had missed the D-9 self-authorization dimension; the bound on the overreach is asserted by the artifacts themselves). B's discharged-condition observation verified (SCC closed → retirement may be the smallest act).
- Smallest action: owner ruling recording PKG-00 as a control overlay outside decomposition truth (or a CONTROL_PACKAGE provision in the SOW standard via M2); retirement disposition available. Owner: D-APP register or D-GOV-16 instrument.

### FI-10 · AGREED (severity resolved by challenge concession) — `contract_invariant_coverage_register.csv` required-or-deferred, absent, undeferred; the §10A.1 family table does not reach the §1.13 runtime invariants at all
- Members: **RB-010 (REVIEW)** ≡ **RA-014 (WARN)**. A CONFIRMed RB-010 and conceded REVIEW (A had not checked the §1.13 blind spot — the invariant family most affected by the rehoming is the one the substitute surface omits). B's challenge OOS-2: classify with FI-08 as one shared root cause (absent companion register); one corrective act discharges both.
- Smallest action: create the register (including §1.13 families as consumed invariants) or record an explicit deferral naming REVIEW closure as gate. Owner: App loop before any REVIEW closure.

## Cluster 3 — Supersession and propagation

### FI-11 · AGREED — Root `DEL-02-01` would settle instruction-surface membership from a superseded enumeration; the omission of SPEC §0.2.1 / D-GOV-26/27 / CLAUDE.md is total
- Members: **RA-006 (REVIEW)**, CONFIRMed and strengthened by B (zero occurrences of any governing instrument in the contract). B disclosed this as "the strongest finding in A's report that my lens missed" and recorded it as a counterexample sharpening RB-008: even single-product supersession fails to reach the executable layer. B considered and rejected BLOCK (nothing ISSUED; ruling exists; contained remediation).
- Smallest action: amend CLM-002/CON-001 to cite SPEC §0.2.1 + D-GOV-26/27 (eight members); re-scope CON-001 to what genuinely remains open. Owner: Root deliverable remediation; no new instrument.

### FI-12 · AGREED + candidate systematic-defect flag — Multi-clause PRD commitments collapsed into single scope items where registers cannot see the missing clause (O-1 membership clause; O-2 runtime clause)
- Members: **RA-013 (WARN)**, CONFIRMed and strengthened by B (zero of 103 scope items name any instruction-surface member); B's pass-1 M1 found the same mechanism on O-2 independently. Challenge OOS (B-3): two reviewers, two commitments, same normalization defect, in a decomposition that split N-1/N-5/D-14 for exactly this reason — systematicity untested; a targeted check across the remaining ~100 scope items is the natural follow-up.
- Smallest action: record the O-1 clause gap on the OI-013 pattern or split SOW-026 per DEC-004/005 precedent; owner decides whether to commission the systematic check. Owner: Root SCOPE_CHANGE.

### FI-13 · AGREED — Tier-0 D-T0-23 preserves PEC capabilities that PEC PRD v2.1 retired; no supersession recorded at the Tier-0 surface
- Members: **RB-003 (REVIEW)**, CONFIRMed exactly (register grep: zero supersession/residual rows referencing T0-23; ordering verified; PEC PRD names only D-PEC-56).
- Smallest action: Tier-0 residual row on the register's own convention (8 precedents). Owner: Tier-0 register / owner ruling.

### FI-14 · AGREED (conflict) + RESOLVED_BY_EVIDENCE (urgency narrowed) — `_DomainEngines/profiles/pec.yaml` remains ADOPTED at L3 with grants PEC PRD v2.1 forbids
- Members: **RB-004 (REVIEW)**, NARROWed by A: the authority conflict is confirmed at every cited line and is the most valuable no-counterpart finding in B's report (A never examined the profile); the "live blast radius / do not wait" urgency is overstated — the residency grant self-limits to scratch/demo mutation and PEC PRD §13 records no production data, so it is a standing grant over a retired, dataless prototype. Severity REVIEW stands on the narrowed basis; B's fan-in ranking of this as "the urgent half" should be down-weighted.
- Smallest action (unchanged by narrowing): interim owner ruling on the D-GOV-06 pattern (demote grant-bearing fields or mark SUPERSEDED_PENDING_V2); full supersession stays SOW-090's deferred work. Owner: DOMAIN_ENGINE proposal → owner ruling. Timing is the owner's call with the narrowed urgency in view.

### FI-15 · AGREED + RESOLVED_BY_EVIDENCE (supporting scan corrected) — The only runtime reliance-boundary register is consumer-owned (App), asserts the daemon boundary, and its `RB-PEC-ADAPTER` row describes the retired PEC product
- Members: **RB-006 (REVIEW)**, ADD-MISSING-EVIDENCE by A: assertion verified in full; B's supporting Root-SOW scan corrected (named a non-matching contract, omitted three matching; corrected set — mostly export-script path hits — supports B's conclusion *more* strongly).
- Smallest action: (a) routed notice of the RB-PEC-ADAPTER row to PEC now; (b) re-home the daemon rows to Root when FI-02's package exists; meanwhile the register should self-describe as consumer-side. Owner: App DEL-01-02 remediation + notice per change-notice rule.

### FI-16 · AGREED — The event-contract home and daemon global event feed are cross-loop decisions whose named closing act has no addressee
- Members: **RB-007 (REVIEW)**, CONFIRMed exactly, including the D-T0-19 coupling-row precedent. Both reviewers record PEC's self-fencing as exemplary; the defect is producer-side ownership.
- Smallest action: Tier-0 coupling row for the three items (event-contract home; daemon feed design+ownership; auth-token reuse). Owner: Tier-0 register + owner ruling. If FI-02 lands first, the row becomes a pointer.

### FI-17 · AGREED (complementary halves, kept distinct) — The PEC↔runtime boundary is unowned in both directions
- Members: **RA-012 (WARN)** (consumer-side: PEC-K-03/K-11 obligations on harnesses/agent instructions with no assigned owner; MEDIUM/UNKNOWN calibration confirmed by B) + **RB-007** (producer-side, FI-16). B's challenge: "the manager should not treat them as one issue" — together they show the boundary unowned both ways, which neither shows alone. Honored: recorded as two findings, one conjunction note.
- Smallest action: RA-012's register annotation in PEC's open-issue table naming the external owner; FI-16's coupling row. Owners: PEC loop; Tier-0.

### FI-18 · AGREED — Root-doctrine notice routing is asymmetric (App 4, domains/chirality 3 no-D-GOV-26, PEC 0, Piping 0)
- Members: **RA-011 (WARN)** ≡ **RB-015 (INFO)** — same underlying asymmetry, cross-confirmed on each reviewer's own measure (A: files citing D-GOV-20..27 — App 20 / PEC 2 / domains-chirality 4 / Piping 0; B: routed D-GOV-* notice files — App 4 / domains-chirality 3 (no D-GOV-26) / PEC 0 / Piping 0; both sets reproduced exactly at challenge). Divergence is presentational only (B folds the remedy into FI-13/FI-15; A carries it as its own with MEDIUM materiality). One immaterial correction logged by A on RB-015 (a notice-title attribution).
- Smallest action: ship routed D-GOV-26/27 notices to PEC and Piping coordination surfaces. Owner: Root loop (DEL-04-04 owns this class).

## Cluster 4 — Method layer and acceptance quality

### FI-19 · AGREED + recorded calibration tension — The ratified SOW standard has no interface/consumer/dependency element, so cross-product relations have no home in the executable contract layer
- Members: **RB-008 (WARN)**, CONFIRMed exactly (all three structural claims; 130-contract frontmatter census). A's challenge flags the tension B's own framing creates: the mechanism behind both BLOCK-cluster issues ranks ninth by severity — defensible (no contract violates the standard as written; remedy correctly optional) but worth the owner's eye. Challenge OOS (A-b): the D-APP-48 `boundaries` object + per-file sha pins + lint command is an in-corpus precedent for the proposed `interfaces:`/`consumers:` shape.
- Smallest action: optional `interfaces:`/`consumers:` element via M2 tranche against the D-GOV-16 instrument. Candidate to ride the same tranche: RA-016's optional `acceptance_status:` field (B's challenge suggests combining). Owner: D-GOV-16 / shared method layer.

### FI-20 · AGREED (measurement) + open factor routed to owner — App acceptance criteria test conversion fidelity, not deliverable fitness; 0/53 name a human gate in-contract (vs 41/45, 28/32)
- Members: **RA-007 (REVIEW, MEDIUM on severity)**, CONFIRMed to the digit on all six metrics by independent extraction; A's counter-evidence (real, well-evidenced `_STATUS.md` human gate) verified; A's "at least 13" conversion-shaped is a lower bound (B: 16 by broader pattern). Open factor (B's challenge + OOS-4): App's SOW validation era is UNKNOWN (manifest condition 15 fixes eras only for Root/PEC), so part of the divergence may be method-era artifact — supports A's routing to owner rather than asserting failure.
- Smallest action: owner judgment first (deliberate rebaseline consequence vs defect); if remediation, start with the five P0 reliance-boundary deliverables per RA-007, using PEC's contracts as the in-corpus pattern (RA-018). Owner: App loop / WORKING_ITEMS-equivalent sequencing.

## Cluster 5 — Findings dispositioned outside the 20 issues (stand as found; RA-016 and RA-017 were sampled and CONFIRMed at challenge, the rest unchallenged)

- **RA-009 (WARN)** six stale App folder labels — fold into FI-07's tranche or record labels-frozen-at-creation. **RA-015 (WARN)** D-GOV-27 EffectiveSHA unbound + Root SOW pins behind DEC-021 (content verified current; pin metadata behind; conditions 1/3 consequence assessment). **RA-016 (INFO)** candidate-status machine-opacity → FI-19 tranche. **RA-017 / RA-018 (INFO, positive)** Root+PEC register integrity and PEC contract discipline — B's challenge independently reproduced RA-017's five zero-mismatch checks; adopted as the corpus's positive baseline. **RB-012 (WARN)** PEC kill test lacks an accepted release path to bind into — two halves of one unbuilt path with Root DEL-06-07; correct posture already in-contract. **RB-014 (WARN)** Root RD-2 attribution path names PEC against PEC's permanent non-goals — latent, not-current-scope; smallest act is an OI-009/SOW-094 inheritance note.

## SHARED_BLIND_SPOT_RISK (explicit register)

1. **Daemon consumption fact.** Neither reviewer examined whether any governed run has actually consumed the daemon — the fact that would settle FI-02's F3 limb. Both treated ownership documentarily (both declared boundaries exclude runtime behavior). Flagged by A's challenge; endorsed here.
2. **Heading-set conformance.** Three App contracts carry a seventh L2 heading (`## SCA-APP-004 Gate-5 Current Contract (Controlling)`) against the standard's six-"in order"; neither register covers heading conformance (B's challenge OOS-1).
3. **App SOW validation era.** UNKNOWN at this basis (affects FI-20's interpretation); not resolvable from the frozen corpus (B's OOS-4).
4. **PEC PKG-07 seam depth.** Structurally unreviewable until P3/P4 SOWs exist (validation-record limitation; both reviewers noted via other evidence).
5. **Scope-item clause-granularity sweep.** FI-12's mechanism found twice independently; the remaining ~100 root scope items untested for it.

## STALE_INPUT

None. No finding in either report rests on superseded bytes; all evidence was drawn from the frozen corpus, and the five detail corrections surfaced in challenge (RA-001 "five of six"→three-with-mechanism; RA-002 "six"→seven packages; RB-006 scan set; RB-011 "6"→5 deliverables; RB-015 notice-title attribution) were non-load-bearing and are recorded inside FI-06/FI-02/FI-15/FI-04/FI-18.

## Positives adopted at fan-in (so the corpus is not misdescribed)

Root's four-category coverage without folder mimicry (both M3-Q3: "exemplary"/"PASSES — done well"); Root's OBJ-2/OI-013 deferral as the model machine-visible disposition; Root+PEC register integrity at zero mismatches under exhaustive independent reproduction; 0-mismatch SOW frontmatter across all 128/130 checked contracts; PEC's boundary discipline, kill-test posture, and current-basis SOW layer (only product byte-current); App's human/agent mediation FR layer (B M3-Q6 "strongest area") and its real, evidenced `_STATUS.md` human gate; no decomposition invented candidate architecture (application profile, reusable work surface, resource governance all correctly absent).
