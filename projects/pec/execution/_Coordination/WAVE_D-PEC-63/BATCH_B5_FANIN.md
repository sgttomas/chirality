# BATCH B5 FAN-IN — D-PEC-63 SOW initialization wave (internal fan-in)

**Date:** 2026-07-25 · **Decision:** D-PEC-63 · **Cadence:** internal
fan-in (owner cleared B3–B8; no halt re-armed) · **Verdict:** **B5
ACCEPTED**

## 1. Members and final state (all INITIALIZED)

| Deliverable | Final sha256 | item_count |
|---|---|---|
| DEL-03-02 | `d1335c01c54686427d6a04658a43ce9e5c4abe2e446e0acf4d1e87df3a7785b5` | 15 |
| DEL-03-03 | `83366eee4d11a26ca65e9c81d4baa29fe88c099998b37021821ec1eb4a1fbf70` | 15 |
| DEL-03-04 | `e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02` | 17 |
| DEL-04-01 | `dc667f992c25ed037b195400167319d120a1e5e0118ce777a29f5a64186d0feb` | 16 |
| DEL-10-02 | `99730e4e85ce4920d676d9fd62d26c193d5fd714ea0592c15462f37a62011a82` | 13 |
| DEL-10-10 | `a174099336f5fe62df27648514afa3121abcede57932dd17894a336696246377` | 16 |

Authoring: 6 sealed `TASK + scope-of-work MODE=INIT` (opus-5), 5/6
first-pass `PASS format=SOW_V1` (DEL-04-01 had one transient validator
FAIL — an own-voice reference to an upstream CLM ID, fixed by qualified
attribution per the B2 convention; no content change). Three C-08
standing nodes (DEL-03-04, DEL-10-02, DEL-10-10); DEL-04-01 carries the
wave's first DECLARED-stratum edge E-A27 (bound distinctly from the
PROPOSAL flags-as-flags framing — refuter-verified correct). Status
act: 6/6 via `write_status.sh` only
(`_run_records/TASK_RUN_2026-07-25_status_B5.md`).

## 2. Standing-node directing sentence (durable carrier)

The DEL-03-04, DEL-10-02, and DEL-10-10 briefs directed the accepted
DEL-01-05/DEL-10-03 standing pattern and promised this record as the
durable carrier of the directing sentence, quoted verbatim:

> Author this contract as a STANDING assertion — a continuously
> re-runnable verification, not a one-shot artifact.

All three contracts cite this record for that sentence (forward-looking
form per refutation F2, now discharged by this file's existence). Each
carries C-08's arithmetic exclusion as settled, the release-gating
force as an open CON with an owner-routed AC and a HUMAN_REVIEW matrix
row. DEL-10-02's CON is deliberately narrower (the operative binding
question only) because SOW-055/PEC-SVC-004 state release-gate character
as accepted source truth — refuter-verified a strict specialization
that does not foreclose the owner's answer.

## 3. Refutation (B5 round) and remediation

Sealed refuter (opus-5): **0 CRIT, 3 MAJ, 7 MIN**; verdict "no finding
challenges batch acceptance". All six warrant claims passed both
SCA-002 tests; all edge citations byte-exact against the gate exhibit;
E-A27 DECLARED handling verified; all AnticipatedArtifacts bounds and
Dependencies.csv counts verified; cross-contract consistency
(examined-SHA surface, DriftFinding two-producer surface, gate-wiring
split vs DEL-10-03) verified clean.

- **F1 MAJ (DEL-03-04):** "exactly one elision" trailer claim false —
  CON-004 quoted SOW-093 with a spurious ellipsis → fixed by quoting the
  contiguous ledger span.
- **F2 MAJ (DEL-10-02, DEL-10-10):** both asserted this fan-in record
  as existing in present tense → aligned to DEL-03-04's forward-looking
  form.
- **F3 MAJ (DEL-03-03):** warrant inflated a measured register
  precedent into "ruled" → restated at measured strength, mirroring
  DEL-03-02.
- **F4–F10 MIN:** section misattribution, C10 Source-cell
  identity-vs-inclusion, trailer accounting, truncated quote without
  carve-out, mid-sentence clause quote, half-recorded gate-wiring
  residue (extended as a positively-stated observation), one omitted
  own-voice deliverable in a completeness claim — all applied.
- **F6b reversal (notable):** the refuter's proposed fix (add a
  trailing ellipsis to DEL-10-10's DL-11 quote) was itself wrong — the
  source cell terminates there. The revision agent correctly BLOCKED
  rather than improvised; dispatcher verified against
  SOFTWARE_DECOMP.md line 629 and ruled the true repair via a versioned
  brief amendment (drop the phantom trailer item, "Exactly six"→"Exactly
  five", correct the CLM-017 lead-in). Both the refuter's proposal error
  and the agent's refusal are part of this record.

Revision: one sealed dispatch (5 contracts, DEL-03-02 finding-free and
untouched) + one versioned brief amendment (v2, DEL-10-10 only); all
ten findings resolved, nothing improvised, item_counts and record
counts unchanged, frontmatter byte-identical. Independent re-validation
6/6 PASS; hashes recomputed at fan-in (table above); register
cross-check 6/6 token-exact.

## 4. Dispositions at this fan-in

1. **Dispatcher brief errors (register attribution):** the B5 briefs
   mis-assigned SOW-006 to DEL-04-02 (truth: SOW-005→DEL-04-02;
   SOW-006, SOW-007→DEL-04-03; latency budget SOW-041→DEL-08-04).
   DEL-03-02 (CLM-012) and DEL-04-01 both corrected against the ledger
   rather than propagating; refuter confirmed no contract carries the
   error. Same class as B3's "exactly 12 files" slip: dispatcher error,
   not a fence event.
2. **DEL-03-04 "(C10)" resolution accepted:** the brief said carry the
   ambiguity; the agent resolved it mechanically (C10 hard constraint,
   not register row C-10) on a chain the refuter verified link-by-link
   (Source cell locus, shared "Permanent", accepted DEL-10-01
   precedent). Ruled: register-truth override of a brief's
   carry-ambiguity instruction is acceptable exactly when the chain is
   airtight — as here. F5's precision restatement applied.
3. **DEL-03-02 CON-001 (examined-SHA baseline ownership):** the
   register edge presupposes a baseline no accepted source obliges
   anyone to hold; package-level ownership (DEL-04-02/DEL-03-03 may
   need the same value) is a scope-change question. Carried as a
   wave-level observation for a later packet; reaches the owner at
   REVIEW, not as a wave blocker.
4. **Unclaimed gate-wiring residue (F9):** no accepted contract owns
   binding DEL-10-03's negative-surface suite into a release gate
   (DEL-10-02's wiring covers only its own harness). Recorded in
   DEL-10-02 CLM-012 as an observation; remediation candidate for a
   later packet.
5. **Blocker-report invocation note:** `report_blocker_state.py`
   requires `execution_root` positional + `--output`; a bare stdout
   redirect produces a headline-only file. Dispatcher re-ran correctly;
   snapshot below is the full report. (Tooling note only; script
   behavior correct.)

## 5. Verification numbers

Census `25 INITIALIZED / 39 OPEN` — calibrated ladder match (B5 = 25).
Blocker snapshot (`BLOCKER_STATE_2026-07-25_B5.md`): 29 BLOCKED / 35
UNBLOCKED (B4: 33/31; +4). Invariants held (64 registers, 255 rows =
135 ANCHOR + 120 EXECUTION, standing-excluded 1). All 25 INITIALIZED
wave members UNBLOCKED. Newly unblocked: DEL-03-06, DEL-04-02,
DEL-04-03 (three of four B6 members; DEL-10-11 already UNBLOCKED early
via the named standing-edge exclusion, sequenced B6) plus out-of-wave
DEL-04-04 (deferred to later packets by design).

## 6. Next

B6 = DEL-03-06, DEL-04-02, DEL-04-03, DEL-10-11 (four; DEL-03-06 was
in the SCA-002 owner-attribution set — warrant handling per B1
precedent). Then B7 (DEL-04-05, DEL-08-03), B8 (DEL-08-04). Owner
returns at wave closure unless a halt re-arms.
