# VERIFY-DEL-10-02 Portability Record

All verifier-generated method evidence and root terminal artifacts use repository-relative paths. No immutable accepted source/control or candidate content contains a machine-specific absolute path or `file://` URI.

The TASK run record initially contained resolved absolute execution paths as required during runtime. WORKING_ITEMS evidence-only closeout replaced those three generated metadata values with `{REPO_ROOT}` tokens after terminal substantive PASS; `EVIDENCE_CLOSEOUT_01.md` records that normalization. No generated metadata retains a temporary-root path, host-specific path, or `file://` URI. The deterministic HTML is script/form-free and contains no external resource reference.
