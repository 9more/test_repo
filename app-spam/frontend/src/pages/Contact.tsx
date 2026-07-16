function Contact() {
    return (
        <section id="contact" className="container py-5">

            <div className="text-center mb-5">

                <h2 className="fw-bold">
                    Contact
                </h2>

                <p className="text-secondary">
                    Interested in collaborating, discussing opportunities,
                    machine learning projects, analytics solutions or research?
                </p>

            </div>

            <div className="row justify-content-center">

                <div className="col-lg-8">

                    <div className="contact-card p-4 text-center">

                        <h4 className="mb-4">

                            Let's Connect

                        </h4>

                        <div className="d-flex flex-wrap justify-content-center gap-3">

                            <a
                                href="imoh.ekpenyong@aol.com"
                                className="btn btn-primary"
                            >
                                <i className="bi bi-envelope-fill me-2"></i>
                                Email
                            </a>

                            <a
                                href="https://www.linkedin.com"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="btn btn-outline-light"
                            >
                                <i className="bi bi-linkedin me-2"></i>
                                LinkedIn
                            </a>

                            <a
                                href="https://github.com/9more/test_repo/tree/main/health_analysis"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="btn btn-outline-light"
                            >
                                <i className="bi bi-github me-2"></i>
                                GitHub
                            </a>

                            <a
                                href="/Imoh_Ekpenyong_CV.pdf"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="btn btn-outline-primary"
                            >
                                <i className="bi bi-file-earmark-person me-2"></i>
                                Download CV
                            </a>

                        </div>

                    </div>

                </div>

            </div>

        </section>
    );
}

export default Contact;