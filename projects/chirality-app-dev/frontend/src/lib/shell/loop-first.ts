/**
 * Pure routing helpers for the loop-first / direct-chat surface (`/chat`).
 *
 * D-APP-23 (hybrid portal): the portal gains a loop-first "start session" entry
 * that focuses the live loop with the multi-view sidebar on the right; the
 * route surfaces (`/workbench`, `/pipeline`) keep the left sidebar. D-APP-24:
 * the direct-chat persona picker is restricted to Type-0/Type-1; the picker
 * drives the surface by setting `?agent=`, which `chat-panel` already resolves.
 */

export const CHAT_ROUTE = '/chat';
export const CHAT_SECTION = 'CHAT';

/**
 * Build the `/chat` href, optionally pre-selecting a persona via `?agent=`. The
 * portal "start session" entry uses the bare route; the persona picker uses the
 * `agent` form to drive `chat-panel`'s route-free `resolvePersona`.
 */
export function buildDirectChatHref(persona?: string | null): string {
  const trimmed = persona?.trim();
  if (!trimmed) {
    return CHAT_ROUTE;
  }
  return `${CHAT_ROUTE}?agent=${encodeURIComponent(trimmed)}`;
}
