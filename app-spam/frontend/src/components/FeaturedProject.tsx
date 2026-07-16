import { Link } from "react-router-dom";
import { projects } from "../data/projects";

function FeaturedProject() {
    const project = projects.find((p) => p.featured);

    if (!project) return null;

    return (
        <section className="container py-4">

            <div className="card project-card shadow-sm border-0">

                <div className="card-body p-4">

                    <div className="d-flex justify-content-between align-items-center mb-3">

                        <div>

                            <span className="badge bg-warning text-dark mb-2">
                                ⭐ Featured Project
                            </span>

                            <h2 className="fw-bold mb-1">
                                {project.title}
                            </h2>

                            <p className="text-secondary mb-0">
                                {project.description}
                            </p>

                        </div>

                        <span
                            className={`badge fs-6 ${
                                project.status === "Live"
                                    ? "bg-success"
                                    : "bg-warning text-dark"
                            }`}
                        >
                            {project.status}
                        </span>

                    </div>

                    <hr />

                    <p className="mb-4">

                        {project.overview}

                    </p>

                    <div className="mb-4">

                        {project.technologies.slice(0, 5).map((tech) => (

                            <span
                                key={tech}
                                className="badge bg-dark border me-2 mb-2"
                            >
                                {tech}
                            </span>

                        ))}

                    </div>

                    {project.metrics && (

                        <div className="row text-center mb-4">

                            {Object.entries(project.metrics).map(([key, value]) => (

                                <div
                                    key={key}
                                    className="col-6 col-md-3"
                                >

                                    <div className="metric-card p-3 rounded">

                                        <small className="text-secondary text-uppercase">

                                            {key}

                                        </small>

                                        <h5 className="fw-bold mb-0">

                                            {value}

                                        </h5>

                                    </div>

                                </div>

                            ))}

                        </div>

                    )}

                    <div className="d-flex flex-wrap gap-3">

                        <Link
                            to={`/projects/${project.slug}`}
                            className="btn btn-primary"
                        >
                            View Case Study
                        </Link>

                        <a
                            href={project.github}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="btn btn-outline-light"
                        >
                            GitHub Repository
                        </a>

                    </div>

                </div>

            </div>

        </section>
    );
}

export default FeaturedProject;