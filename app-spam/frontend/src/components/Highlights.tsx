import { highlights } from "../data/highlights";

function Highlights() {
    return (
        <section className="highlights">

            <div className="container">

                <div className="row g-3">

                    {highlights.map((item) => (

                        <div
                            key={item.label}
                            className="col-lg-3 col-md-6"
                        >

                            <div className="highlight-card">

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