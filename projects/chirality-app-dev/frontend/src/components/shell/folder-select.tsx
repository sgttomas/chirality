'use client';

import React, { useEffect, useState } from 'react';
import { useWorkspace } from '../workspace/workspace-provider';

export type NativeFolderBridge = {
  registerRecent: (path: string) => Promise<{ ok: boolean; error?: string }>;
  pathForFile: (file: File) => string;
  subscribeOpen: (listener: (intent: { path?: string; error?: string }) => void) => () => void;
};
export function getNativeFolderBridge(): NativeFolderBridge | undefined {
  return typeof window === 'undefined' ? undefined : (window as unknown as { chirality?: { folders?: NativeFolderBridge } }).chirality?.folders;
}

export function FolderSelect({ locked, root, disabled, knownRoots = [], onPendingChange }: {
  knownRoots?: readonly { path: string; lastUsedAt: string }[];
  locked: boolean; root: string | null; disabled: boolean; onPendingChange?: (pending: boolean) => void;
}): JSX.Element {
  const { applyProjectRoot, chooseProjectRoot, hasElectronDirectoryPicker, errorMessage } = useWorkspace();
  const [path, setPath] = useState(root ?? '');
  const [pending, setPending] = useState(false);
  const [mounted, setMounted] = useState(false);
  useEffect(() => { setMounted(true); }, []);
  useEffect(() => { setPath(root ?? ''); }, [root]);
  const choose = async (native: boolean, candidate = path) => {
    if (locked || disabled || pending) return;
    setPending(true); onPendingChange?.(true);
    try { if (native) await chooseProjectRoot(); else if (candidate.trim()) await applyProjectRoot(candidate.trim()); }
    finally { setPending(false); onPendingChange?.(false); }
  };
  const label = root ? root.split('/').filter(Boolean).at(-1) ?? '/' : 'Choose folder';
  if (locked) return <span className="chat-folder-fixed" title={root ?? undefined}>▱ {label}</span>;
  // The native picker is the primary action; the typed path is a fallback kept
  // behind a disclosure so the menu reads as one decision, not a form.
  return <details className="chat-folder-select">
    <summary aria-label="Chat folder" title={root ?? 'Choose a folder before sending'}>▱ {label}⌄</summary>
    <div className="chat-folder-menu">
      <button type="button" disabled={disabled || pending || !mounted || !hasElectronDirectoryPicker} title={mounted && !hasElectronDirectoryPicker ? 'The native folder picker is available only in Chirality Desktop.' : undefined} onClick={() => void choose(true)}>Choose folder…</button>
      {knownRoots.length ? <label>Known folders<select aria-label="Known folders" value="" disabled={disabled || pending} onChange={event => { if (event.target.value) void choose(false, event.target.value); }}><option value="">Choose a known folder…</option>{knownRoots.map(item => <option key={item.path} value={item.path}>{item.path}</option>)}</select></label> : null}
      <details className="chat-folder-path">
        <summary>Enter a path…</summary>
        <label>Folder path<input aria-label="Folder path" value={path} disabled={disabled || pending} onChange={event => setPath(event.target.value)} /></label>
        <button type="button" className="button-muted" disabled={disabled || pending || !path.trim()} onClick={() => void choose(false)}>Use folder</button>
      </details>
      {errorMessage ? <p role="alert">{errorMessage}</p> : null}
    </div>
  </details>;
}
