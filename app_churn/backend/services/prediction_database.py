from database.connection import get_connection


def save_prediction(
    model_name,
    model_version,
    probability,
    threshold,
    prediction,
    encounter_id=None,
    customer_id=None,
):
    if (encounter_id is None) == (customer_id is None):
        raise ValueError("Provide exactly one of encounter_id or customer_id.")

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO predictions (
                encounter_id,
                customer_id,
                model_name,
                model_version,
                probability,
                threshold,
                prediction
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING prediction_id;
        """

        cursor.execute(
            query,
            (
                encounter_id,
                customer_id,
                model_name,
                model_version,
                probability,
                threshold,
                prediction,
            ),
        )

        prediction_id = cursor.fetchone()[0]
        connection.commit()

        return prediction_id

    except Exception:
        connection.rollback()
        raise

    finally:
        if "cursor" in locals():
            cursor.close()

        connection.close()
