# PKG09 D121 corrected preparation return — v2

Verdict: `READY_CARRIER_APPLICATION_HELD_FOR_PARENT_RELEASE`.

The v1 carrier-readiness claim is withdrawn because two v1 records contain the wrong DEL-09-06 status postimage hash. `V1_FAILURE_NOTICE.md` preserves the exact defect and cause. No live application occurred, so no rollback is needed.

Correct exact identities, derived directly from accepted bytes and an isolated full three-carrier patch application:

- accepted patch: `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32`;
- DEL-02-03 status: `da18f6ef905840270718f88947fcbfdd13d26609f1c9a06522f1463385999ecd` → `af33c2623097cdffb3eedb58819a0bfbdf8c5dcb987b4f13befbeed6b72b1960`;
- DEL-09-06 status: `d8152c669ca3e57768004e184ec75ac9aaccaba5791d96589547e017545c1fe0` → `0f4b65b53f0e05183fcd8a5f489bb2da8ccdb4ead6fab22944f89f8daf42e6ba`;
- DEL-09-06 SOW: `1fed47a10b3f480a545947e6cf1d60ef7e150f166caceb4a26c0267f92dde652` → `02725ce67b4329672abec8fd6838f0c37c8261cf764bfd4a1894d8c12215b7d0`.

All three isolated patch results are byte-identical to the retained postimages. The corrected SOW result validates as `SOW_V1`. Configured-Python checks pass, including APP-HOLD `ALLOW`, corpus MATCH, receipt validation, harness status/self-check exit 0, and 379 practitioner-harness tests.

Use only `CARRIER_APPLICATION_v2.md` and `PREFLIGHT_AND_IDENTITIES_v2.json` for application. Existing `PACKAGED_PROOF_BRIEF.md` contains no affected carrier posthash and remains a held future brief; it still cannot dispatch before accepted carrier application, parent-frozen PKG02 source, and process-lane release.

No carrier/source/test/process write occurred. HELP_HUMAN remains the next owner for explicit application release after its fixed-head/shared-scope gates.
