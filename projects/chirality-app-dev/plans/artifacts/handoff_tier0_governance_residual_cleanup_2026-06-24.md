# Hand-off to tier-0 / DOMAIN_ENGINE — governance-record residual cleanup

**From:** chirality-app-dev governance loop (WORKING_ITEMS persona)
**To:** tier-0 root governance (`AGENT_DOMAIN_ENGINE` / DOMAIN_ENGINE persona) + CHANGE
**Date:** 2026-06-24
**Type:** Advisory hand-off (NOT a ruling, NOT a tier-0 edit). App-dev cannot edit `{REPO_ROOT}/_DomainEngines/**`.
**Origin:** readiness-assessment finding 6 (stale-state residuals) + finding 7 (event-count drift).

## Why this is a hand-off and not a fix

Every residual below lives under `{REPO_ROOT}/_DomainEngines/**` (or the piping repo), which the app-dev
loop is fenced out of. Editing them would itself violate the tier boundary this assessment is about. Each is
verified cold against source on 2026-06-24 with exact line anchors so tier-0/CHANGE can apply the fix
directly. The **content** that landed (profile ADOPTED, FM-01..04 applied at `77a327727`) is accurate — the
problem is that the canonical records the downstream loops read are **internally contradictory** about it,
which is a real misread risk for any loop that binds against them.

## Residual 1 — `RULINGS_PUBLISHED.md` self-contradicts on adoption

- **`_DomainEngines/RULINGS_PUBLISHED.md:48-50`** says: *"The profile-schema validator (TOOLMAKER) is built
  and the profile passed → VALIDATED; the owner then ruled Gate 2 (VALIDATED → ADOPTED) on 2026-06-21 →
  ProfileStatus ADOPTED. Tier-0 adoption is complete."*
- **`_DomainEngines/RULINGS_PUBLISHED.md:56`** says: *"Profile remains DRAFT (not VALIDATED — validator not
  built; D-T0-06) and not ADOPTED."*
- **Fix:** delete or supersede line 56 — it is a stale pre-validator sentence contradicted by lines 48-50 and
  by the live validator (`tools/validation/validate_domain_engine_profile.py`, 8/8 passing) and report
  (`_DomainEngines/profiles/_validation/open_pipe_stress.validation.json`, VALID / 0 errors).

## Residual 2 — profile YAML header contradicts its own status field

- **`_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:1-10`** (header comment) says: *"DRAFT (NOT
  validated, NOT adopted) … Nothing here is adopted. No deterministic profile-schema validator exists yet
  (TOOLMAKER handoff)."*
- **`_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:18`** says: `profile_status: "ADOPTED"` (with a
  correct inline note that the validator passed and Gate 2 was owner-approved).
- **Fix:** update the header comment to match the authoritative `profile_status: ADOPTED` (validator built and
  passed). Consider whether the filename's historical `.DRAFT` suffix should be retired or annotated; line 18
  already notes "filename retains historical .DRAFT; profile_status is authoritative", so at minimum the
  header prose should stop asserting the opposite.
  *[Executed 2026-07-01 per D-GOV-06: header reauthored and the file renamed to
  `_DomainEngines/profiles/open_pipe_stress.yaml`; the anchors above cite the pre-rename file.]*

## Residual 3 — `DOMAIN_ENGINE_INDEX.md` contradicts itself and mislabels the FM diffs

- **`_DomainEngines/DOMAIN_ENGINE_INDEX.md:7`** says: *"No profile is ADOPTED. No decision is ruled."*
- **`_DomainEngines/DOMAIN_ENGINE_INDEX.md:15`** (table) says: `open_pipe_stress … ADOPTED (validated +
  Gate-2 adopted 2026-06-21)`.
- **`_DomainEngines/DOMAIN_ENGINE_INDEX.md:29` and `:43`** label FM-01..04 as **"NOT applied"** / **"not
  applied"**, though `RULINGS_PUBLISHED.md:41-42` records them applied + pushed at `77a327727`.
- **Fix:** the line 7 blanket "PROPOSAL / unratified / no profile ADOPTED / no decision ruled" banner is now
  false for the adopted profile and the 8 ruled D-T0 decisions; scope it to what remains unratified. Update
  the FM diff labels at :29/:43 from "NOT applied" to "applied at `77a327727`".

## Residual 4 — ruling-SHA back-stamp (K-AUTH-2)

All 8 tier-0 rulings (D-T0-01..08) plus the cross-tier records carry **"Ruling SHA: TBD (binds at CHANGE
publish)"** despite being on `origin/main`. The substance is committed, but the SHA the binding rests on is
unrecorded.

- **Fix:** at the next CHANGE publish, back-stamp the ruling SHAs (the FM/ruling publish commit is
  `77a327727`; the D-T0-04 ruling text was committed at `6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45`). Then
  ratify root `docs/CONTRACT.md`, which `RULINGS_PUBLISHED.md:45` still marks DRAFT-pending-ratification.
- **Note:** the app-dev-side records mirror this (`D-APP-44_RULING:7` carries the same "TBD"); app-dev will
  back-stamp its own once tier-0's binding lands, to keep attribution consistent.

## Residual 5 — the "immutable" BRIDGE snapshot was edited post-closure (K-SNAP-1)

The `_DomainEngines/bridge/BRIDGE_2026-06-21_tier0-prep/` snapshot was edited after its declared closure,
which deviates from the K-SNAP-1 immutability convention.

- **Fix:** stop editing the closed snapshot; land any further state in a **new** dated snapshot with a
  `_LATEST` pointer, per K-SNAP-1. (Advisory — tier-0's convention to enforce.)

## Residual 6 — event-vocabulary count is stale in the keystone definition (finding 7)

The Flow-A contract **keystone** is the harness event vocabulary. The live source
`frontend/src/lib/harness/event-schema.ts:3-46` enumerates **43** types (`runtime.mirror.error` at `:46` is
the 43rd); the canonical DEC-041 definition says **42**.

- **`projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md:611`** — *"the ~19 dependency-free
  harness lib files: **the 42-type event vocabulary** …"* (piping repo; app-dev cannot edit).
- **App-dev side already fixed:** `plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md` now
  reads 43 with a dated correction note (D-APP-46 hygiene).
- **Fix (piping/tier-0):** reconcile DEC-041's "42-type" to **43** before any Flow-A version is pinned, so the
  version pins against the true keystone count.

## Suggested ownership

| Residual | Owner | Action |
|---|---|---|
| 1, 2, 3, 5 | tier-0 / DOMAIN_ENGINE + CHANGE | Edit the `_DomainEngines/` records as above |
| 4 | tier-0 + CHANGE | Back-stamp ruling SHAs at next publish; ratify root CONTRACT |
| 6 (piping half) | piping loop | Reconcile DEC-041 "42-type" → 43 |
| 6 (app-dev half) | app-dev (done) | Corrected in the bridge artifact 2026-06-24 |

No fence, scope, lifecycle, release, professional, or SHA claim is created by this hand-off. It is a list of
verified record-consistency fixes for the tiers that own the affected files.
