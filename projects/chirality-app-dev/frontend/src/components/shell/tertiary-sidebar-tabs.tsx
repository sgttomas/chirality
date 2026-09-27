'use client';

import { AgentMatrix } from '../portal/agent-matrix';

export function createTertiarySidebarTabs(): {
  portalTab: JSX.Element;
} {
  return {
    portalTab: <AgentMatrix />
  };
}
