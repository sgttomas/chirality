# PR 764 stub forwarding correction

Parent-author correction on `cf15e194a35539f4dcc099f2878b2e470f4d8203` restores `contentBlocks` and `turnId` forwarding through the controlled stub Runtime entrypoint. Optional receiver arguments preserve the existing adapter calling convention. No test assertions, context guards, or simulation behavior changed.

Exact source SHA-256: `aae3d33cff689c8bcb057583d20c74e71c62621cfb4c49467ee64b531752d097`.

WORKING_ITEMS `/root/app_adoption` validated the full App suite: 2,001 passed, four skipped; App typecheck passed; diff check passed. Full test log SHA-256: `ec274c057b93de7680313e9cb7be54963fd1dbc788df5f10b2a01f081edbf15f`. Typecheck log SHA-256: `dc2149dec385adf46be71c88c67ddcf056f04bdcdba97507bdc9056781a90d1f`. Raw logs remain preserved locally.

Separate reviewer `/root/astra_runtime_second_pass` returned PASS with no findings. Its selected review and manifest bind the exact source and unchanged attachment test.

The prior CI head passed Root, PEC, typecheck, Section 9, and all eight Section 8 checks. Its only App full-suite failure was the missing forwarded attachment argument, now repaired and covered by the unchanged test. Fresh exact-head CI remains required before merge; no release or native qualification is claimed.
