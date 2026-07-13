import Hero from "../components/Hero";
import Highlights from "../components/Highlights";
import About from "../pages/About";
import Projects from "../pages/Projects";
import Contact from "../pages/Contact";

function Home() {
    return (
        <>
            <Hero />

            <Highlights />

            <About />

            <Projects />

            <Contact />
        </>
    );
}

export default Home;