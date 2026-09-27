'use client';

import React from 'react';
import type { WovenSurface } from './navigator';
import { WovenDialogueShell } from './woven-dialogue-shell';

type WovenDialogueRouteProps = {
  defaultSurface: WovenSurface;
};

export function WovenDialogueRoute({ defaultSurface }: WovenDialogueRouteProps): JSX.Element {
  // Every route enters the same continuing conversation surface.
  return <WovenDialogueShell defaultSurface={defaultSurface} />;
}
