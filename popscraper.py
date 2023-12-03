import requests
from bs4 import BeautifulSoup
import pandas as pd

# State abbreviations
land_area_list = [
    {"State": "Alabama", "Land Area": 50645},
    {"State": "Arizona", "Land Area": 113594},
    {"State": "Arkansas", "Land Area": 52035},
    {"State": "California", "Land Area": 155779},
    {"State": "Colorado", "Land Area": 103642},
    {"State": "Connecticut", "Land Area": 4842},
    {"State": "Delaware", "Land Area": 1949},
    {"State": "District of Columbia", "Land Area": 61},
    {"State": "Florida", "Land Area": 53625},
    {"State": "Georgia", "Land Area": 57513},
    {"State": "Idaho", "Land Area": 82643},
    {"State": "Illinois", "Land Area": 55519},
    {"State": "Indiana", "Land Area": 35826},
    {"State": "Iowa", "Land Area": 55857},
    {"State": "Kansas", "Land Area": 81759},
    {"State": "Kentucky", "Land Area": 39486},
    {"State": "Louisiana", "Land Area": 43204},
    {"State": "Maine", "Land Area": 30843},
    {"State": "Maryland", "Land Area": 9707},
    {"State": "Massachusetts", "Land Area": 7800},
    {"State": "Michigan", "Land Area": 56539},
    {"State": "Minnesota", "Land Area": 79627},
    {"State": "Mississippi", "Land Area": 46923},
    {"State": "Missouri", "Land Area": 68742},
    {"State": "Montana", "Land Area": 145546},
    {"State": "Nebraska", "Land Area": 76824},
    {"State": "Nevada", "Land Area": 109781},
    {"State": "New Hampshire", "Land Area": 8953},
    {"State": "New Jersey", "Land Area": 7354},
    {"State": "New Mexico", "Land Area": 121298},
    {"State": "New York", "Land Area": 47126},
    {"State": "North Carolina", "Land Area": 48618},
    {"State": "North Dakota", "Land Area": 69001},
    {"State": "Ohio", "Land Area": 40861},
    {"State": "Oklahoma", "Land Area": 68595},
    {"State": "Oregon", "Land Area": 95988},
    {"State": "Pennsylvania", "Land Area": 44743},
    {"State": "Rhode Island", "Land Area": 1034},
    {"State": "South Carolina", "Land Area": 30061},
    {"State": "South Dakota", "Land Area": 75811},
    {"State": "Tennessee", "Land Area": 41235},
    {"State": "Texas", "Land Area": 261232},
    {"State": "Utah", "Land Area": 82170},
    {"State": "Vermont", "Land Area": 9217},
    {"State": "Virginia", "Land Area": 39490},
    {"State": "Washington", "Land Area": 66456},
    {"State": "West Virginia", "Land Area": 24038},
    {"State": "Wisconsin", "Land Area": 54158},
    {"State": "Wyoming", "Land Area": 97093},
]

land_area_df = pd.DataFrame(land_area_list)

state_abbreviations = {
    'Alabama': 'AL',  'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA',
    'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN',
    'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
    'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
    'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

land_area_df['State'] = land_area_df['State'].map(state_abbreviations)

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
            if i < len(state_abbreviations):
                cols = row.find_all('td')
                if cols:
                    population = cols[2].text.strip().replace(',', '').replace('.', '')
                    state = list(state_abbreviations.values())[i]
                    population_data = population_data.append({'State': state, 'Year': year, 'Population': population}, ignore_index=True)


population_data['Population'] = pd.to_numeric(population_data['Population'], errors='coerce')

merged_data = population_data.merge(land_area_df, on='State', how='inner')

merged_data['Population Density'] = merged_data['Population'] / merged_data['Land Area']

population_density_df = merged_data

#COAL DATA
coal_data = pd.read_excel('coal.xlsx', skiprows=2)  # Adjust the skiprows parameter if the header is not in the second row
state_names_to_abbreviations = {v: k for v, k in state_abbreviations.items()}
coal_long_format = coal_data.melt(id_vars='State', var_name='Year', value_name='Coal')
coal_long_format = coal_long_format[coal_long_format['State'] != "State total1"]

coal_long_format['Year'] = pd.to_numeric(coal_long_format['Year'], errors='coerce')

coal_long_format = coal_long_format.dropna(subset=['Year'])

coal_long_format['Year'] = coal_long_format['Year'].astype(int)

coal_long_format = coal_long_format.dropna(subset=['Coal'])
coal_long_format['Coal'] = pd.to_numeric(coal_long_format['Coal'], errors='coerce')

# Filter the DataFrame for the years 2000 to 2016
coal_long_format = coal_long_format[(coal_long_format['Year'] >= 2000) & (coal_long_format['Year'] <= 2016)]

coal_long_format['State'] = coal_long_format['State'].map(state_names_to_abbreviations)

#PETROLEUM DATA
petroleum_data = pd.read_excel('petroleum.xlsx', skiprows=2)  # Adjust the skiprows parameter if the header is not in the second row
state_names_to_abbreviations = {v: k for v, k in state_abbreviations.items()}
petroleum_data_df = petroleum_data.melt(id_vars='State', var_name='Year', value_name='Petroleum')
petroleum_data_df = petroleum_data_df[petroleum_data_df['State'] != "State total1"]

petroleum_data_df['Year'] = pd.to_numeric(petroleum_data_df['Year'], errors='coerce')

petroleum_data_df = petroleum_data_df.dropna(subset=['Year'])

petroleum_data_df['Year'] = petroleum_data_df['Year'].astype(int)

petroleum_data_df = petroleum_data_df.dropna(subset=['Petroleum'])
petroleum_data_df['Petroleum'] = pd.to_numeric(petroleum_data_df['Petroleum'], errors='coerce')

petroleum_data_df = petroleum_data_df[(petroleum_data_df['Year'] >= 2000) & (petroleum_data_df['Year'] <= 2016)]

petroleum_data_df['State'] = petroleum_data_df['State'].map(state_names_to_abbreviations)


# GAS DATA
gas_data_df = pd.read_excel('natural_gas.xlsx', skiprows=2)  # Adjust the skiprows parameter if the header is not in the second row
state_names_to_abbreviations = {v: k for v, k in state_abbreviations.items()}
gas_data_df = gas_data_df.melt(id_vars='State', var_name='Year', value_name='gas_data')
gas_data_df = gas_data_df[gas_data_df['State'] != "State total1"]

gas_data_df['Year'] = pd.to_numeric(gas_data_df['Year'], errors='coerce')

gas_data_df = gas_data_df.dropna(subset=['Year'])

gas_data_df['Year'] = gas_data_df['Year'].astype(int)

gas_data_df = gas_data_df.dropna(subset=['gas_data'])
gas_data_df['gas_data'] = pd.to_numeric(gas_data_df['gas_data'], errors='coerce')

# # Filter the DataFrame for the years 2000 to 2016
gas_data_df = gas_data_df[(gas_data_df['Year'] >= 2000) & (gas_data_df['Year'] <= 2016)]

gas_data_df['State'] = gas_data_df['State'].map(state_names_to_abbreviations)

petroleum_data_df = petroleum_data_df.dropna(subset = ['State'])
coal_long_format = coal_long_format.dropna(subset = ['State'])
gas_data_df = gas_data_df.dropna(subset = ['State'])

population_density_df.to_csv('population.csv')
petroleum_data_df.to_csv('petroleum.csv')
coal_long_format.to_csv('coal.csv')
gas_data_df.to_csv('gas_data.csv')
