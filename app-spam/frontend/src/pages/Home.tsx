import Hero from "../components/Hero";
import Highlights from "../components/Highlights";

import Projects from "./Projects";
import About from "./About";
import Experience from "./Experience";
import Contact from "./Contact";

function Home() {
    return (
        <>
            <Hero />

            <Highlights />

            <Projects />

            <About />

            <Experience />

            <Contact />
        </>
    );
}

export default Home;