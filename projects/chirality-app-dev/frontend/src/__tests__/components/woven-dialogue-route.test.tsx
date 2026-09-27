import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it, vi } from 'vitest';
import { WovenDialogueRoute } from '../../components/woven-dialogue/woven-dialogue-route';

vi.mock('../../components/woven-dialogue/woven-dialogue-shell', () => ({
  WovenDialogueShell: ({ defaultSurface }: { defaultSurface: string }) => (
    <main data-woven-surface={defaultSurface}>Woven Dialogue</main>
  )
}));

describe('Woven Dialogue route selection', () => {
  it('renders Woven Dialogue by default', () => {
    const html = renderToStaticMarkup(<WovenDialogueRoute defaultSurface="dialogue" />);

    expect(html).toContain('data-woven-surface="dialogue"');
    expect(html).not.toContain('data-legacy="true"');
  });

  it.each(['workbench', 'pipeline'] as const)('opens /%s in the continuing conversation surface', (surface) => {
    const html = renderToStaticMarkup(<WovenDialogueRoute defaultSurface={surface} />);
    expect(html).toContain(`data-woven-surface="${surface}"`);
  });
});
