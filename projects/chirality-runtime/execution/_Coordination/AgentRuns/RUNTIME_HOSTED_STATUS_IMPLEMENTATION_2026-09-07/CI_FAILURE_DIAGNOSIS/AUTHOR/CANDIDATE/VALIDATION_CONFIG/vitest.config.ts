import { fileURLToPath } from "node:url";
import { defineConfig } from "vitest/config";

export default defineConfig({
  root: fileURLToPath(new URL("../../../../../../../../", import.meta.url)),
  plugins: [],
  test: {
    setupFiles: [], globalSetup: [],
    include: ["tests/codex-manager.test.ts", "tests/delegated-runtime.test.ts", "tests/manager-approval-integration.test.ts"],
  },
});
