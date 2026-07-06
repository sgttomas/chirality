# PEC D-PEC-17 evidence 01 — built-in agent UI v1, stub engine, scratch basis

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture
> convention). Facts only; no pilot-readiness, correctness, or go-live claim
> (F-PEC-2). Every claim below is reproducible from the transcripts in
> `artifacts/` plus the committed source at the SHA named under Basis.

## Basis

- **Authority:** D-PEC-17 RULED O-A (recorded 2026-07-06 under the owner's
  Receipt 32 item 4 conditional standing pre-ruling; packet:
  `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-17_builtin_agent_ui_source_tranche.md`).
- **Code under test:** branch `codex/pec-dpec17-agent-ui` at `68fab1c00`
  (the five D-PEC-17 tranche commits on top of `55bfd9d0d`).
- **Instance:** fresh scratch DB `pec-scratch-dpec17.db` in the session
  scratchpad (outside the repo), seeded with the Aurora demo cast via the
  D-PEC-06-guarded `npm run seed` (`PEC_DB` carrying the required scratch
  token). Server `PEC_PORT=4899`; sidecar started with the shipped
  `npm run start --workspace agent-sidecar` (`PEC_AGENT_ENGINE` unset ⇒ the
  `stub` default), loopback only. **The scratch DB (+ -shm/-wal) was deleted
  after capture**; no real data ever existed in it. `pec.db*`, `pec-demo.db*`,
  `pilot-scratch/**`, and `backups/**` were untouched.
- **Actors (WF-8):** agent under its own provisioned person
  `pec-agent@rehearsal.demo` (personId 16, `coordinator`, `is_admin=0` — the
  rehearsal-01 pattern; credentials were a throwaway local-env value, never
  committed, deleted with the DB). Panel director: `pm@aurora.dev`
  (personId 2, holds `agent.direct`). Human accept/apply: `admin@aurora.dev`
  (personId 15) — **disclosed demo-cast human acts on the scratch basis**
  (D-PEC-12 full-agency amendment; Receipt 32 exclusions); `force` was never
  sent in any request (the apply bodies carry only `version`).
- **Wire path:** every agent turn went through the REAL HTTP surface the
  panel uses — `POST /api/projects/1/agent/messages` under the pm's human
  session (RBAC + same-origin gate in the pec server) → proxy (cookie
  stripped, pid injected) → sidecar `127.0.0.1:4812` → pec API under the
  agent person's own session. Nothing bypassed RBAC.

## No key existed — stated verbatim

**No `ANTHROPIC_API_KEY` existed this session, the engine ran `'stub'`, and
live-LLM demonstration is deferred.** The sdk engine remains the shipped
key-droppable loader (dependency + key + config, no source change); selecting
it without the package fails with the documented message (pinned in
`agent-sidecar/test/sidecar-e2e.test.ts`). The P4 owner-at-the-screen
rehearsal (D-T0-19) remains a separate, undischargeable-agent-side gate and
is **not claimed** by this evidence.

## What happened (transcripts are the artifacts named)

| Step | Act | Artifact | Result |
|---|---|---|---|
| 0 | Panel health probe through the proxy (pm session) | 00 | engine `stub`, egress `none`, configured, agent name "PEC Agent" |
| 0b | `document_controller` probes the panel routes | 00b | **403** — "agent.direct: directing the agent requires admin, pm, or coordinator" (GOV MINOR-2 exclusion live) |
| 1 | File drop → agent proposes (MDL CSV attachment) | 01 | IPR-0001 filed by personId 16, `ready_for_review`, dry-run 2 create / 0 update / 0 conflicts / 0 rejected / 0 to intake; reply ends with the Admin deep link + agent name line |
| 2 | `refresh IPR-0001` turn | 02 | dry-run recomputed; reply states any prior acceptance is voided and a human must re-accept |
| 3 | `triage INTK-0002 as parked: <grounds>` | 03 | open-triage + disposition through the live routes; disposition note carries the grounds verbatim |
| 4 | `triage INTK-0003 as converted: …` **twice** | 04, 04b | **deterministic `act:refused`** directing the owner to perform the conversion on-screen; byte-identical on repeat (`deterministic: true`); **no disposition call was issued** (INTK-0003 stays `raised` — see 06b) |
| 5 | `triage INTK-0001 as parked` (no grounds) | 05 | `act:refused` — "no grounds given … left for the owner (D-PEC-10 rider)" |
| 6 | `status` and `intake` turns | 06, 06b | agent proposals with lifecycle states; intake queue summary (INTK-0001/0003 still open, INTK-0002 dispositioned) |
| 7 | Human opens the proposal and accepts | 07, 08a | **409 `STALE_PROPOSAL`** — the triage in step 3 moved the watermark after step 2's refresh: the ruled staleness flow fired live, unforced |
| 8 | Ruled recovery: agent `refresh IPR-0001` → human re-accepts → human applies | 08b, 08c, 09 | re-accept 200 (`acceptedBy` 15, hash+version echoed), apply 200 (`appliedBy` 15, `force` absent), state `applied` |
| 9 | History extracts (WF-8 actor split) | 10, 10b, 11, 12 | IPR-0001: `created`/`proposal_dry_run` ×3 by **16** (agent); `proposal_accepted`/`proposal_applied` by **15** (human). INTK-0002: `created` by 13, `transition`+`dispositioned` by **16** |
| 10 | Sidecar health read directly on 127.0.0.1:4812 | 13 | same identity/engine/egress as through the proxy |

## Named evidence observation (GOV MINOR-4 — the panel-side pin)

**"The panel renders no accept/apply/reject-of-others control; the human act
was performed through the Admin deep-link under the human's own session."**

Basis of this observation, stated exactly:

- The human accept and apply in this run (08c, 09) were performed under the
  human admin's own session against the same `import-proposals/:id/accept`
  and `/apply` routes the Admin "Proposed imports" section calls — never by
  the agent, whose only pointer is the `/p/1/admin` deep link its replies and
  proposal cards carry (01, 02).
- The panel component of record (`web/src/agent/AgentPanel.tsx` at
  `68fab1c00`) contains no accept/apply/reject-of-others/force control: its
  only lifecycle-adjacent elements are read-only badges and the two Admin
  deep links (`Open Admin — Proposed imports (accept/apply)`; `review in
  Admin (accept/apply is yours)`). `@pec/web` has no unit-test framework
  (packet-verified), so panel coverage is `tsc` typecheck + `vite build`
  (both green at this SHA) + this rehearsal — stated plainly.
- A live browser click-through of the rendered panel was **not** performed in
  this capture (the agent-run environment had no confirmed browser session);
  the render claim above rests on the component source at the pinned SHA and
  the built bundle, and the human-act claim on the 08c/09 transcripts. Not
  worked around, stated as-is.

## Checklist against the packet's evidence plan

- [x] scratch `PEC_DB`, guarded seed, seeded cast + provisioned agent person
- [x] server + sidecar via the shipped scripts; stub engine (default)
- [x] file drop → agent proposes (IPR ref + full dry-run report incl. `intakeCreated`)
- [x] triage with grounds; groundless and `converted` refusals (deterministic)
- [x] status query with lifecycle states
- [x] accept/apply as disclosed demo-cast human acts, `force` never sent
- [x] ruled staleness flow exercised live (409 → refresh → re-accept → apply)
- [x] history extract showing the agent/human actor split (WF-8)
- [x] GOV MINOR-4 named observation captured above, with its basis stated
- [x] live-LLM deferral stated verbatim; no key sourced, hardcoded, or fabricated
- [x] scratch DB deleted after capture

## Artifacts (SHA-256)

```
90dfbbab9b99dbcdf44467cc230157bcd947cd375c70370c0eaaef94710727a8  inputs/mdl-aurora-evidence.csv
9520a60411f16bd77f2cb7b4940ffefa06e79c50c63430b6296564b093628546  artifacts/00-proxy-agent-status.json
9f94d9698642c2695a8f1d4b5e1b649045b67be774a2a85967428f93d2e20f6b  artifacts/00b-dc-agent-status-403.json
6a370229454fcd24f1277200ac0d5dc71d90b560adc04fafd23bf59892023214  artifacts/01-turn-propose.json
60540c3ed41529f3b8809eeb202b1c5db22929a7a1c91da4e3756d40cc992544  artifacts/02-turn-refresh.json
b98773393c254818c1900f6a5a5bbf85779f90ba758ddfc74b9be9ed5aa40635  artifacts/03-turn-triage-parked.json
61f6bc29f5b41f2ee13482dbbf8ac6c2ed29b1adcd34eb2fd41d9a1f7bc91f4b  artifacts/04-turn-triage-converted-refused.json
ec957364a09cd04e0391e59da97a4d532dea7af607c245d83795034ef17f9549  artifacts/04b-turn-triage-converted-refused-repeat.json
5a1fa4f523b0206705bd59cce059574f44a0932cd5b4f53330b9105a03636d8f  artifacts/05-turn-triage-groundless-refused.json
81f20fe6e01c4ecee8755ac0424977b4f85f58c51e0549aaa830b71cc71b5300  artifacts/06-turn-status.json
fc179799badf7fbd435612c60da78dad817c8049f6f168e88fcdef2a31df9aa0  artifacts/06b-turn-intake-summary.json
f294cdd46890b875555bf349c6ffada1f704cd4c57dd55327b5e1257d3bc0c6b  artifacts/07-admin-proposal-view.json
53dede7cfeb35c40cdda077883268c739ed20c3b7c309b9d6c79f22fd9600bb1  artifacts/08a-admin-accept-stale-409.json
a59c7ad534520f6f362838ec7e91db06a18b9aead463d1f7547b769240bf5b68  artifacts/08b-turn-refresh-after-stale.json
5207ca1fe968bafc939c9cd37fabc753e8ee89f140ba6a76bcd0d58485ab7648  artifacts/08c-admin-reaccept.json
3b68eb4ee9207c7243b2ea62d64254f75f3b32afc5a9cde97f2ad3fa32f23e7b  artifacts/09-admin-apply.json
b6ebec0525fdc5fb770e283c1250261f93654b0b207ca1944198292fcc12f572  artifacts/10-history-proposal.json
3a0521bbb28eec8e603938c583d6c0d69d7a03ff618c70c03f9f757b1687916f  artifacts/10b-history-intk0002.json
3d5c5f234b79a7dadb8db932386dff6edb4b163b7d080218ecb57528f148278a  artifacts/11-proposals-final.json
da08bb825e4e41180cf52b4de9182a96af6318e0b8b10d4ba7a255b39c18ca84  artifacts/12-people.json
4b884ca437f21752ae7f1ea99d30a70a58a6042e7ea4ae6993ca08bf7184f01d  artifacts/13-sidecar-health-direct.json
```

## Boundaries respected

Scratch/demo basis only; DB deleted after capture. No `force` anywhere. Every
accept/apply stayed human (personId 15), disclosed above. No approval record
was created by any route (the `converted` instruction was refused before any
network call — artifact 04). No tier-0 act; no real instance content
(synthetic Aurora demo data throughout); the sidecar and panel added
capability, never permission (pec RBAC refused the misgranted role at 00b and
would refuse any agent accept — pinned in `sidecar-e2e.test.ts`). No
pilot-readiness or go-live claim.
