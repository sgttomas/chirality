# PEC_2026-07-06_DPEC20-evidence-01 — enumerated-vs-broad capture (D-PEC-20 O-A / D-T0-21 O-B)

**Captured:** 2026-07-06, by the PEC work loop agent, under the D-PEC-20 O-A
tranche's verification plan (packet ruled 2026-07-06; execution deferred to and
performed in this session). Authority: D-T0-21 O-B (dual access basis) +
D-PEC-20 O-A (source tranche), rulings verbatim in their packets.

## Basis (scratch only)

Hermetic scratch instance: `projects/pec/server/test/harness.ts`
`createTestEnv()` — temp DB in the OS tmpdir, seeded test cast (project TST,
one package, one deliverable, one revision). **Scratch DB deleted after
capture** (with `-wal`/`-shm`). No pilot DB, no real/non-scratch pec data, no
standing instance touched. The owner's live `pec-demo.db` was never involved.

Basis prep (disclosed): the agent person provisioned per the rehearsal-01
pattern (`is_admin=0`, coordinator grant); ONE intake item raised and ONE
risks import proposal filed by the seeded **human** coordinator so that
inside-enumeration reads and the withdraw-of-others pin have live subjects.
**No accept, no apply, no `force`, no disposition — performed by anyone** in
this capture (stricter than the demo-cast pattern; Receipt-42 precedent).

## Method (disclosed)

Reads were exercised by direct invocation of the sidecar acts layer
(`bindActs`) against the live scratch HTTP API as the agent person, with
egress class `'model-provider'` set at the acts seam — the exact context the
SDK engine drives (`engine/sdk.ts` dispatches through the same `BoundActs`).
**No `ANTHROPIC_API_KEY` exists in this environment; no model session
occurred; live-LLM demonstration under `broad` remains deferred to the
owner's screen.** The sidecar HTTP surface itself was exercised for the
health disclosure (both bases) and one full stub-engine turn.

## Artifacts

| File | What it shows |
|---|---|
| `enumerated-vs-broad.json` | The same 12 questions on both bases, one identity, one instance: under `enumerated`, every read outside the D-T0-20 O-B enumeration is refused naming the basis (overview, deliverables/risks/tracker registers, deliverable history, revision explain, sponsor brief, deliverable screen-read) while inside-enumeration acts pass unchanged (intake_item history, intake_item screen-read, proposal status, intake summary); under `broad`, all twelve pass over the agent person's own RBAC. |
| `boundary-refusals-under-broad.json` | Under `broad`: accept / apply / outcome / supersede / waive / `force` (query and body) all refused `AGENT_FORBIDDEN_ACT` **before any network call**; `converted` disposition refused at the acts layer with no disposition call issued; withdraw of the coordinator's proposal refused before the reject call; and — client guards bypassed via raw HTTP as the agent person — the **server itself** refuses the direct accept with HTTP 403 (RBAC, the real gate). |
| `health-disclosure.json` | `/agent/health` states the active basis on both launches (`access: enumerated` / `access: broad`). |
| `stub-turn-register-read.json` | One full sidecar HTTP turn (`register deliverables`, stub engine): route wiring live end-to-end. The stub's egress class is `none`, so the basis does not bind it — by design (D-T0-20's scoping covers external-model sessions only). |
| `capture-record.json` | Basis-prep facts, agent identity, and the egress/method disclosure. |
| `capture-driver.ts` | The exact driver that produced every artifact (reproducible; scratch-only by construction). |
| `SHA256SUMS` | Hashes of every artifact above. |

## Boundaries honored

- Mutation basis: scratch only; the DB was deleted after capture.
- Accept/apply/reject-of-others/`force`/conversion dispositions: excluded
  regardless of basis (D-T0-21 O-B exclusion list) — demonstrated refused
  under `broad` at the client, acts, and server layers.
- Visibility: everything read under `broad` was the agent person's own RBAC
  visibility over existing GET routes; no server change, no new dependency.
- No pilot-readiness, go-live, or issuance claim (F-PEC-2).
