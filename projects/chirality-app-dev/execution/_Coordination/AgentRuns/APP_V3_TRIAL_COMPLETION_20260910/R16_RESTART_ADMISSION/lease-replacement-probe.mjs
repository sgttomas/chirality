import assert from 'node:assert/strict';
import { HostAccountAuthority } from 'file:///Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335/projects/chirality-runtime/packages/daemon/dist/host-account-authority.js';
import { issueHostedAccountAuthorityV2FromP2, revalidateHostedAccountAuthorityV2 } from 'file:///Users/ryan/dev/chirality/.claude/worktrees/owner-alignment-inspection-db4335/projects/chirality-runtime/packages/daemon/dist/runtime-conformance-v2-admission.js';
// Synthetic in-memory carrier only: no native server, credentials or filesystem state.
const source = Object.create(HostAccountAuthority.prototype);
source.generation='controlled-daemon-generation'; source.closing=false;
source.active={clientId:'host-A',connectionId:'connection-A',revoked:false};
const subject={purpose:'worker',projectId:'controlled',manifestHash:'a'.repeat(64),canonicalRoot:'/controlled',account:{accountId:'synthetic-account',accountEpoch:1,accountDigest:'b'.repeat(64)},consentDigest:'c'.repeat(64)};
const old = issueHostedAccountAuthorityV2FromP2(source,subject);
await revalidateHostedAccountAuthorityV2(old,subject);
source.active.revoked=true;
await assert.rejects(revalidateHostedAccountAuthorityV2(old,subject),e=>e.details.reason==='HOST_AUTHORITY_NOT_LIVE');
source.active={clientId:'host-B',connectionId:'connection-B',revoked:false};
await assert.rejects(revalidateHostedAccountAuthorityV2(old,subject),e=>e.details.reason==='HOST_AUTHORITY_NOT_LIVE');
const renewed=issueHostedAccountAuthorityV2FromP2(source,subject);
await revalidateHostedAccountAuthorityV2(renewed,subject);
assert.notEqual(old.liveLeaseDigest,renewed.liveLeaseDigest);
assert.equal(old.daemonGeneration,renewed.daemonGeneration);
console.log(JSON.stringify({status:'PASS',scope:'synthetic lease issuer/revalidator only; no native ceremony',before:'valid',disconnected:'HOST_AUTHORITY_NOT_LIVE',newHostOldAdmission:'HOST_AUTHORITY_NOT_LIVE',newHostFreshAdmission:'valid',daemonGeneration:'unchanged'}));
