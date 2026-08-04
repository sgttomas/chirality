import { RuntimeError } from "@chirality/runtime-contracts";
export class EngineRegistry {
    engines = new Map();
    register(engine) {
        const key = this.key(engine.descriptor.adapterId, engine.descriptor.providerId);
        if (this.engines.has(key))
            throw new Error(`Engine already registered: ${key}`);
        this.engines.set(key, engine);
    }
    resolve(selection) {
        const engine = this.engines.get(this.key(selection.adapterId, selection.providerId));
        if (engine === undefined) {
            throw new RuntimeError("ENGINE_UNAVAILABLE", `Engine ${selection.adapterId}/${selection.providerId} is unavailable`, 503);
        }
        return engine;
    }
    descriptors() {
        return [...this.engines.values()].map((engine) => engine.descriptor);
    }
    key(adapterId, providerId) {
        return `${adapterId}\0${providerId}`;
    }
}
