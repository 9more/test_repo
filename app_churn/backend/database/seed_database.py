import pandas as pd

from database.connection import get_connection



CHURN_DATASET = (
    "/Users/imohekpenyong/test_repo/"
    "production-ml-project/data/raw/telecom_customer.csv"
)

READMISSION_DATASET = (
    "/Users/imohekpenyong/test_repo/"
    "diabetes_ml_prediction/src/data.csv"
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
    "totcalls"
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
    "number_diagnoses"
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
    "diabetesMed"
]


READMISSION_FEATURES = (
    READMISSION_NUMERIC
    + READMISSION_CATEGORICAL
)



def clean_value(value):

    if pd.isna(value):
        return None

    return value

def seed_churn():

    print("\nLoading churn dataset...")

    df = pd.read_csv(
        CHURN_DATASET
    )

    print(
        f"Original churn rows: {len(df)}"
    )

    df = df.sample(
        n=SAMPLE_SIZE,
        random_state=42
    )

    print(
        f"Selected churn rows: {len(df)}"
    )

    connection = get_connection()
    cursor = connection.cursor()

    customer_count = 0
    feature_count = 0

    try:

        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO customers DEFAULT VALUES
                RETURNING customer_id;
                """
            )

            customer_id = cursor.fetchone()[0]

            customer_count += 1

            values = []

            for feature in CHURN_FEATURES:

                values.append(
                    clean_value(row[feature])
                )
            cursor.execute(
                """
                INSERT INTO customer_features (
                    customer_id,
                    eqpdays,
                    months,
                    change_mou,
                    totmrc_mean,
                    mou_mean,
                    avgqty,
                    asl_flag,
                    change_rev,
                    hnd_price,
                    mou_cvce_mean,
                    avg3mou,
                    uniqsubs,
                    crclscod,
                    refurb_new,
                    totcalls
                )
                VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s
                );
                """,
                (
                    customer_id,
                    *values
                )
            )

            feature_count += 1

        connection.commit()

        print(
            f"Customers inserted: {customer_count}"
        )

        print(
            f"Customer feature records inserted: "
            f"{feature_count}"
        )

    except Exception:

        connection.rollback()

        raise

    finally:

        cursor.close()
        connection.close()




def seed_readmission():

    print("\nLoading readmission dataset...")

    df = pd.read_csv(
        READMISSION_DATASET
    )

    print(
        f"Original readmission rows: {len(df)}"
    )


    positive = df[
        df["readmitted"] == "<30"
    ]

    negative = df[
        df["readmitted"] != "<30"
    ]

    positive_sample_size = round(
        SAMPLE_SIZE * len(positive) / len(df)
    )

    negative_sample_size = (
        SAMPLE_SIZE - positive_sample_size
    )

    positive_sample = positive.sample(
        n=positive_sample_size,
        random_state=42
    )

    negative_sample = negative.sample(
        n=negative_sample_size,
        random_state=42
    )

    df = pd.concat(
        [
            positive_sample,
            negative_sample
        ]
    ).sample(
        frac=1,
        random_state=42
    )

    print(
        f"Selected readmission rows: {len(df)}"
    )

    print(
        "30-day readmissions in sample:",
        (df["readmitted"] == "<30").sum()
    )

    connection = get_connection()
    cursor = connection.cursor()

    patient_cache = {}

    patient_count = 0
    encounter_count = 0

    try:

        for _, row in df.iterrows():

            patient_nbr = int(
                row["patient_nbr"]
            )

            # -------------------------------------------------
            # Create patient if we have not seen this patient
            # -------------------------------------------------

            if patient_nbr not in patient_cache:

                cursor.execute(
                    """
                    INSERT INTO patients (
                        patient_nbr,
                        gender,
                        race,
                        age
                    )
                    VALUES (
                        %s, %s, %s, %s
                    )
                    RETURNING patient_id;
                    """,
                    (
                        patient_nbr,
                        clean_value(row["gender"]),
                        clean_value(row["race"]),
                        clean_value(row["age"])
                    )
                )

                patient_id = cursor.fetchone()[0]

                patient_cache[patient_nbr] = patient_id

                patient_count += 1

            else:

                patient_id = patient_cache[
                    patient_nbr
                ]

            # -------------------------------------------------
            # Prepare encounter values
            # -------------------------------------------------

            encounter_values = []

            for feature in READMISSION_FEATURES:

                encounter_values.append(
                    clean_value(row[feature])
                )

            # -------------------------------------------------
            # Database column names
            #
            # PostgreSQL cannot use the '-' names directly
            # as unquoted column names, so our schema uses
            # underscores for these medication columns.
            # -------------------------------------------------

            cursor.execute(
                """
                INSERT INTO encounters (
                    patient_id,
                    admission_type_id,
                    discharge_disposition_id,
                    admission_source_id,
                    time_in_hospital,
                    num_lab_procedures,
                    num_procedures,
                    num_medications,
                    number_outpatient,
                    number_emergency,
                    number_inpatient,
                    number_diagnoses,
                    weight,
                    payer_code,
                    medical_specialty,
                    diag_1,
                    diag_2,
                    diag_3,
                    max_glu_serum,
                    A1Cresult,
                    metformin,
                    repaglinide,
                    nateglinide,
                    chlorpropamide,
                    glimepiride,
                    acetohexamide,
                    glipizide,
                    glyburide,
                    tolbutamide,
                    pioglitazone,
                    rosiglitazone,
                    acarbose,
                    miglitol,
                    troglitazone,
                    tolazamide,
                    examide,
                    citoglipton,
                    insulin,
                    glyburide_metformin,
                    glipizide_metformin,
                    glimepiride_pioglitazone,
                    metformin_rosiglitazone,
                    metformin_pioglitazone,
                    change_status,
                    diabetes_med
                )
                VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s
                )
                RETURNING encounter_id;
                """,
                (
                    patient_id,
                    *encounter_values
                )
            )

            cursor.fetchone()

            encounter_count += 1

        connection.commit()

        print(
            f"Patients inserted: {patient_count}"
        )

        print(
            f"Encounters inserted: {encounter_count}"
        )

    except Exception:

        connection.rollback()

        raise

    finally:

        cursor.close()
        connection.close()


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("=" * 60)
    print("PRODUCTION ML DATABASE SEED")
    print("=" * 60)

    seed_churn()

    seed_readmission()

    print("\nDatabase seeding completed successfully.")


if __name__ == "__main__":
    main()
```

### Run it

From the **project root**:

```bash
cd /Users/imohekpenyong/test_repo/production-ml-project
```

Then:

```bash
python backend/database/seed_database.py
```

One thing to watch for: because you've already created test records such as `customer_id=1` and `patient_id=1`, this script will **add** the sample data rather than replace those records.

After it finishes, we'll check:

```sql
SELECT COUNT(*) FROM customers;

SELECT COUNT(*) FROM customer_features;

SELECT COUNT(*) FROM patients;

SELECT COUNT(*) FROM encounters;
```

and also check that the readmission sample retained roughly the expected number of `<30` cases.

**Don't run the seeding script yet if you want us to first make it safe to re-run without creating duplicate records.** The version above is suitable for the initial population; before deployment, we'll make ingestion/migrations more robust.
