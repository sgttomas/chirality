# App Ruling — Joint Pi G1-B TM-APP-039 / TM-ROOT-106 Disposition

Status: `RULED — JOINT DISPOSITION RECORDED`

Date: `2026-08-03`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

Related App row: `TM-APP-039`

Related Root row: `TM-ROOT-106` (coordination only; Root retains authority)

## Owner-side verification before adoption

The owner stated:

> Owner-side verification performed before adoption: all seven
> CURRENT_G1B_HASHES independently recomputed against committed main
> 88e7590d3 — exact match; drift confirmed on exactly adapter/package_json/
> package_lock; the four remaining pins held.

## Exact owner ruling

The owner adopted the following verbatim:

```text
RULE JOINT_PI_G1B_TM_APP_039_TM_ROOT_106_V1

PIA-U20=AMEND_NO_SPLIT_CURRENT_HASH_SET
PIA-U21=AMEND_NO_SPLIT_CURRENT_HASH_SET_FRESH_INSTALL
PIA-U22=AMEND_NO_SPLIT_EVIDENCE_ONLY_ELECTRON_SEPARATE_AUTHORITY
PIA-U23=AMEND_NO_SPLIT_CURRENT_HASH_SET_POST_REPAIR
PIA-U24=DEFER_WORK_UNITS_NO_MODEL_OR_CREDENTIAL_AUTHORITY
PIA-U25=AMEND_NO_SPLIT_RELEASE_EVIDENCE_ONLY_NO_DISTRIBUTION

CURRENT_G1B_HASHES:
adapter=dd333f02d092dad05d15fb0936fb00f48ee89f75ec530bcfb74db32468f6f728
runtime_host=2e02f592e7e8a6c0008a50cb427044d95aa908e6276b6a9cd8bfe6a1dce248c8
package_json=1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53
package_lock=5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56
proof_launcher=7354e0af73f40e308a5204fe04621a4db0c6e68c964065bb1f029d0aeec5674f
supply_verifier=912a07d5db0d574c3de3acd69898b6567612fbc456807902b83c0a5c38165b7e
pi_notice=0195b5ce8b7be8b6bff6de3e50f6a38b3d9d4919c075e7c93ca8118b7e866328

TM-APP-039=RESOLVED_BY_DECISION_AFTER_APP_DECISION_RECORD
TM-ROOT-106=CONTINUE_G1B_VALIDATION_ONLY_KEEP_OPEN
ROOT_G1B_TARGET=REFRESH_AND_REINGEST_REQUIRED
PIA-U30=HELD_NO_DISPATCH
ELECTRON_43_2_0=NO_SUPERSESSION_SEPARATE_APP_AUTHORITY_REQUIRED
D_APP_72_AND_SCA_APP_002=REMAIN_OPERATIVE
NO_WORK_DISPATCH_NO_RELEASE_NO_RELIANCE_NO_GIT_EFFECT
```

## Exact owner additions

The owner added the following in the same ruling:

> 1. ROUTED_NOTICE_TO_ROOT=REQUIRED_IN_CLOSEOUT. The joint disposition's Root
> side (TM-ROOT-106 continuation, G1-B target refresh and re-ingest) has no
> carrier without it — App does not write Root's register. Ship a routed
> coordination notice to Root's surface carrying this ruling, the amended
> current hash set, and pointers to the run's validation evidence.
> Coordination, not authority; Root acts under its own instruments.

> 2. GIT_CLOSEOUT=AUTHORIZED, superseding the block's NO_GIT_EFFECT line for
> closeout purposes only: commit the untracked derivative run package, the App
> decision record, and the routed notice on this session's branch and open the
> PR. Merge remains my gate. The evidence must reach committed main — Root's
> side of this ruling and the coming selection packet both consume it.

> 3. APP_DECISION_RECORD=AUTHORIZED — transcribe this ruling as the App
> decision record; TM-APP-039 then closes per the block.

> 4. ARCHITECTURE_SELECTION=PACKET_REQUIRED. No A/B/C ruling is given here.
> Prepare the separately governed selection packet (next free decision ID) per
> the D-APP-90 rider — the resume and fresh-verifier preconditions are now
> satisfied — presenting A, B, and C with the comparative evidence and your C
> recommendation with its rationale (six-slot alignment with exact U; A's
> unmeasured target-awareness exposure, which stays NOT_YET_MEASURED with no
> zero inference; B's extraction-heavy MCI). Present it decision-ready; the
> selection is mine to make in that packet.

## Ruled semantics

- PIA-U20, U21, U22, U23, and U25 are amended without split exactly as
  recorded; U24 is deferred and grants no model or credential authority.
- No PIA unit is accepted for execution or dispatched by this record. Exact
  App sealed briefs and their later owning gates remain required.
- TM-APP-039 is eligible for App TASK_MANAGEMENT closeout after this decision
  record exists. This file does not edit the App Task Management register.
- TM-ROOT-106 remains open. Root target refresh/re-ingest and any Root register
  disposition remain Root-owned.
- PIA-U30 remains held and undispatched.
- Electron `43.2.0` creates no supersession. D-APP-72 and SCA-APP-002 remain
  operative until a separate App authority act.
- U25 remains release-evidence-only and grants no signing, notarization,
  publication, distribution, or release authority.

## Closeout-only Git supersession

The exact `NO_WORK_DISPATCH_NO_RELEASE_NO_RELIANCE_NO_GIT_EFFECT` line remains
the substantive ruling fence for work dispatch, release, reliance, and
non-closeout Git effects. Owner addition 2 supersedes only its Git clause for
the bounded closeout: commit the named derivative run package, this App
decision record, the authorized Root notice, and the coming selection packet/
register row on the session branch and open a PR. Merge remains the owner's
gate. This record performs no Git action.

## No-effect boundary

No App or Root Task Management register is edited by this record. No work is
dispatched; no product/source, dependency, PRD, decomposition, SCOPE_CHANGE,
deliverable/status, lifecycle, release, reliance, model/credential, PIA-U30,
Electron-supersession, merge, or professional-acceptance effect is created.
