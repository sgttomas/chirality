'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useMemo, useState, type ReactNode } from 'react';
import { deriveRuntimeConnectivityPresentation } from '../../lib/shell/runtime-connectivity';
import { ApiKeySettings } from '../settings/api-key-settings';
import { RuntimeSettings } from '../settings/runtime-settings';
import { useWorkspace } from '../workspace/workspace-provider';
import { ThemeControl } from './theme-control';
import { useRuntimeConnectivity } from './use-runtime-connectivity';

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
  variant?: 'default' | 'workspace';
};

/**
 * Shared shell chrome — one compact 48px top bar carrying the brand mark, the
 * surface name, the working-root chip (a disclosure holding the full working
 * root and runtime/credential controls), primary navigation and the theme
 * control — wrapping a surface-specific layout (`children`).
 *
 * Recomposed for the calm-editorial design system: the stacked brand header
 * and Working Root card collapse into this single bar, and every control they
 * carried is preserved inside the disclosure.
 */
export function ShellFrame({
  section,
  title,
  subtitle,
  children,
  variant = 'default'
}: ShellFrameProps): JSX.Element {
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

  const rootDotClassName = errorMessage
    ? 'shell-root-dot shell-root-dot--error'
    : projectRoot
      ? 'shell-root-dot shell-root-dot--ready'
      : 'shell-root-dot';

  // Runtime connectivity is a second, independent axis from the working root: the
  // root can be valid while every harness request fails because the daemon is
  // unreachable. It is absent entirely outside the desktop app, where there is no
  // daemon to report on. Class names are kept off the `shell-root-dot` prefix so
  // the two indicators stay independently addressable.
  const runtimeConnectivity = useRuntimeConnectivity();
  const runtimeIndicator = deriveRuntimeConnectivityPresentation(runtimeConnectivity);

  async function applyDraftPath(): Promise<void> {
    const nextPath = draftPath.trim();
    if (!nextPath) {
      clearProjectRoot();
      return;
    }

    await applyProjectRoot(nextPath);
  }

  return (
    <main className={variant === 'workspace' ? 'shell shell--workspace' : 'shell'}>
      <header
        className={
          variant === 'workspace' ? 'shell-header shell-header--workspace' : 'shell-header'
        }
      >
        <div className="shell-brand-row">
          <img
            src="/chirality-app-icon.svg"
            alt=""
            className="shell-brand-tile"
            width={26}
            height={26}
          />
          <span className="shell-wordmark">
            Chira<em>lity</em>
          </span>
        </div>

        <div className="shell-header-main">
          <p className="shell-kicker">{section}</p>
          <h1>{title}</h1>
          <p className="shell-subtitle" title={subtitle}>
            {subtitle}
          </p>
        </div>

        <div className="shell-header-controls">
          {runtimeIndicator ? (
            <span
              className={`shell-runtime-chip shell-runtime-chip--${runtimeIndicator.tone}`}
              title={runtimeIndicator.title}
              role="status"
            >
              <span
                className={`shell-runtime-dot shell-runtime-dot--${runtimeIndicator.tone}`}
                aria-hidden="true"
              />
              <span className="shell-runtime-chip-key">runtime</span>
              <span className="shell-runtime-chip-value">{runtimeIndicator.label}</span>
            </span>
          ) : null}

          <details className="shell-root-disclosure">
            <summary className="shell-root-chip" title={currentRootLabel}>
              <span className={rootDotClassName} aria-hidden="true" />
              <span className="shell-root-chip-key">root</span>
              <span className="shell-root-chip-value">{currentRootLabel}</span>
            </summary>

            <section
              className={
                variant === 'workspace'
                  ? 'working-root-bar working-root-bar--workspace'
                  : 'working-root-bar'
              }
            >
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

              <details className="working-root-settings working-root-settings--disclosure">
                <summary>Runtime &amp; credentials</summary>
                <div className="working-root-settings-disclosure-body">
                  <RuntimeSettings />
                  <ApiKeySettings />
                </div>
              </details>
            </section>
          </details>

          {variant === 'workspace' ? (
            <div className="shell-nav" aria-label="Current workspace">
              <span className="shell-nav-link shell-nav-link--active">WORKSPACE</span>
            </div>
          ) : (
            <nav className="shell-nav" aria-label="Primary navigation">
              {NAVIGATION_ITEMS.map((item) => {
                const active = pathname === item.href;
                return (
                  <Link
                    key={item.href}
                    className={
                      active ? 'shell-nav-link shell-nav-link--active' : 'shell-nav-link'
                    }
                    href={item.href}
                  >
                    {item.label}
                  </Link>
                );
              })}
            </nav>
          )}

          <ThemeControl />
        </div>
      </header>

      {children}
    </main>
  );
}
