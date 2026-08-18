import Hero from "../components/Hero";
import Biography from "../components/Biography";
import Research from "../components/Research";
import Publications from "../components/Publications";
import Teaching from "../components/Teaching";
import Contact from "../components/Contact";
import Layout from "../components/Layout";

function Home() {
    return (
        <>
            <Hero
                name="Dr Ikechukwu Ogbuagu"
                title="Senior Lecturer in Economics"
                research="Macroeconomic Modelling • Development Financing • SME Development"
                description="Economist and researcher working on macroeconomic modelling, development financing and small and medium enterprise development."
            />

            <Layout>
                <Biography />
                <Research />
                <Publications />
                <Teaching />
                <Contact />
            </Layout>
        </>
    );
}

export default Home;