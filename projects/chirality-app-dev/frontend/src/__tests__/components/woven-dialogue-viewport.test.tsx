import React, { useEffect } from 'react';
import { act, create, type ReactTestRenderer } from 'react-test-renderer';
import { describe, expect, it, vi } from 'vitest';
import { DialogueViewport } from '../../components/woven-dialogue/dialogue-viewport';

describe('Woven Dialogue viewport', () => {
  it('keeps the primary dialogue mounted while replay and focused surfaces change', () => {
    let mounted = 0;
    let unmounted = 0;
    const onReturn = vi.fn();

    function Primary(): JSX.Element {
      useEffect(() => {
        mounted += 1;
        return () => {
          unmounted += 1;
        };
      }, []);
      return <div data-controller="primary">Primary controller</div>;
    }

    let renderer!: ReactTestRenderer;
    act(() => {
      renderer = create(
        <DialogueViewport primaryDialogue={<Primary />} onReturnToPrimary={onReturn} />
      );
    });
    expect(mounted).toBe(1);
    expect(unmounted).toBe(0);

    act(() => {
      renderer.update(
        <DialogueViewport
          primaryDialogue={<Primary />}
          replayLens={<section data-replay="selected">Replay</section>}
          onReturnToPrimary={onReturn}
        />
      );
    });
    expect(mounted).toBe(1);
    expect(unmounted).toBe(0);
    expect(
      renderer.root.findByProps({ 'data-primary-dialogue-mounted': 'true' }).props.hidden
    ).toBe(true);
    expect(renderer.root.findByProps({ 'data-replay': 'selected' })).toBeTruthy();

    act(() => {
      renderer.update(
        <DialogueViewport
          primaryDialogue={<Primary />}
          focusedSurface={{
            id: 'document',
            title: 'Artifacts',
            content: <div data-artifact="focused">Artifact</div>
          }}
          onReturnToPrimary={onReturn}
        />
      );
    });
    expect(mounted).toBe(1);
    expect(unmounted).toBe(0);
    expect(renderer.root.findByProps({ 'data-focused-surface': 'document' })).toBeTruthy();

    act(() => {
      renderer.unmount();
    });
    expect(unmounted).toBe(1);
  });

  it('offers a persistent return action for a focused surface', () => {
    const onReturn = vi.fn();
    const renderer = create(
      <DialogueViewport
        primaryDialogue={<div>Primary</div>}
        focusedSurface={{
          id: 'pipeline',
          title: 'Pipeline',
          content: <div>Pipeline intent</div>
        }}
        onReturnToPrimary={onReturn}
      />
    );

    const button = renderer.root.findByType('button');
    act(() => {
      button.props.onClick();
    });
    expect(onReturn).toHaveBeenCalledTimes(1);
  });
});
