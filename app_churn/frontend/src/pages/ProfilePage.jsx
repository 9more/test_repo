function ProfilePage() {
  return (
    <div className="info-page">
      <header className="info-page-header">
        <p className="eyebrow">MY PROFILE</p>
        <h1>
          Imoh <span>Ekpenyong</span>
        </h1>
        <p className="info-intro">
          Data Scientist and Economist with an interest in applying quantitative
          methods, machine learning and software engineering to practical
          problems.
        </p>

        <div className="profile-page-links">
          <a
            href="https://github.com/9more/test_repo"
            target="_blank"
            rel="noreferrer"
          >
            GitHub ↗
          </a>
          <a
            href="https://www.linkedin.com/in/imoh-ekpenyong-95983045/"
            target="_blank"
            rel="noreferrer"
          >
            LinkedIn ↗
          </a>
        </div>
      </header>

      <section className="info-section">
        <h2>About Me</h2>
        <p>
          My work combines economic analysis, data science and machine learning.
          I am interested in building practical applications that take
          analytical models beyond experimentation and make their outputs
          accessible through usable software.
        </p>
      </section>

      <section className="info-section">
        <h2>Technical Skills</h2>

        <div className="skill-groups">
          <article className="info-card">
            <h3>Data Science & ML</h3>
            <div className="skill-tags">
              <span>Python</span>
              <span>Scikit-learn</span>
              <span>XGBoost</span>
              <span>Pandas</span>
              <span>Model Evaluation</span>
            </div>
          </article>

          <article className="info-card">
            <h3>Application Development</h3>
            <div className="skill-tags">
              <span>Flask</span>
              <span>REST APIs</span>
              <span>React</span>
              <span>SQL</span>
              <span>PostgreSQL</span>
              <span>Docker</span>
            </div>
          </article>

          <article className="info-card">
            <h3>Analytics & Economics</h3>
            <div className="skill-tags">
              <span>Econometrics</span>
              <span>Statistical Analysis</span>
              <span>Data Visualisation</span>
              <span>Policy Analysis</span>
            </div>
          </article>
        </div>
      </section>

      <section className="info-section" id="projects">
        <h2>Featured Projects</h2>
        <a
          className="project-link"
          href="https://imoh-ml.dev"
          target="_blank"
          rel="noreferrer"
        >
          Explore project ↗
        </a>

        <div className="info-grid">
          <article className="info-card">
            <h3>Imoh AI</h3>
            <p>
              An AI assistant project exploring language models, LangChain and
              retrieval-augmented generation.
            </p>
          </article>
          <article className="info-card">
            <h3>Production ML Platform</h3>
            <p>
              Deploying machine learning models through a Flask API, React
              interface and PostgreSQL-backed prediction history.
            </p>
          </article>
        </div>
      </section>
    </div>
  );
}

export default ProfilePage;
