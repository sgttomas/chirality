# N1 return — Gate-5 execution stopped and recovered

Status: `BLOCKED — INTERMEDIATE R3-A IDENTITY MISMATCH; REVISION 1.2 RESTORED`

Role evidence: bounded ephemeral Agent 2; role not mechanically enforced;
governed evidence instruction-asserted.

## Result

The node stopped before the approved Gate-5 application append was checked or
applied. The repository-approved patch-edit materialization of the seven
Gate-3 candidate surfaces did not reproduce all seven R3-A identities. Under
the sealed brief's exact execution contract, the application was not retried.
All seven live decomposition surfaces were restored to their bound revision-1.2
bytes and byte-verified. No SCA record, decision log, handoff, audit evidence,
pointer, folder, SOW, status, dependency, Task Management, tool, runtime, or App
surface was written.

## Pre-application identity fence

- Basis: `6da0b548d4ec5d303adecdd448ad1a5517c9e27b` = `origin/main`.
- PR #628 merge `4fbbb57999f1acf390fc2218a78b1a30249fd600` is an ancestor.
- Every bound Phase-0e SHA matched.
- Fresh `validate_gate5_package.py`: `PASS: 64 checks, 0 failures`.
- Embedded approved-candidate clean-scratch Gate-3 result: `PASS 98/98`,
  failures `0`.
- Embedded applied-state Gate-3 equivalent: `PASS 98/98`, failures `0`.
- `Gate_5_Validation.json` remained byte-identical at SHA-256
  `4831fb2757bfcdeb2faa0dff51a15d4f04ec68d4c9716928a36f1ea8844df966`.

## Stop condition

The intermediate materialization attempt produced these observed identities:

| Surface | Observed intermediate SHA-256 | Required R3-A SHA-256 | Result |
|---|---|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `00c35044872f3a8722a39e84bb028ee087d378190d3a108314d23ab5e9e739c8` | `0696190db9fb9319ccee40232d1a5ed77133030fea1361716ae1c05c4d8a9641` | MISMATCH |
| `chirality_root_deliverable_register_v1_0.csv` | `5f99b33e1f08ff23e74b874e11ef3884f30c9a6562a0500299d14676d7e29ca0` | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | MISMATCH |
| `chirality_root_scope_ledger_v1_0.csv` | `2fa252ab9be4759f1510578512c866c8029e60df9b157d91ae542eab30705484` | `54287bad4a9561e7dc38bea305ecb232ce081d51d49c05b94d8d86a44017a3cc` | MISMATCH |
| `chirality_root_objective_register_v1_0.csv` | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | same | PASS |
| `chirality_root_prd_coverage_forward_v1_0.csv` | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | same | PASS |
| `chirality_root_trace_reverse_v1_0.csv` | `734c030494a00018cd501bbbfb5f36de2a180a802a6c76ecca8831365b8f0785` | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | MISMATCH |
| `chirality_root_coverage_telemetry_v1_0.md` | `316185be54ec75f0ddaad847a00427a9051527ce9b94019cad2a3b4c2120d765` | same | PASS |

The failed materialization arose from transforming the approved zero-context
Git diff into the repository patch-edit format: zero-context hunks without
stable surrounding context matched non-canonically and some inserted content
landed at the end of files. This is an execution-method failure, not drift in
the approved package.

The owner-approved command
`git apply --unidiff-zero --check Gate_5_Application_Append.diff` and the one
corresponding `git apply --unidiff-zero` were **not run**.

## Recovery verification

The owner-mandated mismatch recovery restored all seven live files from the
accepted branch basis. Their final SHA-256 values are:

| Surface | Restored revision-1.2 SHA-256 |
|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| `chirality_root_deliverable_register_v1_0.csv` | `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395` |
| `chirality_root_scope_ledger_v1_0.csv` | `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2` |
| `chirality_root_objective_register_v1_0.csv` | `c645c3bd5457f3922640d2e9dfc4f315923a412fc098ad2d3bb9b2d0f8521f55` |
| `chirality_root_prd_coverage_forward_v1_0.csv` | `adde466ac0b7ea708084ed08ab16f10c5710473fd0c53a68e32c3eb53496cb84` |
| `chirality_root_trace_reverse_v1_0.csv` | `6cce13b19f27c3638fce5bd383423ee79e872bb5b1080441c3b525424e8ec3b0` |
| `chirality_root_coverage_telemetry_v1_0.md` | `6882c713763d31613ab22fe8122baf9d98739fe7cc8dbfdfead5bb84255da282` |

`git status --short` after recovery showed only the Phase-0e coordination run
tree as untracked; no governed target remained modified.

## Blocker and required owner disposition

Gate 5 remains unexecuted. The exact sequence may not be retried under this
sealed brief because the one application attempt entered the materialization
stage and triggered the explicit identity-mismatch stop rule. A fresh owner
direction is required to authorize another exact Gate-5 execution attempt and
its materialization method.

