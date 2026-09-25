from database.connection import get_connection


def create_customer():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers
        DEFAULT VALUES
        RETURNING customer_id;
    """

    cursor.execute(query)

    customer_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return customer_id


def create_customer_features(customer_id, features):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
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
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        RETURNING feature_record_id;
    """

    values = (
        customer_id,
        features["eqpdays"],
        features["months"],
        features["change_mou"],
        features["totmrc_Mean"],
        features["mou_Mean"],
        features["avgqty"],
        features["asl_flag"],
        features["change_rev"],
        features["hnd_price"],
        features["mou_cvce_Mean"],
        features["avg3mou"],
        features["uniqsubs"],
        features["crclscod"],
        features["refurb_new"],
        features["totcalls"],
    )

    cursor.execute(query, values)

    feature_record_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return feature_record_id
