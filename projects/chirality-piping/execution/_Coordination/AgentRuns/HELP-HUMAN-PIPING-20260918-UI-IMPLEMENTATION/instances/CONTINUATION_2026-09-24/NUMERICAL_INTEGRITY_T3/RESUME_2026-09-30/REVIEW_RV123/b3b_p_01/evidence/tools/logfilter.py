"""RV123: keep a cargo log's outcome lines (job header/footer, binaries, per-test results, summaries,
panics, compile errors, RV123 markers); drop build noise and debug prints."""
import re, sys
keep = re.compile(r'^(RV123_JOB|\s*Running |test |test result|RV123_|thread .* panicked|error(\[|:)|\s*Finished |failures:|    [a-z_:0-9]+$)')
for line in open(sys.argv[1], errors='replace'):
    if keep.match(line):
        sys.stdout.write(line[:2000] + ('\n' if len(line) > 2000 else ''))
