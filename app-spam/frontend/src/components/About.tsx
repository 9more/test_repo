import { portfolio } from "../data/portfolio";
import { skills } from "../data/skills";

function About() {
  return (
    <section id="about" className="container py-5">

      <div className="row">

        <div className="col-lg-12">

          <h2 className="fw-bold mb-4">
            About Me
          </h2>

          <p className="lead">
            {portfolio.summary}
          </p>

          <p className="mb-5">
            My focus is on building practical machine learning
            solutions that move from experimentation to deployment,
            combining data science, software engineering,
            cloud technologies and economic research.
          </p>

        </div>

      </div>

      <div className="row g-4">

        {skills.map((group) => (

          <div
            key={group.category}
            className="col-lg-4 col-md-6"
          >

            <div className="card h-100 shadow-sm border-0">

              <div className="card-body">

                <h5 className="card-title mb-3">
                  {group.category}
                </h5>

                <div className="d-flex flex-wrap gap-2">

                  {group.skills.map((skill) => (

                    <span
                      key={skill}
                      className="badge bg-primary"
                    >
                      {skill}
                    </span>

                  ))}

                </div>

              </div>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}

export default About;