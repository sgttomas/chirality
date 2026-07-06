# PEC D-PEC-10 rehearsal 01 — the weekly agent intake+triage cycle, rehearsed end to end

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture
> convention). Facts only; no pilot-readiness, correctness, or go-live claim
> (F-PEC-2). The rehearsed instance — not code landing — is what discharges
> obligations (owner direction item 3).

## Basis

- **Authority:** D-PEC-10 O-A, owner-ruled 2026-07-05 in-session ("1. I rule
  `O-A` 2. merge PR #86" — verbatim in the packet's Human-ruling section;
  ruling SHA `9dd310cc3`, the PR #86 merge the owner ruled on). Mechanism,
  obligations WF-1..11, and this rehearsal's design are the packet:
  `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-10_agent_intake_triage.md`.
- **Instance:** fresh scratch DB `pilot-scratch/db/pec-scratch-dpec10.db`
  (D-PEC-06-guarded `npm run seed` demo cast + basis-prep: synthetic project
  `SYN` id 2, roles), served on `127.0.0.1:4899`; **DB deleted after capture**;
  no real data ever existed in it.
- **Data:** synthetic RAIL + MDL documents fabricated by the agent (committed
  under `inputs/` — synthetic, so no D-T0-14 residency question; CLOSED
  unchanged).
- **Actors (WF-8):** agent under its own provisioned person
  `pec-agent@rehearsal.demo` (personId 16, `coordinator`, `is_admin=0`) —
  proposals, refreshes, triage; owner `admin@aurora.dev` (personId 15, screen)
  — every accept and apply. Basis-prep (seed, SYN project, actor provisioning)
  ran script-side as instance setup, not as a WF workflow act.
- **Code under test:** `main` at `9dd310cc3` (PR #82 seam; no pec source
  change in this run).

## What happened (all through the live HTTP API; nothing bypassed RBAC)

| Step | Act | Result |
|---|---|---|
| 1 | Agent filed MDL v1 (IPR-0001); owner accepted+applied | 4 created; apply report identical to dry-run |
| 2 | Agent filed RAIL v1 (IPR-0002) pre-MDL-apply; dry-run showed 6-to-intake; after the MDL apply the agent refreshed → anchor resolved | applied: 1 work item (SYN-R-1 anchored to SYN-D-001), 5 intake items INTK-0001..0005 |
| 3 | Weekly v2, serial: MDL v2 (IPR-0003) then RAIL v2 (IPR-0004), owner accepting+applying each | MDL: 4 update (incl. rev B seed) + 1 create. RAIL: 5 update-in-place (zero duplication among un-dispositioned items — WF-6), **1 OM-3 conflict on SYN-R-4 reported and NOT applied** (WF-9 conflict-for-owner), 1 new intake (SYN-R-7) |
| 4 | Agent triage | INTK-0001 `converted` → **DEC-0001** (decisions arrive via triage — WF-10); INTK-0004 `converted` → **WI-0001** anchored to SYN-D-002; INTK-0002 `parked` (grounds in note); INTK-0003 `duplicate` of INTK-0004 (resolves the OM-3 conflict; statement never rewritten); INTK-0005 (hold) + INTK-0006 left un-dispositioned for the owner |
| 5 | Staleness exercise (WF-7): agent filed MDL v3 (IPR-0005); owner accepted; owner made a targeted screen edit (created revision "Rev B (testing)" on SYN-D-001, superseding rev B — history 230–231); owner's apply refused | on-screen 409 `STALE_PROPOSAL` (basis 226 vs watermark 231); agent refresh voided the acceptance and rebased to 231; owner re-accepted + applied → success |
| 6 | Post-triage re-import observation: agent re-filed RAIL v2 (IPR-0006), **dry-run only**, then withdrew it | 3 update (work item + the 2 un-dispositioned intake items), **4 dispositioned rows would re-land as NEW intake items** → register row D-PEC-15 |
| 7 | Capture | history extracts (agent/owner actor split on every record), exports, this manifest |

## Obligations discharged (packet WF table; no silent trims)

| WF | Status |
|---|---|
| WF-1 RAIL live path | EXERCISED (IPR-0002/0004: v1 + v2) |
| WF-2 MDL live path | EXERCISED (IPR-0001/0003/0005) |
| WF-3 Risk Log | PARKED → register row `D-PEC-14` |
| WF-4 Schedule | PARKED → register row `D-PEC-14` |
| WF-5 Package Tracker | PARKED → register row `D-PEC-13` (no §16 contract exists — verified) |
| WF-6 weekly idempotency | EXERCISED (v2 reports: update-in-place, zero duplication among un-dispositioned) + boundary observed: post-disposition rows re-land → `D-PEC-15` |
| WF-7 interleave/staleness | EXERCISED — forced on screen and recovered (refresh → re-review → re-accept → apply); movers were owner revision acts, history-evented as the packet requires |
| WF-8 own actor identity | EXERCISED — history separates personId 16 (agent: create/dry-run/transition/disposition) from 15 (owner: every accept/apply) on every extract |
| WF-9 disposition audit-to-source | EXERCISED — new (SYN-D-005/006, DEC-0001, WI-0001), update (v2 reports), intake (`[item_id]` verbatim prefixes), conflict (IPR-0004 SYN-R-4 entry + resolution recorded on INTK-0003's disposition note) |
| WF-10 decisions-as-triage | EXERCISED — INTK-0001 `converted` → DEC-0001; no decisions import assumed |
| WF-11 repeatable cycle | EXERCISED at the two-document scope; runbook v1.2 section authored (`IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md`); five-document cycle rides D-PEC-13/14 |

## Observations recorded as fact (deltas feed rows, not prose fixes)

1. **Anchors resolve at dry-run time**: a RAIL proposal filed before the MDL
   apply sees no anchor; the refresh after the apply resolved it. Serialization
   applies across contracts, not just within one (runbook v1.2 step 2).
2. **Post-disposition re-import re-lands dispositioned rows as new intake**
   (IPR-0006 observation dry-run: 4). Register row `D-PEC-15` carries the
   convention/design question; runbook v1.2 step 5 documents the interim rule
   and supersedes v1.1's pre-repair "never re-import a full RAIL file".
3. **UI note (cosmetic, no row):** proposals are row-inline controls; there is
   no detail page — the owner's "not able to open it" moment. `detail` toggles
   the report inline.

## Artifacts (SHA-256)

```
670e9a1ce3df6103b40a79e8b74848654f76f72fc137b67d9bd084ac7f54e16f  inputs/mdl-syn-v1.csv
4dab45cd357c8e133db6f3ca16c565f6ab12793da067307050816352cd9acb10  inputs/mdl-syn-v2.csv
f0e6892a1c8ce50360bf04f302e6d497b00e1efd273a8912c82a8938ae9f773c  inputs/mdl-syn-v3.csv
b069e00c0cb02cd736052ef94423e8743fe509ac9aaec124ea4257525b21536c  inputs/rail-syn-v1.csv
a622354644d51ebcedc227730440e642203350ddcde9c72cb22ce33005f3a38b  inputs/rail-syn-v2.csv
4bce67eb53701a5f8cd67a84374dcce66598a591f2668d2e293a2c437b0883e6  artifacts/00-agent-login.json
1116523b9770fec0a12dd0268cb738342479e00a32682784029e2ca99dfd4bb7  artifacts/01-propose-mdl-v1.json
84461139ff7cea7a01f1a5edb77b0021a5cc62a62df9e6e7b0f29a1ca3bdc41a  artifacts/02-propose-rail-v1.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  artifacts/03-intake-queue-before.json
46fca667cf2954937ccf0cdd99af79433ad7b361ece05408f22659de381e8edc  artifacts/04-ipr0001-post-apply.json
9b9df8de86bef52f7f4aa1e6a0bc13c6634e193dadbaacca9d6d82cdd945dd16  artifacts/05-ipr0002-refresh.json
d5a40c258649e963c6d424546ce18d90d5284d1fadbb10e2158f910081cab08d  artifacts/06-ipr0002-post-apply.json
25a187c49b3aefa4f07b7cc0ee4748690f984f4f799cab475c5449947fdff262  artifacts/07-intake-queue-after-v1.json
4a887fc25bd5d7f915b6f07e7f1c21a5b8fde9621ccd8f63926f66b5d55ccd93  artifacts/08-propose-mdl-v2.json
dd393d0863c7221ee3944cb5b94047caa85d5070a1b822a553d2bf47922a0a3f  artifacts/09-ipr0003-post-apply.json
97e0cd0178d82260172316b09b37ee55c889fa641ef377dee4ddcdb62bc50d0a  artifacts/10-propose-rail-v2.json
ee5968ad660b5799bf40e4b61c3e606c4dc18ed83d094a81b4bb7a8b96f7a063  artifacts/11a-intk0001-open.json
d150a0556e1c631fc5ba1bfe9c1bca2422f893be40f7c405748577fd1422776c  artifacts/11b-intk0001-converted-decision.json
a6fb1be1a16e3c64d2b70bdd7f1cf645f3374dd40fee89e04d420e013b092a8a  artifacts/12a-intk0002-open.json
5777eb1b87b40a4d0cb20cfe03148a513107fe564a26fec61476052cf5f12a55  artifacts/12b-intk0002-parked.json
205def284dcc88d83f3ce6a857ebdead5f8bff34733ee89110bd26c7b6f8c734  artifacts/13a-intk0003-open.json
174b916e18d826587e236a2cbde3fbf63ee326020bc099e12a6111826e9d818c  artifacts/13b-intk0003-duplicate.json
30c78d035bdd5b21182b88bab17d0c5f9e28f68775b5c99338651e258413c338  artifacts/14a-intk0004-open.json
f4e6a562423a451d1b0408c5dfab3dd585898f7fb215bdb183010c8312c5272d  artifacts/14b-intk0004-converted-workitem.json
524262b8a0d3487f058b036035dd1ec12c2c10e8d0918f37d9d25b13a48794d3  artifacts/15-intake-queue-after-triage.json
dd90a1a07ec62006887d013e06b375e5801e0b8a47df1c8a670b400c3ff53d90  artifacts/16-propose-mdl-v3.json
2b273277be617ea18557d2d272761793d11c2fb95b247c213d9bb1704555f4b1  artifacts/17-ipr0005-stale-accepted.json
16a3da6a7bba4173e3a769ebd85dbe1ac04a79e73531bb5c3aeffcf1f1e6d32c  artifacts/18-ipr0005-refreshed.json
81811f0e3359adb423f8a70f07ab4c18350339db51b55948d697df513d63a10c  artifacts/19-ipr0005-post-apply.json
d938723149e0e6c7c93c7f47c6e22394cf2b29f1e0637ae4f6d6207ac24b5761  artifacts/20-observation-rail-reimport-dryrun.json
2f5d8653e5ab16c5949b2660a76934f2c22bfe4ad63892f0f09ca7a5269cc58e  artifacts/21-ipr0006-withdrawn.json
f50a38d1cde91a340bfa2f1ab27fa1512488c62779bb3aa2eb0690af05c085a9  artifacts/22-hist-dec0001.json
05781ab69fee975d9bfc740b46e83b3e6e4f16ab7eba5d3992e5c6f557f35e89  artifacts/22-hist-intk0001.json
7a3d93c8680916498e2e8d56f93e48b90b94647024287f90eccfca82c6948585  artifacts/22-hist-intk0002.json
ce7c0d73285db8651a0da57754105859361feb719be031107692b01faa858c4e  artifacts/22-hist-intk0003.json
001e0d50ab4d494ee0fa8c75811348812767f55578cf077a77bd0548df96afdb  artifacts/22-hist-intk0004.json
fbc914c8bd214b4b82224c3fa1b33c050dec55d844013d495c77d01c769de913  artifacts/22-hist-intk0005.json
3f4aa2a02cf647c6d1198509b2bfa374dd39587c61de220ad20b123973cd83ff  artifacts/22-hist-intk0006.json
a3615ceb89799d4707280be1a933a9ea3028c883b94c2fb1d48fcb5af2b00379  artifacts/22-hist-ipr0001.json
adc3223fe650422848e9a8f4599d023ec6be5c792468d742bc166a4abe77f229  artifacts/22-hist-ipr0003.json
b66ba8514c9ad93bfe4ac4e5e484fe80cc7f0e2e5095547d1383c9620807c00b  artifacts/22-hist-ipr0005.json
af5dbd36b6d5332654ba58856b473aea97e3ddc65b56ad5784e51fcb05e90caa  artifacts/22-hist-synd001.json
4f81692e189f01be1bf7cca2438c4005a795c2ee1ced7ac3347221e5e46c8c0e  artifacts/22-hist-wi0001.json
09811f77145301e619858f741a453d33c8ab401400f6156471bece8bbe3eee66  artifacts/23-hist-rev16-superseded.json
d7f9249289a2142da554862424655aa3728318daa7a66e7e41e916351c62e340  artifacts/23-hist-rev18-owner-edit.json
b4d82463521ddc26c2d1f45f2e4c246be79e9eaeb6c6cb0907bdaf42a9058996  artifacts/24-export-intake.csv
5f4a484cd96d662fb9a80832192013b7966066c8c48d97cb420df54435b22c90  artifacts/24-export-mdl.csv
e926c7d01b1881a0872b6cb8029afc76fb7a965bb1f7172b0a595bff0ff8e1ca  artifacts/25-proposals-final.json
```

Mirror artifact (non-authoritative, batch form disclosed):
`_DomainEngines/proposals/pec/OP_2026-07-05_DPEC10_rehearsal_IPR-0001-0006.md`.

## Boundaries respected

Scratch/demo basis only; DB deleted after capture; the D-PEC-01 surfaces
(`pec-scratch-import.db`, backups) untouched. No `force` anywhere. Accept,
apply, and `force` stayed human (owner personId 15 on every accept/apply).
No pec source change; no approval records via conversion; no tier-0 act; no
real instance content (synthetic data throughout; D-T0-14 CLOSED untouched);
no pilot-readiness or go-live claim. The 272-item real-data triage run remains
gated on the owner's visibility-basis confirmation (packet Scope note 4).
