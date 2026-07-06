/**
 * ScreenContext (D-PEC-17 rider 5): route + visible record ids ONLY — derived
 * from the router (route params), never scraped from the DOM. v1 context is
 * the route plus the route-param record (e.g. /p/1/deliverables/7 → one
 * deliverable record); list pages MAY publish visible ids later through the
 * optional usePublishScreenContext hook — no page file adopts it in v1
 * (recorded scope note in the D-PEC-17 packet). Everything the agent then
 * reads back goes through the API under the agent person's own visibility.
 */

import { createContext, useContext, useEffect, useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import { useLocation } from 'react-router-dom'

export interface ScreenRecord {
  recordType: string
  ref: string
  id: number
}

export interface ScreenContextValue {
  route: string
  records: ScreenRecord[]
}

const ScreenCtx = createContext<ScreenContextValue>({ route: '/', records: [] })
const PublishCtx = createContext<(records: ScreenRecord[] | null) => void>(() => {})

/** route-param records: the detail pages whose URL carries a record id */
const ROUTE_RECORDS: Array<{ re: RegExp; recordType: string }> = [
  { re: /^\/p\/\d+\/deliverables\/(\d+)$/, recordType: 'deliverable' },
  { re: /^\/p\/\d+\/packages\/(\d+)$/, recordType: 'package' },
]

export function ScreenContextProvider({ children }: { children: ReactNode }): JSX.Element {
  const loc = useLocation()
  const [published, setPublished] = useState<ScreenRecord[] | null>(null)
  // published ids never outlive the page that published them
  useEffect(() => { setPublished(null) }, [loc.pathname])
  const value = useMemo<ScreenContextValue>(() => {
    const derived: ScreenRecord[] = []
    for (const { re, recordType } of ROUTE_RECORDS) {
      const m = re.exec(loc.pathname)
      if (m) derived.push({ recordType, ref: `#${m[1]}`, id: Number(m[1]) })
    }
    return { route: loc.pathname, records: published ?? derived }
  }, [loc.pathname, published])
  return (
    <ScreenCtx.Provider value={value}>
      <PublishCtx.Provider value={setPublished}>{children}</PublishCtx.Provider>
    </ScreenCtx.Provider>
  )
}

export function useScreenContext(): ScreenContextValue {
  return useContext(ScreenCtx)
}

/**
 * Optional adoption hook for list pages (post-v1): publish the records
 * currently visible on screen. Unmounting clears the publication.
 */
export function usePublishScreenContext(records: ScreenRecord[]): void {
  const publish = useContext(PublishCtx)
  const key = JSON.stringify(records)
  useEffect(() => {
    publish(records)
    return () => publish(null)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [publish, key])
}
