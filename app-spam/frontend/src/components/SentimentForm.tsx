import { useState } from "react";
import ResultCard from "./ResultCard";
import { predictSentiment } from "../services/api";

function SentimentForm() {

    const [text, setText] = useState("");

    const [prediction, setPrediction] = useState("");

    const [confidence, setConfidence] = useState(0);

    const [loading, setLoading] = useState(false);

    const handlePrediction = async () => {

        if (text.length < 5) {

            alert("Please enter some text.");

            return;
        }

        try {

            setLoading(true);

            const result = await predictSentiment(text);

            setPrediction(result.prediction);

            setConfidence(result.confidence);

        } catch (error) {

            console.error(error);

            alert("Prediction failed.");

        } finally {

            setLoading(false);

        }
    };

    return (

        <div className="card shadow-lg border-0">

            <div className="card-body">

                <h4 className="mb-3">
                    Live Sentiment Analysis
                </h4>

                <textarea
                    className="form-control"
                    rows={8}
                    placeholder="Enter text for sentiment analysis..."
                    value={text}
                    onChange={(e) =>
                        setText(e.target.value)
                    }
                />

                <button
                    className="btn btn-primary btn-lg mt-4 w-100"
                    onClick={handlePrediction}
                    disabled={loading}
                >

                    {loading
                        ? "Analysing..."
                        : "Analyse Sentiment"}

                </button>

                {prediction && (

                    <ResultCard
                        prediction={prediction}
                        confidence={confidence}
                    />

                )}

            </div>

        </div>

    );
}

export default SentimentForm;