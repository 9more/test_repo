import { Link } from "react-router-dom";
import type { Project } from "../data/projects";

type Props = {
    project: Project;
};

function ProjectCard({ project }: Props) {
    return (
        <div className="col-lg-4 col-md-6 mb-4">
            <div className="card project-card h-100 shadow-sm">

                <div className="card-body d-flex flex-column">

                    {/* Status */}

                    <div className="d-flex justify-content-between align-items-center mb-3">

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

                    {/* Title */}

                    <h4 className="fw-bold mb-3">

                        {project.title}

                    </h4>

                    {/* Description */}

                    <p className="text-secondary flex-grow-1">

                        {project.description}

                    </p>

                    {/* Project Type */}

                    <p className="small mb-3">

                        <strong>Type:</strong> {project.type}

                    </p>

                    {/* Technologies */}

                    <div className="mb-4">

                        {project.technologies.map((tech) => (

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
                            to={`/projects/${project.id}`}
                            className="btn btn-primary"
                        >
                            View Project
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