function Publications() {

    const publications = [
        {
            title: "The Impact of Labour Market Policies",
            journal: "Journal of Economic Studies",
            year: 2025
        },
        {
            title: "Economic Growth and Public Investment",
            journal: "Economic Policy Review",
            year: 2024
        },
        {
            title: "Behavioural Economics in Public Policy",
            journal: "Applied Economics",
            year: 2023
        }
    ];

    return (
        <section
            className="publications"
            id="publications"
        >
            <div className="container">

                <h2>Publications</h2>

                <div className="publication-list">

                    {publications.map(publication => (
                        <article
                            key={publication.title}
                            className="publication"
                        >

                            <p>
                                {publication.title}
                            </p>

                            <p>
                                {publication.journal}
                                {" · "}
                                {publication.year}
                            </p>

                        </article>

                    ))}

                </div>

            </div>
        </section>

    );
}

export default Publications;