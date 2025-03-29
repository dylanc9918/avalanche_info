
from DBconn.db_connection import create_connection
import HandleFatal.IncidentSummary.HandleIncident as HandleIncident
import HandleFatal.AvalancheSummary.HandleAvalanche as HandleAvalanche
import HandleFatal.WeatherSummary.HandleWeather as HandleWeather
import HandleFatal.SnowpackSummary.HandleSnowpack as HandleSnowpack
import HandleFatal.DocumentSummary.HandleDocuments as HandleDocuments
import requests

# main entry point for the program to extract fatal incidents


def handle_fatal(conn):
    # URL to scrape
    core = "https://incidents.avalanche.ca/public/incidents/"
    url = url = 'http://incidents.avalanche.ca/public/incidents/?page=1&format=json'

    url_pages = [
        'http://incidents.avalanche.ca/public/incidents/?page=1&format=json']

    # extract json data from the url

    def extract_json(url):
        response = requests.get(url)
        data_json = response.json()
        return data_json

    table = extract_json(url)

    while table['next']:
        url = table['next']
        table = extract_json(url)
        url_pages.append(url)

    for url in url_pages:

        response = requests.get(url)
        data_json = response.json()

        # top level data
        for incident in data_json['results']:
            # Make a request to the view URL
            incident_response = requests.get(core + incident['id'])

            incident_json = incident_response.json()

            # Extract respective sections of data for fatal incident
            HandleIncident.insert_incident_summary(incident_json)

            if len(incident_json['avalanche_obs']) > 0:
                HandleAvalanche.insert_avalanche_summary(incident_json)

            if len(incident_json['weather_obs']) > 0:
                HandleWeather.insert_weather_summary(incident_json)

            if len(incident_json['snowpack_obs']) > 0:
                HandleSnowpack.insert_snowpack_summary(incident_json)

            if len(incident_json['documents']) > 0:
                HandleDocuments.insert_documents_summary(incident_json)
