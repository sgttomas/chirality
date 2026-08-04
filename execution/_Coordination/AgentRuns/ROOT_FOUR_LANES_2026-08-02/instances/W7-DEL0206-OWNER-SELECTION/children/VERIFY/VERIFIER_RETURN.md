# W7-VERIFY terminal return — attempt-2 owner-selection refutation

- Runtime identity: `/root/w1_del0206/w7_verify`
- Parent runtime identity: `/root/w1_del0206`
- Form: genuinely fresh read-only ephemeral Agent 2 generalist
- Package: `PKG-02` / `DEL-02-06` only
- Candidate posture: `DERIVATIVE_NONAUTHORITATIVE_DECISION_SUPPORT`
- Verdict: `RETURN_TO_MANAGER`

## Declared-input and candidate identity result

All `42/42` launch-declared files were read in full with bounded non-shell file
reads. Every declared SHA-256 reproduced exactly; there were no missing bytes
or hash mismatches. No directory was discovered or read. No attempt-1 semantic
artifact, return, or status was read.

The frozen attempt-2 candidate is exactly its three semantic files plus its
terminal return/status:

| Candidate member | Reproduced SHA-256 |
|---|---|
| `OWNER_SELECTION_SLATE.md` | `b8d7d7cbfd92a15ca4144967ce7aaf3ec5683aef7a91ae9ff872e7ad57a8f03d` |
| `OWNER_SELECTION_MATRIX.csv` | `d13efba666bdf64c8b4687bfae49bcc474c07d845d2f698698873c7a37d3998b` |
| `SEMANTIC_PATCH_PLAN.md` | `eefde51dce7a2e1a384a60ed152ff315365974d32cae64fdf1bf67cdf52849a1` |
| `AUTHOR_RETURN.md` | `7beff43c1db6f92b6eff85b889f4dd11f4bcf59cafcd397f7f111c6b655d8769` |
| `STATUS.json` | `9fbee3ae3f4e919d5d08e34d9e5755fd5d4c5958f85b30f293c34484ea8a0378` |

The other declared-input identities also reproduced exactly: verifier launch
`f8f96df356cc746188c7ff9fa74e1cfaac9e78880c8690430f87add17df73063`;
original author launch
`cc29413761180676154d702b58d6c92b04dbab4b7f008922689fd86dae092f9a`;
attempt-2 launch
`8c31a6db290be98052d834952cb50c02ec6134ff1ca9f5232da0629b65a21aab`;
and all 34 original-launch basis identities, including W7 manager launch
`307598058d168361afa4b8ff3d8dd7273d502d631bab35768bdf301b7e635a13`,
V20 plan/graph
`6b8f471bccf1f4d1d7fcf50dd731176755b729dc3fe795ae5edd5d0ca11b6b0c` /
`0c98f27efee591ebd3faa04f4883e1ca4c2cce23a7d7088716130243f78d5b4b`,
Scope of Work
`dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`,
accepted packet, N0-N6, W6, and W6-R1 at every hash enumerated in the sealed
original launch.

## Structural and semantic coverage

- Matrix: exact eleven-column header; `27/27` unique rows in the required
  order (`D1-D9`, `TBD-001..TBD-016`, `CENSUS`, `COMPAT-DELTA`); every record
  has eleven fields.
- Options/recommendations: `54/54` stable row-local unique option identifiers;
  `27/27` recommendations name an exact listed option and say
  `non-authoritative decision support`.
- Patch mapping: `54/54` identifiers occur exactly once. Each individual row
  names a future versioned-candidate path, heading/placeholder, dependencies,
  reruns/refutation, and a no-effect fence.
- Evidence grounding: all matrix evidence-reference/hash pairs align with the
  accepted basis. The 27 recommendation rationales are supported within the
  stated candidate/non-authoritative posture. The N2 five-row census and the
  compatibility-delta-if-adopted condition are preserved exactly.
- Slate: D1-D9 recommendation/alternative/consequence coverage is `9/9`; TBD
  summary coverage is `16/16`; the response template contains placeholders
  for all 27 rows, contains no completed owner token, and says silence is not
  acceptance.
- Text shape: all five candidate members are valid UTF-8-compatible text with
  LF endings, exactly one terminal LF, no CRLF, no NUL, and no surplus terminal
  blank line.

## Required-check results

| Check | Result | Basis |
|---|---|---|
| 1. `42/42` hashes and exact candidate identity | `PASS` | All declared identities reproduced; rejected attempt 1 was not consumed. |
| 2. CSV header, order, uniqueness, two options, recommendation shape | `PASS` | `28` records including header; all widths `11`; `27/27`, `54/54`. |
| 3. Rationale/evidence support | `PASS` | All cited accepted references/hashes align and support the bounded recommendations. |
| 4. Slate coverage and exact response grammar | `FAIL — MATERIAL` | The grammar admits mutually contradictory census tuples and says either named option may be chosen; see `W7V-F01` and `W7V-F02`. |
| 5. Deterministic future patch mapping | `FAIL — MATERIAL` | Individual mappings are complete, but no allowed-tuple/coherence rule prevents contradictory dispositions from being inserted into separate placeholders; see `W7V-F01`. |
| 6. N2 census and conditional compatibility delta | `PASS` | Exact five-row N2 result retained; `DELTA` remains conditional on later recovery-spec adoption. |
| 7. Foreign ownership | `FAIL — MATERIAL` | Current prose recommends PEC retention/routing, but the selectable grammar includes a Root PEC classification option; see `W7V-F02`. App, Tier-0, and Piping current no-effect fences otherwise pass. |
| 8. Derivative/no-effect boundary | `PASS` | No adoption, current-byte edit, implementation/check, dependency, SCA/decomposition/PRD, Task Management, lifecycle/release/reliance, Git/PR/merge/notice, or foreign-loop effect occurred. |
| 9. UTF-8/LF/CSV shape | `PASS` | Strict byte and CSV checks passed. |

## Findings

| ID | Class | Exact locus | Claim and refutation | Accepted evidence reference/hash | Required disposition |
|---|---|---|---|---|---|
| `W7V-F01` | `MATERIAL` | `OWNER_SELECTION_SLATE.md`, “How to use this slate,” “Stable TBD/OD6 recommendations,” “Cross-cutting rows,” and “Exact response grammar”; `OWNER_SELECTION_MATRIX.csv` rows `TBD-005`, `TBD-013`, and `CENSUS`; `SEMANTIC_PATCH_PLAN.md` mappings `TBD-005-A/B`, `TBD-013-A/B`, and `CENSUS-A/B`, plus “Package-wide checks” | The slate says the accountable human may choose either named option and the response invalidation rule rejects missing/unknown/placeholding/hash/signer defects, but it defines no cross-row consistency rule. It therefore admits contradictory complete responses such as `TBD-005-A` (accept the exact N2 census) with `CENSUS-B` (defer it), or `CENSUS-A` (accept N2, including Piping `NOT_AFFECTED`) with `TBD-013-B` (retain Piping unresolved). The patch plan deterministically inserts those selections into different placeholders in the same future census candidate but supplies no allowed tuple, equality constraint, precedence, or mandatory contradiction rejection. A structurally valid owner response can therefore produce semantically contradictory future bytes, defeating deterministic compositional patching and exact response grammar. | `clients/N2_CLIENT_CENSUS.md` `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52`; `clients/N2_RETURN.md` `7f4d2aefccf289bb9b26fbde1cc84aaa66a0436dbd1543cb12b8d5718ca49d64`; `handoff/OWNER_GATE_HANDOFF.md` `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`. These establish one exact five-row census and keep its acceptance owner-gated. | Return to the author/manager. A new candidate must define the exact allowed cross-row tuples (or eliminate duplicated choices), make contradictory tuples explicitly no-effect, and carry the same rule into response validation and future-patch assembly/refutation. The verifier performs no repair. |
| `W7V-F02` | `MATERIAL` | `OWNER_SELECTION_SLATE.md`, “How to use this slate,” row `TBD-011`, and “Exact response grammar”; `OWNER_SELECTION_MATRIX.csv` row `TBD-011`; `SEMANTIC_PATCH_PLAN.md` mapping `TBD-011-B` | The package correctly recommends `TBD-011-A`, but it simultaneously says the accountable human may choose either named option, exposes `TBD-011-B: Root declares PEC not affected` in the exact global response grammar, and maps that choice into future semantic bytes. Calling B a rejected authority-expanding alternative and requiring later refutation does not make the present selection grammar authority-safe: the grammar's stated invalidity conditions do not reject B, while the accepted evidence says Root may only preserve `UNRESOLVED` and route a PEC-owned ruling. This is an ambiguous foreign-authority boundary and can also conflict with `CENSUS-A`, which requires PEC `UNRESOLVED`. | `clients/N2_CLIENT_CENSUS.md` `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52`, finding `N2-F-001`; `integration/OPEN_ITEM_MAP.md` `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf`, row `TBD-011`; `handoff/OWNER_GATE_HANDOFF.md` `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`. All require PEC to remain `UNRESOLVED` until a PEC-owned ruling and forbid inferred PEC work, dependency, classification, or veto. | Return to the author/manager. Root-selectable alternatives must remain within retain-unresolved/route/defer/no-current-effect authority, or any PEC disposition must be moved to a separately PEC-owned exact instrument. The response grammar and patch plan must reject any Root classification of PEC before future semantic bytes can be produced. The verifier performs no repair. |

Finding totals: `MATERIAL 2`; `MINOR 0`; `OBSERVATION 0`.

## Derivative, no-effect, and containment posture

This verification is read-only semantic/static refutation of derivative
decision support. It adopts no option, edits no accepted/current candidate,
integration, or handoff byte, and performs no implementation, executable or
runtime/software check, client/project/profile/check write, dependency act,
SCA/decomposition/PRD or Task Management act, lifecycle/release/publication/
issuance/reliance act, Git/PR/merge/notice, or foreign-loop act.

Tools were limited to bounded non-shell file reads, SHA-256, UTF-8/CSV/text
parsing, and `apply_patch` for this exact return. Shell, shell-backed commands,
network, delegation, repair, and Git were not used. The only write is this one
regular non-symlink `children/VERIFY/VERIFIER_RETURN.md`; the manager alone
owns `STATUS.json`.

`RETURN_TO_MANAGER`
