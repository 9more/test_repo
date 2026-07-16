import { experience } from "../data/experience";

function Experience() {
    return (
        <section id="experience" className="container py-5">

            <div className="text-center mb-5">

                <h2 className="fw-bold">
                    Professional Experience
                </h2>

                <p className="text-secondary">
                    Experience spanning data analysis, research, economics and operational analytics.
                </p>

            </div>

            <div className="row">

                {experience.map((job, index) => (

                    <div
                        key={index}
                        className="col-lg-12 mb-4"
                    >

                        <div className="timeline-card p-4">

                            <div className="d-flex flex-column flex-lg-row justify-content-between mb-3">

                                <div>

                                    <h4 className="fw-bold mb-1">
                                        {job.role}
                                    </h4>

                                    <h5 className="text-primary mb-2">
                                        {job.company}
                                    </h5>

                                </div>

                                <div className="text-lg-end">

                                    <div className="fw-semibold">
                                        {job.period}
                                    </div>

                                    {job.location && (

                                        <div className="text-secondary">
                                            {job.location}
                                        </div>

                                    )}

                                </div>

                            </div>

                            <ul className="mb-0">

                                {job.responsibilities.map((item) => (

                                    <li
                                        key={item}
                                        className="mb-2"
                                    >
                                        {item}
                                    </li>

                                ))}

                            </ul>

                        </div>

                    </div>

                ))}

            </div>

        </section>
    );
}

export default Experience;