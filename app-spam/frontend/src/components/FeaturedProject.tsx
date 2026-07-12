import SpamForm from "./SpamForm";

function FeaturedProject() {
  return (
    <section id="featured-project" className="container py-5">
      <div className="row align-items-center">

        {/* Left Column */}
        <div className="col-lg-5 mb-4">

          <h2 className="fw-bold mb-4">
            Featured Project
          </h2>

          <h3 className="text-primary">
            Spam Email Detection
          </h3>

          <p className="lead">
            This application demonstrates an end-to-end machine learning
            workflow for classifying emails as <strong>Spam</strong> or
            <strong> Not Spam</strong>. It combines natural language
            processing, supervised machine learning, a REST API, and a
            responsive web interface into a production-ready solution.
          </p>

          <h5 className="mt-4">Key Features</h5>

          <ul className="list-group">

            <li className="list-group-item">
              ✅ Text preprocessing using NLP
            </li>

            <li className="list-group-item">
              ✅ TF-IDF Vectorisation
            </li>

            <li className="list-group-item">
              ✅ Logistic Regression Classifier
            </li>

            <li className="list-group-item">
              ✅ Flask REST API
            </li>

            <li className="list-group-item">
              ✅ React + TypeScript Frontend
            </li>

            <li className="list-group-item">
              ✅ Docker & AWS Ready
            </li>

          </ul>

        </div>

        {/* Right Column */}

        <div className="col-lg-7">

          <SpamForm />

        </div>

      </div>
    </section>
  );
}

export default FeaturedProject;