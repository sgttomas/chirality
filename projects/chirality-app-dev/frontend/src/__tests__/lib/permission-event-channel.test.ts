import { afterEach, describe, expect, it } from 'vitest';
import type { HarnessEvent } from '../../lib/harness/event-schema';
import {
  PermissionEventChannelRegistry,
  SessionPermissionChannel,
  getPermissionEventChannel,
  resetPermissionEventChannelForTests
} from '../../lib/harness/permission-event-channel';

afterEach(() => {
  resetPermissionEventChannelForTests();
});

function evt(id: string): HarnessEvent {
  return {
    schemaVersion: 1,
    eventId: id,
    sessionId: 's1',
    timestamp: '2026-06-18T00:00:00.000Z',
    type: 'tool.permission',
    data: { behavior: 'ask', toolUseId: id }
  };
}

describe('SessionPermissionChannel', () => {
  it('delivers a published event to a waiter that is already parked', async () => {
    const channel = new SessionPermissionChannel();
    const pending = channel.next();
    channel.publish(evt('a'));
    await expect(pending).resolves.toEqual({ value: evt('a'), done: false });
  });

  it('buffers events published before they are consumed, preserving order', async () => {
    const channel = new SessionPermissionChannel();
    channel.publish(evt('a'));
    channel.publish(evt('b'));
    await expect(channel.next()).resolves.toMatchObject({ value: { eventId: 'a' }, done: false });
    expect(channel.drain().map((event) => event.eventId)).toEqual(['b']);
  });

  it('resolves a parked next() as done on close and ignores later publishes', async () => {
    const channel = new SessionPermissionChannel();
    const pending = channel.next();
    channel.close();
    await expect(pending).resolves.toEqual({ value: undefined, done: true });
    channel.publish(evt('a'));
    await expect(channel.next()).resolves.toEqual({ value: undefined, done: true });
  });
});

describe('PermissionEventChannelRegistry', () => {
  it('routes publishes only to the open session channel', async () => {
    const registry = new PermissionEventChannelRegistry();
    const channel = registry.open('s1');
    const pending = channel.next();

    registry.publish('other', evt('x')); // no channel — dropped
    registry.publish('s1', evt('a'));

    await expect(pending).resolves.toMatchObject({ value: { eventId: 'a' }, done: false });

    registry.close('s1');
    await expect(channel.next()).resolves.toEqual({ value: undefined, done: true });
  });

  it('exposes a resettable process-wide singleton', () => {
    const first = getPermissionEventChannel();
    expect(getPermissionEventChannel()).toBe(first);
    resetPermissionEventChannelForTests();
    expect(getPermissionEventChannel()).not.toBe(first);
  });
});
