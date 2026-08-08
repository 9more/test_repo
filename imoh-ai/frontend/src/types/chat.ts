export type ChatMessage = {
  role: "user" | "assistant";
  content: string;
  showActions?: boolean;
  component?: "insurance";
};
