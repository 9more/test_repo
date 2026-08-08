function Hero({ name, title, research, description }) {
  return (
    <section className="hero">
      <h1>{name}</h1>

      <p className="hero-title">{title}</p>

      <p className="hero-research">{research}</p>

      <p className="hero-description">
        {description}
      </p>

      <div className="hero-buttons">
        <a href="#publications">View Publications</a>

        <a href="#contact">Contact</a>
      </div>
    </section>
  );
}

export default Hero;