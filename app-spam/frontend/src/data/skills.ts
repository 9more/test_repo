export interface SkillCategory {
  category: string;
  skills: string[];
}

export const skills: SkillCategory[] = [
  {
    category: "Programming",
    skills: [
      "Python",
      "SQL",
      "R",
      "TypeScript"
    ]
  },

  {
    category: "Machine Learning",
    skills: [
      "Scikit-learn",
      "PyTorch",
      "TensorFlow",
      "spaCy",
      "MLflow"
    ]
  },

  {
    category: "Data Engineering",
    skills: [
      "Pandas",
      "NumPy",
      "Databricks",
      "Snowflake"
    ]
  },

  {
    category: "Business Intelligence",
    skills: [
      "Power BI",
      "DAX",
      "Excel"
    ]
  },

  {
    category: "Cloud & Development",
    skills: [
      "Azure",
      "Flask",
      "React",
      "Git",
      "Docker"
    ]
  }
];