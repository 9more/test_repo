
function Publications() {
    const publications = [

    {
        id: 1,
        authors: ["Jane Smith", "John Brown"],
        title: "The Impact of Labour Market Policies",
        journal: "Journal of Economic Studies",
        year: 2026,
        link: "#"
    },
    {
        id: 2,
        authors: ["Jane Smith"],
        title: "Economic Growth and Public Investment",
        journal: "Economic Policy Review",
        year: 2025,
        link: "#"
    },

        {id: 3,
            authors: ["Jane Smith"],
            title: "The Impact of Labour Market Policies",
            journal: "Journal of Economic Studies",
            year: 2025,
            link: "#"
        },
        {
            id: 4,
            authors: ["Jane Smith"],
            title: "Economic Growth and Public Investment",
            journal: "Economic Policy Review",
            year: 2024,
            link: "#"
        },
        {
            id: 5,
            authors: ["Jane Smith"],
            title: "Behavioural Economics in Public Policy",
            journal: "Applied Economics",
            year: 2023,
            link: "#"
        },
        {
            id: 6,
            authors: ["Jane Smith"],
            title: "Labour Markets and Economic Development",
            journal: "Development Economics Review",
            year: 2022,
            link: "#"
        }
    ];

    return (
        <section className="publications" id="publications">
            <div className="container">

                <h2>Publications</h2>

                <div className="publication-list">
                    {publications.map(publication => (
                        <article
    key={publication.id}
    className="publication"
>
    <p className="publication-authors">
        {publication.authors.join(", ")}
    </p>

    <h3>{publication.title}</h3>

    <p className="publication-details">
        {publication.journal} · {publication.year}
    </p>

    <a href={publication.link}>
        Read publication
    </a>
</article>
                    ))}
                </div>

            </div>
        </section>
    );
}

export default Publications;
