import json
from shapely.geometry import Point, shape, Polygon


def label_forecast_area(conn):
    """
    Label the locations with the forecast area they are in.
    """
    # Get the forecast area data from the database
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, ST_X(coord) as lat, ST_Y(coord) as lon FROM incident_summary_nonfatal WHERE coord IS NOT NULL")

    incident_location = cursor.fetchall()

    with open("ForecastAreaLabel/avalanche_areas.json", "r") as f:
        polygons_data = json.load(f)
    # Create a dictionary to store the forecast area for each location
    forecast_area_dict = {}

    polygons = []
    for feature in polygons_data["features"]:
        # Convert GeoJSON geometry to Shapely Polygon
        polygon = Polygon(feature["geometry"]['coordinates'][0][0])

        id = feature["properties"]["id"]  # Get the label from properties
        polygons.append({"polygon": polygon, "id": id})

    for location in incident_location:
        point = Point(location[2], location[1])
        for poly in polygons:
            if poly["polygon"].contains(point):
                forecast_area_dict[location[0]] = poly["id"]

    # Update the database with the forecast area for each location
    for location_id, forecast_area_id in forecast_area_dict.items():
        cursor.execute("UPDATE incident_summary_nonfatal SET forecast_region = %s WHERE id = %s",
                       (forecast_area_id, location_id))

    conn.commit()

    print("Forecast area labeling completed.")
