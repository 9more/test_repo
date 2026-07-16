import ProjectCard from "./ProjectCard";
import { projects } from "../data/projects";

type Props = {
    title: string;
    category: string;
};

function ProjectSection({ title, category }: Props) {

    const filteredProjects = projects.filter(
        (project) =>
            project.category === category &&
            !project.featured
    );

    if (filteredProjects.length === 0) {
        return null;
    }

    return (
        <section className="container py-5">

            <div className="mb-4">

                <h2 className="fw-bold">
                    {title}
                </h2>

            </div>

            <div className="row g-4">

                {filteredProjects.map((project) => (

                    <ProjectCard
                        key={project.id}
                        project={project}
                    />

                ))}

            </div>

        </section>
    );
}

export default ProjectSection;