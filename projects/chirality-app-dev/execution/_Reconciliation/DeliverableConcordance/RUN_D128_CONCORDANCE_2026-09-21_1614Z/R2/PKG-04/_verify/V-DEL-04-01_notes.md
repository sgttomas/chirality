# V-DEL-04-01 — verifier shard notes (R2, PKG-04)

Graded against `GRADING_KEY.md` and `CONVENTIONS.md`, with evidence read at the frozen basis `00115c719`. No errata file exists for DEL-04-01, so there are no class e items.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 1 | 1 | 0 | 0 |
| n | 9 | 3 | 1 | 5 |
| b | 6 | 6 | 0 | 0 |
| c | 3 | 3 | 0 | 0 |
| **Total** | **19** | **13** | **1** | **5** |

No Disposition was refuted or contested. Every non-CONFIRMED verdict is at field level.

- REFUTED: `DEL-04-01#CLM-017` AuthorityTier. The row has `LOCAL_DESIGN`, but the correct value is `GOVERNANCE_INVARIANT`, because the Prerequisites table restates DIRECTIVE 2.9, CONTRACT K-RELIANCE-1 and SPEC 10. The row's own NormativeSource lists these, and GRADING_KEY 7 takes the highest source restated. The Disposition `STALE_SPECIFICATION` stands: the `_DEPENDENCIES.md` TBD is false against `Dependencies.csv`.
- CONTESTED: AssessmentEvidence on `CLM-001`, `CLM-004.2`, `CLM-008`, `CLM-015` and `CLM-022` (see pattern 1).

## (ii) Systematic patterns

1. **The same INSP-03 fact is graded three ways across SEE rows.** INSP-03 (2026-06-20) concluded that the REF-006 PRD hash mismatch "remains open". At 00115c719 the PRD hash again does not reproduce (`REFERENCE_HASHES.csv`, Match=NO). The worker's rows handle this in three ways:
   - `CLM-001` and `CLM-004.2` say `OVERTAKEN`, because the hash pair changed.
   - The identical SEE rows `CLM-008`, `CLM-015` and `CLM-022` say `NOT APPLICABLE`.
   - `STILL CURRENT` is also defensible, because the mismatch conclusion holds in substance.

   MR-1 and MR-9 do not settle a note that postdates the assessment but restates a fact the assessment concluded on. This has no Disposition impact, because STALE_ASSESSMENT is not used. At minimum, SEE rows should carry the same AssessmentEvidence as their target.
2. **The AuthorityTier on STATE_ASSERTION rows that cite normative sources.** `CLM-017` uses `LOCAL_DESIGN` although it restates DIRECTIVE, CONTRACT and SPEC items. The other STATE_ASSERTION rows sampled (`CLM-001`, `CLM-004.2`, `CLM-008`) restate only register state and correctly take `NOT_APPLICABLE`.

Checked and holding:
- **CLM-003.** The AUTHORITY_CONFLICT holds. App `DIRECTIVE.md` 2.8 (line 117, unamended) still names the Claude Agent SDK as the key-aware default adapter. App §0 ranks DIRECTIVE above PRD, CONTRACT and SPEC, but the Codex-only preambles in those three documents come from D-GOV-43. D-GOV-43 undercuts 2.8 without naming it: grep of the D-GOV-43 IMPACT finds no reference to App DIRECTIVE 2.8. That matches the §1 case "a ruling undercuts an unamended GOVERNING clause without naming it".
- **CLM-003, CLM-011, CLM-024.** The reach tags hold at symbol level:
  - `AgentEnginePort` is imported by the LIVE `core/src/engine-registry.ts`.
  - The SDK manager, options builder, permission overlay and message mapper are LEGACY_ONLY.
  - `run-logger.ts` `redactConfiguredApiKeys` has a live importer in `lib/woven-dialogue/chat-organization.ts`.
- **PostReleaseBasis.** `NO` is correct on every sampled row. No cited file appears on `TOUCHED_PATHS.csv`: package.json, the harness modules, agent-engine-port, the decomposition, the deliverable files and the App docs.

## (iii) Capability-file inaccuracies

- **CAP-RTCONTRACT-045.** Tagged `REACH=LEGACY_ONLY`, while `REACHABILITY.csv` marks `contracts/src/harness/sdk-version.ts` LIVE (via the contracts barrel from `daemon/src/standalone-bin.ts`). At symbol level, `CLAUDE_AGENT_SDK_PACKAGE_VERSION` is consumed only by `claude-agent-sdk-manager.ts` and `runtime-fingerprint.ts`, and both are LEGACY_ONLY. The capability tag is therefore correct at symbol level, and this is the GRADING_KEY 1 module-versus-symbol case.
- **CAP-BUILD-012.** Tagged `REACH=LIVE; BUILD-TIME`. The script is chained in `desktop:pack` and `desktop:dist` (package.json:42-43) and is enabled. However, it is not reached from a §9 product entry point. The qualifier is informative, but it is outside the REACH vocabulary. This is minor.
- **CAP-HARNESS-032.** No issue found.

## (iv) Effort

About 25 targeted reads and greps were made at the frozen tree. The files covered were:
- App DIRECTIVE §0 and §2.8, the PRD, CONTRACT and SPEC preambles, and Root DIRECTIVE §7;
- the DEL-04-01 ScopeOfWork, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, the Decision record, the DAPP52 evidence and INSP-03;
- the decomposition rows and the SCA-APP-009 Impact_Assessment;
- the harness symbols and their importers;
- the evidence-pack CSVs.

Read-only git was used for log and log -S. The context budget was not tight.
