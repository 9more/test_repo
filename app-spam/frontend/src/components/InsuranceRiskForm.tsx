import { useState } from "react";
import ResultCard from "./ResultCard";
import { predictInsuranceRisk } from "../services/api";

function InsuranceRiskForm() {

    const [age, setAge] = useState("");
    const [sex, setSex] = useState("male");
    const [bmi, setBmi] = useState("");
    const [children, setChildren] = useState("");
    const [smoker, setSmoker] = useState("no");
    const [region, setRegion] = useState("southwest");

    const [prediction, setPrediction] = useState("");
    const [confidence, setConfidence] = useState(0);

    const [loading, setLoading] = useState(false);

    const handlePrediction = async () => {

        try {

            setLoading(true);

            const result = await predictInsuranceRisk({

                age: Number(age),
                sex,
                bmi: Number(bmi),
                children: Number(children),
                smoker,
                region

            });

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

                <h4 className="mb-4">
                    Insurance Risk Predictor
                </h4>

                <input
                    type="number"
                    className="form-control mb-3"
                    placeholder="Age"
                    value={age}
                    onChange={(e) =>
                        setAge(e.target.value)
                    }
                />

                <select
                    className="form-select mb-3"
                    value={sex}
                    onChange={(e) =>
                        setSex(e.target.value)
                    }
                >

                    <option value="male">
                        Male
                    </option>

                    <option value="female">
                        Female
                    </option>

                </select>

                <input
                    type="number"
                    step="0.1"
                    className="form-control mb-3"
                    placeholder="BMI"
                    value={bmi}
                    onChange={(e) =>
                        setBmi(e.target.value)
                    }
                />

                <input
                    type="number"
                    className="form-control mb-3"
                    placeholder="Children"
                    value={children}
                    onChange={(e) =>
                        setChildren(e.target.value)
                    }
                />

                <select
                    className="form-select mb-3"
                    value={smoker}
                    onChange={(e) =>
                        setSmoker(e.target.value)
                    }
                >

                    <option value="yes">
                        Yes
                    </option>

                    <option value="no">
                        No
                    </option>

                </select>

                <select
                    className="form-select mb-4"
                    value={region}
                    onChange={(e) =>
                        setRegion(e.target.value)
                    }
                >

                    <option value="southwest">
                        Southwest
                    </option>

                    <option value="southeast">
                        Southeast
                    </option>

                    <option value="northwest">
                        Northwest
                    </option>

                    <option value="northeast">
                        Northeast
                    </option>

                </select>

                <button
                    className="btn btn-primary w-100"
                    disabled={loading}
                    onClick={handlePrediction}
                >

                    {loading
                        ? "Assessing Risk..."
                        : "Assess Insurance Risk"}

                </button>

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

export default InsuranceRiskForm;