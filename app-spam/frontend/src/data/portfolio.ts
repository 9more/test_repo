export interface Portfolio {
    name: string;
    title: string;
    location: string;
    summary: string;
    introduction: string;
    technologies: string[];
    expertise: string[];
    focusAreas: string[];
    email: string;
    github: string;
    linkedin: string;
}

export const portfolio: Portfolio = {

    name: "Imoh Ekpenyong",

    title:
        "Data Scientist | Economist | Machine Learning Engineer",

    location:
        "United Kingdom",

    summary:
        "Economist and data professional specialising in machine learning, analytics, econometrics and data-driven decision making.",

    introduction:
        "I combine economics research expertise with practical data science experience, applying machine learning, statistical modelling and analytics to solve real-world problems.",

    technologies: [
        "Python",
        "Machine Learning",
        "Natural Language Processing",
        "SQL",
        "Power BI",
        "Econometrics",
        "Data Analytics",
        "Cloud Technologies"
    ],

    expertise: [
        "Machine Learning",
        "Natural Language Processing",
        "Econometrics",
        "Business Intelligence",
        "Predictive Modelling"
    ],

    focusAreas: [
        "Healthcare Analytics",
        "Economic Assessment",
        "Data Visualisation",
        "Decision Support Systems"
    ],

    email: "imoh.ekpenyong@aol.com",

    github: "https://github.com/9more/test_repo",

    linkedin: "linkedin.com/in/imoh-ekpenyong-95983045"
};