import { Link } from "react-router-dom";
import type { Project } from "../data/projects";

type Props = {
    project: Project;
};

function ProjectCard({ project }: Props) {
    return (
        <div className="col-lg-4 col-md-6 mb-4">

            <div className="card project-card h-100 shadow-sm border-0">

                <div className="card-body d-flex flex-column p-4">

                    {/* Header */}

                    <div className="d-flex justify-content-between align-items-start mb-3">

                        <div>

                            <span className="badge bg-primary mb-2">
                                {project.category}
                            </span>

                            <h4 className="fw-bold mb-1">
                                {project.title}
                            </h4>

                        </div>

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

                    {/* Description */}

                    <p className="text-secondary flex-grow-1 mb-3">
                        {project.description}
                    </p>

                    {/* Type */}

                    <small className="text-secondary mb-3">
                        <strong>Type:</strong> {project.type}
                    </small>

                    {/* Technologies */}

                    <div className="mb-4">

                        {project.technologies.slice(0, 4).map((tech) => (

                            <span
                                key={tech}
                                className="badge bg-dark border me-2 mb-2"
                            >
                                {tech}
                            </span>

                        ))}

                    </div>

                    {/* Buttons */}

                    <div className="d-grid gap-2 mt-auto">

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

        </div>
    );
}

export default ProjectCard;