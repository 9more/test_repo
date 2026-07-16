type Props = {
    prediction: string;
    confidence: number;
};

function ResultCard({
    prediction,
    confidence
}: Props) {

    return (

        <div className="card border-0 shadow-sm">

            <div className="card-body text-center">

                <h5 className="mb-3">
                    Prediction Result
                </h5>

                <h3
                    className={`fw-bold ${
                        prediction.toLowerCase().includes("spam")
                            ? "text-danger"
                            : "text-success"
                    }`}
                >
                    {prediction}
                </h3>

                <p className="text-secondary mb-0">
                    Confidence: {confidence.toFixed(2)}%
                </p>

            </div>

        </div>

    );
}

export default ResultCard;