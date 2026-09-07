# QA report

- Parsed the SOFTWARE working surface by semantic headings and its authoritative companion registers.
- Found one declared package and seven declared deliverables; all exact folders exist and no reverse-only folder exists in scope.
- Compared every declared name, package, type, responsible party, description and `ContextEnvelope` against all seven `_CONTEXT.md` files; all matched.
- Validated all seven production contracts with `tools/scope_of_work/validate_scope_of_work.py --json`; each resolved to valid `SOW_V1` with zero issues.
- Verified all seven deliverables remain `INITIALIZED`; the 40 anticipated production outputs remain absent and are recorded as INFO.
- Verified live ledger SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d` and byte equality with the approved v6 postimage. The candidate patch has one deletion and one insertion and changes only the CSV `DecisionRef` and `Notes` fields from preimage SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`.
- Verified the other SCA-002 canonical postimages remain SHA256 `19baaea22ba3a5b2dc465c30f7e8273db7b1833fd4a9bf6c2de0fc6056dcdd9d` and `413687ca6a857f5464a3205e9f9c4b29ace512c8d2b67dfa095ef3640fab883e`.
- Independently rehashed all 16 SCA-003 manifest members; zero member or byte-count failures. `_ScopeChange/_LATEST.md` is byte-identical to SCA-003 `LATEST_POSTIMAGE.md`.
- Rehashed SCA-002 manifest and the first blocked audit manifest, return and issue log to their prior recorded identities.
- Rehashed the external PKG02 owner decision and manifest at the absolute ledger-cited paths; they record `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` as accepted contract basis with later acts excluded.
- Counted one IN scope row, one package, seven carriers, four objectives, 66 unique qualified source and successor requirements, ten hold rows comprising nine `HELD_UNAVAILABLE` plus one R16-B disposition, and seven full-wire/source gate rows.
- `git diff --name-only 579015fab0c121e702d10c255d2824a86bcad58d -- projects/chirality-runtime/execution/PKG-02_Runtime_Product` returned empty. No deliverable contract, context, status, dependency or lifecycle file changed from the SCA application basis.
- Limitation: this audit establishes decomposition/file consistency and exact SCA-003 poststate only. It does not establish implementation, supplier qualification, signing/identity proof, paired client conformance, recovery/lifecycle completion, protected-fixture status, hold release, hosted readiness, publication, Root adoption, Gate 5 acceptance or release.
