# Attempt-7 protocol ordering and observed bytes

## Ordered observations

1. C231-C232 bound both scripts to their frozen identities.
2. C233 proved the fixed root absent; C234 created it.
3. C235 started session A once. Its first and only pre-result line arrived in
   the initial PTY yield, whose tool-reported wall interval was `0.253854292`
   seconds. The line was:

   ```json
   {"schema":"chirality-dapp92-two-session-controller/v1","controllerPid":13085,"directChildPid":13086,"childExecutable":"/bin/sleep","childArgv":["35"],"state":"ATTACH_READY"}
   ```

4. C236 bound the already durable controller record before acknowledgment to
   SHA-256 `f30f66344085e1d906fdee51695f99e9e5b6b9f474099fd52d10bfb3df8acae0`.
5. C237 then emitted exactly this one line and exited `0`:

   ```json
   {"schema":"chirality-dapp92-two-session-sentinel/v1","directChildPid":13086,"state":"SECOND_SESSION_ACKNOWLEDGED"}
   ```

6. C238 polled only existing session A with an empty byte string. The first
   polling interval remained active for `11.0` tool-reported seconds and the
   continued wait completed after a further `20.991025083` tool-reported
   seconds. Together with the preceding bounded C235-C237 intervals, the
   result arrived before the 45-second deadline. Session A emitted exactly
   this one result line and terminated with exit code `0`:

   ```json
   {"schema":"chirality-dapp92-two-session-result/v2","directChildPid":13086,"sentinelMatched":true,"sentinelState":"SECOND_SESSION_ACKNOWLEDGED","childExecutable":"/bin/sleep","childArgv":["35"],"sentinelWindowMs":30000,"childExitCode":0,"childSignal":null,"controllerState":"COMPLETE"}
   ```

7. C239-C241 preserved only the successful result at SHA-256
   `0409681a1bab450372e5374d2726822e847da35671b067344ac22eabbe7905a9`.
8. C242 confirmed the already terminal session without bytes, signals, or
   inspection. Only then did C243 remove the root and C244 prove it absent.

The PID, schema, child executable/argv, sentinel state, natural exit code, and
no-signal result agree across all observable protocol records. No retry or
alteration occurred.
