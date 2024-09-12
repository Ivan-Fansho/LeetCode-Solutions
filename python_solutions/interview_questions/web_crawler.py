import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')[1:]

countries = {}

for row in rows:
    columns = row.find_all('td')
    if len(columns) >= 2:
        country = columns[0].text.strip()
        population = columns[1].text
        population = int(population.replace(',', ''))
        countries[country] = {'country_population': population}

total_country_population = 0
for data in countries.values():
    total_country_population += data['country_population']

for country, data in countries.items():
    data['country_population_percentage'] = "{:.2f}%".format((data['country_population'] / total_country_population) * 100, '.2f')

print(json.dumps(countries, indent=4))

filename = 'countries.json'
previous = {}

if os.path.exists(filename):
    with open(filename, 'r') as file:
        previous = json.load(file)
if countries != previous:
    with open(filename, 'w') as file:
        json.dump(countries, file, indent=2)