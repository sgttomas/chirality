'use client';

import { useCallback, useEffect, useState } from 'react';
import {
  DEFAULT_WOVEN_WORKSPACE_THEME,
  WOVEN_WORKSPACE_THEMES,
  readWovenWorkspaceStateFromStorage,
  writeWovenWorkspaceThemeToStorage,
  type WovenWorkspaceTheme
} from '../../lib/woven-dialogue/woven-workspace-state';

const THEME_LABELS: Record<WovenWorkspaceTheme, string> = {
  light: 'Light',
  dark: 'Dark',
  system: 'Auto'
};

/**
 * Every browser-only global is reached through here so the control renders in
 * a bare node environment (`renderToStaticMarkup`, `react-test-renderer`) with
 * no `window`, `localStorage` or `matchMedia` present. `system` needs no
 * `matchMedia` at all: it is resolved in CSS by `prefers-color-scheme`.
 */
function browserStorage(): Storage | undefined {
  if (typeof window === 'undefined') {
    return undefined;
  }
  try {
    return window.localStorage ?? undefined;
  } catch {
    return undefined;
  }
}

export function readPersistedTheme(): WovenWorkspaceTheme {
  const storage = browserStorage();
  if (!storage) {
    return DEFAULT_WOVEN_WORKSPACE_THEME;
  }
  return readWovenWorkspaceStateFromStorage(storage).theme;
}

export function applyTheme(theme: WovenWorkspaceTheme): void {
  if (typeof document === 'undefined') {
    return;
  }
  document.documentElement.setAttribute('data-theme', theme);
}

/**
 * Light / Dark / Auto selector for the compact top bar. Light is the rendered
 * and persisted default; the stored choice is read after mount so the server
 * markup stays deterministic, while `layout.tsx` stamps `data-theme` before
 * first paint so there is no flash.
 */
export function ThemeControl(): JSX.Element {
  const [theme, setTheme] = useState<WovenWorkspaceTheme>(
    DEFAULT_WOVEN_WORKSPACE_THEME
  );

  useEffect(() => {
    const stored = readPersistedTheme();
    setTheme(stored);
    applyTheme(stored);
  }, []);

  const chooseTheme = useCallback((next: WovenWorkspaceTheme): void => {
    setTheme(next);
    applyTheme(next);
    const storage = browserStorage();
    if (storage) {
      writeWovenWorkspaceThemeToStorage(storage, next);
    }
  }, []);

  return (
    <div className="shell-theme" role="group" aria-label="Theme">
      {WOVEN_WORKSPACE_THEMES.map((value) => (
        <button
          key={value}
          type="button"
          className="shell-theme-option"
          data-theme-option={value}
          aria-pressed={theme === value}
          onClick={() => chooseTheme(value)}
        >
          {THEME_LABELS[value]}
        </button>
      ))}
    </div>
  );
}
