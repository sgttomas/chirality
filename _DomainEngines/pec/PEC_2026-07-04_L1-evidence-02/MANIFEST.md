# PEC L1 evidence capture 02 — MANIFEST (immutable snapshot)

> **Epistemic status: generated evidence — not authority.** Read-only L1
> evidence per the D-T0-13 O-A staging ruling and the Receipt-4
> ladder-as-core-goal addendum. Captured outputs are derivative packages, not
> substitute authority; pec's tests and source govern. Immutable after
> publication — corrections go in a new dated snapshot.

## What this proves

The remaining L1 seams beyond `L1-evidence-01`'s deterministic checks:
authenticated session (`POST /api/auth/login`, cookie session per ADR-007),
RBAC'd read routes, all 11 §15/§16 register exports, both print reports
(sponsor brief, package pack), Explain payloads (ADR-004/012 gate
explanations), and the plan view — end-to-end over the live HTTP API.

## Source refs

- Tree: `origin/main` @ `8e42b126c` (PR #57 merge), isolated worktree; pec
  sources unmodified.
- Database: **scratch demo only** — created fresh by `npm run seed`
  (committed `tools/seed.ts`, demo project `AUR`), served, captured, then
  **deleted** with its `-wal`/`-shm` and the session cookie jar. No
  pre-existing database was read or replaced.

## Actor / visibility basis (owner-provisioned)

- Owner provisioning direction (2026-07-04, in-session, Ryan Tufts):
  "provision the demo basis: scratch DB, seeded demo data, capture as
  admin@aurora.dev" — this is the D-T0-13 required actor/visibility basis.
- Session actor: `admin@aurora.dev` ("Ada Admin", instance admin, personId 15
  in the seeded DB) — full visibility; log export is the admin-visible view.
- Residency: D-T0-14 CLOSED respected — every byte captured derives from
  committed seed code, not from any real project or pilot content.

## Commands and captures

- Server: `node server/src/index.ts` on `:4810` against the seeded scratch DB;
  stopped after capture. Web UI not started.
- Login: `POST /api/auth/login` → httpOnly cookie session; logout issued
  before shutdown.
- Captured (all authed GETs, project `AUR` pid 1) — SHA-256:

```
696610f2878d075d05db05219f3b1e339bd983e2c6bb84a5061067c6ea0ead4a  auth_me.json
6d00bc29fab38dfa6423cd035fcd90169ffa42d67922540fe439386587ba26c7  explain/revision_1_explain.json
fc91b0cf6e40aa4e979128f993e6bedc61a6eb9a30b8d849dd789e2b91126c37  explain/revision_2_explain.json
f9de363234be6192f7f00ebe28dce7350127f689516d6517050a1fcaa4bc4e7b  exports/approvals.csv
4db31764aa42001a7caa3f6859e9fa1ca794b1448a6ea76de04dca699d517f25  exports/commitments.csv
818d4816ddfa60943646b009c9365812b138ad0875a62d27a79957e1f42cb956  exports/decisions.csv
a4859a6669442440959fb065aaeb4ae47d5950b2293f7142255d698852f25e0e  exports/intake.csv
8e09b63bb3c8bee6958deffb6e6c2ca2afa823bb0b0da34722d8d22dbbec87ab  exports/interfaces.csv
a5b42a1f66dca75eee1587dd549f239f582aad5edf5eadb7840eeec181ce5ce2  exports/log.csv
a38b8230b4b96d55924392463fd6fc36c1accb284ee0c001f97c6f583194f3ae  exports/lookahead.csv
58e58861723db0cb8612146bb55c7422a3e6afaa09bed8fc0c8847a564151852  exports/mdl.csv
b2a7685b3e89fde9ebca87f1d6372a32b9d6482af2382957954539438495f6c2  exports/rail.csv
309f31d49bac4ce614150e347e5fa137f66ef3104ecb994c8888a8f049788412  exports/risks.csv
572824571ce80de1c4ed79cf14de751e753f632d3d9dd9fd9348d5a1f6abcaa9  exports/schedule.csv
f3b5bf61027e543fb0140487e38f981ee27f47d4b10f030050be12713327643e  overview.json
8ee35c15cb84a16d6144e933c87ebdf1a831da3809f86da6a0706a7981cae8a8  plan.json
5e78b11cb539bb217088447da14c541e82273098fbf8ee2711218bcc57fb68ae  reports/package-pack_PKG-EI.html
a66342eb372ea88fff6915d32d87599bfbf806b83b6ab1563a4a7eca07f1e79d  reports/sponsor-brief.html
```

## Warnings and limitations

- Demo content only: values are the committed seed's fiction (project `AUR`);
  nothing here characterizes any real project. No pilot-readiness,
  go-live, or engineering-correctness claim (F-PEC-2; profile professional
  boundary).
- Explain payloads show `revision.issue` `permitted:false` with open hard
  conditions — correct engine behavior for the seeded state, not a defect.
- **Tool gap found (for the harness backlog / future `pec_api_adapter`):**
  `tools/seed.ts:43` hardcodes its DB path (`projects/pec/pec.db`) and ignores
  `PEC_DB`, unlike the server (`server/src/index.ts:17`). Safe here because
  the worktree was isolated and the file is gitignored, but the profile's
  `seed.demo` open issue (no refuse-non-demo-DB guard) is compounded by the
  env var being silently ignored. A future repair should honor `PEC_DB` and
  refuse non-scratch paths.
- Visibility filtering was exercised only at admin scope; a scoped-persona
  capture (restricted log visibility) is a natural `L1-evidence-03` if wanted.
