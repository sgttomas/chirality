import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it, vi } from 'vitest';
import { Navigator } from '../../components/woven-dialogue/navigator';

vi.mock('../../components/shell/file-tree-panel', () => ({
  FileTreePanel: () => <div>File tree</div>
}));

describe('Woven Dialogue Navigator', () => {
  it('opens the legacy compatibility surface separately so primary dialogue stays mounted', () => {
    const html = renderToStaticMarkup(
      <Navigator
        activeSurface="dialogue"
        legacyHref="/?legacy=1"
        onOpenSurface={vi.fn()}
      />
    );

    expect(html).toContain('href="/?legacy=1"');
    expect(html).toContain('target="_blank"');
    expect(html).toContain('Open legacy interface in a new window');
  });
});
