import { projects } from "../data/projects";
import ProjectCard from "./ProjectCard";

type Props = {
    title: string;
    category: "Machine Learning" | "Business Intelligence" | "Research";
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

            <h2 className="fw-bold mb-4">
                {title}
            </h2>


            <div className="row">

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