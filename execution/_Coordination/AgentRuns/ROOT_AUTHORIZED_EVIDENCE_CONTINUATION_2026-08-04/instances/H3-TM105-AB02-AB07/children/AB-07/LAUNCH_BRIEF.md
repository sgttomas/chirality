# Agent-2 sealed brief — TM105 AB-07 store/privacy evidence

ChildID: `H3-TM105-AB02-AB07/AB-07`

Parent: `H3-TM105-AB02-AB07` (`HELPS_HUMANS`, Agent 1)

Construction: bounded ephemeral Agent-2 generalist. The work is novel,
heterogeneous evidence reasoning; no live TASK skill supplies this exact
store/retention/redaction/privacy acquisition method. This child must not
delegate.

## Objective

Execute only acquisition brief AB-07 under the standing TM105-A
preparation-only posture. Inventory current store/delete/migration paths,
content and metadata classes, tamper/truncation/reorder behavior, access
controls, encryption/key-custody evidence if present, redaction reversibility,
and gaps in retention, deletion, legal hold, privacy, incident, and
e-discovery facts. Separate engineering observations from product/legal/
privacy facts and leave every unsupported policy fact `UNKNOWN`.

## Authority and boundaries

- Evidence only; no semantic selection, approved-store choice, retention or
  deletion duration, access-role decision, redaction policy, privacy/legal
  conclusion, contract-candidate drafting, or no-TBD successor.
- Treat current code/tests as implementation evidence, not generic TM105
  semantic authority. Treat H2 and AB-09 as derivative prerequisite evidence.
- Do not infer protected-data classes, legal obligations, approved stores,
  access populations, encryption guarantees, key custody, incident/e-discovery
  requirements, or product acceptability.
- Do not use credentials, access remote providers, run product tests, or
  mutate any evidence store.
- Do not authorize semantics, implementation, client acceptance, lifecycle,
  release, reliance, publication, Git, PR, register, receipt, or notice acts.

## Exact read scope and expected hashes

Resolve `REPO_ROOT` using `git rev-parse --show-toplevel`. Read only this brief
and the following evidence sources; do not discover or read other files:

| SHA-256 | Repo-relative path |
|---|---|
| `380e0c22ca554a604c10d30a3ed49c3fdc79e4806910b80369c8eb88ba0e19a1` | `execution/_Coordination/AgentRuns/ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04/instances/H2-TM105-AB01-AB09/RETURN.md` |
| `f43b4dd8c1165a8318d4c4287036cb3faf2d879e0c9cb540329641e9acbe021b` | `execution/_Coordination/AgentRuns/ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04/instances/H2-TM105-AB01-AB09/children/AB-09/RETURN.md` |
| `fc0dc536f01c39345e6ee195e789fb07ce28f7fd593f9e83dccdcae3ec7c78aa` | `execution/_Coordination/AgentRuns/ROOT_TM105_EVIDENCE_COLLECTION_2026-08-03/OWNER_VENDOR_PLATFORM_FACTS.md` |
| `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | `runtime/packages/contracts/src/events.ts` |
| `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` | `runtime/packages/contracts/src/harness/event-schema.ts` |
| `05cd1eae2a8c911775b00e8957ff9b4141f2072e6f063eaadec9b3bc62b1b99a` | `runtime/packages/contracts/src/harness/transcript-replay.ts` |
| `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | `runtime/packages/core/src/session-store.ts` |
| `28f8bade3372a6b0f1797a0c9623f0ad68f54f4ef2a6dee6638aeaeef20a29fa` | `runtime/packages/core/src/auth-registry.ts` |
| `21ed1bb39afa1a0c773f45f547892182af3c18f7a52c4505895e52924ac513b5` | `runtime/packages/core/src/fs.ts` |
| `f397ac1a54b4af77d5d131b8fed27308b5d24852d5e856c36136c8d3bdb5d592` | `runtime/packages/engine-claude/src/index.ts` |
| `531f69c42c87d799b2b9aecec4bbfb96e2a1210dcd17135542c3483b48a9c208` | `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts` |
| `2025db32a48dc261bb6d0b753cfa99b99a4ad97a85f795a8930cac8af6b3f306` | `runtime/packages/engine-pi-omlx/src/omlx-client.ts` |
| `5d9c1cda16267557ea8ca599109568718fcb7a22b3dcb8f58a67f760fa596b02` | `runtime/tests/session-and-residency.test.ts` |
| `e5880870ef7ee94b90ebef4baf72335bf24073ca35b1d829ead05c3be9ee7b2b` | `runtime/tests/turn-hardening.test.ts` |

The parent resolved authority. Controlling child constraints are K-PROV-1,
K-INVENT-1, K-CONFLICT-1, K-CLAIM-1, K-GHOST-1, and K-WRITE-1/2.

## Allowed tools and write scope

Read-only shell operations (`git rev-parse`, `sed`, `rg`, `shasum`, `wc`) are
allowed only against the exact paths above. Use `apply_patch` to create only:

- `children/AB-07/RETURN.md`
- `children/AB-07/STATUS.json`

No other write is permitted. Do not use network tools, credentials, stores, or
product tests.

## Required return

`RETURN.md` must include:

1. input hash verification and any drift;
2. store/delete/migration path inventory with provenance;
3. content-class and metadata-class inventory;
4. tamper, truncation, reorder, access-control, encryption/key-custody, and
   redaction-reversibility evidence/unknown matrix;
5. testable observed store behaviors distinguished from absent tests;
6. product/legal/privacy/retention/deletion/legal-hold/incident/e-discovery
   facts kept `UNKNOWN` unless directly supported by an attributable primary
   source in the sealed set;
7. explicit conflicts/non-coverage and separately owned evidence actions; and
8. a statement preserving all semantic, implementation, lifecycle, release,
   reliance, publication, Git, and byte-gate holds.

`STATUS.json` must be valid JSON and state child ID, terminal status, input
drift, output path, unresolved policy facts, and no-authority-effect flags.
Do not claim completeness beyond the sealed set.
