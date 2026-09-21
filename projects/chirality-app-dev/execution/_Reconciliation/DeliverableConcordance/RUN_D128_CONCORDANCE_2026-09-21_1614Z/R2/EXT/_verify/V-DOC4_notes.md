# V-DOC4 notes (EXT verifier shard DOC4)

Shard DOC4 checked 43 items from the SELECTION_DOC4 snapshot. The items come from these ledgers:

- DOC-BUILDREL: 11 items.
- DOC-RQGATES: 7 items.
- DOC-RQRUN: 2 items.
- DOC-VALSTRAT: 5 items.
- DOC-RELIANCE: 18 items.

Each item has exactly one verdict line in `V-DOC4.csv`, giving 43 lines plus `#END`.

- Grading key: `BRIEFS/V_SHARD.md`.
- Evidence: read at the frozen basis `00115c719`.
- No errata files exist, so there are no class `e` items.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / AUTHORITY_CONFLICT / UNKNOWN) | 7 | 5 | 0 | 2 |
| b (30% of other non-ALIGNED) | 23 | 17 | 2 | 4 |
| c (15% of ALIGNED) | 13 | 11 | 2 | 0 |
| **Total** | **43** | **33** | **4** | **6** |

**By field:**

| Field | REFUTED | CONTESTED |
|---|---:|---:|
| Disposition | 0 | 5 |
| AuthorityTier | 3 | 0 |
| PostReleaseBasis | 1 | 0 |
| ImplementationEvidence (REACH) | 0 | 1 |

- **Verdict-field refutations: 0 of 43 distinct rows.** The Addendum 3 rerun threshold is not reached. All four REFUTED lines are field corrections for CORRECTIONS.csv.
- **REFUTED:**
  - `DOC:VALSTRAT#4.10` and `DOC:VALSTRAT#4.11`: AuthorityTier should be NOT_APPLICABLE.
  - `DOC:RELIANCE#12`: AuthorityTier should be GOVERNANCE_INVARIANT.
  - `DOC:RELIANCE#4.7`: PostReleaseBasis should be YES.
- **CONTESTED:**
  - Disposition: `DOC:RQGATES#2.2`, `DOC:RELIANCE#11.7`, `DOC:RELIANCE#11.8`, `DOC:RELIANCE#3.1` and `DOC:RELIANCE#3.8`.
  - ImplementationEvidence: `DOC:RELIANCE#3.11`.

## (ii) Systematic patterns

1. **The two workers tier command-table rows differently.**
   - DOC-VALSTRAT tiers its §3 command-table STATE_ASSERTION rows `LOCAL_DESIGN` (14 rows; two were sampled and refuted: `#4.10`, `#4.11`).
   - DOC-BUILDREL gives the same kind of rows `NOT_APPLICABLE`.
   - CONVENTIONS §2.3 and the worker brief put STATE_ASSERTION rows that restate no normative source at NOT_APPLICABLE. R3 may apply the same correction to the unsampled `DOC:VALSTRAT#4.x` rows and `#7`.
   - In the other direction, `DOC:RELIANCE#12` restates a D-GOV rule but is tiered NOT_APPLICABLE.
2. **The same underlying conflict gets different Dispositions.** The K-ENGINE-4 versus amended K-EVENT pass-through tension (R4-Q5) is:
   - `AUTHORITY_CONFLICT` in `DOC:RQGATES#5`;
   - `IMPLEMENTED_DIFFERENTLY` in `DOC:RELIANCE#3.1`.

   Similarly, legacy-only guarantee rows on the live Codex path fall on both sides of STALE_SPECIFICATION and IMPLEMENTED_DIFFERENTLY:
   - STALE_SPECIFICATION: `DOC:RQGATES#6`, `DOC:RELIANCE#3.2`, `DOC:RELIANCE#10`;
   - IMPLEMENTED_DIFFERENTLY: `DOC:RELIANCE#3.8`, `DOC:RELIANCE#3.11`.

   CONVENTIONS §2.3 ("met only on a LEGACY_ONLY path … IMPLEMENTED_DIFFERENTLY if the live path uses another mechanism") and the Addendum 5 tie-break do not settle this. R3 clustering should normalise it.
3. **R4-Q6 subjects are not cited.** These rows restate DIRECTIVE §2.8/§2.10/§4.2 against D-GOV-43:
   - `DOC:RELIANCE#3.8` (the unfiltered `~/.codex` link);
   - `DOC:RELIANCE#3.1` and `DOC:RELIANCE#3.14`.

   R4-Q6 was adopted after the EXT ledgers were sealed (EXT STATE.jsonl), so this is a mapping item for R3, not a worker error.
4. **Build-sequence tension.**
   - `DOC:BUILDREL#10.6` is STALE_SPECIFICATION because §8.2 omits the prepare steps (`instruction-root:prepare`, and also `runtime:build`, which the row does not mention).
   - `DOC:BUILDREL#9.1` and `DOC:RQGATES#10` list the same build/pack steps without those prepare steps and are ALIGNED.

   Both readings are defensible, since the latter two are evidence lists rather than procedures. The difference is recorded in ConventionIssue.
5. **REACH and PostReleaseBasis mechanics.**
   - `DOC:RELIANCE#3.11` uses the symbol-level `LEGACY_ONLY` tag from CAP-RTCONTRACT-042 for `tool-descriptor.ts`, but REACHABILITY.csv lists that file as LIVE. Its R4-Q1 citation depends on which tag R3 uses.
   - `DOC:RELIANCE#4.7` cites the touched file `codex-supervisor.ts` without line numbers. The relied-on `thread/start` call at line 219 blames to `da95ec194`. The SEE target `DOC:RELIANCE#3.7` (not sampled) has the same NO and likely the same defect.
   - Scripts and `package.json` are outside REACHABILITY.csv. The tags on them follow the BUILD capability file.
6. **Minor slips, recorded but not refuted.**
   - `pack-electron.mjs` REQUIRED_BUILD_INPUTS is cited as `:26-33`; it is `:27-34` at the frozen basis.
   - `DOC:RQGATES#2.10` says 51 of 54 deliverables; REFERENCE_HASHES.csv shows 52.
   - `DOC:RQRUN#2` omits CAUSE2:PRE_V3_DRIFT for the contract-deps pre-step (`ecc9c5a35`, 2026-07-02).
   - Some VerificationEvidence test paths are written `src/__tests__/…` instead of fully repo-relative.
   - R4-Q3 is used by analogy in `DOC:RELIANCE#3.10` and `#4.10`. The self-declared actor there is on the live deliverable route, not the legacy tool.
7. **Self-flagged LOW rows mostly hold.** Of the seven class `a` items, five are CONFIRMED. The remaining two are `DOC:RELIANCE#11.7` and `#11.8`, where the workers' own LEAST-CONFIDENT alternatives are equally supported and are graded CONTESTED.

## (iii) Effort

About 40 reads or greps:

- the five source documents, read in full;
- the rulebook sections and the evidence-pack CSVs;
- 4 AgentRuns records and the two workflow files;
- the capability-file rows for 19 CAP IDs;
- about 15 code and test excerpts;
- 7 `git log`/`blame -L` calls against the frozen tree.

No tests were run and nothing was installed. The context budget was adequate.
