import { Suspense } from 'react';
import { WovenDialogueRoute } from '../components/woven-dialogue/woven-dialogue-route';

export default function PortalPage(): JSX.Element {
  return (
    <Suspense fallback={<main className="shell">Loading...</main>}>
      <WovenDialogueRoute defaultSurface="dialogue" />
    </Suspense>
  );
}
