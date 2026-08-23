# Activation — implementation evidence hygiene repair cycle 1

- Authority: Amendment 09 and sealed repair brief `A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-REPAIR-01.md`.
- Scope: remove exactly the final LF from the four named implementation records; no source/shared/product write.
- Preconditions: all four preimages ended `0a0a`; test source SHA-256 `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e`; proof-script SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`.
- Preimages: `ACTIVATION.md` `1119` bytes / `c0060da4fb916aafc890d34c37f961a35ee0a17849288bd179350dfcfaf5c52e`; `CHECKS_AND_LINEAGE.md` `3608` / `18d5d95b822b853bf4c860c2a390d4dab299bba78310fe4c7e0c71c2c264f5df`; `IMPLEMENTATION_MODE_INVENTORY.md` `1658` / `9f5a804ea6abe93c989c99ec60a326a82b4a586ed59bcfa71d255a4086147b59`; `RETURN.md` `1987` / `505e6e0ab4e19c3b626fe0f20aa16216b91312ab94ed6b3867c220538af392b9`.
- Immutable gzip evidence: `focused-normal.log.gz` `56094069868c3e730f0f63d2400848cd742d4a18ba67a42860251f95b4be01e2`; `focused-umask-0002-postfix.log.gz` `1d979a898aafe56660872f7a8778dacaa30b8e9d22c0b95d555534480d796a44`; `typecheck.log.gz` `eb355223a12447bc6afe239b3e311ce8b1215f87a33ae438018bcaeb98198309`.
- Git fence: no stage, commit, fetch, push, PR mutation, rebase, force-push, or merge.
