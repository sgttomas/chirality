# WORKING-A3-PKG10 Software-Check Normalization

Only generated check evidence was normalized. `PROJECT_CHECKS.json` replaced
three checkout-root and two harness-temp literals; preimage
`84fb8745942fa7651f4f7b814695becff70c416f5c9ad4d401a6a121e510ada1` /
46,806 bytes, postimage
`bf1bcc1150aced199c64f1570e69f214f1b5b3cb7be24b1f80de83a69664067b` /
46,650 bytes. `PROJECT_CHECKS_PREMERGE.json` replaced 21 checkout-root, two
harness-temp, and two Section-9-temp literals; preimage
`7bb248be9c6b19d9f08ddd4063c04c0e5c458290b1f914152eea51d6ccf418d0` /
13,508 bytes, postimage
`74e7bfe55e9eee4150a697e50e866b307a976bfed2ecf19aa63fb283ca352798` /
12,824 bytes.

Both JSON postimages parse and contain zero captured checkout or temporary
roots. The first preserves five PASS checks and the initial no-server
frontend-premerge FAIL. The second preserves the stub-provider-backed
frontend-premerge PASS with Section 8 at 8/8 and Section 9 at 16/16
report-only. The temporary local Next server was stopped.
