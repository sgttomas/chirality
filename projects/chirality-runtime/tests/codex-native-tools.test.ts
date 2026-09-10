import { describe, expect, it } from "vitest";
import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { digestCodexNativeToolDefinitionsV1, encodeCodexNativeToolDefinitionsV1 } from "../packages/daemon/src/codex-native-tools.js";
import { compileCodexNativePolicyStageC } from "../packages/daemon/src/codex-containment.js";

const definitions = [
  { name: "chirality_load_method", description: "Load | method: 🧬", inputSchema: { required: ["qualifiedId"], properties: { qualifiedId: { type: "string", enum: ["a:b", "Ω"] } }, additionalProperties: false, type: "object" } },
  { name: "chirality_list_methods", description: "List methods", inputSchema: { additionalProperties: false, type: "object" } }
];

type FixtureRecipe = {
  kind: "replace-value" | "generate-indexed-object" | "generate-integer-range" | "nest-array-schema" | "repeat-ascii-string";
  input: unknown;
  path: (string | number)[];
  value?: { semantic: "negative-zero" } | { semantic: "nonfinite-number"; token: "NaN" | "+Infinity" | "-Infinity" }
    | { semantic: "unpaired-utf16-code-unit"; codeUnit: number }
    | { semantic: "non-plain-object"; prototype: "Date"; epochMilliseconds: number };
  count?: number;
  keyPrefix?: string;
  item?: unknown;
  start?: number;
  depth?: number;
  leaf?: unknown;
  byte?: string;
  byteLength?: number;
};

function replaceAtPath(input: unknown, path: readonly (string | number)[], value: unknown): unknown {
  const cloned = structuredClone(input);
  let target = cloned as Record<string | number, unknown>;
  for (const part of path.slice(0, -1)) target = target[part] as Record<string | number, unknown>;
  target[path.at(-1)!] = value;
  return cloned;
}

function materializeRecipe(recipe: FixtureRecipe): unknown {
  if (recipe.kind === "replace-value") {
    let value: unknown;
    if (recipe.value?.semantic === "negative-zero") value = -0;
    else if (recipe.value?.semantic === "nonfinite-number") value = recipe.value.token === "NaN" ? NaN : recipe.value.token === "+Infinity" ? Infinity : -Infinity;
    else if (recipe.value?.semantic === "unpaired-utf16-code-unit") value = String.fromCharCode(recipe.value.codeUnit);
    else if (recipe.value?.semantic === "non-plain-object") value = new Date(recipe.value.epochMilliseconds);
    else throw new Error("Unknown fixture replacement semantic");
    return replaceAtPath(recipe.input, recipe.path, value);
  }
  if (recipe.kind === "generate-indexed-object") {
    const generated = Object.fromEntries(Array.from({ length: recipe.count! }, (_, index) => [`${recipe.keyPrefix}${index}`, structuredClone(recipe.item)]));
    return replaceAtPath(recipe.input, recipe.path, generated);
  }
  if (recipe.kind === "generate-integer-range") {
    const generated = Array.from({ length: recipe.count! }, (_, index) => recipe.start! + index);
    return replaceAtPath(recipe.input, recipe.path, generated);
  }
  if (recipe.kind === "nest-array-schema") {
    let generated = structuredClone(recipe.leaf);
    for (let index = 0; index < recipe.depth!; index++) generated = { type: "array", items: generated };
    return replaceAtPath(recipe.input, recipe.path, generated);
  }
  if (recipe.kind === "repeat-ascii-string") return replaceAtPath(recipe.input, recipe.path, recipe.byte!.repeat(recipe.byteLength!));
  throw new Error("Unknown fixture recipe");
}

const materialize = (vector: { input?: unknown; inputEncoding?: FixtureRecipe }): unknown =>
  vector.inputEncoding === undefined ? structuredClone(vector.input) : materializeRecipe(vector.inputEncoding);

describe("Codex native inherited-tool encoder v1", () => {
  it("matches the checked-in golden and ignores tool/object insertion order", async () => {
    const golden = JSON.parse(await readFile(fileURLToPath(new URL("./fixtures/codex-native-tools-v1.json", import.meta.url)), "utf8"));
    const goldenInput = golden.input as Parameters<typeof encodeCodexNativeToolDefinitionsV1>[0];
    const reordered = [definitions[1]!, { ...definitions[0]!, inputSchema: { type: "object", additionalProperties: false, properties: { qualifiedId: { enum: ["a:b", "Ω"], type: "string" } }, required: ["qualifiedId"] } }];
    expect(encodeCodexNativeToolDefinitionsV1(goldenInput).toString("hex")).toBe(golden.encodedHex);
    expect(digestCodexNativeToolDefinitionsV1(goldenInput)).toBe(golden.sha256);
    expect(encodeCodexNativeToolDefinitionsV1(definitions).toString("hex")).toBe(golden.encodedHex);
    expect(digestCodexNativeToolDefinitionsV1(reordered)).toBe(golden.sha256);
    for (const vector of golden.vectors) {
      const input = materialize(vector) as Parameters<typeof encodeCodexNativeToolDefinitionsV1>[0];
      expect(encodeCodexNativeToolDefinitionsV1(input).toString("hex"), vector.name).toBe(vector.encodedHex);
      expect(digestCodexNativeToolDefinitionsV1(input), vector.name).toBe(vector.sha256);
    }
    for (const vector of golden.rejections) {
      expect(vector.expected, vector.name).toBe("reject");
      const input = materialize(vector) as Parameters<typeof encodeCodexNativeToolDefinitionsV1>[0];
      expect(() => encodeCodexNativeToolDefinitionsV1(input), vector.name).toThrow("Invalid inherited native tool definitions");
    }
  });
  it("covers empty, delimiter, Unicode, negative zero and safe integer values", () => {
    expect(encodeCodexNativeToolDefinitionsV1([]).subarray(0, 26).toString()).toBe("chirality-native-tools/v1\0");
    const values = [{ name: "x", description: ":;|", inputSchema: { type: "object", additionalProperties: false, enum: [-0, Number.MAX_SAFE_INTEGER], title: "🧬" } }];
    expect(encodeCodexNativeToolDefinitionsV1(values).toString()).toContain("i0;");
  });
  it.each([NaN, 1.5, Number.MAX_SAFE_INTEGER + 1])("rejects unsupported schema number %s", value => {
    expect(() => encodeCodexNativeToolDefinitionsV1([{ name: "x", description: "x", inputSchema: { value } }])).toThrow();
  });
  it("rejects unpaired surrogates, duplicate names, excessive depth and non-plain values", () => {
    expect(() => encodeCodexNativeToolDefinitionsV1([{ name: "x", description: String.fromCharCode(0xd800), inputSchema: {} }])).toThrow();
    expect(() => encodeCodexNativeToolDefinitionsV1([{ name: "x", description: "a", inputSchema: {} }, { name: "x", description: "b", inputSchema: {} }])).toThrow();
    let value: unknown = 0; for (let i = 0; i < 10; i++) value = [value];
    expect(() => encodeCodexNativeToolDefinitionsV1([{ name: "x", description: "x", inputSchema: { value } }])).toThrow();
    expect(() => encodeCodexNativeToolDefinitionsV1([{ name: "x", description: "x", inputSchema: new Date() as unknown as Record<string, unknown> }])).toThrow();
  });
  it("binds native-11 to the immutable selector, readback and full definitions without changing native-10", () => {
    const native10 = Object.freeze({ policyDigest: "a".repeat(64), permissionProfile: "chirality_aaaaaaaaaaaaaaaaaaaaaaaa",
      configOverrides: Object.freeze(["approval_policy=\"never\"", "permissions={\"chirality_aaaaaaaaaaaaaaaaaaaaaaaa\"={}}"]),
      args: Object.freeze([]), configToml: "", policyInstance: {} as never, policyInstanceDigest: "b".repeat(64), expectedPermissions: { filesystem: {}, network: { enabled: false } } });
    const compiled = compileCodexNativePolicyStageC(native10 as never, definitions);
    expect(native10.policyDigest).toBe("a".repeat(64));
    expect(compiled.compilerIdentity).toMatchObject({ version: 11, nativeSkills: "disabled", effectiveReadback: { nativeSkills: "disabled" } });
    expect(compiled.appServerArguments.slice(0, 2)).toEqual(["app-server", "--chirality-disable-native-skills"]);
    expect(compiled.configOverrides.join("\n")).toContain(compiled.permissionProfile);
    expect(compiled.compilerIdentity.inheritedToolsSchema).toBe("chirality-native-tools/v1");
  });
});
