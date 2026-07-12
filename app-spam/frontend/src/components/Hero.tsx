import { Link } from "react-router-dom";

function Hero() {
    return (
        <section className="hero">
            <div className="container">

                <div className="row align-items-center">

                    <div className="col-lg-8">

                        <h1 className="hero-title">
                            Imoh Ekpenyong
                        </h1>

                        <h2 className="hero-subtitle">
                            Machine Learning Engineer • Data Scientist • Economist
                        </h2>

                        <p className="hero-location">
                            <i className="bi bi-geo-alt-fill me-2"></i>
                            United Kingdom
                        </p>

                        <p className="hero-description">
                            Building intelligent, data-driven solutions using
                            Machine Learning, Deep Learning, Econometrics,
                            Business Intelligence and Cloud Technologies.
                            Passionate about transforming complex data into
                            actionable insights through scalable and
                            production-ready applications.
                        </p>

                        <div className="d-flex flex-wrap gap-3">

                            <a
                                href="#projects"
                                className="btn btn-primary btn-lg"
                            >
                                View Projects
                            </a>

                            <Link
                                to="/about"
                                className="btn btn-outline-light btn-lg"
                            >
                                About Me
                            </Link>

                            <a
                                href="/Imoh_Ekpenyong_CV.pdf"
                                className="btn btn-outline-primary btn-lg"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                Download CV
                            </a>

                        </div>

                    </div>

                    <div className="col-lg-4 text-center mt-5 mt-lg-0">

                        <div className="card shadow-lg">

                            <div className="card-body p-4">

                                <h4 className="mb-4">
                                    Technology Stack
                                </h4>

                                <div className="d-flex flex-wrap justify-content-center gap-2">

                                    <span className="badge bg-primary">Python</span>
                                    <span className="badge bg-primary">SQL</span>
                                    <span className="badge bg-primary">Scikit-learn</span>
                                    <span className="badge bg-primary">PyTorch</span>
                                    <span className="badge bg-primary">spaCy</span>
                                    <span className="badge bg-primary">MLflow</span>
                                    <span className="badge bg-primary">Flask</span>
                                    <span className="badge bg-primary">React</span>
                                    <span className="badge bg-primary">TypeScript</span>
                                    <span className="badge bg-primary">Power BI</span>
                                    <span className="badge bg-primary">DAX</span>
                                    <span className="badge bg-primary">Azure</span>
                                    <span className="badge bg-primary">Fabric</span>
                                    <span className="badge bg-primary">Docker</span>

                                </div>

                            </div>

                        </div>

                    </div>

                </div>

            </div>
        </section>
    );
}

export default Hero;