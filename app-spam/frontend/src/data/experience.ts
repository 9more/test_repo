export interface Experience {
    role: string;
    company: string;
    period: string;
    location?: string;
    responsibilities: string[];
}


export const experience: Experience[] = [

    {
        role: "MCR Support Engineer / Analyst",
        company: "Igamemedia Limited",
        period: "2024 - Present",
        location: "United Kingdom",

        responsibilities: [
            "Analysing incoming data feeds to ensure compliance with client specifications.",
            "Monitoring live events, data flows and system performance.",
            "Performing latency analysis and operational reporting.",
            "Using data insights to improve content delivery and operational efficiency."
        ]
    },

    {
        role: "Data and Research Analyst",
        company: "Finance and Commercial Securities Limited",
        period: "2010 - 2013",

        responsibilities: [
            "Performed quantitative analysis to support business and financial decisions.",
            "Analysed financial data and produced analytical reports.",
            "Applied statistical methods to interpret trends and patterns."
        ]
    },

    {
        role: "Lecturer in Economics",
        company: "Federal University",
        period: "Previous Academic Experience",

        responsibilities: [
            "Delivered lectures in Econometrics, Macroeconomics and Health Economics.",
            "Developed teaching materials and assessed student performance.",
            "Supported quantitative research and analytical projects."
        ]
    }

];