import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { WovenDialogueRoute } from '../../components/woven-dialogue/woven-dialogue-route';

const routerState = vi.hoisted(() => ({ query: '' }));

vi.mock('next/navigation', () => ({
  useSearchParams: () => new URLSearchParams(routerState.query)
}));
vi.mock('../../components/woven-dialogue/woven-dialogue-shell', () => ({
  WovenDialogueShell: ({ defaultSurface }: { defaultSurface: string }) => (
    <main data-woven-surface={defaultSurface}>Woven Dialogue</main>
  )
}));

describe('Woven Dialogue route selection', () => {
  beforeEach(() => {
    routerState.query = '';
  });

  it('renders Woven Dialogue by default', () => {
    const html = renderToStaticMarkup(
      <WovenDialogueRoute
        defaultSurface="dialogue"
        legacy={<main>Legacy</main>}
      />
    );

    expect(html).toContain('data-woven-surface="dialogue"');
    expect(html).not.toContain('data-legacy="true"');
  });

  it('keeps the direct legacy route available', () => {
    routerState.query = 'legacy=1';
    const html = renderToStaticMarkup(
      <WovenDialogueRoute
        defaultSurface="dialogue"
        legacy={<main>Legacy</main>}
      />
    );

    expect(html.match(/data-legacy="true"/g)).toHaveLength(1);
    expect(html).toContain('style="display:contents"');
    expect(html).toContain('<main>Legacy</main>');
  });
});
