'use client';

import React from 'react';
import { summarizeTurnActivity, type TurnActivity } from '../../lib/shell/turn-activity';

/**
 * Compact, expandable activity for one assistant turn. While the turn runs the
 * summary line names the latest observed action; after it ends the same
 * disclosure reads "Turn details" and stays collapsed unless the reader opened
 * it. Failures are counted in the summary so they are never hidden. Approval
 * requests and required user actions are separate cards that stay visible
 * until resolved; they are not folded in here.
 */
export function TurnActivityDisclosure({ activity, running, children }: { activity: TurnActivity; running: boolean; children?: React.ReactNode }): JSX.Element | null {
  if (activity.items.length === 0 && !children) return null;
  const summary = summarizeTurnActivity(activity, running);
  return <details className={running ? 'turn-activity turn-activity--live' : 'turn-activity'} data-failed={activity.failed || undefined}>
    <summary><span className="turn-activity-summary">{summary}</span></summary>
    {activity.items.length ? <ol className="turn-activity-list" aria-label="Observed activity">
      {activity.items.map(item => <li key={item.key} className={`turn-activity-item turn-activity-item--${item.kind} turn-activity-item--${item.status}`} data-status={item.status}>
        <span className="turn-activity-title">{item.title}</span>
        {item.detail ? <span className="turn-activity-detail">{item.detail}</span> : null}
      </li>)}
    </ol> : null}
    {children}
  </details>;
}
