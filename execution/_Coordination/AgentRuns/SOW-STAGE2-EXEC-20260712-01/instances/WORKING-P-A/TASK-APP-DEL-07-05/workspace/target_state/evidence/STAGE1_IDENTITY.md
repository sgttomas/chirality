# DEL-07-05 Stage-1 Identity

Verdict: `PASS`

- Stage-1 App evidence commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26` exists, and its live-path `ScopeOfWork.md` blob hashes to `f38b0e741949abd9a892e8fea1a93c91be7da95bda668b3c80c2fd4dac7f450e`.
- The extracted Stage-2 candidate and target seed are byte-identical to that Stage-1 blob.
- The Stage-1 inventory exact `DEL-07-05` entry records the same candidate, four source, and status hashes; `IN_PROGRESS`; `SOW-029`; `OBJ-006`; 35 mapping rows; 419 mapped source lines; one `OUT`, `AC`, and `VER`; and PASS for validation, parity, render, map identity, frozen-base equality, and status equality.
- Fresh `claim-map.csv` is byte-identical to the Stage-1 map at SHA-256 `a1e27777b54c94f31b9365bf87b2ed909a13bcf188eca11f3cf040b5965127ae`.
- Fresh parity is semantically identical to Stage-1 after excluding the run-local `scope_of_work` path; both canonicalized reports hash to `95722a8678c4989be4dbe821903b9dc20a15fb33104a3291635e796a144a8dd0`.
- Fresh HTML is byte-identical to both Stage-1 renders at SHA-256 `6c974e08c102c493d8de38cad67875af3c659da5791fb847bffd184ca35508a7`.
- The fresh checklist reproduces exactly one `AC-001` with the same criterion text recorded by Stage-1, plus current exact source identity, qualified ID, candidate hash, `OUT-001`, and `VER-001` linkage. The historical Stage-1 checklist envelope and fresh corrected `SOW_V1` envelope are not asserted byte-identical.
- Stage-1 historical `PILOT_DUAL` validation was read as provenance only and was not replayed. `PILOT-VALIDATION-001` controls this run's separate legacy-only and target-only validation.
