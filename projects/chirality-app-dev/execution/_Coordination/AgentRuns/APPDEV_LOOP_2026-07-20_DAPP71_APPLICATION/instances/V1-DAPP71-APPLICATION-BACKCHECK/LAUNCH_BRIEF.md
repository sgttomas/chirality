# V1-DAPP71-APPLICATION-BACKCHECK Launch Brief

- **Role:** EVALUATION (Agent 1; load and obey
  `agents/AGENT_EVALUATION.md`)
- **Parent/dispatcher:** HELP_HUMAN
- **RunID:** `APPDEV_LOOP_2026-07-20_DAPP71_APPLICATION`
- **Phase:** independent post-application backcheck
- **Branch / basis:** `codex/app-dev-dapp71-application-20260720` /
  `3346120cb7c765aa7a230ee4c579ecd14f2cb022`
- **Release update:** `../../updates/v2.md`
- **Release-update SHA-256:**
  `324bdc82a90ac34122768cb176255803b58599d3db34095ac0c927e6053b0a68`
- **Basis manifest:** `../../BASIS.json`
- **Basis-manifest SHA-256:**
  `3ef9c6e03fe6d58e1db67227c5826b87426033fef44bae732279b1de82df372e`
- **Subject posture:** read-only
- **Delegation:** prohibited
- **Repair / CHANGE / Git:** prohibited

## Objective and decision criterion

Independently attempt to refute the complete R1 D-APP-71 application against
the frozen basis, R1 brief, exact HEAD preimages, D-APP-71, Receipt-81/82,
prior and new derivatives, and current worktree. Return `ACCEPT` only if every
required hash, schema, count, transformation, retained-boundary assertion,
no-change claim, validator result, and containment claim is independently
reproduced with zero findings, blockers, unknowns, conflicts, waivers, or
required reruns. Otherwise return `BLOCK` with exact evidence. Do not repair.

## Frozen subject and provenance

Require these R1 terminal hashes:

- `RETURN.md`:
  `f7f2578dfb9fdd0cd15a5eca7141205d9fd5491b92b5494a1337a9a43bfa401c`
- `HANDOFF.md`:
  `57402fe7be6a2ebb46a55366c61c9e614c09d78d543b64c89c48ce47151f7ac3`
- `STATUS.json`:
  `2ea858329fdf7f3bfb7631b1682b5cd6775c81e6907ded306a4e0c0792cad45c`
- applied derivative `MANIFEST.json`:
  `3f8d5cd16d932dce37dee2b73df1079f15eca843d1f22d2ca98b6f23e7a54c21`
- receipt ledger through Receipt-82:
  `8eabef4042ee83e44403fffead019748109c76c66013c050f45b431bcfb0b520`

Require the plan-v1 control provenance at the exact hashes recorded in
`updates/v2.md`: basis, orchestration plan, work graph, handoff state, and R1
launch brief. Require v2 itself at its bound hash. No control file is
authority; each must correctly cite the live authoritative source it uses.

## Required independent audit

### 1. Basis, authority, and terminal schema

- Strict-parse `BASIS.json`, `WORK_GRAPH.json`, R1 `STATUS.json`, the applied
  `MANIFEST.json`, and every V1 JSON output with all-depth duplicate-key
  rejection.
- Reproduce all 20 direct-file hashes and all three frozen-tree counts,
  sorted-path hashes, and sorted content-manifest hashes in `BASIS.json`.
- Require D-APP-71 exactly
  `RULED (Option 2 — DEL-02-05 physical lead)`, with coordination-only meaning
  and the three retained semantic boundaries.
- Validate R1 RETURN/HANDOFF/STATUS agreement, exact terminal `ACCEPT`, output
  maps, zero findings/unknowns/conflicts/waivers/reruns, and truthful
  attribution.

### 2. New derivative and accounting

Independently hash and inspect exactly seven files under
`execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/APPLIED_DAPP71_3346120C/`.
Reproduce these hashes in filename/schema order:

1. `RUN_BASIS.md` — `1af232efc520cefd4c9537678b0a179c4ee8838d4e9b444fe957fa4ba21e84db`
2. `APPLIED_MAPPING.csv` — `e22af22f9886a660da74e851511f6d0d9eaca0d2560ca85c4da6e5b157e87805`
3. `RETAINED_BOUNDARIES.md` — `be28c460de1bacdb21f24e00318f02de01335589396a291672a5e4a7d68a5e44`
4. `REMAINING_DISPOSITION.csv` — `f64a0b84fe9c3c686b9ee8c23b6a8ebbaecd369b5aa527cfe6744512c1be9d66`
5. `QA.md` — `d58856e5075f950e0221859b2e15dff87a3d0f4b90c0f93320e33f14efa4b61f`
6. `HANDOFF.md` — `4986335fd79e8fab5acdf060f2ac9552bc2a0a715df30da6e504c2e809321255`
7. `MANIFEST.json` — `3f8d5cd16d932dce37dee2b73df1079f15eca843d1f22d2ca98b6f23e7a54c21`

Verify the exact headers and values frozen by the R1 brief: one mapping row
for group 6 / preload / DEL-02-05 /
`APPLIED_PHYSICAL_COORDINATION_LEAD`, and two disposition rows in DEL-02-05,
DEL-09-04 order. Recompute every manifest file/status/record/receipt binding.
Prove accounting is exactly: one mapped path, one coordination lead, three
retained boundaries, two status-history edits, two local records, one closed
D-APP-71 residual, one byte-preserved non-CQF1 Remaining item, and zero
source/SOW/dependency/lifecycle/release changes.

### 3. Exact status transformations and local records

Use `git show HEAD:<path>` as the two status preimages; do not trust only the
derivative summary.

- DEL-02-05 final SHA-256 must be
  `18b67eb473d012d6634804198c4e2c3e3b8d89b52970480836ee9373f9f887ac`.
  Its only delta is one 2026-07-20 history bullet; `## Remaining` stays empty
  and all status metadata/history preimage bytes remain otherwise identical.
- DEL-09-04 final SHA-256 must be
  `d8cc8a536141f4cba2805d575ad1bcb873c825c07fed9d0fb049b07589c69472`.
  Its only deltas are removal of the exact D-APP-71 preload residual and
  insertion of one 2026-07-20 history bullet. Independently prove the entire
  packaging/release Remaining line is byte-identical to HEAD and all metadata
  and prior-history bytes remain identical.
- Require exactly one new local record in each frozen nine-file run-record
  tree, both named
  `R1_DAPP71_PRELOAD_PHYSICAL_LEAD_APPLICATION_2026-07-20.md`, at hashes
  `cc9c5a220561989e68068a4f1acefcce5effa1dde6e80e383bc0cf1907105e20`
  and `d057870537410318ace07c7788ad87f2621ceb51da1498a17344877b078d0561`.
  Validate required headings, bindings, and no-change assertions.

### 4. Preservation and no-change audit

- Reproduce the prior `APPLIED_DAPP70_36A422AC/` population of seven and every
  individual/path/content-manifest hash from `BASIS.json` and the R1 brief.
- Reproduce the frozen preload hash. Inspect the complete worktree delta and
  prove there is no frontend/runtime source, ScopeOfWork, `_DEPENDENCIES.md`,
  `Dependencies.csv`, MEMORY, decomposition, authority, decision packet/ruling/
  register, pre-Receipt-82 ledger prefix, other status, lifecycle, release,
  publication, hard-fence, waiver, or Git mutation.
- Prove the physical lead is coordination only everywhere summarized and that
  DEL-02-03 `selectDirectory`, DEL-02-05 `apiKey`, and DEL-09-06
  `safeStorage`/security remain distinct.

### 5. Receipt, validators, hygiene, and containment

- Require Receipt-82 unique/latest, parent Receipt-81, Examined-Through exact
  basis, valid pointers, accurate pass/fail-only checks, correct attribution,
  and accurate no-effect statements. Prove Receipt-81-and-earlier bytes are an
  unchanged prefix. Run the receipt validator.
- Run authority corpus v9 status and require no drift. Run repository
  practitioner self-check and require exit zero at the existing 3 REVIEW / 6
  WARN baseline.
- Run `git diff --check`; perform `git diff --no-index --check /dev/null` (or
  an equivalent byte-level check) for every new subject and V1 output file.
- Inventory tracked, untracked non-ignored, and ignored state before and after
  V1. Require the subject delta to match the R1 release exactly and V1 writes
  to match only the paths below. No unaccounted path is acceptable.

## Exact V1 output and write scope

The evaluated subject is read-only. V1 is the serialized evaluation owner for
this stage and may use read-only filesystem/Git inspection and deterministic
validation commands. It may write only:

1. `projects/chirality-app-dev/execution/_Evaluation/DAPP71_APPLICATION_BACKCHECK_3346120C_2026-07-20/`
   with exactly `EVALUATION_PROTOCOL.md`, `FINDINGS.csv`,
   `EVALUATION_REPORT.md`, `HANDOFF.md`, and `MANIFEST.json`;
2. this instance directory's new `RETURN.md` and `HANDOFF.md`, plus replacement
   of this released `STATUS.json` with terminal status.

`FINDINGS.csv` uses the exact header
`FindingID,Concern,Classification,Severity,Scope,Claim,EvidenceRefs,Status,RecommendedOwner,RerunRequirement`.
On `ACCEPT` it has zero data rows. On `BLOCK`, record every finding without
repair. The evaluation report contains basis, method, coverage, exact
validated inventory, findings, conflicts/unknowns, recommendations, decision
queue, derivative status, and handoff. The evaluation manifest binds all
other evaluation-root and instance output hashes without self-hashing itself.

Terminal `RETURN.md`, `HANDOFF.md`, and `STATUS.json` bind the exact subject and
output hashes, all validation results, findings/blockers/unknowns/conflicts/
waivers/reruns, read-only containment, and next gate. Set terminal `status` and
`verdict` to the same exact `ACCEPT` or `BLOCK`, `terminal=true`,
`accepted=false`, `delegated=false`, and `waivers=[]`.

## Absolute prohibitions and terminal gate

No delegation. No subject repair or mutation. No Receipt-83. No R1/control
rewrite. No source, SOW, dependency, status, local-record, decision, lifecycle,
release, hard-fence, waiver, CHANGE, staging, commit, push, PR, merge, cleanup,
or branch action. Frontend execution gates remain skipped because runtime
source is frozen; verify the skip rationale rather than running them.

Return `ACCEPT` only on complete independent reproduction with zero adverse or
unknown population. Otherwise return `BLOCK`. CHANGE remains held regardless
of V1's raw verdict until HELP_HUMAN separately validates fan-in and releases
it through another versioned control update.
