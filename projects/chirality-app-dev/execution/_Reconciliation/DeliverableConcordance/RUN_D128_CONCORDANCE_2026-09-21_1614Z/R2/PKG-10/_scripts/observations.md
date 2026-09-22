## 8. Cross-package observations for R3 (hand-written by the PKG-10 manager; evidence, not rulings)

1. **The domain-engine surface is live only as inert types (R4-Q1 cluster, 22 rows).** The contract modules
   `packages/contracts/src/harness/domain-profile.ts` and `operation-proposal.ts` are LIVE in the module map, but no
   non-test product code consumes them. The registry, the domain read/propose tools, the headless preview runner and
   the PEC bridge client (`frontend/src/lib/harness/mcp/**`) are LEGACY_ONLY. SoW text in DEL-10-01, 10-04 and 10-05
   calls the D-APP-49..52 staged surface "live". This is the same legacy-harness question as PKG-04/06/08 (R0 §8
   item 1), and it should be clustered with them under R4-Q1. Note: DEL-10-01..04 were sealed before Addendum 6, so R3
   re-derives R4-Q1 on them from the REACH tags. DEL-10-05 applied the subject test (`ALSO_MODULE:` in Notes).
2. **K-DOMAIN-2 protected-path enforcement has no live enforcement surface.** App CONTRACT K-DOMAIN-2 names path
   hooks, and `reliance_boundary_register.md` RB-HOOKS points to the legacy hooks. D-GOV-43 bars Chirality from
   pinning Codex approval and sandbox policy. On the live path nothing guards a profile's `protected_write_paths`,
   including the adopted pec profile's `projects/pec/v2/**`. The ledgers disagree on how to classify this:
   AUTHORITY_CONFLICT with R4-Q1 (DEL-10-02#CLM-010.9, #CLM-024), PARTIALLY_IMPLEMENTED (DEL-10-03#CLM-003.2), and
   ACCEPTED_DIVERGENCE under D-APP-37 for sibling rows. Verifiers marked all three CONTESTED. This belongs with the
   PKG-06 K-PATH/K-HOOK rows as one R4-Q1 framing.
3. **The reach map and the capability files disagree about the domain contract modules.** RTCONTRACT capability
   rows 040/041 tag them TEST_ONLY; the pack tags them LIVE because they are exported. Four PKG-10 workers flagged
   this independently. R3 should decide run-wide whether "exported through a LIVE package but consumed by no product
   code" counts as LIVE. It changes no PKG-10 Disposition except the contested DEL-10-04#CLM-004.6.
4. **The pre-v3 text was never revised (PRE_V3_DRIFT 88 rows, CAUSE2 CARRIER_PROPAGATION 43).** SoW bodies still
   carry 2026-05/06 TBD text, although later reconciliations (D-APP-53/56/58, P40/P45 notes) appended dated notes
   saying the TBDs are resolved: profiles are ADOPTED, schema refs are bound, the adapter manifest path is assigned
   and TYPES §11.3 has renamed the proposal path. No PKG-10 carrier cites D-APP-127/D-GOV-43, and `_CONTEXT.md` still
   names the Claude SDK as the current engine in several deliverables. The pattern matches R0 §8 item 6.
5. **`_REFERENCES.md` hash drift and a wrong REF-006 attribution.** All 15 CONTRACT/SPEC/PRD MATCH hashes fail to
   reproduce (one REGISTER row per deliverable). DEL-10-05 repeats "REF-006 is MATCH under D-APP-38" nine times, but
   the current pin comes from the D-GOV-43 application (`23b3879b3`, 2026-09-12). This supports R0 §8 item 7:
   repair once corpus-wide.
6. **The two REF-008 targets are split (R4-Q4).** REF-008 maps to the domain-engine persona in SoW and to the
   domain-engine workflow in `_REFERENCES.md`, and the 2026-09-09 four-role adoption (`9b005c23a`) remapped it
   (DEL-10-01#CLM-019, DEL-10-03). Cluster these with PKG-08's R4-Q4 rows.
7. **Two ownership questions for the owner:**
   - DEL-10-04#CLM-016.1 claims ownership of `_DomainEngines/profiles/pec.yaml` and its validation record, although
     D-APP-58 and SPEC §18 say this project never writes `_DomainEngines/**` (AUTHORITY_CONFLICT, plain R4;
     CONTESTED as "accountability" under D-APP-70 §9).
   - DEL-10-01#REM-1 ("register PEC as a shared-runtime client") rests on the per-user daemon topology that D-GOV-43
     retired without naming the item (AUTHORITY_CONFLICT, R4). R0 REFUTED an earlier reading of that row. The R2
     ledger instead cites DEC-019 and DIRECTIVE §8, which fits the R0 verifier's evidence.
8. **Boundary incidents.**
   - The DEL-10-01 worker read the Root top-level `execution/` tree for DEL-10-01#CLM-022.2 (VER-001). This is outside
     RUN_BASIS §3. The worker self-reported it, and the verifier regraded the row on in-root evidence. No other crossing
     was reported.
   - One coverage gap (DEL-10-03: D-APP-52 live demo, CAP-BUILD-040) exists only in reverse notes.
   - The `open_pipe_stress` validation record contains a machine-absolute path (DEL-10-04 finding). That is a
     deliverable defect, not a run artifact.
