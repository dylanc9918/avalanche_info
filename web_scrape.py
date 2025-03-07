import requests
from bs4 import BeautifulSoup


core = "https://www.avalanche.ca"
url = "https://avalanche.ca/incidents"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table')

# Extract headers
headers = [header.text for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    values = [col.text for col in row.find_all('td')]
    rows.append(dict(zip(headers, values)))

    view_link = row.find('a', text='view')
    if view_link:
        view_url = view_link['href']
        # Make a request to the view URL
        view_response = requests.get(core + view_url)
        view_soup = BeautifulSoup(view_response.content, 'html.parser')
        # Process the view page as needed
        # Example: store the entire page text
        row_data['view_page'] = view_soup.text

    rows.append(row_data)

# Print the extracted data
for row in rows:
    print(row)
