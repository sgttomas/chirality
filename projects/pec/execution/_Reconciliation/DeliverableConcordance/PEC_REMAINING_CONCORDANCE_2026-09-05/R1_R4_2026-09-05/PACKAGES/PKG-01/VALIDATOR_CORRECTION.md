# Validator path correction

BATCH01_PRECHECK.json is preserved failed manager-tool evidence. The first helper used a nearest-AGENTS traversal, resolving projects/pec instead of the canonical repository, and falsely reported source paths missing. This was a validator defect, not worker/source drift. The helper now resolves git rev-parse --show-toplevel as required. BATCH01_PRECHECK_CORRECTED.json validates DEL-01-02 without errors. No worker ledger was changed.
