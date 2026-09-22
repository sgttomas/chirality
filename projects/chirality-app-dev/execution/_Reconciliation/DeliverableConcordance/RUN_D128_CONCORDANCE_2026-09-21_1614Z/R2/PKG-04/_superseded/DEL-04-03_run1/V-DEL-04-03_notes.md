# V-DEL-04-03: verifier shard notes (R2, PKG-04)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 3 | 0 | 1 | 2 |
| n | 13 | 7 | 2 | 4 |
| b | 2 | 2 | 0 | 0 |
| c | 3 | 3 | 0 | 0 |
| e | 5 | 5 | 0 | 0 |
| **Total** | **26** | **17** | **3** | **6** |

There are no Disposition-level refutations. All 3 refutations are field-level: HumanDecisionNeeded on CLM-004.5, and DirectionEvidence on CLM-003 and CLM-023. All 6 CONTESTED rows contest the Disposition: CLM-009.3, CLM-009.12, CLM-002, CLM-009.2 and CLM-018.

## (ii) Systematic patterns

1. **Mapper-subject requirements are judged only on the live path (GRADING_KEY 2).** REQ002, REQ003 and REQ012 and the CLM-018 verification checks all name "the mapper" as their subject. The deliverable is the SdkMessageMapper, "or equivalent mapper module". Read at module level, the retained mapper satisfies them: INSP-03 recorded PASS, and the mapper is REACH=LEGACY_ONLY. Read on the live path, the Codex envelope diverges. Under the key these rows are CONTESTED rather than CONFIRMED. Keys: CLM-009.2, CLM-009.3, CLM-009.12, CLM-018.
2. **CTX: is used for declared-state carriers (GRADING_KEY 5).** `Dependencies.csv` (DEP-04-03-007) is cited as `CTX:`, and so is `_CONTEXT.md` in CLM-008, which is class c and so is not graded here. RUN_BASIS §5 classes both as Declared state, not CONTEXT. The probe closure was a D-APP-52 act, so it is better cited as `GOV:D-APP-52`. Keys: CLM-003, CLM-023 (also CLM-008).
3. **K-EVENT-6 is not cited on the redaction rows.** App CONTRACT K-EVENT-6, as amended under D-GOV-43, keeps structural redaction before every sink and preserves payloads *after* redaction. That rules out the LEAST-CONFIDENT alternative (ACCEPTED_DIVERGENCE, or "no key so nothing to redact"). It also makes the live gap a repair rather than an R4-Q1 question. I confirmed that the live path has no redaction step: the delegated adapter carries `params` verbatim, `session-store.persistEvent` appends directly, and the only runtime redaction is stderr e-mail in the codex-app-server-client. The contracts `types.ts:336` comment even describes the harness:event as "redacted". Keys: CLM-004.5, CLM-009.12.
4. The reach errata are correct. Symbol-level reach for engine-conformance is TEST_ONLY: the module is LIVE only through the harness barrel. `validate-harness-section9.mjs` is imported by a vitest file and run by npm and validation scripts, so TEST_ONLY fits better than LEGACY_ONLY/UNREACHED. The pack's REACHABILITY.csv does not map `frontend/scripts/**`. Nothing in the rulebook says whether an npm or CI validation script counts as a "test" entry. I flagged this as a §2.3 ambiguity.
5. CLM-002 is the hash-drift SoW cell. It says the PRD "has HASH_MISMATCH", and the recompute does mismatch. The now-false record is `_REFERENCES.md` MATCH (REGISTER-1), so it is unclear whether the SoW cell is itself a defect.

## (iii) Capability-file observations

- CAP-RTCONTRACT-039 (engine conformance): REACH=TEST_ONLY checks out at symbol level.
- CAP-BUILD-027: REACH=TEST_ONLY and its entry points (the npm script, premerge and release-quality validators) check out.
- CAP-RTCONTRACT-051: REACH=TEST_ONLY and STATE=DISABLED are consistent. I found no non-test source importer of `engine-pi-omlx` in the runtime packages or the App src/electron.
- CAP-RTCONTRACT-036: REACH=LIVE (type-only through the delegated adapter) holds.
- No inaccuracies found.

## (iv) Effort

About 25 targeted reads and greps of the frozen tree: the SoW, _REFERENCES, Dependencies, _CONTEXT, _STATUS, the INSP-03 assessment, delegated-engine-adapter, turn-coordinator, session-store, codex-supervisor, contracts types and event-schema, engine-conformance importers, the section9 script, and App DIRECTIVE §0/§2.10, SPEC §9.2/§10.3/§11 and CONTRACT K-EVENT-6. I also read the evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES) and the SURFACES rows. PostReleaseBasis: none of the cited lines fall in TOUCHED_PATHS ranges. codex-supervisor.ts:546-560 sits between the touched ranges 535-544 and 570-573, so every row's `NO` stands. The context budget was not tight.
