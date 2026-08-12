# D-APP-93 owner trace execution record

Status: `FACTS-ONLY OWNER-EXECUTED EVIDENCE RECORD — DISPOSITION RESERVED TO OWNER`

## Authority and execution basis

The owner ruling dated 2026-08-11 froze the six packet files at aggregate
SHA-256 `db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83`.
Under K-AUTH-1, the ruling states that owner assembly superseded the twelfth
lineage's manager-freeze step and that the minder integrity verification and
semantic review plus the owner's own runbook read superseded the standing
fresh-agent-verifier precondition. The ruling is preserved at SHA-256
`82ff1f170bad5277d4391211a37245f4dcde838ea4129f953d8f61ca84191bd3`;
the minder review is preserved at
`5c7584a95fa25e3258aa1b3b112895da3064c75a0fc502cdfbefaad31f765631`.

The owner executed the packet. Step 0 passed: all five binary identities
matched, the LLDB neutral probe exited 0 with the required output shape, and
the owner-side process-list probe exited 0 with numeric output. The Step 0
record is SHA-256
`cda4b36b007ace33514a20479091a8053e6436c84f4cca36cca704878677f845`.
The trace completed with zero stop rules triggered. The capture script bound
the transcript into the completed evidence form. The transcript is SHA-256
`43763e06b4d3536f48713cfc5b5d4a69b496d3fd4057212b5da3694262740536`;
the completed evidence form is SHA-256
`fe0f89eea64a294e1c050e6bc46cd6d2934fe185f98d149fe54cfd6a8191d707`.

The target was rebuilt from the frozen D-APP-88 R2 candidate source. The
completed evidence form records reproduction of all 12/12
`SOURCE_MANIFEST.md` hashes per the D-APP-92 rows. The rebuild card is
preserved at SHA-256
`b51709676ab502508b486ecbd28211b967485e7dd3ecc7f15ecb645287279651`.

## Trace facts

- SIGTERM was delivered to thread #1, `CrBrowserMain`, while it was blocked in
  `mach_msg2_trap` inside the AppKit / `NSApplication` event loop.
- At signal time, the helper held its listener plus two live client
  connections on the helper control socket, as recorded by
  `pre-signal.lsof.helper.txt` at SHA-256
  `cfa4128caa6108e6aaf29b264150c06b12fdf35d1f951f740d9d83d5be293d59`.
- No Node, libuv, or V8 signal-handler frames were present on any thread at the
  stop instant.
- The helper remained alive after detach. The daemon continued serving: the
  completed evidence form records a 408 response to the expired holder and a
  GUI reconnection; `post-detach.lsof.helper.txt` records the listener plus one
  re-established connection at SHA-256
  `ee0c1fb9ced1d8c289d1f95b800413b2772d2a0fa8a960cf87fd73a300864ded`.
- The matching pre-attach and post-detach helper lsof identities are expected;
  each is SHA-256
  `ee0c1fb9ced1d8c289d1f95b800413b2772d2a0fa8a960cf87fd73a300864ded`.

## Scope limit

LLDB configured SIGTERM with `PASS=false`; the debugger intercepted the signal
and did not forward it to the process. Unintercepted signal processing was not
tested by the packet trace. The trace therefore records delivery topology and
thread state under held client connections; it does not establish the
helper's behavior after an unintercepted SIGTERM and does not itself resolve
the D-APP-88 held-connection stall hypothesis.

Informal cleanup observation (2026-08-12T03:44Z, outside the packet): the owner
delivered the helper's first unintercepted SIGTERM (kill -TERM 44712) during
cleanup with the GUI in idle-poll state; the helper exited within 8 seconds
(HELPER-EXITED; GUI logged bind_failed from 03:44:10Z). Connection state at the
signal instant was not recorded; the GUI's idle poll holds a connection only
~4 s per ~10 s cycle. This observation neither confirms nor refutes the
D-APP-88 held-connection stall hypothesis.

## Coordination effect

The D-APP-93 packet is owner-executed and this evidence is prepared to land.
Disposition of the evidence and any D-APP-88 conclusion, remedy, acceptance,
or follow-on remains reserved to the owner. This record performs no closure,
lifecycle, reliance, product/runtime/source, or packet-byte act.
