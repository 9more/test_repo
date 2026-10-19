import { BrowserRouter, Routes, Route } from "react-router-dom";
import ReadmissionPage from "./pages/ReadmissionPage";

import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";
import ChurnPage from "./pages/ChurnPage";
import "./App.css";
import AboutPage from "./pages/AboutPage";
import ProfilePage from "./pages/ProfilePage";

function HistoryPage() {
  return <h1>Prediction History</h1>;
}

function NotFoundPage() {
  return <h1>Page not found</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <div className="app-layout">
        <Sidebar />

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/churn" element={<ChurnPage />} />
            <Route path="/readmission" element={<ReadmissionPage />} />
            <Route path="/history" element={<HistoryPage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="*" element={<NotFoundPage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
