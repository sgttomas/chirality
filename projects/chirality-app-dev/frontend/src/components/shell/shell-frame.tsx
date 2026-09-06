'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useCallback, useEffect, useId, useMemo, useRef, useState, type ReactNode } from 'react';
import { deriveRuntimeConnectivityPresentation } from '../../lib/shell/runtime-connectivity';
import { ApiKeySettings } from '../settings/api-key-settings';
import { RuntimeSettings } from '../settings/runtime-settings';
import { useWorkspace } from '../workspace/workspace-provider';
import { useRuntimeConnectivitySnapshot } from './runtime-connectivity-provider';
import { ThemeControl } from './theme-control';

export type ShellSection = 'PORTAL' | 'PIPELINE' | 'WORKBENCH' | 'CHAT';

type NavigationItem = {
  href: string;
  label: string;
};

type RuntimeStatusResult =
  | {
      ok: true;
      launchAgent: {
        installed: boolean;
        loaded: boolean;
      };
      daemon: {
        running: boolean;
        pid?: number;
        startedAt?: string;
      };
    }
  | { ok: false; error: string };

type RuntimeStatusBridge = {
  status: () => Promise<RuntimeStatusResult>;
};

type RuntimeStatusWindow = typeof window & {
  chirality?: {
    runtime?: {
      daemon?: RuntimeStatusBridge;
    };
  };
};

function getRuntimeStatusBridge(): RuntimeStatusBridge | undefined {
  if (typeof window === 'undefined') {
    return undefined;
  }
  return (window as RuntimeStatusWindow).chirality?.runtime?.daemon;
}

// The loop-first pivot keeps route entry points for deep links, but Workbench
// and Pipeline are tertiary sidebar tabs rather than primary top-nav screens.
const NAVIGATION_ITEMS: NavigationItem[] = [
  { href: '/', label: 'PORTAL' }
];

type ShellFrameProps = {
  section: ShellSection;
  title: string;
  subtitle: string;
  children?: ReactNode;
  folderLocked?: boolean;
  onFolderSelectionPending?: (pending: boolean) => void;
  renderWorkspaceContent?: (controls: { reconnectControl: ReactNode; settingsControl: ReactNode }) => ReactNode;
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
  variant = 'default',
  folderLocked = false,
  onFolderSelectionPending,
  renderWorkspaceContent
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
  const settingsRef = useRef<HTMLDetailsElement | null>(null);
  const positionSettings = useCallback(() => {
    const disclosure = settingsRef.current;
    if (!renderWorkspaceContent || !disclosure?.open) return;
    const trigger = disclosure.querySelector('summary');
    const panel = disclosure.querySelector<HTMLElement>('.working-root-bar');
    if (!trigger || !panel) return;
    const rect = trigger.getBoundingClientRect();
    const above = Math.max(0, rect.top - 16);
    const below = Math.max(0, window.innerHeight - rect.bottom - 16);
    const opensAbove = above >= below;
    panel.style.top = opensAbove ? 'auto' : `${rect.bottom + 8}px`;
    panel.style.bottom = opensAbove ? `${window.innerHeight - rect.top + 8}px` : 'auto';
    panel.style.left = `${Math.max(12, Math.min(rect.left, window.innerWidth - Math.min(460, window.innerWidth - 24) - 12))}px`;
    panel.style.maxHeight = `${opensAbove ? above : below}px`;
  }, [renderWorkspaceContent]);

  useEffect(() => {
    if (!renderWorkspaceContent || typeof document === 'undefined') return;
    const dismissOutside = (event: PointerEvent) => {
      const disclosure = settingsRef.current;
      if (disclosure?.open && event.target instanceof Node && !disclosure.contains(event.target)) disclosure.open = false;
    };
    const dismissEscape = (event: KeyboardEvent) => {
      const disclosure = settingsRef.current;
      if (event.key === 'Escape' && disclosure?.open) {
        disclosure.open = false;
        disclosure.querySelector('summary')?.focus();
      }
    };
    document.addEventListener('pointerdown', dismissOutside);
    document.addEventListener('keydown', dismissEscape);
    window.addEventListener('resize', positionSettings);
    window.addEventListener('scroll', positionSettings, true);
    return () => {
      document.removeEventListener('pointerdown', dismissOutside);
      document.removeEventListener('keydown', dismissEscape);
      window.removeEventListener('resize', positionSettings);
      window.removeEventListener('scroll', positionSettings, true);
    };
  }, [renderWorkspaceContent, positionSettings]);


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
  const runtimeConnectivity = useRuntimeConnectivitySnapshot();
  const runtimeIndicator = deriveRuntimeConnectivityPresentation(runtimeConnectivity);
  const [runtimeCheckPending, setRuntimeCheckPending] = useState(false);
  const [runtimeCheckError, setRuntimeCheckError] = useState<string | null>(null);
  const runtimeCheckActiveRef = useRef(false);
  const runtimeFeedbackId = useId();

  useEffect(() => {
    // A new main-process snapshot supersedes any local probe failure. The chip's
    // tone and visible label always remain derived from that snapshot alone.
    setRuntimeCheckError(null);
  }, [runtimeConnectivity?.changedAt]);

  async function checkRuntimeConnection(): Promise<void> {
    if (runtimeCheckActiveRef.current) {
      return;
    }

    runtimeCheckActiveRef.current = true;
    setRuntimeCheckPending(true);
    setRuntimeCheckError(null);
    try {
      const bridge = getRuntimeStatusBridge();
      if (!bridge) {
        setRuntimeCheckError('Runtime control is unavailable');
        return;
      }

      const result = await bridge.status();
      if (!result.ok) {
        setRuntimeCheckError(result.error);
      } else if (!result.daemon.running) {
        setRuntimeCheckError('Runtime daemon is unreachable');
      }
    } catch {
      setRuntimeCheckError('Unable to contact the Chirality runtime');
    } finally {
      runtimeCheckActiveRef.current = false;
      setRuntimeCheckPending(false);
    }
  }

  async function applyDraftPath(): Promise<void> {
    if (folderLocked) return;
    const nextPath = draftPath.trim();
    if (!nextPath) {
      clearProjectRoot();
      return;
    }

    onFolderSelectionPending?.(true);
    try { await applyProjectRoot(nextPath); } finally { onFolderSelectionPending?.(false); }
  }

  const reconnectControl = (runtimeIndicator ? (
            <span className="shell-runtime-control">
              <button
                type="button"
                className={`shell-runtime-chip shell-runtime-chip--${runtimeIndicator.tone}`}
                title={
                  runtimeCheckError
                    ? `${runtimeIndicator.title}. Last check failed: ${runtimeCheckError}`
                    : `${runtimeIndicator.title}. Check connection now.`
                }
                aria-label={`${runtimeCheckPending ? 'Checking' : 'Check'} runtime connection; reported status: ${runtimeIndicator.label}`}
                aria-describedby={runtimeFeedbackId}
                aria-busy={runtimeCheckPending}
                data-runtime-check-error={runtimeCheckError ? true : undefined}
                disabled={runtimeCheckPending}
                onClick={() => void checkRuntimeConnection()}
              >
                <span
                  className={`shell-runtime-dot shell-runtime-dot--${runtimeIndicator.tone}`}
                  aria-hidden="true"
                />
                <span className="shell-runtime-chip-key">runtime</span>
                <span className="shell-runtime-chip-value">{runtimeIndicator.label}</span>
              </button>
              <span
                id={runtimeFeedbackId}
                className="shell-runtime-feedback"
                role="status"
                aria-live="polite"
              >
                {runtimeCheckError
                  ? `Runtime connection check failed: ${runtimeCheckError}`
                  : runtimeCheckPending
                    ? `Checking runtime connection; reported status remains ${runtimeIndicator.label}`
                    : `Runtime reported ${runtimeIndicator.label}`}
              </span>
            </span>
          ) : null);
  const settingsControl = (<details ref={settingsRef} className="shell-root-disclosure" onToggle={positionSettings}>
            <summary className="shell-root-chip" title={currentRootLabel}>
              {renderWorkspaceContent ? 'Settings' : <>
              <span className={rootDotClassName} aria-hidden="true" />
              <span className="shell-root-chip-key">root</span>
              <span className="shell-root-chip-value">{currentRootLabel}</span>
              </>}
            </summary>

            <section
              className={
                variant === 'workspace'
                  ? 'working-root-bar working-root-bar--workspace'
                  : 'working-root-bar'
              }
            >
              {!renderWorkspaceContent ? (              <div className="working-root-fields">
                {folderLocked ? <p>Folder is fixed for this chat. Start a new chat to change it.</p> : null}
                <label htmlFor="project-root-input">Working Root (`projectRoot`)</label>
                <div className="working-root-controls">
                  <input
                    disabled={folderLocked}
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
                  <button type="button" disabled={folderLocked} onClick={() => void applyDraftPath()}>
                    Apply Path
                  </button>
                  <button
                    type="button"
                    disabled={folderLocked}
                    className={hasElectronDirectoryPicker ? '' : 'button-muted'}
                    onClick={() => { if (!folderLocked) { onFolderSelectionPending?.(true); void chooseProjectRoot().finally(() => onFolderSelectionPending?.(false)); } }}
                  >
                    Choose Folder
                  </button>
                  <button type="button" disabled={folderLocked} className="button-muted" onClick={() => { if (!folderLocked) clearProjectRoot(); }}>
                    Clear
                  </button>
                </div>
                <p className="working-root-current" title={currentRootLabel}>
                  Active root: {currentRootLabel}
                </p>
                {errorMessage ? <p className="working-root-error">{errorMessage}</p> : null}
              </div>) : null}

              <details className="working-root-settings working-root-settings--disclosure">
                <summary>Runtime &amp; credentials</summary>
                <div className="working-root-settings-disclosure-body">
                  <RuntimeSettings />
                  <ApiKeySettings />
                </div>
              </details>
            </section>
          </details>);
  if (variant === 'workspace' && renderWorkspaceContent) {
    return <main className="shell shell--workspace shell--stone">{renderWorkspaceContent({
      reconnectControl,
      settingsControl: <div className="woven-settings-controls">{settingsControl}<ThemeControl /></div>
    })}</main>;
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
          {reconnectControl}

          {settingsControl}

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
