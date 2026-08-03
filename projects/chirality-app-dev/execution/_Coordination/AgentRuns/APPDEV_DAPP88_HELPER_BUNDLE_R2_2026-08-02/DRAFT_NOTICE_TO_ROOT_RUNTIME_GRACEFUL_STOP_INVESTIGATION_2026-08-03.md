# Draft notice to Root `_Coordination/` — runtime graceful-stop investigation request

Status: `DRAFT / NOT ROUTED`. This file remains on the App loop's R2 run surface for App `HELP_HUMAN` routing. No Root surface was written.

## From / to

- From: `chirality-app-dev`, D-APP-88 Option B R2, PKG-09 / DEL-09-04
- To: Root runtime owner / Root coordination loop
- Request type: bounded cross-package investigation; coordination, not authority

## App finding

The App loop separately built a complete Electron helper product with canonical helper ID `com.chirality.app.runtime-helper`, builder-generated matching Chromium helper topology, and deterministic whole-bundle embedding. A fresh helper produced a directly logged graceful stop. After GUI contact on the same Unix-socket runtime, the retained App logs show the helper restart, GUI contact, no later daemon shutdown entry, and eventual GUI transport loss. The required auditable post-GUI first-signal graceful-stop proof was not achieved, so D-APP-88 remains open and all R2 product bytes were rolled back.

The operator also observed first-signal process survival/socket retention and second-signal termination, but no contemporaneous command/process/socket snapshot was retained. Those stronger observations are unauditable and are not promoted as findings.

## Claim-calibrated Root hypothesis

`HYPOTHESIS`: a live GUI Unix-socket/SSE or other long-lived client connection may prevent Root `RuntimeDaemon.stop()` from completing its awaited Node `server.close()` callback, which in turn prevents the App shutdown path from reaching socket/owner cleanup and `desktop.shutdown.completed`.

This mechanism is not proven. It is supported only by the source sequence and the fresh-stop/post-GUI contrast:

- Root `runtime/packages/daemon/src/runtime-daemon.ts` SHA-256 `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`, lines 90–101: `stop()` awaits `server.close(...)` before unlinking the socket and owner record.
- Frozen App candidate `electron/main.ts` SHA-256 `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491`, lines 710–744: App teardown awaits `runtimeHost.stop()` before completion logging/exiting.
- R2 drill report SHA-256 `0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275`.
- Sanitized daemon log SHA-256 `3be7915b764dee035ec2a33d57c14fdac66c92373d14c22f623b9672a49f73b5`.
- Sanitized GUI log SHA-256 `3c9ca281da3ac124dd0eb2ac5e894e21f68de71de68d40e6380ae4ec01faa44a`.
- R2 corrected implementation return SHA-256 `8ae2d74fae740b287e94b5730f0222a3fa4047e0f3e4c591e5af883462dbd49e`.

## Requested Root action

Please investigate Root-owned graceful shutdown semantics with an active Unix-socket client, including a live SSE/long-lived response:

1. reproduce `RuntimeDaemon.stop()` with an active client/stream and bind whether `server.close()` completes;
2. define the intended connection-drain/termination contract for graceful daemon shutdown;
3. add bounded Root tests for ordinary stop with active clients and socket/owner cleanup;
4. if a Root change is warranted, implement it under Root authority and return exact commit/test/evidence references to the App loop; and
5. if no Root defect exists, return the disproving evidence and the next bounded App diagnostic seam.

No Root source change is authorized by this notice. The App loop will not fake GUI teardown or weaken D-APP-88 recovery semantics.

`TM-CANDIDATE: Root runtime graceful stop may await active Unix-socket/SSE connections indefinitely, blocking App daemon teardown after GUI coexistence | D-APP-88 R2 DRILL_REPORT.md SHA-256 0ea6c32de0ed122750d2c759e9aee1a163d4275509c6861258c34f5203c09275; runtime-daemon.ts SHA-256 a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46 lines 90-101`
