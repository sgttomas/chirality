# A2 Adversarial Verification Return

Verdict: `OWNER_PRESENTABLE`

| Severity | Finding | Evidence | Required repair |
|---|---|---|---|
| NOTE | No substantive defect found. `WORK_GRAPH.json` still shows A2/FANIN pending because this return has not yet been integrated. | Active AgentRun work graph and launch briefs. | None; ordinary parent fan-in finalization only. |

Preservation result: `PASS`

- D-APP-84 Root conditions and “H1 grants no Bash now” are explicit.
- UI/API parity remains unselected; DEL-05-04 lines 11–32 are excluded entirely.
- All six D-APP-81 historical relations remain `HISTORICAL_RELATION_UNKNOWN`.
- Both Task Management registers, lifecycle states, Checking Approval SHAs, authority, decomposition, dependency truth, runtime/source behavior, release/issuance, and no-blanket-closure boundaries are preserved.
- Current changes are path-contained to the packet, D-APP-85 register row, and AgentRun.

Exact-scope result: `PASS`

- D-APP-85 is the next unused decision ID.
- C01–C18 comprise exactly 18 rows, each marked only `CANDIDATE_FOR_VERIFICATION`.
- C03 correctly includes DEL-02-05 `_STATUS.md:11`.
- DEL-05-04 is absent from the candidate population.
- C12 correctly binds the complete DEL-08-03 block at lines 11–26.
- Every named sibling exclusion remains outside disposition.
- No evidence is treated as authority or as a satisfaction finding.

Activation/repair-gate result: `PASS`

- Option A requires ruling/register merge to `main` before discovery.
- Discovery is read-only and terminates at Gate 2 with an exact repair/no-change manifest.
- No target write, repair, receipt, or Git closeout is authorized before the later exact Gate-2 owner ruling.
- Option B is a genuine no-action deferral.
- No unsupported ordinary-maintenance bypass is offered.

Ruling-token result: `PASS`

```text
APPROVE D-APP-85 OPTION A: ACTIVATE THE NARROW READ-ONLY RECONCILIATION RUN AND STOP AT GATE 2.
```

```text
DEFER D-APP-85 OPTION B: NO ACTIVATION, DISCOVERY, OR REPAIR.
```

Both tokens are exact and unambiguous.
