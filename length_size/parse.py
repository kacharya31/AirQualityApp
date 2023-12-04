import os
import pandas as pd

folder_path = 'C:/Users/richi/OneDrive/Desktop/Data Viz/AirQualityApp/length_size'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

total_rows = 0

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    total_rows += len(df)

print(f'Total number of rows in the CSV files: {total_rows}')
