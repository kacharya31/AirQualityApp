import pandas as pd

# List to hold DataFrames temporarily
dfs = []

# Assuming files are named '2000.csv', '2001.csv', ..., '2016.csv'
for year in range(2000, 2017):
    # Construct the file name for each year
    file_name = f'o3_data/{year}.rds.csv'
    
    # Read the data from the year file
    yearly_data = pd.read_csv(file_name)
    
    # Add a column for the year
    yearly_data['YEAR'] = year
    
    # Add the yearly data to the list
    dfs.append(yearly_data)

# Combine all DataFrames in the list into one DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Group by STATE and YEAR and calculate the mean ozone levels
aggregated_data = combined_data.groupby(['STATE', 'YEAR'])['ozone'].mean().reset_index()

# Save the aggregated data to a new CSV file
aggregated_data.to_csv('aggregated_ozone_by_state_and_year.csv', index=False)
