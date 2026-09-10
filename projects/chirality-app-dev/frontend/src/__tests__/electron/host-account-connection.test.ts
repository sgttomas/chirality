import { afterEach, describe, expect, it, vi } from 'vitest';
import type { HostAccountClient } from '@chirality/runtime-daemon/hosted';
import { createHostAccountConnection } from '../../../electron/host-account-connection';

function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((done) => { resolve = done; });
  return { promise, resolve };
}

function client() {
  return { close: vi.fn(async () => undefined) } as unknown as HostAccountClient;
}

afterEach(() => vi.useRealTimers());

describe('host account connection lifecycle', () => {
  it('publishes only a current connected client and replaces it after a daemon bounce', async () => {
    const first = client();
    const second = client();
    const connect = vi.fn().mockResolvedValueOnce(first).mockResolvedValueOnce(second);
    const connection = createHostAccountConnection({ connect, log: vi.fn() });
    await connection.update(true);
    expect(connection.client()).toBe(first);
    const disconnecting = connection.update(false);
    expect(connection.client()).toBeUndefined();
    await disconnecting;
    expect(first.close).toHaveBeenCalledOnce();
    expect(connection.client()).toBeUndefined();
    const reconnecting = connection.update(true);
    expect(connection.client()).toBeUndefined();
    await reconnecting;
    expect(connection.client()).toBe(second);
  });

  it('closes a stale in-flight client instead of publishing it after disconnect', async () => {
    const candidate = client();
    const started = deferred<HostAccountClient>();
    const entered = deferred<void>();
    const connection = createHostAccountConnection({ connect: () => { entered.resolve(); return started.promise; }, log: vi.fn() });
    const connecting = connection.update(true);
    await entered.promise;
    const disconnected = connection.update(false);
    started.resolve(candidate);
    await Promise.all([connecting, disconnected]);
    expect(candidate.close).toHaveBeenCalledOnce();
    expect(connection.client()).toBeUndefined();
  });

  it('unpublishes a failed current client before replacing it', async () => {
    const first = client();
    const second = client();
    const connect = vi.fn().mockResolvedValueOnce(first).mockResolvedValueOnce(second);
    const connection = createHostAccountConnection({ connect, log: vi.fn() });
    await connection.update(true);
    const replacing = connection.invalidate(first);
    expect(connection.client()).toBeUndefined();
    await replacing;
    expect(first.close).toHaveBeenCalledOnce();
    expect(connection.client()).toBe(second);
    await connection.invalidate(first);
    expect(connection.client()).toBe(second);
  });

  it('awaits an in-flight start and closes its client during final teardown', async () => {
    const candidate = client();
    const started = deferred<HostAccountClient>();
    const entered = deferred<void>();
    const connection = createHostAccountConnection({ connect: () => { entered.resolve(); return started.promise; }, log: vi.fn() });
    void connection.update(true);
    await entered.promise;
    const closing = connection.close();
    started.resolve(candidate);
    await closing;
    expect(candidate.close).toHaveBeenCalledOnce();
    expect(connection.client()).toBeUndefined();
  });

  it('retries a transient start failure while the same daemon connection remains current', async () => {
    vi.useFakeTimers();
    const candidate = client();
    const connect = vi.fn()
      .mockRejectedValueOnce(new Error('temporarily unavailable'))
      .mockResolvedValueOnce(candidate);
    const connection = createHostAccountConnection({ connect, log: vi.fn() });
    await connection.update(true);
    expect(connection.client()).toBeUndefined();
    expect(connect).toHaveBeenCalledOnce();
    await vi.advanceTimersByTimeAsync(250);
    expect(connect).toHaveBeenCalledTimes(2);
    expect(connection.client()).toBe(candidate);
    await connection.close();
  });

  it('cancels a pending retry when the daemon disconnects', async () => {
    vi.useFakeTimers();
    const connect = vi.fn().mockRejectedValue(new Error('temporarily unavailable'));
    const connection = createHostAccountConnection({ connect, log: vi.fn() });
    await connection.update(true);
    await connection.update(false);
    await vi.advanceTimersByTimeAsync(10_000);
    expect(connect).toHaveBeenCalledOnce();
    expect(connection.client()).toBeUndefined();
    await connection.close();
  });
});
