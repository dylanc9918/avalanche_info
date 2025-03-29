from shapely.geometry import Point


def insert_avalanche_summary(response_json, conn):

    incident_json = response_json['observations']['incident']
    unique_id = response_json['submissionID']

    coord = Point(
        response_json['location'].get('latitude'), response_json['location'].get('longitude')).wkt

    try:
        description = response_json['observations']['avalanche'].get('comment')
    except:
        description = None

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO incident_summary_nonfatal (
        id, date, location, locat_desc, province, coord, elev, activity, involvement, injury, fatality, description
    )
    VALUES (%s, %s, %s, %s, %s, ST_GeomFromText(%s), %s, %s, %s, %s, %s, %s)
    """

    data = (
        unique_id,
        response_json.get('datetime'),
        response_json.get('region'),
        response_json.get('location_description'),
        response_json.get('province'),
        coord,
        incident_json.get('elevation'),
        incident_json.get('groupActivity'),
        incident_json.get('numberInvolved'),
        incident_json.get('numberInjured'),
        0,
        incident_json.get('description', description)

    )

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Record {unique_id} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
