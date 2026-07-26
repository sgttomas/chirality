# S3 Terminal Return — export-boundary audit (ROOT-OGC-20260725)

Executor: ephemeral bounded Agent 2 generalist (`opus-5`). Mode: READ-ONLY —
no export run, no commits, nothing written outside this return and
`execution/_Coordination/AgentRuns/ROOT-OGC-20260725/evidence/EXPORT_BOUNDARY_AUDIT.md`.
Basis: HEAD `4aaa66483`; export artifacts last refreshed at `5af6c4a49`
(2026-07-24), verified ancestor.

## Verdict

**SAFE — WITH CAVEATS.** The standing deferral of export-staging regeneration
accumulates no leak risk and no silent staleness hazard.

## Allowlist summary

`exports/chirality-app/export_public.py` is a pure allowlist copier with a
fail-closed post-scan; no external config. Membership: 6 root files
(`.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CHIRALITY_FRAMEWORK.md`,
`PROFESSIONAL_ENGINEERING.md`, `LICENSE.md`), 7 root dirs (`.github`,
`agents`, `skills`, `tools`, `docs`, `init`, `runtime`), plus staged
`README.md` sourced from `PUBLIC_README.md` (canonical root README not
copied) and a generated public `init/init-prompt.md`. Subtractions: 2 exact
paths, 1 prefix (`docs/governance_harness/briefs/`), 26 `SKIP_DIRS` matched on
any path component, `.DS_Store`/`.env*` and 6 binary suffixes. Sanitization
rewrites 6 legacy `/Users/ryan/ai-env/projects/...` prefixes.

Failure conditions: missing allowlist entry → SystemExit; `CLAUDE.md` not
byte-exact `@AGENTS.md\n` → SystemExit; boundary scan → exit 2 on public-README
marker violations (3 required / 5 forbidden), forbidden top-level
(`projects|domains|migration|plans|exports`), any `SKIP_DIRS` directory,
forbidden files, or **any residual `/Users|/home|C:\Users` path**. `--apply-target`
refuses a target without `.git`.

The load-bearing property is the residual-private-path regex, not the
replacement list: the replacement list is stale for the current checkout
location, which makes an unrecognized private path a *failure*, never a leak.

Read-only dry-run at this basis: 13/13 allowlist entries present, `CLAUDE.md`
exact, both README marker sets pass, **0 boundary findings**, 738 files would
stage, no credential patterns in allowlisted roots, only `__pycache__`
(already in `SKIP_DIRS`) among ignored files inside allowlisted roots. The
deferral is not masking a failing export.

## IN/OUT for state added since the profile was last exercised

| State | IN/OUT | Rule |
|---|---|---|
| `execution/PKG-01…06` | OUT | `execution` not in `ROOT_DIRS` — never traversed |
| `execution/_harness/` guard state | OUT | same; cited as outside the boundary in `validate_root_harness_adapter.py` docstring |
| `execution/_Decomposition/` | OUT | same |
| `execution/_Coordination/AgentRuns/` | OUT | same |
| `projects/`, `domains/`, `plans/` | OUT ×3 | non-membership + `SKIP_DIRS` + `forbidden_top` |
| `_DomainEngines/` | OUT | non-membership only (not in `SKIP_DIRS`/`forbidden_top`) — see C3 |
| root `README.md`, `exports/**` | OUT | replaced by `PUBLIC_README.md`; `exports` triple-blocked |
| Decision records `_DECISIONS/D-GOV-21…26` | IN | `docs` allowlisted; deliberate per profile README (authority verification) |
| Proposal packets `_PROPOSALS/D-GOV-21…24/PACKET.md` | IN | only `briefs/` is prefix-excluded |
| Tranche manifests (4, directory new since basis) | IN | `docs` allowlisted, no exclusion — the one materially new consequence |
| `docs/PRD_ROOT.md` | IN | owner-ruled: RD-4 (§9.4, Receipt 38) chose root `docs/` "through the existing export allowlist … no boundary change occurs" |
| 11 new `tools/validation/validate_root_*` + tests | IN | `tools` allowlisted |
| `.github/workflows/governance-harness.yml` (adds G0–G4) | IN | only `harness-premerge.yml` excluded |
| `docs/SPEC|CONTRACT|DIRECTIVE|TYPES`, thesis, `runtime/**`, `AGENT_CHANGE.md` | IN | allowlisted roots; content-hash stale only |

**Nothing added since the last export crosses from OUT to IN.** Every new
private-evidence surface from the root loop lands under `execution/`.

## Staleness findings

- Only manifest/report/READMEs are committed under `exports/`; **no staging
  tree exists** (`.gitignore` 115–118) and `--apply-target` copies only from a
  stage built in the same run. A stale tree therefore cannot be published.
- Regeneration headline: 711 → **738** manifest rows; `docs/` 72 → 88 (+16:
  PRD, 6 decisions, 4 packets, handoff, 4 tranche manifests); `tools/` 334 →
  345 (+11 root guards/tests); hash churn on ~28 more files; boundary findings
  expected to stay 0.
- **S1** `PUBLIC_README.md` still frames the product as "a governed macOS
  application environment", pre-dating the D-GOV-23 genus supersession and
  D-GOV-22 adoption. Regeneration will **not** fix it — it is copied verbatim.
- **S2** `PUBLIC_README.md`'s contents table omits `.github/` (sibling of the
  already-open C-4 finding about root `README.md` omitting `runtime/`).
- **S3** tracked `export-manifest.csv`/`export-report.md` understate the tree
  and carry no basis annotation; they gate nothing.

## Material finding for the next export (not caused by the deferral)

The exported `governance-harness.yml` now runs G0–G4. G0–G3 PASS-idle when
`execution/` is absent — exactly the public tree's condition. **G4 does not
depend on `execution/`**: it validates `docs/governance_harness/tranche_manifests/`,
which is exported, and asserts routed-notice existence.
`ROOT-CLOSEOUT-20260725.yaml` has `disposition: routed` →
`domains/chirality/_Coordination/NOTICE_2026-07-25_AGENT_CHANGE_MERGE_VERDICT_RULE.md`,
and `domains/` can never be exported. **A public export at this basis would
ship CI that fails on its own tree.** This argues *for* the deferral: the next
actual export need is the right moment to resolve it (fixture-aware exception,
manifest-dir exclusion, or dropping G4 from the public workflow — this audit
decides none).

## Caveats on the disposition

- **C1** G4 will fail in the public tree; must be resolved before the next
  apply, not before the next commit. Correctness, not disclosure.
- **C2** `PUBLIC_README.md` will not self-heal (S1/S2) — the next export is an
  authoring task, not just a regeneration.
- **C3** The allowlist has no negative-space alarm: a new root sibling becomes
  OUT silently (`_DomainEngines/` is the live instance). Correct-by-default,
  but a monitoring gap if the deferral runs long.
- **C4** RD-4 states every future PRD amendment is an M2 tranche requiring
  "export-manifest regeneration"; the owner may wish to say which governs a
  future PRD-amendment tranche — the standing deferral or RD-4's obligation.
- **C5** Derivative artifacts cite no generating commit (AGENTS.md
  derivative-package rule); non-blocking.
- **C6** Two publication questions open (below).

## Flagged as ambiguous under the D-GOV-20 boundary — owner's to settle

- **A1** Exported governance records *name* private-tree paths and pin
  structure: `ROOT-CLOSEOUT-20260725.yaml` cites
  `domains/chirality/_Sources/Source_Manifest.csv` row 37 with a sha256 pin;
  `D-GOV-21_IMPLEMENTATION_HANDOFF.md` names two private notice paths;
  D-GOV-23/24 name `projects/chirality-app-dev` pinning behaviour. These are
  references and structural facts, not evidence content, and the scan permits
  them (not machine-absolute). Whether disclosing the existence and pin
  structure of private workspaces is intended publication is a publication
  judgement — the same class RD-4 shows the owner reserves.
- **A2** `_PROPOSALS/*/PACKET.md` export as a class (only `briefs/` is
  excluded), carrying declined options and adversarial-review history.
  Decisions clearly publish; whether *candidate deliberation* equally does is
  unstated in profile doctrine. Predates this period; raised as standing.

Full evidence, including the dry-run table, per-rule IN/OUT derivations, and
the G0–G4 idle analysis:
`execution/_Coordination/AgentRuns/ROOT-OGC-20260725/evidence/EXPORT_BOUNDARY_AUDIT.md`.
