/* ==========================================
   SENTIMENT
========================================== */

export interface SentimentFormData {
    text: string;
}

/* ==========================================
   SPAM
========================================== */

export interface SpamFormData {
    message: string;
}

/* ==========================================
   DIABETES
========================================== */

export interface DiabetesFormData {
    pregnancies: number;
    glucose: number;
    bloodPressure: number;
    skinThickness: number;
    insulin: number;
    bmi: number;
    diabetesPedigreeFunction: number;
    age: number;
}

/* ==========================================
   INSURANCE
========================================== */

export interface InsuranceFormData {
    age: number;
    sex: string;
    bmi: number;
    children: number;
    smoker: string;
    region: string;
}

/* ==========================================
   ECONOMIC ASSESSMENT
========================================== */

export interface EconomicAssessmentInput {
    [key: string]: string | number;
}