import { useState, useEffect, useRef, type FormEvent } from "react";
import { predictModel } from "../api";

type Props = {
  onClose: () => void;
};

export default function SpamForm({ onClose }: Props) {
  const [email, setEmail] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const resultRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (result) {
      resultRef.current?.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }, [result]);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();

    setLoading(true);
    setResult("");

    try {
      const prediction = await predictModel("spam", {
        message: email,
      });

      setResult(prediction);
    } catch (err) {
      console.error(err);
      setResult("Prediction failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="prediction-form">
      <h3>📧 Email Threat Detection</h3>

      <form onSubmit={handleSubmit}>
        <textarea
          rows={8}
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Paste an email..."
          disabled={loading}
          required
        />

        <button className="estimate-btn" type="submit" disabled={loading}>
          {loading ? "Analysing..." : "Detect Threat"}
        </button>
      </form>

      {result && (
        <div ref={resultRef} className="prediction-result">
          <h4>Prediction</h4>
          <p>{result}</p>
        </div>
      )}

      <button className="back-btn" type="button" onClick={onClose}>
        ← Back to Chat
      </button>
    </div>
  );
}
