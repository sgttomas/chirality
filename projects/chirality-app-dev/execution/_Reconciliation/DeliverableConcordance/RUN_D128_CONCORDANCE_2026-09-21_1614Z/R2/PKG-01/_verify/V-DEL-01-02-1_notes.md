# V-DEL-01-02-1 — verifier notes (DEL-01-02, 39 items)

Graded against CONVENTIONS.md, RUN_BASIS §3/§5 and Addenda 1–7, the shared grading key in
`BRIEFS/VERIFIER_BRIEF.md`, and the HELP_HUMAN clarification to key 4a. That clarification says
TEST_ONLY code does not meet a product claim, and an R4-Q1 difference that arises only from it
is graded CONTESTED. All evidence comes from the frozen tree at `00115c719`, inside the
permitted roots. No Root `execution/` or Runtime `execution/` material was read.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT, LOW/self-flag, REMAINING_WORK) | 14 | 8 | 4 | 2 |
| a30 (sample of other non-ALIGNED) | 25 | 20 | 4 | 1 |
| **Total** | **39** | **28** | **8** | **3** |

- **Refutations on a verdict field (Disposition): 0.** All 8 REFUTED items are field-level: ImplementationEvidence, VerificationEvidence, DirectionEvidence, RemainingWork or Notes.
- **CONTESTED items that touch Disposition: 3.**
  - CLM-038.3 and CLM-059.3: the row's own LEAST-CONFIDENT flag already names the alternative.
  - CLM-006.3: contested on Disposition and on HumanDecisionNeeded.
- **Disposition questions noted inside refuted items:**
  - CLM-038.2: the Disposition is contested as well as the evidence being refuted.
  - CLM-006.8 and CLM-018.16: the Disposition still holds, but on thinner evidence.
- **The AUTHORITY_CONFLICT rows are all confirmed.** Checked: CLM-006.7, CLM-007.3, CLM-018.5, CLM-018.8, STATE-1, CLM-040 and CLM-044.
  - Neither D-GOV-43 nor D-APP-127 names App DIRECTIVE §2.8 or §5, K-SDK-1 or K-PERM-1/6.
  - IMPACT.md:56 names Root DIRECTIVE, not App DIRECTIVE.
  - None of these rows lets a lower preamble override a higher unamended source.
  - Their R4-Q1/R4-Q5 and plain-R4 citations fit.

## (ii) Systematic patterns

1. **Module-level LIVE tags where the specific symbol is not live (grading key 3).** Examples: CLM-006.1, CLM-006.13, CLM-006.8, CLM-018.16.
   - `engine-conformance.ts` is LIVE only through `contracts/src/harness/index.ts:3` (a re-export). `runEngineConformance` is called only from tests.
   - `GovernedAgent1RunCoordinator` is never constructed. `app-owned-composition.ts:226` passes `agent1Runs = undefined`, so `runAgent1` throws `REQUIRED_DELEGATION_MISSING`.
   - On CLM-006.8 and CLM-018.16, this removes the strongest live evidence behind PARTIALLY_IMPLEMENTED. Only envelope validation remains (`delegated-runtime.ts:100-115`).
2. **Split halves disagree on the same authority question.**
   - K-PERM-1 hard-deny precedence against D-GOV-43 item 4:
     - S2 (CLM-044) calls it AUTHORITY_CONFLICT.
     - S1 (CLM-006.3) calls it IMPLEMENTED_DIFFERENTLY with R4-Q1. This is graded CONTESTED.
   - App DIRECTIVE §2.8 (Claude first adapter) against the Codex sole-engine rule:
     - CLM-040 and STATE-1 call it AUTHORITY_CONFLICT.
     - The BLK-RBR-003 row (CLM-038.3) calls it STALE_SPECIFICATION with "authority route: none". This is graded CONTESTED.
   - R3 may want to cluster these rows together.
3. **Evidence and gloss slips in S2 blocker/TBD rows.**
   - CLM-038.2 miscounts the live register surfaces. `sanitize.ts`, `deliverable-contracts.ts` and the status route are also LIVE.
   - CLM-059.5 misses `contract-pins.manifest.ts:410-440`, which does validate the register's schema and inventory. Its RemainingWork and its ALIGNED alternative are therefore wrong.
   - CLM-026 says the A2 re-hash was "not applied to this deliverable". In fact, `23b3879b3` re-hashed DEL-01-02's `_REFERENCES.md`, and later corpus edits caused the drift.
4. **Minor, not graded as refutations.**
   - **AssessmentEvidence for INSP-03 PASS rows.**
     - S1 marks CLM-018.8, CLM-018.12, CLM-018.15 and CLM-018.16 OVERTAKEN ("not a live-path conclusion").
     - S2 marks CLM-044 STILL CURRENT "at module level" in the same situation.
     - The validation IDs still exist, so the literal MR-1 reading favours STILL CURRENT. Both halves have exactly one token.
   - **CLM-018.5** lacks the test case name. It is REFUTED on VerificationEvidence (§2.3); the row disclosed this itself.
   - **CLM-005** omits SOW-074 at decomp :477. This is immaterial.

## (iii) Effort

- **Files read:** about 35 files or line ranges, including:
  - the DEL-01-02 SoW, `_STATUS`, `_CONTEXT`, `_REFERENCES` and INSP-03;
  - the register;
  - App DIRECTIVE and CONTRACT;
  - D-GOV-43 proposed/IMPACT and D-APP-127;
  - about 15 Runtime and frontend source and test files;
  - the evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES).
- **Git:** read-only `git log` and `show` against the frozen tree (`23b3879b3`, corpus-doc history).
- **Budget:** moderate. Most time went to the symbol-level reach tracing for pattern 1.
