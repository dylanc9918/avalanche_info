import requests
import pandas as pd
import HandleNonFatal.AvalancheSummary.HandleAvalanche as HandleAvalanche


def handle_non_fatal(conn):
    url = "https://avcan-services-api.prod.avalanche.ca/min/en/submissions/"

    id_list = pd.read_csv("HandleNonFatal/id_list.csv", skiprows=1)

    for id in id_list:
        response = requests.get(url + id)
        if response.status_code == 200:
            response_json = response.json()
            HandleAvalanche.insert_avalanche_summary(response_json, conn)

        else:
            print(f"Request failed with status code {response.status_code}")
