'use client';

import { useRouter, useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import type { AgentRosterEntry } from '../../lib/harness/agent-roster';
import { harnessApiErrorMessage, listDirectChatPersonas } from '../../lib/harness/client';
import { buildDirectChatHref } from '../../lib/shell/loop-first';
import { resolvePersona } from '../../lib/shell/persona-resolution';

type PersonaPickerProps = {
  buildHref?: (persona: string) => string;
  disabled?: boolean;
  onPersonaSelected?: (persona: string) => void;
};

/**
 * Direct-chat persona picker (D-APP-24). Lists Type-0/Type-1 personas only
 * (server-filtered via `listDirectChatPersonas`); selecting one drives the
 * surface by setting `?agent=`, which `chat-panel`'s route-free `resolvePersona`
 * already consumes to boot the chosen persona on the next turn. Type-2 task
 * agents are never offered — they run only via orchestration.
 */
export function PersonaPicker({
  buildHref = buildDirectChatHref,
  disabled = false,
  onPersonaSelected
}: PersonaPickerProps): JSX.Element {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [personas, setPersonas] = useState<AgentRosterEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    listDirectChatPersonas()
      .then((agents) => {
        if (!cancelled) {
          setPersonas(agents);
          setLoadError(null);
        }
      })
      .catch((error) => {
        if (!cancelled) {
          setLoadError(harnessApiErrorMessage(error));
        }
      })
      .finally(() => {
        if (!cancelled) {
          setLoading(false);
        }
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const selected = resolvePersona(searchParams.get('agent'));
  const selectedInRoster = personas.some((persona) => persona.name === selected);

  return (
    <div className="persona-picker">
      <label htmlFor="persona-picker-select">Persona</label>
      <select
        id="persona-picker-select"
        value={loading ? '' : selected}
        disabled={disabled || loading || personas.length === 0}
        onChange={(event) => {
          const persona = event.target.value;
          router.replace(buildHref(persona));
          onPersonaSelected?.(persona);
        }}
      >
        {loading ? <option value="">Loading personas…</option> : null}
        {/* A `?agent=` that is not a Type-0/Type-1 persona (e.g. a hand-edited
            URL) is shown disabled so the control stays controlled without
            silently offering a non-direct-chat agent. */}
        {!loading && !selectedInRoster ? (
          <option value={selected} disabled>
            {selected} (unavailable)
          </option>
        ) : null}
        {personas.map((persona) => (
          <option key={persona.name} value={persona.name}>
            {persona.name}
            {persona.type === 0 ? ' · Type 0' : ' · Type 1'}
          </option>
        ))}
      </select>
      {loadError ? (
        <p className="persona-picker-error" role="alert">
          {loadError}
        </p>
      ) : null}
    </div>
  );
}
