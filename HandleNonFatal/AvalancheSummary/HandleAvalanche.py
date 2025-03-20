from datetime import datetime
import re
from shapely.geometry import Point
from DBconn.db_connection import conn


def insert_avalanche_summary(incident_json):

    avalanche_json = incident_json['avalanche_obs']

    unique_id = incident_json['id']

    cursor = conn.cursor()

    try:
        size = float(avalanche_json[0].get('size'))
    except:
        size = None

    insert_query = """
    INSERT INTO avalanches_nonfatal (date,size,type,avy_trigger,elevation,aspect,slab_width,slab_thick,id	
)
    VALUES (%s,  %s, %s,  %s, %s,  %s,  %s, %s, %s)
    """
    data = (
        avalanche_json[0].get('observation_date'),
        size,
        avalanche_json[0].get('type'),
        avalanche_json[0].get('trigger'),
        avalanche_json[0].get('elevation'),
        avalanche_json[0].get('aspect', None),
        avalanche_json[0].get('slab_width', None),
        avalanche_json[0].get('slab_thickness', None),
        unique_id)

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Record {unique_id} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
