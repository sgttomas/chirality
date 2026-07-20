# D-APP-71 Application Backcheck — Evaluation Report

## Verdict

`ACCEPT`

The complete R1 application reproduced independently. Findings, blockers,
unknowns, conflicts, waivers, and required reruns are all zero. This verdict
validates documentary application only; it grants no repair, lifecycle,
release, publication, hard-fence, waiver, CHANGE, or Git authority.

## Basis and control provenance

- Branch / basis:
  `codex/app-dev-dapp71-application-20260720` /
  `3346120cb7c765aa7a230ee4c579ecd14f2cb022`.
- `BASIS.json`:
  `3ef9c6e03fe6d58e1db67227c5826b87426033fef44bae732279b1de82df372e`.
- Plan-v1 controls reproduced exactly: orchestration plan
  `006ab756abc8f03c4da06bbf05728a16a722f4159e07db3d146436c9a54c66a2`,
  work graph
  `3875bf5ab2a5c3d7a7e953d23914a11fc9706e29a1b56f629d5e32fca3c34349`,
  handoff state
  `783a4e8c9cade4b6897ca4d1bb3991f55ed46f4dad7443b2c55bd5dab6bba9ba`,
  and R1 brief
  `734b4c3e2cc2c88ef2c61cf4539776a56aafc52d2ed0ed0cf9263564c7589acc`.
- V1 update / launch brief reproduced at
  `324bdc82a90ac34122768cb176255803b58599d3db34095ac0c927e6053b0a68` /
  `570fc7655c2d59c63bef76677c5c1b37b774799113b3729b64209b58183578b2`.

Every control correctly cites its live authority and is treated only as
provenance. D-APP-71 is exactly
`RULED (Option 2 — DEL-02-05 physical lead)`. The meaning is coordination
only, with DEL-02-03 `selectDirectory`, DEL-02-05 `apiKey`, and DEL-09-06
`safeStorage`/security retained as distinct semantic boundaries.

## Method and coverage

The audit reconstructed all 20 `BASIS.json` direct-file hashes from exact
`HEAD` preimages where the subject had changed. It reconstructed all three
frozen trees:

- prior D-APP-70 derivative: 7 files, sorted-path hash
  `bdbf139da07a5a00ef90bf0b78b00c24bb48e64e4a6f8433026fe5c14f1fa9bd`,
  sorted content-manifest hash
  `82d585a2a22aac4a27dbee39461917077f80a7b5b9f4cbff75750332f930df16`;
- DEL-02-05 pre-existing records: 9 files, sorted-path hash
  `70ac6264ddc0e3399b55f4e4e3a9c6708c6053222ba874f65daefd64af562721`,
  sorted content-manifest hash
  `1fa84aef91e67cbd5bbdae4a12ba04b59cc8a4523a48eca4ceafee6f0502a2de`;
- DEL-09-04 pre-existing records: 9 files, sorted-path hash
  `545d2f853d1fa1ac78c33ecd1d561d9d85526d962ad618a85eeeeb602abd4930`,
  sorted content-manifest hash
  `cd2a846b792f324fce24f366b53107d9a67b745cc879cdb9e5ffe811d85082dc`.

Strict duplicate-key parsing passed for `BASIS.json`, `WORK_GRAPH.json`, R1
`STATUS.json`, the applied `MANIFEST.json`, and V1 JSON. R1 RETURN, HANDOFF,
and STATUS agree on `ACCEPT`, output maps, accounting, attribution, and zero
adverse populations. Their hashes reproduced as
`f7f2578dfb9fdd0cd15a5eca7141205d9fd5491b92b5494a1337a9a43bfa401c`,
`57402fe7be6a2ebb46a55366c61c9e614c09d78d543b64c89c48ce47151f7ac3`,
and `2ea858329fdf7f3bfb7631b1682b5cd6775c81e6907ded306a4e0c0792cad45c`.

## Validated derivative inventory and accounting

The new derivative contains exactly seven files. Hashes in required schema
order are:

1. `RUN_BASIS.md` —
   `1af232efc520cefd4c9537678b0a179c4ee8838d4e9b444fe957fa4ba21e84db`.
2. `APPLIED_MAPPING.csv` —
   `e22af22f9886a660da74e851511f6d0d9eaca0d2560ca85c4da6e5b157e87805`.
3. `RETAINED_BOUNDARIES.md` —
   `be28c460de1bacdb21f24e00318f02de01335589396a291672a5e4a7d68a5e44`.
4. `REMAINING_DISPOSITION.csv` —
   `f64a0b84fe9c3c686b9ee8c23b6a8ebbaecd369b5aa527cfe6744512c1be9d66`.
5. `QA.md` —
   `d58856e5075f950e0221859b2e15dff87a3d0f4b90c0f93320e33f14efa4b61f`.
6. `HANDOFF.md` —
   `4986335fd79e8fab5acdf060f2ac9552bc2a0a715df30da6e504c2e809321255`.
7. `MANIFEST.json` —
   `3f8d5cd16d932dce37dee2b73df1079f15eca843d1f22d2ca98b6f23e7a54c21`.

The mapping CSV has its exact nine-column schema and one group-6 row for
`frontend/electron/preload.ts`, DEL-02-05, and
`APPLIED_PHYSICAL_COORDINATION_LEAD`. The disposition CSV has its exact
nine-column schema and two rows in DEL-02-05 / DEL-09-04 order. Every manifest
file, status, record, and receipt binding recomputes.

Accounting is exactly one mapped path, one coordination lead, three retained
boundaries, two status-history edits, two local records, one closed D-APP-71
residual, one byte-preserved non-CQF1 Remaining item, and zero source, SOW,
dependency, lifecycle, or release changes.

## Status transformations and preservation

The DEL-02-05 current status hash is
`18b67eb473d012d6634804198c4e2c3e3b8d89b52970480836ee9373f9f887ac`.
Relative to `git show HEAD:<path>`, its sole delta is one 2026-07-20 history
bullet; its empty Remaining section and every other byte are preserved.

The DEL-09-04 current status hash is
`d8cc8a536141f4cba2805d575ad1bcb873c825c07fed9d0fb049b07589c69472`.
Its only deltas are removal of the exact D-APP-71 residual and insertion of one
2026-07-20 history bullet. The full packaging/release Remaining line is
byte-identical to `HEAD`, and all other bytes are preserved.

Exactly one new record was added to each frozen nine-file record tree. Their
hashes are
`cc9c5a220561989e68068a4f1acefcce5effa1dde6e80e383bc0cf1907105e20`
and
`d057870537410318ace07c7788ad87f2621ceb51da1498a17344877b078d0561`.
Both contain all required headings, bindings, and no-change assertions.

The prior D-APP-70 derivative remains byte-identical across all seven files.
The preload remains
`189b0d30bd8f6daf84862e14cfc3ec68c2c211b5c123283c7108c50c3b750ba0`.
The complete delta contains no frontend/runtime source, ScopeOfWork,
dependency, MEMORY, decomposition, authority, decision, lifecycle, release,
publication, hard-fence, waiver, staging, or other Git mutation.

## Receipt, validators, hygiene, and containment

Receipt-82 is unique and latest, has parent Receipt-81, and examines through
the exact basis commit. Its pointers resolve, attribution is accurate, and its
pass/fail and no-effect statements match the reproduced evidence. The entire
Receipt-81-and-earlier byte sequence is an unchanged prefix. The ledger hash
is `8eabef4042ee83e44403fffead019748109c76c66013c050f45b431bcfb0b520`.

- Receipt validator: PASS.
- Authority corpus v9: PASS, 8/8 `MATCH`, no drift.
- Repository self-check: PASS, exit zero at 3 `REVIEW` / 6 `WARN`.
- `git diff --check`: PASS.
- Per-new-file no-index whitespace checks: PASS.
- Pre-V1 containment: exactly 3 modified, 20 untracked non-ignored, and 51
  ignored files; the released subject/control population is exact and staged
  state is empty.
- Frontend execution: SKIPPED because every runtime source is frozen and
  unchanged.

## Findings, recommendations, and decision queue

Findings: 0. Blockers: 0. Unknowns: 0. Conflicts: 0. Waivers: 0. Required
reruns: 0 at the current bound state. There is no remediation recommendation
and no human decision in this evaluation.

The only next gate is HELP_HUMAN validation of this terminal V1 return. CHANGE
remains held until separately released. Any bound-byte, population, authority,
receipt-cursor, or Git-state change requires a fresh evaluation release.

## Derivative status and handoff

The applied D-APP-71 package is current additive derivative evidence. It does
not replace authoritative decomposition, decision, deliverable, lifecycle, or
source truth. Subject files remained read-only throughout V1.
