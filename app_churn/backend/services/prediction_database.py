from database.connection import get_connection


def save_prediction(
    encounter_id, model_name, model_version, probability, threshold, prediction
):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO predictions (
            encounter_id,
            model_name,
            model_version,
            probability,
            threshold,
            prediction
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING prediction_id;
    """

    cursor.execute(
        query,
        (encounter_id, model_name, model_version, probability, threshold, prediction),
    )

    prediction_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return prediction_id
