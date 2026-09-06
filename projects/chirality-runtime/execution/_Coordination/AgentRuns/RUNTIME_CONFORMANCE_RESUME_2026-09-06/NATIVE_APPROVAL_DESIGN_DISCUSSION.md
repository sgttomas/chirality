# Native child approvals — decision before implementation

A real Candidate2 child approval request was rejected by the current primary-only Runtime adapter. Primary approvals pass. The existing child association map is insufficient to authorize the child: it does not track exact child turn lifetime, and supplier events can arrive before the parent spawn-completed association.

The governing basis remains DEL-02-09 continuity and network constraints, DEL-02-10 attributed requests/decisions and closed projection, and DEL-02-11 retirement and terminalization. This note is a derivative diagnosis, not an amendment to those deliverables. Pi SDK and the pinned t3code comparison are implementation references only.

The proposed direction for discussion is to keep the existing live Runtime worker generation as the authorization boundary and separately validate the child that originated each approval. This would require consistent checks when a request arrives, when it is shown, when a decision is sent, and when either child or parent ends. Removing the primary check alone is not a valid repair.

Before implementation, decide whether accepted approval attribution must preserve the exact child origin after shutdown. The current persisted request identifies the Runtime authority and trusted supervisor; it does not include a closed child-origin projection. Durable child attribution could require a public schema decision. Transient attribution still needs lifecycle state and an explicit policy for out-of-order events. These are material design choices, not justified merely by an external example.

Recommended next step: discuss the required attribution contract, then authorize the smallest design that satisfies it. Bounded, sanitized lifecycle observations can establish actual event ordering before authoring that design. No native approval source change, new registry, public field, lifecycle semantic, or migration has been made in this follow-on. The current failure remains explicit.

Evidence: IMPLEMENTATION/REVIEW_APPROVAL_NATIVE_ATTRIBUTION_DIAGNOSIS/RETURN.md and REFERENCE_PATTERNS/REPORT.md; exact actual result is PARENT_CHECKS/NETWORK_PUBLIC_NATIVE_ASK_ALLOW_CANDIDATE2_01. The latest owner instruction requires discussion before significant refactoring, migration, overhaul, or rethink.

HELP_HUMAN / Agent 0, OpenAI GPT-6; exact serving model ID unavailable. Role enforcement is instruction-asserted.
