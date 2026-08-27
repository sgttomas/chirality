# R16 quarantine and disposable-state cleanup proof

All artifact and probe bytes were removed after the last authorized exact
binary use and before N4 fan-in.

## Exact paths deleted and verified absent

- `/private/tmp/chirality-r16-n1.iMyfhF`
- `/private/tmp/chirality-r16-g-env.POzLM8`
- `/private/tmp/chirality-r16-g-env.8RMCMo`
- `/private/tmp/chirality-r16-g-env.wXAr0z`
- `/private/tmp/chirality-r16-g-env.29D2aB`
- `/private/tmp/chirality-r16-g-sbx.46AYwj`
- `/private/tmp/chirality-r16-g-role.JFUs2I`
- G-PROT disposable prefix `/private/tmp/chirality-r16-gprot.*`
- G-APPR disposable `/private/tmp/chirality-r16-g-appr-n3-5-20260827`
- G-SENT disposable `/private/tmp/chirality-r16-gsent.zPMQbE`
- G-WIRE disposable `/private/tmp/chirality-r16-gwire-n3-7-vOTSmc`

The final sorted scan
`find /private/tmp -maxdepth 1 \( -name 'chirality-r16-*' -o -name 'chirality-root-r16-*' \)`
returned zero paths. Direct `test ! -e` checks passed for every exact parent
path. The G-SBX outside target and G-SENT outside-write target were also
absent.

Repository checks found no tracked path containing `codex-app-server`, the
quarantine name, or an R16 `.tar.gz`, and no repository file exceeded
70,000,000 bytes. The 71,843,308-byte archive, 179,721,344-byte payload,
release metadata, full static scan, App Server JSONL output, databases,
skills, logs, and every probe fixture remain untracked and are deleted.

Cleanup is destructive only to the expressly disposable paths above. No
workspace evidence, accepted record, host configuration, credential, account,
or user file was removed.
