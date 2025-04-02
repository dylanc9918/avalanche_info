import requests
import csv


# module responsible for getting id of all the incidents for further processing (foudn to be less than 1000)
incident_url = "https://avcan-services-api.prod.avalanche.ca/min/en/submissions?fromdate=2016-01-01&todate=2025-02-15&obtype=incident&pagesize=1000"

avalanche_url = "https://avcan-services-api.prod.avalanche.ca/min/en/submissions?fromdate=2016-01-01&todate=2020-02-15&obtype=avalanche&pagesize=4000"

id_list = []

headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': '92kJB50eJq7RZlZyWlA5ZaxgZaluOV1Q9OQzLzX7'
}

response = requests.get(avalanche_url, headers=headers)
if response.status_code == 200:
    response_json = response.json()
    data = response_json['items']["data"]
    for item in data:
        print(item['id'])
        id_list.append(item['id'])
else:
    print(f"Request failed with status code {response.status_code}")

csv_filename = "HandleNonFatal/avalanche_id_list.csv"
with open(csv_filename, mode='a', newline='') as file:  # Open in append mode
    writer = csv.writer(file)
    for id in id_list:
        writer.writerow([id])

print("completed")
