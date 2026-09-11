'use client';

import React, { createContext, useContext, useMemo, type ReactNode } from 'react';
import type { HostedModelCatalogEntry, HostedModelSelection } from '@chirality/runtime-contracts';
import type { HostedBootstrapStatusResponse } from './hosted-bootstrap-client';

/**
 * Read-only view of the single hosted-bootstrap controller instance owned by
 * the shell frame. Surfaces rendered inside the frame (the chat panel's model
 * and reasoning selectors) consume it without a second controller or a second
 * status poll. Outside a provider the value reads as "not signed in".
 */
export type HostedBootstrapContextValue = {
  snapshot: HostedBootstrapStatusResponse | null;
  loading: boolean;
};

/** The authenticated Codex catalog as exposed by Runtime status while admission is ready. */
export type HostedModelCatalogView = {
  models: readonly HostedModelCatalogEntry[];
  selection: HostedModelSelection;
};

const HostedBootstrapContext = createContext<HostedBootstrapContextValue>({ snapshot: null, loading: false });

export function HostedBootstrapProvider({ snapshot, loading, children }: HostedBootstrapContextValue & { children: ReactNode }): JSX.Element {
  const value = useMemo(() => ({ snapshot, loading }), [snapshot, loading]);
  return <HostedBootstrapContext.Provider value={value}>{children}</HostedBootstrapContext.Provider>;
}

export function useHostedBootstrap(): HostedBootstrapContextValue {
  return useContext(HostedBootstrapContext);
}

/**
 * The catalog is usable only while the account is signed in and the engine is
 * admitted; Runtime publishes `models`/`selection` together in exactly that
 * state. Any other snapshot yields null so the selectors stay disabled rather
 * than offering a stale or empty list.
 */
export function selectHostedModelCatalog(snapshot: HostedBootstrapStatusResponse | null): HostedModelCatalogView | null {
  if (snapshot?.registration !== 'registered') return null;
  const { status } = snapshot;
  if (status.ceremony !== 'signed-in' || status.admission !== 'ready') return null;
  if (!status.models || status.models.length === 0 || !status.selection) return null;
  return { models: status.models, selection: status.selection };
}

/** True when the pair names a catalog model and one of that model's supported efforts. */
export function isSelectionInCatalog(catalog: HostedModelCatalogView, selection: HostedModelSelection | null | undefined): selection is HostedModelSelection {
  if (!selection) return false;
  const entry = catalog.models.find(model => model.model === selection.model);
  return Boolean(entry && entry.supportedReasoningEfforts.includes(selection.reasoningEffort));
}
