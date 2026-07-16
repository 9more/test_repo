import FeaturedProject from "../components/FeaturedProject";
import ProjectSection from "../components/ProjectSection";

function Projects() {
    return (
        <section id="projects">

            <FeaturedProject />

            <ProjectSection
                title="Machine Learning Projects"
                category="Machine Learning"
            />

            <ProjectSection
                title="Decision Analytics"
                category="Decision Analytics"
            />

            <ProjectSection
                title="Business Intelligence Projects"
                category="Business Intelligence"
            />

            <ProjectSection
                title="Research & Econometrics"
                category="Research"
            />

        </section>
    );
}

export default Projects;