# Repair cycle 1 — RF-001 exact evidence bindings

Date: `2026-08-24`

Basis: `8884b143f3d8dbca49756e981e4e20299d55875d`

Trigger: fresh independent `REVIEW-01` returned one `MAJOR`, `RF-001`, because
three packet-unique material evidence bindings were abbreviated. The review
artifacts remain byte-identical:

- `reviews/REVIEW-01/REVIEW.md` SHA-256
  `76596ca1c3bb91d0f8372719c15050a99e584aa722f4c14945e93c2d51d449f9`;
- `reviews/REVIEW-01/RETURN.md` SHA-256
  `fef7e5731d03ed55aabe717c693fc3719af5ad16cb29378378253f0b92b412cf`;
- `reviews/REVIEW-01/STATUS.json` SHA-256
  `f0ce33977a48f499f600d6b74b8ed4e42ef6efaec511a33ebb5e9d5abf91a2d5`.

## Bounded repair

The four affected authored passages now carry the exact root-relative path
and full SHA-256 specified by REVIEW-01:

1. acceptance-005 snapshot:
   `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`,
   SHA-256 `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4`;
2. SCA-APP-008 Carrier Map, in both affected artifacts:
   `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Carrier_Map.md`,
   SHA-256 `72a1b55b5307b6df5131011e30581e323737e95f3bcf85471121481ded25b619`;
3. graceful-stop notice:
   `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-04_ROOT_TM-ROOT-112_ACCEPTED_GRACEFUL_STOP_REPAIR.md`,
   SHA-256 `1029648d039edd3c0449d0bea867853b033cc457a4b1f477c458dd4e127a6ed3`.

## Hash lineage

| Artifact | Pre-repair SHA-256 | Post-repair SHA-256 |
| --- | --- | --- |
| `OWNER_TRIAGE_SHEET.md` | `00a219236ea4c3d7bae518e42c50cb95339b05f123bdf57f803b1726ecae21ea` | `cb82835ddd9730c669e37fd49e0a155a8fb23aa6b789190a3e2bd5b2dcf97cc4` |
| `ELECTRON_DRIFT_DISPOSITION_CANDIDATE.md` | `d3f1e9248b387934e6ce3e539c13a0d6b538a0824cad37e08ceda10c03859b99` | `f9008f3cd2076e38572fc849c749c82aa8afbeec1863353944f721d4a3e9cca0` |
| `STALENESS_AND_CLOSURE_ECHO.md` | `d9167a51c34ee9177cebdcfdf55f04ef2753564d2ff9a5f6488a5c07a50dd762` | `bd43eb746f4bec0a65322641d758b8a6b5780b9e48e168e7cd9ee93a91ab33c4` |

All substantive classifications and options are unchanged. The hypothetical
CSV candidate remains byte-identical at SHA-256
`00f7754c4effe1cbd240976023834b891161fc8781373a63a94ae6fecc2db016`.
No live or closed register byte changed.

## Post-repair gates

- candidate whitespace against exact basis: `PASS`, zero skipped paths;
- Receipt validator: `VALID`;
- Task Management register validator: `PASS`, 13 rows;
- field-aware candidate comparison: `PASS`, exactly 12 changes, all
  `LastReviewed -> 2026-08-24`;
- live register SHA-256:
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`;
- closed register SHA-256:
  `8e75d44ab11b20877f86a3b57e7d27a47f60f0188d71181db120144cab51d1e6`;
- candidate CSV SHA-256:
  `00f7754c4effe1cbd240976023834b891161fc8781373a63a94ae6fecc2db016`;
- `git diff --check`: `PASS`;
- containment: only Receipt 201, this RunID, and the authorized packet root;
- exact source-identity verification and REVIEW-01 immutability: `PASS`.

Outcome: `REPAIRED — READY_FOR_FRESH_REVIEW-02`.
