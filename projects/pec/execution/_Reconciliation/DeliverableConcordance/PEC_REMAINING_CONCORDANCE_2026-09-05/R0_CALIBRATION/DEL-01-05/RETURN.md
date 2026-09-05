# DEL-01-05 R0 return

**Assessment: ASSESSED_WITH_RESIDUALS.** 61 claims; 5 proposed residuals.
Disposition counts: `{"ALIGNED": 46, "LIFECYCLE_REASSESSMENT_REQUIRED": 1, "PARTIALLY_IMPLEMENTED": 7, "UNKNOWN": 7}`.
All 32 REQ/AC/VER identifiers and all 28 other local stable IDs are covered,
plus one explicitly mapped lifecycle claim. This is sample calibration only.

Source basis: accepted decomposition revision 1.4, live PRD v2.2 and D-PEC-81
O-A at `faf22452528b5ba895e88ba0ad3770855100de08`. Accepted D-PEC-77 checker SHA-256
`3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643`
is unchanged; all 17 accepted artifact rows and all 7 historical manifest rows
rehash exactly. READ_MANIFEST.json binds every read file and current/historical
verification source. Later acceptance, AC-010/011 confirmation and CHECKING
remain intact; tests are not acceptance, issuance or release.

Current 19/19 enforcement tests pass, and live posture returns PASS with core-tree
`2c830d1fe9bc7f550c47d5f22223f330a3a95118360e61bb6d9c785b47c151ca`.
Two static scratch probes nevertheless return PASS incorrectly against the broad
REQ-001/REQ-003 obligations: aliased import_module("requests") and external UDP
socket.sendto. PROBES.py and PROBE_RESULTS.json preserve source, source hashes,
checker/workflow hashes and actual results. No fixture was executed. Additional
unreadable-surface fault injection correctly returns BLOCK. Exact command and
captured existing test results are in READ_MANIFEST.json.

Owner choices: accept/amend the two detected-gap proposals and route an exact
source/test repair packet; supply or clarify VER-004 state-sequence/release-candidate
evidence; retain explicitly historical frozen SOW prose or authorize exact
harmonization; direct REVIEW's lawful candidate disposition. No automatic source,
Remaining, lifecycle, dependency or TM act follows. Source repair and Remaining
application need separate exact owner grants beyond D-PEC-81.

Convention lessons: finite method PASS can coexist with behavioral partial;
static scanner coverage differs from a runtime enforcement guarantee. Exact
accepted artifacts can contain newly demonstrated weaknesses without erasing
historical owner acts. Frozen dated context should not automatically trigger
metadata/currency work. Unknown present-state-text treatment is kept separate
from known CHECKING and AC-011 acceptance; VER-004 is a genuine evidence gap,
not an invented release task. These conventions remain proposals.

Hold preflight for exact-correction-preparation on the actual SOW and status
returned ALLOW; register is header-only. Local dependencies are three satisfied
anchors and create no blocking edge. TM-PEC-023 dedicated hold, TM-PEC-022
lifecycle deferral, ordinary currency completion, PRDv2.3/DPEC79 non-application
and all source fences are preserved without new gates.

Writes are limited to this worker subtree: CLAIMS.csv, RESIDUALS.csv, COVERAGE.md,
READ_MANIFEST.json, RETURN.md, PROBES.py and PROBE_RESULTS.json. BRIEF.md remains
sealed. Source/target current bytes reproduce their base Git objects; git status
including ignored files is empty for v2 and the target tree. Scratch probes and
suite temporary files use /tmp; bytecode writes are disabled. No Git mutation,
service start, network operation or production mutation occurred.

Closure: COMPLETE_FOR_R0_WORKER_RETURN / DERIVATIVE_NOT_ACCEPTED. Accepted upstream
snapshots are unchanged. No derivative production repair was performed; it is
explicitly deferred pending owner action. Next: independent verification and
manager calibration fan-in, then owner calibration/scale-out ruling. Source,
authority, hold or target drift requires affected claim rerun; exact repair and
Remaining application remain later gates.
