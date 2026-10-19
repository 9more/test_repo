function AboutPage() {
  return (
    <div className="info-page">
      <header className="info-page-header">
        <p className="eyebrow">ABOUT THE PROJECT</p>
        <h1>
          From Data to <span>Real-World Impact</span>
        </h1>
        <p className="info-intro">
          An end-to-end machine learning platform demonstrating how trained
          models can be deployed, accessed through APIs, and integrated into an
          interactive application.
        </p>
      </header>

      <section className="info-section">
        <h2>Project Overview</h2>
        <p>
          This platform brings together machine learning, backend API
          development, database integration and frontend engineering. Users can
          submit data to trained models, obtain predictions and review
          previously recorded prediction results.
        </p>
      </section>

      <section className="info-section">
        <h2>Machine Learning Models</h2>

        <div className="info-grid">
          <article className="info-card">
            <span className="info-tag">MODEL 01</span>
            <h3>Customer Churn Prediction</h3>
            <p>
              Uses a Random Forest model to estimate the likelihood of a
              telecommunications customer leaving a service.
            </p>
            <p className="info-tech">Algorithm: Random Forest</p>
          </article>

          <article className="info-card">
            <span className="info-tag">MODEL 02</span>
            <h3>Hospital Readmission Prediction</h3>
            <p>
              Uses an XGBoost model to estimate the likelihood of a patient's
              readmission within 30 days.
            </p>
            <p className="info-tech">Algorithm: XGBoost</p>
          </article>
        </div>
      </section>

      <section className="info-section">
        <h2>Technology Stack</h2>

        <div className="technology-list">
          <div>
            <strong>Frontend</strong>
            <span>React, Vite, CSS</span>
          </div>
          <div>
            <strong>Backend</strong>
            <span>Python, Flask, REST API</span>
          </div>
          <div>
            <strong>Database</strong>
            <span>PostgreSQL</span>
          </div>
          <div>
            <strong>Machine Learning</strong>
            <span>Scikit-learn, XGBoost</span>
          </div>
          <div>
            <strong>Deployment</strong>
            <span>Docker, Docker Compose</span>
          </div>
        </div>
      </section>

      <section className="info-section">
        <h2>End-to-End Workflow</h2>
        <div className="workflow-list">
          <span>Data preparation</span>
          <span>Model training</span>
          <span>API integration</span>
          <span>Predictions</span>
          <span>Database storage</span>
        </div>
      </section>

      <p className="info-disclaimer">
        The hospital readmission model is a demonstration project and is not
        intended for clinical decision-making.
      </p>
    </div>
  );
}

export default AboutPage;
