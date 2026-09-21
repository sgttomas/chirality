# V-DEL-01-04 verifier notes (PKG-01, R2)

Shard `V-DEL-01-04`, unit `DEL-01-04`, 37 items. Frozen basis `00115c719`. Sealed ledger, errata and
reverse files read by script; none edited.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT) | 12 | 9 | 0 | 3 |
| a30 | 10 | 9 | 0 | 1 |
| b (ALIGNED) | 4 | 4 | 0 | 0 |
| c (reverse PARTIAL) | 9 | 9 | 0 | 0 |
| e (errata) | 2 | 2 | 0 | 0 |
| **Total** | **37** | **33** | **0** | **4** |

No verdict-field (Disposition / Response) refutation. All four CONTESTED items are on
`HumanDecisionNeeded`, so none counts toward the Addendum 3 rerun threshold.

## (ii) Patterns

1. **Authority routing (grading key 4) holds on all 12 AUTHORITY_CONFLICT rows.**
   - App DIRECTIVE §0 ranks App documents only. It does not place Root D-GOV rulings.
   - Every conflict row sets a GOVERNING ruling against an unamended clause that the ruling does not name:
     - D-GOV-43 item 3: shared plugins and MCP definitions, no effective-configuration veto.
     - D-GOV-43 item 4: "Full access is available by explicit user choice".
     - The Codex sole-engine rule, which D-GOV-43 item 14 keeps.
   - The unamended clauses are DIRECTIVE §4.2 (lines 263–265), DIRECTIVE §2.8 (line 117) and K-PERM-6. The CONTRACT and PRD preambles read only K-NET-1 and K-RELEASE-1 with D-GOV-43 items 1 and 4. Amended K-NET-1 still says remote MCP fails closed.
   - D-GOV-43's list of amended surfaces names only Root DIRECTIVE §5 and §7. It never names App DIRECTIVE §2.8 or §4.2.
   - No row lets a lower preamble override a higher, unamended source. STATE-2 and STATE-4 apply the §0 order explicitly and still route the ruling correctly.
   - The §0 order resolves none of the 12 rows, because in every case the disagreement is ruling against document, not document against document.
   - Plain `R4` fits wherever it is used: no named question R4-Q1..Q5 covers "D-GOV-43 items 3–4 or the sole-engine rule against DIRECTIVE §2.8/§4.2 and K-PERM-6". The worker's method-friction note proposes framing that question.
2. **R4-Q1 on bundled claims (grading key 4a, CONTESTED).**
   - Keys: CLM-003.5, CLM-006.2 and CLM-024.
   - Each claim bundles an ambient-settings exclusion with a shipped-bypass exclusion.
   - The ledger itself records the settings half as met on LIVE (CLM-010.3). The guarded-bypass half is met only by `REACH=LEGACY_ONLY` `sdk-options-builder.ts:55-59`.
   - Rule 3 and Addendum 8 ("the only code meeting the claim") give no clear answer for a partly-LIVE bundle.
   - CLM-010.4 (bypass only) and CLM-025 (the other rows have no code evidence) cite R4-Q1 cleanly and are CONFIRMED.
3. **CLM-004.5 (CONTESTED on HumanDecisionNeeded).**
   - The residual work is to add the unsurfaced conflicts to the CLM-027 conflict table. That is a text repair that needs no ruling, which points to `NO`.
   - Either value is defensible, because the rulings those conflicts await are carried on CLM-003.4, CLM-003.5 and STATE-2.
4. **Evidence and field checks passed:**
   - All code line anchors match their content at the frozen tree: effective home 41–89; chat-panel 129–133 and 2132–2135; delegated.ts 322–330; delegated-runtime 320; codex-supervisor 44, 104–108 and 261; app-server client 41 and 52; electron main 475–478 and 831; sdk-options-builder 30–33, 55–59 and 248.
   - The REACH tags match `REACHABILITY.csv`.
   - PostReleaseBasis `NO` is correct: no cited codex-supervisor line falls in a da95ec194 range.
   - REGISTER-1 hashes and git history are confirmed.
   - Errata: `domain-profile.ts` has no non-test importer, only the contracts barrel, so it is TEST_ONLY at symbol level. The Pi packages are devDependencies. Both ProposedValues are correct.

## (iii) Effort

- **Read:** about 25 files or slices:
  - rulebook, basis, brief and ledger rows;
  - App DIRECTIVE §0, §2.8 and §4.2; the CONTRACT preamble, K-ENGINE-3, K-PERM-6 and K-NET-1; the PRD preamble;
  - the D-GOV-43 record (items, findings, IMPACT App table), D-APP-127 (grep) and the engine-policy notice (grep);
  - DEL-01-04 SoW, `_REFERENCES`, `_CONTEXT` and INSP-03;
  - the cited code and the capability rows.
- **Git:** read-only `log` on the frozen tree.
- **Out of bounds:** Root `execution/` and `chirality-runtime/execution/` were not read.
- **Context budget:** comfortable.
