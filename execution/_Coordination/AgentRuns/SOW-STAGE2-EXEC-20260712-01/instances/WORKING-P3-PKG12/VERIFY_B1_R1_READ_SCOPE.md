# VERIFY-B1-R1 Enforced Read Scope

Status: `FROZEN BEFORE DISPATCH`

The replacement verifier may read only:

- root and Piping `AGENTS.md`, `agents/AGENT_TASK.md`, its own launch brief,
  the parent package launch/activation/preflight/work-graph records, original
  package/verifier contract, and `BRIEF_V2.md`;
- `B1_AUTHOR_ACCEPTANCE.md`, which freezes candidate counts and hashes;
- accepted W-P3 preflight rows and package/member live source/control inputs;
- clean candidate families beneath `candidates/W_P3/PIP-PKG12/**`;
- registered Scope-of-Work standard, skill companions, deterministic tools,
  tests, and Piping check profile.

Every path beneath `children/AUTHOR-B1/**` is prohibited, including its
manifest, helpers, and evidence. Every path beneath `children/VERIFY-B1/**` is
also prohibited except the parent-owned disposition summarizes its terminal
exclusion. Other package candidate and child paths are prohibited. Writes are
limited to `children/VERIFY-B1-R1/**`. A post-run access/containment audit is a
mandatory acceptance gate.
