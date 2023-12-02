import requests
from bs4 import BeautifulSoup
import pandas as pd

# State abbreviations
state_abbreviations = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

# Base URL
base_url = "https://fred.stlouisfed.org/release/tables?rid=118&eid=259194&od={}-01-01"

# Initialize an empty DataFrame to store the data
population_data = pd.DataFrame(columns=['State', 'Year', 'Population'])

# Iterate over each year from 2000 to 2016
for year in range(2000, 2017):
    # Construct URL for each year
    url = base_url.format(year)

    # Fetch the content from the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', id='release-elements-tree')

        # Extract data from each row
        for i, row in enumerate(table.find_all('tr')[1:]):
            if i < len(state_abbreviations):  # Check to ensure index is within the length of the states list
                cols = row.find_all('td')
                if cols:
                    # Get population data (assuming third td in each tr)
                    population = cols[2].text.strip().replace(',', '').replace('.', '')  # Population data
                    state = list(state_abbreviations.values())[i]  # Get the corresponding state abbreviation
                    population_data = population_data.append({'State': state, 'Year': year, 'Population': population}, ignore_index=True)

# Optionally, save the DataFrame to a CSV file
print(population_data)
population_data.to_csv("state_population_abbrev_2000_2016.csv", index=False)
