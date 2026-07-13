# WORKING-A1-PKG01 Work Graph v1

Status: FROZEN — AUTHOR STAGE READY

Selection authority: accepted A1-PACKAGE-ACTIVATION-001, the exact APP-PKG-01
row of snapshots/W_A1/preflight/PACKAGE_PLAN.tsv, and the four
WORKING-A1-PKG01 rows of A1_MANIFEST.tsv.

Posture: MIXED. At most two disjoint author nodes run concurrently. Each
verifier is dependency-gated on manager acceptance of its matching author.
Package checks and fan-in are gated on all four verifier returns.

| Node | Role | Member | Depends on | Writes | Expected return | Fan-in gate |
|---|---|---|---|---|---|---|
| A-01 | TASK author | DEL-01-01 | accepted A1-B0 | candidates/W_A1/APP-PKG01/DEL-01-01/**; children/AUTHOR-DEL-01-01/** | terminal author return plus candidate/evidence | exact row hashes, authority, deterministic evidence, containment |
| A-02 | TASK author | DEL-01-02 | accepted A1-B0 | candidates/W_A1/APP-PKG01/DEL-01-02/**; children/AUTHOR-DEL-01-02/** | terminal author return plus candidate/evidence | exact row hashes, authority, deterministic evidence, containment |
| A-03 | TASK author | DEL-01-03 | accepted A1-B0 | candidates/W_A1/APP-PKG01/DEL-01-03/**; children/AUTHOR-DEL-01-03/** | terminal author return plus candidate/evidence | exact row hashes, authority, deterministic evidence, containment |
| A-04 | TASK author | DEL-01-04 | accepted A1-B0 | candidates/W_A1/APP-PKG01/DEL-01-04/**; children/AUTHOR-DEL-01-04/** | terminal author return plus candidate/evidence | exact row hashes, authority, deterministic evidence, containment |
| V-01 | TASK verifier | DEL-01-01 | accepted A-01 | children/VERIFY-DEL-01-01/** | independent terminal verification return | no repair; exact identities; negative gates |
| V-02 | TASK verifier | DEL-01-02 | accepted A-02 | children/VERIFY-DEL-01-02/** | independent terminal verification return | no repair; exact identities; negative gates |
| V-03 | TASK verifier | DEL-01-03 | accepted A-03 | children/VERIFY-DEL-01-03/** | independent terminal verification return | no repair; exact identities; negative gates |
| V-04 | TASK verifier | DEL-01-04 | accepted A-04 | children/VERIFY-DEL-01-04/** | independent terminal verification return | no repair; exact identities; negative gates |
| F | WORKING_ITEMS fan-in | APP-PKG-01 | accepted V-01..V-04 | package instance outputs only | package PASS/BLOCKED/DECISION_REQUIRED | 4/4 pairs, checks, exact 20+20 manifests, portability, containment |

Concurrent writes are pairwise disjoint. Live project paths are shared reads
only. Children do not delegate or communicate with siblings. All coordination
returns through WORKING-A1-PKG01. Drift or any contract failure escalates to
HELP_HUMAN.
