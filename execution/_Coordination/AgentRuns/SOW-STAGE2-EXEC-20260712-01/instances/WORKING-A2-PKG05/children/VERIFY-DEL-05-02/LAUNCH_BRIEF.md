# TASK Verifier Brief — DEL-05-02

RequestedBy: `WORKING-A2-PKG05`; RunID: `SOW-STAGE2-EXEC-20260712-01`; ChildInstanceID: `VERIFY-DEL-05-02`. Dependency: terminal manager acceptance of `AUTHOR-DEL-05-02`.

Act as a fresh Agent 2 TASK verifier; do not delegate. Read complete `agents/AGENT_TASK.md` and all four `skills/scope-of-work/*` method files. Use `TaskSkill: scope-of-work`, `MODE=VERIFY`, `ApplyEdits: true` for evidence only.

Exact accepted row: `DEL-05-02` in `snapshots/W_A2/preflight/A2_MANIFEST.tsv`; exact candidate: `candidates/W_A2/APP-PKG05/DEL-05-02/ScopeOfWork.md`; author evidence is read-only. Bind all row hashes and values, `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176`, and `main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa`.

AllowedWriteTargets: only `instances/WORKING-A2-PKG05/children/VERIFY-DEL-05-02/**`. Candidate and live project are read-only. Exclude Git, other deliverables/packages, `.claude-worktrees`, H1/H2, repair, lifecycle, integration, release, retirement.

Independently reconstruct an isolated workspace from exact live legacy sources/status/control plus accepted candidate. Reproduce format resolution, all hashes, schema validation, claim map, parity, checklist twice, renderer twice, source/status identity, authority, conservative semantic-addition review, negative partial/unauthorized-dual fail-closed behavior, portability, and write containment. Do not repair candidate.

Produce portable `INIT-TASK.md`, isolated workspace and `_run_records`, `SOURCE_HASHES.tsv`, `VALIDATION.json`, `CLAIM_MAP.csv`, `PARITY.json/.md`, two checklists, two HTMLs, negative-test evidence, `CHECKS.md`, exact five-row `REPLACEMENT_MANIFEST.tsv`, self-excluding `MANIFEST.tsv`, terminal `STATUS.json`, and `RETURN.md` with candidate SHA, mapping/source-line counts, verdict classes, containment, blockers/waivers/reruns. Replacement is one ADD candidate-to-live `ScopeOfWork.md` plus four DELETE legacy docs only; exclude status/control paths. Inventory immutable source literals; preserve initial failures and mechanically terminalize evidence if needed.
