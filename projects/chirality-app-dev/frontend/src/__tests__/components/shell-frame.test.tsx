import React from 'react';
import renderer, { act, type ReactTestRenderer } from 'react-test-renderer';
import { beforeEach, describe, expect, it, vi } from 'vitest';

type WorkspaceFixture = {
  projectRoot: string | null;
  hasElectronDirectoryPicker: boolean;
  errorMessage: string | null;
  clearError: () => void;
  applyProjectRoot: (path: string) => Promise<void>;
  chooseProjectRoot: () => Promise<void>;
  clearProjectRoot: () => void;
};

const workspace = vi.hoisted(() => ({
  value: null as unknown
}));

vi.mock('next/navigation', () => ({ usePathname: () => '/' }));
vi.mock('next/link', () => ({
  default: ({ children, ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) =>
    React.createElement('a', props, children)
}));
vi.mock('../../components/workspace/workspace-provider', () => ({
  useWorkspace: () => workspace.value
}));
vi.mock('../../components/settings/api-key-settings', () => ({ ApiKeySettings: () => null }));
vi.mock('../../components/settings/runtime-settings', () => ({ RuntimeSettings: () => null }));

function setWorkspace(overrides: Partial<WorkspaceFixture> = {}): void {
  workspace.value = {
    projectRoot: null,
    hasElectronDirectoryPicker: false,
    errorMessage: null,
    clearError: vi.fn(),
    applyProjectRoot: vi.fn(),
    chooseProjectRoot: vi.fn(),
    clearProjectRoot: vi.fn(),
    ...overrides
  } satisfies WorkspaceFixture;
}

async function renderShell(): Promise<ReactTestRenderer> {
  Object.assign(globalThis, { React });
  const { ShellFrame } = await import('../../components/shell/shell-frame');
  let tree!: ReactTestRenderer;
  act(() => {
    tree = renderer.create(
      <ShellFrame section="PORTAL" title="Portal" subtitle="Workspace">
        <div>content</div>
      </ShellFrame>
    );
  });
  return tree;
}

function textOf(node: renderer.ReactTestInstance): string {
  return node.children
    .map((child) => (typeof child === 'string' ? child : textOf(child)))
    .join('');
}

describe('ShellFrame', () => {
  beforeEach(() => {
    setWorkspace();
  });

  it('renders the PORTAL header link with the active class', async () => {
    const tree = await renderShell();

    const portalLink = tree.root.find(
      (node) => node.type === 'a' && node.props.href === '/'
    );
    expect(portalLink.props.className).toBe('shell-nav-link shell-nav-link--active');
    expect(portalLink.children).toEqual(['PORTAL']);
  });

  it('keeps every Working Root control inside the top-bar disclosure', async () => {
    const tree = await renderShell();

    const disclosure = tree.root.find(
      (node) => node.type === 'details' && node.props.className === 'shell-root-disclosure'
    );

    const input = disclosure.find(
      (node) => node.type === 'input' && node.props.id === 'project-root-input'
    );
    expect(input.props.placeholder).toBe('/absolute/path/to/execution/root');

    const buttonLabels = disclosure
      .findAll((node) => node.type === 'button')
      .map((node) => textOf(node));
    expect(buttonLabels).toEqual(['Apply Path', 'Choose Folder', 'Clear']);

    const current = disclosure.find(
      (node) => node.props.className === 'working-root-current'
    );
    expect(textOf(current)).toBe('Active root: No working root selected');

    expect(
      disclosure.findAll((node) => node.props.className === 'working-root-error')
    ).toHaveLength(0);

    // The runtime/credentials disclosure survives the recomposition.
    const settings = disclosure.find(
      (node) =>
        node.type === 'details' &&
        node.props.className === 'working-root-settings working-root-settings--disclosure'
    );
    expect(textOf(settings.find((node) => node.type === 'summary'))).toBe(
      'Runtime & credentials'
    );
  });

  it('marks the root chip ready and shows the active root when one is set', async () => {
    setWorkspace({ projectRoot: '/tmp/execution-root' });
    const tree = await renderShell();

    const dot = tree.root.find((node) =>
      String(node.props.className ?? '').startsWith('shell-root-dot')
    );
    expect(dot.props.className).toBe('shell-root-dot shell-root-dot--ready');

    const chipValue = tree.root.find(
      (node) => node.props.className === 'shell-root-chip-value'
    );
    expect(textOf(chipValue)).toBe('/tmp/execution-root');
  });

  it('surfaces a working-root error on the chip and in the disclosure', async () => {
    setWorkspace({ errorMessage: 'Path is not readable' });
    const tree = await renderShell();

    const dot = tree.root.find((node) =>
      String(node.props.className ?? '').startsWith('shell-root-dot')
    );
    expect(dot.props.className).toBe('shell-root-dot shell-root-dot--error');

    const error = tree.root.find(
      (node) => node.props.className === 'working-root-error'
    );
    expect(textOf(error)).toBe('Path is not readable');
  });

  it('renders the theme control with light selected by default', async () => {
    const tree = await renderShell();

    const group = tree.root.find((node) => node.props.className === 'shell-theme');
    expect(group.props.role).toBe('group');
    expect(group.props['aria-label']).toBe('Theme');

    const options = group.findAll((node) => node.type === 'button');
    expect(options.map((node) => node.props['data-theme-option'])).toEqual([
      'light',
      'dark',
      'system'
    ]);
    expect(options.map((node) => textOf(node))).toEqual(['Light', 'Dark', 'Auto']);
    expect(options.map((node) => node.props['aria-pressed'])).toEqual([
      true,
      false,
      false
    ]);
  });

  it('moves the pressed state when another theme is chosen', async () => {
    const tree = await renderShell();

    const darkOption = tree.root.find(
      (node) => node.type === 'button' && node.props['data-theme-option'] === 'dark'
    );
    act(() => {
      darkOption.props.onClick();
    });

    const pressed = tree.root
      .findAll(
        (node) => node.type === 'button' && node.props['aria-pressed'] === true
      )
      .map((node) => node.props['data-theme-option']);
    expect(pressed).toEqual(['dark']);
  });
});

it('anchors woven Settings outside its trigger and dismisses with Escape or an outside pointer', async () => {
  const handlers = new Map<string, (event: unknown) => void>();
  class FixtureNode {}
  const trigger = { getBoundingClientRect: () => ({ top: 700, bottom: 730, left: 24 }), focus: vi.fn() };
  const panel = { style: {} as Record<string, string> };
  const disclosure = { open: true, querySelector: (selector: string) => selector === 'summary' ? trigger : panel, contains: (target: unknown) => target === trigger };
  vi.stubGlobal('Node', FixtureNode);
  vi.stubGlobal('document', { documentElement: { setAttribute: vi.fn() }, addEventListener: (name: string, handler: (event: unknown) => void) => handlers.set(name, handler), removeEventListener: (name: string) => handlers.delete(name) });
  vi.stubGlobal('window', { innerHeight: 800, innerWidth: 1000, addEventListener: vi.fn(), removeEventListener: vi.fn() });
  setWorkspace();
  const { ShellFrame } = await import('../../components/shell/shell-frame');
  let tree!: ReactTestRenderer;
  try {
    act(() => { tree = renderer.create(<ShellFrame section="CHAT" title="Chat" subtitle="" variant="workspace" renderWorkspaceContent={({ settingsControl }) => settingsControl} />, { createNodeMock: element => element.props.className === 'shell-root-disclosure' ? disclosure : null }); });
    tree.root.findByProps({ className: 'shell-root-disclosure' }).props.onToggle();
    expect(panel.style.bottom).toBe('108px'); // Popup ends eight pixels before the trigger.
    expect(panel.style.maxHeight).toBe('684px');
    handlers.get('keydown')?.({ key: 'Escape' });
    expect(disclosure.open).toBe(false); expect(trigger.focus).toHaveBeenCalledTimes(1);
    disclosure.open = true;
    handlers.get('pointerdown')?.({ target: new FixtureNode() });
    expect(disclosure.open).toBe(false);
    act(() => tree.unmount());
    expect(handlers.size).toBe(0);
  } finally { vi.unstubAllGlobals(); }
});
