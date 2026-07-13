import { useState } from "react";
import ResultCard from "./ResultCard";

function SpamForm() {

    const [message, setMessage] = useState("");

    const [prediction, setPrediction] = useState("");

    const [confidence, setConfidence] = useState(0);

    const [loading, setLoading] = useState(false);

    const handlePrediction = async () => {

        if (message.trim().length < 5) {
            alert("Please enter an email to analyse.");
            return;
        }

        setLoading(true);

        // Temporary until Flask API is connected

        setTimeout(() => {

            setPrediction("Not Spam");
            setConfidence(98.74);

            setLoading(false);

        }, 800);

    };

    return (

        <div className="card shadow-lg border-0">

            <div className="card-body p-4">

                <div className="d-flex align-items-center mb-3">

                    <i className="bi bi-envelope-check-fill text-primary fs-3 me-3"></i>

                    <div>

                        <h4 className="mb-0">
                            Live Spam Detector
                        </h4>

                        <small className="text-secondary">
                            Test the machine learning model using your own email text.
                        </small>

                    </div>

                </div>

                <textarea

                    className="form-control"

                    rows={10}

                    placeholder="Paste an email message here..."

                    value={message}

                    onChange={(e) => setMessage(e.target.value)}

                />

                <div className="d-grid mt-4">

                    <button

                        className="btn btn-primary btn-lg"

                        disabled={loading}

                        onClick={handlePrediction}

                    >

                        {loading ? (

                            <>

                                <span
                                    className="spinner-border spinner-border-sm me-2"
                                    role="status"
                                />

                                Analysing...

                            </>

                        ) : (

                            <>
                                <i className="bi bi-cpu me-2"></i>
                                Detect Spam
                            </>

                        )}

                    </button>

                </div>

                {prediction && (

                    <div className="mt-4">

                        <ResultCard

                            prediction={prediction}

                            confidence={confidence}

                        />

                    </div>

                )}

            </div>

        </div>

    );

}

export default SpamForm;