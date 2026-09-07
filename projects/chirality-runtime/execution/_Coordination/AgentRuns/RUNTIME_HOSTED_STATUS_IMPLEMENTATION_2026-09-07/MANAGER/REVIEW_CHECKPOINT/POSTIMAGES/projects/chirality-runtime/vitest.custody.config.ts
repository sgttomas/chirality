import { fileURLToPath } from "node:url";
import { defineConfig } from "vitest/config";

// Only the four owner-approved invocations may select tests from this inventory.
export default defineConfig({
  root: fileURLToPath(new URL(".", import.meta.url)),
  plugins: [],
  test: {
    setupFiles: [], globalSetup: [],
    include: [
      "tests/custody-config-status.test.ts", "tests/codex-login.test.ts",
      "tests/codex-session.test.ts", "tests/codex-supervisor.test.ts",
      "tests/standalone.test.ts", "tests/hosted-consent.test.ts",
      "tests/runtime-conformance.test.ts",
    ],
  },
});
