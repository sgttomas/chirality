# Chirality v3 user journey campaign

Status: real journeys, artifact evaluation, source repairs and direct rechecks
are complete. PR validation and consolidated packaging are in progress. The
owner approved all four native interaction additions, including native steering.
RUN_LOG.md and JOURNEY_RESULTS.md carry current outcomes and limitations.
Owner direction: simulate real professional knowledge work in parallel from
signed-in sessions; first, tenth and hundredth use; collect failures through a
complete campaign and fix the useful tranche afterwards. Target release v3.0.0,
with publishing still subject to explicit owner direction.

Basis: main 6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f, product 26657ff90.
The prior signed artifact and all trial evidence remain preserved.

## Design work graph

- HELP_HUMAN owns alignment, source investigation, final campaign and UI testing.
- HELPS_HUMANS Astra/medium designs journeys independently under
  briefs/EXPERIENCE_DESIGN.md; no children or product writes.
- TASK Astra/medium maps UI failures and concurrent production paths under
  briefs/UI_SOURCE_TRIAGE.md; read-only, no children.
- Parent validates both returns and discusses the concrete campaign with owner.

Owner decisions, 2026-09-13T00:15:50Z: approve first picker at home with remembered
explicit folder, inline activity/message formatting and quiet Plan refresh;
request a concrete proposal for further native Codex features; authorize a CORE
create-workflow method followed for authoring; retain path/discovery testing;
hide Skills UI for this release and keep background skill use; investigate
workflow refresh after conversational authoring. The new workflow author writes
only the declared library/instruction files under briefs/CREATE_WORKFLOW.md.
HELPS_HUMANS designs additional interactions read-only under
briefs/NATIVE_INTERACTIONS_PROPOSAL.md. Baseline uses frozen 26657ff90 source,
isolated from these source writes. No package is rebuilt per repair.

No live identity, auth, binding, token, keychain, Codex home or session/event
file reads; no security commands. Owner performs authentication if needed.
Use existing permitted production UI and guarded launch path during execution.
Synthetic fixtures and outputs occupy dedicated writable test folders. All logs
exclude lines containing an at-sign. No external communication or publication.

## Proposed campaign, 2026-09-13T00:05:10Z

This is a discussion proposal, not a claim that the journeys have run. The
owner's subsequent screenshot confirms visually concatenated progress messages
and a clearly rendered final document. It does not independently establish
artifact accuracy or expose the in-progress banner's position.

Measure whether ordinary professionals can express an objective, help resolve
ambiguities, obtain reviewable work and reuse what they learned. Technical test
passing and attractive output are insufficient by themselves. Synthetic users
are diagnostic probes; they cannot establish real novice usability or adoption.

### Journeys

| ID | Experience | Work and expected result |
|---|---|---|
| J01 | First | Meeting notes into a saved action brief. Separate agreements from suggestions, keep the unassigned action visible, apply an owner correction. |
| J02 | First | Compare three workshop venues. Detect capacity and budget constraints; a later accessibility requirement makes every option noncompliant, requiring an explicit tradeoff. |
| J03 | First | Explain two conflicting fictional internal policy documents. Surface unresolved authority, then use the supplied amendment and cite the basis. |
| J04 | Tenth | Plan a staff workshop, answer a native clarification, shorten its duration, execute the revised plan and inspect the agenda/materials. |
| J05 | Tenth | Turn a successful monthly briefing into a workflow, find it from a fresh chat, use changed inputs and identify missing information. Compare button-assisted and ordinary chat authoring. |
| J06 | Tenth | Continue interrupted supplier-summary work, preserve completed work, apply a corrected source and finish without duplication or unsupported completion. |
| J07 | Hundredth | Three-cycle operations review: plan, execute, correct, save method, reuse with changed owners and a reopened item, refine method, reuse again and validate the combined pack. |
| J08 | Hundredth | Change a client deadline in an established project. Propagate two affected outputs, preserve the unaffected one, explain remaining decisions. |

Tenth/hundredth describe supplied familiarity and accumulated artifacts, not
10/100 simulated chats or unearned long-history/compaction evidence. J07 really
executes successive cycles and carries its outputs forward. Historical seed
documents, when used, are labeled fixtures. The eight journeys use different
small work folders, ordinary prose/CSV/office-document/image attachments and
known facts or arithmetic. Prefer two to four small source files per stage.
PDF uses the accepted default-app path. No real business files are required.

Expected quantities and hidden omissions are frozen in an evaluator-only answer
key outside the App's workspace. The simulated user receives persona, objective,
visible inputs and later steering, with no answer key, implementation hints or
repair instructions. Follow-ups react to actual App responses in normal language.
An expert workaround is recorded separately and never converts a failed novice
journey into a pass. Evaluate the work with a fresh instance that did not produce
the artifact, and verify known arithmetic mechanically where useful.

### Parallelism and Agent 0 oversight

HELP_HUMAN remains the sole UI driver and coordinator. HELPS_HUMANS has advised
the campaign; bounded Type 2 instances can simulate human follow-ups and evaluate
outputs directly without adding a permanent manager per lane. Product agents
inside Chirality remain distinct from these test workers.

Target three simultaneous product conversations in isolated work folders, with
J07's dependent cycles sequential within its lane. First prove two distinct chats
can run concurrently through permitted real renderers. Source supports Runtime
per-session concurrency but the current App window disables chat switching while
streaming. Multiple browser renderers against the existing App-owned service are
a candidate, not yet proven. Verify per-tab session identity, root and draft
isolation and shared-storage behavior before increasing to three. Only one
computer-use driver owns clicks and typing. Native dialogs remain serialized;
model and tool work can overlap. No copied credentials, fake session injection,
direct bypass of App turn construction or multiple drivers on one window.

If multiple renderers cannot operate safely, continue serial UI journeys while
fixture preparation and evaluation run in parallel. Report the limitation rather
than quietly replacing UI tests with API tests. Do not build a new multi-window
feature simply for the campaign. Active-work chat navigation can be considered
as a user-facing issue during triage, not presumed to be in the release tranche.

### Efficient use of the real account

Start signed in and confirm the available model/effort catalog through the App.
Use gpt-5.6-sol medium for ordinary production journeys and gpt-6-astra medium
for sustained coordination. Verify actual availability and preserve any deliberate
substitutions in results. The owner-directed test workers use gpt-6-astra medium,
with high reserved for consequential or repeated failures under the standing
exception. One bounded comparison with the owner's selected model may distinguish
model-sensitive behavior. Do not run a model-by-scenario matrix by default.

Allow roughly three to five user turns per ordinary journey, and nine to twelve
for J07 with stage-based extension if needed. These are scope expectations,
not timers that interrupt valid work. Long runs do meaningful document work,
not manufactured sleeps. Begin with two simultaneous turns, sample observed
latency and available usage telemetry, then allow three if sustainable. Count
product subagents in total concurrency; discourage unnecessary fan-out through
bounded task briefs without changing permanent product behavior.

Use compact inputs, concise outputs appropriate to the assignment, reused
fixture families with changed facts, and targeted repetitions after failures.
Record actual token/usage evidence when the App provides it; missing data is
unavailable, not zero. Do not infer an unlimited quota from the plan name.
Unexpected rate pressure reduces new launches while active work finishes.

### Observation and anomaly record

One result row per journey stage records run ID, product revision, App mode,
actual model/effort, visible chat identity, fixture and output references, user
actions, expected observable, actual observable, outcome and anomaly IDs.
Capture timestamps for first acknowledgment, useful progress, question, artifact
and ending, plus available usage. Take focused screenshots at transitions and
retain concise visible transcript excerpts. No protected session-file scraping.

Score two axes separately:
- Experience: discoverable controls, intelligible questions/progress, avoidable
  confirmations, retained drafts/history, ability to steer and resume, and
  whether an ordinary user can locate and inspect the result.
- Work quality: correct arithmetic and constraints, source traceability,
  fact/assumption separation, acknowledged conflicts, consistency after revisions,
  useful artifacts and reuse with fresh facts rather than stale copying.

The anomaly log distinguishes reported, reproduced, source hypothesis, confirmed
cause, repaired and rechecked. Cluster duplicate symptoms under a cause while
preserving each original observation. Record false completion, lost/crossed
history, wrong-root writes, unresolved question stalls and invalid artifacts as
more consequential than cosmetic friction. Never declare all professional work
validated from eight synthetic journeys.

Freeze the baseline source during collection. Ordinary failures stay recorded;
continue unaffected stages and lanes. One normal recovery attempt is permitted
before marking a blocked step and continuing what remains possible. Do not keep
repeating the same broken step or abort useful running work. A shared failure
that threatens data, mixes sessions, or prevents meaningful progress across the
campaign pauses affected launches and receives immediate owner notice.

### Owner observations and proposed response

| ID | Observation and status | Investigation or proposed refinement |
|---|---|---|
| O01 | Trial folder restored. Source initializes no default root, then restores localStorage. No hard-coded Trial Workspace found in shipped frontend. | Test clean selection state separately from returning profile. Propose first native picker at home, then last explicitly chosen valid work folder; do not automatically turn all home contents into a project. |
| O02 | Floating progress and joined text. Screenshot confirms missing boundaries; supervisor text events discard distinct native message IDs. | Preserve native item identity and phase through live/replay. Put compact activity beside the latest assistant entry, show supplied reasoning summaries and current tool/child, group past activity, separate final output. Keep Activity panel. No invented progress percentages or reasoning. |
| O03 | Plan Refresh cycling. Source polls each second and toggles manual busy state each fetch. | Reproduce active and terminal cases; separate quiet background updates from manual refresh. Do not claim an infinite loop until observed. |
| O04 | Native question UI was useful. Protocol has plan, reasoning, tool and collaboration events and server requests. | Map supported vs generically displayed vs unavailable in pinned 0.154. Codex sends data, not drop-in Codex desktop components. Prefer more faithful rendering; broader features remain future scope. |
| O05 | Workflow-authoring method hard to discover. Current index has no dedicated creator found; preserved former HELPS_HUMANS has a multi-phase design method. | Trace that history and existing standard/template before adding anything. The current instructions should point to canonical authoring shape; reading a template is reasonable, unnecessary hesitation is testable. |
| O06 | Workflow link becomes localhost URL for Downloads/.chirality/workflows/name/WORKFLOW.md. | Filesystem location is correct for a Downloads-rooted project; personal library belongs under home/.chirality/workflows. Resolve actual raw href, four-level depth vs catalog depth three, URL fallback and library presence separately. Never treat arbitrary localhost URLs as trusted file reads. |
| O07 | Skills Inspect appears inert. Source puts returned inspection below whole catalog without focus. | Compare filtered/unfiltered inspection and error path; use visible focused details or inline expansion if confirmed. Skill editing remains read-only. |
| O08 | Chat-authored workflow absent while plan action appeared. No post-turn method-list invalidation; plan action only prepares a chat prompt. | Check package validity and manual refresh/reopen before blaming authoring. Prefer catalog refresh on relevant completion/change; preserve explicit selection and avoid polling/flicker. |

### Bounded progress presentation

Keep existing typography, dark/light palettes, warm accent, composer and side
panels. At the current assistant position, show a small working indicator and
the latest meaningful supplied status; expand to readable reasoning summaries,
tool steps and delegated work. Subsequent commentary occupies its own entry
with native boundaries, and the final answer is distinct. Collapse completed
work by default while retaining inspection. Respect deliberate scrolling and
reduced motion. A compact return-to-live control may point back to active work.
Status reflects observed state, never estimated completion or fabricated thought.

References checked 2026-09-13 UTC:
- OpenAI App Server: https://learn.chatgpt.com/docs/app-server (reasoning summary
  deltas, item boundaries, plan items, user input and server-request handling).
- T3 timeline: https://github.com/pingdotgg/t3code/blob/main/apps/web/src/components/chat/MessagesTimeline.tsx
  (working/thinking timeline rows and grouped work). T3 also has composer status;
  the relevant comparison is clear context and message boundaries, not an
  absolute claim that it has no composer indicator.

### Delivery

After the baseline completes, HELP_HUMAN reconciles evaluations and selects one
bounded repair tranche centered on successful plan, execute, save, reuse and
iterate. Small repairs to broken controls are release candidates; new planning
features or a broad redesign are not prerequisites. Independent review covers
the actual changed source. Re-run affected journeys and an unchanged control,
plus appropriate deterministic integration checks, rather than every possible
test per cosmetic change. One consolidated package follows stable fixes. Set
actual release identity to v3.0.0 with matching bundle/release artifacts at that
point, then owner final review and explicit publishing direction.
