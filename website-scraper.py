from bs4 import BeautifulSoup
import json
import requests

response = requests.get("https://www.example.com")
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the table rows
rows = soup.find_all("tr")

# Extract the data
data = []
for row in rows[1:]:
    cols = row.find_all("th")
    entry = {
        "name": cols[0].text.strip(),
        "hash": cols[1].text.strip(),
    }
    data.append(entry)

# Write the data to a JSON file
with open("output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
