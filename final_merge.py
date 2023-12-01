import pandas as pd

o3_data = pd.read_csv('aggregated_o3_by_state_and_year.csv')
no2_data = pd.read_csv('aggregated_no2_by_state_and_year.csv')
pm25_data = pd.read_csv('aggregated_pm25_by_state_and_year.csv')

merged_data = o3_data.merge(no2_data, on=['STATE', 'YEAR']).merge(pm25_data, on=['STATE', 'YEAR'])

# Save the merged DataFrame to a new CSV file
merged_data.to_csv('aggregated_pollutants_by_state_and_year.csv', index=False)
