import publications from "../data/publications";

function PublicationsPage() {
    return (
        <section className="publications-page">
            <div className="container">

                <h1>Publications</h1>

                <div className="publication-list">

                    {publications.map(publication => (
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

            </div>
        </section>
    );
}

export default PublicationsPage;