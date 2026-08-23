# Phase-B orchestration plan v9 — PR #632 postcommit validation, review, and receipt

1. `WP-B4G GATE`: exact committed-range candidate whitespace gate runs first at intermediate commit `de2080a7ac82f636fca3f8be57b20dc0e9a80fa8`; it must pass before any other gate. WORKING_ITEMS observed PASS/exit 0.
2. `WP-B4V VALIDATE`: one bounded Agent 2 runs the remaining governance-only pre-push gates, freezes commands/exits/hashes, and proves frontend/package/proof bytes untouched.
3. `WP-B4R REVIEW`: after gate and candidate bytes freeze, one genuinely fresh evidence-only Agent 2 reviews the exact 12-path repair, 11 gzip recoveries, three-byte RETURN normalization, sequencing record, full governance gate evidence, scope/fences, and receipt-ready claim calibration.
4. `WP-B4F RECEIPT`: only after fresh PASS, WORKING_ITEMS minimally amends Receipt 191 with verbatim owner authority and pointers to exact lineage/intermediate commit, then runs receipt-specific validation/whitespace/containment and returns one-path CHANGE readiness.
5. Any substantive gate or review failure stops. No product/test/build/package/proof rerun or Git publication action is permitted.
