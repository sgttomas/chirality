import { describe, expect, it, vi } from "vitest";
import { ViewportOwnershipLedger, ViewportResource } from "./viewportResource";

// The actual measurement hook with an inert renderer; no WebGL/geometry is mocked as measured evidence.
describe("viewport label measurement ownership", () => {
  it("accounts observers/listeners and disposes once whether owner or effect releases first", () => {
    const observers: Array<{ disconnect: ReturnType<typeof vi.fn> }> = [];
    class Observer {
      disconnect = vi.fn();
      observe = vi.fn();
      constructor(_callback: ResizeObserverCallback) { observers.push(this); }
    }
    vi.stubGlobal("ResizeObserver", Observer);
    const fonts = new EventTarget();
    const previousFonts = Object.getOwnPropertyDescriptor(document, "fonts");
    Object.defineProperty(document, "fonts", { configurable: true, value: fonts });
    try {
      const canvas = document.createElement("canvas");
      const plate = document.createElement("button");
      const ownership = new ViewportOwnershipLedger(90001);
      const disposers = new Set<() => void>();
      const resource = Object.assign(Object.create(ViewportResource.prototype), {
        disposed: false, renderer: { domElement: canvas }, ownership, labelMeasurementDisposers: disposers
      }) as ViewportResource;
      const invalidate = vi.fn();
      const stop = resource.observeLabelMeasurements([plate], invalidate);
      expect(ownership.snapshot().live.resizeObservers).toBe(1);
      expect(ownership.snapshot().live.eventBindings).toBe(1);
      fonts.dispatchEvent(new Event("loadingdone"));
      expect(invalidate).toHaveBeenCalledTimes(1);
      // This is the exact registered disposal route called by resource.dispose().
      for (const dispose of disposers) dispose();
      stop();
      expect(observers[0].disconnect).toHaveBeenCalledTimes(1);
      expect(ownership.snapshot().live.resizeObservers).toBe(0);
      expect(ownership.snapshot().live.eventBindings).toBe(0);
      fonts.dispatchEvent(new Event("loadingdone"));
      expect(invalidate).toHaveBeenCalledTimes(1);
      const stopAgain = resource.observeLabelMeasurements([plate], invalidate);
      stopAgain();
      for (const dispose of disposers) dispose();
      expect(observers[1].disconnect).toHaveBeenCalledTimes(1);
      Object.assign(resource, { disposed: true });
      resource.observeLabelMeasurements([plate], invalidate)();
      expect(observers).toHaveLength(2);
      expect(ownership.snapshot().live.resizeObservers).toBe(0);
    } finally {
      if (previousFonts) Object.defineProperty(document, "fonts", previousFonts);
      else Reflect.deleteProperty(document, "fonts");
      vi.unstubAllGlobals();
    }
  });
});
