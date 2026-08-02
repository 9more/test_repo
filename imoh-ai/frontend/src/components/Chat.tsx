import { useState, useEffect, useRef } from "react";
import { streamMessage } from "../api";
import { FaGithub } from "react-icons/fa";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import ActionButtons from "./ActionButtons";

type Message = {
  role: "user" | "assistant";
  content: string;
  showActions?: boolean;
};

export default function Chat() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [tool, setTool] = useState("gemini"); // <-- NEW
  const demoMessages: Record<string, string> = {
    spam: `🛡️ **Email Threat Detection**

Paste an email below and I'll classify it as:

• Ham
• Spam
• Phishing`,

    sentiment: `😊 **Sentiment Analysis**

Paste a customer review below.

I'll classify it as:

• Positive
• Negative`,
  };

  const prompts = [
    "Ask me about NLP projects",
    "Ask me about Machine Learning",
    "Ask me about AI Engineering",
    "Ask me about Data Analytics",
    "Ask me about Power BI projects",
    "Ask me about my portfolio",
  ];

  const [placeholderIndex, setPlaceholderIndex] = useState(0);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const interval = setInterval(() => {
      setPlaceholderIndex((prev) => (prev + 1) % prompts.length);
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  async function handleSubmit() {
    if (!message.trim()) return;

    const userMessage = message;
    setMessage("");

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
      {
        role: "assistant",
        content: "",
        showActions: true,
      },
    ]);

    try {
      const activeTool = tool;

      await streamMessage(activeTool, userMessage, (chunk) => {
        setMessages((prev) => {
          const updated = [...prev];

          updated[updated.length - 1] = {
            ...updated[updated.length - 1],
            content: updated[updated.length - 1].content + chunk,
          };

          return updated;
        });
      });

      // Automatically return to Gemini after one prediction
      if (activeTool !== "gemini") {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content: `✅ ${
              activeTool === "spam" ? "Email" : "Sentiment"
            } analysed successfully.

You can continue asking me about my projects, skills, or experience, or launch another live demo.`,
            showActions: false,
          },
        ]);

        setTool("gemini");
      }
    } catch (error) {
      console.error("Failed to send message:", error);

      setMessages((prev) => {
        const updated = [...prev];

        updated[updated.length - 1] = {
          role: "assistant",
          content:
            "Sorry, something went wrong while contacting the AI service.",
          showActions: false,
        };

        return updated;
      });
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
          className="prompt-card github-card"
          onClick={() =>
            window.open(
              "https://github.com/9more/test_repo",
              "_blank",
              "noopener,noreferrer",
            )
          }
        >
          <h3 className="card-title">
            <FaGithub className="card-icon" />
            Explore My GitHub
          </h3>
          <p>Browse source code, projects & documentation</p>
        </div>

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
            setMessage("Tell me about your AI and Machine Learning projects")
          }
        >
          <h3>🤖 AI & ML Projects</h3>
          <p>Predictive Models & Analytics</p>
        </div>

        <div
          className="prompt-card"
          onClick={() =>
            setMessage("Tell me about your technical skills and experience")
          }
        >
          <h3>🛠 Skills & Experience</h3>
          <p>Python, SQL, Power BI & AI Engineering</p>
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
              {msg.role === "assistant" ? (
                <>
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>
                    {msg.content}
                  </ReactMarkdown>

                  {msg.showActions &&
                    (msg.content.includes("Email Threat Detection") ||
                      msg.content.includes("Sentiment Analysis")) && (
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
                            url: "https://imoh-ml-portfoliovercelapp.vercel.app",
                            label: "🌐 Open Interactive ML Portfolio",
                          },
                        ]}
                        onSelectTool={(selectedTool) => {
                          setTool(selectedTool);

                          setMessages((prev) => [
                            ...prev,
                            {
                              role: "assistant",
                              content:
                                demoMessages[
                                  selectedTool as keyof typeof demoMessages
                                ],
                              showActions: false,
                            },
                          ]);
                        }}
                      />
                    )}
                </>
              ) : (
                msg.content
              )}
            </div>
          ))}

          <div ref={messagesEndRef} />
        </div>

        <div className="input-panel">
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder={prompts[placeholderIndex]}
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
