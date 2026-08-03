# Recovered sanitized transcript excerpts

These are verbatim excerpts copied from retained tool-call results in the active managed run after the original later temporary trees had already been removed. They contain no token bytes. They are not substitutes for original log files; claims are narrowed accordingly in `DRILL_REPORT.md`.

## Packaged CLI observed the helper PID

```json
{
  "daemon": {
    "apiVersion": "v1",
    "status": "ok",
    "daemonId": "dc30c94d-f01f-4a5b-8fe9-a59177c1842d",
    "pid": 22313,
    "startedAt": "2026-08-03T06:36:58.257Z",
    "socketPath": "/tmp/chirality-dapp88-final.8zXqCY/user-data-exact/runtime/control.sock"
  }
}
```

The full returned engine inventory was observed but is omitted here as immaterial to bundle identity.

## GUI/helper coexistence owner and process excerpts

```text
owner daemonId=dc30c94d-f01f-4a5b-8fe9-a59177c1842d pid=22313 startedAt=2026-08-03T06:36:58.257Z
22313 .../Chirality Runtime Helper.app/Contents/MacOS/Chirality --runtime-daemon
23632 .../Chirality.app/Contents/MacOS/Chirality
```

Later final conventional candidate:

```text
owner daemonId=da6c2ab5-f719-4a20-8573-2bd70127080d pid=32164 startedAt=2026-08-03T06:48:02.613Z
32164 .../Chirality Runtime Helper.app/Contents/MacOS/Chirality --runtime-daemon
32218 .../Chirality.app/Contents/MacOS/Chirality
```

## Fresh graceful stop

```text
[chirality-desktop] 2026-08-03T06:45:52.677Z [info] runtime.daemon.starting {"activationPolicy":"prohibited","packaged":true,"userData":"/tmp/chirality-dapp88-mp.L2NCiI/user-data","pid":31453}
[chirality-desktop] 2026-08-03T06:45:52.693Z [info] runtime.daemon.started {"socketPath":"/tmp/chirality-dapp88-mp.L2NCiI/user-data/runtime/control.sock","runtimeDirectory":"/tmp/chirality-dapp88-mp.L2NCiI/user-data/runtime"}
[chirality-desktop] 2026-08-03T06:46:33.460Z [info] desktop.shutdown.started {"reason":"before-quit","exitCode":0,"daemonMode":true,"pid":31453}
[chirality-desktop] 2026-08-03T06:46:33.461Z [info] desktop.shutdown.completed {"reason":"before-quit","exitCode":0}
SOCKET_ABSENT
```

The independently salvaged raw `flags-desktop-daemon.log` records the same clean-start/clean-stop shape for PID 16953.

## Post-GUI SIGTERM failure

After GUI PID 32218 exited, first SIGTERM to helper PID 32164 produced no shutdown log; the bounded poll returned:

```text
32164 Ss+ .../Chirality Runtime Helper.app/Contents/MacOS/Chirality --runtime-daemon
SOCKET_PRESENT
```

After a second SIGTERM:

```text
process absent
SOCKET_PRESENT
```

## Post-GUI SIGUSR2 diagnostic failure

After GUI PID 35558 exited, SIGUSR2 to helper PID 35524 produced no shutdown log; the bounded poll returned:

```text
35524 Ss+ .../Chirality Runtime Helper.app/Contents/MacOS/Chirality --runtime-daemon
SOCKET_PRESENT
```

The SIGUSR2 diagnostic code was removed before candidate freeze and product rollback.

## SIGKILL recovery excerpt

After exact helper PID 22313 was killed, a same-state restart reported:

```text
[chirality-desktop] 2026-08-03T06:40:54.516Z [info] runtime.daemon.starting {"activationPolicy":"prohibited","packaged":true,"userData":"/tmp/chirality-dapp88-final.8zXqCY/user-data-exact","pid":29500}
[chirality-desktop] 2026-08-03T06:40:54.536Z [info] runtime.daemon.started {"socketPath":"/tmp/chirality-dapp88-final.8zXqCY/user-data-exact/runtime/control.sock","runtimeDirectory":"/tmp/chirality-dapp88-final.8zXqCY/user-data-exact/runtime"}
owner daemonId=02bb8bec-9d07-46bb-b937-91dfe5266ffe pid=29500 startedAt=2026-08-03T06:40:54.517Z
```

## Stability limitation

The retained raw logs prove successful startup/socket publication, not a particular stable duration. Duration bounds were observed through live session polls but the original later session transcript files are unavailable. The durable claim is therefore only: the helper reached socket-ready, the CLI queried the same PID, and GUI coexistence retained that owner PID during the observed bounded window.
