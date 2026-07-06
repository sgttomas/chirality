# PEC L3 evidence 01 — first agent-authored import proposal through the live API

> **Epistemic status: immutable evidence snapshot** (D-T0-13 capture convention;
> L3 rung per D-T0-18 O-A + D-PEC-12, owner-ruled 2026-07-05). Facts only; no
> pilot-readiness, correctness, or go-live claim (F-PEC-2).

## Basis

- **Authority:** D-T0-18 O-A (advance to `OPERATION_PROPOSAL`, imports scope) and
  D-PEC-12 with the owner's full-agency amendment; owner direction "Merge the PR
  first and then proceed accordingly" (2026-07-05). Demo/scratch basis per the
  standing 2026-07-05 approval of demo-basis rungs (Receipt 17).
- **Instance:** scratch DB seeded by `npm run seed` (demo cast, password-gated),
  served on `:4899`; DB deleted after capture; no real data existed in it.
- **Actor:** seeded demo admin `admin@aurora.dev` (personId 15). All acts ran
  through the live HTTP API with session auth — nothing bypassed RBAC. On real
  data, accept/apply remain acts of the operating human; here the agent drove
  end-to-end under the owner's full-agency amendment, on demo content only.
- **Source file:** committed fixture `projects/pec/fixtures/mdl-sample.csv`,
  SHA-256 `6f546f5a88c143c9bc8e71dc9090e170099187869a8eb1448328cc97f0b5109b`.
- **Code under test:** `main` at `45ff3e6a7` (PR #82 upload-agent v1 + PR #84
  slate merged), branch `codex/pec-l3-execution` (governance edits only — no
  pec source change between merge and capture).

## What happened (the L3 lifecycle, end to end)

| Step | Act | Result |
|---|---|---|
| 1 | Agent filed `POST /import-proposals?contract=mdl` with the fixture body | `IPR-0001` created; dry-run auto-ran; state `ready_for_review` (v2) |
| 2 | Dry-run report | 4 create, 0 update, 0 conflicts, **1 rejected** (fixture's deliberate bad row 6: bad state, bad date, unknown owner — reported, never silently dropped), 0 to intake; registers untouched (dry-run rolled back) |
| 3 | Accept with echoed `version=2` + source SHA-256 | state `accepted` (v3), `acceptedSha256` = source hash (RV-13 binding) |
| 4 | Apply with `version=3`, no `force` | state `applied`; apply report **identical to the dry-run** (4/0/0/1) — deterministic preview held |
| 5 | History extract for `IPR-0001` | kinds `created → proposal_dry_run → proposal_accepted → proposal_applied` |
| 6 | Export-and-compare (`GET /export/mdl.csv`) | all 4 imported rows round-trip field-for-field (e.g. `AUR-P-005`, `AUR-M-004`) |

## Artifacts (SHA-256)

```
696610f2878d075d05db05219f3b1e339bd983e2c6bb84a5061067c6ea0ead4a  artifacts/00-me.json
47b5c83850a2fa56461b69a20df3239cb935a93d056f3dd392442b5ccbe561a5  artifacts/01-propose.json
15a34a0d1b3dd09c8af47d612d4cacb235be0fcbdd9c6773298dd5c488f263fb  artifacts/02-accept.json
aeb20d50d740ed8e8b88c2bbbb49361d4860e21f1398fc38ee1652adcfa1d90c  artifacts/03-apply.json
2991691bd2cdd918597171ddd34bf62df00ce92a6f5f38656847a11cd26d0d26  artifacts/04-history.json
21cb6e7949851d0aa653b1a14d49ea7bb897c248832de54fce4e1a47e1fcb82b  artifacts/05-export-mdl.csv
```

Mirror artifact (non-authoritative, per D-PEC-12 §1):
`_DomainEngines/proposals/pec/OP_2026-07-05_IPR-0001_mdl_fixture.md`.

## Boundaries respected

Scratch/demo basis only; DB deleted after capture. No `force`. No real
instance content (D-T0-14 CLOSED untouched). No professional claim. The
demo-admin accept/apply here evidences the seam, not an authority precedent
for real data.
