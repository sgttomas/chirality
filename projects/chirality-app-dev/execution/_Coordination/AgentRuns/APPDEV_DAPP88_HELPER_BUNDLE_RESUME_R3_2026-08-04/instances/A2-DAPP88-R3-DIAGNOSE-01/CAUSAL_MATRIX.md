# D-APP-88 post-GUI signal causal matrix

| Evidence | Causal role | Finding | Confidence / limit |
|---|---|---|---|
| No-GUI first `SIGTERM` to exact helper PID `68812` logged shutdown start/completion, exited in one poll, and removed socket/owner. | Control | The App funnel and accepted Root bounded stop work when entered. | High. |
| Post-GUI first `SIGTERM` to exact helper PID `64825` left the process and same socket/owner inodes after 8 seconds and logged no shutdown start. | Earliest divergence | Divergence is before the first `teardown()` log; Root stop was not entered. | High for boundary; signal callback versus `before-quit` entry is not separately instrumented. |
| Repeated post-GUI first signal survived; second signal exited in one poll with no shutdown logs and stale socket/owner. | Consequence | Native termination bypasses App/Root cleanup after the absorbed first signal. | High. |
| Frozen helper entry adds `single-process`; frozen main already has JS `SIGTERM` and Electron `before-quit` funnels. | Candidate contributor | `single-process` is plausible but unproved; existing lifecycle funnels are insufficiently observable. | Source fact high; causality unknown. |
| R2's standard-process arm reportedly also failed but has no retained raw evidence. | Alternative | Removing `single-process` cannot be named a remedy from R2 observation alone. | Unauditable. |
| Four local Electron 43.2.0 arms—standard idle/contact and single idle/contact—each aborted before ready with exit `134` and no event/stdout/stderr. | Reproduction blocker | No standard-versus-single live comparison was obtained; no signal was sent. | High for abort; abort cause unknown. |
| Accepted Root stop bytes succeed when invoked and were never invoked in the failed post-GUI attempt. | Ruled-out alternative | This diagnosis supports no additional generic Root change. | High; Node 22.19 unexecuted. |

Conclusion: `CONFIRMED_BLOCKER`. The root cause remains inside the
Electron/App signal-dispatch seam before observable teardown entry. A lawful
remedy requires the exact instrumented standard-versus-single packaged matrix
defined in `RETURN.md`; no current source hunk has adequate causal support.
