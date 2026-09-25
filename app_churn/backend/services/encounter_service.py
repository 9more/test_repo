from database.connection import get_connection


def create_encounter(patient_id, features):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
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
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
        RETURNING encounter_id;
    """

    values = (
        patient_id,
        features["admission_type_id"],
        features["discharge_disposition_id"],
        features["admission_source_id"],
        features["time_in_hospital"],
        features["num_lab_procedures"],
        features["num_procedures"],
        features["num_medications"],
        features["number_outpatient"],
        features["number_emergency"],
        features["number_inpatient"],
        features["number_diagnoses"],
        features["weight"],
        features["payer_code"],
        features["medical_specialty"],
        features["diag_1"],
        features["diag_2"],
        features["diag_3"],
        features["max_glu_serum"],
        features["A1Cresult"],
        features["metformin"],
        features["repaglinide"],
        features["nateglinide"],
        features["chlorpropamide"],
        features["glimepiride"],
        features["acetohexamide"],
        features["glipizide"],
        features["glyburide"],
        features["tolbutamide"],
        features["pioglitazone"],
        features["rosiglitazone"],
        features["acarbose"],
        features["miglitol"],
        features["troglitazone"],
        features["tolazamide"],
        features["examide"],
        features["citoglipton"],
        features["insulin"],
        features["glyburide-metformin"],
        features["glipizide-metformin"],
        features["glimepiride-pioglitazone"],
        features["metformin-rosiglitazone"],
        features["metformin-pioglitazone"],
        features["change"],
        features["diabetesMed"],
    )

    cursor.execute(query, values)

    encounter_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return encounter_id


def get_encounter(encounter_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        patients.race,
        patients.gender,
        patients.age,

        encounters.admission_type_id,
        encounters.discharge_disposition_id,
        encounters.admission_source_id,
        encounters.time_in_hospital,
        encounters.num_lab_procedures,
        encounters.num_procedures,
        encounters.num_medications,
        encounters.number_outpatient,
        encounters.number_emergency,
        encounters.number_inpatient,
        encounters.number_diagnoses,

        encounters.weight,
        encounters.payer_code,
        encounters.medical_specialty,

        encounters.diag_1,
        encounters.diag_2,
        encounters.diag_3,

        encounters.max_glu_serum,
        encounters.A1Cresult,

        encounters.metformin,
        encounters.repaglinide,
        encounters.nateglinide,
        encounters.chlorpropamide,
        encounters.glimepiride,
        encounters.acetohexamide,
        encounters.glipizide,
        encounters.glyburide,
        encounters.tolbutamide,
        encounters.pioglitazone,
        encounters.rosiglitazone,
        encounters.acarbose,
        encounters.miglitol,
        encounters.troglitazone,
        encounters.tolazamide,
        encounters.examide,
        encounters.citoglipton,
        encounters.insulin,

        encounters.glyburide_metformin,
        encounters.glipizide_metformin,
        encounters.glimepiride_pioglitazone,
        encounters.metformin_rosiglitazone,
        encounters.metformin_pioglitazone,

        encounters.change_status,
        encounters.diabetes_med

    FROM encounters

    JOIN patients
        ON encounters.patient_id = patients.patient_id

    WHERE encounters.encounter_id = %s;
"""

    cursor.execute(query, (encounter_id,))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row is None:
        return None

    columns = [
        "race",
        "gender",
        "age",
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

    return dict(zip(columns, row))
