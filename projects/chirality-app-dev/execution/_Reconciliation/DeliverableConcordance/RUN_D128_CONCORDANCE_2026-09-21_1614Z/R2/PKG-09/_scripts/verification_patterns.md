## §4 Rerun decisions (hand-written by the PKG-09 manager)

Threshold computed by `_scripts/threshold.py` separately on ledger rows (classes a, a30, b, e; verdict field =
Disposition) and on reverse responses (class c; verdict field = Response or its ClaimKey), per RUN_BASIS Addendum 3:

| Shard | Ledger rows checked (distinct) | Disposition REFUTED | Ledger share | Reverse responses checked | Response REFUTED | Reverse share | Rerun? |
|---|---:|---:|---:|---:|---:|---:|---|
| V-DEL-09-01 | 13 | 0 | 0.0% | 2 | 0 | 0.0% | no |
| V-DEL-09-02_A | 21 | 0 | 0.0% | 1 | 0 | 0.0% | no |
| V-DEL-09-03 | 21 | 0 | 0.0% | 7 | 0 | 0.0% | no |
| V-DEL-09-04 | 25 | 2 | 8.0% | 10 | 0 | 0.0% | no |
| V-DEL-09-05 | 26 | 0 | 0.0% | 6 | 0 | 0.0% | no |
| V-DEL-09-06 | 27 | 0 | 0.0% | 11 | 0 | 0.0% | no |
| V-DEL-09-07 | 8 | 0 | 0.0% | 0 | 0 | 0.0% | no |

- No structural failure; no ledger crosses 10% on either measure. **No reruns.** DEL-09-04 is the closest
  (2 of 25 = 8.0%): both refutations are the P2 half's AUTHORITY_CONFLICT on the release-signing posture (below).
- Field-level refutations (13 CORRECTIONS.csv rows, incl. the HumanDecisionNeeded half of the two DEL-09-04 Disposition refutations) are recorded by `_scripts/corrections.py` in `CORRECTIONS.csv`; nobody edited a
  sealed ledger. Two class-e refutations (DEL-09-03 errata on CLM-003 and CLM-009.12) mean the **sealed** value
  stands; R3 must not apply those two errata (CORRECTIONS.csv carries the verifier's reading for them).

## §5 Patterns (hand-written; evidence, not rulings)

1. **Release-signing posture: the split parts disagreed, the verifiers side with STALE_SPECIFICATION.**
   DEL-09-04 P1 and DEL-09-05 P1 read SoW text keeping the release unsigned/unnotarized as STALE_SPECIFICATION
   (App CONTRACT preamble line 17, amended by `23b3879b3`, names K-RELEASE-1 and reads it with D-GOV-43; SPEC
   §19.4 and PRD §12.8 name a signed and notarized consolidated candidate; DIRECTIVE §0 order). DEL-09-04 P2
   (CLM-022, CLM-023.3) and DEL-09-05 P2 (CLM-026) marked AUTHORITY_CONFLICT with plain R4 because the K-RELEASE-1
   row text and PRD §6.2 are unamended. V-DEL-09-04 **REFUTED** the P2 reading on Disposition (MR-11 applies:
   the amendment names the clause); V-DEL-09-05 graded the same question on CLM-026 **CONTESTED** (the D-APP-97
   F-APP-2 fence on signing is also unamended). R3 should resolve all four rows together; done-declaration
   Q-02 (release act vs F-APP-2) is the CONTEXT behind it and is not a ruling.
2. **G6a phase gate (DEL-09-05).** CLM-016.3 AUTHORITY_CONFLICT + R4 was CONFIRMED: D-APP-127 never names G6a and
   decomposition v3_2 line 382 is unamended; P2's REGISTER-52 treats G6a as retired on `_STATUS` carrier text alone
   and needs R3 review alongside it.
3. **Build and validation script reach was graded inconsistently, by manager-brief ambiguity.** The worker brief
   made a script LIVE when a `package.json` *release or packaging* script invokes it; the DEL-09-01 dispatch
   note widened that to any `package.json` script or the in-root workflow. R1b's BUILD capability file tags the
   Section 8/9, premerge, release-quality and `proof:*` scripts TEST_ONLY. Workers split three ways (02_A/B, 01,
   05 kept LIVE; 03 and 06 filed errata to TEST_ONLY), and V-DEL-09-03 REFUTED DEL-09-03's two errata because
   `validate:release-quality` runs `npm run test` by default. No Disposition depends on it, but R3's scripted
   R4-Q1 re-derivation from REACH tags must not treat the manual `proof:*` scripts' `LEGACY_ONLY`/TEST_ONLY tags
   as evidence of retained-harness obligation (DEL-09-04 reverse notes, DEL-09-05 reverse notes).
4. **Split-and-merge seams.** SEE links could not cross parts at sealing (DEL-09-04 CLM-001 → REGISTER-51 REFUTED
   on Notes; DEL-09-05 errata added the three missing SEE links, CONFIRMED), and one tiering inconsistency
   (DEL-09-04 CLM-019 LOCAL_DESIGN vs CLM-001 NOT_APPLICABLE, REFUTED on AuthorityTier). A future split should
   assign all REGISTER rows to one part and let the other part cite them by key.
5. **R4-Q6 lag.** DEL-09-03 cited R4-Q6 on three rows after the Addendum 9 notice but missed it on CLM-017 and
   CLM-023 (K-PERM-1 hard-deny precedence; REFUTED on HumanDecisionNeeded). DEL-09-02_A CLM-010.6 (K-PERM-1..4)
   sealed before Addendum 9 and maps to R4-Q6 (noted, not refuted).
6. **Retirement handling (DEL-09-07).** RETIRED_BY_RULING on 15 rows passed the strict §2.6 (iii) check (D-APP-127
   names the deliverable and preserves the folder, its SoW and D-APP-104 as history). REGISTER-1 is CONTESTED:
   the ruling preserves `_REFERENCES.md` as history, but the validator allows only REMAINING_STATE_MISMATCH or
   STALE_SPECIFICATION on a REGISTER_DEFECT row (method friction for R3).
7. **Addendum 10 (owner direction, received after every shard returned).** No verifier graded against it. Rows
   whose verdict leans on the absence of an in-root record of an out-of-code event are listed under
   "OWNER_CHECK candidates" in `PACKAGE_SUMMARY.md` §8 for R3 to put to the owner; the owner has stated that
   v3.0.1 was notarized, as v3.0.0 was.
8. **Out-of-root limits.** The repository-root `.github/workflows/**` (desktop-release-template, the executed
   harness-premerge) was not read by any worker or verifier. Items that turn on it (DEL-09-05 CLM-010.9 secret
   scan "not chained from CI"; DEL-09-01 CLM-003 actual CI behaviour) are unconfirmed, not refuted.
