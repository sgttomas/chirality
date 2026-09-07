import { defineConfig } from "vitest/config";
export default defineConfig({
  root: "/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime",
  plugins: [],
  test: { setupFiles: [], globalSetup: [], include: ["tests/supervisor.test.ts"] },
});
