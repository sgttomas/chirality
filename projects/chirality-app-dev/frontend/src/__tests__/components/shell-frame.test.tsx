import React from 'react';
import renderer from 'react-test-renderer';
import { describe, expect, it, vi } from 'vitest';

vi.mock('next/navigation', () => ({ usePathname: () => '/' }));
vi.mock('next/link', () => ({
  default: ({ children, ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) =>
    React.createElement('a', props, children)
}));
vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => ({
    projectRoot: null,
    hasElectronDirectoryPicker: false,
    errorMessage: null,
    clearError: vi.fn(),
    applyProjectRoot: vi.fn(),
    chooseProjectRoot: vi.fn(),
    clearProjectRoot: vi.fn()
  })
}));
vi.mock('../../components/settings/api-key-settings', () => ({ ApiKeySettings: () => null }));
vi.mock('../../components/settings/runtime-settings', () => ({ RuntimeSettings: () => null }));

describe('ShellFrame', () => {
  it('renders the PORTAL header link with the active class', async () => {
    Object.assign(globalThis, { React });
    const { ShellFrame } = await import('../../components/shell/shell-frame');
    const tree = renderer.create(
      <ShellFrame section="PORTAL" title="Portal" subtitle="Workspace">
        <div>content</div>
      </ShellFrame>
    );

    const portalLink = tree.root.find(
      (node) => node.type === 'a' && node.props.href === '/'
    );
    expect(portalLink.props.className).toBe('shell-nav-link shell-nav-link--active');
    expect(portalLink.children).toEqual(['PORTAL']);
  });
});
