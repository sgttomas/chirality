import { describe, expect, it, vi } from "vitest";
import { OmlxClient, normalizeOmlxBaseUrl } from "@chirality/engine-pi-omlx";

const credentials = {
  async get(providerId: string) {
    return providerId === "omlx" ? "secret-key" : undefined;
  },
  async status(providerId: string) {
    return { configured: providerId === "omlx" };
  }
};

describe("oMLX control client", () => {
  it("is literal-loopback-only, authenticated, no-redirect, and parses exact status IDs", async () => {
    const fetchImpl = vi.fn(async (_input: RequestInfo | URL, init?: RequestInit) => {
      expect(init?.redirect).toBe("manual");
      expect((init?.headers as Record<string, string>).authorization).toBe("Bearer secret-key");
      return new Response(
        JSON.stringify({
          models: [
            {
              id: "mlx-community/Qwen3.6-35B-A3B-8bit",
              type: "llm",
              loaded: true,
              is_loading: false
            }
          ]
        }),
        { status: 200, headers: { "content-type": "application/json" } }
      );
    });
    const client = new OmlxClient({
      credentials,
      fetchImpl: fetchImpl as typeof fetch,
      baseUrl: "http://127.0.0.1:8123/v1"
    });
    expect((await client.listStatus())[0]?.id).toBe(
      "mlx-community/Qwen3.6-35B-A3B-8bit"
    );
    expect(String(fetchImpl.mock.calls[0]?.[0])).toBe(
      "http://127.0.0.1:8123/v1/models/status"
    );
    expect(() => normalizeOmlxBaseUrl("http://localhost:8000/v1")).toThrow();
    expect(() => normalizeOmlxBaseUrl("https://127.0.0.1:8000/v1")).toThrow();
    expect(() => normalizeOmlxBaseUrl("http://user:pass@127.0.0.1:8000/v1")).toThrow();
  });

  it("rejects redirects before following them", async () => {
    const client = new OmlxClient({
      credentials,
      fetchImpl: vi.fn(async () => new Response(null, { status: 302 })) as typeof fetch
    });
    await expect(client.listStatus()).rejects.toMatchObject({
      code: "OMLX_PROTOCOL_FAILURE"
    });
  });
});
