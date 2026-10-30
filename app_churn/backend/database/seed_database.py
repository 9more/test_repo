import os
import pandas as pd

from sqlalchemy import (
    create_engine,
    text,
    MetaData,
    Table,
    insert,
    URL,
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ.get("DB_HOST", "localhost"),
    port=int(os.environ.get("DB_PORT", 5432)),
    database=os.environ["DB_NAME"],
)

engine = create_engine(DATABASE_URL)

# --------------------------------------------------
# DATASET PATHS
# --------------------------------------------------

CHURN_DATASET = "/app/data/churn/telecom_customer.csv"
READMISSION_DATASET = "/app/data/readmission/data.csv"

SAMPLE_SIZE = 10_000

# --------------------------------------------------
# FEATURE DEFINITIONS
# --------------------------------------------------

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


# --------------------------------------------------
# SAFETY CHECK
# --------------------------------------------------


def check_empty_database():

    tables = [
        "patients",
        "encounters",
        "customers",
        "customer_features",
        "predictions",
    ]

    with engine.connect() as connection:

        for table in tables:

            count = connection.execute(
                text(f"SELECT COUNT(*) FROM {table}")
            ).scalar_one()

            if count > 0:
                raise RuntimeError(
                    f"{table} already contains {count:,} rows. "
                    "Seeding stopped to prevent duplicate records."
                )


# --------------------------------------------------
# CHURN SEEDING
# --------------------------------------------------


def seed_churn():

    print("\nLoading churn dataset...")

    df = pd.read_csv(CHURN_DATASET)

    print(f"Original churn rows: {len(df):,}")

    if len(df) < SAMPLE_SIZE:
        raise ValueError("Churn dataset contains fewer than 10,000 rows.")

    df = df.sample(n=SAMPLE_SIZE, random_state=42).copy()

    # Generate a separate database ID for every customer.
    metadata = MetaData()

    customers_table = Table(
        "customers",
        metadata,
        autoload_with=engine,
    )

    customer_rows = [{} for _ in range(len(df))]

    with engine.begin() as connection:

        result = connection.execute(
            insert(customers_table).returning(
                customers_table.c.customer_id,
                sort_by_parameter_order=True,
            ),
            customer_rows,
        )

        customer_ids = list(result.scalars())

        feature_df = df[CHURN_FEATURES].copy()

        feature_df = feature_df.rename(columns=CHURN_COLUMN_MAP)

        feature_df.insert(0, "customer_id", customer_ids)

        feature_df.to_sql(
            "customer_features",
            connection,
            if_exists="append",
            index=False,
        )

    print(f"Customers inserted: {len(customer_ids):,}")
    print(f"Customer features inserted: {len(feature_df):,}")


# --------------------------------------------------
# READMISSION SEEDING
# --------------------------------------------------


def seed_readmission():

    print("\nLoading readmission dataset...")

    df = pd.read_csv(READMISSION_DATASET)

    print(f"Original readmission rows: {len(df):,}")

    positive = df[df["readmitted"] == "<30"]
    negative = df[df["readmitted"] != "<30"]

    positive_size = round(SAMPLE_SIZE * len(positive) / len(df))

    negative_size = SAMPLE_SIZE - positive_size

    positive_sample = positive.sample(
        n=positive_size,
        random_state=42,
    )

    negative_sample = negative.sample(
        n=negative_size,
        random_state=42,
    )

    df = (
        pd.concat([positive_sample, negative_sample])
        .sample(frac=1, random_state=42)
        .copy()
    )

    print(f"Selected readmission rows: {len(df):,}")
    print(
        "30-day readmissions:",
        (df["readmitted"] == "<30").sum(),
    )

    patients = (
        df[["patient_nbr", "gender", "race", "age"]]
        .drop_duplicates(subset=["patient_nbr"])
        .copy()
    )

    with engine.begin() as connection:

        patients.to_sql(
            "patients",
            connection,
            if_exists="append",
            index=False,
        )

        patient_lookup = pd.read_sql(
            text("""
                SELECT patient_id, patient_nbr
                FROM patients
            """),
            connection,
        )

        df = df.merge(
            patient_lookup,
            on="patient_nbr",
            how="left",
            validate="many_to_one",
        )

        if df["patient_id"].isna().any():
            raise RuntimeError("Some encounters have no patient ID.")

        encounter_features = READMISSION_NUMERIC + [
            feature
            for feature in READMISSION_CATEGORICAL
            if feature not in ["race", "gender", "age"]
        ]

        encounter_df = df[["patient_id"] + encounter_features].copy()

        encounter_df = encounter_df.rename(columns=READMISSION_COLUMN_MAP)

        encounter_df.to_sql(
            "encounters",
            connection,
            if_exists="append",
            index=False,
        )

    print(f"Unique patients inserted: {len(patients):,}")
    print(f"Encounters inserted: {len(encounter_df):,}")


# --------------------------------------------------
# DATABASE SUMMARY
# --------------------------------------------------


def show_summary():

    print("\n" + "=" * 60)
    print("DATABASE SUMMARY")
    print("=" * 60)

    tables = [
        "patients",
        "encounters",
        "customers",
        "customer_features",
        "predictions",
    ]

    with engine.connect() as connection:

        for table in tables:

            count = connection.execute(
                text(f"SELECT COUNT(*) FROM {table}")
            ).scalar_one()

            print(f"{table:20} {count:,}")


# --------------------------------------------------
# MAIN
# --------------------------------------------------


def main():

    print("=" * 60)
    print("PRODUCTION ML DATABASE SEED")
    print("=" * 60)

    check_empty_database()

    seed_churn()
    seed_readmission()

    show_summary()

    print("\nDatabase seeding completed.")


if __name__ == "__main__":
    main()
