export type RuntimeAdmissionUnavailableReason = "not-configured" | "unsupported-platform" | "lock-contended" | "inode-mismatch" | "unsafe-lock-file" | "native-adapter-unavailable";

export interface RuntimeAdmissionLease {
  readonly device: bigint;
  readonly inode: bigint;
  readonly held: boolean;
  readonly created: boolean;
  close(): void;
}

export interface RuntimeAdmissionNativeAdapter {
  acquire(directory: string, name: "runtime-admission-authority.lock"): RuntimeAdmissionLease;
}

export class RuntimeAdmissionUnavailable extends Error {
  readonly code = "AUTHORITY_UNAVAILABLE";
  constructor(readonly reason: RuntimeAdmissionUnavailableReason) { super(`Runtime admission authority unavailable: ${reason}`); }
}

/** Deterministic fake with the same opaque, nonduplicable lease surface; it makes no OS qualification claim. */
export function createFakeRuntimeAdmissionNativeAdapter(options: { device?: bigint; inode?: bigint; contended?: boolean; pathMatches?: boolean; created?: boolean } = {}): RuntimeAdmissionNativeAdapter {
  let outstanding = false;
  return { acquire() {
    if (options.contended || outstanding) throw new RuntimeAdmissionUnavailable("lock-contended");
    if (options.pathMatches === false) throw new RuntimeAdmissionUnavailable("inode-mismatch");
    outstanding = true;
    let held = true;
    return Object.freeze({ created: options.created ?? true, device: options.device ?? 1n, inode: options.inode ?? 1n, get held() { return held; }, close() {
      if (!held) throw new RuntimeAdmissionUnavailable("unsafe-lock-file");
      held = false; outstanding = false;
    } });
  } };
}
