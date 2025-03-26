import requests


# module responsible for getting id of all the incidents for further processing (foudn to be less than 1000)
url = "https://avcan-services-api.prod.avalanche.ca/min/en/submissions?fromdate=2016-01-01&todate=2025-02-15&obtype=incident&pagesize=1000"

id_list = []

headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': '92kJB50eJq7RZlZyWlA5ZaxgZaluOV1Q9OQzLzX7'
}

# for page in range(1, 8):
response = requests.get(url, headers=headers)
if response.status_code == 200:
    response_json = response.json()
    data = response_json['items']["data"]
    for item in data:
        print(item['id'])
        id_list.append(item['id'])
else:
    print(f"Request failed with status code {response.status_code}")

print("completed")
