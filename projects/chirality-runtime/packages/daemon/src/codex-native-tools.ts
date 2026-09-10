import { createHash } from "node:crypto";
import type { RuntimeToolCallbackDeclaration } from "@chirality/runtime-contracts";

export const CODEX_NATIVE_TOOLS_SCHEMA = "chirality-native-tools/v1" as const;

const fail = (): never => { throw new Error("Invalid inherited native tool definitions"); };
const scalar = (value: string): string => {
  for (let index = 0; index < value.length; index++) {
    const code = value.charCodeAt(index);
    if (code >= 0xd800 && code <= 0xdbff) {
      const next = value.charCodeAt(++index);
      if (!Number.isFinite(next) || next < 0xdc00 || next > 0xdfff) fail();
    } else if (code >= 0xdc00 && code <= 0xdfff) fail();
  }
  return value;
};
const utf8 = (value: string): Buffer => Buffer.from(scalar(value), "utf8");
const length = (value: number): Buffer => Buffer.from(String(value), "ascii");

function encode(value: unknown, depth = 0): Buffer {
  if (depth > 64) fail();
  if (value === null) return Buffer.from("n");
  if (value === false) return Buffer.from("f");
  if (value === true) return Buffer.from("t");
  if (typeof value === "number") {
    if (!Number.isSafeInteger(value)) fail();
    return Buffer.from(`i${Object.is(value, -0) ? "0" : String(value)};`, "ascii");
  }
  if (typeof value === "string") {
    const bytes = utf8(value);
    return Buffer.concat([Buffer.from("s"), length(bytes.length), Buffer.from(":"), bytes]);
  }
  if (Array.isArray(value)) {
    return Buffer.concat([Buffer.from("a"), length(value.length), Buffer.from(":"), ...value.map(item => encode(item, depth + 1))]);
  }
  if (!value || typeof value !== "object" || Object.getPrototypeOf(value) !== Object.prototype) fail();
  const entries = Object.entries(value as Record<string, unknown>).map(([key, item]) => ({ key, bytes: utf8(key), item }));
  entries.sort((left, right) => Buffer.compare(left.bytes, right.bytes));
  return Buffer.concat([Buffer.from("o"), length(entries.length), Buffer.from(":"), ...entries.flatMap(({ key, item }) => [encode(key, depth + 1), encode(item, depth + 1)])]);
}

function inspectDefinition(value: RuntimeToolCallbackDeclaration): void {
  if (!value || Object.keys(value).sort().join(",") !== "description,inputSchema,name"
    || !/^[A-Za-z][A-Za-z0-9_-]{0,63}$/.test(value.name)
    || typeof value.description !== "string" || !value.description.trim()
    || Buffer.byteLength(value.description, "utf8") > 4096
    || !value.inputSchema || typeof value.inputSchema !== "object" || Array.isArray(value.inputSchema)) fail();
  scalar(value.name); scalar(value.description);
  if (Buffer.byteLength(JSON.stringify(value.inputSchema), "utf8") > 16384) fail();
  inspectSchema(value.inputSchema);
  encode(value.inputSchema);
}

const SCHEMA_KEYS = new Set(["type", "properties", "required", "additionalProperties", "items", "maxItems", "minItems", "maxLength", "minLength", "minimum", "maximum", "enum", "description", "title"]);
function inspectSchema(schema: Readonly<Record<string, unknown>>, depth = 0): void {
  if (depth > 8 || !schema || typeof schema !== "object" || Array.isArray(schema) || Object.getPrototypeOf(schema) !== Object.prototype
    || Object.keys(schema).some(key => !SCHEMA_KEYS.has(scalar(key)))) fail();
  if (!["object", "array", "string", "number", "integer", "boolean", "null"].includes(String(schema.type))) fail();
  if (schema.description !== undefined && typeof schema.description !== "string" || schema.title !== undefined && typeof schema.title !== "string") fail();
  if (typeof schema.description === "string") scalar(schema.description);
  if (typeof schema.title === "string") scalar(schema.title);
  if (schema.enum !== undefined) {
    if (!Array.isArray(schema.enum) || schema.enum.length > 64) fail();
    const values = schema.enum as readonly unknown[];
    for (const value of values) {
      if (value !== null && !["string", "number", "boolean"].includes(typeof value)) fail();
      if (typeof value === "string") scalar(value);
      if (typeof value === "number" && !Number.isSafeInteger(value)) fail();
    }
  }
  for (const key of ["maxItems", "minItems", "maxLength", "minLength", "minimum", "maximum"]) if (schema[key] !== undefined && !Number.isSafeInteger(schema[key])) fail();
  if (schema.type === "object") {
    const properties = schema.properties ?? {};
    if (schema.additionalProperties !== false || !properties || typeof properties !== "object" || Array.isArray(properties) || Object.getPrototypeOf(properties) !== Object.prototype || Object.keys(properties).length > 64) fail();
    for (const [key, child] of Object.entries(properties)) { scalar(key); inspectSchema(child as Record<string, unknown>, depth + 1); }
    if (schema.required !== undefined && (!Array.isArray(schema.required) || schema.required.some(key => typeof key !== "string" || !Object.hasOwn(properties, key) || (scalar(key), false)))) fail();
  } else if (schema.type === "array") inspectSchema(schema.items as Record<string, unknown>, depth + 1);
}

export function encodeCodexNativeToolDefinitionsV1(definitions: readonly RuntimeToolCallbackDeclaration[]): Buffer {
  if (!Array.isArray(definitions) || definitions.length > 32) fail();
  definitions.forEach(inspectDefinition);
  const ordered = definitions.map(value => structuredClone(value));
  ordered.sort((left, right) => Buffer.compare(utf8(left.name), utf8(right.name)));
  if (ordered.some((value, index) => index > 0 && value.name === ordered[index - 1]!.name)) fail();
  return Buffer.concat([Buffer.from(`${CODEX_NATIVE_TOOLS_SCHEMA}\0`, "ascii"), encode(ordered)]);
}

export function digestCodexNativeToolDefinitionsV1(definitions: readonly RuntimeToolCallbackDeclaration[]): string {
  return createHash("sha256").update(encodeCodexNativeToolDefinitionsV1(definitions)).digest("hex");
}
