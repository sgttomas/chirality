# Publication EOF normalization

Only surplus final LF bytes were removed from HANDOFF_STATE.md and R4_DECISION_CANDIDATES.md. FORMAT_MAP.json records exact pre/post hashes and byte counts. ORIGINALS_BASE64.json losslessly carries both old files and the entire prior package manifest. Decoding reproduces exact original bytes and SHA-256 values; non-whitespace bytes are unchanged.

Historical seals continue to describe their original logical path/byte state. Resolve the two historical paths to their decoded original carriers; all other historical entries remain unchanged. The current package manifest seals the normalized publication representation and these preservation artifacts. No semantic, source, claim, receipt, authority, lifecycle or routing change occurred; no fresh semantic rerun was warranted.
