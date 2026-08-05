import { API_URL } from "./config";

export async function streamMessage(
  tool: string,
  data: string | Record<string, unknown>,
  onChunk: (chunk: string) => void,
) {
  const payload =
    typeof data === "string"
      ? {
          tool,
          message: data, // Backwards compatibility
        }
      : {
          tool,
          data,
        };

  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Failed to connect to backend.");
  }

  if (!response.body) {
    throw new Error("Streaming is not supported.");
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();

    if (done) break;

    onChunk(decoder.decode(value));
  }
}
