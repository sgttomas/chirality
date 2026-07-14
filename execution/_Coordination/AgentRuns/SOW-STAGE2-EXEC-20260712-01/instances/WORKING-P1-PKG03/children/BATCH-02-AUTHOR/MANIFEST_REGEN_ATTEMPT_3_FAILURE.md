# Manifest regeneration attempt 3 failure

Parent fan-in found blank digest and size bindings in the invalid manifest,
reason `MANIFEST_BLANK_BINDINGS`. A subsequent regeneration command attempted
to quote an `awk` field expression inside nested shell quoting and failed
before populating the manifest, reason `MANIFEST_REGEN_AWK_ESCAPE`.

No candidate or live/project file changed. The invalid manifest remains
unaccepted. Final remediation freezes all terminal files, computes SHA-256
without `awk`, computes byte counts with `stat`, includes every ordinary file
under the child root except only `MANIFEST.tsv`, and independently checks row
shape, existence, digest, and size. No child file changes after that command.
