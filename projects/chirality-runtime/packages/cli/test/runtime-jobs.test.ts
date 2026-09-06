import { describe, expect, it } from "vitest";
import { renderRuntimeJobs, type RuntimeJobsInput } from "../src/runtime-jobs.js";
function input(): RuntimeJobsInput {
  return { privateDirectory: "/private/runtime", daemon: { label: "test.runtime.daemon", executablePath: "/trusted/daemon", args: ["/trusted/daemon-config.json"], socketPath: "/private/runtime/daemon.sock" }, supervisor: { label: "test.runtime.supervisor", executablePath: "/trusted/supervisor", args: ["/trusted/supervisor-config.json"], socketPath: "/private/runtime/supervisor.sock" } };
}
describe("render-only two-job topology", () => {
  it("renders distinct exact trusted commands with private requirements and no fabricated switches", () => {
    const plan = renderRuntimeJobs(input());
    expect(plan.daemon.programArguments).toEqual(["/trusted/daemon", "/trusted/daemon-config.json"]);
    expect(plan.supervisor.programArguments).toEqual(["/trusted/supervisor", "/trusted/supervisor-config.json"]);
    expect(plan.supervisor.plist).not.toContain("--runtime-daemon");
    expect(plan.daemon.label).not.toBe(plan.supervisor.label);
    expect(plan.mode).toBe("render-only"); expect(plan.transport).toBe("unix"); expect(plan.supervisorExposure).toBe("daemon-only");
    expect(plan.requirements).toEqual({ directoryMode: 0o700, socketMode: 0o600, credentialExchange: "runtime-only" });
    expect(plan.supervisor.plist).toContain("<key>Umask</key><integer>63</integer>");
    expect(plan.supervisor.plist).not.toContain("EnvironmentVariables");
  });
  it("escapes XML in exact argument and executable strings", () => {
    const config = input(); config.supervisor.executablePath = "/trusted/a&b<runner>"; config.supervisor.args = ['a<&"\'>'];
    const plan = renderRuntimeJobs(config); expect(plan.supervisor.plist).toContain("/trusted/a&amp;b&lt;runner&gt;"); expect(plan.supervisor.plist).toContain("a&lt;&amp;&quot;&apos;&gt;");
    expect(plan.supervisor.programArguments[1]).toBe('a<&"\'>');
  });
  it("rejects colliding labels and sockets", () => {
    const labels = input(); labels.supervisor.label = labels.daemon.label; expect(() => renderRuntimeJobs(labels)).toThrow("distinct");
    const sockets = input(); sockets.supervisor.socketPath = sockets.daemon.socketPath; expect(() => renderRuntimeJobs(sockets)).toThrow("distinct");
  });
  it("rejects relative, escaping and noncanonical paths", () => {
    for (const path of ["relative.sock", "/public/socket", "/private/runtime/../socket"]) { const config = input(); config.supervisor.socketPath = path; expect(() => renderRuntimeJobs(config)).toThrow(); }
    const config = input(); config.daemon.executablePath = "node"; expect(() => renderRuntimeJobs(config)).toThrow("absolute");
  });
  it("rejects credential material and public exposure configuration", () => {
    for (const args of [["--token", "test-secret"], ["--port=9000"], ["--listen", "0.0.0.0"], ["tcp://localhost:9000"]]) { const config = input(); config.supervisor.args = args; expect(() => renderRuntimeJobs(config)).toThrow("forbidden"); }
    expect(() => renderRuntimeJobs({ ...input(), token: "secret" } as RuntimeJobsInput)).toThrow("forbidden");
    expect(() => renderRuntimeJobs({ ...input(), supervisorExposure: "public" } as RuntimeJobsInput)).toThrow("forbidden");
  });
});
