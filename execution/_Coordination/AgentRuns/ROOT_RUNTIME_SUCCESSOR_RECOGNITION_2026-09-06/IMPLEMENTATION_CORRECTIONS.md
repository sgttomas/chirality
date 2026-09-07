# Preserved development findings

Initial G0 validation failed: reference hash mismatch in retired Root DEL-02-06 ScopeOfWork. The retired Root SOW is not byte-identical to the initialized Runtime SOW. Corrected historical successor proof to use the exact Runtime SOW blob at already published Gate5 confirmation commit, preserving its original binding SHA. No Root or Runtime source document changed. G0 rerun PASS.
