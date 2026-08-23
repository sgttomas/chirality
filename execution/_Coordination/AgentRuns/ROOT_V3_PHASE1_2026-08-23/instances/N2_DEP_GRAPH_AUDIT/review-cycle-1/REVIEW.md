# Fresh review — N2 graph and dependency-closure audit cycle 1

Verdict: `ACTIONABLE FINDINGS — REPAIR REQUIRED`

Role entry was instruction-asserted. This fresh read-only Agent 2 reviewer did
not delegate and did not repair any project file, N2 evidence file, or N2
terminal-return file.

## Independent review basis

- Branch basis: `origin/main@e677edbe81188465eb36e700b6bd441715bcbccd`.
- Accepted N1 commit:
  `dab470e2f0c7345f10c34bcce9e489eb68bf0541`.
- Governing steer:
  `plans/steers/chirality_app_v3_phase1_steer_root_2026-08-23.md`.
- Approved propagation plan:
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md`,
  SHA-256
  `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`.
- N2 graph manifest SHA-256:
  `675357b85e806631014531de2df0fc6c02e026fc6c8bf82b4e6131d0ef416955`.
- N2 audit manifest SHA-256:
  `21990f80e3b365deed3a03bb3128b5352bb1bd22836ac57b342ac8d7aaa8b42e`.

## Independently recomputed checks

1. **Write containment — PASS.** Relative to the accepted N1 commit, the N2
   project-content additions are confined to the two declared evidence
   folders. The N2 control-plane changes are its declared `RETURN.md` and
   terminal `STATUS.json`. No live decomposition, pointer, deliverable
   metadata, prior graph/audit, Task Management, tool, runtime, project, or
   docs path differs from the N1 basis.
2. **Graph node set and path resolution — PASS.** Independent CSV parsing
   found 53 unique full register IDs and six exact package IDs. These sets
   equal the graph's 53 `ROOT_DELIVERABLE` nodes and six `ROOT_PACKAGE` nodes.
   All 59 declared paths resolve to live directories.
3. **Graph edge semantics — PASS.** The graph has exactly the 53 register
   package-membership pairs, all `PARENT_MEMBERSHIP`, structural, and
   `gating=false`. The strict dependency set is empty. No objective, scope,
   prose resemblance, or package co-membership was converted into an invented
   sequencing edge.
4. **SCC and cycle result — PASS.** Independent SCC recomputation over the
   declared graph yields 59 singleton components, zero non-trivial SCCs, and
   zero cycle-participating edges. `SCC_Report.md` covers the complete node set.
   No cut or merge is needed or claimed, so no owner gate is implicated.
5. **Deterministic graph rerun — PASS.** In a detached scratch extraction of
   N1 commit `dab470e2f...`, rerunning `derive_graph.py` reproduced all eight
   graph-package files byte-for-byte, including its manifest.
6. **Dependency-closure semantics — PASS.** Independent live-folder parsing
   found all 53 register folders, 46 pre-existing `NOT_RUN_YET` dependency
   containers, and seven new `OPEN` containers with the exact initialized-empty
   contract. The empty new state is correctly treated as expected, not a
   defect. There are zero declared dependency rows, orphan targets, non-trivial
   deliverable SCCs, hubs, or bidirectional pairs. The two schema/anchor
   coverage warnings correctly remain warnings pending the separately gated
   SOW and dependency-extraction acts.
7. **Prior-audit comparison — PASS.** The preserved Gate-1 graph and audit
   return remain byte-identical at SHA-256 `86159f1e...` and `14e131fe...`.
   The current package expressly records the broader method scope and does not
   treat the warning counts as like-for-like. No unresolved closure violation
   is asserted for the 46 unchanged pre-existing empty containers.
8. **Deterministic audit rerun — PASS.** In the same detached scratch
   extraction, rerunning the repository generic analyzer and the preserved
   `analyze_closure.py` reproduced all 24 audit-package files byte-for-byte,
   including its manifest. All three JSON documents parse.
9. **Derivative identity and rerun posture — PASS.** Both packages bind the
   accepted SCA-004 pointer, all seven revision-1.3 identities, N1 commit,
   N1 return/review identities, and declare themselves derivative. Both require
   graph and audit regeneration after accepted SOWs and dependency extraction.
10. **Artifact manifests — PASS.** The graph manifest exactly covers its seven
    other files with correct hashes; the audit manifest exactly covers its 23
    other files with correct hashes. No manifest entry is absent, extra, or
    stale.
11. **Mechanical checks — PARTIAL PASS.** `WORK_GRAPH.json`, both closure JSONs,
    candidate whitespace, and `git diff --check` pass. The raw-evidence
    convention fails as detailed below.

## Actionable finding

### F1 — Raw generic-tool evidence is not normalized or gzipped

**Exact evidence.** The six CSV preimages under
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/AUDIT_DEP_CLOSURE_POST_GATE5/Generic_Tool_Raw/`
(`bidirectional_pairs.csv`, `coverage.csv`, `hubs.csv`,
`id_normalization.csv`, `orphans.csv`, and `scc_summary.csv`) use CRLF line
terminators. `Generic_Tool_Raw/closure_summary.json` has no terminal newline.
The package calls these the generic tool's preserved raw outputs, and the
artifact manifest records those unnormalized identities.

**Violated requirement.** The Phase 1 direction and sealed N2 brief require raw
captured evidence to follow the evidence-whitespace convention: normalize it or
gzip its preimage before commit. Passing `validate_candidate_whitespace.py`
does not cure this defect; that validator intentionally ignores CRLF itself and
does not require a terminal newline.

**Bounded repair.** Inside the declared audit evidence folder, normalize the
six CSV preimages to LF and add the terminal LF to the JSON preimage, or retain
the exact raw preimages only as gzip files. Make the replay procedure perform
the same normalization deterministically; regenerate the audit artifact
manifest and update the N2 return/status identities that depend on it. Do not
change graph semantics, audit findings, or any protected surface. Then run a
fresh review cycle.

**Human gate.** None. This is an evidence-format repair only; no graph cut or
merge is implicated.

## Non-actionable observations

- The audit's `WARNING` verdict is properly calibrated to missing extracted
  dependency schemas and anchors. Those warnings are expected at this
  post-INIT/pre-extraction boundary and do not authorize extraction here.
