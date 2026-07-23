'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useMemo, useState, type ReactNode } from 'react';
import { ApiKeySettings } from '../settings/api-key-settings';
import { RuntimeSettings } from '../settings/runtime-settings';
import { useWorkspace } from '../workspace/workspace-provider';

export type ShellSection = 'PORTAL' | 'PIPELINE' | 'WORKBENCH' | 'CHAT';

type NavigationItem = {
  href: string;
  label: string;
};

// The loop-first pivot keeps route entry points for deep links, but Workbench
// and Pipeline are tertiary sidebar tabs rather than primary top-nav screens.
const NAVIGATION_ITEMS: NavigationItem[] = [
  { href: '/', label: 'PORTAL' }
];

type ShellFrameProps = {
  section: ShellSection;
  title: string;
  subtitle: string;
  children: ReactNode;
};

/**
 * Shared shell chrome — brand header + primary nav + the Working Root bar +
 * API-key settings — wrapping a surface-specific layout (`children`). Extracted
 * from `AppShell` so the loop-first `LoopShell` reuses the same chrome and
 * working-root control without duplicating it.
 */
export function ShellFrame({ section, title, subtitle, children }: ShellFrameProps): JSX.Element {
  const pathname = usePathname();
  const {
    projectRoot,
    hasElectronDirectoryPicker,
    errorMessage,
    clearError,
    applyProjectRoot,
    chooseProjectRoot,
    clearProjectRoot
  } = useWorkspace();
  const [draftPath, setDraftPath] = useState(projectRoot ?? '');

  useEffect(() => {
    setDraftPath(projectRoot ?? '');
  }, [projectRoot]);

  const currentRootLabel = useMemo(
    () => projectRoot ?? 'No working root selected',
    [projectRoot]
  );

  async function applyDraftPath(): Promise<void> {
    const nextPath = draftPath.trim();
    if (!nextPath) {
      clearProjectRoot();
      return;
    }

    await applyProjectRoot(nextPath);
  }

  return (
    <main className="shell">
      <header className="shell-header">
        <div className="shell-header-main">
          <div className="shell-brand-row">
            <img
              src="/chirality-app-icon.svg"
              alt="Chirality app icon"
              className="shell-brand-tile"
              width={48}
              height={48}
            />
            <div className="shell-brand-meta">
              <p className="shell-kicker">{section}</p>
              <h1>{title}</h1>
            </div>
          </div>
          <p className="shell-subtitle">{subtitle}</p>
        </div>

        <nav className="shell-nav" aria-label="Primary navigation">
          {NAVIGATION_ITEMS.map((item) => {
            const active = pathname === item.href;
            return (
              <Link
                key={item.href}
                className={active ? 'shell-nav-link shell-nav-link--active' : 'shell-nav-link'}
                href={item.href}
              >
                {item.label}
              </Link>
            );
          })}
        </nav>
      </header>

      <section className="working-root-bar">
        <div className="working-root-fields">
          <label htmlFor="project-root-input">Working Root (`projectRoot`)</label>
          <div className="working-root-controls">
            <input
              id="project-root-input"
              value={draftPath}
              onChange={(event) => {
                setDraftPath(event.target.value);
                if (errorMessage) {
                  clearError();
                }
              }}
              placeholder="/absolute/path/to/execution/root"
            />
            <button type="button" onClick={() => void applyDraftPath()}>
              Apply Path
            </button>
            <button
              type="button"
              className={hasElectronDirectoryPicker ? '' : 'button-muted'}
              onClick={() => void chooseProjectRoot()}
            >
              Choose Folder
            </button>
            <button type="button" className="button-muted" onClick={clearProjectRoot}>
              Clear
            </button>
          </div>
          <p className="working-root-current" title={currentRootLabel}>
            Active root: {currentRootLabel}
          </p>
          {errorMessage ? <p className="working-root-error">{errorMessage}</p> : null}
        </div>
        <div className="working-root-settings">
          <RuntimeSettings />
          <ApiKeySettings />
        </div>
      </section>

      {children}
    </main>
  );
}
