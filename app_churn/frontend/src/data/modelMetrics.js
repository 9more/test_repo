const modelMetrics = {
  churn: {
    name: "Customer Churn",
    model: "Random Forest",
    threshold: 0.5,
    metrics: {
      rocAuc: 0.6759,
      accuracy: 0.6253,
      precision: 0.6174,
      recall: 0.6417,
      f1Score: 0.6293,
    },
  },

  readmission: {
    name: "Hospital Readmission",
    model: "XGBoost",
    threshold: 0.15,
    metrics: {
      rocAuc: 0.6905,
      accuracy: 0.7814,
      precision: 0.231,
      recall: 0.4117,
      f1Score: 0.2959,
    },
  },
};

export default modelMetrics;
