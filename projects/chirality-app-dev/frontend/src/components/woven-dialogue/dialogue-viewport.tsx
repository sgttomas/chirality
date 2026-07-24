'use client';

import React, { type ReactNode } from 'react';

export type FocusedDialogueSurface = {
  id: 'document' | 'workbench' | 'pipeline';
  title: string;
  content: ReactNode;
};

type DialogueViewportProps = {
  primaryDialogue: ReactNode;
  replayLens?: ReactNode;
  focusedSurface?: FocusedDialogueSurface;
  onReturnToPrimary: () => void;
};

/**
 * Keeps the primary controller in one stable React subtree. Replay and focused
 * artifacts/surfaces are observational siblings; changing their visibility
 * never transfers controller props or replaces the mounted primary node.
 */
export function DialogueViewport({
  primaryDialogue,
  replayLens,
  focusedSurface,
  onReturnToPrimary
}: DialogueViewportProps): JSX.Element {
  const primaryVisible = !replayLens && !focusedSurface;

  return (
    <>
      <div
        className="woven-primary-dialogue"
        data-primary-dialogue-mounted="true"
        hidden={!primaryVisible}
        aria-hidden={!primaryVisible}
      >
        {primaryDialogue}
      </div>

      {replayLens ? <>{replayLens}</> : null}

      {!replayLens && focusedSurface ? (
        <section className="woven-focused-surface" data-focused-surface={focusedSurface.id}>
          <header className="woven-focused-header">
            <div>
              <p className="woven-eyebrow">Focused workspace surface</p>
              <h2>{focusedSurface.title}</h2>
            </div>
            <button type="button" onClick={onReturnToPrimary}>
              Return to primary dialogue
            </button>
          </header>
          {focusedSurface.content}
        </section>
      ) : null}
    </>
  );
}
