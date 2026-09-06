# Raw output packaging

Raw command logs are gzip-compressed byte-for-byte (mtime 0) to preserve terminal whitespace while satisfying the candidate text-whitespace guard. Decompress each .log.gz to inspect the original output; exit codes remain in each checks summary. No test result or source byte is normalized. Initial whitespace failure is retained as check-2.log.gz and superseded only by the final validator result.
