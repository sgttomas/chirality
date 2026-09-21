# DEL-10-03 — reverse-pass notes

**Inputs.** Seven capability files, concatenated in the manager's order: BUILD, ELECTRON,
HARNESS, INSTRUCTIONS, RTCONTRACT, SETTINGS, WORKSPACE. Together they hold 286 rows.

**Responses.**

| Response | Rows | Capabilities |
|---|---:|---|
| CLAIMED_BY | 2 | HARNESS-055 → CLM-015; RTCONTRACT-041 → CLM-010.1 |
| PARTIAL | 5 | HARNESS-053 → CLM-007; RTCONTRACT-040 → CLM-010.7; RTCONTRACT-043 → CLM-010.5; RTCONTRACT-044 → CLM-015; SETTINGS-042 → REGISTER-5 |
| NOT_MINE | 279 | Everything else |

**Errata: none.** The sealed ledger is unchanged; its SHA-256 still reproduces as
`527584cf…0a70`. Sealed and errata-applied census figures are therefore identical (see
`DEL-10-03_notes.md` §1).

**REACH difference, recorded but not raised as an erratum.**
- CAP-RTCONTRACT-041 and CAP-RTCONTRACT-040 tag the contract modules `REACH=TEST_ONLY`, because
  they have no non-test consumer.
- The forward ledger tags `operation-proposal.ts` and `domain-profile.ts` `REACH=LIVE`. That tag
  follows the evidence-pack REACHABILITY.csv module map, as CONVENTIONS §2.3 [INTEG] requires,
  and the rows already note "inert: consumed by no runtime code".
- No Disposition changes either way:
  - these are data-model shape claims, judged at the contract surface;
  - the live-path behavioural rows (CLM-010.3/.4/.5) rest on the absence of any apply path, not
    on the reach of the type.
- **For the manager / R3:** decide whether a symbol-level TEST_ONLY override of the module map
  should be adopted run-wide.

**Coverage gaps (for the manager; they cannot be added as errata).**
- CAP-BUILD-040, the D-APP-52 live-LLM demo driver. DEL-10-03's `_STATUS.md` History (2026-07-18)
  and `Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18.md` record this demonstration as the discharge of
  a former DEL-10-03 Remaining item. No forward row covers that history claim, because it is a
  dated history line and not an indexed unit. I answered NOT_MINE, since CLM-015 assigns PEC
  fixture evidence to DEL-10-04 and D-APP-70 §9 selects DEL-10-04 as primary for the pec
  evidence drivers.
- CAP-BUILD-038 and CAP-BUILD-039: NOT_MINE on the same D-APP-70 §9 basis. DEL-10-03 keeps a
  verification interest in them, per that ruling.

**Validation.** `validate_ledger.py reverse` was run once per capability file (7 runs). Every run
returned `RESULT PASS errors=0 warnings=0`.
