import { describe, expect, it } from 'vitest';
import { CHAT_SECTION } from '../../lib/shell/loop-first';

describe('loop-first routing helpers', () => {
  it('exposes the CHAT section constant', () => {
    expect(CHAT_SECTION).toBe('CHAT');
  });
});
