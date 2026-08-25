# Root Supply Pinning R14 Validation

Date: 2026-08-24

Basis: `origin/main@5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`

Candidate state: `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

## Candidate review

- N1 source/currentness: `PASS`
- N2 primary supply inventory: `PASS_UNDER_R13_AMENDED_SIGNATURE_GATE`
- N2b three-packaging equivalence: `PASS_EQUIVALENT_2_OF_2`
- N3 contained execution: `PASS_WITH_ADMITTED_DENIED_EGRESS_AND_DOCUMENTED_GAPS`
- N4 candidate assembly: `PASS_WITH_DOCUMENTED_GAPS`
- N4 fresh review: zero actionable findings
- Parent byte and claim review: `PASS`

N4's first review pass reported a possible `.zst` archive/payload digest mix-up.
Parent and N2b reinspection showed the current N2b evidence was already correct:
the archive digest is `c4c31ecd…73677` and the decompressed payload digest is
`b1d1a8c3…de2`. No no-op repair was made. The same review found a real N3
structured-summary calibration defect: the explicit `plugins=false` result had
been mixed into the baseline feature row. N3 repaired only its summaries and
hash manifest without rerunning vendor code. Raw baseline and override traces
now reconcile as `true/true` and `false/true`, respectively. N4 then restarted
fresh review and closed with zero actionable findings.

## Containment and teardown

- Every vendor invocation was preceded by executable SHA-256 verification,
  sandbox-profile SHA-256 verification, and a bounded network-denial preflight.
- Sandbox profile SHA-256: `17a579161aa13d50b1f5f735c48408ce2ae45000a6fd1a26a4a0d58a045676ab`.
- Completed connections: `0`.
- Credential prompts, login/device flows, and approvals granted: `0`.
- Writes outside disposable state: `0`.
- Both artifact quarantines, the disposable `CODEX_HOME`, disposable workspace,
  and temporary static extracts were deleted and verified absent.
- All committed raw traces are normalized or deterministic gzip files; all 53
  gzip files pass decompression checks.

## Final validators

- Root G0 materialization fence: `PASS`.
- Root G1 harness adapter: `PASS` (`status_files=53`).
- Root G2 surface ownership: `PASS`.
- Root G3 work graph: `PASS` (six nodes, none active).
- Candidate whitespace against `origin/main`: `PASS`.
- Agent instructions: `PASS` (34 files, 0 errors, 0 warnings).
- Instruction entrypoints: `PASS`.
- CI-form G4: `PASS` (48 manifests; 122 changed paths; zero instruction-surface
  paths; zero covering manifests required).
- Task Management register: `PASS` (19 rows).
- Focused practitioner harness: `PASS` (56 passed).
- Candidate JSON parse and evidence-hash manifests: `PASS`.
- Candidate gzip integrity: `PASS` (53 files).
- `git diff --check`: `PASS`.

No instruction surface, pin, lifecycle, Task Management register, project,
runtime, tool, plan, or existing DEL-02-08 contract/metadata byte changed.
