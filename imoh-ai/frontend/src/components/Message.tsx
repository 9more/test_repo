import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import ActionButtons from "./ActionButtons";
import InsuranceForm from "./InsuranceForm";
import SpamForm from "./SpamForm";
import SentimentForm from "./SentimentForm";

export type WidgetType =
  | "spam"
  | "sentiment"
  | "insurance"
  | "diabetes"
  | "economic"
  | "risk";

export type ChatMessage = {
  role: "user" | "assistant";
  content: string;
  showActions?: boolean;
  component?: WidgetType;
};

type Props = {
  message: ChatMessage;
  onSelectTool: (tool: string) => void;
  onCloseWidget: () => void;
};

export default function Message({
  message,
  onSelectTool,
  onCloseWidget,
}: Props) {
  // ---------- Spam ----------
  if (message.component === "spam") {
    return (
      <div className="message assistant insurance-message">
        <SpamForm onClose={onCloseWidget} />
      </div>
    );
  }

  // ---------- Sentiment ----------
  if (message.component === "sentiment") {
    return (
      <div className="message assistant insurance-message">
        <SentimentForm onClose={onCloseWidget} />
      </div>
    );
  }

  // ---------- Insurance ----------
  if (message.component === "insurance") {
    return (
      <div className="message assistant insurance-message">
        <InsuranceForm onClose={onCloseWidget} />
      </div>
    );
  }

  // ---------- Normal Chat ----------
  return (
    <div className={`message ${message.role}`}>
      {message.role === "assistant" ? (
        <>
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {message.content}
          </ReactMarkdown>

          {message.showActions && (
            <ActionButtons
              actions={[
                {
                  tool: "spam",
                  label: "🛡️ Launch Email Threat Detection",
                },
                {
                  tool: "sentiment",
                  label: "😊 Launch Sentiment Analysis",
                },
                {
                  tool: "insurance",
                  label: "🏥 Launch Insurance Analytics",
                },
                {
                  url: "https://imoh-ml-portfoliovercelapp.vercel.app",
                  label: "🌐 Open Interactive ML Portfolio",
                },
              ]}
              onSelectTool={onSelectTool}
            />
          )}
        </>
      ) : (
        message.content
      )}
    </div>
  );
}
