# Stop diagnosis and compact progress recommendation

Scope: read-only product inspection at frozen candidate `266c121bb32f9a22c072e7fb3b3f650b290bcdc6`. This return records parent-observed live evidence; this specialist performed no live UI/API operation, product edit, build, or Git mutation.

## Stop evidence and disposition

Parent observed two successful Cua Playwright `getByRole('button', {name: 'Stop', exact: true}).click()` calls during J06, but no Stopping state and no interrupt request in filtered development logs; work continued. These click success reports alone do not establish handler execution.

Source inspection found the Stop button's disabled condition matches the handler's only entry guard (`!isRunning || !activeSession`). The handler sets `stopRequested` before awaiting the immediate client POST to `/api/harness/interrupt`; a client failure should instead show a runtime error. Ordinary progress events do not clear `stopRequested`. Relevant source: `frontend/src/components/shell/chat-panel.tsx` (`interruptTurn`, Stop button, derived turn phase), `frontend/src/lib/harness/client.ts` (`interruptHarnessSession`), and `frontend/src/app/api/harness/interrupt/route.ts`.

Parent then performed the discriminating J08 keyboard test: Stop was enabled, `locator.press('Space')` immediately displayed “Stopping the turn…”, the filtered log recorded `POST /api/harness/interrupt 200`, and the UI reached “Stopped” with two actions.

Disposition: pointer automation/hit-test discrepancy; no established Runtime Stop defect. Exact pointer failure mechanism remains unproven. No Stop source repair is warranted by this evidence.

## Compact progress recommendation

Parent observed the primary compact progress line displaying `/bin/zsh -lc cat fullpath...`, which is too technical for the target professional user. `frontend/src/lib/shell/turn-activity.ts::summarizeTurnActivity` currently appends the latest activity detail (up to 140 characters) to its title; tool detail can contain the supplied raw command summary.

Recommend a concise plain-language activity label plus observed action count in the compact line, for example “Running an action · 4 actions”. Use more specific labels such as “Reading a file” only when reliable tool metadata identifies that activity; do not infer purpose from arbitrary shell text. Retain the raw command and full path in expandable Activity details. Preserve truthful approval, failure, stopping, and completion states. This is a proposed future tranche change, not an implemented repair.

Handoff: diagnosis complete; no product files changed and no tests required for this evidence-only return. Parent continues remaining live journeys and owns subsequent repair selection. This record is derivative diagnostic evidence, not governed deliverable acceptance or closure.
