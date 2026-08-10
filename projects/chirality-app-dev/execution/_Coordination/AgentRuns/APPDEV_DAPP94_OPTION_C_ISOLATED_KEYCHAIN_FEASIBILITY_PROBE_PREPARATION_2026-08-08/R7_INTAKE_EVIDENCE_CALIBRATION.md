# R7 intake-evidence calibration successor

Status: `CALIBRATED DERIVATIVE INTAKE — 58 RAW OBJECTS`

Accepted predecessor intake:
`R6_SYNTHESIZED_DEFAULT_DISCOVERY_INTAKE.md`, SHA-256
`ff99492074fd0e7e7ca8005f1bceb57c8d1b11b2f2a8b9894d3b27df264bc27e`.
Its manifest correctly enumerates all 58 available raw evidence files totaling
1,469 bytes. The derivative directory
`intake/r6_synthesized_default_discovery/` byte-compares exactly with the
retained source at
`/private/tmp/chirality-dapp94-option-c-keychain-probe-r5-20260809/evidence/`.

Calibrated terminal classification:

- raw evidence: `terminal-status.txt` contains the named STOP
  `FAILED_AFTER_ISOLATED_SECURITY_START:observe-bound-isolated-default`;
- owner report: the process exited `45`;
- branch consistency: the frozen R7 driver maps that exact named STOP route to
  exit 45;
- epistemic limit: no raw process-exit-status object exists, so exit 45 is not
  classified as raw exit-status evidence.

The retained R5 source, copied 58-object intake, occupied `returned_r5/`,
absent R7 root/`returned_r7/`, and all R7 driver/route/scope semantics remain
unchanged. This calibration does not create a 59th object or alter raw bytes.
