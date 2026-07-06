# PEC D-APP-52 bridge rehearsal 01 — the live proposal tools, driven end to end on a scratch basis

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture
> convention). Facts only; no pilot-readiness, correctness, go-live, or
> live-LLM-binding claim (K-DOMAIN-4; F-PEC-2).

## Basis

- **Authority:** D-APP-52 O-A (riders 1–11 binding), recorded 2026-07-06 under
  the owner's conditional pre-ruling — packet
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-52_PACKET_PEC_TRANSPORT_PROPOSAL_TOOLS_2026-07-06.md`;
  ruling record `D-APP-52_RULING_2026-07-06.md`.
- **Code under test:** this repository at `cb8441c2a69cb49e94fbc3ea0e409bd83025c72d` (the D-APP-52 tranche
  source commit; handlers `domainProposeOperationTool` /
  `domainProposalValidateTool` in
  `projects/chirality-app-dev/frontend/src/lib/harness/mcp/domain-proposal-tools.ts`
  over `pec-bridge-client.ts`; zero pec source change).
- **Instance:** fresh scratch DB `<tmpdir>/pec-scratch-bridge-rehearsal-*/pec-scratch-bridge.db`
  (D-PEC-06-guarded `npm run seed` + script-side basis prep: synthetic project
  `SYN` id 2, actor provisioning), served on `127.0.0.1:4907`;
  **scratch DB (+wal/shm) deleted after capture** — recorded below. No real
  data ever existed in it.
- **Driver mechanism (key-independence, stated plainly):** **no
  `ANTHROPIC_API_KEY` exists this session and none was used.** The two
  handlers are deterministic HTTP wrappers, so this rehearsal drives them by
  **direct handler invocation** — the same functions
  `buildChiralityMcpTools` registers — via
  `npx vite-node scripts/run-pec-bridge-rehearsal.ts` (vitest's TS runtime;
  run from `projects/chirality-app-dev/frontend/`), capturing the exact
  envelopes a model session would receive. **Live-LLM demonstration through a
  harness model session is DEFERRED.** Nothing is faked, stubbed-as-if-live,
  or key-worked-around.
- **Data:** synthetic MDL CSV fabricated for this rehearsal (`inputs/`);
  no D-T0-14 residency question.

## Actors

| Actor | Identity | Acts |
|---|---|---|
| Agent person | `pec-bridge-agent@rehearsal.demo` (personId 16, `is_admin=0`, coordinator — `import.propose`, never `import.accept`) | every registered-tool act: propose, validate, refresh; credentials generated at runtime from the local environment, never committed, never in artifacts |
| Demo-cast owner persona | `admin@aurora.dev` (personId 15, admin role on SYN) | every accept / screen act / apply — script-side HTTP, disclosed per act below; permitted on the scratch basis by the D-PEC-12 full-agency amendment |
| Non-granted persona | `viewer@aurora.dev` (viewer role) | the 403 taxonomy capture only |

Basis prep (seed, SYN project, actor provisioning) ran script-side as instance
setup, not as workflow acts.

## What happened (every step verbatim in `artifacts/`)

| Step | Artifact | Act | Result |
|---|---|---|---|
| 00 | `00-agent-login.json` | agent session established (identity fact only) | ok |
| 01 | `01-propose-mdl-v1.json` | `domain_propose_operation` mode=propose, contract=mdl, csvFileRef → IPR-0001 | ready_for_review; dry-run 3 create |
| 02 | `02-validate-initial.json` | `domain_proposal_validate` | stored report verbatim; `dryRunAt` unchanged (no recompute) |
| 03 | `03-demo-cast-accept.json` | **demo-cast** owner accept (version + sha256 echo) | accepted |
| 04 | `04-demo-cast-screen-act.json` | **demo-cast** owner screen act (intake item raised) | watermark moved |
| 05 | `05-demo-cast-apply-stale-409.json` | **demo-cast** owner apply attempt, `force: false` | **409 STALE_PROPOSAL** verbatim |
| 06 | `06a-validate-pre-refresh.json`, `06b-refresh-recovery.json` | agent recovery through the tool surface: validate → `mode=refresh` | acceptance voided (RV-13); rebased dry-run |
| 07 | `07-validate-post-refresh.json` | `domain_proposal_validate` | post-refresh state |
| 08 | `08a-demo-cast-re-accept.json`, `08b-demo-cast-apply.json` | **demo-cast** owner re-accept + apply, `force: false` | applied; apply report captured |
| 09a | `09a-taxonomy-400-refresh-of-applied.json` | tool refresh of the applied (terminal) proposal | `ok:false, errorClass: bad_request` (engine 400) |
| 09b | `09b-taxonomy-403-viewer-propose.json` | tool propose as the non-granted viewer persona | `ok:false, errorClass: forbidden` (engine 403; reported verbatim, not retried) |
| 09c | `09c1-propose-second-ipr0002.json`, `09c2-taxonomy-409-version-conflict.json` | second proposal IPR-0002; tool refresh with stale expectedVersion | `ok:false, errorClass: version_conflict` (engine 409) |
| 10 | `10a-hist-ipr0001.json`, `10b-hist-ipr0002.json` | history extracts | agent-person vs demo-cast-admin attribution on every record |
| 11 | `11-taxonomy-network-error-after-teardown.json` | validate after server teardown | `ok:false, errorClass: network_error` |

The `409 STALE_PROPOSAL` normal-flow surfacing (a P2 requirement) is
unreachable through propose/validate alone — the 409 arises only on
accept/apply — so the demo-cast acts are the minimum needed to evidence the
ruled recovery loop. They change nothing about what is registered: no
accept/apply/force tool exists.

## Demo-cast disclosure (rider 5 / rider 9; one line per owner-role act)

- Step 03 accept — demo-cast as `admin@aurora.dev`; script-side HTTP; no force parameter on accept.
- Step 04 screen act (intake raise) — demo-cast as `admin@aurora.dev`; script-side HTTP.
- Step 05 apply attempt — demo-cast as `admin@aurora.dev`; **force: false**; refused 409 STALE_PROPOSAL.
- Step 08a re-accept — demo-cast as `admin@aurora.dev`; script-side HTTP; no force parameter on accept.
- Step 08b apply — demo-cast as `admin@aurora.dev`; **force: false**; applied.
- Step 10 history extracts — demo-cast read as `admin@aurora.dev` (capture only).

`force: false` on every apply act; `force=true` never occurred in any form
in this rehearsal, its tests, or its scripts (Receipt 32 exclusion — absolute,
no scratch carve-out; the driver hard-codes `force: false` with no override
parameter).

## Deferred live-LLM statement

No `ANTHROPIC_API_KEY` existed this session; the live-LLM demonstration of
these tools through a governed harness model session is **deferred** and
remains unclaimed. This pack evidences the transport, handlers, taxonomy, and
actor model only — exposure makes the tools *available*; no working-agent-
bridge, pilot-readiness, or L-level claim is made (K-DOMAIN-4).

## Teardown

Scratch server stopped, then the network_error taxonomy captured against the
dead port (artifact 11); scratch DB `pec-scratch-bridge.db` (+`-wal`/`-shm`)
**deleted after capture**. The D-PEC-01 surfaces and the owner's real
instance were never touched.

## Artifacts (SHA-256)

```
b53971bfaa3cffc470c0bcf6c3a8543bd7b802c9d88ffc4fbfeaf9c0994fcc30  inputs/mdl-syn-v1.csv
9897f4e81d8c02b7532f88f1f37fd589d5ccabaf45466f30e15e206fac94e83a  artifacts/00-agent-login.json
e12d1d61de28c25dfca3199c8c70e0aee124e2026a13887a4e58a2a3d30b5257  artifacts/01-propose-mdl-v1.json
bba6e08a444592507286e62e2df77b621abe11a9b7a06a479a53fec4788113c5  artifacts/02-validate-initial.json
602ad72f0185afa8fe9ff56f7858dc8baa0f18c7042c0de7f546ef6c4f02a787  artifacts/03-demo-cast-accept.json
16e10d7032aa9e76139f790e3ebf860de535e154229950fc479458ff46bd7436  artifacts/04-demo-cast-screen-act.json
48854f578b16d84f08181efc89d3f075416668f3af9c2de9bb8e4a36418ee33e  artifacts/05-demo-cast-apply-stale-409.json
b486f1f9ddfb65362900737aff4eede5942aba8b81206b1ae4009f75aae1d5ad  artifacts/06a-validate-pre-refresh.json
12a6d8d663921793abd8a2b1384073068307c4a22baed168b3c2de963f2a94d3  artifacts/06b-refresh-recovery.json
34560f15079845a67da16668bac7662186d5f0f004ee49d397581b8c95fc61cb  artifacts/07-validate-post-refresh.json
ccae82ab74c51acd98b3a4bdf854d1c4df81f43cad3a539fbfdbac9c020a9c6b  artifacts/08a-demo-cast-re-accept.json
25f61e419b7833caf6d0f2682efded2bcc2a894fa71a3fedb2ebc5ddc5f96398  artifacts/08b-demo-cast-apply.json
87e426388b6d325852ffd35b1478dd4edec6d9f9e8205d95d8d363873d4c1e47  artifacts/09a-taxonomy-400-refresh-of-applied.json
e3e481c5f49caa2258e099eb6d353213b9099a9bbd045fc5f69a2f07bc5cf879  artifacts/09b-taxonomy-403-viewer-propose.json
161c2f76d5251cc744a7e6a1ea608c42af1ad95fe183f8fd8cb185e213c39288  artifacts/09c1-propose-second-ipr0002.json
b23be44bea2c07b191ee9df9b3b25612767d110207597919fc590220dac47d36  artifacts/09c2-taxonomy-409-version-conflict.json
ea4bfc88865e4f65a11a2996bb9dd2dbff37f7ffcad3c080eafe1a6a8c12b270  artifacts/10a-hist-ipr0001.json
760373cce7eacc728250410cffc25ab8afd0c79680ba768e9d7dbe813f5fda37  artifacts/10b-hist-ipr0002.json
bf7c4de9d19b7b13d60807eb5c27f3987573ca9c4d8cf25a3644a8a851e144b4  artifacts/11-taxonomy-network-error-after-teardown.json
```

Mirror artifact (non-authoritative, batch form disclosed):
`_DomainEngines/proposals/pec/OP_2026-07-06_BRIDGE_rehearsal_IPR-0001-0002.md`.

## Boundaries respected

Scratch/demo basis only; DB deleted after capture. Accept, apply, and every
owner-role act demo-cast and disclosed; `force: false` on every apply. No
accept/apply/force tool registered or reachable; no pec source change; no
real-instance content; no tier-0 act; no publication or release act; every
claim above is reproducible from the transcripts in `artifacts/`.
