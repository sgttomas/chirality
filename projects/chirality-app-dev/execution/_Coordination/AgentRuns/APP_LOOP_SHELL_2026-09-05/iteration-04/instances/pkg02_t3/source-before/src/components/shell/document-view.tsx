'use client';

import { useEffect, useMemo, useState } from 'react';
import { resolveDocumentViewState } from '../../lib/shell/document-view-state';
import { useWorkspace } from '../workspace/workspace-provider';
import { ChatMarkdown } from './chat-markdown';

type Deliverable = {
  id: string;
  name: string;
  pkg: string;
  status: string;
  path: string;
};

type DeliverablesResponse = {
  deliverables?: Deliverable[];
  deliverableContracts?: Array<{
    path: string;
    selectedProductionDocuments: Array<{ fileName: string }>;
  }>;
  error?: { message?: string };
};

type ContentResponse = {
  content?: string;
  file?: string;
  error?: { message?: string };
};

// The well-known deliverable document files (see the knowledge buckets in
// `lib/workspace/filesystem.ts`). `_STATUS.md` is always present; the rest are
// offered so the viewer can open whichever the deliverable contains. A missing
// file simply surfaces the endpoint's 404.
const CONTROL_PLANE_DOCUMENT_FILES = [
  '_STATUS.md',
  '_CONTEXT.md',
  '_REFERENCES.md',
  '_DEPENDENCIES.md',
  '_SEMANTIC.md',
  'MEMORY.md'
];

const DEFAULT_FILE = '_STATUS.md';

export function DocumentView(): JSX.Element {
  const { projectRoot } = useWorkspace();
  const [deliverables, setDeliverables] = useState<Deliverable[]>([]);
  const [canonicalDocumentsByPath, setCanonicalDocumentsByPath] = useState<
    Record<string, string[]>
  >({});
  const [rosterLoading, setRosterLoading] = useState(false);
  const [rosterError, setRosterError] = useState<string | null>(null);
  const [selectedPath, setSelectedPath] = useState<string>('');
  const [selectedFile, setSelectedFile] = useState<string>(DEFAULT_FILE);

  const [content, setContent] = useState<string | null>(null);
  const [contentLoading, setContentLoading] = useState(false);
  const [contentError, setContentError] = useState<string | null>(null);

  // Load the deliverable roster whenever the Working Root changes.
  useEffect(() => {
    let cancelled = false;
    setDeliverables([]);
    setCanonicalDocumentsByPath({});
    setRosterError(null);
    setSelectedPath('');
    setContent(null);
    setContentError(null);

    if (!projectRoot) {
      setRosterLoading(false);
      return () => {
        cancelled = true;
      };
    }

    setRosterLoading(true);

    async function loadRoster(): Promise<void> {
      try {
        const response = await fetch(
          `/api/project/deliverables?projectRoot=${encodeURIComponent(projectRoot as string)}`
        );
        const payload = (await response.json()) as DeliverablesResponse;
        if (cancelled) {
          return;
        }
        if (!response.ok || !payload.deliverables) {
          throw new Error(payload.error?.message ?? 'Unable to load deliverables.');
        }
        setDeliverables(payload.deliverables);
        setCanonicalDocumentsByPath(
          Object.fromEntries(
            (payload.deliverableContracts ?? []).map((contract) => [
              contract.path,
              contract.selectedProductionDocuments.map((file) => file.fileName)
            ])
          )
        );
        setSelectedPath(payload.deliverables[0]?.path ?? '');
      } catch (error) {
        if (cancelled) {
          return;
        }
        setRosterError(error instanceof Error ? error.message : 'Unable to load deliverables.');
      } finally {
        if (!cancelled) {
          setRosterLoading(false);
        }
      }
    }

    void loadRoster();
    return () => {
      cancelled = true;
    };
  }, [projectRoot]);

  // Fetch the selected document content.
  useEffect(() => {
    let cancelled = false;
    if (!projectRoot || !selectedPath) {
      setContent(null);
      setContentError(null);
      setContentLoading(false);
      return () => {
        cancelled = true;
      };
    }

    async function loadContent(): Promise<void> {
      setContentLoading(true);
      setContentError(null);
      try {
        const response = await fetch(
          `/api/working-root/deliverable/content?projectRoot=${encodeURIComponent(
            projectRoot as string
          )}&deliverablePath=${encodeURIComponent(selectedPath)}&file=${encodeURIComponent(
            selectedFile
          )}`
        );
        const payload = (await response.json()) as ContentResponse;
        if (cancelled) {
          return;
        }
        if (!response.ok || typeof payload.content !== 'string') {
          throw new Error(payload.error?.message ?? 'Unable to load document.');
        }
        setContent(payload.content);
      } catch (error) {
        if (cancelled) {
          return;
        }
        setContent(null);
        setContentError(error instanceof Error ? error.message : 'Unable to load document.');
      } finally {
        if (!cancelled) {
          setContentLoading(false);
        }
      }
    }

    void loadContent();
    return () => {
      cancelled = true;
    };
  }, [projectRoot, selectedPath, selectedFile]);

  const documentFiles = useMemo(
    () => [
      CONTROL_PLANE_DOCUMENT_FILES[0],
      ...(canonicalDocumentsByPath[selectedPath] ?? []),
      ...CONTROL_PLANE_DOCUMENT_FILES.slice(1)
    ],
    [canonicalDocumentsByPath, selectedPath]
  );

  const body = useMemo(() => {
    const state = resolveDocumentViewState({
      hasProjectRoot: Boolean(projectRoot),
      rosterLoading,
      rosterError,
      deliverableCount: deliverables.length,
      contentLoading,
      contentError,
      hasContent: content !== null
    });

    switch (state.kind) {
      case 'no-root':
        return <p className="panel-empty">Select a Working Root to view deliverable documents.</p>;
      case 'roster-loading':
        return <p className="panel-empty">Loading deliverables...</p>;
      case 'roster-error':
        return <p className="panel-error">{state.message}</p>;
      case 'empty':
        return <p className="panel-empty">No deliverables found in this Working Root.</p>;
      case 'content-loading':
        return <p className="panel-empty">Loading document...</p>;
      case 'content-error':
        return <p className="panel-error">{state.message}</p>;
      case 'content':
        return <ChatMarkdown source={content as string} />;
      case 'idle':
      default:
        return <p className="panel-empty">Select a deliverable and document to preview.</p>;
    }
  }, [projectRoot, rosterLoading, rosterError, deliverables, contentLoading, contentError, content]);

  return (
    <aside className="panel panel--document">
      <header className="panel-header">
        <h2>Document</h2>
        {deliverables.length > 0 ? (
          <div className="document-view-controls">
            <label className="document-view-selector">
              <span>Deliverable</span>
              <select
                value={selectedPath}
                onChange={(event) => {
                  setSelectedPath(event.target.value);
                  setSelectedFile(DEFAULT_FILE);
                }}
              >
                {deliverables.map((deliverable) => (
                  <option key={deliverable.path} value={deliverable.path}>
                    {deliverable.id} — {deliverable.name}
                  </option>
                ))}
              </select>
            </label>
            <label className="document-view-selector">
              <span>File</span>
              <select
                value={selectedFile}
                onChange={(event) => {
                  setSelectedFile(event.target.value);
                }}
              >
                {documentFiles.map((file) => (
                  <option key={file} value={file}>
                    {file}
                  </option>
                ))}
              </select>
            </label>
          </div>
        ) : null}
      </header>
      <div className="panel-body document-view-body">{body}</div>
    </aside>
  );
}
