# Repair cycle 1 — rehearsal command-transcript completeness

Finding: `PHASE0F-N1-R1-F1`

Disposition: `REPAIRED — READY FOR FRESH RE-REVIEW`

## Scope

This repair changed evidence and dependent record references only. It did not
rerun, revert, or alter Stage B or any live decomposition byte.

## Exact repair

`Gate_5_Rehearsal_Record.md` now records, in chronological order:

1. the initial scratch validator invocation and its `64/65` PASS, one-failure
   result;
2. the relative-source `/bin/cp` command executed from the scratch root, its
   same-file no-op limitation, the resulting duplicate `64/65` validator
   result, and failure JSON SHA-256
   `74aca90ec293c156f98c84486bee4c5bb2b6a61eae2d10db9cf87d5c948945df`;
3. the exact absolute governed-source `/bin/cp` that propagated repaired
   validator bytes into scratch;
4. the subsequent validator invocation that returned PASS 65/65, zero
   failures, and the final scratch JSON SHA-256
   `2001925dd5b2706d7f186a4d69bd54ecfc029d682dfa6916a18b9211e78f3112`.

The repair uses the original execution transcript. No command or result was
inferred.

Dependent SHA references were cascaded through
`Gate_5_Application_Record.md`, the `G5-EXECUTED-001` Decision Log row, and
the N1 return. `STATUS.json` required no semantic or hash-reference change.

## Before → after evidence hashes

| Target | Before SHA-256 | After SHA-256 |
|---|---|---|
| `Gate_5_Rehearsal_Record.md` | `0adbdc2d82d4dc13d92338d26cdb3edcaab631d892e369d7ba9ac1a9152316fe` | `ea5d90e88ebc7528f758664bf354f815deb8c50b638276ead19a5f49f9f92532` |
| `Gate_5_Application_Record.md` | `e73d7bc585f4faf4b6e0fc244b97d244d21b86fe30f07933961b0f55be6d1244` | `31207f122e9d64b4734a701cae364b2456df65d0605b2b1d0c6880ce5595760a` |
| `Decision_Log.md` | `c6de5a1671971bf87f526fc0a9fdaaa232ab457cce547db564e22905b02db931` | `90aa5da58be6ac97a7eec60762ac9f685d275dd80caaf694e7795496a1d5d0b1` |
| N1 `RETURN.md` | `1578ce61e086fc07b589a650a6f243b8bb45fdce01a4f885fe61073686e10153` | `24cc8f9270cd19698a3d8c9b1029d87d3ad3de407d875ade7df5496cc3406c68` |
| N1 `STATUS.json` | `992c6b0069979aa9d645518ef9d040791a919ba248ba41f5bee5124e2eebbd50` | `992c6b0069979aa9d645518ef9d040791a919ba248ba41f5bee5124e2eebbd50` |

## Validation rerun

Command:

```text
python3 execution/_ScopeChange/SCA-004_2026-08-22_1749/validate_gate5_applied.py
```

Result: `PASS: 65 checks, 0 failures`.

`Gate_5_Applied_Validation.json` was SHA-256
`f811bf1c08742833ef13ca0a503ecb8d5ac965a093b21f04767c4e8df6daa1b1`
before and after the rerun: byte-identical.

## Protected live R4-A proof

| Surface | SHA-256 | Result |
|---|---|---|
| Working surface | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` | R4-A MATCH |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` | R4-A MATCH |
| Scope ledger | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` | R4-A MATCH |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` | R4-A MATCH |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` | R4-A MATCH |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` | R4-A MATCH |
| Coverage telemetry | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` | R4-A MATCH |

Stage-B attempt count remains one. No live copy or append command was invoked
during this repair cycle.
