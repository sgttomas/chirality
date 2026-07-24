'use client';

import Link from 'next/link';
import React from 'react';
import { FileTreePanel } from '../shell/file-tree-panel';

export type WovenSurface =
  | 'dialogue'
  | 'workbench'
  | 'pipeline';

type NavigatorProps = {
  activeSurface: WovenSurface;
  legacyHref: string;
  onOpenSurface: (surface: WovenSurface) => void;
};

const SURFACES: ReadonlyArray<{ id: WovenSurface; label: string; note: string }> = [
  { id: 'dialogue', label: 'Dialogue', note: 'Primary human–agent conversation' },
  { id: 'workbench', label: 'Workbench', note: 'Documents, evidence & contracts' },
  { id: 'pipeline', label: 'Pipeline', note: 'DECOMP, PREP, TASK, and AUDIT intent' }
];

export function Navigator({
  activeSurface,
  legacyHref,
  onOpenSurface
}: NavigatorProps): JSX.Element {
  return (
    <nav className="woven-navigator" aria-label="Workspace Navigator">
      <header className="woven-region-header">
        <div>
          <p className="woven-eyebrow">Workspace</p>
          <h2>Navigator</h2>
        </div>
      </header>

      <div className="woven-navigator-sections" aria-label="Workspace surfaces">
        {SURFACES.map((surface) => (
          <button
            key={surface.id}
            type="button"
            className={
              activeSurface === surface.id
                ? 'woven-nav-item woven-nav-item--active'
                : 'woven-nav-item'
            }
            aria-current={activeSurface === surface.id ? 'page' : undefined}
            onClick={() => {
              onOpenSurface(surface.id);
            }}
          >
            <span>{surface.label}</span>
            <small>{surface.note}</small>
          </button>
        ))}
      </div>

      <section className="woven-navigator-files" aria-label="Project files">
        <FileTreePanel />
      </section>

      <footer className="woven-compatibility">
        <p>Compatibility</p>
        <Link href={legacyHref} target="_blank" rel="noreferrer">
          Open legacy interface in a new window
        </Link>
      </footer>
    </nav>
  );
}
