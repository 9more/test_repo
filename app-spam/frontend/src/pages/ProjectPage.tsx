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

            <div className="container py-4 text-center">

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

        <div className="container py-4 project-page">

            {/* Back Button */}

            <Link
                to="/"
                className="btn btn-outline-light mb-4"
            >
                ← Back to Projects
            </Link>

            {/* Header */}

            <div className="mb-4">

                <div className="d-flex flex-wrap gap-2 mb-3">

                    <span className="badge bg-primary">
                        {project.category}
                    </span>

                    <span
                        className={`badge ${
                            project.status === "Live"
                                ? "bg-success"
                                : "bg-warning text-dark"
                        }`}
                    >
                        {project.status}
                    </span>

                </div>

                <h1 className="fw-bold mb-3">
                    {project.title}
                </h1>

                <p className="lead text-secondary mb-0">
                    {project.description}
                </p>

            </div>

            {/* Overview */}

            <div className="mb-4">

                <h2 className="fw-bold mb-3">
                    Overview
                </h2>

                <p className="mb-0">
                    {project.overview}
                </p>

            </div>

            {/* Information Grid */}

            <div className="row g-4 mb-4">

                {/* Technology */}

                <div className="col-lg-6">

                    <div className="project-info-card p-4 h-100">

                        <h3 className="mb-3">
                            Technology Stack
                        </h3>

                        {project.technologies.map((tech) => (

                            <span
                                key={tech}
                                className="badge bg-dark border me-2 mb-2"
                            >
                                {tech}
                            </span>

                        ))}

                    </div>

                </div>

                {/* Results */}

                <div className="col-lg-6">

                    <div className="project-info-card p-4 h-100">

                        <h3 className="mb-3">
                            Results
                        </h3>

                        {project.metrics ? (

                            <div className="row">

                                {Object.entries(project.metrics).map(
                                    ([key, value]) => (

                                        <div
                                            key={key}
                                            className="col-6 mb-3"
                                        >

                                            <div className="metric-card p-2 text-center">

                                                <small className="text-secondary text-uppercase">

                                                    {key}

                                                </small>

                                                <h6 className="mt-2 mb-0">

                                                    {value}

                                                </h6>

                                            </div>

                                        </div>

                                    )
                                )}

                            </div>

                        ) : (

                            <p className="text-secondary mb-0">
                                Results currently being updated.
                            </p>

                        )}

                    </div>

                </div>

                {/* Workflow */}

                <div className="col-12">

                    <div className="project-info-card p-4">

                        <h3 className="mb-3">
                            Workflow
                        </h3>

                        <ol className="mb-0 ps-3">

                            {project.workflow.map((step) => (

                                <li
                                    key={step}
                                    className="mb-1"
                                >
                                    {step}
                                </li>

                            ))}

                        </ol>

                    </div>

                </div>

            </div>

            {/* Demo */}

            <div className="mb-4">

                <LiveDemo slug={project.slug} />

            </div>

            {/* Actions */}

            <div className="d-flex flex-wrap gap-3">

                <a
                    href={project.github}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-outline-light"
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

        </div>

    );
}

export default ProjectPage;