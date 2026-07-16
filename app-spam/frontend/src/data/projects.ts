export interface Project {
    id: number;
    slug: string;

    title: string;

    category:
        | "Machine Learning"
        | "Decision Analytics"
        | "Business Intelligence"
        | "Research";

    description: string;
    overview: string;

    status: "Live" | "Coming Soon";

    type: string;

    technologies: string[];

    workflow: string[];

    futureImprovements: string[];

    github: string;

    demo: string;

    featured: boolean;

    image: string;

    icon: string;

    metrics?: {
        accuracy?: string;
        precision?: string;
        recall?: string;
        f1?: string;
        rmse?: string;
        mae?: string;
        r2?: string;
    };
}

export const projects: Project[] = [

    {
        id: 1,
        slug: "spam-email-detection",
        title: "Spam Email Detection",
        category: "Machine Learning",

        description:
            "Production-ready spam email classifier built using NLP, Flask and React.",

        overview:
            "This application detects whether an email is spam or legitimate using a machine learning pipeline. The project demonstrates an end-to-end workflow from text preprocessing and feature engineering to model deployment through a REST API and an interactive React frontend.",

        status: "Live",

        type: "Binary Classification",

        technologies: [
            "Python",
            "spaCy",
            "Scikit-learn",
            "Flask",
            "React",
            "Docker"
        ],

        workflow: [
            "Email Input",
            "Text Cleaning",
            "spaCy Lemmatization",
            "TF-IDF Vectorisation",
            "GridSearchCV Pipeline",
            "Prediction",
            "REST API Response"
        ],

        metrics: {
            accuracy: "98%",
            precision: "98%",
            recall: "98%",
            f1: "98%"
        },

        futureImprovements: [
            "AWS Deployment",
            "User Authentication",
            "Prediction History",
            "Batch Prediction",
            "Explainable AI"
        ],

        github: "#",

        demo: "#",

        featured: true,

        image: "",

        icon: "bi-envelope-fill"
    },

    {
        id: 2,
        slug: "sentiment-analysis",
        title: "Sentiment Analysis",
        category: "Machine Learning",

        description:
            "Customer review sentiment prediction using Natural Language Processing.",

        overview:
            "Predicts whether customer reviews are positive, neutral or negative using supervised machine learning and NLP preprocessing.",

        status: "Live",

        type: "Multi-class Classification",

        technologies: [
            "Python",
            "spaCy",
            "Scikit-learn",
            "Pandas"
        ],

        workflow: [
            "Review Input",
            "Text Cleaning",
            "spaCy",
            "TF-IDF",
            "Classification",
            "Prediction"
        ],

        metrics: {
            accuracy: "95%",
            f1: "94%"
        },

        futureImprovements: [
            "Transformer Models",
            "Explainable Predictions",
            "Live Dashboard"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-chat-heart-fill"
    },

    {
        id: 3,
        slug: "medical-insurance-charge-estimator",
        title: "Medical Insurance Charge Estimator",
        category: "Machine Learning",

        description:
            "Regression model estimating medical insurance charges.",

        overview:
            "Predicts expected insurance charges from demographic and health information using supervised regression techniques.",

        status: "Live",

        type: "Regression",

       technologies: [
                "Python",
                "Pandas",
                "Scikit-Learn",
                "Flask",
                "React"
            ],

        workflow: [
            "User Input",
            "Preprocessing",
            "Encoding",
            "Quantile Transformation",
            "Random Forest Regression",
            "Charge Estimation"
],

        metrics: {
            rmse: "To be updated",
            mae: "To be updated",
            r2: "To be updated"
        },

        futureImprovements: [
            "Confidence Intervals",
            "Feature Importance",
            "Cloud Deployment"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-cash-stack"
    },

    {
        id: 4,
        slug: "insurance-risk-classifier",
        title: "Insurance Risk Classifier",
        category: "Machine Learning",

        description:
            "Predicts whether an insured individual belongs to a high-risk category.",

        overview:
            "Binary classification model supporting insurance risk assessment.",

        status: "Live",

        type: "Binary Classification",

        technologies: [
            "Python",
            "Scikit-learn",
            "Pandas"
        ],

        workflow: [
            "Input",
            "Preprocessing",
            "Classification",
            "Risk Prediction"
        ],

        metrics: {
            accuracy: "To be updated"
        },

        futureImprovements: [
            "Probability Scores",
            "Explainable AI"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-shield-check"
    },

    {
        id: 5,
        slug: "diabetes-prediction",
        title: "Diabetes Prediction",
        category: "Machine Learning",

        description:
            "Predicts diabetes risk using patient clinical measurements.",

        overview:
            "Healthcare machine learning application currently under development.",

        status: "Coming Soon",

        type: "Binary Classification",

        technologies: [
            "Python",
            "Scikit-learn"
        ],

        workflow: [
            "Patient Data",
            "Preprocessing",
            "Prediction"
        ],

        futureImprovements: [
            "Probability Estimates",
            "Model Explainability",
            "Deployment"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-heart-pulse-fill"
    },

    {
        id: 6,
        slug: "economic-assessment-tool",
        title: "Economic Assessment Tool",
        category: "Decision Analytics",

        description:
            "Interactive decision-support application for investment appraisal under uncertainty.",

        overview:
            "An interactive application developed to evaluate investment projects under uncertainty. The application includes discounted payback period calculations alongside additional financial analysis functions to support investment appraisal and economic decision-making.",

        status: "Live",

        type: "Decision Support System",

        technologies: [
            "Python",
            "Flask",
            "JavaScript",
            "HTML",
            "CSS"
        ],

        workflow: [
            "Input Project Parameters",
            "Financial Calculations",
            "Discounted Payback Analysis",
            "Decision Support Output"
        ],

        futureImprovements: [
            "Monte Carlo Simulation",
            "Sensitivity Analysis",
            "Interactive Charts",
            "Export Reports"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-calculator-fill"
    },

    {
        id: 7,
        slug: "retail-sales-dashboard",
        title: "Retail Sales Dashboard",
        category: "Business Intelligence",

        description:
            "Interactive dashboard analysing sales and profitability.",

        overview:
            "Power BI dashboard for monitoring sales performance, customer trends and profitability.",

        status: "Live",

        type: "Power BI",

        technologies: [
            "Power BI",
            "SQL",
            "DAX"
        ],

        workflow: [
            "Data Extraction",
            "Transformation",
            "Data Modelling",
            "Dashboard Development"
        ],

        futureImprovements: [
            "Microsoft Fabric",
            "Automated Refresh"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-bar-chart-fill"
    },

    {
        id: 8,
        slug: "crime-analytics-dashboard",
        title: "Crime Analytics Dashboard",
        category: "Business Intelligence",

        description:
            "Business Intelligence dashboard exploring crime trends.",

        overview:
            "Interactive dashboard analysing crime hotspots and historical trends.",

        status: "Live",

        type: "Power BI",

        technologies: [
            "Power BI",
            "Power Query",
            "DAX"
        ],

        workflow: [
            "Data Cleaning",
            "Transformation",
            "Visualisation"
        ],

        futureImprovements: [
            "Real-time Data",
            "Azure Integration"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-graph-up-arrow"
    },

    {
        id: 9,
        slug: "health-expenditure-research",
        title: "Health Expenditure Research",
        category: "Research",

        description:
            "Econometric research analysing the relationship between health expenditure, productivity and economic development.",

        overview:
            "Applied advanced econometric techniques to large panel datasets to investigate the impact of healthcare expenditure on productivity and long-term economic growth.",

        status: "Live",

        type: "Econometrics",

        technologies: [
            "Stata",
            "R",
            "Python"
        ],

        workflow: [
            "Data Collection",
            "Data Cleaning",
            "Econometric Modelling",
            "Statistical Testing",
            "Policy Interpretation"
        ],

        futureImprovements: [
            "Interactive Visualisations",
            "Published Paper Links"
        ],

        github: "#",

        demo: "#",

        featured: false,

        image: "",

        icon: "bi-journal-text"
    }

];