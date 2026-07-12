import { useParams, Link } from "react-router-dom";
import { projects } from "../data/projects";
import LiveDemo from "../components/LiveDemo";

function ProjectPage() {
    const { slug } = useParams();

    const project = projects.find(
        (p) => p.slug === slug
    );

    if (!project) {
        return (
            <div className="container py-5 text-center">
                <h2>Project not found</h2>

                <Link
                    to="/"
                    className="btn btn-primary mt-3"
                >
                    Back Home
                </Link>
            </div>
        );
    }

    return (
        <div className="container py-5">

            {/* Icon */}

            <div className="display-2 text-primary mb-3">
                <i className={`bi ${project.icon}`}></i>
            </div>

            {/* Title */}

            <h1 className="fw-bold">

                {project.title}

            </h1>

            <p className="lead text-secondary">

                {project.description}

            </p>

            <hr className="my-5" />

            {/* Overview */}

            <section className="mb-5">

                <h2>Overview</h2>

                <p>

                    {project.overview}

                </p>

            </section>

            {/* Tech Stack */}

            <section className="mb-5">

                <h2>Technology Stack</h2>

                <div>

                    {project.technologies.map((tech) => (

                        <span
                            key={tech}
                            className="badge bg-dark me-2 mb-2"
                        >

                            {tech}

                        </span>

                    ))}

                </div>

            </section>

            {/* Workflow */}

            <section className="mb-5">

                <h2>Workflow</h2>

                <ol>

                    {project.workflow.map((step) => (

                        <li key={step}>

                            {step}

                        </li>

                    ))}

                </ol>

            </section>
            
            <LiveDemo slug={project.slug} />

            {/* Metrics */}

            {project.metrics && (

                <section className="mb-5">

                    <h2>Model Performance</h2>

                    <div className="row">

                        {Object.entries(project.metrics).map(([key, value]) => (

                            <div
                                key={key}
                                className="col-md-3 mb-3"
                            >

                                <div className="card bg-dark text-white">

                                    <div className="card-body text-center">

                                        <h5>

                                            {key.toUpperCase()}

                                        </h5>

                                        <h3>

                                            {value}

                                        </h3>

                                    </div>

                                </div>

                            </div>

                        ))}

                    </div>

                </section>

            )}

            {/* Future */}

            <section className="mb-5">

                <h2>Future Improvements</h2>

                <ul>

                    {project.futureImprovements.map((item) => (

                        <li key={item}>

                            {item}

                        </li>

                    ))}

                </ul>

            </section>

            {/* GitHub */}

            <a
                href={project.github}
                target="_blank"
                rel="noreferrer"
                className="btn btn-outline-primary me-3"
            >

                GitHub Repository

            </a>

            <Link
                to="/"
                className="btn btn-primary"
            >

                Back Home

            </Link>

        </div>
    );
}

export default ProjectPage;