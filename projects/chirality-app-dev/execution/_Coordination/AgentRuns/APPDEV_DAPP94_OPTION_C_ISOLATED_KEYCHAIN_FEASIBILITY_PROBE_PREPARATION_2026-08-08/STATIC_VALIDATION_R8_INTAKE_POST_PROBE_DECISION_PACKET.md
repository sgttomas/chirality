# Static validation — D-APP-94 R8 intake and post-probe decision surface

Verdict: `AUTHORING_PASS — WAITING_FOR_FRESH_VERIFIER`

- Returned R8 evidence count: `134`.
- Intake evidence count, excluding its two derivative Markdown controls:
  `134`.
- Byte comparison against same-named returned evidence: `134/134 PASS`.
- Primary count: `67`.
- True adjacent sidecar count: `67`.
- Independently validated adjacent sidecars: `67/67 PASS`.
- Primary evidence names ending in `.sha256.txt`: exactly
  `electron-archive.sha256.txt`, `electron-executable.sha256.txt`, and
  `probe-script.sha256.txt`; each has a validated
  `.sha256.txt.sha256.txt` sidecar.
- Derived feasibility facts match the evidence: `PASS`.
- Fixed R8 temp root absence, read-only intake-time observation: `PASS`.
- Unique D-APP-94 register-row count: `1`.
- Register state: `AWAITING_FINAL_POSTURE_RULING`.
- Historical Option A rejection and Option C probe-preparation ruling:
  preserved.
- Packet options A/B/C, evidence-supported Option A recommendation, exact
  owner tokens, preparation/planning-only boundary, and explicit no-attempt-3
  authority: present.
- Product-byte patch route: rejected and out of scope.
- No attempt-3 command, execution token, C1118 authority, reliance, product
  acceptance, runtime/security/Electron/deletion/Git/Task Management/product/
  package/trace action, or verifier dispatch occurred.

Recommended sealed fresh-verifier scope: read-only review of the 134 intake
evidence bytes against `returned_r8/`; independent validation of all 67 true
adjacent sidecars, including the three double-extension cases; exact
feasibility-fact derivation; fixed R8-root absence; decision-packet option and
token fidelity; unique register-row transition with historical-ruling
preservation; freeze hash stability; and authority-boundary/exclusion
coherence. Return exactly PASS or the smallest material blocker in one sole
review artifact. Do not repair, execute, dispatch, delete, mutate runtime or
security state, use Electron, perform Git/Task Management/product/package/trace
action, or infer reliance.
