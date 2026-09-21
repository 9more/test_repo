function Teaching() {
    const courses = [
        {
            id: 1,
            name: "Microeconomics",
            levels: ["Undergraduate", "Postgraduate"]
        },
        {
            id: 2,
            name: "Econometrics",
            levels: ["Postgraduate"]
        },
        {
            id: 3,
            name: "Development Economics",
            levels: ["Undergraduate", "Postgraduate"]
        },
        {
            id: 4,
            name: "Public Economics",
            levels: ["Undergraduate"]
        }
    ];

    return (
        <section className="teaching" id="teaching">
            <div className="container">

                <h2>Teaching</h2>

                <div className="teaching-philosophy">
                    <h3>Teaching Philosophy</h3>

                    <p>
                        I believe effective economics education should be
                        learner-centred, combining rigorous theory with
                        practical applications and encouraging students
                        to engage critically with economic issues.
                    </p>
                </div>

                <div className="courses">

                    <h3>Courses</h3>

                    <div className="course-list">

                        {courses.map(course => (
                            <article
                                key={course.id}
                                className="course"
                            >
                                <h4>{course.name}</h4>

                                <p>
                                    {course.levels.join(" · ")}
                                </p>
                            </article>
                        ))}

                    </div>

                </div>

            </div>
        </section>
    );
}

export default Teaching;