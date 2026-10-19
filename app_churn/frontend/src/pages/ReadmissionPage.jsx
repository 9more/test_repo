import { useState } from "react";

function ReadmissionPage() {
  const [encounterId, setEncounterId] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();

    setResult(null);
    setError("");

    if (
      !encounterId ||
      !Number.isInteger(Number(encounterId)) ||
      Number(encounterId) <= 0
    ) {
      setError("Please enter a valid encounter ID.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/predict`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          model: "readmission",
          encounter_id: Number(encounterId),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Prediction request failed.");
      }

      setResult(data);
    } catch (error) {
      console.error("Readmission prediction error:", error);

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
        <h1>Hospital Readmission Prediction</h1>
        <p>
          Estimate the likelihood of a patient being readmitted using
          information associated with a hospital encounter.
        </p>
      </div>

      <div className="prediction-card">
        <h2>Run a prediction</h2>
        <p>
          Enter a hospital encounter ID to retrieve the stored encounter
          features and generate a readmission prediction.
        </p>

        <form onSubmit={handleSubmit}>
          <label htmlFor="encounterId">Hospital Encounter ID</label>

          <input
            id="encounterId"
            type="number"
            min="1"
            step="1"
            value={encounterId}
            onChange={(event) => setEncounterId(event.target.value)}
            placeholder="e.g. 1"
            required
          />

          <button type="submit" disabled={loading}>
            {loading ? "Generating prediction..." : "Predict readmission"}
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
                ? "Readmission predicted"
                : "No readmission predicted"}
            </span>
          </div>

          <div className="result-metrics">
            <div className="result-metric">
              <p>Predicted class</p>
              <h3>{result.prediction}</h3>
            </div>

            <div className="result-metric">
              <p>Readmission probability</p>
              <h3>{result.probability_percentage}</h3>
            </div>

            <div className="result-metric">
              <p>Decision threshold</p>
              <h3>{(result.threshold * 100).toFixed(0)}%</h3>
            </div>
          </div>

          <p className="result-note">
            This result is based on the model's estimated probability and
            configured decision threshold. It is a model prediction, not a
            clinical diagnosis.
          </p>
        </div>
      )}
    </section>
  );
}

export default ReadmissionPage;
