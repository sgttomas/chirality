# V1 Terminal Return — Adversarial verification of the candidate root decomposition

Run: `ROOT-STEP8-DECOMP-20260725` · Node: V1 · Role: ephemeral bounded Agent 2
generalist under sealed brief from `HELP_HUMAN`
Basis: `24726a73c64a849909e3615c32ef1a888b3dfd36` (= worktree HEAD) · Date: 2026-07-25
Posture: read-only; the only file written is this return.

**Overall verdict: BLOCKERS-FOUND — one (1) BLOCKER, one (1) MAJOR, six (6)
MINOR.** The BLOCKER is a false quantitative claim in the narrative, not a
structural defect: every register, count, and trace direction reconciles
mechanically on independent recomputation. The candidate's partition,
identifiers, ledger, and both F4 registers survive falsification attempts.

---

## 1. Method

I did not read N1's telemetry and accept it. I re-derived every count from the
CSVs with an independent script (`scratchpad/verify.py`, outside the repo),
re-enumerated the PRD's §5 IDs directly from `docs/PRD_ROOT.md`, recomputed the
sha256 of every pinned reference, re-ran all five validators, and read all 103
ledger rows and all 45 deliverable rows.

---

## 2. Per-check verdicts

### Check 1 — F4 traceability, both directions · **PASS (with one MAJOR)**

**(a) Every proposed PKG/DEL traces to a real PRD requirement or objective.**
The reverse register carries exactly 51 rows = the 6 `PKG-*` ∪ 45 `DEL-*`
identifiers, no more, no fewer (set equality verified). All 51 read `TRACED`;
no row has an empty `PRDItems`. Every `PRDItem` cited in the reverse register
exists in the forward population (0 dangling). Independently, for each of the
six packages I recomputed the union of `PRDItem` and `ScopeItemID` over the
ledger rows it owns and compared to the reverse row: **symmetric difference
empty for all six**. Every cited PRD ID exists in `docs/PRD_ROOT.md` — the
42 §5 commitments, OBJ-1..7, F1..F6, RD-1..RD-5, C-1..C-4, and the section-tag
items all resolve. Spot-reading of substance (all 6 PKGs, all 45 DELs) found no
deliverable claiming a PRD ID that does not support it, with one weak mapping
noted at MINOR-3.

**(b) Every OBJ and every §5 commitment covered or deferred.** I enumerated the
§5 IDs from the PRD myself rather than from N1's register:

```
N-1..N-9 (9) · O-1..O-10 (10) · D-1, D-2, D-4..D-16 (15; D-3 absent) · E-1..E-8 (8) = 42
```

matching the PRD's own §10.4 provenance count. All 42 appear in the ledger's
`PRDItem` column and in the forward register at `COVERED`. All of OBJ-1..OBJ-7
appear as forward rows at `COVERED` with non-empty scope-item, package, and
deliverable mappings. **No §5 commitment and no objective is silently missing
from both coverage and deferral.** Forward register: 84 rows, 84 `COVERED`, 0
`DEFERRED`, 0 `UNCOVERED`, 0 duplicate `PRDItem`, 0 rows with empty
`ScopeItemIDs`, 0 dangling SOW/DEL references. The 84-item enumeration in
telemetry §5 sums to exactly 84.

The **MAJOR** below concerns the *granularity* at which objectives are traced,
not a missing ID.

### Check 2 — D-15 category coverage · **PASS on the obligation, FAIL on one supporting claim**

All four §4.1 categories are `COVERED`; none is deferred, and none is claimed
deferred. Recomputed from the ledger's `Categories` column — the D-15 table's
own numbers reproduce **exactly**:

| §4.1 category | Scope items (claimed / recount) | Packages (claimed / recount) | Deliverables (claimed / recount) |
|---|---|---|---|
| Normative basis | 41 / **41** | 6 / **6** | 21 / **21** |
| Operative product | 26 / **26** | 5 / **5** | 18 / **18** |
| Developmental machinery | 59 / **59** | 5 / **5** | 25 / **25** |
| Evidence | 18 / **18** | 4 / **4** | 16 / **16** |

The per-category deliverable membership lists in telemetry §4 also enumerate
exactly 21 / 18 / 25 / 16 members. No scope item lacks a category.

The partition is **not** a forced mirror of the four categories: six packages,
not four; no package is coextensive with any category; every category spans
four or more packages. **But the second half of the non-identity claim is
false** — see BLOCKER-1.

### Check 3 — D-9 no-invention scan (I2) · **PASS**

Sampled every PKG (6/6) and every DEL (45/45 — full, not half), plus all 103
ledger rows.

- **Every one of the 103 `SourceRef` values names a `docs/PRD_ROOT.md` section.**
  Zero rows cite `AGENTS.md`, `DIRECTIVE`, `CONTRACT`, `TYPES`, D-GOV-21, a live
  registry, the sealed brief, or the app-dev precedent. No scope is drawn from
  incorporated-by-reference documents.
- Every deliverable's substance reduces to its `CoversScopeItems`, and every
  such scope item is PRD-derived. The deliverable↔ledger coverage mapping is
  **bijectively consistent in both directions** (0 mismatches over 45
  deliverables); no deliverable covers a scope item the ledger does not assign
  it, and no deliverable covers zero scope items.
- Splits (N-1→2, N-5→3, D-14→2) are declared at DEC-004/005 and each part is
  traceable to source prose. The v1-boundary, §7.2, §8.3, §9.2 and §10.3 splits
  likewise track enumerated source clauses.
- Two project-specific deliverable types were added. `REF-003` expressly permits
  "or project-specific equivalents" and requires recording in the Vocabulary
  Map; both are recorded (DEC-011). `REGISTER` is used 7×; `GOVERNANCE_TRANCHE`
  is declared but unused (MINOR-6).
- One boundary observation at MINOR-5: `DEL-03-05`'s *AnticipatedArtifacts* name
  four concrete `execution/_harness/*.yaml` paths that are not in the PRD. I
  verified they are real (the live G0–G3 validators reference exactly those
  paths) and the underlying scope (SOW-001, SOW-034 → v1 boundary (a), O-9) is
  PRD-grounded. This is implementation detail, not invented scope.

### Check 4 — Standard conformance · **PASS**

| Item | Result |
|---|---|
| **I3 flat partitions** | 6 packages, no nesting, no phases, no sub-partitions. PASS |
| **I4 exactly one partition per IN unit** | Mechanically checked over all 103 rows: every row carries exactly one `PackageID`, all six resolve to real packages, 0 multi-valued, 0 unknown. OUT rows also carry one (stricter than REF-002; disclosed at OI-012/DEC-007 — a strengthening, not a weakening). PASS |
| **I5 ID stability** | First revision; no prior IDs to break. `SOW-001..SOW-103` is exactly sequential with no duplicates or gaps; `DEL-XX-YY` YY is sequential within every package. PASS |
| **I6 coupling** | All 45 `DEL-XX-YY` prefixes mechanically equal their `ParentPackageID`'s `PKG-XX`. 0 violations. PASS |
| **I9 telemetry** | Present, and every base field of both `DECOMPOSITION_STANDARD` §STRUCTURE and `AGENT_SOFTWARE_DECOMP` §6 is present under the manager's declared domain names. `UnassignedScopeItems` (= `UnassignedINUnits`) recomputed **0**; `ScopeItemsWithoutDeliverableMapping` **0**; `UnmappedObjectives` **0**. **All counts reconcile on recount** — see §3. PASS |
| **I10 vocabulary map** | Present (§5), `CanonicalTerm`/`Synonyms`/`Notes`. PASS |
| **Required sections** | All 8 of `AGENT_SOFTWARE_DECOMP` §STRUCTURE present (Vocabulary Map §5, SSOW §6, Packages §8, Deliverables §9, Scope Ledger §10, Coverage & Telemetry §11, Open Issues §12, Decision Log §13), plus Gate Log, References, Intake Summary, Companion Inventory, Downstream Notes. `ContextEnvelope` on all 45; `ContextEnvelopeNotes` present on all 45 (mandatory only for L/XL); `AnticipatedArtifacts` non-empty on all 45; `ResponsibleParty` = `TBD` on all 45. PASS |
| **Package-role labels** | Working surface and telemetry carry in-file `Package Role:` labels; the five CSVs are labeled through the companion inventories (§3 and telemetry §7). Meets the standard's requirement; see MINOR-4. PASS |
| **No acceptance claimed** | All 7 Gate Log rows read `PENDING_OWNER_RULING`. A full-package grep for acceptance/approval/ratification language returned only (i) transcribed PRD prose containing the word "accepted", (ii) `RATIFIED` describing REF-002, and (iii) explicit *disclaimers*. Gate 7 states the acceptance phrase "has not been said by anyone". **No agent-side acceptance anywhere.** PASS |

### Check 5 — SPEC ID format and G2 readiness · **PASS**

All 6 package IDs match `^PKG-\d\d_[A-Za-z0-9_]+$` and all 45 deliverable IDs
match `^DEL-\d\d-\d\d_[A-Za-z0-9_]+$`, conforming to `docs/SPEC.md` §1
(`PKG-XX_{PkgLabel}` / `DEL-XX-YY_{DelLabel}`) and §10.1 sanitization (no
`/ \ : * ? " < > |`, no whitespace). **G2 literal containment: all 51
identifiers verified present verbatim in
`Chirality_Root_SOFTWARE_DECOMP_v1_0.md`; missing = none.**

### Check 6 — Scope hygiene · **PASS**

```
$ git status --porcelain
?? execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/
?? execution/_Decomposition/

$ find execution -type d \( -name 'PKG-*' -o -name 'DEL-*' \)
(no output)

$ python3 tools/validation/validate_root_materialization_fence.py
G0 PASS: no PKG-*/DEL-* direct children under root execution/; fence idle (D-GOV-21 gate not yet in play).
exit=0

$ python3 tools/validation/validate_path_anchors.py
PASS: no literal home-dir absolute paths found in 996 live path-anchor surfaces
exit=0
```

No tracked file is modified; no instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/`) is touched; nothing
exists under `execution/_harness/`. I also independently re-ran the three
guards N1 reported beyond its brief — G1, G2, G3 all PASS idle, output
identical to N1's transcript.

### Check 7 — Candidate-posture hygiene · **PASS**

- **No machine-absolute paths.** Independent sweep of `execution/_Decomposition/`
  for `/Users/`, `/home/`, `C:\Users\` → 0 matches. N1's caveat that
  `_Decomposition` sits on the path-anchor validator's excluded-directory list
  is **true and verified** (`tools/validation/validate_path_anchors.py:44`) —
  an honest disclosure, correctly requiring the separate sweep.
- **Reference pins verified independently with `shasum -a 256`:**

  | RefID | File | Claimed sha256 | Verified |
  |---|---|---|---|
  | REF-001 | `docs/PRD_ROOT.md` | `e98031c1…bb63eb` | **MATCH** |
  | REF-002 | `docs/DECOMPOSITION_STANDARD.md` | `9e356ea1…5252cea` | **MATCH** |
  | REF-003 | `agents/AGENT_SOFTWARE_DECOMP.md` | `ad849d9a…feb43409` | **MATCH** |
  | REF-004 | `docs/SPEC.md` | `aa43e932…dcd0621f64` | **MATCH** |

  Basis commit `24726a73c…` exists and is this worktree's HEAD.
- **Interpretive context is labelled non-source.** §2.3 lists the six
  incorporated-by-reference surfaces under the heading "Interpretive context —
  **non-source, generates no scope**"; §2.4 labels the app-dev precedent
  non-source. Confirmed by the `SourceRef` audit under Check 3.

---

## 3. Commitment-coverage and telemetry recount

Every claimed figure re-derived from the CSVs. **Claimed = recount in every
cell.**

| Metric | N1 claim | Independent recount | |
|---|---:|---:|---|
| Ledger rows | 103 | **103** (`SOW-001..SOW-103`, no gaps/dups) | ✓ |
| IN / OUT / TBD | 94 / 9 / 0 | **94 / 9 / 0** | ✓ |
| Packages | 6 | **6** | ✓ |
| Deliverables | 45 | **45** (8/5/6/10/8/8 per PKG-01..06) | ✓ |
| Objectives | 7 | **7** (OBJ-001..007, 1:1 with PRD OBJ-1..7) | ✓ |
| UnassignedScopeItems | 0 | **0** | ✓ |
| ScopeItemsWithoutDeliverableMapping | 0 | **0** | ✓ |
| UnmappedObjectives | 0 | **0** (each has ≥1 ledger item and ≥1 supporting DEL) | ✓ |
| ContextEnvelope | S=14 M=30 L=1 XL=0 | **S=14 M=30 L=1 XL=0** (S list identical) | ✓ |
| PRD forward items | 84 | **84**, all `COVERED` | ✓ |
| Reverse units | 51 | **51**, all `TRACED`, set-equal to 6 PKG ∪ 45 DEL | ✓ |
| §5 commitments enumerated from PRD | 42 | **42** (9 N / 10 O / 15 D / 8 E; D-3 absent) | ✓ |
| Open issues | 12 | **12**; 12 ledger rows flagged `TRUE`; type counts sum to 12; per-issue row partition (8+2+1+1) reconciles | ✓ |
| Objective→deliverable table (§7) vs objective register | — | **identical for all 7** | ✓ |
| Reverse package rows vs ledger-derived unions | — | **identical for all 6** | ✓ |
| Deliverable `CoversScopeItems` vs ledger `DeliverableIDs` | — | **0 mismatches over 45** | ✓ |

---

## 4. Findings

### BLOCKER-1 — False claim: "every package participates in at least three categories"

**Locations (three, all load-bearing for the D-15 / §4.3 argument):**
- `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md:245–247`
  (§8, "Why six and not four")
- `execution/_Decomposition/chirality_root_coverage_telemetry_v1_0.md:81–82` (§4)
- `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/returns/N1_RETURN_RAW.md:66–67`
  (§3) — the sentence wraps across lines, so a single-line grep misses it

**The fact.** Recomputing category participation per package from the ledger's
`Categories` column:

| Package | Categories participated | Count |
|---|---|---:|
| PKG-01 | Normative basis, Operative product, Developmental machinery, Evidence | 4 |
| **PKG-02** | **Normative basis, Operative product** | **2** |
| PKG-03 | Normative basis, Operative product, Developmental machinery | 3 |
| PKG-04 | all four | 4 |
| PKG-05 | Normative basis, Developmental machinery, Evidence | 3 |
| PKG-06 | all four | 4 |

**PKG-02 participates in two categories, not three.** This holds under every
available reading: PKG-02's eight scope items (SOW-013, 019, 026, 027, 028,
029, 030, 035) carry only `NormativeBasis` and `OperativeProduct`; no PKG-02
deliverable appears in telemetry §4's `Developmental machinery` or `Evidence`
membership lists; and no PKG-02 scope item or deliverable maps across package
boundaries in a way that would add a category.

**Why it is a BLOCKER rather than a MINOR.** Per the brief's severity
definition it "misstates a fact to the owner", and it is not incidental prose:
it is offered in all three surfaces as *the evidence* that the proposed
partition is not a disguised mirror of the four §4.1 categories — the exact
question §4.3 and D-15 put to this gate. The owner would be ruling Gate 4 and
Gate 6 partly on a recomputable claim that does not hold.

**Mitigation the owner should know.** The D-15 table itself is **correct** — it
lists PKG-02 only under Normative basis and Operative product, so the register
does not carry the error, only the narrative gloss does. The conclusion also
survives correction: six packages ≠ four categories; no package is coextensive
with any category; every category still spans four or more packages (verified);
and the largest package, PKG-04, spans all four. The fix is a text correction
in three files (e.g. "every category spans four or more packages, and no
package is coextensive with a category — participation ranges from two
categories (PKG-02) to all four"), not a re-partition.

### MAJOR-1 — OBJ-2's "and in at least one situated working root" has no coverage and no deferral

**Location:** `chirality_root_objective_register_v1_0.csv` OBJ-002;
`chirality_root_prd_coverage_forward_v1_0.csv` row `OBJ-2`;
`Chirality_Root_SOFTWARE_DECOMP_v1_0.md` §7.

PRD §3 OBJ-2's success condition ends: "**Demonstrated at root and in at least
one situated working root.**" The objective register faithfully restates that
clause. But of the eight deliverables mapped to OBJ-002, none addresses the
situated-working-root half: `DEL-03-06` carries the deliverable stream **at
root only** ("carry one complete deliverable stream end to end"). The one
situated-root deliverable, `DEL-06-08_Situated_Working_Root_Convergence_
Demonstration`, is mapped to **OBJ-005**, covers only SOW-003, and is about a
*recorded convergence path* (v1 boundary (c)) — not about a deliverable stream
reaching an issuance decision in a variant. No scope item states the missing
clause, and no reasoned deferral is recorded.

**Mechanism — why the registers cannot see this.** The ledger contains no scope
items derived from the objectives' internal success conditions; objectives are
traced only as whole units through the objective register. F4 therefore reads
`COVERED` for OBJ-2 at objective granularity while a testable condition inside
it is uncovered. F4 is **not formally tripped** (the objective has coverage),
but the gap is real and the owner should see it before ruling Gate 3/Gate 6.
Two cheap dispositions: add a scope item for the clause and map it (to
`DEL-03-06` or a new PKG-06 deliverable), or record an explicit reasoned
deferral to a post-v1 stage.

*Related but lower-grade instances of the same mechanism, checked and found
adequately covered:* OBJ-3's pre-registration requirement (covered explicitly
by `DEL-05-08`), OBJ-6's stale/orphan detectability (covered explicitly by
`DEL-06-02`). OBJ-5(ii) ("every root change claiming variant-derived
provenance used the governed path") is only implicitly covered by `DEL-06-06`
— worth an owner glance but not separately raised.

### MINOR-1 — §6 "Derivation by source section" tally does not reconcile with the ledger

`Chirality_Root_SOFTWARE_DECOMP_v1_0.md:187–188` states "§3 (7) … §9 (9)".
Attributing each row by the first section named in its `SourceRef` gives
**§3 (6)** and **§9 (10)**; all other sections match exactly and the total is
103 either way. The cause is `SOW-007`, whose `SourceRef` is `PRD §9.5` but
which sits positionally in the §3 block. Cosmetic, but it is a stated fact that
a recount contradicts.

### MINOR-2 — Inconsistent granularity for PRD §8.1 non-goals

The ledger carries six §8.1 items (SOW-074..079): the five packet non-goals plus
"not a roadmap". PRD §8.1's second paragraph states further document-specific
non-goals that have **no ledger row**: that the PRD adopts/accepts/ratifies
nothing including itself; that it performs none of the §9.1 follow-on
obligations; that it changes no instruction-surface file; and that it does not
re-litigate the philosophical framework (including the statement that
`docs/thesis/` stands at CITED/REVIEWED, **not** AUTHENTICATED). The forward
register aggregates all of §8.1 into a single `nongoals-8.1` row marked
`COVERED`, so the omission is invisible to the F4 check. These are non-goals
*of the document* rather than product scope, and §8.1 is not a §5 commitment,
so F4 is not affected — but the granularity is inconsistent, since "not a
roadmap" from the same paragraph *was* carried.

### MINOR-3 — Weak objective mapping: `DEL-06-07_Release_Authority_Gate` → OBJ-004

Release authority (PRD §8.3) appears in neither OBJ-4's statement nor its
success condition (F1–F3 unobserved; capabilities accepted before consumption;
G0–G4 registered and passing). OBJ-2 or OBJ-3 is the closer fit. The mapping is
defensible on a "no self-authorization" reading and the reverse trace resolves
correctly through SOW-086/087 → `release-8.3`, so nothing breaks; but it
inflates OBJ-004's apparent support.

### MINOR-4 — CSV companion registers carry no in-file package-role label

The two Markdown artifacts carry `Package Role:` in their headers; the five
CSVs declare their role only through the companion inventories (working surface
§3, telemetry §7). This satisfies the standard's package-role requirement, but
a reader who opens a CSV in isolation sees no role label.

### MINOR-5 — `DEL-03-05` anticipated artifacts name paths not in the PRD

`AnticipatedArtifacts` for `DEL-03-05` names `execution/_harness/root_guards.yaml`,
`adapter.yaml`, `surface_ownership.yaml`, `work_graph.yaml`. These come from the
run's `evidence/GUARD_STATE_SPEC.md` and the live guard validators, not from
`docs/PRD_ROOT.md`. I verified the paths are real and correct against
`tools/validation/validate_root_{materialization_fence,harness_adapter,
surface_ownership,work_graph_dispatch}.py`, and the underlying scope (SOW-001,
SOW-034) is PRD-grounded — so this is implementation detail, not invented
scope. Worth noting only because the working surface extends its "planning
note, not authorization" caveat to `AnticipatedWriteLocus` but not to
`AnticipatedArtifacts`.

### MINOR-6 — Declared-but-unused deliverable type

`GOVERNANCE_TRANCHE` is added to the Vocabulary Map and used zero times
(DEC-011 discloses this). A vocabulary entry with no referent invites later
drift; either use it or drop it at revision.

---

## 5. Falsification attempts that FAILED (i.e. the candidate held)

Listed so the empty spaces are legible as checked, not skipped.

- Attempted to find a scope item assigned to two packages, or to none → none.
- Attempted to find an IN item with no deliverable → none.
- Attempted to find a deliverable covering a scope item the ledger does not
  assign it, or vice versa → 0 mismatches in either direction over all 45.
- Attempted to find a dangling ID (ledger→DEL, ledger→OBJ, forward→SOW,
  forward→DEL, reverse→PRD item, deliverable→SOW) → 0 in all six directions.
- Attempted to find a `PKG-*`/`DEL-*` identifier absent from the working surface
  (G2 failure) → 0 of 51.
- Attempted to find an I6 coupling break or a malformed ID → 0 of 45.
- Attempted to find a non-sequential or duplicated `SOW-*` / `DEL-XX-YY` → none.
- Attempted to find a §5 commitment or objective present in the PRD but absent
  from both coverage and deferral → none; my independent enumeration (42 + 7)
  is fully covered.
- Attempted to find scope sourced from an incorporated-by-reference document →
  all 103 `SourceRef` values name PRD sections only.
- Attempted to find an acceptance, approval, or ratification claim → none; all
  seven gates `PENDING_OWNER_RULING`.
- Attempted to find a stale or wrong sha256 pin → all four MATCH.
- Attempted to find a machine-absolute path → none, sweep run independently
  because `_Decomposition` is validator-excluded (N1's disclosure verified true).
- Attempted to find a write outside scope, a created `PKG-*`/`DEL-*` directory,
  an instruction-surface touch, a commit, or a branch → none.
- Attempted to find a telemetry figure that does not reconcile → every figure in
  §3's table matches on independent recount.
- Attempted to find the partition secretly mirroring the four categories → it
  does not; six packages, every category across 4+ packages, no package
  coextensive with a category (but see BLOCKER-1 for the overstated version of
  this claim).

---

## 6. Recommendation to Agent 0

The candidate is materially sound and unusually well-instrumented; N1's open
issues (OI-001..OI-012) are honest and include the framing strains that matter.
Two items should reach the owner **before** any ruling:

1. **BLOCKER-1** — correct the "at least three categories" sentence in all three
   surfaces (working surface §8, telemetry §4, N1 return §3). Text-only; no
   register, count, or partition change is implied.
2. **MAJOR-1** — obtain an owner disposition on OBJ-2's situated-working-root
   demonstration clause: cover it or record a reasoned deferral.

MINOR-1..6 are revision-time cleanups and need not gate the ruling.
