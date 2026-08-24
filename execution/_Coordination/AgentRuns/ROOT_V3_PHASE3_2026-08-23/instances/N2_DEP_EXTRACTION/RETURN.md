# N2 return — dependency extraction

- **Terminal result:** `COMPLETE`
- **Role:** bounded Agent 2 ephemeral generalist; role entry
  instruction-asserted; no delegation.
- **Write containment:** eight authorized `_DEPENDENCIES.md` files plus this
  instance return and terminal status only.
- **Basis:** validated N1 commit and owner-authorized merge of current
  `origin/main` into the Phase-3 branch.

## Result summary

Dependency extraction produced nine unique Root-deliverable relationships:
eight gating relationships for the release-pathway objective and one
non-gating validator relationship. The reciprocal local declarations produce
16 table rows across the eight files. Two cross-loop App relationships are
recorded separately as non-gating notice/fan-in, never foreign authority.

```csv
DeliverableID,UpstreamCount,DownstreamCount,NoticeFanInCount,PostSHA256
DEL-02-06,7,0,1,20773668bd8086164c1cd7ee4119d7744d0c2f9a045e546b5565791bc772537f
DEL-02-07,0,1,0,2cececdade0f58deadce326e14926e47dfd862b48694cb77bb57c14c1277e8bf
DEL-02-08,0,1,0,2065317900f62f75a76081ce64593b5cf93dbcb53887f35e1b538c53893ebda9
DEL-02-09,0,1,0,20b6592c76b7a81ce0705a10daa34d7e4ed52730790c71688951c914e61f1a62
DEL-02-10,0,1,0,4fe6d9bc3d2852d3f43b916c848b56e50535af0a15e352b5ebf1ec23bfa9c28f
DEL-02-11,0,1,0,10c25130e663b6d29c25b5e543f4382302082c447ed82da2da68365607234f60
DEL-02-12,0,1,1,f4a635b3c65523dbe8c819f53b92d1889f3dc34a521e0658422d26e1f7ad2998
DEL-04-11,2,1,0,750a0a83e8b93143d6bcf35251c3f716e12c289dc2e0c269f98d33f389279211
```

## Unique Root relationships

| From | To | Type | Gating | Accepted grounding |
|---|---|---|---|---|
| DEL-02-07 | DEL-02-06 | `EVIDENCE_FAN_IN` | yes | DEL-02-07 accepted SOW outputs; applied DEL-02-06 register row and propagated `_CONTEXT.md` fan-in requirement |
| DEL-02-08 | DEL-02-06 | `EVIDENCE_FAN_IN` | yes | DEL-02-08 accepted SOW outputs; same DEL-02-06 accepted fan-in requirement |
| DEL-02-09 | DEL-02-06 | `EVIDENCE_FAN_IN` | yes | DEL-02-09 accepted SOW outputs; same DEL-02-06 accepted fan-in requirement |
| DEL-02-10 | DEL-02-06 | `EVIDENCE_FAN_IN` | yes | DEL-02-10 accepted SOW outputs; same DEL-02-06 accepted fan-in requirement |
| DEL-02-11 | DEL-02-06 | `EVIDENCE_FAN_IN` | yes | DEL-02-11 accepted SOW outputs; same DEL-02-06 accepted fan-in requirement |
| DEL-02-12 | DEL-02-06 | `EVIDENCE_FAN_IN` | yes | DEL-02-12 accepted SOW outputs; same DEL-02-06 accepted fan-in requirement |
| DEL-04-05 | DEL-04-11 | `DOCTRINE_INPUT` | yes | DEL-04-11 accepted SOW `CLM-002`/`AX-002` and accepted DEL-04-05 SOW |
| DEL-05-02 | DEL-04-11 | `EVIDENCE_CROSSCHECK_INPUT` | yes | DEL-04-11 accepted SOW `CLM-002`/`AX-002` and accepted DEL-05-02 SOW |
| DEL-04-11 | DEL-02-06 | `VALIDATION_RELATIONSHIP` | no | Phase-3 steer N2; DEL-04-11 accepted SOW `OUT-004`; DEL-02-06 accepted SOW `OUT-008` |

The two notice/fan-in relationships are:

1. DEL-02-06 sends affected-client requirements to App coordination under
   DEL-02-06 `REQ-032`/`REQ-049` and Propagation Plan section 4.1.
2. App-owned conformance/evidence may enter DEL-02-12 only as a notice/fan-in
   input pending separately accepted App evidence, per DEL-02-12 `OUT-001`,
   `OUT-006`, held-binding row 3, and Propagation Plan section 4.1.

## Source identities and citations used

- Applied deliverable register:
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`,
  SHA-256 `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba`.
- Accepted SCA pointer:
  `execution/_ScopeChange/_LATEST.md`, SHA-256
  `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`.
- Approved `Propagation_Plan.md`, SHA-256
  `abf5ff142b351eef3c16a7d33525f5688db8826f3e0eda58810eb47637645a05`,
  especially section 4.1.
- R7 record SHA-256
  `dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53`.
- Accepted current carrier SOW hashes after N1's ruled one-line status
  transcription: DEL-02-07 `9fb8703bc2a130339d021d90b78648dfaa508de4bedd537b0eb4df756772f1f5`;
  DEL-02-08 `d9871a4a024ff3c48a70a3e6ae4b8eac37ece8873a5e00cbb0ea47dae861e430`;
  DEL-02-09 `e0cf3285f36c4397840d4875641d48bae53c493cff1bc065c3315e6575478176`;
  DEL-02-10 `bfe374aa986718860ebc8b0c877f3a849a25ce0f3246ce33df18d649e30e1b29`;
  DEL-02-11 `abd5dcef7a835bafac3e1dd29d7f7b6771ad0aeb60e4af9c25734bfa2534ab02`;
  DEL-02-12 `62bcfbdd6a20b647f15594fdd35b312d62942f85cf96aedb4aae5db12ea04663`;
  DEL-04-11 `2d5cd066ddee42cd055e4c615078f07d7a91a53b7dddd4da9fa95f1eabc32f2b`.
- DEL-02-06 accepted SOW SHA-256
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`
  and propagated `_CONTEXT.md` SHA-256
  `8b24522fa87c1903a6390c8b87bd8935e7c28c628564da455676c1147666cbf7`.
- Existing accepted DEL-04-05 SOW SHA-256
  `34ea69516d0483e0da40db6e1676564edb20465b4a9d1c7ea7a182346af66fd6`
  and DEL-05-02 SOW SHA-256
  `2b0b3dfd89e64bfcd0ef7aaa9204d456c443eac2dca0f1859a2aab75275a40af`.

## Before and after hashes

| Deliverable | Before SHA-256 | After SHA-256 |
|---|---|---|
| DEL-02-06 | `21261de261dfdbc077cb14df103fd7074b7b8785da58b56318e7d4e06ef0506f` | `20773668bd8086164c1cd7ee4119d7744d0c2f9a045e546b5565791bc772537f` |
| DEL-02-07 | `d7369b6cec97e5682f916fddd17cae6fd9d125f54b49dec88c2d2911e25c5363` | `2cececdade0f58deadce326e14926e47dfd862b48694cb77bb57c14c1277e8bf` |
| DEL-02-08 | `d339932c07937efdf06d32f0b1d587e5d2e05a5fcdf1124fe5e55287cdd4c6c3` | `2065317900f62f75a76081ce64593b5cf93dbcb53887f35e1b538c53893ebda9` |
| DEL-02-09 | `d5483f9f5f16ad4255bbd1741e5e5ffc3b9c78fc2c07faea28a1bc9c9c7409a4` | `20b6592c76b7a81ce0705a10daa34d7e4ed52730790c71688951c914e61f1a62` |
| DEL-02-10 | `9f32b0e4ce08b7f6b212678f244df68e133592da12f1b3673a09946ae5796088` | `4fe6d9bc3d2852d3f43b916c848b56e50535af0a15e352b5ebf1ec23bfa9c28f` |
| DEL-02-11 | `dba4affd0ebdf739ff051bb8ecf29ccfca40acac8357d71410750882e723c5d9` | `10c25130e663b6d29c25b5e543f4382302082c447ed82da2da68365607234f60` |
| DEL-02-12 | `b600948b6db7036c369982d4eae01025fa410e35ce8e2acec8f01af30fda09f4` | `f4a635b3c65523dbe8c819f53b92d1889f3dc34a521e0658422d26e1f7ad2998` |
| DEL-04-11 | `5306b1c89024dc0a1eac68d528b97c01482b295e6b2375c632c226af61ab6b78` | `750a0a83e8b93143d6bcf35251c3f716e12c289dc2e0c269f98d33f389279211` |

## Omitted candidates

- All inter-carrier edges among DEL-02-07..DEL-02-12 other than their explicit
  fan-in to DEL-02-06 were omitted: shared scope, objectives, runtime concepts,
  write loci, or evidence semantics do not establish ordering.
- Potential DEL-04-11 relationships to DEL-05-06, a CI carrier, or other audit
  carriers were omitted: the accepted source set does not declare them.
- App-installer, App-consent-mirror, client-fixture, and similar foreign-loop
  candidates were omitted as strict dependencies. Only the two non-gating
  notice/fan-in relationships above are grounded.

## Validation and protected-byte checks

- All 16 local edge declarations resolve to accepted register IDs; nine unique
  directed Root relationships remain after reciprocal declaration
  deduplication.
- Declared per-file counts equal parsed table-row counts: `PASS`.
- Every Root table row contains an accepted-grounding citation: `PASS`.
- `git diff --check`: `PASS`.
- `validate_candidate_whitespace.py --base-ref HEAD`: `PASS`.
- DEL-02-06 folder diff versus N2 basis contains only `_DEPENDENCIES.md`;
  `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, and all other files are
  byte-identical to the N2 basis.
- Live decomposition, `_LATEST.md`, approved Propagation Plan, SOWs, statuses,
  contexts, references, Task Management state, tools, runtime, projects, and
  SCA evidence are not written by this instance.

## Fresh review

Fresh edge-by-edge review found zero actionable findings. Every direction is
explicit, every Root target resolves, strict and non-gating relationships are
distinguished, reciprocal local declarations agree, App coupling remains
notice/fan-in only, omitted candidates are recorded, and no estimate,
schedule, implementation, activation, pin, hold lift, or foreign authority is
claimed.

## Blockers

- None for N2. Estimates, scheduling, implementation, activation, client
  evidence acceptance, and hold dispositions remain later governed acts.
