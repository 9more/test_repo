import { useState } from "react";

function ChurnPage() {
  const [customerId, setCustomerId] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();

    setResult(null);
    setError("");

    if (
      !customerId ||
      !Number.isInteger(Number(customerId)) ||
      Number(customerId) <= 0
    ) {
      setError("Please enter a valid customer ID.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          model: "churn",
          customer_id: Number(customerId),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Prediction request failed.");
      }

      setResult(data);
    } catch (error) {
      console.error("Churn prediction error:", error);

      setError(
        error.message === "Failed to fetch"
          ? "Unable to reach the backend. Check that Flask is running and the API URL is correct."
          : error.message ||
              "Something went wrong while generating the prediction.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="prediction-page">
      <div className="page-header">
        <p className="page-eyebrow">PREDICTION MODEL</p>
        <h1>Customer Churn Prediction</h1>
        <p>
          Estimate whether a customer is likely to leave a service using the
          trained machine learning model.
        </p>
      </div>

      <div className="prediction-card">
        <h2>Run a prediction</h2>
        <p>
          Enter a customer ID to retrieve the stored customer features and
          generate a churn prediction.
        </p>

        <form onSubmit={handleSubmit}>
          <label htmlFor="customerId">Customer ID</label>

          <input
            id="customerId"
            type="number"
            min="1"
            step="1"
            value={customerId}
            onChange={(event) => setCustomerId(event.target.value)}
            placeholder="e.g. 1"
            required
          />

          <button type="submit" disabled={loading}>
            {loading ? "Generating prediction..." : "Predict churn"}
          </button>
        </form>

        {error && (
          <p className="prediction-error" role="alert">
            {error}
          </p>
        )}
      </div>

      {result && (
        <div className="prediction-result">
          <div className="result-header">
            <div>
              <p className="page-eyebrow">RESULT</p>
              <h2>Prediction complete</h2>
            </div>

            <span
              className={`result-badge ${
                result.prediction === 1 ? "high-risk" : "low-risk"
              }`}
            >
              {result.prediction === 1
                ? "Churn predicted"
                : "Churn not predicted"}
            </span>
          </div>

          <div className="result-metrics">
            <div className="result-metric">
              <p>Predicted class</p>
              <h3>{result.prediction}</h3>
            </div>

            <div className="result-metric">
              <p>Churn probability</p>
              <h3>{result.probability_percentage}</h3>
            </div>

            <div className="result-metric">
              <p>Decision threshold</p>
              <h3>{(result.threshold * 100).toFixed(0)}%</h3>
            </div>
          </div>

          <p className="result-note">
            This result reflects the model's estimated probability and
            configured decision threshold. It is a prediction, not a guarantee
            of customer behaviour.
          </p>
        </div>
      )}
    </section>
  );
}

export default ChurnPage;
