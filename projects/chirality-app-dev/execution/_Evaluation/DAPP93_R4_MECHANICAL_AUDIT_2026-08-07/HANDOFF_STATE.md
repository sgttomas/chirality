# D-APP-93 R4 mechanical audit — handoff state

Status: `EVALUATION COMPLETE — REPAIR REQUIRED`

Accepted upstream basis:

- R3 freeze: `2957d3f3a2a528a26dabecccfe91e8c2775e5c6942be5785b237a44252c22963`;
- R3 verifier BLOCK return: `528d6c3fea76bfb2e811c31891153a40715b0db1f0c35079a67f4902d973c006`;
- owner R4 repair authority: `032691216ac07054d975fad04aedb234e4bf3f1319b638bfac63ffd924b4fd1e`;
- all nine R3-bound `prepared/` object hashes matched at audit entry.

Derivative-package status: this evaluation report and handoff are read-only derivative audit artifacts. They are not prepared-packet authority, execution authority, a repair, a freeze, or the required post-repair verifier return.

Coverage and closure verdict:

- 31/31 numbered runbook steps assessed;
- 15/15 distinct branch/terminal-path classes assessed, including pre-C1070, partial-C1070, incomplete-baseline, and post-first-reconstruction-write phases;
- all 81 ledger command rows traced;
- 40 grouped required-evidence rows assessed;
- 5 findings, limited to the two owner-authorized defect classes;
- verdict `REPAIR_REQUIRED`; the R4 repair phase is not closed.

Required next owner-authorized work:

1. repair step disposition to one literal row for each step 1-31;
2. replace every post-reconstruction pre-C196 preservation route with a pre-C196/pre-C197 route invoking neither C1144 nor C1130, and separately route pre-C1070, partial-C1070, and incomplete-baseline failures so unavailable C1131-C1137 sources are never invoked;
3. enumerate hash-bound capture and return of complete C1105-C1108 outputs;
4. add the shared CONTROL transcript, per-step byte-range/hash map, explicit proof of complete C1105-C1108 inclusion, completed-form, retained-manifest, per-file hash, and failure-disposition operations described as C1146-C1151 in `EVALUATION_REPORT.md`;
5. update only the owner-adopted affected packet/control cross-references, freeze the repaired bytes immutably, and then run one genuinely fresh read-only post-freeze verifier.

Rerun requirements: mechanically rerun both matrices against the repaired frozen packet; reproduce every new frozen identity; verify no command range/token/index drift; verify C196/C197 byte preservation and the ordinary C1145→C1144→C1130 chain; verify every pre-C196 terminal path excludes C1144/C1130; verify all required evidence has an enumerated capture and return/disposition action.

Remaining blockers: current prepared packet cannot be presented for execution approval because its early-failure command prerequisite and evidence-return completeness contracts are not closed. No runtime facts were evaluated; dynamic outcomes remain `UNKNOWN` until separately authorized execution.
