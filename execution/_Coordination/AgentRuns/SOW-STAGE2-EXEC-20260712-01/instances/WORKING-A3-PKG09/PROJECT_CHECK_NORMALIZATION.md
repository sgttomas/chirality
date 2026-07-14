# WORKING-A3-PKG09 Software-Check Normalization

Only generated check evidence was normalized. PROJECT_CHECKS.json replaced 5 checkout-root and 2 harness-temp literals; preimage a22ae5366d1d85823fcc2a341ef7bf3f54fd6097a92537ed2bf55e631c7f5de6 / 46,993 bytes, postimage 7f366fc65d203f35635253b70cf40644a12e72dccdf81dbc4b3b42239a216bd7 / 46,677 bytes. PROJECT_CHECKS_PREMERGE.json replaced 23 checkout-root, 2 harness-temp, and 2 Section-9-temp literals; preimage 496dda8564f42a3e7755fd9addc160710cb7d1d33f5c146fc6a71b8a377cbbb4 / 13,702 bytes, postimage 0835f3e901d9eac57fa6b8b42c8ec61c8c7c2c932b74555e824bd27c65c1afeb / 12,602 bytes.

Both JSON postimages parse, contain zero captured roots, and reverse in memory to exact prehashes. The first preserves five PASS checks and initial no-server frontend-premerge FAIL. The second preserves stub-backed frontend-premerge PASS with Section 8 8/8 and Section 9 16/16 report-only. The temporary server was stopped.
