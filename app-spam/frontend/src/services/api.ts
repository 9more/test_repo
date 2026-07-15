import config from "./config";

import type {
    SpamPredictionResponse,
    SentimentPredictionResponse,
    DiabetesPredictionResponse,
    InsurancePredictionResponse,
    EconomicAssessmentResponse
} from "../types/api";

const API_BASE_URL = config.API_BASE_URL;

/* ==========================================
   SPAM DETECTION
========================================== */

export async function predictSpam(
    message: string
): Promise<SpamPredictionResponse> {

    const response = await fetch(
        `${API_BASE_URL}/predict/spam`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message
            })
        }
    );

    if (!response.ok) {
        throw new Error("Spam prediction failed");
    }

    return await response.json();
}

/* ==========================================
   SENTIMENT ANALYSIS
========================================== */

export async function predictSentiment(
    text: string
): Promise<SentimentPredictionResponse> {

    console.log(
        "API URL:",
        `${API_BASE_URL}/predict/sentiment`
    );

    const response = await fetch(
        `${API_BASE_URL}/predict/sentiment`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text
            })
        }
    );

    if (!response.ok) {
        throw new Error("Sentiment prediction failed");
    }

    return await response.json();
}

/* ==========================================
   DIABETES PREDICTION
========================================== */

export async function predictDiabetes(
    data: unknown
): Promise<DiabetesPredictionResponse> {

    const response = await fetch(
        `${API_BASE_URL}/predict/diabetes`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {
        throw new Error("Diabetes prediction failed");
    }

    return await response.json();
}

/* ==========================================
   INSURANCE ESTIMATION
========================================== */

export async function predictInsurance(
    data: unknown
): Promise<InsurancePredictionResponse> {

    const response = await fetch(
        `${API_BASE_URL}/predict/insurance`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {
        throw new Error("Insurance prediction failed");
    }

    return await response.json();
}

/* ==========================================
   ECONOMIC ASSESSMENT
========================================== */

export async function economicAssessment(
    data: unknown
): Promise<EconomicAssessmentResponse> {

    const response = await fetch(
        `${API_BASE_URL}/predict/economic`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {
        throw new Error("Economic assessment failed");
    }

    return await response.json();
}

/* ==========================================
   INSURANCE Risk Classification
========================================== */

export async function predictInsuranceRisk(
    data: unknown
): Promise<PredictionResponse> {

    const response = await fetch(
        `${API_BASE_URL}/predict/insurance-risk`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {
        throw new Error(
            "Insurance risk prediction failed"
        );
    }

    return await response.json();
}