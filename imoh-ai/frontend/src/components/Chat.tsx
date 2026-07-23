import { useState } from "react";
import { sendMessage } from "../api";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function Chat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);

  async function handleSubmit() {
    if (!message.trim()) return;

    const userMessage = message;

    try {
      const data = await sendMessage(userMessage);

      setMessages((prev) => [
        ...prev,
        {
          role: "user",
          content: userMessage,
        },
        {
          role: "assistant",
          content: data.response,
        },
      ]);

      setMessage("");
    } catch (error) {
      console.error("Failed to send message:", error);
    }
  }

  return (
    <div className="chat-container">
      <div className="background">
        <div className="blob blob-1"></div>
        <div className="blob blob-2"></div>
        <div className="blob blob-3"></div>
      </div>
      <h1 className="title">Imoh AI</h1>

      <p className="subtitle">AI Engineer | Machine Learning Engineer</p>

      <div className="suggestions">
        <div
          className="prompt-card"
          onClick={() => setMessage("Tell me about your NLP projects")}
        >
          <h3>📚 NLP Projects</h3>
          <p>Spam Detection & Sentiment Analysis</p>
        </div>

        <div
          className="prompt-card"
          onClick={() =>
            setMessage("Tell me about your machine learning projects")
          }
        >
          <h3>🤖 ML Projects</h3>
          <p>Predictive Models & Analytics</p>
        </div>

        <div
          className="prompt-card"
          onClick={() => setMessage("What technologies do you use?")}
        >
          <h3>🛠 Skills</h3>
          <p>Python, SQL, Power BI & AI</p>
        </div>
      </div>

      <div className="chat-layout">
        <div className="messages">
          {messages.length === 0 && (
            <div className="empty-state">
              Ask me about:
              <br />
              • Machine Learning
              <br />
              • NLP Projects
              <br />
              • Data Science
              <br />• AI Engineering
            </div>
          )}

          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              {msg.content}
            </div>
          ))}
        </div>

        <div className="input-panel">
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask me anything..."
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSubmit();
              }
            }}
          />

          <button onClick={handleSubmit}>Send</button>
        </div>
      </div>
    </div>
  );
}
