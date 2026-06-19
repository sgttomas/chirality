'use client';

import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
  type ReactNode
} from 'react';
import type { HarnessEvent } from '../../lib/harness/event-schema';

/**
 * Holds the live, bridged `harness:event` stream for the active turn so that
 * the producer (the chat panel / live loop) and the consumers (the Tools and
 * Subagents sidebar views) share one source of truth. The chat panel appends
 * rich events as they arrive and clears them when a new turn starts.
 *
 * The stream is exposed through two separate contexts: a *data* context (the
 * events array, which changes on every append) and an *actions* context
 * (append/clear, whose identity is stable). The producer subscribes only to the
 * stable actions context, so appending an event does not re-render the heavy
 * chat transcript; only the data consumers (the stream views) re-render.
 */
type HarnessEventActions = {
  appendEvent: (event: HarnessEvent) => void;
  clearEvents: () => void;
};

const HarnessEventsDataContext = createContext<HarnessEvent[] | null>(null);
const HarnessEventActionsContext = createContext<HarnessEventActions | null>(null);

/** Bound the buffer so a long-running, tool-heavy turn cannot grow without limit. */
export const MAX_LIVE_HARNESS_EVENTS = 2000;

export function HarnessEventsProvider({ children }: { children: ReactNode }): JSX.Element {
  const [events, setEvents] = useState<HarnessEvent[]>([]);

  const appendEvent = useCallback((event: HarnessEvent) => {
    setEvents((existing) => {
      const next = [...existing, event];
      if (next.length > MAX_LIVE_HARNESS_EVENTS) {
        return next.slice(next.length - MAX_LIVE_HARNESS_EVENTS);
      }
      return next;
    });
  }, []);

  const clearEvents = useCallback(() => {
    setEvents([]);
  }, []);

  const actions = useMemo<HarnessEventActions>(
    () => ({ appendEvent, clearEvents }),
    [appendEvent, clearEvents]
  );

  return (
    <HarnessEventActionsContext.Provider value={actions}>
      <HarnessEventsDataContext.Provider value={events}>
        {children}
      </HarnessEventsDataContext.Provider>
    </HarnessEventActionsContext.Provider>
  );
}

/** Data hook for consumers that render the stream (Tools / Subagents views). */
export function useHarnessEvents(): { events: HarnessEvent[] } {
  const events = useContext(HarnessEventsDataContext);
  if (events === null) {
    throw new Error('useHarnessEvents must be used inside HarnessEventsProvider');
  }
  return { events };
}

/** Actions hook for the producer (the chat panel); stable across event appends. */
export function useHarnessEventActions(): HarnessEventActions {
  const actions = useContext(HarnessEventActionsContext);
  if (!actions) {
    throw new Error('useHarnessEventActions must be used inside HarnessEventsProvider');
  }
  return actions;
}
