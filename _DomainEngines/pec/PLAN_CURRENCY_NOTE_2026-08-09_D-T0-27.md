# PEC standing-plan currency note — D-T0-27

> **Epistemic status: derivative, non-authoritative coordination note.** This
> note records a plan-to-live-source currency delta on the owner-directed
> 2026-08-09 basis at `origin/main`
> `d269f0e04204bc463a11684499213b2283bd28f7`. It is not a ruling, adoption,
> profile, register, receipt, plan amendment, lifecycle act, or substitute for
> any cited source. The live sources cited below govern on every conflict.

## Currency determination

The standing plan's `Parked work and owner gates` section contains this named
follow-on:

> **Named open follow-on:** supersession of the `pec.yaml` profile (the L3
> operation-proposal lane sunsets with the old product); the profile is
> superseded when v2 has shape, and the `_DomainEngines/pec` loop continues as
> the governing development loop meanwhile.

That clause is stale as a statement of open work. The named profile-successor
follow-on is already complete through effective D-T0-27 O-A:

- D-T0-27 records `RULED O-A / EFFECTIVE / ADOPTED / READ_ONLY`, adopts exact
  profile SHA-256
  `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`,
  and says it discharges the separately adopted PEC v2 successor requirement.
- Its exact application identity is PublicationSHA
  `0e47c218c26830a4efeb29eb2d2f3ea99142b987` and EffectiveSHA
  `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`. The effective merge's second
  parent is the PublicationSHA, and the accepted 2026-08-09 `origin/main`
  basis `d269f0e04204bc463a11684499213b2283bd28f7` descends from the effective
  merge.
- D-T0-28 and D-T0-29 are both `APPLIED / EFFECTIVE SUPPORTING AMENDMENT`;
  they change only the conscious live-baseline pins and exact Git whitespace
  treatment described in their records.
- D-PEC-76 is the non-duplicative PEC-local pointer row. It reports D-T0-27
  `EFFECTIVE / ADOPTED / READ_ONLY`, D-T0-28/29 effective, and leaves semantic
  profile authority at Tier-0.
- The live `_DomainEngines/profiles/pec.yaml` bytes reproduce the adopted
  candidate SHA-256 exactly; its parsed fields are `profile_status: ADOPTED`
  and `integration_level: READ_ONLY`. The live validation report is `VALID`,
  `ADOPTED`, with zero errors, zero warnings, and no findings. The Domain
  Engine index likewise identifies PEC as `ADOPTED / EFFECTIVE` at
  `READ_ONLY` through D-T0-27 and PR #459.

Therefore, operators should treat the standing plan clause above as a stale
map delta and use the live Tier-0 decision chain, D-PEC-76 pointer, live
profile, validation report, and Domain Engine index for current posture. This
note deliberately does not edit or supersede the standing plan.

## Exact live-source basis

| Live source | SHA-256 | Fact used |
|---|---|---|
| `_DomainEngines/pec/LOOP_INIT.md` | `a2128e773edeaf4e64fc53f13bedfe6ae4ffdda39d996a7742e88a87eb6515f5` | Live tree wins over stale derivative map claims; deltas are recorded without editing the map. |
| `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | `70f697f78141f6791c310629ad973309b6560b2f551a5ebfb1dabc66a12b2448` | Contains the stale named-open-follow-on clause quoted above and says accepted decisions and the live tree remain authoritative. |
| `_DomainEngines/_DECISIONS/D-T0-27_pec_v2_profile_successor.md` | `04488af489a997fd3edbbe58f32572d15d2ff71fe5bb330469bcb4ed6903c4f4` | Effective successor adoption, exact profile hash, PublicationSHA, EffectiveSHA, and authority fence. |
| `_DomainEngines/_DECISIONS/D-T0-28_pec_v2_profile_live_pin_amendment.md` | `dbd89a45dbe99303e37f3401412b2d45d62215fdd2e87253d85f6452751e64f5` | Effective supporting live-pin amendment. |
| `_DomainEngines/_DECISIONS/D-T0-29_d_t0_28_patch_whitespace_attribute.md` | `2e66a3403d00fb1e6caa828220eb6e283c5f7ebdf03728437481980b16bd0104` | Effective supporting whitespace amendment. |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` | `8eb80613b711508b77590d0fbfd2ad4139205603a6a6f86c2f8dc9525b672afc` | D-PEC-76 pointer status and non-duplicative Tier-0 authority boundary. |
| `_DomainEngines/profiles/pec.yaml` | `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d` | Exact adopted profile bytes; declared `ADOPTED / READ_ONLY` boundary. |
| `_DomainEngines/profiles/_validation/pec.validation.json` | `54bd06c61db9c57597a5c02e242c124f3190f7699d47c9caaadca00b899c6d6c` | `VALID`, `ADOPTED`, zero findings/errors/warnings. |
| `_DomainEngines/DOMAIN_ENGINE_INDEX.md` | `92587f651018a00b0836e5c93dfb5aff3cc8a263fa1e9abfe2d1938558fa55b9` | Live PEC index posture: effective adoption at `READ_ONLY`, with no invocation inferred. |

## Adversarial checks and apparent counterevidence

- Git identity check: the effective merge has exact second parent
  `0e47c218c26830a4efeb29eb2d2f3ea99142b987`; both that publication ancestry
  and the effective merge's ancestry to accepted basis
  `d269f0e04204bc463a11684499213b2283bd28f7` pass.
- Source-drift check: every source in the table matches its `origin/main`
  bytes at the accepted basis.
- Independent validator rerun against a temporary copy of the exact profile
  returns `VALID` with no findings. The validator test suite passes 8/8.
- The profile's leading comments still say "candidate" and "awaiting owner
  ruling." Those comments are apparent contrary evidence but are part of the
  exact bytes later adopted by D-T0-27. They do not override the human ruling,
  effective merge identity, parsed `ADOPTED` field, validation result,
  D-PEC-76 pointer, or live index. This note authorizes no profile-comment
  repair.
- D-T0-27's recorded `Current descendant basis`
  `556ae59a34ac2f06ef924d367843a72ea00d1f37` is a point-in-time identity, not
  the current 2026-08-09 head. The accepted basis used here is the later
  descendant `d269f0e04204bc463a11684499213b2283bd28f7`.

## Authority fence

This note authorizes no profile-mediated or adapter invocation, source act or
source authority, software-workflow write, lifecycle or artifact-fitness act,
release, reliance of any kind, cross-loop duty, or change to any owner gate.
It does not reopen, narrow, or extend D-T0-27, D-T0-28, D-T0-29, D-PEC-76, or
any project tranche.
