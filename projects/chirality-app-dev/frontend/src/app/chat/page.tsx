import { Suspense } from 'react';
import { LoopShell } from '../../components/shell/loop-shell';

export default function ChatPage(): JSX.Element {
  return (
    <Suspense fallback={<main className="shell">Loading direct chat...</main>}>
      <LoopShell />
    </Suspense>
  );
}
