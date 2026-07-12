import Hero from "../components/Hero";
import About from "../components/About";
import FeaturedProject from "../components/FeaturedProject";
import ProjectSection from "../components/ProjectSection";
import Architecture from "../components/Architecture";
import Contact from "../components/Contact";

function Home() {
    return (
        <>
            <Hero />

            <About />

            <FeaturedProject />

            <ProjectSection
                title="Machine Learning"
                category="Machine Learning"
            />

            <ProjectSection
                title="Business Intelligence"
                category="Business Intelligence"
            />

            <ProjectSection
                title="Research"
                category="Research"
            />

            <Architecture />

            <Contact />
        </>
    );
}

export default Home;