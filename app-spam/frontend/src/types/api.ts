/* ==========================================
   COMMON
========================================== */

export interface PredictionResponse {
    prediction: string;
    confidence: number;
}

/* ==========================================
   SPAM
========================================== */

export interface SpamPredictionResponse
    extends PredictionResponse {}

/* ==========================================
   SENTIMENT
========================================== */
export interface SentimentPredictionResponse
    extends PredictionResponse {}

/* ==========================================
   DIABETES
========================================== */

export interface DiabetesPredictionResponse {
    prediction: string;
    probability?: number;
}

/* ==========================================
   INSURANCE
========================================== */

export interface InsurancePredictionResponse {
    estimatedCharge: number;
}

/* ==========================================
   ECONOMIC ASSESSMENT
========================================== */

export interface EconomicAssessmentResponse {
    result: string;
    score?: number;
}

/* ==========================================
   INSURANCE RISK CLASSIFICATION
========================================== */

export interface InsuranceRiskResponse
    extends PredictionResponse {}   