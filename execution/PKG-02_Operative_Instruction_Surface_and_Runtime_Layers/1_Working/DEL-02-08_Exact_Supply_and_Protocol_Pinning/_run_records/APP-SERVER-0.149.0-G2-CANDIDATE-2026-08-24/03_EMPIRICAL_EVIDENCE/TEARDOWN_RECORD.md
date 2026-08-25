# R14 N3 Teardown Record

**Completed:** 2026-08-24 America/Edmonton

After all normalized/compressed traces and structured evidence were copied to
the authorized candidate folder, the exact disposable and quarantine targets
were resolved and removed:

```text
/private/tmp/chirality-root-supply-r14-n3.NQGDlu Directory 352
/private/tmp/chirality-root-supply-r14-primary.lTtHP2 Directory 224
/private/tmp/chirality-root-supply-r14-equivalence.BmK7x0 Directory 224
/private/tmp/r14_appserver_strings_focus.txt Regular File 537449
/private/tmp/r14_codehost_strings_focus.txt Regular File 46239
```

Post-delete existence checks returned `ABSENT` for all five exact targets.
The three downloaded release assets, all extracted vendor binaries, generated
disposable databases/skills/state, probe fixtures, and temporary static-string
files are gone. No artifact bytes were committed or retained in a live
`CODEX_HOME`, PATH, launchd, daemon, credential, or runtime surface.

The separately preserved prior-stop evidence archive was not a current
artifact quarantine and was not modified or deleted by N3.
