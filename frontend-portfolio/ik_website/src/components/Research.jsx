function Research() {
    const researchAreas = [
        "Labour Economics",
        "Public Policy",
        "Development Economics",
        "Behavioural Economics",
        "Economic Growth"
    ];

    return (<section
        className="research"
        id="research"
    >
        <h2>Research Interests</h2>

        <div className="research-grid">
            {
                researchAreas.map(area => (

                    <div className="research-card">

                        <h3>{area}</h3>

                    </div>)
                )};

        </div>

    </section>)

}

export default Research;