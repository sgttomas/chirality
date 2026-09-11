import type { HostAccountClient } from '@chirality/runtime-daemon/hosted';

export type HostAccountConnection = {
  update(runtimeConnected: boolean): Promise<void>;
  client(): HostAccountClient | undefined;
  invalidate(client: HostAccountClient): Promise<void>;
  close(): Promise<void>;
};

export function createHostAccountConnection(options: {
  connect(): Promise<HostAccountClient>;
  log(event: 'connected' | 'unavailable' | 'closed'): void;
}): HostAccountConnection {
  const retryDelaysMs = [250, 1_000, 5_000] as const;
  let generation = 0;
  let active: HostAccountClient | undefined;
  let selectedConnected = false;
  let closed = false;
  let pending = Promise.resolve();
  let retryTimer: ReturnType<typeof setTimeout> | undefined;

  const retire = async (client: HostAccountClient | undefined): Promise<void> => {
    if (client) await client.close().catch(() => undefined);
  };

  const clearRetry = (): void => {
    if (retryTimer !== undefined) clearTimeout(retryTimer);
    retryTimer = undefined;
  };

  const scheduleConnect = (selectedGeneration: number, retryIndex: number): void => {
    if (closed || selectedGeneration !== generation) return;
    const delay = retryDelaysMs[Math.min(retryIndex, retryDelaysMs.length - 1)]!;
    retryTimer = setTimeout(() => {
      retryTimer = undefined;
      pending = pending.then(() => connect(selectedGeneration, retryIndex + 1));
      void pending;
    }, delay);
  };

  const connect = async (selectedGeneration: number, retryIndex: number): Promise<void> => {
    if (closed || selectedGeneration !== generation) return;
    try {
      const candidate = await options.connect();
      if (closed || selectedGeneration !== generation) {
        await candidate.close().catch(() => undefined);
        return;
      }
      active = candidate;
      options.log('connected');
    } catch {
      if (!closed && selectedGeneration === generation) {
        options.log('unavailable');
        scheduleConnect(selectedGeneration, retryIndex);
      }
    }
  };

  const update = (runtimeConnected: boolean): Promise<void> => {
    // Daemon reachability is sampled independently of the desktop project's
    // binding state. Repeated healthy samples must not tear down and recreate
    // an already usable account client.
    if (selectedConnected === runtimeConnected) return pending;
    selectedConnected = runtimeConnected;
    const selectedGeneration = ++generation;
    clearRetry();
    // Revoke publication synchronously. Closing may have to wait behind an
    // in-flight connection, but IPC must never observe the old client once a
    // disconnect or replacement transition has begun.
    const retired = active;
    active = undefined;
    pending = pending.then(async () => {
      await retire(retired);
      if (closed || !runtimeConnected || selectedGeneration !== generation) return;
      await connect(selectedGeneration, 0);
    });
    return pending;
  };

  return {
    update,
    client: () => active,
    invalidate(client: HostAccountClient): Promise<void> {
      if (closed || active !== client) return pending;
      const selectedGeneration = ++generation;
      clearRetry();
      active = undefined;
      pending = pending.then(async () => {
        await retire(client);
        if (!closed && selectedConnected && selectedGeneration === generation) {
          await connect(selectedGeneration, 0);
        }
      });
      return pending;
    },
    async close(): Promise<void> {
      if (closed) return pending;
      closed = true;
      selectedConnected = false;
      generation += 1;
      clearRetry();
      const retired = active;
      active = undefined;
      pending = pending.then(() => retire(retired));
      await pending;
      options.log('closed');
    }
  };
}
