'use client';

import React from 'react';

import { useCallback, useEffect, useId, useRef, useState } from 'react';
import { AccountPopover, type AccountPopoverProps } from './account-popover';
import { accountTitle, LocalModelStatus } from './account-settings-controls';
import { hostedBootstrapSummary, hostedBootstrapTitle } from '../settings/hosted-bootstrap-view';
import styles from './account-controls.module.css';

export function AccountRow(props: AccountPopoverProps): JSX.Element {
  const [open, setOpen] = useState(false);
  const root = useRef<HTMLDivElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);
  const panel = useRef<HTMLDivElement>(null);
  const id = useId();
  const position = useCallback(() => {
    if (!trigger.current || !panel.current) return;
    const rect = trigger.current.getBoundingClientRect();
    const width = Math.min(300, window.innerWidth - 24);
    const above = rect.top - 16;
    const below = window.innerHeight - rect.bottom - 16;
    Object.assign(panel.current.style, { width: `${width}px`, left: `${Math.max(12, Math.min(rect.left, window.innerWidth - width - 12))}px`,
      top: above >= below ? 'auto' : `${rect.bottom + 8}px`, bottom: above >= below ? `${window.innerHeight - rect.top + 8}px` : 'auto',
      maxHeight: `${Math.max(100, above >= below ? above : below)}px` });
  }, []);
  const dismiss = useCallback(() => { setOpen(false); trigger.current?.focus(); }, []);
  useEffect(() => {
    if (!open || typeof document === 'undefined') return;
    position();
    panel.current?.focus();
    const outside = (event: PointerEvent) => { if (event.target instanceof Node && !root.current?.contains(event.target)) setOpen(false); };
    const key = (event: KeyboardEvent) => { if (event.key === 'Escape') { event.preventDefault(); dismiss(); } else if ((event.metaKey || event.ctrlKey) && event.key === ',') { setOpen(false); } };
    document.addEventListener('pointerdown', outside);
    document.addEventListener('keydown', key);
    window.addEventListener('resize', position);
    window.addEventListener('scroll', position, true);
    return () => { document.removeEventListener('pointerdown', outside); document.removeEventListener('keydown', key); window.removeEventListener('resize', position); window.removeEventListener('scroll', position, true); };
  }, [open, position, dismiss]);
  useEffect(() => { setOpen(false); }, [props.folder]);
  return <div ref={root} className={styles.root} onBlur={event => {
    if (event.relatedTarget instanceof Node && !event.currentTarget.contains(event.relatedTarget)) setOpen(false);
  }}>
    <button ref={trigger} type="button" className={styles.row} aria-label="Account and settings" aria-expanded={open} aria-controls={id} aria-haspopup="dialog" onClick={() => {
      // Opening is the moment the operator looks at account state: ask the
      // daemon again rather than show what was last written optimistically.
      if (!open) props.hosted?.onRefresh();
      setOpen(!open);
    }}>
      <span className={styles.avatar} aria-hidden="true">{props.hosted?.snapshot?.registration === 'registered' && props.hosted.snapshot.status.ceremony === 'signed-in' ? 'A' : props.account.snapshot?.account.status === 'loggedIn' ? 'A' : '?'}</span>
      <span className={styles.identity}><strong>{props.hosted ? hostedBootstrapTitle(props.hosted) : accountTitle(props.account)}</strong><small>{props.hosted ? hostedBootstrapSummary(props.hosted) : <LocalModelStatus />}</small></span><span aria-hidden="true">⌃</span>
    </button>
    {open ? <div ref={panel} id={id} role="dialog" aria-label="Account and settings" tabIndex={-1} className={styles.popover}>
      <AccountPopover {...props} onOpenSettings={group => { dismiss(); props.onOpenSettings(group); }} />
    </div> : null}
  </div>;
}
