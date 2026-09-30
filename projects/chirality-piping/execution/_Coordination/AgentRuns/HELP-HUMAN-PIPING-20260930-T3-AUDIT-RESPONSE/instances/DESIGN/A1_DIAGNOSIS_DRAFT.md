# A1-DIAGNOSIS — draft TASK brief, not a launch

Status: initial DESIGN proposal. No child is launched by this document and no
build is authorized by it. ROOT/DESIGN must seal the fields below after V0 and
the slot grant. No fixture outcome below is an observed runtime result.

## Identity, basis and boundary

You are TASK / Type 2, child of DESIGN / HELPS_HUMANS, ultimately reporting to
ROOT / HELP_HUMAN. Do not delegate. Derive REPO_ROOT with Git. Read Root
`AGENTS.md`, `projects/chirality-piping/AGENTS.md`, `agents/AGENT_TASK.md`, the
sealed launch brief, `Run/ACTIVATION.md`, the current response graph, DESIGN's
`INITIAL_PLAN.md`, and `.agents/skills/software-defect-diagnosis/SKILL.md`.
Record their actual origins, hashes and read ranges. Other full role bodies
are not routine context.

Aliases are those of `INITIAL_PLAN.md`. Known product/audit basis is
`3bddc2b05f6106e969c7cf43373b230845c7cc66`; initial checkpoint/brief commit is
`86bb36d6fb88e7699df595bce1d6a31f5fbd6be5`. The launch must fill and hash:

- V0 independent review path, hash and disposition;
- exact permitted product/launch SHA and source-tree equality evidence;
- TASK slot grant and write ownership;
- E0 record and ROOT's heavy-slot grant, if Rust execution is admitted;
- task-owned `<probe-root>` and `<target-root>` bindings and command limits.

Write only `Run/instances/A1-DIAGNOSIS/**` and separately granted task-owned
scratch/target paths. Product, tests, old evidence, rulings and graph are
read-only. No Git/index writes, fetch, install, network call, broad suite or
repair. A shared filesystem fence is a brief restriction, not a separate OS
sandbox. If an API requires instrumentation, propose the exact scratch-copy
change first; do not edit the active source. Diagnostic instrumentation is not
the unmutated runtime witness and must be isolated and disclosed.

## Assignment and evidence levels

Determine whether AUD-T3-01 survives V0 and the actual source/selection boundary.
Do not assume it is correct. Separately answer:

1. Is the general R7/RV19 transfer premise true under its stated hypotheses?
2. Can an unmutated, valid source selected by the full procedure realize the
   alleged scale discrepancy?
3. Can such a source publish any row outside its allowed claim, including an
   exact-zero bound when independent truth is nonzero?
4. Can a scale underestimate move a row across the relative threshold and
   threaten its 1e-9 assurance? Check this independently of the absolute bound;
   a changed class alone is not proof of wrong numerical output.

Read `T3/AUDIT/{REPORT,A1_A2_REVIEW,HANDOFF}.md`; R7 §5.1–5.3; ROOT's A1
ruling at `ROOT_RULINGS_V1.md:2016–2031` and A2 at `:2544–2575`; RV19 D.4;
and the actual `source.rs`, `adaptive.rs`, formation/recovery and public API
paths needed for the chosen fixture. Relocate line numbers on the launch SHA.
No OCR/extracted equation corpus is an authoritative physics source.

## Valid-source constructions: start tiny

All sources must go through `PrimitiveSource::new(SourceParts { ... })` and
the normal retained solve/selection path, with all mutations/seeds disabled.
Use exact binary64 bit patterns; preserve canonical source/load encodings.
Keep units explicit: coordinates in m, E/G in Pa, A in m², I/J in m⁴,
force in N, moment in N·m, translation in m, rotation in rad.

Proposed first fixture: one straight member on the x-axis, nodes (0,0,0) and
(L,0,0), y_reference (0,1,0); root fully restrained, tip restrained except Rx.
Take G=1, J=4L, and E=A=Iy=Iz=1 in their respective units. Apply tip Mx=5h,
h=2^-1074. Independently, torsional free stiffness is GJ/L=4 and exact
rotation is 5h/4. Choose L=2^100 first; all listed inputs are finite and each
derived primitive is normal and positive. The candidate rotation should be
publishable as h if the ordinary solver selects it; input-derived rotations
must not supply its raw scale. Check that no other free rotation or translation
row changes the maxima. This targets the scale premise, not a promised bad
row: the exact solution may be fully honest despite the scale gap.

Mirror construction: tip restrained except Ux, E=1, A=4L, G=Iy=Iz=J=1,
tip Fx=5h, L=2^-100. Axial stiffness EA/L=4 gives exact translation 5h/4;
rotation scale then exercises division by L. Preserve positive normal A.
These are mathematical kernel-source probes, not realistic piping designs or
claims of present product capture. Verify every construction against the
actual source and geometry validation; do not treat this draft as validation.

Boundary variants, within a frozen matrix of at most 24 cases:

- L=1 as an unamplified control; L=2^85 and 2^86 for the multiplication
  threshold neighborhood, and reciprocal L values for division;
- L=2^-100 for the torsional driver and L=2^100 for the axial driver to
  exercise a zero published coupled scale with positive retained scale;
- replace 5h by 4h for an exactly representable raw output control, and a
  normal-output case with otherwise identical structure;
- subnormal nonzero publication, tie/underflow exclusion, dominating raw
  same-kind row, and L=0 single-node omission controls as needed.

For a source-level classification control, the torsion fixture can also free
tip Ux and set A=4L with E=1, giving independent axial stiffness 4. Set its
axial force to 4q with q immediately below, equal to, and immediately above
2^-1008. The free block is diagonal, its exact truth is known, and the raw
translation remains below the rotation-coupled scale. This may demonstrate
classification sensitivity while every row remains honest. Keep these cases
inside the 24-case limit. Separately reproduce the abstract relative example
in INITIAL_PLAN with independent rational arithmetic; label it synthetic
states, never an unmutated-source result.

Freeze exact case choices before execution. Do not force a success: a source,
gate, receipt or budget refusal is recorded with its first cause. A raw
nonzero that rounds to zero is unpublishable; it is not a published-zero
witness. A candidate exact zero with nonzero truth is a different case.

If the first matrix leaves the harmful consequence open, return a proposed
one-to-three-member, at-most-two-free-DOF cancellation extension. Explain the
mechanism that could consume the retained error allowance before running it.
Use a public source and independent exact stiffness/load equations. Do not
substitute candidate/verification vectors or a seeded fault as a realized
case. No random or large-model search is part of this brief.

## Oracle and acceptance checks

Use an independent integer/Fraction oracle from the explicit model equations,
not K4 GEN, its expected-value files, production Wide arithmetic, production
scale helpers or the audit's arithmetic function. The one-DOF fixtures need
only exact scalar division; a later tiny rational block can use exact
elimination. Verify geometry is exactly axis aligned and all relevant
lengths/coefficients are rational before invoking a rational oracle. For
non-rational geometry, stop for an independently bounded oracle plan.

Implement binary64 nearest-even and directed rounding from integer significand
and exponent logic, checking ties and range boundaries. Decode actual output
bits to exact rationals for comparison. Preserve nonzero truth below h/2;
never turn it into a binary64 zero expectation. As a cross-check, compare the
oracle's ordinary finite conversions with the host's conversion where valid.

For every executed case retain:

- all primitive/load bits, constraints, dimensions, source validation, source
  hash/encoding, candidate SHA and command/environment;
- selected p/P or named refusal, all gate reasons and reported work;
- row IDs, input-derived/unpublishable classification, value and bound bits,
  reported body scales and floor evidence;
- exact truth and oracle derivation, exact expected raw/coupled scale values,
  and which scale maximum branch dominates;
- the difference between a reconstructed mathematical S_v and an actually
  observed internal S_v. Do not present one as the other.

For `absolute_verified`, test the published claim with the accepted factor
1+2^-22 at p=128/256 and 1+2^-21 at p=512, using exact rational comparisons.
For b=0 require equality with exact truth. If uncertainty intervals are used,
prove they separate the truth from the claim before declaring failure.
For other classes, use their authoritative claim or refusal contract and name
the source; never invent a tolerance. Independently reconstruct publication
scale and class using the specified operation order. Include signed copies or
one symmetry check only when it adds discriminating evidence.

Specifically for relative rows, preserve R=2^-34 and the 1e-9 criterion from
D1's floor/propagation argument. Record exact |q_pub-q*|/|q_pub| and, where
defined, |q_pub-q*|/|q*| so denominator conventions remain visible; use the
authoritative criterion for the disposition. Do not replace this with a
body-scale-relative comparison, which could mask the issue. Trace coupled
translation/rotation, force/moment and covered derived-stress consequences
separately; p=512 floors may change applicability. A closure proof must cover
the class threshold and guarantee, not only an amended absolute b.

A realized false claim is BLOCKING: stop the affected path and return the
smallest complete source/reproducer immediately. A selected scale gap without
false claims confirms reachability of the premise issue only. An exclusion
claim must name and prove the enforced invariant and its full domain; no
finite passing matrix proves universal exclusion. Record failed attempts that
materially eliminate competing explanations.

## Host limits and return

This is the M3 Air with 16 GB, not the former M5 Max with 128 GB. Before a Rust
run, ROOT must grant the single global heavy slot after E0 verifies guard
coverage, target ownership and current headroom. Use the pinned toolchain and
offline/locked dependency settings, cargo -j 1 and RUST_TEST_THREADS=1. No
installation or assumption of an old target/venv is allowed. Preserve at least
35% available-memory reserve and the admitted cap (initial observation cap at
most 2 GiB unless separately derived); stop owned processes on guard/pressure
events. No dense/large model, performance claim or full gate is requested.

Return `RETURN.md`, exact case/oracle/probe files, raw outputs, `CONTEXT.json`
and `SHA256SUMS` in the child folder. Name actual parentage, native launch
mechanism, supplied basis, source hashes, actual permissions, environment,
commands, evidence level, causal alternatives, potential affected consumers
and limits. State no-repair/no-Git status truthfully. Return to DESIGN through
native collaboration, which forwards the integrated checkpoint to ROOT.
