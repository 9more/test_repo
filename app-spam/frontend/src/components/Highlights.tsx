import { highlights } from "../data/highlights";

function Highlights() {
    return (
        <section className="highlights py-5">

            <div className="container">

                <div className="row g-4">

                    {highlights.map((item) => (

                        <div
                            key={item.label}
                            className="col-lg-3 col-md-6"
                        >

                            <div className="highlight-card text-center">

                                <h3 className="highlight-value">
                                    {item.value}
                                </h3>

                                <p className="highlight-label">
                                    {item.label}
                                </p>

                            </div>

                        </div>

                    ))}

                </div>

            </div>

        </section>
    );
}

export default Highlights;