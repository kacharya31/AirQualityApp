import json
import pandas as pd

# Load the aggregated O3 data
aggregated_data_path = 'aggregated_ozone_by_state_and_year.csv'
o3_data = pd.read_csv(aggregated_data_path)

# Load the GeoJSON file
geojson_file_path = 'states.geojson'
with open(geojson_file_path, 'r') as file:
    geojson_data = json.load(file)

# Merge the O3 data with the GeoJSON features
for feature in geojson_data['features']:
    state_code = feature['properties']['STUSPS']

    # Adding O3 data for each year to the GeoJSON properties
    for year in range(2000, 2017):
        # Extract the O3 value for the specific state and year
        o3_value = o3_data[(o3_data['STATE'] == state_code) & (o3_data['YEAR'] == year)]['ozone'].values
        if len(o3_value) > 0:
            feature['properties'][f'ozone_{year}'] = o3_value[0]
        else:
            # If no data is available for a particular year, set it to None or a default value
            feature['properties'][f'ozone_{year}'] = None

# Saving the modified GeoJSON to a new file
modified_geojson_path = 'modified_states_geojson.json'
with open(modified_geojson_path, 'w') as file:
    json.dump(geojson_data, file)

modified_geojson_path