# DEL-08-03 — reverse-pass notes (RUN_D128, R2 PKG-08)

I answered all 360 rows of `REVERSE_INPUT_capabilities.csv` in `DEL-08-03_reverse.csv`. The input covers eight areas: BUILD, ELECTRON, HARNESS, ROUTES, RTCONTRACT, SHELL, WORKSPACE and WOVEN.

- **Validator:** `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.
- **Sealed ledger:** SHA-256 re-checked and unchanged: `e652bd88823b28855dfc98c7327d9ef68e4e4296afa71f76b3773038945f4bb7`.

## Responses

| Response | Rows |
|---|---:|
| NOT_MINE | 349 |
| PARTIAL | 8 |
| CLAIMED_BY | 3 |

**CLAIMED_BY (3)**

| Capability | ClaimKey |
|---|---|
| WORKSPACE-036 (dispatch contract) | SEC-1 |
| WORKSPACE-029 (task-scope normalization and sanitization) | CLM-013.7 |
| WORKSPACE-012 (knowledge-type buckets) | CLM-013.8 |

**PARTIAL (8)**

| Capability | ClaimKey | Why only partial |
|---|---|---|
| WORKSPACE-030 (Pipeline selectors) | CLM-013.1 | Retired presentation; DEL-02-02 owns the presentation. |
| WORKSPACE-008 (deliverables scan context) | CLM-013.10 | Shared provider. |
| ROUTES-028 (`/api/project/deliverables`) | CLM-013.10 | — |
| ROUTES-029 (`/api/working-root/scope`) | CLM-016 | Referenced only by wording that is stale under D-APP-56 P21. |
| WOVEN-001 (route discards the legacy prop) | SEC-1 | — |
| ROUTES-042 (`/pipeline` deep link) | SEC-1 | — |
| WOVEN-025 (live native-child Agents view) | CLM-013.14 | — |
| WOVEN-041 (unmounted Work projection) | CLM-013.14 | — |

**Notable NOT_MINE rows**

- **Pipeline-hosted but out of scope:**
  - scaffold form WORKSPACE-031, HARNESS-022, ROUTES-021;
  - lifecycle contracts panel WORKSPACE-032. CLM-012 and REQ-016 exclude these.
- **Owned by DEL-08-04:** HARNESS-058, the legacy subagent governance gates.
- **Scope-scan implementation:** WORKSPACE-018.

## Errata

None. The area notes confirm the sealed forward rows and do not contradict them. Two points add detail beyond what the sealed rows record:

- **WORKSPACE-008 / WORKSPACE-012.**
  - `DeliverablesProvider` fetches `/api/project/deliverables` on every root change.
  - Only the retired Pipeline reads `knowledgeTypes`. The live document view uses `deliverables` and `deliverableContracts`.
  - CLM-013.10 says "the scan runs live". That is still true, but its knowledge output has no rendered consumer. This refines CLM-013.10 but does not change its Disposition, so I did not file an erratum.
- **ROUTES-042 / WOVEN-001.** `WovenDialogueShell` also ignores `defaultSurface` (`woven-dialogue-shell.tsx:77`). This is consistent with SEC-1 and CLM-013.1.

## Coverage gaps

None found. Every capability that carries DEL-08-03 semantics maps to an existing forward row. Nothing in the eight areas owns anything that DEL-08-03 claims but that is missing from the ledger.

Two claim-to-capability observations:

- The duplicated Pipeline option tables in `pipeline-surface.tsx` and `pipeline-dispatch-contract.ts` (WORKSPACE notes) are already recorded at CLM-006 and CLM-013.13.
- `buildDeliverableCompositeKey` is defined twice, in `task-scope.ts` and `filesystem.ts` (WORKSPACE notes). This is not a DEL-08-03 claim, so I raised no row.
