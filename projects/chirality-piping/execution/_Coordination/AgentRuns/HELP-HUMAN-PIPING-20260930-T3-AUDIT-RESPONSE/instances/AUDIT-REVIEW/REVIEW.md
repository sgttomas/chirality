# AUDIT-REVIEW — V0 independent post-merge review

**Verdict: suitable for ROOT fan-in, with one non-blocking reproducibility NOTE.**
The frozen audit packet has no blocking or SHOULD-FIX review finding. Its
principal proof finding is confirmed within its expressly stated limits.
This verdict does not close A1, certify the solver, accept a changed design,
authorize F2a reliance, or retroactively establish pre-merge independent review.

Reviewed diff: `74b3c7313491f27f71c4361d5e1657ee4a39e2f1` to
`7fd632f60ee0d4eeb0429ff4dbd2193eaeeb5d6d`, merged as
`3bddc2b05f6106e969c7cf43373b230845c7cc66` in PR #1064. All 15 changed
paths are additive files under `T3/AUDIT/`, and their current bytes match the
frozen head. Source line numbers below use the audit base. The response-plan
review uses activation commit `86bb36d6fb88e7699df595bce1d6a31f5fbd6be5`.

Aliases: `P = projects/chirality-piping`; `T3 = P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3`;
`FK = P/core/solver/frame_kernel`; `H = P/core/solver/performance_harness`;
`VR = P/validation/benchmarks/numerical_robustness`.
`Run = P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`.
This report and its scripts/results live in `Run/instances/AUDIT-REVIEW/`.

## Audit finding dispositions

| Finding | Disposition | Independent conclusion |
|---|---|---|
| AUD-T3-01, SHOULD-FIX | **CONFIRMED as a proof defect; QUALIFIED as to reachability** | The claimed universal transfer from retained verification scale to rounded publication scale is false. The exact 20% loss and abstract error/bound ratio 9/8 reproduce. Neither the audit nor this review demonstrates an unmutated source model producing a wrong publication. Retain SHOULD-FIX and the closure requirement before F2a relies on this guarantee; a realized false publication meets the existing BLOCKING criterion. |
| AUD-T3-02, NOTE | **CONFIRMED** | All five parent-directory manifest bases independently resolve. All 90 historical manifests and all 9,088 entries verify. The handoff's one-exception instruction is incomplete; no observed hash mismatch. |
| AUD-T3-03, NOTE | **CONFIRMED, as disclosure evidence** | S11K, K2B and K6 disclose index write/reset pairs; K6B discloses a fetch; S11K's separate fast-forward is explicitly authorized by its fix brief. This proves the blanket no-write account is unsupported; it is not a complete command-history reconstruction. |
| AUD-T3-04, NOTE | **CONFIRMED, scoped to the named evidence paths** | The six merge folders lack `dec025/suites/*.log`; KF2's merge record identifies scratch-only large gate JSONL; K4's generator imports pinned dated-tree inputs excluded by numerical CI's sparse checkout. These are reproducibility limits, not evidence of failed historical gates. Original-host recovery remains separate. |

No audit finding is refuted. A2's conditional source/proof conclusion also
survives this review; its limits are detailed below.

## Review finding against the audit packet

**AUD-REV-N1 — NOTE, non-blocking: replay output can retain an incorrect basis label.**

- Location: `T3/AUDIT/_run_records/audit_checks.py:27`, `:203-209`,
  and `T3/AUDIT/_run_records/README.md:3-7`.
- Trigger: a later user follows the replay commands in a checkout where a
  runner, counts file or other input has changed. `BASE` is a constant, but
  `admissions()` imports the current working-tree runner and reads current
  counts. Other modes likewise read working-tree records. No precondition
  verifies those bytes against the declared base before returning its label.
- Consequence: a later replay can be attributed to the historical audit basis
  despite using another input set. This does **not** invalidate the preserved
  historical outputs: this review verified the packet against its frozen
  head, all 61 principal basis hashes against both current bytes and the
  audit-base Git objects, and independently reproduced the decision figures.
- Remedy: add a new replay erratum or a separately versioned checked wrapper
  that materializes or validates the precise input snapshot and pins the audit
  script from its own head before executing it. Record actual input identities
  and reject drift, or label it as a new analysis. Preserve the original
  hash-bound audit files unchanged. Merely printing `BASE` is insufficient;
  the script itself did not exist at that base, so identify both revisions.

## A1: independent derivation and attempted exclusions

`independent_math.py` imports neither the audit probe, the generator, the
solver nor a runner. It implements binary64 rounding with integer arithmetic
over exact fractions and checks the resulting binary64 values against Python.
`math_results.json` retains its results.

Let `h = 2^-1074`, `r = 5h/4`, and `L = 2^100`. Retained candidate and
verification rotation are both r. Publication rounds r to h. Thus
`S_v = Lr = 5·2^-976` and `S_pub = Lh = 2^-974`: the loss is exactly 1/5
of S_v. This exceeds `(2^-64 + 2^-52)S_v + h/2`. All coupling products are
exact power-of-two operations; the lost information is in the operand.

For the audit's abstract target translation, candidate zero and stipulated
truth/verification `q* = (9/8)·2^-1038` give disagreement below
`2^-64 S_v`, while `b = 2^-64 S_pub = 2^-1038` and `q*/b = 9/8`.
This is an absolute row: `S_pub >= 2^-988` and zero is below its positive
classification threshold. The small-scale A1 term is not taken. The nonzero
verification translation is smaller than the coupled scale and does not
change the raw maxima used in this computation.

The audit's wording is appropriately limited: it demonstrates a failed
inference from the stated scale/disagreement premises, not every requirement
for an accepted solve. In particular, **zero W_plus is stipulated**. Source
derived t1/t3, residuals, loads, positive-definiteness, theta/g checks, all
force/moment rows and their charge/estimate conditions, candidate/refinement
behavior, and receipt encodability have not been jointly realized.
Even an exact verification truth does not mean the implementation's W_plus
bound is zero. No valid-source experiment was performed by this reviewer.

Specific exclusions checked:

- **Input range and retained representation:** `source.rs:379` checks finite
  coordinates; it does not impose the product capture's 2^53 numeric boundary.
  `body_extent` (`adaptive.rs:276`) exactly produces 2^100 or 2^-100 from
  coordinates `(0,0,0)` and `(L,0,0)`. Neither square overflows/underflows.
  The few-significant-bit dyadics fit every retained precision and the
  exponent range (`wide.rs:134`). This is necessary representability evidence,
  not a complete source model. Product-capture restrictions can exclude the
  large-coordinate construction; they do not establish a kernel-wide exclusion.
- **Dimensions and body identity:** rotation-to-translation multiplies by L;
  translation-to-rotation divides by L. All maxima must belong to one body
  and include the required layout. Reversing the construction with raw
  translation r and `L = 2^-100` yields the same 20% rotation-scale loss,
  without large coordinates. This is another algebraic case, not a product
  witness; downstream geometry/source constraints still need examination.
- **Publication filtering:** r rounds to a nonzero subnormal h and is
  publishable; it is not removed by the O9 skip in `adaptive.rs:2055`.
  Candidate zero is also publishable. Non-input-derived rows were assumed,
  as both scale builders require (`:1917`, `:2606`). Prescribed-only rows
  would not suffice for the raw-scale construction.
- **Magnitude rows:** `recover.rs:114` adds node displacement magnitudes.
  With one nonzero component the magnitude is the absolute component.
  The extra `2^(1-P)|q_2p|` charge at `adaptive.rs:2122` still fits the
  abstract margin for P = 256, 512 and 1024, independently checked. This
  removes that particular proposed exclusion; it does not demonstrate a
  realizable full layout or zero source-derived magnitude W_plus.
- **A1 boundary:** L exponents 85, 86, 87 and 100 were checked. At L = 2^86
  the published scale reaches 2^-988 and the small branch stops. Even just
  below it, one unamplified h is not a universal replacement for the missing
  transfer: at L = 2^85, `2^-64(S_v-S_pub) = 2^19 h`.
- **Zero scales:** at `L = 2^-100`, raw rotation r yields positive retained
  translation scale but zero published coupled translation scale. The source
  `row_bound(0,0)` is zero (`adaptive.rs:382`). Actual nonzero candidate
  translations may instead be unpublishable, and source constraints can make
  zero translations input-derived. The algebra alone proves neither a false
  zero-bound publication nor its exclusion.

R7 §5.2 (`D1_REV_5A3_SSTAR_RESOLUTION_R7.md:342`), the A1 ruling
(`ROOT_RULINGS_V1.md:2016-2025`) and RV19's extended argument
(`REVIEW/K4_REVIEW.md:456`) do not charge this pre-coupling subnormal error
with L or 1/L. The local direct-row rounding allowance is not the defect.
The unclosed obligation is a valid complete transfer bound or a proven
realized-input exclusion. Failure to find a wrong solve is insufficient closure.

## A2 and other source observations

Under R7's existing certification premises, each available candidate is at
least the same block inverse norm, so a nonempty minimum remains an upper
bound. Refusing to form a candidate cannot make a surviving certificate
smaller. The code and theorem use that property, not a particular producer.

Independently inspected `bound.rs` refusal mapping (`295-321`), per-block
passes (`365-563`), refused `uc: None` state and formation (`601-710`), shift
scheduling/propagation (`1011-1147`, `1187-1270`), minimum (`1149`) and
certificate/missing-bound construction (`1274`). Non-Span/Exponent stops
propagate; partial refused recurrence values do not become a certificate;
the existing block-diagonal premise isolates other blocks.

`verify.rs:1021` returns missing-bound refusal before proceeding;
`:1052-1160` forms theta, body maxima and t1/t3/W_plus using certified B.
Without a refusal, `adaptive.rs:2188` rejects a data-carrying block with no
bound. R7 §5's Lemmas A/C, theorem and corollary need the upper-bound property;
D/E establish the individual candidates under their premises. Data-free
blocks remain subject to their existing exact-zero premises. This does not
re-prove every numerical lemma or certify every error/cache path by execution.

The factor diff from `cef218a10` contains observers/accessors, visibility,
documentation and the gated geometry fault; no change to the factor's
arithmetic loop was found. Feature and estimate consumer inspections are
consistent with the audit's limited source claims. K6c remains necessary;
A2's acceptance argument is not a memory-bound argument. Existing RV23C-N1
remains a disclosed regression-test gap, not a newly reproduced cache defect.

## Evidence, identities and reproducibility

`check_records.py` independently checked all added packet bytes, its 14-entry
manifest, the 61 basis inputs and all historical manifest hashes. It resolves
manifest bases by actual referenced-file existence, rather than copying the
audit's exception list. The five exceptions match AUD-T3-02 exactly.

Local Git checks confirm all six candidates are the named merge's second
parent, all dispatch bases are ancestors of those candidates, and the
Piping/tools/.github trees match candidate versus merge. Only KF3's dispatch
base differs from the merge first parent, as disclosed. The stored 30 CI
records and six full-selection plans match those heads and successful
conclusions; all twelve numerical-job durations recompute. Final-head review
or confirmation passages exist for K4, KF1, VK, K6B, KF3 and KF2. These are
historical review records, not a new execution of their checks.

Live read-only samples independently confirm PR #1064's head/merge and PR
#1059's head/merge/time, plus KF3 dispatch 36669370536's success at its recorded
head. #1064's GitHub `reviews` list is empty; that is not itself proof that no
review happened elsewhere. The activation expressly identifies this as the
post-merge review. No claim of retroactive pre-merge coverage is made.

`check_admissions_figures.py` imports neither the audit nor either runner.
It independently implements the exercised W1 admission branch with asserted
preconditions, recomputes the historical calibration and recalibrates it for
the sensitivity estimates. **All fields of all 36 original dictionaries and
all 36 sensitivity dictionaries match; zero decisions change.** It also
reproduces the source-record B1 coefficients, twelve 10,000-member records,
six suite deltas, both 10,799,688-byte shift omissions, and the margins
6,970,722 B and 7,511,329 B. Numerical minutes use decimal half-up rounding
for the cited tie cases; no discrepancy was found.

The sensitivity reuses historical measurements, assumes the original
approval/ascent context, and changes only estimates/calibration. It neither
proves E_max nor admits an M3 run. The audit correctly retains K6c's complete
phase derivation, refusal-slot/transient accounting and final replay.

AUD-T3-03 disclosures were checked at the exact named return lines and the
S11K fix brief's line 12. The three index pairs, fetch and authorized
fast-forward must remain distinct. Nil net effect is a reported historical
fact; the records cannot establish unseen command history.

AUD-T3-04's missing per-suite logs prevent independent recovery of exact
failure names from those summaries alone. KF2's scratch-only gate JSONL
reference is at `IMPLEMENTATION/KF2_MERGE/RECORD.md:78`. The K4 generator
dependency is at `FK/tests/retained_k4/gen_k4_vectors.py:119-143`; numerical
sparse checkout excludes that execution tree at
`.github/workflows/piping-desktop-e2e.yml:183-190`. A full checkout does carry
those generator inputs; a sparse numerical checkout does not. Neither state
recreates absent old raw gate files. GEN-8's transcribed output is explicitly
identified as a transcription, not an original log. This reviewer did not
rerun GEN-8, DEC-025, Rust, mutation suites, models or performance tests.

## Response plan and launch assessment

**No blocking problem found in the activated first-wave launch.** The sealed
V0 brief, activation, graph and manager briefs give disjoint record ownership,
ROOT-only Git/shared writes, a fresh independent review assignment, two initial
TASK slots, and no heavy authorization until E0 establishes the host boundary.
The M3 Air/16-GB correction is explicit; M5 timings and caps do not migrate by
assumption. The guard proposal is initially documentary and cannot kill jobs.
The preserved 35% reserve and proposed caps are operating precautions, not a
proved engineering bound. Current monitoring/headroom is required before a
later heavy-slot grant. No grant is inferred from this review.

The frozen graph's pre-launch status is historical; ROOT must record actual
dispatch IDs/returns and complete B0's focused dependency assessment. That
does not block this read-only review and is not a readiness verdict. The
planning packet still requires independent review of its final mergeable
revision under its own gate; this launch assessment is narrower. Reviewers
must remain separate from authors/implementers as specified.

## Execution and return record

Native delegation: `collaboration.spawn_agent` descendant `/root/audit_reviewer`
under `/root`; this TASK spawned no child. The sealed brief's SHA256 is
`2f08ff9a32fcbc8593378ced41dd8b00be579e58d02160067248c555f34b3f7c`.
The reviewer did not author the audit. The actual model was inherited; the
host exposes no independently verified model identifier here, and no model
diversity claim is made. Full role context loaded: TASK only. Selected skill:
`.agents/skills/software-code-review/SKILL.md`. No reusable workflow selected.

`CONTEXT.json` preserves instruction, brief, planning and checked-source
origins/hashes plus consultation ranges. `COMMANDS.md` gives the performed
checks, outcomes, network limitation and reproducible commands. All owned
writes are confined to this review directory. Shared repository state changed
concurrently under ROOT/other owners and was not staged, reverted or repaired.
The write fence is a prompt restriction in a shared sandbox, not a separate
OS-enforced per-agent capability. No Git/index write, build, installation,
model run, heavy slot, or old-ruling/audit mutation occurred.

Return to ROOT: integrate these dispositions and add a replay erratum/wrapper
for AUD-REV-N1; retain A1 diagnosis/design and K6c obligations. The present
checkpoint is complete, with realized-source A1 reachability and original raw
evidence recovery explicitly outstanding.
