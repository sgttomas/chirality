# Independent immutable SSL read review — initial verdict

OpenAI GPT-6; exact serving ID unavailable. Actual Agent2 instruction-asserted/not mechanically enforced. No vendor, account, network, system writes, product writes or delegation.

## Changes required: S1 descriptor/path identity validation

Compiler initial path stat validates root ownership and non-group/world-writable mode. Opened descriptor validation only compares inode/device/size to the earlier path stat; it omits descriptor uid/mode validation. Final validation compares before/after descriptor stats but not the current pathname. A metadata change between stat/open can therefore be accepted under a mode that violates the immutable-read requirement; a path replacement after open can bind the descriptor's old bytes while the generated rule grants the new pathname. These require system-privileged mutation or ordinary system update; no unprivileged exploit is claimed.

A controlled mock changes only the returned opened descriptor mode for the exact SSL leaf after the real initial stat. The actual compiler returns a policy carrying mode&022==022. One test PASS reproduces the gap, without modifying system files (METADATA_REPRO.log; source preserved .test.ts.source). Parent notified to validate opened-fd owner/mode and compare final lstat/realpath identity to the accepted descriptor. This improves bounded observation; it does not establish atomicity with later vendor execution.

## Scope findings

New defaults name /usr/bin/curl and /private/etc/ssl/openssl.cnf. They do not grant /usr/bin or /private/etc/ssl as new parent directories. The special system configuration exception is exact SSL leaf equality; unrelated configuration paths remain rejected. Existing broad system-code directories are unchanged and are not represented as newly proved narrow leaves. File bytes, size, mode and uid enter policy digest version4. Supervisor recompiles against bound continuity identity before launch, so changed stable content requires an updated accepted policy/conformance basis.

Read-only observation of the actual SSL leaf is in SYSTEM_FILE_OBSERVATION.json; no active include or engine-loading directive was observed. Parsing every future OpenSSL directive is not claimed. Adding its read does not itself grant network access, and actual curl/native network execution remains parent-owned. No native gate, source acceptance or owner act is supplied by this review.
