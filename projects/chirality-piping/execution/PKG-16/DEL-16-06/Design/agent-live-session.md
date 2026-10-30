# Embedded agent live session — implementation candidate

RT-E1 / DEL-16-06. The owner's activation authority in embedded-agent-host.md
applies. This increment implements the live binding and native lifecycle while
its public Start branch remains refused by the compiled `NATIVE_QUALIFIED =
false` gate. There is no panel, button, automatic supplier start or environment
bypass. Native qualification uses a separate opt-in native-smoke process mode
of the actual app executable and the same internal runtime constructor.

## Trust and custody

The raw `embedded_agent_host` command admits at most 256 KiB before typed
interpretation, with a separate 32 MiB ingress allowance for derived values.
It derives the invoking main webview and bundled origin from Tauri, and native
resource and state paths from AppHandle. The model cannot select them. Windows
and Linux return isolation unavailable. macOS owns one lazy actor with a bounded
16-request channel, separately admitted 1 MiB stack/2 MiB thread allowance,
32 MiB state allowance and 512 KiB response allowance. No worker starts merely
from constructing the workspace session or checking availability.

Native registration issues a random workspace handle, generation, private
producer capability and separate protocol session token. Only the actual
workspace execution closure keeps the capability. It is absent from notices,
claims, model arguments, provider traffic, persisted settings and logs. This
trust boundary assumes the bundled workspace JavaScript, not arbitrary script
execution in the webview. Tool data never installs an execution producer.
The original JSON-RPC destination remains private to Protocol; completion uses
only an opaque requestRef. Claims remain one-shot on transport failure.

The producer publishes actual queue/read/job evidence before completion. The
native owner separately retains that record and checks exact completion-byte
equality, catalog validity, basis and job standing. A completion cannot create
its own evidence. Queued, detached, lost and unconfirmed delivery do not change
actual standing. Closed contexts accept late actuals for already claimed work;
there is no automatic domain replay. Native take_actual transfers a copy of the
actual while preserving tombstones and historical references. The four retained
workspace contexts and their 64-call ledgers refuse capacity explicitly rather
than evicting outcome evidence; restarting the app loses ephemeral handles.
These limits do not provide durable audit/history.

The workspace owner supplies its actual immutable batch registration, proposal
standing and existing native solve receipt. Agent operations are stamped as
proposed/agent, with original request/thread/turn/call, basis and assumptions
outside the native intent schema. Supplier validation/source claims are reset.
The sole operation engine validates; only existing person Apply publishes a
model. Outcome hash/standing updates in that same synchronous publication.
Interruption withdraws only still-pending agent batches; a synchronous application
admission set prevents withdrawal once Apply has begun. It never cancels a solve
or claims rollback. Existing queue events preserve withdrawn/unknown standing.

Read producers bound pages before collecting rows. Cursors bind tool, basis,
offset and run. Summary counts do not serialize the model. Node pages preserve
source units and negative zero. Results use existing numerical overlay policy;
this initial adapter conservatively withholds retained-precision values rather
than substituting rounded binary64. Full criterion 17 operation discriminators,
retained source-value presentation and the actual desktop review witness remain
open; the canonical v2 catalog bytes are unchanged.

## Native lifecycle and the qualification harness

Live owns the admitted dual-family loopback relay, private runtime and original
supplier Child. It starts fixed initialize/thread/start protocol steps and holds
partial startup custody through cleanup and worker joins. Provider selection
loads the exact saved revision from the reviewed Store; the secret goes only
to the host relay. The child receives only a fresh relay capability. No profile,
credential, persistence format or TLS-trust permission is widened here.

The new narrow unsafe process_scope boundary uses SDK kqueue/kevent on that
retained original Child only: NOTE_EXIT, NOTE_EXITSTATUS and NOTE_FORK. It checks
FD_CLOEXEC. Fork, identity and observation errors latch permanently. It never
uses unsupported NOTE_TRACK/NOTE_CHILD, descendant snapshots, recursive ancestry
or signal authority. The inherited deny-process-fork policy, including
posix_spawn(self), covers supplier startup before observation is armed. A group
census alone is not proof of descendants. Native removal needs both original
group cleanup and a non-invalidated exit observation; unknown retains marker,
backing and refusal state. No later sample can repair invalidation.

The actor's ordinary quit hook requests close and exits the app only after
original group cleanup and distinct driver/relay joins. Cleanup unknown keeps
custody and refuses exit/restart rather than using saved PIDs. Hard-death cleanup
is not claimed by that quit hook and must pass the following native matrix.

The native-smoke mode reads bounded invented configuration from anonymous stdin,
resolves resources from its actual bundle and runs negative probes first, under
the very same profile builder with only the probe executable substituted. The
C probe requires EPERM for fork, posix_spawn(self) and forbidden exec. The Rust
probe checks private writes, outside reads/writes/symlink, both owned loopback
families, an unowned loopback alias/port, off-host, syslog, Users reads, listening
and exec. Missing records are not_run/unknown; terminating signal and first-record
standing are explicit. Fresh probe copies avoid invalidating a cached Mach-O
signature by rewriting an executed file.

The Python controller owns the actual app and anchor Popen objects. The app
holds its original SDK unreaped at a startup gate. While it is alive, the
controller arms original-process exit/fork observation and joins its owned
anchor to that group, then opens the protocol gate. The anchor preserves rescue
authority after app SIGKILL. It kills only its own group through a fixed command;
no recorded PID becomes signal authority. Owned-app and owned-anchor signals
use their original Popen handles. Liveness checks signal only zero.

Qualification order is a harmless summary-tool round trip, then stdin EOF and
app SIGKILL, each at idle, active-turn and pending-tool stages. Trigger records
follow bounded protocol draining and current stage/observer checks. A crash
result requires bounded control-reader completion through normal EOF, then a
stable full drain and terminal/failure validation. Final successful samples
recheck cancellation/safety and the deadline. Observed policy/observation failure
permanently forbids scope certification and runtime/marker removal while retaining
owned-group rescue. EOF/crash success requires original exit status zero and PID
absence, separately from group cleanup; a normal forced stop's status is not
relabelled as an EOF pass.

## Evidence and reconciliation

Source/component candidate only; no new supplier, model or app fixture execution
has yet occurred. Targeted checks cover controller EOF/cancellation/latching,
workspace authority, outcome-before-delivery, stale preparation, source pages,
late actuals and original native group preservation. The forthcoming run must
use the retained actual bundle with verified stock 0.160 resource bytes and
current candidate native-smoke code. ARM evidence cannot qualify Intel; the
public gate must remain unavailable on any unqualified architecture.

DEL-16-06 ScopeOfWork claims/ACs and all dependency conditions remain unchanged:
this implements their existing binding, proposal and cleanup duties, not their
acceptance. deliverable.yaml adds source/check pointers. DEL-08-01's exact unsafe
module list grows from twelve to thirteen only for process_scope, and its command
macro pin reflects the new command. No Cargo dependency or foreign block is
added; exact-set enforcement and report-release reach remain intact. Root routing
and runtime-read inventories are regenerated from the combined tree.
