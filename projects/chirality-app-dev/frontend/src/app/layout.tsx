import type { Metadata } from 'next';
import localFont from 'next/font/local';
import './globals.css';
import { WorkspaceProvider } from '../components/workspace/workspace-provider';
import { ToolkitProvider } from '../components/workspace/toolkit-provider';
import { DeliverablesProvider } from '../components/workspace/deliverables-provider';
import { HarnessEventsProvider } from '../components/workspace/harness-events-provider';
import { RuntimeConnectivityProvider } from '../components/shell/runtime-connectivity-provider';
import { WOVEN_WORKSPACE_STORAGE_KEY } from '../lib/woven-dialogue/woven-workspace-state';

// IBM Plex ships with the app: the woff2 files under `src/fonts/` are bundled
// by `next/font/local`, so the declared type identity resolves without any
// runtime network fetch (F-APP-1 untouched).
const plexSans = localFont({
  src: [
    { path: '../fonts/ibm-plex-sans-latin-400-normal.woff2', weight: '400', style: 'normal' },
    { path: '../fonts/ibm-plex-sans-latin-400-italic.woff2', weight: '400', style: 'italic' },
    { path: '../fonts/ibm-plex-sans-latin-500-normal.woff2', weight: '500', style: 'normal' },
    { path: '../fonts/ibm-plex-sans-latin-600-normal.woff2', weight: '600', style: 'normal' },
    { path: '../fonts/ibm-plex-sans-latin-700-normal.woff2', weight: '700', style: 'normal' }
  ],
  variable: '--font-sans',
  display: 'swap',
  fallback: ['Avenir Next', 'Segoe UI', 'system-ui', 'sans-serif']
});

const plexSerif = localFont({
  src: [
    { path: '../fonts/ibm-plex-serif-latin-400-normal.woff2', weight: '400', style: 'normal' },
    { path: '../fonts/ibm-plex-serif-latin-400-italic.woff2', weight: '400', style: 'italic' },
    { path: '../fonts/ibm-plex-serif-latin-600-normal.woff2', weight: '600', style: 'normal' }
  ],
  variable: '--font-serif',
  display: 'swap',
  fallback: ['Iowan Old Style', 'Palatino', 'Georgia', 'serif']
});

const plexMono = localFont({
  src: [
    { path: '../fonts/ibm-plex-mono-latin-400-normal.woff2', weight: '400', style: 'normal' },
    { path: '../fonts/ibm-plex-mono-latin-500-normal.woff2', weight: '500', style: 'normal' }
  ],
  variable: '--font-mono',
  display: 'swap',
  fallback: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace']
});

// Light is the persisted default (§3.1 rule 3). This stamp runs before first
// paint so a stored `dark`/`system` choice never flashes light first; it is
// deliberately tiny, defensive, and never throws.
const THEME_BOOTSTRAP_SCRIPT = `(function(){var d=document.documentElement;var t="light";try{var raw=window.localStorage.getItem(${JSON.stringify(
  WOVEN_WORKSPACE_STORAGE_KEY
)});if(raw){var parsed=JSON.parse(raw);if(parsed&&(parsed.theme==="dark"||parsed.theme==="system"||parsed.theme==="light")){t=parsed.theme;}}}catch(e){t="light";}d.setAttribute("data-theme",t);})();`;

export const metadata: Metadata = {
  title: 'Chirality Workflow Shell',
  description: 'PORTAL, PIPELINE, and WORKBENCH shell for local agent execution'
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${plexSans.variable} ${plexSerif.variable} ${plexMono.variable}`}
      data-theme="light"
      suppressHydrationWarning
    >
      <body>
        <script dangerouslySetInnerHTML={{ __html: THEME_BOOTSTRAP_SCRIPT }} />
        {/* Outermost so every runtime-backed pane below can depend on the
            reconnect epoch, and so the top bar and the data panes read one
            shared connectivity snapshot rather than two subscriptions that
            could disagree. */}
        <RuntimeConnectivityProvider>
          <WorkspaceProvider>
            <DeliverablesProvider>
              <ToolkitProvider>
                <HarnessEventsProvider>{children}</HarnessEventsProvider>
              </ToolkitProvider>
            </DeliverablesProvider>
          </WorkspaceProvider>
        </RuntimeConnectivityProvider>
      </body>
    </html>
  );
}
