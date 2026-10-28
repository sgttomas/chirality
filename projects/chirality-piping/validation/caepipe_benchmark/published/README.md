# Published CAEPIPE benchmark agreement

This folder is the one place where benchmark agreement between SWBPIPE and CAEPIPE is published, as
`summary.json` and its fixed rendering `summary.md`. It holds no summary until the owner has ruled the
tolerance class and checked the licence terms, and Agent 0 has added the ruling record
`loop/rulings/caepipe-benchmark-publication.json`. The form, the gate and the check are set by
`docs/IP_AND_DATA_BOUNDARY.md` §6.2 and DEL-17-05 `Design/caepipe-correlation-pilot.md` §8.1. Write
`summary.json` against `schemas/caepipe_benchmark_summary.schema.json`, then, from the repository root, write
`summary.md` with `python3 projects/chirality-piping/tools/caepipe_correlation/check_public_observations.py
--render-summary`; never edit the rendering by hand.

<!-- reliance -->
Agreement on the benchmark set is not acceptance, validation of a user's design, code compliance,
compatibility or a release; reliance on SWBPIPE's results stays with the user, and acceptance, issuance
and release remain the owner's acts.
<!-- /reliance -->
