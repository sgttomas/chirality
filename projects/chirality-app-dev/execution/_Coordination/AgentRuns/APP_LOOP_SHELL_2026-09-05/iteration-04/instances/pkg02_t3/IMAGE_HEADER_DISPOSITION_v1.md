# Image response header disposition v1
OwnerStandingApproval: D-APP-64 §3
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: remove the draft image-response CSP override and use the existing-policy path: image-only embedding, explicit attachment disposition and nosniff, with actual image/direct-download proof under unchanged Electron CSP.
JudgedBy: WORKING_ITEMS /root/pkg02
OwnerCaseSelection: NONE
RejectedAlternatives: the draft short CSP omitted explicit frame-ancestors and was not equivalent to existing policy; a newly constructed supposedly stricter policy would still override the owner boundary; asserting callback/header tests prove SVG browser isolation is false. No PDF/other frame permission is added.
RationaleArtifact: execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t3/IMAGE_HEADER_DISPOSITION_v1.md
IndependentVerifier: Initial source reviewer /root/pkg02/t3_review CHANGES_REQUESTED remains historical. Fresh whole-revised-diff review required, including actual final headers; parent governed refutation pending. No PASS implied.
EffectStatus: HELD
PreservedGates: D64 §5.1 classes1–10; unchanged renderer-window-policy/pins/proof expectations and all ancestry/nonce/default-source semantics; exact17-file fence; no new scope/security waiver/owner/release/Root/lifecycle/acceptance/merge act; APP-HOLD, full native/browser/source/global evidence and D108 PDF residual.

Actual history: during authorized completeness draft author added an image-only CSP intended to be restrictive. Manager independently caught the omission/override and raised it before source freeze. Parent selected removal; this correction is not an original unqualified PASS. Exact superseded draft is preserved in IMAGE_HEADER_SUPERSEDED_DRAFT_v1.json. This disposition precedes removal effects; no frozen source/review record is overwritten.

Author must remove the CSP header override, retain img-only display and attachment/nosniff binary response, and make metadata reasons truthful for supported images. Existing main/preload policies stay unchanged. Real browser proof must show script/external-resource-negative SVG safe in img and direct response downloaded rather than executed. If this path cannot prove a type safely, report that concrete residual; never invent a policy workaround. Fresh reviewer checks actual headers and all revised source.

Ontology: a file resource is not a new policy authority. Epistemology: exact draft header versus existing explicit denials revealed a real mismatch; unit assertions did not prove runtime safety. Praxeology: capture draft, remove unapproved override under frozen disposition, test actual constrained path, then full review and real browser/native proof. Axiology: retain usable images without quietly weakening or replacing a governed security boundary.
