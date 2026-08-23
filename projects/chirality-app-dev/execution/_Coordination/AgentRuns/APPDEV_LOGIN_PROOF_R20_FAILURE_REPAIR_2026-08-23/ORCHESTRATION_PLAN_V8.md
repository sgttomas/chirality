# Phase-B orchestration plan v8 — PR #632 record-only whitespace repair

1. `WP-B3D DIAGNOSE`: WORKING_ITEMS runs the exact candidate whitespace validator once on clean HEAD `85caafd4882a2ffff204ed87334171608ce462be` and freezes the complete output plus exact flagged-file/line inventory. No repair begins before this diagnostic.
2. `WP-B3R REPAIR_VALIDATE`: one bounded delegated-harness-native Agent 2 repairs exactly the diagnostic's flagged files using the frozen evidence convention, records complete lineage, and runs the authorized non-product pre-push gates. It owns only the enumerated evidence paths and its unique instance evidence.
3. `WP-B3V REVIEW`: only after candidate bytes and checks freeze, one genuinely fresh evidence-only Agent 2 reviews 100% of repair lineage, gzip recoverability/normalization identity, retained exemptions, Receipt 191, scope, hashes, and gate evidence.
4. Overlapping RunID and Receipt writes are serialized. No child may touch frontend, product/package/proof surfaces, Git state, or another child's evidence.
5. Any failed repair or validation gate stops. A review finding may enter the standing failure rule only when its repair is record-only and within this exact authority; otherwise stop and escalate.
6. Fresh review PASS permits manager fan-in and CHANGE publication readiness. WORKING_ITEMS performs no Git publication act.
