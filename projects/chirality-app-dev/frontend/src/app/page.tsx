import { Suspense } from 'react';
import { PortalLoopShell } from '../components/shell/portal-loop-shell';

export default function PortalPage(): JSX.Element {
  return (
    <Suspense fallback={<main className="shell">Loading live loop portal...</main>}>
      <PortalLoopShell />
    </Suspense>
  );
}
