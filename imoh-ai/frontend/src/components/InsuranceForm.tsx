import { useState, type FormEvent } from "react";
import { streamMessage } from "../api";

export default function InsuranceForm() {
  const [age, setAge] = useState("");
  const [sex, setSex] = useState("male");
  const [bmi, setBmi] = useState("");
  const [children, setChildren] = useState("");
  const [smoker, setSmoker] = useState("no");
  const [region, setRegion] = useState("northwest");

  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setLoading(true);
    setResult("");

    try {
      await streamMessage(
        "insurance",
        {
          age: Number(age),
          sex,
          bmi: Number(bmi),
          children: Number(children),
          smoker,
          region,
        },
        (chunk) => {
          setResult((prev) => prev + chunk);
        },
      );
    } catch (error) {
      console.error(error);
      setResult("Failed to generate prediction.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="insurance-form">
      <h3>🏥 Insurance Analytics</h3>

      <form onSubmit={handleSubmit}>
        <label>Age</label>
        <input
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />

        <label>Sex</label>
        <select value={sex} onChange={(e) => setSex(e.target.value)}>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>

        <label>BMI</label>
        <input
          type="number"
          step="0.1"
          value={bmi}
          onChange={(e) => setBmi(e.target.value)}
          required
        />

        <label>Children</label>
        <input
          type="number"
          value={children}
          onChange={(e) => setChildren(e.target.value)}
          required
        />

        <label>Smoker</label>
        <select value={smoker} onChange={(e) => setSmoker(e.target.value)}>
          <option value="yes">Yes</option>
          <option value="no">No</option>
        </select>

        <label>Region</label>
        <select value={region} onChange={(e) => setRegion(e.target.value)}>
          <option value="northwest">Northwest</option>
          <option value="northeast">Northeast</option>
          <option value="southwest">Southwest</option>
          <option value="southeast">Southeast</option>
        </select>

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Estimate"}
        </button>
      </form>

      {result && (
        <div className="prediction-result">
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}
