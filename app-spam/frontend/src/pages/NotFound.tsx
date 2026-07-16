import { Link } from "react-router-dom";

function NotFound() {

    return (

        <section className="container py-5 text-center">

            <h1 className="display-1 fw-bold text-primary">
                404
            </h1>

            <h2 className="fw-bold mb-3">
                Page Not Found
            </h2>

            <p className="text-secondary mb-4">
                The page you are looking for does not exist or has been moved.
            </p>

            <Link
                to="/"
                className="btn btn-primary"
            >
                Return Home
            </Link>

        </section>

    );

}

export default NotFound;