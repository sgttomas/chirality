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

function sameMethod(left: QualifiedMethodReference, right: QualifiedMethodReference): boolean {
  return left.kind === right.kind && left.name === right.name && left.source === right.source && left.sourceRootId === right.sourceRootId;
}

export function MethodLibraryView({ projectRoot, selected, onSelectedChange, refresh = 0 }: {
  projectRoot: string;
  selected: readonly QualifiedMethodReference[];
  onSelectedChange: (methods: QualifiedMethodReference[]) => void;
  refresh?: number;
}): JSX.Element {
  const [query, setQuery] = useState('');
  const [methods, setMethods] = useState<MethodDescriptor[]>([]);
  const [inspection, setInspection] = useState<MethodInspectionResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const inspectionGeneration = useRef(0);
  const runtimeEpoch = useRuntimeEpoch();

  useEffect(() => {
    const controller = new AbortController();
    inspectionGeneration.current += 1;
    setInspection(null); setMethods([]); setLoading(true); setError(null);
    const timer = setTimeout(() => {
      void listMethods(projectRoot, query, controller.signal)
        .then(result => { if (!controller.signal.aborted) setMethods([...result.methods]); })
        .catch(reason => { if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : 'The method catalog is unavailable.'); })
        .finally(() => { if (!controller.signal.aborted) setLoading(false); });
    }, query ? 150 : 0);
    return () => { clearTimeout(timer); controller.abort(); };
  }, [projectRoot, query, refresh, runtimeEpoch]);

  const ordered = useMemo(() => [...methods].sort((a, b) => Number(b.central) - Number(a.central) || a.name.localeCompare(b.name)), [methods]);
  const openInspection = (method: MethodDescriptor): void => {
    const generation = inspectionGeneration.current + 1;
    inspectionGeneration.current = generation;
    setError(null); setInspection(null);
    void inspectMethod(projectRoot, method)
      .then(result => { if (inspectionGeneration.current === generation) setInspection(result); })
      .catch(reason => { if (inspectionGeneration.current === generation) setError(reason instanceof Error ? reason.message : 'Method details are unavailable.'); });
  };
  return <section className="method-library" aria-label="Method library">
    <p className="woven-eyebrow">Skills and workflows</p>
    <h2>Method library</h2>
    <p>Choose a method, then add your directions in the message.</p>
    <label>Search methods<input type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="Search skills and workflows" /></label>
    {loading ? <p role="status">Loading methods…</p> : null}
    {error ? <p role="alert">{error}</p> : null}
    {!loading && !error && ordered.length === 0 ? <p>No matching methods are available.</p> : null}
    <ul className="method-library-list">
      {ordered.map(method => {
        const active = selected.some(item => sameMethod(item, method));
        return <li key={qualifiedMethodId(method)}>
          <div><strong>{method.name}</strong>{method.central ? <small> Central</small> : null}</div>
          <p>{method.description}</p>
          <p><small>{method.kind} · {method.source}{method.compatibility === 'legacy' ? ' · legacy compatibility' : ''}</small></p>
          <div>
            <button type="button" onClick={() => openInspection(method)}>Inspect</button>
            <button type="button" aria-pressed={active} onClick={() => onSelectedChange(active
              ? selected.filter(item => !sameMethod(item, method))
              : [...selected, { kind: method.kind, name: method.name, source: method.source, sourceRootId: method.sourceRootId }])}>
              {active ? 'Remove' : 'Use next message'}
            </button>
          </div>
        </li>;
      })}
    </ul>
    {inspection ? <article className="method-inspection" aria-label={`${inspection.method.name} method details`}>
      <h3>{inspection.method.name}</h3>
      <p>{inspection.method.description}</p>
      <dl><dt>Source</dt><dd>{inspection.method.source} · {inspection.method.sourceRootId}</dd>
        <dt>Compatibility</dt><dd>{inspection.method.compatibility}</dd>
        <dt>Eligible roles</dt><dd>{inspection.method.executionRoleIds.join(', ') || 'None recorded'}</dd></dl>
      <details><summary>Instructions</summary><pre>{inspection.entrypoint.content}</pre><small>SHA-256 {inspection.entrypoint.sha256}</small></details>
      {inspection.resources.length ? <details><summary>Resources</summary><ul>{inspection.resources.map(resource => <li key={resource.path}>{resource.path} · {resource.sha256}</li>)}</ul></details> : null}
    </article> : null}
  </section>;
}
