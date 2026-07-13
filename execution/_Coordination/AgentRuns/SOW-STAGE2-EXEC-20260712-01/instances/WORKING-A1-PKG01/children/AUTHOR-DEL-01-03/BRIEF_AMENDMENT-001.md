# AUTHOR-DEL-01-03 Brief Amendment 001

Status: ACTIVE — PORTABILITY/PRESERVATION CLARIFICATION

The generated-evidence portability gate does not authorize rewriting any
exact copied source, status, or control byte. It also excludes verbatim
source blocks preserved by the deterministic converter in ScopeOfWork.md and
the same verbatim source text reproduced by deterministic HTML rendering.
Those preservation-bound occurrences are exact-source exceptions, not
generated path authority.

All genuinely generated metadata, TASK run-record fields, return/status,
claim-map/parity/checklist metadata, verdicts, checks, and manifests must
contain zero literal checkout prefix and zero temp prefix. Use portable ~/ or
repository-relative notation in those generated surfaces.

Record every exception with path, occurrence count, source binding, and
reason. Prove the copied source/control hashes, candidate parity, and render
determinism remain exact. Any occurrence outside the recorded preservation
exceptions blocks terminal PASS.

This amendment reconciles the sealed preservation and portability gates. It
changes no meaning, scope, authority, write target, acceptance criterion,
lifecycle, H1/H2, ISSUED, integration, release, or retirement posture.
