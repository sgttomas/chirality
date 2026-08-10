# Frozen work graph v1 — D-APP-93 fresh packet authoring

Status: `FROZEN BEFORE DISPATCH`

- Frozen at: `2026-08-10T02:40:08Z`
- Selection authority: explicit owner-directed finite serialized pipeline.
- Posture: `TERMINAL_FAN_OUT_IN` implemented as a strictly serialized chain to
  prevent authority and byte fan-in drift.
- Package: `PKG-09`; selected deliverable: `DEL-09-04`.
- Shared-write rule: only one child owns writable packet surfaces at a time.
  Predecessor terminal return acceptance is required before successor release.
- Finite convergence: one child session per node; no remediation chain or
  replacement child may be invented after a failed required fan-in. On failure,
  manager closes the lineage `BLOCKED`.

## Nodes and gates

| Node | Fresh Agent 2 objective | Reads | Allowed writes | Release gate | Expected return |
|---|---|---|---|---|---|
| N1 | Accepted-source and command-surface reconstruction | Activation; live accepted sources; only allowed terminal old-root pointers; deterministic old-root inventory | `source_reconstruction/**`, `returns/N1_*` | immediate | exact accepted-source ledger, hashes, command/operator surface, historical command-identity exclusion list, old-root before inventory/digest, terminal return |
| N2 | Author complete fresh command-authority ledger | accepted N1 outputs and accepted source paths only | `candidate_packet/COMMAND_AUTHORITY_LEDGER.md`, `returns/N2_*` | N1 accepted | individually enumerated fresh command IDs and operator inputs; all `OWNER_APPROVAL_REQUIRED`; zero executable text outside entries within ledger |
| N3 | Author supporting packet aligned to frozen ledger | accepted N1/N2 outputs and accepted source paths only | supporting files under `candidate_packet/**` except ledger/index; `returns/N3_*` | N2 accepted and ledger hash recorded | literal runbook, scripts/config/contracts/return forms required by basis; exact one-to-one ledger mapping; no historical command identities |
| N4 | Integration owner and terminal author return | accepted N1/N2/N3 fan-in and all candidate bytes | `candidate_packet/PACKET_INDEX.md`, `candidate_packet/FUTURE_OWNER_APPROVAL_REQUEST.md`, `TERMINAL_AUTHOR_RETURN.md`, `returns/N4_*` | N3 accepted | exact index without self-hash cycle, prominently unapproved prospective approval surface with no pending hash placeholder, complete terminal author return |
| M5 | WORKING_ITEMS static validation and freeze | all accepted outputs | `validation/**`, `FROZEN_PACKET_MANIFEST.tsv`, manager records | N4 accepted | deterministic validation, sorted path/size/SHA-256 manifest over candidate packet plus terminal author return, manifest identity |
| N6 | One fresh read-only verifier | exact frozen set, accepted basis, manager validation, old-root inventory evidence | `VERIFIER_RETURN.md` only | freeze accepted; verifier brief sealed after identity exists | PASS/BLOCK over completeness, one-to-one mapping, historical-ID absence, fidelity, hashes/index, containment, non-executability, old-root preservation, STOP gate |
| M7 | WORKING_ITEMS post-verifier closeout | all run-local evidence | manager validation, recomputation evidence, runtime summary, `HANDOFF_STATE.md` | N6 terminal | exact success or blocked closure |

## Escalation points

- Any accepted-source ambiguity or hash mismatch.
- Any evidence that excluded attempt-3 content would be needed as authoring input.
- Missing or non-unique ledger coverage for any executable command/operator input.
- Any historical command identity in completed packet bytes.
- Any candidate executable text not mapped exactly once.
- Any child write outside its target, missing terminal return, inconsistent fan-in,
  freeze mutation, or verifier result other than `PASS`.

Each escalation stops dependent nodes and closes the lineage without
improvisation. Agent 2 children may not delegate.
