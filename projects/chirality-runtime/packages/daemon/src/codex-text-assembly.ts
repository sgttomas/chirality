/** Ordered append-only native text projection. Later items wait for earlier completion. */
export class CodexTextAssembly {
  private readonly emitted = new Map<string, number>();
  text = "";
  flush(items: ReadonlyMap<string, { text: string; completed: boolean }>, terminal = false): string {
    let delta = "";
    for (const [id, item] of items) {
      const offset = this.emitted.get(id) ?? 0;
      if (item.text.length > offset) {
        delta += (offset === 0 && (this.text.length > 0 || delta.length > 0) ? "\n\n" : "") + item.text.slice(offset);
        this.emitted.set(id, item.text.length);
      }
      if (!terminal && !item.completed) break;
    }
    this.text += delta;
    return delta;
  }
}
