import { useState, useEffect, useRef, type FormEvent } from "react";
import { predictModel } from "../api";
type Props = {
  onClose: () => void;
};

export default function InsuranceForm({ onClose }: Props) {
  const [age, setAge] = useState("");
  const [sex, setSex] = useState("male");
  const [bmi, setBmi] = useState("");
  const [children, setChildren] = useState("");
  const [smoker, setSmoker] = useState("no");
  const [region, setRegion] = useState("northwest");

  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);
  const resultRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (result) {
      resultRef.current?.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }, [result]);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setLoading(true);
    setResult("");

    try {
      const prediction = await predictModel("insurance", {
        age: Number(age),
        sex,
        bmi: Number(bmi),
        children: Number(children),
        smoker,
        region,
      });

      setResult(prediction);
    } catch (error) {
      console.error(error);
      setResult("Failed to generate prediction.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="prediction-form">
      <h3>🏥 Insurance Analytics</h3>

      <form onSubmit={handleSubmit} className="insurance-grid">
        <div className="form-group">
          <label>Age</label>
          <input
            type="number"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            required
            disabled={loading}
          />
        </div>

        <div className="form-group">
          <label>Sex</label>
          <select
            value={sex}
            onChange={(e) => setSex(e.target.value)}
            disabled={loading}
          >
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
        </div>

        <div className="form-group">
          <label>BMI</label>
          <input
            type="number"
            step="0.1"
            value={bmi}
            onChange={(e) => setBmi(e.target.value)}
            required
            disabled={loading}
          />
        </div>

        <div className="form-group">
          <label>Children</label>
          <input
            type="number"
            value={children}
            onChange={(e) => setChildren(e.target.value)}
            required
            disabled={loading}
          />
        </div>

        <div className="form-group">
          <label>Smoker</label>
          <select
            value={smoker}
            onChange={(e) => setSmoker(e.target.value)}
            disabled={loading}
          >
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
        </div>

        <div className="form-group">
          <label>Region</label>
          <select
            value={region}
            onChange={(e) => setRegion(e.target.value)}
            disabled={loading}
          >
            <option value="northwest">Northwest</option>
            <option value="northeast">Northeast</option>
            <option value="southwest">Southwest</option>
            <option value="southeast">Southeast</option>
          </select>
        </div>

        <button className="estimate-btn" type="submit" disabled={loading}>
          {loading ? "⏳ Estimating..." : "Estimate Insurance Premium"}
        </button>
      </form>

      {result && (
        <div ref={resultRef} className="prediction-result">
          <h4>Prediction</h4>
          <p>{result}</p>
        </div>
      )}

      <button type="button" className="back-btn" onClick={onClose}>
        ← Back to Chat
      </button>
    </div>
  );
}
