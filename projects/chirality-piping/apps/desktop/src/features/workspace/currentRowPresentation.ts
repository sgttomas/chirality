import { useCallback, useLayoutEffect, useRef, useState } from "react";
import type { EntityKey } from "./selectionState";
import type { ModelIndex } from "./modelIndex";

export type TableCurrentRow = Readonly<{ generation: string; rowKey: EntityKey | null }>;
export type CurrentRowPublication = TableCurrentRow & Readonly<{ source: "node-fields" | "node-review" }>;

function liveNode(key: EntityKey | null, index: ModelIndex | null | undefined): EntityKey | null {
  const entity = key ? index?.entities.get(key) : undefined;
  return entity?.ref.type === "node" && entity.anchor && !entity.geometryIssue && !index?.invalidGeometry.has(key!) ? key : null;
}

/** Presentation only: no selection, controller, or persistence ownership. */
export function useCurrentRowPresentation(generation: string, index: ModelIndex | null | undefined) {
  const [current, setCurrent] = useState<CurrentRowPublication | null>(null);
  const latest = useRef({ generation, index });
  latest.current = { generation, index };
  const publish = useCallback((publication: CurrentRowPublication) => {
    const live = latest.current;
    if (publication.generation !== live.generation) return;
    const rowKey = liveNode(publication.rowKey, live.index);
    setCurrent((previous) => {
      if (!rowKey) return previous?.source === publication.source ? null : previous;
      if (previous?.generation === publication.generation && previous.source === publication.source && previous.rowKey === rowKey) return previous;
      return { ...publication, rowKey };
    });
  }, []);
  const rowKey = current?.generation === generation ? liveNode(current.rowKey, index) : null;
  useLayoutEffect(() => { if (current && !rowKey) setCurrent((previous) => previous === current ? null : previous); }, [current, rowKey]);
  return { currentRowNodeKey: rowKey, publishCurrentRow: publish };
}
