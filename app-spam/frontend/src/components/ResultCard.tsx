interface ResultCardProps {
    prediction: string;
    confidence: number;
}


function ResultCard({ prediction, confidence }: ResultCardProps) {

    const isSpam = prediction.toLowerCase() === "spam";


    return (
        <div
            className={`card mt-4 shadow ${
                isSpam ? "border-danger" : "border-success"
            }`}
        >

            <div className="card-body">

                <h4 className="card-title">
                    Prediction Result
                </h4>


                <h2
                    className={`fw-bold ${
                        isSpam
                            ? "text-danger"
                            : "text-success"
                    }`}
                >
                    {prediction}
                </h2>


                <p className="mb-0">
                    Confidence:
                    <strong>
                        {" "}
                        {confidence.toFixed(2)}%
                    </strong>
                </p>

            </div>

        </div>
    );
}


export default ResultCard;