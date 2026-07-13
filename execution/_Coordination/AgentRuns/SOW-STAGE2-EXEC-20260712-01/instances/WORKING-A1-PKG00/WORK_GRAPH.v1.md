# WORKING-A1-PKG00 Work Graph v1

Status: `FROZEN — AUTHOR STAGE READY`

Selection authority: accepted `A1-PACKAGE-ACTIVATION-001`, the exact
`APP-PKG-00` row of `snapshots/W_A1/preflight/PACKAGE_PLAN.tsv`, and the two
`WORKING-A1-PKG00` rows of `A1_MANIFEST.tsv`.

Posture: `MIXED`. The two author nodes are disjoint and may run concurrently.
Each verifier is dependency-gated on the manager accepting its matching author
return. Package checks and fan-in are gated on both verifier returns.

| Node | Role | Member | Depends on | Writes | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|
| A-01 | TASK author | DEL-00-01 | accepted A1-B0 | `candidates/W_A1/APP-PKG00/DEL-00-01/**`; `children/AUTHOR-DEL-00-01/**` | terminal author return plus candidate/evidence | exact row hashes, conversion authority, validation/map/parity/checklist/render, containment |
| A-02 | TASK author | DEL-00-02 | accepted A1-B0 | `candidates/W_A1/APP-PKG00/DEL-00-02/**`; `children/AUTHOR-DEL-00-02/**` | terminal author return plus candidate/evidence | exact row hashes, conversion authority, validation/map/parity/checklist/render, containment |
| V-01 | TASK verifier | DEL-00-01 | accepted A-01 | `children/VERIFY-DEL-00-01/**` | independent terminal verification return | no repair; exact candidate/source/status; negative gates; semantic-addition review |
| V-02 | TASK verifier | DEL-00-02 | accepted A-02 | `children/VERIFY-DEL-00-02/**` | independent terminal verification return | no repair; exact candidate/source/status; negative gates; semantic-addition review |
| F | WORKING_ITEMS fan-in | APP-PKG-00 | accepted V-01 and V-02 | package instance outputs only | package PASS/BLOCKED/DECISION_REQUIRED | 2/2 pairs, project checks, exact 10+10 manifests, portability, containment |

Concurrent writes are pairwise disjoint. Live project paths are shared reads
only. Children do not delegate or communicate with siblings. All coordination
returns through WORKING-A1-PKG00. Any source, status, lifecycle, membership,
authority, profile, tool, caller, or write-scope drift escalates to HELP_HUMAN.

