function Hero({ name, title, research }) {
  return (
    <section className="hero">

    <h1>{name}</h1>

    <p className="hero-title">
        {title}
    </p>

    <p className="hero-research">
        {research}
    </p>

</section>
  );
}

export default Hero;