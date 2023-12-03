import json
import pandas as pd

# Load the original data
o3_data = pd.read_csv('aggregated_ozone_by_state_and_year.csv')
no2_data = pd.read_csv('aggregated_no2_by_state_and_year.csv')
pm25_data = pd.read_csv('aggregated_pm25_by_state_and_year.csv')

# Load additional datasets
coal_data = pd.read_csv('coal.csv')
gas_data = pd.read_csv('gas_data.csv')
petroleum_data = pd.read_csv('petroleum.csv')
population_data = pd.read_csv('population.csv')

# Correct the State column for merging
coal_data = coal_data.rename(columns={'State': 'STATE'})
gas_data = gas_data.rename(columns={'State': 'STATE'})
petroleum_data = petroleum_data.rename(columns={'State': 'STATE'})
population_data = population_data.rename(columns={'State': 'STATE'})

coal_data = coal_data.rename(columns={'Year': 'YEAR'})
gas_data = gas_data.rename(columns={'Year': 'YEAR'})
petroleum_data = petroleum_data.rename(columns={'Year': 'YEAR'})
population_data = population_data.rename(columns={'Year': 'YEAR'})

# Function to merge pollutant data into GeoJSON features
def merge_data(geojson_data, data, key, feature_key):
    for feature in geojson_data['features']:
        state_code = feature['properties']['STUSPS']
        for year in range(2000, 2017):
            value = data[(data['STATE'] == state_code) & (data['YEAR'] == year)][key].values
            if len(value) > 0:
                feature['properties'][f'{key}_{year}'] = round(value[0], 2)
            else:
                feature['properties'][f'{key}_{year}'] = None

# Load the GeoJSON file
with open('states.geojson', 'r') as file:
    geojson_data = json.load(file)

# Merge each dataset into the GeoJSON
merge_data(geojson_data, o3_data, 'ozone', 'OZONE')
merge_data(geojson_data, no2_data, 'no2', 'NO2')
merge_data(geojson_data, pm25_data, 'pm25', 'PM2.5')
merge_data(geojson_data, coal_data, 'Coal', 'COAL')
merge_data(geojson_data, gas_data, 'gas_data', 'GAS')
merge_data(geojson_data, petroleum_data, 'Petroleum', 'PETROLEUM')
merge_data(geojson_data, population_data, 'Population Density', 'POP_DENSITY')

# Save the modified GeoJSON
with open('modified_states_geojson.json', 'w') as file:
    json.dump(geojson_data, file)
