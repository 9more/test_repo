import { useState } from "react";
import ResultCard from "./ResultCard";

function SpamForm() {

  const [message, setMessage] = useState("");

  const [prediction, setPrediction] = useState("");

  const [confidence, setConfidence] = useState(0);

  const handlePrediction = () => {

    if (message.length < 5) {

      alert("Please enter an email.");

      return;

    }

    // Temporary until Flask API is connected

    setPrediction("Not Spam");

    setConfidence(98.74);

  };

  return (

    <div className="card shadow-lg border-0">

      <div className="card-body">

        <h4 className="mb-3">

          Live Spam Detector

        </h4>

        <textarea

          className="form-control"

          rows={10}

          placeholder="Paste an email here..."

          value={message}

          onChange={(e) => setMessage(e.target.value)}

        />

        <button

          className="btn btn-primary btn-lg mt-4 w-100"

          onClick={handlePrediction}

        >

          Detect Spam

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

export default SpamForm;