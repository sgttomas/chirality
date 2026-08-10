# Validation — R4.4.6 attempt-2 intake and D-APP-94

Verdict: `PASS DERIVATIVE INTAKE / STOP_INCOMPLETE EXECUTION / D-APP-94 READY`

- immutable returned receipt: 40 objects, exactly 20 primaries and 20 adjacent
  sidecars; all 20 reproduce;
- ordered aggregate:
  `480f1817774d2c2a8bc74e7e584674341f9699a2f9e2a9f5132f75050a790cfb`;
- intake freeze:
  `84d7220874cb738e9fc0edc2fa02e712caa05d058a8789b66c10b5741a6d6fcf`;
- D-APP-94 freeze:
  `4644beb0068357d9598d9dc990d473a51cb7398d27ef9c6def80981c94a5e31f`;
- final fresh-verifier PASS:
  `374efd1646e336856cc2d299509515729fda8450c04a36e796c4f0e6c5c44b83`.

The accepted intake records step 14 FAIL, step 15 DEVIATION, C1118 NOT_RUN,
matching contact-signature records in both GUI stdout and stderr, and the stale
predecessor runbook hash in the immutable completed form. C1105-C1108 pass;
package and direct-child identities are supported at launch only. Eight
signal-path cells remain UNKNOWN; C196/C197 were unused. Cleanup, rollback,
C1141 emptiness, and fixed-root absence pass as returned evidence.

D-APP-94 is a non-decisional A/B/C proposal with Option A conditionally
recommended. Any future attempt requires both a fresh C1118 gate and a separate
repair of the step-14 observation/stop condition. No option, implementation,
execution, keychain, credential, product, release, reliance, Task Management,
or Git action is authorized by this validation.
