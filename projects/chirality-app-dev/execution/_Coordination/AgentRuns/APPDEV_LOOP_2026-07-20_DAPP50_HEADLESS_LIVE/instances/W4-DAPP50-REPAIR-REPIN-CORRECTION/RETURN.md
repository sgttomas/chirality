# W4 D-APP-50 Repair Repin Correction Return

## Verdict

`ACCEPT`

The D-APP-48 source pin is corrected to the reachable G1 repair commit, the
repair and cleanup history is durably recorded without rewriting W2, and
Receipt-84 is valid. No source, lifecycle, boundary, generated-output, or Git
mutation occurred in W4.

## Basis and reproduced repair

- Branch: `codex/app-dev-dapp50-headless-live-20260720`.
- Required HEAD: `fcf152bdae1e1764b11dfabf3f87d50c5680213d`.
- Single parent: `f67d44706f4b2b5495833f809cb0bc714d2bbc18`.
- Exact G1 commit population:
  - `frontend/src/lib/harness/mcp/domain-headless-preview-runner.ts` at
    `d50d5c0c0b453547c8615f8239998b2860233bca6ab71b02e4cd9a135ba86109`;
  - `frontend/src/__tests__/lib/domain-headless-preview-runner.test.ts` at
    `133c8272ccce14f15a566363b9e46450e0b6d5b697242e752c815589dd69eb41`.
- The G1 terminal RETURN/HANDOFF/STATUS hashes reproduce update v7 exactly.
- All W2/V1/W3 evidence hashes reproduce. Receipt-83 and the W2 run record
  remain byte-identical.
- `frontend/dist` was absent before writes, remained absent after validation,
  and no packaging command ran.

## Corrected pull contract

Only `source.commitSha` changed in the D-APP-48 private intra-repo pull
contract: from `f67d44706f4b2b5495833f809cb0bc714d2bbc18` to
`fcf152bdae1e1764b11dfabf3f87d50c5680213d`. Registry version, package
identity, constants, export list/order/targets/hashes, validation commands, and
all boundary flags are byte-identical otherwise. The deterministic validator
passes at the repair commit.

## DEL-10-01 and repair evidence

DEL-10-01 preserves `IN_PROGRESS`, Checking Approval SHA
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`, the complete Remaining
section, and every earlier history line. W4 appended one repair/repin history
line only.

Exactly one distinct repair run record was created. It binds the failed V1
findings, W3's strict result-contract repair and exact ignored-output cleanup,
G1 topology and blob hashes, validation, retained D-APP-50 boundaries, and V2
as the next gate. It records that removed `frontend/dist` was ignored generated
packaging residue, reproducible only by rerunning packaging and not
Git-restorable.

Receipt-83 is byte-identical. Exactly one Receipt-84 was appended with
Parent-Receipt Receipt-83 and Examined-Through
`fcf152bdae1e1764b11dfabf3f87d50c5680213d`. It distinguishes the failed V1
evidence, executed W3 repair, ignored-output cleanup, G1 commit, corrected
repin, and held V2/final-publication gates.

## Before and after hashes

| Surface | Before SHA-256 | After SHA-256 |
|---|---|---|
| D-APP-48 pull contract | `bfe99e17541b2840795cde054f29ddad9fa390610fb58accaafc133c8a22204b` | `e01120ad843578813a558a2f9bffbf6a7504dc8d294eff983f27482dc201caa6` |
| DEL-10-01 `_STATUS.md` | `028fd7b16e1306e1e6977636cf3f924475990c7d9550750d3cf05d10e141aacb` | `b944baff46619f40ce1a20e268ac7a7097712a2434f95f66ddcdee69e3b3d614` |
| Repair run record | absent | `51365d34990e055c9ad9e8042fe845d2807d5728cbd6f002a6f2da1f85ce103a` |
| Receipt ledger | `397fb8ddceef25efe56fa146463c47e34b6a5ab0937a6e418bd163006d45f4db` | `819be78ee30629d5ef1b54814d6d4f849cd5816e675b8fc79899bb97cb12e2e8` |
| W2 run record | `c64c03604ef2b043180ac2d01caa264f18be00d386aee84929d8f4aaf020b387` | `c64c03604ef2b043180ac2d01caa264f18be00d386aee84929d8f4aaf020b387` |
| Decision register | `af1a6dec6f30e81fc19a1aab4ecf2f99874c35c97e8d83aafadeb18ebcb33920` | `af1a6dec6f30e81fc19a1aab4ecf2f99874c35c97e8d83aafadeb18ebcb33920` |

## Validation

- Strict duplicate-key JSON: PASS for the pull contract and terminal status.
- D-APP-48 pull-contract validator and recorded dependency lint: PASS.
- Focused repaired-runner suite: PASS, 48 tests.
- Receipt validator before and after Receipt-84: PASS; Receipt-83 prefix is
  byte-identical.
- Authority corpus v9: PASS, 8/8 match with no drift.
- Repository self-check: PASS at the existing 3 REVIEW / 6 WARN baseline.
- `tools/validation` pytest: PASS, 123 tests.
- `tools/practitioner_harness` pytest: PASS, 311 tests.
- Exact branch/HEAD/topology/hash, diff, no-index, cached, staged, whitespace,
  dirty-state, write-containment, and `frontend/dist` absence checks: PASS.

Packaging, provider/network, release, publication, and distribution commands
were prohibited or not applicable and were not run.

## Exact W4 writes and boundaries

W4 wrote exactly seven released paths: the pull contract, DEL-10-01 status,
the distinct repair run record, the one Receipt-84 append, and this instance's
RETURN/HANDOFF/STATUS. No earlier control/evaluation record, implementation or
test file, W2 run record, Receipt-83, decision/register, piping, tier-0, pec,
ignored/build output, or unrelated path was edited.

No apply/proposal transport, protected-path write, network/provider expansion,
packaging/publication/distribution act, lifecycle transition, waiver, or
professional/certification/sealing/authentication/code-compliance/solver-truth
claim occurred.

Blockers: none. Unknowns: none. Conflicts: none. Waivers: none. The sole next
gate is fresh independent V2 EVALUATION. Final publication remains held.
