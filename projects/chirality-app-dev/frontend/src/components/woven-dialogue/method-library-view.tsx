'use client';

import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  inspectMethod,
  listMethods,
  qualifiedMethodId,
  type MethodDescriptor,
  type QualifiedMethodReference
} from '../../lib/harness/method-selection-client';
import type { MethodInspectionResponse } from '@chirality/runtime-contracts/v3';
import { useRuntimeEpoch } from '../shell/runtime-connectivity-provider';

type LibraryView = 'workflows' | 'skills' | 'legacy';

function sameMethod(left: QualifiedMethodReference, right: QualifiedMethodReference): boolean {
  return left.kind === right.kind && left.name === right.name && left.source === right.source && left.sourceRootId === right.sourceRootId;
}

function metadataText(method: MethodDescriptor, ...keys: string[]): string | undefined {
  for (const key of keys) {
    const value = method.metadata?.[key];
    if (typeof value === 'string' && value.trim()) return value.trim();
    if (Array.isArray(value)) {
      const items = value.filter((item): item is string => typeof item === 'string' && Boolean(item.trim()));
      if (items.length) return items.join(', ');
    }
  }
  return undefined;
}

function sourceLabel(method: MethodDescriptor): string {
  if (method.source === 'project') return 'This project';
  if (method.source === 'user') return 'Your library';
  return 'Chirality library';
}

function workflowGroup(method: MethodDescriptor): string {
  if (method.central) return 'Start here';
  if (method.source === 'project') return 'For this project';
  if (method.source === 'user') return 'Your workflows';
  return metadataText(method, 'category', 'group', 'purpose') ?? 'More workflows';
}

function groupedWorkflows(methods: readonly MethodDescriptor[]): Array<{ label: string; methods: MethodDescriptor[] }> {
  const order = ['Start here', 'For this project', 'Your workflows'];
  const groups = new Map<string, MethodDescriptor[]>();
  for (const method of methods) {
    const label = workflowGroup(method);
    groups.set(label, [...(groups.get(label) ?? []), method]);
  }
  return [...groups].sort(([left], [right]) => {
    const leftIndex = order.indexOf(left); const rightIndex = order.indexOf(right);
    if (leftIndex >= 0 || rightIndex >= 0) return (leftIndex < 0 ? order.length : leftIndex) - (rightIndex < 0 ? order.length : rightIndex);
    return left.localeCompare(right);
  }).map(([label, entries]) => ({
    label,
    methods: entries.sort((a, b) => Number(b.central) - Number(a.central) || a.name.localeCompare(b.name))
  }));
}

function MethodCard({ method, active, inspectionPending, onInspect, onToggle }: {
  method: MethodDescriptor;
  active: boolean;
  inspectionPending: boolean;
  onInspect: () => void;
  onToggle?: () => void;
}): JSX.Element {
  const purpose = metadataText(method, 'purpose', 'useWhen', 'use_when');
  const applicability = metadataText(method, 'applicability', 'appliesTo', 'applies_to');
  return <li className={method.central ? 'method-card method-card--central' : 'method-card'}>
    <div className="method-card-heading"><strong>{method.name}</strong></div>
    <p>{purpose ?? method.description}</p>
    {applicability ? <p className="method-applicability"><strong>Useful for:</strong> {applicability}</p> : null}
    <p className="method-card-meta"><small>{sourceLabel(method)}</small></p>
    <div className="method-card-actions">
      <button type="button" disabled={inspectionPending} onClick={onInspect}>{inspectionPending ? 'Opening…' : 'Inspect'}</button>
      {onToggle ? <button type="button" aria-pressed={active} onClick={onToggle}>{active ? 'Remove' : 'Use in message'}</button> : <small>Read-only reference</small>}
    </div>
  </li>;
}

export function MethodLibraryView({ projectRoot, selected, onSelectedChange, refresh = 0 }: {
  projectRoot: string;
  selected: readonly QualifiedMethodReference[];
  onSelectedChange: (methods: QualifiedMethodReference[]) => void;
  refresh?: number;
}): JSX.Element {
  const [query, setQuery] = useState('');
  const [view, setView] = useState<LibraryView>('workflows');
  const [methods, setMethods] = useState<MethodDescriptor[]>([]);
  const [inspection, setInspection] = useState<MethodInspectionResponse | null>(null);
  const [inspectionPendingId, setInspectionPendingId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const inspectionGeneration = useRef(0);
  const runtimeEpoch = useRuntimeEpoch();

  useEffect(() => {
    const controller = new AbortController();
    inspectionGeneration.current += 1;
    setInspection(null); setInspectionPendingId(null); setMethods([]); setLoading(true); setError(null);
    const timer = setTimeout(() => {
      void listMethods(projectRoot, query, controller.signal)
        .then(result => { if (!controller.signal.aborted) setMethods([...result.methods]); })
        .catch(reason => { if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : 'The method catalog is unavailable.'); })
        .finally(() => { if (!controller.signal.aborted) setLoading(false); });
    }, query ? 150 : 0);
    return () => { clearTimeout(timer); controller.abort(); };
  }, [projectRoot, query, refresh, runtimeEpoch]);

  const visible = useMemo(() => methods.filter(method => view === 'workflows'
    ? method.kind === 'workflow' && method.compatibility !== 'legacy'
    : view === 'legacy' ? method.compatibility === 'legacy' && (method.kind === 'workflow' || method.source === 'bundled')
    : method.kind === 'skill' && method.source === 'bundled' && method.compatibility !== 'legacy'), [methods, view]);
  const workflowGroups = useMemo(() => groupedWorkflows(visible), [visible]);
  const skillGroups = useMemo(() => [
    { label: 'Bundled skill reference', methods: [...visible].sort((a, b) => a.name.localeCompare(b.name)) }
  ].filter(group => group.methods.length), [visible]);
  const groups = view === 'skills' ? skillGroups : view === 'legacy' ? [{ label: 'Historical methods', methods: visible }] : workflowGroups;

  const openInspection = (method: MethodDescriptor): void => {
    const generation = inspectionGeneration.current + 1;
    inspectionGeneration.current = generation;
    const id = qualifiedMethodId(method);
    setError(null); setInspection(null); setInspectionPendingId(id);
    void inspectMethod(projectRoot, method)
      .then(result => { if (inspectionGeneration.current === generation) setInspection(result); })
      .catch(reason => { if (inspectionGeneration.current === generation) setError(reason instanceof Error ? reason.message : 'Method details are unavailable.'); })
      .finally(() => { if (inspectionGeneration.current === generation) setInspectionPendingId(null); });
  };

  return <section className="method-library" aria-label="Method library">
    <h2>{view === 'workflows' ? 'Workflows' : view === 'skills' ? 'Skills' : 'Legacy methods'}</h2>
    <details className="method-library-menu">
      <summary>Library</summary>
      <div role="group" aria-label="Library views">
        <button type="button" aria-pressed={view === 'workflows'} onClick={() => setView('workflows')}>Workflows</button>
        <button type="button" aria-pressed={view === 'skills'} onClick={() => setView('skills')}>Inspect skills</button>
        <button type="button" aria-pressed={view === 'legacy'} onClick={() => setView('legacy')}>Legacy methods</button>
      </div>
    </details>
    <label>Search<input type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder={view === 'skills' ? 'Search skills' : 'Search workflows'} /></label>
    {view === 'legacy' ? <p>Historical methods for compatibility and inspection.</p> : null}
    {loading ? <p role="status">Loading…</p> : null}
    {error ? <p role="alert">{error}</p> : null}
    {!loading && !error && visible.length === 0 ? <p>No matching methods.</p> : null}
    {!loading && !error ? groups.map(group => <section className="method-library-group" key={group.label} aria-labelledby={`method-group-${group.label.replace(/\W+/g, '-').toLowerCase()}`}>
      <h3 id={`method-group-${group.label.replace(/\W+/g, '-').toLowerCase()}`}>{group.label}</h3>
      <ul className="method-library-list">{group.methods.map(method => {
        const active = selected.some(item => sameMethod(item, method));
        const selectable = method.kind === 'workflow';
        return <MethodCard key={qualifiedMethodId(method)} method={method} active={active}
          inspectionPending={inspectionPendingId === qualifiedMethodId(method)} onInspect={() => openInspection(method)}
          onToggle={selectable ? () => onSelectedChange(active
            ? selected.filter(item => !sameMethod(item, method))
            : [...selected, { kind: method.kind, name: method.name, source: method.source, sourceRootId: method.sourceRootId }]) : undefined} />;
      })}</ul>
    </section>) : null}
    {inspection ? <article className="method-inspection" aria-label={`${inspection.method.name} method details`}>
      <h3>{inspection.method.name}</h3>
      <p>{inspection.method.description}</p>
      <details><summary>Technical details</summary><dl><dt>Source</dt><dd>{sourceLabel(inspection.method)} · {inspection.method.sourceRootId}</dd>
        <dt>Kind</dt><dd>{inspection.method.kind}</dd>
        <dt>Compatibility</dt><dd>{inspection.method.compatibility}</dd>
        <dt>Eligible roles</dt><dd>{inspection.method.executionRoleIds.join(', ') || 'None recorded'}</dd></dl></details>
      <details><summary>Read instructions</summary><pre>{inspection.entrypoint.content}</pre><small>SHA-256 {inspection.entrypoint.sha256}</small></details>
      {inspection.resources.length ? <details><summary>Included resources</summary><ul>{inspection.resources.map(resource => <li key={resource.path}>{resource.path} · {resource.sha256}</li>)}</ul></details> : null}
    </article> : null}
  </section>;
}
