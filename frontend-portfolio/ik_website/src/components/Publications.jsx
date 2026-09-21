import publications from "../data/publications";

function Publications() {
    return (
        <section className="publications" id="publications">
            <div className="container">

                <h2>Publications</h2>

                <div className="publication-list">

                    {publications.slice(0, 10).map(publication => (
                        <article
                            key={publication.id}
                            className="publication"
                        >
                            <p className="publication-authors">
                                {publication.authors}
                            </p>

                            <h3>{publication.title}</h3>

                            <p className="publication-details">
                                {publication.journal}
                                {" · "}
                                {publication.year}
                                {" · "}
                                {publication.status}
                            </p>

                            {publication.link && (
                                <a
                                    href={publication.link}
                                    target="_blank"
                                    rel="noreferrer"
                                >
                                    View publication
                                </a>
                            )}
                        </article>
                    ))}

                </div>

                <div className="publication-full-list">
                    <a href="/publications">
                        View full publication list →
                    </a>
                </div>

            </div>
        </section>
    );
}

export default Publications;