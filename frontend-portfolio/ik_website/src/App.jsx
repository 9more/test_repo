import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import PublicationsPage from "./pages/PublicationsPage";

import "./App.css";

function App() {
    return (
        <BrowserRouter>

            <Navbar />

            <Routes>
                <Route path="/" element={<Home />} />
                <Route
                    path="/publications"
                    element={<PublicationsPage />}
                />
            </Routes>

        </BrowserRouter>
    );
}

export default App;