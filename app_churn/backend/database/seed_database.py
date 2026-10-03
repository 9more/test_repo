import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg://" "ml_user:ml_password@localhost:5432/ml_platform"

engine = create_engine(DATABASE_URL)


CHURN_DATASET = (
    "/Users/imohekpenyong/test_repo/"
    "production-ml-project/data/raw/telecom_customer.csv"
)

READMISSION_DATASET = (
    "/Users/imohekpenyong/test_repo/" "diabetes_ml_prediction/src/data.csv"
)

SAMPLE_SIZE = 10_000

CHURN_FEATURES = [
    "eqpdays",
    "months",
    "change_mou",
    "totmrc_Mean",
    "mou_Mean",
    "avgqty",
    "asl_flag",
    "change_rev",
    "hnd_price",
    "mou_cvce_Mean",
    "avg3mou",
    "uniqsubs",
    "crclscod",
    "refurb_new",
    "totcalls",
]

READMISSION_NUMERIC = [
    "admission_type_id",
    "discharge_disposition_id",
    "admission_source_id",
    "time_in_hospital",
    "num_lab_procedures",
    "num_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "number_diagnoses",
]


READMISSION_CATEGORICAL = [
    "race",
    "gender",
    "age",
    "weight",
    "payer_code",
    "medical_specialty",
    "diag_1",
    "diag_2",
    "diag_3",
    "max_glu_serum",
    "A1Cresult",
    "metformin",
    "repaglinide",
    "nateglinide",
    "chlorpropamide",
    "glimepiride",
    "acetohexamide",
    "glipizide",
    "glyburide",
    "tolbutamide",
    "pioglitazone",
    "rosiglitazone",
    "acarbose",
    "miglitol",
    "troglitazone",
    "tolazamide",
    "examide",
    "citoglipton",
    "insulin",
    "glyburide-metformin",
    "glipizide-metformin",
    "glimepiride-pioglitazone",
    "metformin-rosiglitazone",
    "metformin-pioglitazone",
    "change",
    "diabetesMed",
]

READMISSION_FEATURES = READMISSION_NUMERIC + READMISSION_CATEGORICAL

CHURN_COLUMN_MAP = {
    "totmrc_Mean": "totmrc_mean",
    "mou_Mean": "mou_mean",
    "mou_cvce_Mean": "mou_cvce_mean",
}


READMISSION_COLUMN_MAP = {
    "A1Cresult": "a1cresult",
    "glyburide-metformin": "glyburide_metformin",
    "glipizide-metformin": "glipizide_metformin",
    "glimepiride-pioglitazone": "glimepiride_pioglitazone",
    "metformin-rosiglitazone": "metformin_rosiglitazone",
    "metformin-pioglitazone": "metformin_pioglitazone",
    "change": "change_status",
    "diabetesMed": "diabetes_med",
}


def seed_churn():

    print("\nLoading churn dataset...")

    df = pd.read_csv(CHURN_DATASET)

    print(f"Original churn rows: {len(df):,}")

    df = df.sample(n=SAMPLE_SIZE, random_state=42).copy()

    print(f"Selected churn rows: {len(df):,}")

    customers = pd.DataFrame(index=df.index)

    customers.index.name = "source_index"

    customers["created_at"] = pd.Timestamp.now()

    customers.to_sql("customers", engine, if_exists="append", index=False)

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT customer_id
                FROM customers
                ORDER BY customer_id DESC
                LIMIT :limit
                """),
            {"limit": len(customers)},
        )

        customer_ids = [row[0] for row in result]

    customer_ids.reverse()

    feature_df = df[CHURN_FEATURES].copy()

    feature_df = feature_df.rename(columns=CHURN_COLUMN_MAP)

    feature_df.insert(0, "customer_id", customer_ids)

    feature_df.to_sql("customer_features", engine, if_exists="append", index=False)

    print(f"Customers inserted: {len(customers):,}")

    print(f"Customer feature records inserted: " f"{len(feature_df):,}")


def seed_readmission():

    print("\nLoading readmission dataset...")

    df = pd.read_csv(READMISSION_DATASET)

    print(f"Original readmission rows: {len(df):,}")

    positive = df[df["readmitted"] == "<30"]

    negative = df[df["readmitted"] != "<30"]

    positive_size = round(SAMPLE_SIZE * len(positive) / len(df))

    negative_size = SAMPLE_SIZE - positive_size

    positive_sample = positive.sample(n=positive_size, random_state=42)

    negative_sample = negative.sample(n=negative_size, random_state=42)

    df = (
        pd.concat([positive_sample, negative_sample])
        .sample(frac=1, random_state=42)
        .copy()
    )

    print(f"Selected readmission rows: {len(df):,}")

    print("30-day readmissions:", (df["readmitted"] == "<30").sum())

    patients = (
        df[["patient_nbr", "gender", "race", "age"]]
        .drop_duplicates(subset=["patient_nbr"])
        .copy()
    )

    patients = patients.rename(columns={"patient_nbr": "patient_nbr"})

    with engine.connect() as connection:

        existing = pd.read_sql(
            text("""
                SELECT
                    patient_id,
                    patient_nbr
                FROM patients
                """),
            connection,
        )

    existing_ids = set(existing["patient_nbr"])

    new_patients = patients[~patients["patient_nbr"].isin(existing_ids)].copy()

    if not new_patients.empty:

        new_patients.to_sql("patients", engine, if_exists="append", index=False)

    with engine.connect() as connection:

        patient_lookup = pd.read_sql(
            text("""
                SELECT
                    patient_id,
                    patient_nbr
                FROM patients
                """),
            connection,
        )

    df = df.merge(patient_lookup, on="patient_nbr", how="left")

    encounter_features = READMISSION_NUMERIC + [
        feature
        for feature in READMISSION_CATEGORICAL
        if feature not in ["race", "gender", "age"]
    ]

    encounter_df = df[["patient_id"] + encounter_features].copy()
    encounter_df = encounter_df.rename(columns=READMISSION_COLUMN_MAP)
    print(encounter_df.columns.tolist())

    print("\nEncounter columns:")
    print(encounter_df.columns.tolist())

    print("\nEncounter dtypes:")
    print(encounter_df.dtypes)

    print("\nFirst encounter:")
    print(encounter_df.head(1).to_dict("records"))

    encounter_df.to_sql("encounters", engine, if_exists="append", index=False)

    print(f"Patients inserted: " f"{len(new_patients):,}")

    print(f"Unique patients in sample: " f"{len(patients):,}")

    print(f"Encounters inserted: " f"{len(encounter_df):,}")


def show_summary():

    print("\n" + "=" * 60)
    print("DATABASE SUMMARY")
    print("=" * 60)

    with engine.connect() as connection:

        tables = [
            "patients",
            "encounters",
            "customers",
            "customer_features",
            "predictions",
        ]

        for table in tables:

            result = connection.execute(text(f"""
                    SELECT COUNT(*)
                    FROM {table}
                    """))

            count = result.scalar()

            print(f"{table:20} {count:,}")


def main():

    print("=" * 60)
    print("PRODUCTION ML DATABASE SEED")
    print("=" * 60)

    # seed_churn()

    seed_readmission()

    show_summary()

    print("\nDatabase seeding completed.")


if __name__ == "__main__":
    main()
