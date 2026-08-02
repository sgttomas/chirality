'use client';

import { useSearchParams } from 'next/navigation';
import React, { type ReactNode } from 'react';
import type { WovenSurface } from './navigator';
import { WovenDialogueShell } from './woven-dialogue-shell';

type WovenDialogueRouteProps = {
  defaultSurface: WovenSurface;
  legacy: ReactNode;
};

export function WovenDialogueRoute({
  defaultSurface,
  legacy
}: WovenDialogueRouteProps): JSX.Element {
  const searchParams = useSearchParams();

  // `useSearchParams()` is nullable in static/component render harnesses that
  // do not provide a Next router. Preserve the established route surface in
  // that compatibility environment rather than guessing at navigation state.
  if (!searchParams || searchParams.get('legacy') === '1') {
    return (
      <div data-legacy="true" style={{ display: 'contents' }}>
        {legacy}
      </div>
    );
  }

  return <WovenDialogueShell defaultSurface={defaultSurface} />;
}
