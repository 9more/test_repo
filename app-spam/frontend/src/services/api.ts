import { API_BASE_URL } from "../config";

export interface PredictionResponse {
    prediction: string;
    probability?: number;
}

export async function predictSpam(message: string): Promise<PredictionResponse> {

    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: message,
        }),
    });

    if (!response.ok) {
        throw new Error("Prediction failed.");
    }

    return response.json();
}