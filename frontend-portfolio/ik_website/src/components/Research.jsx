function Research() {
    const researchAreas = [
        "Labour Economics",
        "Public Policy",
        "Development Economics",
        "Behavioural Economics",
        "Economic Growth"
    ];

    return (
        <section
            className="research"
            id="research"
        >
            <div className="container">

                <h2>Research Interests</h2>

                <div className="research-grid">

                    {researchAreas.map(area => (
                        <div
                            key={area}
                            className="research-card"
                        >
                            <h3>{area}</h3>
                        </div>
                    ))}

                </div>

            </div>
        </section>
    );
}

export default Research;