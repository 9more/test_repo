import { useState } from "react";
import { predictInsurance } from "../services/api";

function InsuranceForm() {

    const [age, setAge] = useState("");
    const [sex, setSex] = useState("male");
    const [bmi, setBmi] = useState("");
    const [children, setChildren] = useState("");
    const [smoker, setSmoker] = useState("no");
    const [region, setRegion] = useState("southwest");

    const [estimate, setEstimate] = useState<number | null>(null);

    const [loading, setLoading] = useState(false);

    const handlePrediction = async () => {

        try {

            setLoading(true);

            const result = await predictInsurance({
                age: Number(age),
                sex,
                bmi: Number(bmi),
                children: Number(children),
                smoker,
                region
            });

            setEstimate(result.estimatedCharge);

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
                    Medical Insurance Cost Estimator
                </h4>

                <input
                    className="form-control mb-3"
                    type="number"
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
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select>

                <input
                    className="form-control mb-3"
                    type="number"
                    placeholder="BMI"
                    value={bmi}
                    onChange={(e) =>
                        setBmi(e.target.value)
                    }
                />

                <input
                    className="form-control mb-3"
                    type="number"
                    placeholder="Number of Children"
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
                    <option value="no">Non-Smoker</option>
                    <option value="yes">Smoker</option>
                </select>

                <select
                    className="form-select mb-4"
                    value={region}
                    onChange={(e) =>
                        setRegion(e.target.value)
                    }
                >
                    <option value="southwest">Southwest</option>
                    <option value="southeast">Southeast</option>
                    <option value="northwest">Northwest</option>
                    <option value="northeast">Northeast</option>
                </select>

                <button
                    className="btn btn-primary btn-lg w-100"
                    onClick={handlePrediction}
                    disabled={loading}
                >

                    {loading
                        ? "Estimating..."
                        : "Estimate Insurance Cost"}

                </button>

                {estimate !== null && (

                    <div className="alert alert-success mt-4">

                        <strong>
                            Estimated Annual Insurance Cost
                        </strong>

                        <div className="fs-4 fw-bold mt-2">

                            £{estimate.toLocaleString(undefined, {
                            minimumFractionDigits: 2,
                            maximumFractionDigits: 2
                        })}

                        </div>

                    </div>

                )}

            </div>

        </div>

    );
}

export default InsuranceForm;