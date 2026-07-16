export interface Education {
    qualification: string;
    institution: string;
    period: string;
    details: string[];
}


export const education: Education[] = [

    {
        qualification: "PhD in Economics",
        institution: "University of Aberdeen",
        period: "Completed",

        details: [
            "Research focused on empirical economics, health expenditure, productivity and economic development.",
            "Applied econometric modelling, statistical analysis and large-scale datasets.",
            "Developed strong quantitative research and analytical skills."
        ]
    },

    {
        qualification: "Data Science & Machine Learning Training",
        institution: "Various Professional Courses",
        period: "Completed",

        details: [
            "Machine Learning algorithms and model development.",
            "Python for Data Science and data analysis.",
            "Natural Language Processing and text analytics.",
            "Model evaluation, optimisation and deployment workflows."
        ]
    },

    {
        qualification: "Cloud, Data Engineering & Analytics Training",
        institution: "Various Professional Courses",
        period: "Completed",

        details: [
            "Cloud technologies and data platforms.",
            "Data engineering concepts and analytics workflows.",
            "Business Intelligence reporting and dashboard development.",
            "Data visualisation and analytical storytelling."
        ]
    }

];