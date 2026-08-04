# Independent SIGKILL recovery and fresh-stop diagnostic

Status: `PASS — INDEPENDENT CONJUNCTS ONLY`

- Exact explicit SIGKILL: `/bin/kill -KILL 68725` at `2026-08-04T11:38:02-06:00`.
- PID `68725` became absent while socket inode `25337028` and owner inode `25337027` remained, mode `0600`; owner schema remained `chirality.daemon-owner/v1` and named PID `68725`.
- Exact final helper PID `68812` restarted on the same isolated store, authenticated/recovered stale state, and created socket inode `25337049` plus owner inode `25337048`.
- Fresh, no-GUI stop command: `/bin/kill -TERM 68812` at `2026-08-04T11:38:24-06:00`.
- PID exited in one 0.1-second poll; socket and owner became absent.
- Logs contain `desktop.shutdown.started` and `desktop.shutdown.completed` at `2026-08-04T17:38:24.597Z` / `.598Z`, reason `before-quit`, exit code 0.

This proves explicit SIGKILL recovery and a fresh no-GUI graceful stop. It does not cure or weaken the mandatory post-GUI first-signal failure.
