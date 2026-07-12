import { portfolio } from "../data/portfolio";

function About() {
  return (
    <section id="about" className="container py-5">

      <div className="row">

        <div className="col-lg-8">

          <h2 className="fw-bold mb-4">
            About Me
          </h2>

          <p className="lead">
            {portfolio.summary}
          </p>

          <p>
            My focus is on building practical machine learning
            solutions that move from experimentation to deployment,
            combining data science, software engineering, and cloud
            technologies.
          </p>

        </div>

      </div>


      <div className="mt-4">

        <h4 className="mb-3">
          Technology Stack
        </h4>


        {portfolio.technologies.map((tech) => (

          <span
            key={tech}
            className="badge bg-primary fs-6 me-2 mb-2"
          >
            {tech}
          </span>

        ))}


      </div>

    </section>
  );
}

export default About;