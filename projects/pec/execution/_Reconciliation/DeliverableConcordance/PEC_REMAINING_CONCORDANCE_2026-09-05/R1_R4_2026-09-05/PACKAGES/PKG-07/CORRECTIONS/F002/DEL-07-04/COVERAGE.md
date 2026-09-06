# DEL-07-04 F002 derivative coverage

Accepted upstream: revision1.4 decomposition, D81 accepted conventions and effective D82, source base 2be412ccea62bdc4bd96deb082c46d7a792076ea. Original and F001 evidence are derivative provenance, never authority.

Summary ASSESSED_UNKNOWN: {'claims': 14, 'unknown': 6, 'aligned': 8, 'residuals': 1, 'added_claim_rows': 2, 'added_claim_cells': 46, 'changed_existing_claim_cells': 0, 'changed_existing_residual_cells': 1}. No warranted NONE.

## Source mapping before run-local IDs

Authority path `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`; locus line 372, §4 Packages, PKG-07 Scope Description; file SHA256 7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81. Exact quote: “Best-effort freshness inputs: idempotent append-only event ingest, the daemon SSE / hooks CLI / cmux bridges, durable message store, the shared-runtime client seam — implementing the PKG-00 event contracts”; UTF-8 quote SHA256 905dc113b305bd4b303a476aeed11e24bc8482cbf82e71cbaf8d7af4a9cd98a4. Then mapped run-local ID `DEL-07-04::PKG07-EVENT-CONTRACTS`.

Authority path `projects/pec/execution/_Decomposition/Deliverables.csv`; locus row DEL-07-04, AnticipatedArtifacts; file SHA256 49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72. Exact quote: “Adapter + tests”; UTF-8 quote SHA256 3fbf333b2c918276550de4e03d93d13b991292df04bd58b4c336ff9932357495. Then mapped run-local ID `DEL-07-04::ARTIFACT.TESTS`.

Package consumer implementation is distinct from documentary prerequisite state. DEL-00-02 Description identifies ingest/hooks consumers; DEL-07-04 DEP-07-04-003 says cmux implements the same contract. Existing behavior rows do not expressly assess this compatibility boundary, hence one added UNKNOWN per member. Test artifact mapping for optional cmux is finite-method expectation only; no method or VER ID is fabricated. Existing residual text already covers claim-specific verification and owner disposition; only reciprocal links expand.

Original claim cells and all gates remain unchanged. Evidence residual Depends remains NONE; new production claim dependencies reflect actual register targets. For DEL-07-03, F001 remains composed: its residual NONE and seven original production Depends are preserved. Optional cmux activation, graceful absence, PKG-00 contract ownership, root runtime, source/application/lifecycle/release gates survive.

All source pins rehashed; exact file preflights including missing ScopeOfWork.md reproduced in READ_MANIFEST. No source/product/Remaining write. CORRECTION_READY_FOR_INDEPENDENT_BACKCHECK only; fresh backcheck and manager selection remain required. Rerun on source/scope/acceptance/hold drift.

## Immutable predecessor coverage (historical population, superseded only by explicit additions above)

# DEL-07-04 coverage

Derivative evidence only. Accepted upstream: revision 1.4 decomposition (current files pinned in READ_MANIFEST), D81 accepted conventions and effective D82 at 2be412ccea62bdc4bd96deb082c46d7a792076ea. No R0 reuse. Native role instruction-asserted, not mechanically enforced; no delegation.

12 claims: 8 ALIGNED (documentary/lifecycle only), 4 UNKNOWN behavioral; 1 shared evidence/authority residual. Summary ASSESSED_UNKNOWN; warranted NONE false. No current finite-test PASS or human-acceptance claim asserted for cmux.

Missing ScopeOfWork.md confirmed by exact candidate-validation preflight and inventory. Zero locally defined REQ/AC/VER IDs found; no replacement contract invented. Mapping: ScopeLedger.csv row SOW-037 and SOFTWARE_DECOMP.md line 212: “Implement the cmux socket adapter as an optional, declared and attributable enricher” (UTF-8 quote SHA256 c9eb42ad4f30d336f0a6aaeda1fe7fbab2b3f0ad81fac58bd9f8082f2beeef56). Parent file SHA 2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25. DEL-07-04::SOW-037 covers adapter implementation, -DECLARED and -ATTRIBUTABLE split the two explicit qualifications; these suffixes are run-local atomic mappings, not source requirement IDs. DEL-07-04::SOW-037-ABSENCE maps Deliverables.csv row DEL-07-04 Description: “Optional declared enricher over the cmux socket API; absence changes nothing.” (quote SHA256 8aca37cf5ae2d06111cda1b2446a7b6fbde0e89e15e2222ecfde5dedc372506f; file SHA 49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72). DOC-OPTIONAL preserves optionality/P4.

All four local DEP-07-04-001..004 IDs are covered directly. E-A04 and E-P50 are provenance aliases for DEP-07-04-003/004, not additional product requirements. C-04 and C-10 are non-gating register-wide ordering/provenance rules, not local implementation claims. SOW-034 and DEL-07-01 appear only as prerequisite evidence and remain owned by their respective deliverables. PKG-07 is an anchor. PEC-STR-003 is source attribution for SOW-037, not an extra local contract. No objectives mapped, so none invented. All other decomposition IDs and historical decision IDs in the broad read/search corpus are explicitly unclaimed as outside SOW-037 and the owning member; hashes of searched files record boundary, not substantive endorsement. EVQ-001/003/004 and DUP/EMPTY/REPAIRED in the D65 record are historical repair classifications, not current cmux acceptance criteria. D65 closure demonstrates evidence repair only. ADR/SPEC bridge descriptions preserve interface separation, not a cmux implementation acceptance. PEC-SVC-001/002 and OI-009 in current v2 posture belong to other owners and are not reopened.

Current source inspection examines the actual JSON loop-registry adapter and core port; their behavior is configuration discovery. Exact v2 cmux/DEL-07-04 search is empty. The sole local run concerns D65 register repair and no local cmux test/REVIEW acceptance was found. This combination leaves UNKNOWN, never DOCUMENTED_UNIMPLEMENTED. Source evidence does not turn optional cmux into mandatory release work. No frozen old PEC implementation is relied upon.

Production prerequisite rows are ACTIVE PREREQUISITE PENDING for DEL-00-02 and DEL-07-01, conditional on building the adapter. Inspection proceeds without satisfying them. No edge maturity/status changes or reverse dependency invented. Runtime remains root-owned; no second loop, dispatch authority or foreign-loop duty. Broader graceful absence release gate belongs to its owner; this local absence claim is a behavioral evidence gap, not a new release obligation. No automatic administrative mirror for TBD, missing Remaining or lifecycle state.

Eight exact file hold preflights all ALLOW, including absent ScopeOfWork.md and the local run file. ALLOW grants no source/lifecycle/owner action. Earlier overbroad search matched dates and was truncated; narrowed exact search and source inspection replace it for conclusions. Manifest hashes include searched files as a conservative read superset. All output validation and source exit rehash results appear in READ_MANIFEST.json.
