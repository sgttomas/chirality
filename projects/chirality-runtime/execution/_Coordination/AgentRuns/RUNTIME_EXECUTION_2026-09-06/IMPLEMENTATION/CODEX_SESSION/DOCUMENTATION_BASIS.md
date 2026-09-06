# Protocol basis calibration

Observed exact 0.149.0 evidence: local SUPPLY_PROBE initialize, initialized, account/read refreshToken:false, thread/start with workspace-write request; negative turn/start parsed minimal text input and reached missing-thread lookup. Neither positive hosted turn events nor resume/interrupt were observed on that payload.

OpenAI Docs skill applied. Official documentation searched and actually opened on 2026-09-06: [Codex App Server](https://learn.chatgpt.com/docs/app-server), redirected from developers.openai.com/codex/app-server. It documents resume by thread ID, explicit turn model overrides, interrupt by thread/turn IDs, streamed message deltas, item lifecycle, and completion status. These supply candidate adapter shapes only. Unknown item kinds, notifications and all server approval/tool requests fail closed; no claim of exhaustive protocol support or successful pinned-payload hosted execution follows.
