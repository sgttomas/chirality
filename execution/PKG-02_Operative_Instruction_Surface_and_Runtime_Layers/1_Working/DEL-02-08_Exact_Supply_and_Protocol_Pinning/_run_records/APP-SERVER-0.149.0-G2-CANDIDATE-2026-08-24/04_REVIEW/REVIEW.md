# N4 Fresh Candidate Review

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

**Verdict:** `PASS_WITH_DOCUMENTED_GAPS`

**Actionable findings remaining:** `0`

## Review scope

The review reread the six cumulative owner instruments, the N1–N3 durable
returns, all structured primary/equivalence/empirical evidence, every N4
candidate file, and the evidence hash chain. It checked exact identities,
claim calibration, decision boundaries, owner-facing completeness, and N4
write scope.

## Checks

| Check | Result |
| --- | --- |
| six governing instrument SHA-256 identities | `PASS` |
| N1, N2, N2b, and corrected N3 return identities | `PASS` |
| every row in `EVIDENCE_HASH_MANIFEST.csv` against repository bytes | `PASS` |
| every row in N3 `ARTIFACT_HASHES.csv`, including normalized/gzipped raw traces | `PASS` |
| JSON parse for all candidate JSON | `PASS` |
| three archive names, sizes, and SHA-256 values | `PASS` |
| app-server 3/3 payload equivalence at `b1d1a8c3…` | `PASS` |
| signature/license/notice/redistribution facts | `PASS` |
| exact `features.plugins` name/default/current/false override | `PASS` |
| three denied destinations, triggers, and dispositions | `PASS` |
| committed traces record completed connections / credential prompts / external writes all zero | `PASS` |
| per-run gate evidence | `PASS_WITH_DOCUMENTED_GAP` — 9 complete; `version` record unavailable |
| configuration and `multi_agent_v2` precedence calibration | `PASS` |
| feature pagination, 118 unique names, and stage/enable counts | `PASS` |
| schema/type/schema-derived method gaps carried exactly | `PASS` |
| R13-B G5 finding carried without disposition | `PASS` |
| OUT-002 inventory distinguished from a complete endpoint policy | `PASS` |
| no G2 acceptance, pin amendment, implementation, cutover, or reliance claim | `PASS` |
| TM-ROOT-106/122 and ten held DEL-02-06 bindings unchanged | `PASS` |
| candidate file hashes in `HASH_VERIFICATION.csv` | `PASS` |
| `git diff --check` | `PASS` |

## Findings repaired during review

1. **Feature baseline calibration.** An inherited structured summary initially
   mixed the explicit `plugins=false` probe with the baseline feature row. N3
   was corrected without vendor re-execution before N4 restarted. The stable
   raw baseline proves `plugins enabled=true/defaultEnabled=true`; the explicit
   override proves `false/true`. N4 pins only the corrected N3 identities.
2. **Enabled-feature count.** Draft N4 prose initially repeated the pre-repair
   count of 41 enabled entries. Direct recomputation over the corrected 118-row
   inventory returned 42 enabled and 42 default-enabled; the N4 files were
   repaired.
3. **Hold boundary.** Draft prose said existing DEL-02-06 holds were unchanged
   without the accepted count. N4 now states explicitly that all ten bindings
   remain held and unchanged.
4. **Packaging-versus-payload digest correction.** The `.zst` row in
   `EQUIVALENCE_INVENTORY.md` incorrectly carried the decompressed payload
   digest `b1d1a8c3…de2` in the archive slot. The row is corrected to the
   official archive digest `c4c31ecd…73677`, and the dependent N2b and N4 hash
   chains were regenerated without download, vendor execution, or network
   probe. `EQUIVALENCE_RESULTS.json`, official release metadata, and the
   consolidated supply manifest independently agree with the corrected value.
5. **Per-run gate calibration on owner return.** Deterministic reinspection of
   the committed raw evidence found nine per-run gate-hash records and nine
   attributable denial-preflight records, not ten. The `version` preflight
   records are empty and no `version.gate_hashes.txt.gz` exists. The standalone
   preflight cannot be attributed to that invocation. All dependent summaries
   now carry `VERSION_RUN_GATE_EVIDENCE_UNAVAILABLE_UNDER_BOUNDS`; no vendor
   code was rerun.
6. **README hash false positive rejected.** An initial parent audit resolved
   the candidate-relative `README.md` path against the repository root and
   incorrectly suspected a stale hash. Correct candidate-relative resolution
   proves the prior `033710f8…` value matched the pre-correction candidate
   exactly. The table was regenerated only because this correction adds a
   return note to the candidate README.

## Documented gaps, not review findings

Generated JSON schema, generated TypeScript types, the exhaustive
schema-derived stable/experimental method inventories, and the version-run
gate record remain `UNAVAILABLE_UNDER_BOUNDS`. The invalid published vendor
signature remains the named R13-B G5 finding. These are deliberately visible
on the G2 decision surface and require owner disposition; they are not
silently narrowed or misstated by N4.

## Final conclusion

After the deterministic corrections, the candidate is internally consistent,
hash-pinned, traceable to the exact 0.149.0 supply bytes and the calibrated
bounded empirical evidence, and explicit about its gaps and negative grants.
Fresh review returns `PASS_WITH_DOCUMENTED_GAPS` with zero actionable
findings. G2 acceptance remains the owner's separate act.
