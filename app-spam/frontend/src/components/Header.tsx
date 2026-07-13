function Header() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm">

      <div className="container">

        <a className="navbar-brand fw-bold" href="#">
          Imoh Ekpenyong
        </a>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>


        <div
          className="collapse navbar-collapse justify-content-end"
          id="navbarNav"
        >

          <ul className="navbar-nav">

            <li className="nav-item">
              <a className="nav-link" href="#about">
                About
              </a>
            </li>


            <li className="nav-item">
              <a className="nav-link" href="#about">
                Technology
              </a>
            </li>


            <li className="nav-item">
              <a className="nav-link" href="#projects">
                Projects
              </a>
            </li>


            <li className="nav-item">
              <a className="nav-link" href="#contact">
                Contact
              </a>
            </li>

          </ul>

        </div>

      </div>

    </nav>
  );
}

export default Header;