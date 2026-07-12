import { projects } from "../data/projects";
import ProjectCard from "./ProjectCard";

function Projects() {

    return (

        <section
            id="projects"
            className="container py-5"
        >

            <h2 className="fw-bold mb-5">

                Machine Learning Portfolio

            </h2>

            <div className="row">

                {projects
                    .filter(project => !project.featured)
                    .map(project => (

                        <ProjectCard
                            key={project.id}
                            project={project}
                        />

                    ))}

            </div>

        </section>

    );

}

export default Projects;