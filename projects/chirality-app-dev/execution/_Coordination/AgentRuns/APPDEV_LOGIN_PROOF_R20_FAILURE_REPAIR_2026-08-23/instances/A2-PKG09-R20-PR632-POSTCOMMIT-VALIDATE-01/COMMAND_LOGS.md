# Command logs — A2-PKG09-R20-PR632-POSTCOMMIT-VALIDATE-01

All commands ran from repository root unless an App-root working directory is stated. Every command below was read-only except that governance tools could create ordinary interpreter/test cache bytes already permitted by their own implementation; no candidate/shared file was edited by a command. The only authored records are in this instance directory.

## Retained predecessor gate

The manager ran this exact command after commit and before this dispatch; this instance retained the result and did not rerun it until the final after-record freeze:

```text
$ python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main
[exit 0]
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

## Rerun governance/control-plane gates

```text
$ python3 tools/run_affected_tests.py --base origin/main
[exit 0]
selection schema: chirality-affected-checks/v1
selected suites: practitioner_harness, validation
skipped suites: analysis, coordination, decomp, drawing_extract, equation_audit, pdf2md, publication, reporting, retrieval, scope_of_work, software_workflow, source_audit, source_catalog, taskmgmt, workflow_runtime
670 passed in 10.84s
```

```text
$ python3 tools/practitioner_harness/harness.py self-check
[exit 0]
Finding severities: INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=43
```

The complete self-check output classified all findings below BLOCK. The four REVIEW findings were three known `_DomainEngines` staleness annotations and one known machine-absolute path in a governed validation surface; the 43 WARN findings were unresolved historical source references. The tool exited zero under its governing severity contract.

```text
$ python3 tools/validation/validate_root_materialization_fence.py
[exit 0]
G0 PASS: G1-G4 registered and passing per execution/_harness/root_guards.yaml; materialization gate satisfied.

$ python3 tools/validation/validate_root_harness_adapter.py
[exit 0]
G1 PASS: root harness adapter execution/_harness/adapter.yaml is schema-valid (root-harness-adapter/v1); declared pointers exist and pinned baselines match the observed tree (status_files=46, pinned_at=2db2c712825af13d6b5425c34d31ff9daf470c89).

$ python3 tools/validation/validate_root_surface_ownership.py
[exit 0]
G2 PASS: surface-ownership register execution/_harness/surface_ownership.yaml is schema-valid (root-surface-ownership/v1); 7 entries declare write targets; 6 materialized PKG-*/DEL-* children all registered.
INFO: identical write target runtime/** for DEL-02-06 and PKG-02 is a recorded static fact; serialization is a G3 question.

$ python3 tools/validation/validate_root_work_graph_dispatch.py
[exit 0]
G3 PASS (CI mode): work graph work_graph.yaml is schema-valid (root-work-graph/v1); 6 nodes, active: none; declared write targets, disjointness/serialization, and M2 markers check out.

$ python3 tools/validation/validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only
[exit 0]
G4 PASS (diff mode): 45 tranche manifests are schema-valid (instruction-tranche-manifest/v1).
INFO: diff origin/main..HEAD: 119 changed paths, 0 on the instruction surface, checked against 0 manifests.
```

```text
$ python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
[exit 0]
VALID /Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/loop/LOOP_RECEIPTS.md: frozen through Receipt-52; versioned receipt contract satisfied

$ git diff --check
[exit 0]
[no output]
```

```text
$ PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status
[working directory: projects/chirality-app-dev]
[exit 0]
corpus current_version: v18
8 MATCH rows: DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD, AGENT_SOFTWARE_DECOMP, AGENT_DOMAIN_ENGINE
no drift.
```

```text
$ PYTHONDONTWRITEBYTECODE=1 python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-PR632-POSTCOMMIT-VALIDATE-01.md --target DEL-09-04
[working directory: projects/chirality-app-dev]
[exit 0]
schema: chirality-app-hold-check/v1
repo_head: de2080a7ac82f636fca3f8be57b20dc0e9a80fa8
register_sha256: e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f
scan_fingerprint_sha256: 6b0d6ced5fa4609385aec213b11a44018bef869a5162ee78f7e6198b08ced27a
DEL-09-04: contract_status CLEAR; hold_status NOT_HELD; verdict ALLOW
overall verdict: ALLOW
```

```text
$ python3 tools/software_workflow/validate_change_scope.py . --allowed projects/chirality-app-dev
[exit 0]
schema: chirality-change-scope/v1
status: PASS
paths: 5
violations: []

$ git diff --cached --name-only
[exit 0]
[no output]

$ git status --porcelain=v1 -- projects/chirality-app-dev/frontend
[exit 0]
[no output]

$ git rev-parse HEAD:projects/chirality-app-dev/frontend cb008dc5d6aa9b249639c91f3453a18609530d0f:projects/chirality-app-dev/frontend
[exit 0]
b4c73edda1fe3346815ce75449b2327c80c79bf8
b4c73edda1fe3346815ce75449b2327c80c79bf8

$ git diff --stat cb008dc5d6aa9b249639c91f3453a18609530d0f..HEAD -- projects/chirality-app-dev/frontend
[exit 0]
[no output]
```

The read-only instruction-root current-byte comparison was an inline Python hash/size comparison over the accepted summary/manifest, every manifest source and bundle member, bundle agent roster, SDK required members, and selected-platform members. It wrote nothing.

```text
[exit 0]
status: PASS
summary_sha256: 3a9666d40235dfbaedf16dc3da29b0bc541b64298ae2faec05dcb27a202d3b36
manifest_sha256: c5b2bf101de6412ae63fd19ba76cac6c73cffa156357551c4203a54ce771135b
gitSha: cb008dc5d6aa9b249639c91f3453a18609530d0f
checked_files: 43
bundle_agents: 34
sdk_required_files: 3
selected_platform_files: 2
sourceCompleteness: needs_remediation
failures: []
```

The read-only repair-lineage comparison parsed the committed 11-row gzip table, required every raw source absent, verified each gzip byte/hash identity and decompressed byte/hash identity, and verified the repaired executor RETURN.

```text
[exit 0]
status: PASS
gzip_rows: 11
raw_sources_absent: 11
gzip_members_exact: 11
return_bytes: 16436
return_sha256: 253819ca75533f6c0f46f9844ea1641f16e694a51ed3e4fffd9bb80b9f0afb55
failures: []
```

The strict duplicate-key JSON/JSONL parser examined the union of changed tracked and untracked App records against `origin/main`.

```text
[exit 0]
status: PASS
count: 11
failures: []
```

The exact immutable semantic/package identity command was:

```text
$ shasum -a 256 <R20> <DEL-status> <TM-candidate> <proof-script> <proof-test> <fixture> <packaged-main-executable> <packaged-runtime-cli> <dist-electron/main.js> <instruction-summary> <instruction-manifest>
[exit 0]
bc9d39ba804c59a4a1cc7b1b5de39785288e2fe6a8539ca2e3936c99c118303c  R20 record
6c864ceebd8769c47519a3fba338dc2932667efa6ad590bc1fd25b62851feb48  DEL-09-04 _STATUS.md
45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8  TM candidate
f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306  proof script
6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18  proof test
9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531  fixture
79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874  packaged main executable
0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989  packaged runtime CLI
bfcf16002fc5132d0d96c68a5574927bfd0593b1ce905e71bea72a957bfc4ce1  dist-electron/main.js
3a9666d40235dfbaedf16dc3da29b0bc541b64298ae2faec05dcb27a202d3b36  instruction-root summary
c5b2bf101de6412ae63fd19ba76cac6c73cffa156357551c4203a54ce771135b  instruction-root manifest
```

## Explicitly not run

No product/frontend/runtime test or typecheck; build; package; supply or package verifier; daemon/precheck; proof/preflight/procedure; GUI; launchd; operator/private evidence; network; signing; release; or Git mutation command ran in this instance.
