# D-APP-97 — Release preparation authorization

Status: `RULED — C1`

DecisionID: `D-APP-97`

Date: `2026-08-17`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Exact owner ruling

```
**C1 — Release preparation authorized.**

The release-preparation phase deferred by D-APP-56 for the R4-P49 claim family is authorized, for the standalone Chirality Desktop target at its current product identity. Executable scope: DEL-09-04 DMG/dist packaging and the login-time `RunAtLoad` LaunchAgent path; the packaged-SDK proof; DEL-09-05 CI artifact and release-verification workflow, including reactivation of `.github/workflows/desktop-release-template.yml.disabled` as an unsigned-artifact workflow; DEL-09-06 network, key-attachment, and renderer security checks over the packaged artifact; and the DEL-09-04 release-quality premerge row. PARTIAL R4-P49 assessments in PKG-09 become open engineering items, not deferred ones.

Fences unchanged: F-APP-2 continues to fence signing, notarization, and distribution — artifacts are unsigned and local/CI-only; APP-HOLD-1 unchanged; no release authority, lifecycle advancement, reliance, or professional-approval effect. Packaging identity may later be revisited under the D-APP-87/91 direction; that rework is accepted and needs no reverification now. Where a packaging step requires host execution, run it under the host-capability paragraph. Update the PKG-09 `_STATUS.md` Remaining items from "deferred to release preparation" to open scope and note the ruling in the DEL-09-04/05/06 History.
```

## Owner act recorded, not a ruling

```
**Owner act, for the record (not a ruling):** the owner-machine daemon deploy remains an owner act; it will be performed from a rebuilt artifact produced under C1 and reported back for DEL-09-04's Remaining item then. Do not act on it.
```

## Effect

The named PKG-09 scopes become selectable engineering work in the next
iteration. No C1 engineering, owner-machine deployment, signing, notarization,
distribution, lifecycle, reliance, or release act occurs in this recording
tranche.
