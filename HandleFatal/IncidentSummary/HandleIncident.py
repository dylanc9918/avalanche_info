from shapely.geometry import Point
from DBconn.db_connection import conn


def insert_incident_summary(incident_json):
    """
    inserts the incident summary from the fatality database into the database. This includes the location, date, and other information about the incident how many caught etc
    """

    cursor = conn.cursor()
# Check if the location_coords is present and has 2 values to avoid dealing with NONE values
    if incident_json.get('location_coords')[0] == None or incident_json.get('location_coords')[1] == None:
        coordinates = None
    else:
        coordinates = Point(
            incident_json['location_coords'][1], incident_json['location_coords'][0]).wkt

    insert_query = """
    INSERT INTO incident_summary (date, location, locat_desc, province, coord, elev, activity, involvement, injury, fatality,description,id)
    VALUES (%s,  %s, %s,  %s, ST_GeomFromText(%s),  %s,  %s, %s, %s, %s, %s, %s)
    """
    data = (
        incident_json.get('ob_date'),
        incident_json.get('location'),
        incident_json.get('location_desc'),
        incident_json.get('location_province'),
        coordinates,
        incident_json.get('location_elevation', None),
        incident_json.get('group_activity'),
        incident_json.get('num_involved', None),
        incident_json.get('num_injured', None),
        incident_json.get('num_fatal', None),
        incident_json.get('comment', ''),
        incident_json.get('id')
    )

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Record {incident_json['location']} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
