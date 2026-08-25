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

N4's first review pass correctly reported a `.zst` archive/payload digest
mix-up in `EQUIVALENCE_INVENTORY.md`: the archive row carried the decompressed
payload digest `b1d1a8c3…de2`. The row is corrected to the official archive
digest `c4c31ecd…73677`; N2b and N4 dependent identities were regenerated.
No download, vendor execution, or network probe was used. The same review
found an N3 structured-summary calibration defect: the explicit
`plugins=false` result had been mixed into the baseline feature row. N3
repaired only its summaries and hash manifest without rerunning vendor code.
Raw baseline and override traces reconcile as `true/true` and `false/true`,
respectively. Fresh N4 review closes with zero actionable findings.

## Deterministic correction return — PR #673

Owner direction: “Return PR #673 for deterministic evidence correction; do
not merge. No new vendor execution is authorized.”

Read-only reinspection found one actionable record defect. Nine runs
had committed per-run gate-hash and attributable denial-preflight records; the
`version` run had empty committed preflight files and no per-run gate-hash
record. The former 10/10 claim was corrected to 9/10 plus
`VERSION_RUN_GATE_EVIDENCE_UNAVAILABLE_UNDER_BOUNDS`. The standalone explicit
preflight remains evidence of a denial but is not attributed to `version`.
An initially suspected stale README hash was rejected after correcting the
verifier's candidate-relative path resolution; the pre-correction table was
accurate. Dependent hashes were regenerated only for the actual correction.
Raw evidence was not edited, downloaded, or regenerated, and no vendor
executable was invoked.

## Containment and teardown

- Nine of ten vendor invocations have committed executable/profile SHA-256
  verification and attributable bounded network-denial preflight records. The
  `version` gate record is the documented unavailable evidence class above.
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
- Deterministic correction audit: `PASS` (25 checks, zero failures), including
  raw-tree immutability, exact 9+1 gate shape, version evidence-gap
  calibration, raw-to-structured feature parity, JSON parse, and all three
  hash manifests.
- Fresh digest-correction semantic audit: `PASS` (29/29 checks; zero
  failures), including exact archive/payload
  slot separation, the full N2b/N4 hash chain, preserved version-run gate
  provenance, and absence of the superseded digest false-positive claim.
- `git diff --check`: `PASS`.

No instruction surface, pin, lifecycle, Task Management register, project,
runtime, tool, plan, or existing DEL-02-08 contract/metadata byte changed.
