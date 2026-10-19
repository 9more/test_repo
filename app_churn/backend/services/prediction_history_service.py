from database.connection import get_connection


def get_prediction_history(limit=5):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                prediction_id,
                customer_id,
                encounter_id,
                model_name,
                model_version,
                probability,
                threshold,
                prediction
            FROM predictions
            ORDER BY prediction_id DESC
            LIMIT %s;
        """

        cursor.execute(query, (limit,))

        columns = [column.name for column in cursor.description]
        rows = cursor.fetchall()

        return [dict(zip(columns, row)) for row in rows]

    finally:
        if "cursor" in locals():
            cursor.close()

        connection.close()
