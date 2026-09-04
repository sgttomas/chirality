# Candidate Check Evidence — R6 / Remediation R2

Status: `PREPARATION_CHECKS_PASS`

Basis: `287b82f16c0d3970bac71e40b0e41fdd50569b08`

Every Python invocation used `PYTHONDONTWRITEBYTECODE=1` or an absolute
`PYTHONPYCACHEPREFIX` outside the worktree. Pytest cache creation was disabled.

| Check | Result | Evidence |
| --- | --- | --- |
| Live-layout APP-HOLD regressions and adversarial matrix | PASS | 28 tests and 91 subtests passed. |
| Standalone frozen-candidate APP-HOLD regressions and adversarial matrix | PASS | 28 tests and 91 subtests passed from proposal-local tool/register/tests. |
| Approval identity, nonregular-entry, and bytecode-containment regressions | PASS | 15 tests passed, including exact frozen verification, two-digest deterministic rendering, exact-answer rejection, malformed-manifest rejection, exact acyclic exclusions, literal file-set equality, cache/bytecode rejection, FIFO rejection with path-naming diagnostic, and final-gate contract checks. |
| APP-HOLD live candidate scan with register parity | PASS | 53 contracts; no holds; bootstrap row structurally valid and `INACTIVE` on the live decomposition and companion preimages. |
| Exact-postimage simulation; folder absent | PASS | Register parity `PASS`; bootstrap state `ELIGIBLE`; both exact tokens returned `ALLOW` with `admission_kind=STRUCTURAL_BOOTSTRAP`. |
| Exact-postimage simulation; subset and all-five folder states | PASS | Absent, two-file subset, and all-five regular-file states admitted under both exact tokens. The implementation treats the five authorized names as a set, covering empty, partial, and complete cardinalities without claiming exhaustive powerset enumeration. |
| Wrong target/package/operation/token | PASS | Each fails closed in the adversarial suite. |
| Decomposition/companion/pointer hash drift | PASS | Each independent mismatch fails closed. |
| ScopeOfWork appearance | PASS | Fails closed. |
| Extra/nested/non-regular/symlink folder content | PASS | Each fails closed; includes a symlink target folder. |
| Symlink authority input | PASS | Fails closed. |
| Malformed/duplicate rows and active-HOLD collision | PASS | Each fails closed; ordinary HOLD precedence is preserved. |
| `harness-self-check` | PASS | Registered command arguments run with the available Python 3.13 dependency environment exited zero; existing REVIEW/WARN/INFO findings are outside this tranche. |
| `app-hold-integrity` | PASS | Registered command exited zero; bootstrap is dormant on the preparation preimages. |
| `harness-pytest` | PASS | Registered command arguments run with the available Python 3.13 dependency environment passed 350 tests. |
| Receipt validator | PASS | Live ledger valid on the preparation basis; physical tail Receipt-225; no candidate receipt appended. The validator's legacy summary still says "frozen through Receipt-52" and is not used as the cursor. |
| Authority corpus status | PASS | v20; no drift. |
| Current-main preservation | PASS | Exact-one-ref remote-main checks at launch and freeze returned the preparation basis. Approved-R4-to-remediation-basis comparison contains only PR #700's five `plans/shell-redesign_2026-09-04/**` paths; no candidate overlap. |
| Exact uncommitted candidate scope | PASS | Exactly 57 paths: eight application-payload paths plus 49 proposal files. No receipt, decision, SCA, pointer, decomposition, companion, product, frontend, runtime-plan, Root, host, signing, release, or other path was changed. |
| Literal future application topology | PASS | `LIVE_SURFACE_MANIFEST.csv` has exactly 61 unique sorted rows: 8 `MODIFY`, 52 `ADD`, and 1 `APPEND_REMINT`. The 52 adds are 49 proposal files, D-APP-104 packet and ruling, and live `bootstrap_expected.json`; the eighth modify is the decision register. |
| Live preimages and D-APP-104 collision | PASS | All eight existing live preimage SHA-256 values and `100644` kinds match basis; all 52 adds are absent; D-APP-103 is highest and D-APP-104 is free. Target folder and ScopeOfWork are absent; authority/pointer states match the frozen prerequisites. |
| Strict JSON and CSV parse | PASS | All 10 proposal JSON files and all 8 proposal CSV files parse strictly. |
| Candidate Python compile | PASS | Live, proposal-local, test, and approval-renderer Python files compile with an absolute bytecode cache outside the worktree. |
| Application payload manifest | PASS | Exact eight-file set and all postimage digests verified; payload bytes are unchanged from approved R4. |
| Approval-effect manifest and deterministic outputs | PASS | Eleven exact authoritative leaves verify. The replacement approval root is `2236de0840fde97efbbfb36ab29aa6a9e11fc839117c75beb81234852f6a9413`; owner question and conditional ruling reproduce from that root plus the external artifact-manifest digest. |
| Proposal/artifact file-set enforcement | PASS | 49 observed regular files equal `PROPOSAL_FILESET.txt` and 49 literal proposal rows; 61 total live-surface rows. The artifact manifest has exactly 46 leaves and excludes exactly itself plus the two digest-dependent deterministic outputs. An injected unlisted FIFO makes verification fail nonzero with its relative path in the diagnostic; clean restore verifies. |
| Complete patch representation | PASS | `COMPLETE_CANDIDATE.diff` contains 53 Git binary-patch records and a nonblank end sentinel, with no textual hunks or zero-context dependency. It excludes only itself, the later artifact manifest, and the two deterministic digest-dependent outputs. |
| Strict patch reconstruction | PASS | A clean exact-basis checkout accepts standard `git apply --check --whitespace=error-all`, applies forward, and reconstructs all 57 candidate paths byte-identically after the two added files and deterministic renders. Standard strict reverse check/application restores the exact basis for all 53 patch-carried paths; no `--unidiff-zero` is used. |
| Complete future tracked application and receipt contract | PASS | A new disposable exact-basis checkout materialized and staged all 61 future paths, including all 49 proposal files and `COMPLETE_CANDIDATE.diff`. Its provisional Receipt-226 uses lawful `AWAITING_OWNER`, identifies the run as simulation-only, disclaims authority and every unperformed act, and is not live. Receipt validation, registered harness self-check, all 350 harness tests, staged `git diff --check`, and basis-to-resulting-tree `git diff --check` exited zero. |
| Candidate `git diff --check` | PASS | The complete 57-path uncommitted candidate has no whitespace errors. |
| F-APP-2 and forbidden scope | PASS | No signing, notarization, publication, external distribution, deployment, release act, host act, product/frontend source, Root, SCA, pointer, decomposition, companion, or lifecycle path is in the candidate write set. |
| Post-application and remediation-review findings | PASS | Binary records prevent embedded patch content from becoming outer text additions with whitespace errors while strict forward/reverse applicability and byte identity remain intact. Artifact-remediation R1 M-1 is closed by fail-closed nonregular-entry verification and FIFO coverage; M-2 is closed by a freshly derived receipt-valid `AWAITING_OWNER` future tree. No reviewer-reported future-tree hash was reused. |
| Frontend build/typecheck/test | NOT APPLICABLE | No `frontend/**`, product, or runtime source path is in the candidate. |
| A1 re-stage declaration | NOT APPLICABLE | No frontend mutation. |

The literal registry uses `python3`; the host's default Xcode interpreter lacks
PyYAML/pytest. Where those dependencies were required, the same registered
arguments were run with
`/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3.13`, matching
the available registered-check environment used by the prior candidate.
