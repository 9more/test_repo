import { experience } from "../data/experience";

function Experience() {
    return (
        <section id="experience" className="container py-5">

            <h2 className="fw-bold mb-5">
                Professional Experience
            </h2>

            <div className="row">

                {experience.map((job) => (

                    <div
                        key={`${job.company}-${job.role}`}
                        className="col-12 mb-4"
                    >

                        <div className="card shadow-sm border-0">

                            <div className="card-body">

                                <h4 className="fw-bold">
                                    {job.role}
                                </h4>

                                <h5 className="text-primary">
                                    {job.company}
                                </h5>

                                <p className="text-secondary mb-3">

                                    {job.period}

                                    {job.location && (
                                        <> • {job.location}</>
                                    )}

                                </p>

                                <ul className="mb-0">

                                    {job.responsibilities.map((item) => (

                                        <li key={item}>
                                            {item}
                                        </li>

                                    ))}

                                </ul>

                            </div>

                        </div>

                    </div>

                ))}

            </div>

        </section>
    );
}

export default Experience;