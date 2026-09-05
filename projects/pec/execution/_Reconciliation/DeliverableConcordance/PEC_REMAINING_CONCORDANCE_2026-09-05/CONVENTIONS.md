# PEC Remaining calibration conventions — candidate

**Status: CANDIDATE / OWNER_CALIBRATION_NOT_ACCEPTED.** This is a derivative
proposal under D-PEC-81 O-A, bound to
`faf22452528b5ba895e88ba0ad3770855100de08`. The pinned D-PEC-81 adoption packet
and shared method govern; this file neither selects work nor extends authority.
Independent findings and manager adjudication must be read with these proposals.

## Proposed common conventions

1. **Complete atomic coverage.** Preserve each current local stable claim ID as
   `<DeliverableID>::<LocalID>`, including defined REQ/AC/VER IDs and additional
   material contract claims. A missing contract uses explicit decomposition
   source mappings with path/locus/quote-hash before run-local IDs. The missing
   contract and evidence boundary stay visible; do not invent a SOW or use a
   source-search miss as proof of absent implementation. Contradictory or missing
   scope routes to the owner, not an invented production task.
2. **Claim classes qualify ALIGNED.** Documentary alignment, observed behavior,
   finite test coverage, human acceptance, lifecycle and release are different
   assertions. A finite fixture method can remain ALIGNED while a broader
   requirement has a supported counterexample; do not attach that method row to
   the broader repair as though its executed fixture set had failed. A documentary ALIGNED row cannot be rolled up as implemented.
   Behavioral ALIGNED needs implementation plus current claim-relevant checks.
   Method/test rows name the exact method and its limits. A passing finite suite
   may coexist with a reproducible counterexample to a broader requirement.
3. **Bind acceptance continuity.** Preserve exact accepted bytes and historical
   acts. Compare source and claim semantics before relying on an earlier
   acceptance for a later artifact. A later exclusion of a new acceptance act
   is not itself reversal; neither is it evidence that old acceptance covers a
   changed claim. Use UNKNOWN/STALE_INPUT if continuity cannot be established.
4. **Separate findings from lawful execution.** All sample residuals are
   NON_SELECTABLE_PENDING_OWNER_APPLICATION. A finding in CHECKING is not a
   reversal or authorization to edit the candidate. Scope/source/contract/lifecycle
   and Remaining changes each use their owning exact ruling. Preserve acceptance
   history even when a new current weakness is proven. D81 authorizes no repair.
5. **Make residual routing explicit.** Candidate reports distinguish accepted
   product obligation, evidence gap, ambiguity/authority question, and
   administrative or lifecycle concern. Retain each finding and its provenance,
   but do not automatically mirror every TM row, unassigned owner, future release
   method or deferred product question into executable Remaining. Such a mirror
   requires an actual deliverable obligation, exact owner trigger and ruled scope.
   A truthful unassigned/TBD field is documentary ALIGNED when that is the claim;
   missing accountable assignment is a separate administrative concern, not
   unimplemented product scope. Unknowns remain in evidence rather than being silently dropped or called NONE.
6. **Exact dependency semantics.** Depends names only source-grounded target IDs.
   Apply LOOP_INIT's ACTIVE PREREQUISITE + TBD/PENDING/IN_PROGRESS + named target
   conjunction. Ordering edges do not block. Accepted predecessor artifacts do
   not silently flip dependency register values. Conversely, unrelated open
   questions and TM-PEC-023 create no blanket downstream gate. Owner acceptance
   is observable on shared main; ordinary predecessor commit/checks/run record
   can be observable on the run branch without transferring human authority.
7. **Preserve dated truth.** Retired plans never select. Current revision 1.4
   scope and later accepted August9 currency take precedence as evidence over
   older pointer prose for their specific claims, without rewriting history.
   Frozen future-production wording may be deliberate framing; qualify its
   meaning before proposing a stale-text repair. A live source file's existence
   does not imply source acceptance or another deliverable's completion.
8. **Warranted NONE is strict.** Missing Remaining, no search hit, CHECKING,
   exact artifact acceptance or documentary ALIGNED alone cannot prove it.
   Every accepted claim/evidence/gate condition must be assessed. Any unresolved
   UNKNOWN prevents NONE. Report ASSESSED_UNKNOWN where uncertainty exists,
   even when known residual proposals are also present; separately count both.
9. **Portable source-bound records.** Use repository-relative source locators,
   exact commit/SHA-256 and local ID/section. Normalize future READ_MANIFEST to
   `{source_commit, hashes:{path:sha256}, historical_sources:[{path,commit,sha256}],
   checks:[{command,cwd,environment,exit_code,result}], source_unchanged}`. Retain
   original sample manifests unchanged; their equivalent shapes are normalized
   only for manager verification. CSV files use LF. Paths are resolved from
   `git rev-parse --show-toplevel`, not a nearest AGENTS overlay.
10. **Hold preflight targets are exact.** Pass project-relative file targets
    matching the register's TargetPath shape for each actual act. Directory or
    repository-prefixed target strings are not a reusable substitute. Empty
    current hold register does not grant production or waive other owner gates.
    Tests/probes keep bytecode/build caches in scratch; frozen/ignored state
    remains unchanged. Negative probe fixture text is never executed as product.

## Validation contract for a later, separately ruled scale-out

Every wave preserves the D81 schema and controlled dispositions. Check complete
claim and deliverable coverage, source-hash equality, source/citation existence,
unique IDs, residual/claim reciprocity, exact gate/Depends meaning and reproduced
summaries. Fresh independent verification covers all non-aligned/self-flagged
claims and residual proposals plus deterministic aligned samples and relevant
acceptance/guarantee boundaries. Preserve original findings before correction;
defective rows rerun through a fresh worker in new derivative evidence.

No package wave starts under this candidate file. Owner calibration acceptance
and an explicit R1–R4 scale-out ruling remain required. Later repair still needs
an exact application manifest and post-repair multiset backcheck; this R0 is not
that backcheck and certifies no project-wide Remaining census.
