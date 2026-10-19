import "./Sidebar.css";
import { NavLink } from "react-router-dom";

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-icon">ML</div>
        <div>
          <h2>ML Platform</h2>
          <p>From Data to Real-World Impact</p>
        </div>
      </div>

      <nav className="sidebar-nav">
        <NavLink to="/" end className="nav-link">
          Dashboard
        </NavLink>

        <NavLink to="/churn" className="nav-link">
          Customer Churn
        </NavLink>

        <NavLink to="/readmission" className="nav-link">
          Hospital Readmission
        </NavLink>

        <NavLink to="/history" className="nav-link">
          Prediction History
        </NavLink>

        <div className="nav-divider" />

        <NavLink to="/about" className="nav-link">
          About Project
        </NavLink>

        <NavLink to="/profile" className="nav-link">
          My Profile
        </NavLink>

        <div className="nav-divider" />

        <p className="nav-section-label">MY PROJECTS</p>

        <a href="/profile#projects" className="nav-link">
          Featured Projects ↗
        </a>

        <a
          href="https://github.com/9more/test_repo"
          target="_blank"
          rel="noreferrer"
          className="nav-link"
        >
          GitHub Repositories ↗
        </a>
      </nav>

      <div className="profile-card">
        <img
          className="profile-avatar"
          src="/profile.jpg"
          alt="Profile portrait"
        />

        <h3>Imoh Ekpenyong</h3>
        <p className="profile-title">Data Scientist | Economist (PhD)</p>
        <p className="profile-description">
          Building practical ML solutions for real-world problems.
        </p>

        <div className="profile-links">
          <a
            href="https://github.com/9more/test_repo"
            target="_blank"
            rel="noreferrer"
          >
            GitHub
          </a>
          <a
            href="https://www.linkedin.com/in/imoh-ekpenyong-95983045/?isSelfProfile=true"
            target="_blank"
            rel="noreferrer"
          >
            LinkedIn
          </a>
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;
