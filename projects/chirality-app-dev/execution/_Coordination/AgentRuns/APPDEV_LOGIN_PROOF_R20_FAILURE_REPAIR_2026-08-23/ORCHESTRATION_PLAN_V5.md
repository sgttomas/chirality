# Phase-B orchestration plan v5 — Option 1 continuation

1. `WP-B1C VALIDATE`: a bounded delegated-harness-native Agent 2 consumes the frozen terminal snapshot, verifies the raw pack log hash before and after, excludes immutable raw logs from an explicitly inventoried semantic whitespace predicate, and runs only unreached read-only deterministic gates. It writes only its unique continuation evidence.
2. `WP-B2C REVIEW`: only after WP-B1C freezes a PASS candidate, one genuinely fresh evidence-only Agent 2 reviews the complete Phase-A/Phase-B evidence, owner-direction matrix, raw-log exemption, procedure safety, claim calibration, retained tests/build/precheck, and final candidate hashes. It writes only its unique review evidence.
3. Shared R20/status/TM bytes remain frozen. Any changed semantic byte or any failed gate stops without rerunning one-shot evidence.
4. A fresh review PASS permits only manager fan-in and handoff to CHANGE for the Phase-B content commit. Receipt 191 remains after that commit.
5. No review repair cycle, supply/build/precheck/test rerun, proof act, operator/private evidence action, or Git publication act is authorized in this continuation.
