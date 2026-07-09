/**
 * App shell: auth gate, project scope, sidebar with the six role homes (PRD §3),
 * global raise-an-item, notifications. Routes per SPEC §9.
 */

import { StrictMode, useCallback, useEffect, useState } from 'react'
import { createRoot } from 'react-dom/client'
import {
  BrowserRouter, NavLink, Navigate, Outlet, Route, Routes, useLocation, useNavigate, useParams,
} from 'react-router-dom'
import './styles.css'
import { api, p } from './api.ts'
import type { Me, ProjectRef } from './api.ts'
import { AppContext, ExplainProvider, useApp, useLoad } from './shared.tsx'
import { RaiseItemButton } from './RaiseItem.tsx'
import { ScreenContextProvider } from './agent/context.tsx'
import { AgentDock } from './agent/AgentPanel.tsx'
import { OverviewPage } from './pages/Overview.tsx'
import { PackagesPage, PackageDetailPage } from './pages/Packages.tsx'
import { DisciplinesPage, DisciplineDetailPage } from './pages/Disciplines.tsx'
import { DeliverablesPage, DeliverableDetailPage } from './pages/Deliverables.tsx'
import { LogPage } from './pages/LogHome.tsx'
import { MyWeekPage } from './pages/MyWeek.tsx'
import { RegistersPage } from './pages/Registers.tsx'
import { PlanPage } from './pages/Plan.tsx'
import { AdminPage } from './pages/Admin.tsx'

function LoginPage({ onLogin }: { onLogin(me: Me, projects: ProjectRef[]): void }): JSX.Element {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)
  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await api.post('/api/auth/login', { email, password })
      const me = await api.get('/api/auth/me')
      onLogin(me.me, [...me.projects, ...me.allProjects.filter((a: ProjectRef) => !me.projects.some((x: ProjectRef) => x.id === a.id))])
    } catch (err: any) {
      setError(err.message)
    }
  }
  return (
    <div className="login-wrap">
      <form className="card login-card stack" onSubmit={submit}>
        <h1>PEC — Project Execution Control</h1>
        <p className="section-note">One record system. Six ways to look at it.</p>
        <label>Email<input value={email} onChange={(e) => setEmail(e.target.value)} autoFocus /></label>
        <label>Password<input type="password" value={password} onChange={(e) => setPassword(e.target.value)} /></label>
        {error && <div className="error-box">{error}</div>}
        <button className="btn">Sign in</button>
      </form>
    </div>
  )
}

function Shell({ me, projects, onLogout }: { me: Me; projects: ProjectRef[]; onLogout(): void }): JSX.Element {
  const { pid } = useParams()
  const navigate = useNavigate()
  const location = useLocation()
  const [people, setPeople] = useState<AppContextPeople>([])
  const [refreshKey, setRefreshKey] = useState(0)
  const [toastMsg, setToastMsg] = useState<string | null>(null)
  const [unread, setUnread] = useState(0)

  const projectId = Number(pid)
  const project = projects.find((x) => x.id === projectId)

  useEffect(() => { api.get('/api/people').then(setPeople).catch(() => {}) }, [])
  useEffect(() => {
    if (!projectId) return
    const load = () => api.get(p(projectId, 'notifications?unread=true'))
      .then((n) => setUnread(n.length)).catch(() => {})
    load()
    const t = setInterval(load, 60_000)
    return () => clearInterval(t)
  }, [projectId, refreshKey])

  const toast = useCallback((msg: string) => {
    setToastMsg(msg)
    setTimeout(() => setToastMsg(null), 4000)
  }, [])

  if (!project) return <Navigate to="/" replace />

  const switchProject = (nextProjectId: string) => {
    const nextPath = location.pathname.replace(/^\/p\/[^/]+/, `/p/${nextProjectId}`)
    navigate(`${nextPath}${location.search}${location.hash}`)
  }

  return (
    <AppContext.Provider value={{
      me, projects, pid: projectId, people,
      refreshKey, refresh: () => setRefreshKey((k) => k + 1), toast,
    }}>
      <ExplainProvider>
        {/* D-PEC-17: screen-context = route + visible record ids only (rider 5) */}
        <ScreenContextProvider>
        <div className="app">
          <aside className="sidebar">
            <div className="brand">
              PEC<small>{project.code} — {project.name}</small>
            </div>
            <nav aria-label="Primary">
              <div className="nav-group">
                <div className="nav-label">Work lenses</div>
                <NavLink to={`/p/${projectId}/overview`}>Overview</NavLink>
                <NavLink to={`/p/${projectId}/packages`}>Packages</NavLink>
                <NavLink to={`/p/${projectId}/disciplines`}>Disciplines</NavLink>
                <NavLink to={`/p/${projectId}/deliverables`}>Deliverables</NavLink>
                <NavLink to={`/p/${projectId}/plan`}>Plan</NavLink>
                <NavLink to={`/p/${projectId}/log`}>Action &amp; Hold Log</NavLink>
                <NavLink to={`/p/${projectId}/my-week`}>
                  My Week{unread > 0 && <span className="notif-dot">{unread}</span>}
                </NavLink>
              </div>
              <div className="nav-group nav-group-controls">
                <div className="nav-label">Control surfaces</div>
                <NavLink to={`/p/${projectId}/registers`}>Registers</NavLink>
                <NavLink to={`/p/${projectId}/admin`}>Admin</NavLink>
              </div>
            </nav>
            <div className="grow" />
            <div className="userbox">
              <b>{me.name}</b>
              {projects.length > 1 && (
                <select
                  value={projectId}
                  onChange={(e) => switchProject(e.target.value)}
                  aria-label="Project"
                >
                  {projects.map((pr) => <option key={pr.id} value={pr.id}>{pr.code}</option>)}
                </select>
              )}
              <button className="signout" type="button" onClick={onLogout}>Sign out</button>
            </div>
          </aside>
          <main className="main">
            <div className="topbar">
              <div className="spacer" />
              {/* D-PEC-17: agent panel toggle — renders only when can('agent.direct') */}
              <AgentDock />
              <RaiseItemButton />
            </div>
            <Outlet />
          </main>
          {toastMsg && <div className="toast">{toastMsg}</div>}
        </div>
        </ScreenContextProvider>
      </ExplainProvider>
    </AppContext.Provider>
  )
}

type AppContextPeople = Array<{ id: number; name: string; email: string; discipline: string | null }>

function ProjectPicker({ projects }: { projects: ProjectRef[] }): JSX.Element {
  if (projects.length === 1) return <Navigate to={`/p/${projects[0]!.id}/overview`} replace />
  return (
    <div className="login-wrap">
      <div className="card login-card">
        <h1>Select project</h1>
        {projects.map((pr) => (
          <p key={pr.id}><a href={`/p/${pr.id}/overview`}>{pr.code} — {pr.name}</a></p>
        ))}
        {projects.length === 0 && <p className="muted">You are not assigned to any project.</p>}
      </div>
    </div>
  )
}

function Root(): JSX.Element {
  const [session, setSession] = useState<{ me: Me; projects: ProjectRef[] } | null | 'loading'>('loading')

  useEffect(() => {
    api.get('/api/auth/me')
      .then((r) => setSession({
        me: r.me,
        projects: [...r.projects, ...r.allProjects.filter((a: ProjectRef) => !r.projects.some((x: ProjectRef) => x.id === a.id))],
      }))
      .catch(() => setSession(null))
  }, [])

  if (session === 'loading') return <div className="login-wrap"><p className="muted">loading…</p></div>
  if (!session) return <LoginPage onLogin={(me, projects) => setSession({ me, projects })} />

  const logout = async () => { await api.post('/api/auth/logout'); setSession(null) }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ProjectPicker projects={session.projects} />} />
        <Route path="/p/:pid" element={<Shell me={session.me} projects={session.projects} onLogout={logout} />}>
          <Route path="overview" element={<OverviewPage />} />
          <Route path="packages" element={<PackagesPage />} />
          <Route path="packages/:id" element={<PackageDetailPage />} />
          <Route path="disciplines" element={<DisciplinesPage />} />
          <Route path="disciplines/:name" element={<DisciplineDetailPage />} />
          <Route path="deliverables" element={<DeliverablesPage />} />
          <Route path="deliverables/:id" element={<DeliverableDetailPage />} />
          <Route path="plan" element={<PlanPage />} />
          <Route path="log" element={<LogPage />} />
          <Route path="my-week" element={<MyWeekPage />} />
          <Route path="registers" element={<RegistersPage />} />
          <Route path="registers/:tab" element={<RegistersPage />} />
          <Route path="admin" element={<AdminPage />} />
          <Route path="admin/:section" element={<AdminPage />} />
          <Route index element={<Navigate to="overview" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Root />
  </StrictMode>,
)
