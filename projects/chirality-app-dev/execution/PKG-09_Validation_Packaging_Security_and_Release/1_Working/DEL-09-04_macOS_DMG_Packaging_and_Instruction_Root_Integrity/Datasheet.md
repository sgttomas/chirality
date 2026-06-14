# Datasheet: DEL-09-04 macOS DMG Packaging and Instruction Root Integrity

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-09-04 |
| DeliverableName | macOS DMG Packaging and Instruction Root Integrity |
| PackageID | PKG-09 |
| PackageName | Validation, Packaging, Security, and Release |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | CI_CD_CHANGE |
| ResponsibleParty | TBD |
| ContextEnvelope | L |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Release target | macOS 15+ Apple Silicon (`arm64`) unsigned/unnotarized local-builder DMG | `docs/PRD.md` Section 6.2; `docs/CONTRACT.md` Section 1.9; `docs/SPEC.md` Section 19.4 |
| Packaging command | `npm run desktop:dist` from `frontend/` | `docs/SPEC.md` Section 19.1; `docs/PLAN.md` release validation commands |
| Required packaging outputs | `frontend/dist/Chirality-0.1.0-arm64.dmg`; `frontend/dist/mac-arm64/Chirality.app`; `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `docs/SPEC.md` Section 19.1; `docs/PRD.md` Section 12.2 |
| Instruction-root integrity command | `npm run instruction-root:integrity` | `docs/SPEC.md` Section 19.1; `docs/TYPES.md` Section 12 |
| Instruction-root packaged resource requirement | Packaged builds must contain required instruction-root resources and verify integrity before distribution. | `docs/CONTRACT.md` Section 1.3; `docs/SPEC.md` Section 1.1 |
| SDK subprocess packaging posture | Packaged Electron builds must verify that the SDK subprocess/binary can be found and executed from the app bundle. | `docs/PRD.md` NFR-030 and Section 12.8; `docs/SPEC.md` Section 19.4 |
| Source-completeness state | Required instruction-root assets may be incomplete in the current source or packaging state; this remains a P0 readiness gate. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` OI-004; `docs/PRD.md` Section 10.1 |
| PRD source status | `HASH_MISMATCH` treated as source warning only for this run. | `_REFERENCES.md` REF-006; assignment override |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Build platform prerequisites | Node.js `>=20`; dependencies installed in `frontend/` with `npm ci` before validation/package sequence. | `docs/PRD.md` Section 6.2 and CI sequence near Section 12.2 |
| Release scope exclusions | Windows/Linux packaging is out of current release scope unless amended. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW-078; `docs/PRD.md` KG-014 |
| Signing posture | Unsigned/adhoc as scoped; no notarization requirement in current target. | `docs/PRD.md` Sections 6.2 and 7.12; `docs/SPEC.md` Section 19.4 |
| Network/security posture during packaged validation | current shipped Anthropic network guardrails remain in force. | `docs/PRD.md` Section 12.8; `docs/SPEC.md` Section 19.4 |

## Construction

The deliverable consists of packaging changes and evidence artifacts sufficient to:

- run the local validation sequence from `frontend/`;
- build the macOS arm64 DMG with `desktop:dist`;
- prove the app bundle includes required instruction-root assets;
- preserve or emit the latest instruction-root integrity summary;
- verify SDK subprocess/binary executability from the package layout; and
- record any residual blockers, especially source-completeness or SDK packaging issues.

## References

- `docs/CONTRACT.md` Sections 1.3 and 1.9.
- `docs/SPEC.md` Sections 1.1, 19.1, and 19.4.
- `docs/TYPES.md` Section 12.
- `docs/PLAN.md` release validation commands and risk table.
- `docs/PRD.md` Sections 6.2, 7.12, 8.11, 10.1, 12.2, 12.8, NFR-030, KG-014, KG-025.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` entries for DEL-09-04, SOW-030, SOW-072, SOW-073, OI-003, OI-004.
