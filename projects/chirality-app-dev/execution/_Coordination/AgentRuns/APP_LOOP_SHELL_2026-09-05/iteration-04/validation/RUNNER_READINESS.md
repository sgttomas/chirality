# Runnable capture preparation

No test/build/service/native launch occurred. run_checks.py was checked with Python AST parsing only; PREPARATION_VERIFICATION.json pins those prepared bytes. It fails closed unless ACTIVATION_FINAL.json exists with parent_go true, final source freeze, final whole-review PASS and inventory identities. ACTIVATION_TEMPLATE.json is inert and intentionally contains no changing source hashes.

At parent go, write a new final activation using exact parent-reviewed freeze/review paths and SHA256 values plus final inventory. Freeze JSON contract: files rows with repo-relative path and sha256; inventory contract: root, product and tests arrays. This can be a validation-local normalized input inventory citing parent final bytes if its source schema differs. Never label active author bytes final. Current expected inventory has17paths; any approved amendment must be cited in activation and its final inventory hash. Runner captures every inventory member, declared test filenames and full broader source identity at actual execution.

Commands from repo root, always under PYTHONDONTWRITEBYTECODE=1:
- python3 <validation>/run_checks.py release release-01 — existing registered service plus full wrapper. Preserve denied sandbox attempt; exact escalation repeats to fresh attempt name.
- After service stopped: python3 <validation>/run_checks.py build build-01 — Next then Electron main/preload/CLI; captures actual built bundle hashes and read-only native Electron SHA. No native launch.
- python3 <validation>/run_checks.py basic basic-01 — sequential selfcheck/practitioner pytest/hold/receipt/ordinary diff.
- python3 <validation>/run_checks.py security security-01 — existing secret-scan and canonical summary.
- After shared integration: python3 <validation>/run_checks.py final final-01.

New attempt names are required; no evidence directory reused. Inspect child command statuses rather than wrapper aggregate alone. Local binding503 means actual failed premerge/new-source CI owed, not a source check waiver. A build whose Next phase fails cannot claim Electron compiled even if older output files exist. Only build_exit_code0 supports current artifact identity handoff. Source drift forces failure.

After build slot completion, parent coordinates manager browser/native ownership; no wrapper/build repeats overlap that ownership. Native PDF-inline remains D-APP-121 blocked, and real Electron handoff proof is manager-owned. Source/menu/types/900px repairs remain active until final freeze; this runner creates no implementation or proof claim. All text streams remain lossless JSON; final staged checks belong to CHANGE.
