import { configDefaults, defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    // Frozen execution evidence is not an executable test inventory.
    exclude: [...configDefaults.exclude, "execution/**"],
  },
});
