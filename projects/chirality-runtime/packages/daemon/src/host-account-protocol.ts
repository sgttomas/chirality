import { createHash, createHmac, timingSafeEqual } from "node:crypto";
import { readFile } from "node:fs/promises";
import { isAbsolute, join, resolve } from "node:path";
import { RuntimeError } from "@chirality/runtime-contracts";

export const HOST_ACCOUNT_SERVICE_NAME = "com.chirality.app.runtime.account-host" as const;
export const HOST_ACCOUNT_SIGNING_PREDICATE_RESOURCE = "runtime-contracts/host-account-signing-predicate.json" as const;
export const HOST_ACCOUNT_SCOPES = ["account:read", "account:control"] as const;
export const HOST_ACCOUNT_CHALLENGE_BYTES = 32;
export const HOST_ACCOUNT_NONCE_BYTES = 32;
export const HOST_ACCOUNT_CEREMONY_TIMEOUT_MS = 10_000;
export const HOST_ACCOUNT_PING_INTERVAL_MS = 5_000;
export const HOST_ACCOUNT_MAX_MISSED_PINGS = 3;
export const HOST_ACCOUNT_SILENCE_TIMEOUT_MS = 15_000;

export type HostAccountScope = (typeof HOST_ACCOUNT_SCOPES)[number];
export type HostAccountOperation =
  | "status"
  | "grant-provider-network-consent"
  | "start-login"
  | "cancel-login"
  | "sign-out";

export interface HostAccountSigningPredicate {
  schema: "chirality.host-account-signing-predicate/v1";
  serviceName: typeof HOST_ACCOUNT_SERVICE_NAME;
  bundleId: "com.chirality.app";
  teamId: string;
  peerRequirement: string;
}

export interface HostAccountRequestDescriptor {
  method: "GET" | "POST";
  route: string;
  requiredScope: HostAccountScope;
  canonicalBody: string;
}

export interface HostAccountProofHeaders {
  authorization: string;
  "content-type"?: "application/json";
  "x-chirality-account-counter": string;
  "x-chirality-account-generation": string;
  "x-chirality-account-proof": string;
}

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/u;
const BASE64URL_32 = /^[A-Za-z0-9_-]{43}$/u;
const ACCOUNT_ROUTE = /^\/v3\/projects\/[A-Za-z0-9](?:[A-Za-z0-9._-]|%3A){0,383}\/hosted-bootstrap\/(?:status|provider-network-consent|login\/(?:start|cancel)|logout)$/u;

function exactRecord(value: unknown, keys: readonly string[]): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value)
    && Object.keys(value).length === keys.length
    && Object.keys(value).every((key) => keys.includes(key));
}

export function parseHostAccountSigningPredicate(value: unknown): HostAccountSigningPredicate {
  const keys = ["bundleId", "peerRequirement", "schema", "serviceName", "teamId"];
  if (!exactRecord(value, keys)
    || value.schema !== "chirality.host-account-signing-predicate/v1"
    || value.serviceName !== HOST_ACCOUNT_SERVICE_NAME
    || value.bundleId !== "com.chirality.app"
    || typeof value.teamId !== "string"
    || !/^[A-Z0-9]{10}$/u.test(value.teamId)
    || typeof value.peerRequirement !== "string"
    || value.peerRequirement.length < 1
    || value.peerRequirement.length > 4096
    || /^\s*designated\s*=>/u.test(value.peerRequirement)
    || /[\u0000\r\n]/u.test(value.peerRequirement)) {
    throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account signing predicate is unavailable", 503);
  }
  return Object.freeze({
    schema: value.schema,
    serviceName: value.serviceName,
    bundleId: value.bundleId,
    teamId: value.teamId,
    peerRequirement: value.peerRequirement
  });
}

export async function loadHostAccountSigningPredicate(resourcesPath: string): Promise<HostAccountSigningPredicate> {
  if (!isAbsolute(resourcesPath) || resolve(resourcesPath) !== resourcesPath) {
    throw new RuntimeError("ENGINE_UNAVAILABLE", "Packaged Runtime resources path is unavailable", 503);
  }
  const source = await readFile(join(resourcesPath, HOST_ACCOUNT_SIGNING_PREDICATE_RESOURCE), "utf8")
    .catch(() => { throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account signing predicate is unavailable", 503); });
  if (Buffer.byteLength(source, "utf8") > 8192) throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account signing predicate is unavailable", 503);
  try { return parseHostAccountSigningPredicate(JSON.parse(source)); }
  catch { throw new RuntimeError("ENGINE_UNAVAILABLE", "Host account signing predicate is unavailable", 503); }
}

function canonicalValue(value: unknown): string {
  if (value === null) return "null";
  if (typeof value === "boolean" || typeof value === "string") return JSON.stringify(value);
  if (typeof value === "number" && Number.isFinite(value)) return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(canonicalValue).join(",")}]`;
  if (typeof value === "object") {
    const record = value as Record<string, unknown>;
    return `{${Object.keys(record).sort().map((key) => `${JSON.stringify(key)}:${canonicalValue(record[key])}`).join(",")}}`;
  }
  throw new RuntimeError("INVALID_REQUEST", "Account request body is not canonical JSON");
}

function canonicalHostAccountBody(value: unknown): string {
  return canonicalValue(value);
}

export function hostAccountRequest(
  operation: HostAccountOperation,
  projectId: string
): HostAccountRequestDescriptor {
  if (!/^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/u.test(projectId)) {
    throw new RuntimeError("INVALID_REQUEST", "Invalid hosted project identity");
  }
  const root = `/v3/projects/${encodeURIComponent(projectId)}/hosted-bootstrap`;
  switch (operation) {
    case "status": return { method: "GET", route: `${root}/status`, requiredScope: "account:read", canonicalBody: "" };
    case "grant-provider-network-consent": return { method: "POST", route: `${root}/provider-network-consent`, requiredScope: "account:control", canonicalBody: canonicalHostAccountBody({ consent: true }) };
    case "start-login": return { method: "POST", route: `${root}/login/start`, requiredScope: "account:control", canonicalBody: canonicalHostAccountBody({}) };
    case "cancel-login": return { method: "POST", route: `${root}/login/cancel`, requiredScope: "account:control", canonicalBody: canonicalHostAccountBody({}) };
    case "sign-out": return { method: "POST", route: `${root}/logout`, requiredScope: "account:control", canonicalBody: canonicalHostAccountBody({}) };
  }
}

export function hostAccountBodyDigest(canonicalBody: string): string {
  return createHash("sha256").update(canonicalBody, "utf8").digest("hex");
}

export function hostAccountCeremonyMessage(challenge: Buffer, generation: string): Buffer {
  if (challenge.length !== HOST_ACCOUNT_CHALLENGE_BYTES || !UUID.test(generation)) {
    throw new RuntimeError("ENGINE_UNAVAILABLE", "Invalid host account ceremony state", 503);
  }
  return Buffer.concat([challenge, Buffer.from(generation, "ascii")]);
}

export function createHostAccountCeremonyProof(hostNonce: Buffer, challenge: Buffer, generation: string): Buffer {
  if (hostNonce.length !== HOST_ACCOUNT_NONCE_BYTES) throw new RuntimeError("UNAUTHORIZED", "Invalid host account nonce", 401);
  return createHmac("sha256", hostNonce).update(hostAccountCeremonyMessage(challenge, generation)).digest();
}

export function hostAccountRequestProofMessage(input: {
  method: string;
  route: string;
  canonicalBodyDigest: string;
  counter: number;
  generation: string;
}): string {
  if (!/^(?:GET|POST)$/u.test(input.method) || !ACCOUNT_ROUTE.test(input.route) || !/^[a-f0-9]{64}$/u.test(input.canonicalBodyDigest)
    || !Number.isSafeInteger(input.counter) || input.counter < 1 || !UUID.test(input.generation)) {
    throw new RuntimeError("UNAUTHORIZED", "Invalid host account request proof fields", 401);
  }
  return JSON.stringify([input.method, input.route, input.canonicalBodyDigest, input.counter, input.generation]);
}

export function createHostAccountRequestProof(hostNonce: Buffer, input: Parameters<typeof hostAccountRequestProofMessage>[0]): string {
  if (hostNonce.length !== HOST_ACCOUNT_NONCE_BYTES) throw new RuntimeError("UNAUTHORIZED", "Invalid host account nonce", 401);
  return createHmac("sha256", hostNonce).update(hostAccountRequestProofMessage(input), "utf8").digest("base64url");
}

export function verifyHostAccountProof(expected: string, supplied: string): boolean {
  if (!BASE64URL_32.test(expected) || !BASE64URL_32.test(supplied)) return false;
  return timingSafeEqual(Buffer.from(expected, "base64url"), Buffer.from(supplied, "base64url"));
}

export function validHostAccountGeneration(value: string): boolean { return UUID.test(value); }
