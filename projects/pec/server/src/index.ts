/**
 * Server entrypoint: HTTP on PEC_PORT (default 4810), hourly notification sweep,
 * static hosting of the built web app (web/dist) in production.
 */

import { createServer } from 'node:http'
import { existsSync, readFileSync } from 'node:fs'
import { join, normalize } from 'node:path'
import { fileURLToPath } from 'node:url'
import { openDb } from './db.ts'
import { buildRouter } from './api.ts'
import { errorPayload, parseCookies, readBody, sendJson } from './http.ts'
import { sweepAll } from './services/sweep.ts'
import { withTx } from './db.ts'

const here = fileURLToPath(new URL('.', import.meta.url))
const DB_PATH = process.env.PEC_DB ?? join(here, '..', '..', 'pec.db')
const PORT = Number(process.env.PEC_PORT ?? 4810)
const WEB_DIST = join(here, '..', '..', 'web', 'dist')

const db = openDb(DB_PATH)
const router = buildRouter(db)

const MIME: Record<string, string> = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.ico': 'image/x-icon', '.woff2': 'font/woff2', '.map': 'application/json',
}

const server = createServer(async (req, res) => {
  const url = new URL(req.url ?? '/', 'http://localhost')
  try {
    const match = router.match(req.method ?? 'GET', url.pathname)
    if (match) {
      const body = await readBody(req)
      const result = await match.handler({
        req, res, method: req.method ?? 'GET', path: url.pathname,
        params: match.params, query: url.searchParams, body,
        cookies: parseCookies(req.headers.cookie),
      })
      if (!res.headersSent) {
        if (typeof result === 'string' && res.getHeader('content-type')) {
          res.end(result)
        } else {
          sendJson(res, 200, result ?? { ok: true })
        }
      } else {
        res.end(typeof result === 'string' ? result : JSON.stringify(result))
      }
      return
    }
    if (url.pathname.startsWith('/api/')) {
      sendJson(res, 404, { error: { code: 'NOT_FOUND', message: `no route: ${req.method} ${url.pathname}` } })
      return
    }
    // static web app (production build)
    if (existsSync(WEB_DIST)) {
      const rel = url.pathname === '/' ? '/index.html' : url.pathname
      const safe = normalize(rel).replace(/^(\.\.[/\\])+/, '')
      let file = join(WEB_DIST, safe)
      if (!file.startsWith(WEB_DIST) || !existsSync(file)) file = join(WEB_DIST, 'index.html') // SPA fallback
      const ext = file.slice(file.lastIndexOf('.'))
      res.writeHead(200, { 'content-type': MIME[ext] ?? 'application/octet-stream' })
      res.end(readFileSync(file))
      return
    }
    sendJson(res, 404, { error: { code: 'NOT_FOUND', message: 'web app not built; run npm run build (dev: use the Vite server on :4811)' } })
  } catch (e) {
    const { status, body } = errorPayload(e)
    if (!res.headersSent) sendJson(res, status, body)
    else res.end()
  }
})

server.listen(PORT, () => {
  console.log(`PEC server on http://localhost:${PORT} (db: ${DB_PATH})`)
})

// hourly working-day-aware notification sweep (SPEC §4 producers)
const sweep = () => {
  try {
    const n = withTx(db, () => sweepAll(db))
    if (n > 0) console.log(`sweep: ${n} notification(s)`)
  } catch (e) {
    console.error('sweep failed', e)
  }
}
sweep()
setInterval(sweep, 3600_000).unref()
