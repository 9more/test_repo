import Hero from "./components/Hero";
import Biography from "./components/Biography";
import Research from "./components/Research";
import Navbar from "./components/Navbar";
import Layout from "./components/Layout";
import "./App.css";

function App() {
    return (
        <>
            <Navbar/>

            <Hero
                name="Dr Jane Smith"
                title="Senior Lecturer in Economics"
                research="Labour Economics • Public Policy • Development Economics"
                description="Researching labour markets, economic growth and evidence-based public policy."
            />

            <Layout>
                <section className="biography">

                    <div className="container">

                         <Biography/>

                    </div>

                </section>

                <Research/>

            </Layout>

        </>
    );
}

export default App;