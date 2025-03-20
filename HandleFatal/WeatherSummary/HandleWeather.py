from DBconn.db_connection import conn


def insert_weather_summary(incident_json):
    cursor = conn.cursor()

    weather_json = incident_json['weather_obs']

    unique_id = incident_json['id']

    insert_query = """
    INSERT INTO weather (temp_present, temp_max, temp_min, temp_trend, wind_speed, wind_dir, sky, precip, weather_desc, id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (
        weather_json.get('temp_present'),
        weather_json.get('temp_max'),
        weather_json.get('temp_min'),
        weather_json.get('temp_trend'),
        weather_json.get('wind_speed'),
        weather_json.get('wind_dir'),
        weather_json.get('sky'),
        weather_json.get('precip'),
        incident_json['weather_comment'],
        unique_id
    )

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Record {unique_id} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
