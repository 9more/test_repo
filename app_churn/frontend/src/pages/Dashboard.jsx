import { useEffect, useState } from "react";
import modelMetrics from "../data/modelMetrics";

function Dashboard() {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchPredictionHistory() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${import.meta.env.VITE_API_URL}/predictions/history?limit=5`,
        );

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.error || "Unable to load prediction history.");
        }

        setPredictions(data.predictions);
      } catch (error) {
        console.error("Prediction history error:", error);
        setError(
          error.message === "Failed to fetch"
            ? "Unable to reach the backend. Check that Flask is running."
            : error.message || "Unable to load prediction history.",
        );
      } finally {
        setLoading(false);
      }
    }

    fetchPredictionHistory();
  }, []);

  return (
    <main className="dashboard">
      <header className="dashboard-header">
        <div>
          <p className="eyebrow">MACHINE LEARNING OPERATIONS</p>
          <h1>
            Production <span>ML Platform</span>
          </h1>
          <p className="intro">
            Make predictions and explore real-world applications of machine
            learning for customer churn and hospital readmission.
          </p>
        </div>
      </header>

      <section className="model-grid">
        <article className="model-card churn-card">
          <div className="model-icon">CC</div>
          <h2>Customer Churn Prediction</h2>
          <p>
            Predict the probability of customer churn using machine learning.
          </p>

          <div className="model-meta">
            <span>Telecom dataset</span>
            <span>{modelMetrics.churn.model}</span>
          </div>

          <div className="model-performance">
            <h3>Model Evaluation Metrics</h3>

            <div className="metrics-grid">
              <div className="metric-item">
                <span>ROC-AUC</span>
                <strong>{modelMetrics.churn.metrics.rocAuc.toFixed(4)}</strong>
              </div>

              <div className="metric-item">
                <span>Accuracy</span>
                <strong>
                  {(modelMetrics.churn.metrics.accuracy * 100).toFixed(2)}%
                </strong>
              </div>

              <div className="metric-item">
                <span>Precision</span>
                <strong>
                  {(modelMetrics.churn.metrics.precision * 100).toFixed(2)}%
                </strong>
              </div>

              <div className="metric-item">
                <span>Recall</span>
                <strong>
                  {(modelMetrics.churn.metrics.recall * 100).toFixed(2)}%
                </strong>
              </div>

              <div className="metric-item">
                <span>F1-score</span>
                <strong>
                  {(modelMetrics.churn.metrics.f1Score * 100).toFixed(2)}%
                </strong>
              </div>
            </div>

            <p className="metrics-threshold">
              Threshold: {(modelMetrics.churn.threshold * 100).toFixed(0)}%
            </p>
          </div>
          <a href="/churn" className="model-button">
            Open Churn Prediction →
          </a>
        </article>

        <article className="model-card readmission-card">
          <div className="model-icon">HR</div>
          <h2>Hospital Readmission Prediction</h2>
          <p>Predict the risk of hospital readmission within 30 days.</p>

          <div className="model-meta">
            <span>Healthcare dataset</span>
            <span>{modelMetrics.readmission.model}</span>
          </div>

          <div className="model-performance">
            <h3>Model Evaluation Metrics</h3>

            <div className="metrics-grid">
              <div className="metric-item">
                <span>ROC-AUC</span>
                <strong>
                  {modelMetrics.readmission.metrics.rocAuc.toFixed(4)}
                </strong>
              </div>

              <div className="metric-item">
                <span>Accuracy</span>
                <strong>
                  {(modelMetrics.readmission.metrics.accuracy * 100).toFixed(2)}
                  %
                </strong>
              </div>

              <div className="metric-item">
                <span>Precision</span>
                <strong>
                  {(modelMetrics.readmission.metrics.precision * 100).toFixed(
                    2,
                  )}
                  %
                </strong>
              </div>

              <div className="metric-item">
                <span>Recall</span>
                <strong>
                  {(modelMetrics.readmission.metrics.recall * 100).toFixed(2)}%
                </strong>
              </div>

              <div className="metric-item">
                <span>F1-score</span>
                <strong>
                  {(modelMetrics.readmission.metrics.f1Score * 100).toFixed(2)}%
                </strong>
              </div>
            </div>

            <p className="metrics-threshold">
              Threshold: {(modelMetrics.readmission.threshold * 100).toFixed(0)}
              %
            </p>
          </div>
          <a href="/readmission" className="model-button">
            Open Readmission Prediction →
          </a>
        </article>
      </section>

      <section className="project-description">
        <h2>About the platform</h2>
        <p>
          This project demonstrates how machine learning models can be
          integrated into an application to generate predictions from stored
          customer and patient data. It combines model inference, a Flask API,
          and PostgreSQL persistence in one workflow.
        </p>
      </section>

      <section className="prediction-history">
        <div className="history-header">
          <div>
            <p className="eyebrow">RECENT ACTIVITY</p>
            <h2>Prediction History</h2>
            <p className="history-description">
              Review predictions generated by your machine learning models.
            </p>
          </div>

          <a href="/history" className="history-link">
            View all →
          </a>
        </div>

        {loading ? (
          <div className="history-empty">
            <p>Loading prediction history...</p>
          </div>
        ) : error ? (
          <div className="history-empty" role="alert">
            <h3>Unable to load history</h3>
            <p>{error}</p>
          </div>
        ) : predictions.length === 0 ? (
          <div className="history-empty">
            <div className="history-icon">↗</div>
            <h3>No recent predictions to display</h3>
            <p>
              Once you run a churn or readmission prediction, your recent
              activity will appear here.
            </p>
          </div>
        ) : (
          <div className="history-list">
            {predictions.map((item) => {
              const isChurn = item.model_name === "churn";
              const entityLabel = isChurn
                ? `Customer #${item.customer_id}`
                : `Encounter #${item.encounter_id}`;

              return (
                <article className="history-item" key={item.prediction_id}>
                  <div className="history-item-main">
                    <div className="history-icon">{isChurn ? "CC" : "HR"}</div>
                    <div>
                      <h3>
                        {isChurn ? "Customer Churn" : "Hospital Readmission"}
                      </h3>
                      <p>
                        {entityLabel} · Prediction #{item.prediction_id}
                      </p>
                    </div>
                  </div>

                  <div className="history-item-result">
                    <span
                      className={`result-badge ${
                        item.prediction === 1 ? "high-risk" : "low-risk"
                      }`}
                    >
                      {item.prediction === 1
                        ? isChurn
                          ? "Churn predicted"
                          : "Readmission predicted"
                        : isChurn
                          ? "No churn predicted"
                          : "No readmission predicted"}
                    </span>
                    <p>
                      Probability: {(Number(item.probability) * 100).toFixed(2)}
                      %
                    </p>
                    <p>
                      Threshold: {(Number(item.threshold) * 100).toFixed(0)}%
                    </p>
                  </div>
                </article>
              );
            })}
          </div>
        )}
      </section>
    </main>
  );
}

export default Dashboard;
