function Hero() {
    return (
        <section className="hero">

            <div className="container">

                <div className="row align-items-center">

                    <div className="col-lg-10">

                        <h1 className="hero-title">
                            Imoh Ekpenyong
                        </h1>

                        <h2 className="hero-subtitle">
                            Data Scientist • Machine Learning Engineer • Economist
                        </h2>

                        <p className="hero-location">
                            <i className="bi bi-geo-alt-fill me-2"></i>
                            United Kingdom
                        </p>

                        <p className="hero-description">
                            Building practical machine learning and analytics
                            solutions by combining data science, econometrics,
                            business intelligence and cloud technologies.
                            Experienced in transforming complex data into
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

                            <a
                                href="#about"
                                className="btn btn-outline-light btn-lg"
                            >
                                About Me
                            </a>

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

                </div>

            </div>

        </section>
    );
}

export default Hero;