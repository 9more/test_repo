function Biography() {
  return (
    <section className="biography" id="biography">
      <div className="biography-image">
        <img
          src="https://placehold.co/300x300"
          alt="Portrait of Dr Jane Smith"
        />
      </div>

      <div className="biography-content">
        <h2>Biography</h2>

        <p>
          Dr Jane Smith is a Senior Lecturer in Economics
          whose research focuses on labour markets,
          public policy and economic development.
        </p>

        <p>
          Her work combines rigorous quantitative
          analysis with practical policy applications,
          helping governments and institutions make
          evidence-based decisions.
        </p>
      </div>
    </section>
  );
}

export default Biography;