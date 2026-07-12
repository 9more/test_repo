export interface Technology {
    name: string;
}

export interface Project {

    title: string;

    description: string;

    github: string;

    technologies: string[];

}

export interface PredictionResponse {

    success: boolean;

    prediction: string;

    confidence: number;

}