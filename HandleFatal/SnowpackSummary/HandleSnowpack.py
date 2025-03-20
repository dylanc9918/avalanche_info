from DBconn.db_connection import conn


def insert_snowpack_summary(incident_json):
    cursor = conn.cursor()

    snowpack_json = incident_json['snowpack_obs']

    unique_id = incident_json['id']

    insert_query = """
    INSERT INTO snowpack (snowpack, snow_trend, storm_snow, storm_date, snow_desc, id)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = (
        snowpack_json.get('hs'),
        snowpack_json.get('hn24'),
        snowpack_json.get('hst'),
        snowpack_json.get('hst_reset'),
        incident_json['snowpack_comment'],
        unique_id
    )

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Record {unique_id} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
