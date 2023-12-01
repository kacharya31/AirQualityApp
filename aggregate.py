import pandas as pd

def aggregate_pollutant_data(data_folder, pollutant_name):
    dfs = []
    for year in range(2000, 2017):
        file_name = f'{data_folder}/{year}.rds.csv'
        yearly_data = pd.read_csv(file_name)
        yearly_data['YEAR'] = year
        dfs.append(yearly_data)
    
    combined_data = pd.concat(dfs, ignore_index=True)
    aggregated_data = combined_data.groupby(['STATE', 'YEAR'])[pollutant_name].mean().reset_index()
    return aggregated_data

o3_data = aggregate_pollutant_data('o3_data', 'ozone')
o3_data.to_csv('aggregated_o3_by_state_and_year.csv', index=False)

no2_data = aggregate_pollutant_data('no2_data', 'no2')
no2_data.to_csv('aggregated_no2_by_state_and_year.csv', index=False)

pm25_data = aggregate_pollutant_data('pm2.5_data', 'pm25')
pm25_data.to_csv('aggregated_pm25_by_state_and_year.csv', index=False)
