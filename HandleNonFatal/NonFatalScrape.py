import requests
import pandas as pd
import HandleNonFatal.AvalancheSummary.HandleAvalanche as HandleAvalanche
import HandleNonFatal.IncidentSummary.HandleIncident as HandleIncident


def handle_non_fatal(conn):
    url = "https://avcan-services-api.prod.avalanche.ca/min/en/submissions/"

    id_list = list(pd.read_csv("HandleNonFatal/avalanche_id_list.csv")['ID'])

    obs_funcs_map = {
        'avalanche': HandleAvalanche.insert_avalanche_data
    }

    for id in id_list:
        response = requests.get(url + id)
        if response.status_code == 200:
            response_json = response.json()
            incident_obs = list(response_json['observationCounts'].keys())

            HandleIncident.insert_avalanche_summary(response_json, conn)

            for obs in incident_obs:
                if obs in obs_funcs_map:
                    obs_funcs_map[obs](response_json, conn)
                else:
                    continue

        else:
            print(f"Request failed with status code {response.status_code}")
