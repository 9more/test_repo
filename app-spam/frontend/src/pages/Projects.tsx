import FeaturedProject from "../components/FeaturedProject";
import ProjectSection from "../components/ProjectSection";

function Projects() {
    return (
        <section id="projects" className="py-5">

            <div className="container mb-5">

                <h2 className="fw-bold">
                    Projects
                </h2>

                <p className="text-secondary">
                    A selection of machine learning, business intelligence and
                    economics projects demonstrating end-to-end analytical,
                    modelling and deployment workflows.
                </p>

            </div>

            <FeaturedProject />

            <ProjectSection
                title="Machine Learning Projects"
                category="Machine Learning"
            />

            <ProjectSection
                title="Business Intelligence Projects"
                category="Business Intelligence"
            />

            <ProjectSection
                title="Research Projects"
                category="Research"
            />

        </section>
    );
}

export default Projects;