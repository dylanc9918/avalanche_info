from datetime import datetime
import re
from shapely.geometry import Point


def insert_avalanche_summary(incident_json, conn):

    avalanche_json = incident_json['observations']['avalanche']

    unique_id = incident_json['submissionID']

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO avalanches_nonfatal (date, num_avalanche, size, type, avy_trigger, elevation, aspect, slab_width, slab_thick, run_length, start_angle, weak_layer_date, id	
)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (

        avalanche_json.get('avalancheOccurrenceDatetime') if avalanche_json.get(
            'avalancheOccurrenceDatetime') else None,
        avalanche_json.get('numberOfAvalanches'),
        avalanche_json.get('avalancheSize'),  #
        avalanche_json.get('avalancheCharacter')[0] if avalanche_json.get(
            'avalancheCharacter') else None,
        avalanche_json.get('triggerSubType') if avalanche_json.get(
            'triggerSubType') else None,
        avalanche_json.get('startZoneElevation'),
        avalanche_json.get('startZoneAspect')[0] if avalanche_json.get(
            'startZoneAspect') else None,
        avalanche_json.get('slabWidth', None),
        avalanche_json.get('slabThickness', None),
        avalanche_json.get('runLength', None),
        avalanche_json.get('startZoneIncline', None),
        avalanche_json.get('weakLayerBurialDate') if avalanche_json.get(
            'weakLayerBurialDate') else None,
        unique_id if unique_id else None
    )

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print(f"Record {unique_id} inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
