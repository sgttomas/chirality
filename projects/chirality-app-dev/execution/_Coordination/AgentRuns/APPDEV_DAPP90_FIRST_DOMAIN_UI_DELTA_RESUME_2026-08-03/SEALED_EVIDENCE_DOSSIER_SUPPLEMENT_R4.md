# Sealed Evidence Dossier Supplement R4

This supplement closes the coverage gaps identified by the R3 verifier. It is
read with `SEALED_EVIDENCE_DOSSIER.md`; no prior BLOCK receives acceptance
credit.

## 1. Exact original Piping-input fitness criteria and crosswalk

The original `PIPING_INPUT_CHECK.md` says accept an input only if a
Piping-owned response:

1. **is present in the committed tree** — PASS: `HEAD=origin/main` at
   `88e7590d3664d4f1daf91bed2a8899bda0748b92`; exact response tree entry is
   mode `100644`, type `blob`, Git blob
   `a71145ec0952cc5ad62b1b12635be44deebffbd3`; response SHA-256 is
   `e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7`.
2. **cites the inbound request and its SHA-256** — PASS: response section 1
   cites the exact inbound path and
   `32f943eefe80d926626c5f63ae574d6df84f461cd23f0728edf6b8a13de769f1`;
   the committed inbound object is Git blob
   `7801a274ce1cca2e3eefeecbdd2ddfb84826936a` and reproduces that SHA.
3. **reciprocally cites the named Root row IDs** — PASS: response section 1
   cites `TM-ROOT-105` and `TM-ROOT-109` and says the event fires their
   triggers without ruling or disposition effect.
4. **names the Piping UI and semantically equivalent agent-facing runtime
   surfaces with exact Piping refs/hashes** — PASS: dossier section 2 renders
   implemented Desktop/operation/review surfaces, bounded CLI, draft API,
   explicitly absent operative runtime, the six semantic-equivalence
   obligations, and full E-03..E-21 identities used by U. All 29 response
   ledger hashes reproduced at the declared survey-basis commit.
5. **preserves Piping-local versus candidate-generic ownership** — PASS:
   dossier section 3 renders the separate response columns, local meanings,
   candidate carrier limit, section-6 identity boundary, and section-8
   no-effect fence.

All five criteria pass; the sequence hold lifts only for derivative proof.

## 2. Six exact preserved D-APP-81 rows

Authoritative source:
`projects/chirality-app-dev/execution/_Coordination/_PROPOSALS/OD6-G4_APP_CONTRACT_CONCORDANCE_2026-07-28/HISTORICAL_RELATIONS.csv`
at SHA-256
`e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`.

For each of `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-05-04`,
`DEL-08-02`, and `DEL-08-03`, the exact `historical_relation` value remains
`HISTORICAL_RELATION_UNKNOWN`; `hold_state` remains
`REPAIR_VALIDATION_PENDING`; `history_reconstructed` remains `false`.
No file outside this fresh run was written, so all six rows are byte-preserved.

## 3. Exact App critical-file manifest

| Path under `projects/chirality-app-dev/` | SHA-256 |
|---|---|
| `frontend/package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `frontend/package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |
| `frontend/next.config.mjs` | `bbf85b81f8dbcbb26ebb2dd76fed99f1c179c454b2e22b8073b5868c6fdc1b66` |
| `frontend/scripts/build-electron.mjs` | `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558` |
| `frontend/electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `frontend/electron/preload.ts` | `61dc59cfe26b2ce73fb4b6d3d34f955e16c60b5838e77a6868975fd7cb334759` |
| `frontend/src/app/layout.tsx` | `aa0c7a1ff047c5b12533c65fbb34420204776ed68e5644cf9441bc878d07b132` |
| `frontend/src/app/page.tsx` | `5996390849e326731866f6cc6f8d98865e683c0bce526ad5304bcd204f300355` |
| `frontend/src/components/woven-dialogue/woven-dialogue-route.tsx` | `3c23b857727b1911c25bd1027089520e8f102a445a689e6a7677713f840ad10b` |
| `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx` | `ddbf4d55ea94bbfdd037a530c26208991654d810a67ea9dc5ee3d9d0039f371b` |
| `frontend/src/components/shell/portal-loop-shell.tsx` | `18fdbe59537854ab9ca66bd853386b6b69504dd92f66238e4649e498a6c0dbc8` |
| `frontend/src/components/shell/shell-frame.tsx` | `217ff129c05e5e105d39c6da2a05e89823378d7f5f5f91108fca3a0cf6e25654` |
| `frontend/src/lib/harness/mcp/domain-profile-registry.ts` | `83c8526618f78e11f22a9c2d573c8086ccab2ea4bc500814e10b0cefacbdd384` |

The complete 185-entry ordered manifest is
`APP_CORPUS_MANIFEST.sha256`. Its data lines select every `.ts`/`.tsx` file
under `frontend/src/app`, `frontend/src/components`, `frontend/src/lib`,
`frontend/electron`, and `frontend/packages/harness-contract/src`, plus
`package.json`, `next.config.mjs`, `tsconfig.json`, and
`tsconfig.electron.json`, sorted bytewise by path. Hash each file, render
`<sha256><two spaces><path><newline>` in that order, then SHA-256 the 185 data
lines. The reproduced digest is
`ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4`.

## 4. Exact metric definitions and results

- `TL = count(unique target-aware source files outside the variant
  allowlist)`; required value zero for all variants.
- `TA = count(unique target-aware shared files)`; A reports the value in a
  later prototype inside its profile/P/U allowlist, B target is numeric `0`,
  C target is numeric `1` generated shared binding. A is deliberately
  `NOT_YET_MEASURED`, not silently numeric zero.
- `DC = count(target-owned route/shell files whose normalized component/import
  tree is equivalent across both targets)`; intended zero for all; B retains
  11 naive-fork risk sites.
- `BM = targets × logical stages = 2 × 4 = 8`; stages are TypeScript/source
  contract, renderer production build, Electron compile/package, packaged
  launch/smoke.
- Current baseline has one target × four stages = four cells, so
  `DeltaBM = 8 - 4 = 4`.
- `MCI = E + N + 3*Pkg + DeltaBM + |U|`; `|U|=6`.

| Variant | TL | TA | DC intended/risk | BM | E | N | Pkg | DeltaBM | U | MCI |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0 | `NOT_YET_MEASURED_WITHIN_ALLOWLIST` | 0/0 | 8 | 9 | 5 | 0 | 4 | 6 | 24 |
| B | 0 | 0 | 0/11 | 8 | 20 | 4 | 3 | 4 | 6 | 43 |
| C | 0 | 1 | 0/0 | 8 | 9 | 9 | 0 | 4 | 6 | 28 |

These are design targets/lower bounds, not implementation telemetry or a
selection rule.

## 5. Exact write root and containment evidence

Fresh write root:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP90_FIRST_DOMAIN_UI_DELTA_RESUME_2026-08-03/`.

Before the run, `git status --short` was empty. Current tracked diff name
inventories (`git diff --name-only` and `git diff --cached --name-only`) are
empty. The only untracked paths are files beneath the exact fresh write root.
No A/B/C packet or decision-register row exists in that set. The run performed
no Git state mutation. The final validation must re-run and record this
containment after all handoff artifacts are written.

Current run artifact classes are activation; Piping input check; exact U;
App corpus manifest/rebind; comparative Markdown/CSV; sealed dossiers;
verifier briefs and returns; repair backcheck; validation; manager return; and
handoff state. Every one is derivative evidence inside the fresh root.

Exact pre-R4 write inventory relative to the fresh root:

- `ACTIVATION.md`;
- `APP_CORPUS_MANIFEST.sha256`;
- `COMPARATIVE_MEASUREMENTS.csv`;
- `COMPARATIVE_RERUN.md`;
- `CURRENT_TREE_REBIND.md`;
- `FIRST_DOMAIN_UI_DELTA.md`;
- `PIPING_INPUT_CHECK.md`;
- `SEALED_EVIDENCE_DOSSIER.md`;
- `SEALED_EVIDENCE_DOSSIER_SUPPLEMENT_R4.md`;
- `briefs/A2_ADVERSARIAL_VERIFIER_BRIEF.md`;
- `briefs/A2_ADVERSARIAL_VERIFIER_BRIEF_R2.md`;
- `briefs/A2_ADVERSARIAL_VERIFIER_BRIEF_R3.md`;
- `reviews/A2_ADVERSARIAL_VERIFIER_RETURN_ATTEMPT01.md`;
- `reviews/A2_ADVERSARIAL_VERIFIER_RETURN_ATTEMPT02.md`; and
- `reviews/A2_ADVERSARIAL_VERIFIER_RETURN_ATTEMPT03.md`.

The only planned additions are
`briefs/A2_ADVERSARIAL_VERIFIER_BRIEF_R4.md`, final
`reviews/A2_ADVERSARIAL_VERIFIER_RETURN.md`, `REPAIR_BACKCHECK.md`,
`VALIDATION.md`, `MANAGER_RETURN.md`, and `HANDOFF_STATE.md`, all beneath the
same fresh root. Final validation must reconcile this exact list.

## 6. R4 coverage contract

The R4 verifier receives the complete original dossier plus this complete
supplement in its launch message. It must assess tests 1–5, U, App rebind,
metrics, coexistence/elimination, D-APP-81 preservation, and containment. It
must not infer semantic access from a SHA alone; the material content required
for each check is rendered across the two dossiers.
