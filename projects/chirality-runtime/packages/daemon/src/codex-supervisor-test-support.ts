import {
  CodexSupervisor,
  type ControlledHostedConformanceVerifier,
  type HostedCodexSupervisorAdmission,
  type HostedCodexSupervisorOptions,
} from "./codex-supervisor.js";

type ControlledAdmissionAccess = {
  admitHostedWithVerifier(
    options: HostedCodexSupervisorOptions,
    verifyConformance: ControlledHostedConformanceVerifier,
  ): Promise<HostedCodexSupervisorAdmission>;
};

/** Source-test-only friend access. This module is absent from every package export surface. */
export function admitHostedControlledForTests(
  options: HostedCodexSupervisorOptions,
  controlled: { verifyConformance: ControlledHostedConformanceVerifier },
): Promise<HostedCodexSupervisorAdmission> {
  if (!controlled || typeof controlled.verifyConformance !== "function") throw new Error("Controlled conformance verifier is unavailable");
  return (CodexSupervisor as unknown as ControlledAdmissionAccess).admitHostedWithVerifier(options, controlled.verifyConformance);
}
