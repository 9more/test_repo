from database.connection import get_connection


def create_patient(gender, race, age):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO patients (
            gender,
            race,
            age
        )
        VALUES (%s, %s, %s)
        RETURNING patient_id;
    """

    cursor.execute(query, (gender, race, age))

    patient_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return patient_id
