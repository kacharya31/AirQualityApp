import json
import pandas as pd

# Load the aggregated data for each pollutant
o3_data = pd.read_csv('aggregated_ozone_by_state_and_year.csv')
no2_data = pd.read_csv('aggregated_no2_by_state_and_year.csv')
pm25_data = pd.read_csv('aggregated_pm25_by_state_and_year.csv')

# Load the GeoJSON file
geojson_file_path = 'states.geojson'
with open(geojson_file_path, 'r') as file:
    geojson_data = json.load(file)

# Function to add pollutant data to GeoJSON features
def add_pollutant_data(pollutant_data, feature, state_code, year, pollutant_name):
    pollutant_value = pollutant_data[(pollutant_data['STATE'] == state_code) & (pollutant_data['YEAR'] == year)][pollutant_name].values
    if len(pollutant_value) > 0:
        feature['properties'][f'{pollutant_name}_{year}'] = pollutant_value[0]
    else:
        feature['properties'][f'{pollutant_name}_{year}'] = None

# Merge the pollutant data with the GeoJSON features
for feature in geojson_data['features']:
    state_code = feature['properties']['STUSPS']
    for year in range(2000, 2017):
        add_pollutant_data(o3_data, feature, state_code, year, 'ozone')
        add_pollutant_data(no2_data, feature, state_code, year, 'no2')
        add_pollutant_data(pm25_data, feature, state_code, year, 'pm25')

# Saving the modified GeoJSON to a new file
modified_geojson_path = 'modified_states_geojson.json'
with open(modified_geojson_path, 'w') as file:
    json.dump(geojson_data, file)
