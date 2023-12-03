import pandas as pd
import matplotlib.pyplot as plt

file_path = 'industrial.xlsx'
data = pd.read_excel(file_path)

emissions_data = data.iloc[2:, 31:48]
emissions_data = emissions_data.apply(pd.to_numeric, errors='coerce')
average_emissions = emissions_data.mean()
years = list(range(2000, 2017))

plot_data = pd.DataFrame({
    'Year': years,
    'Average Emissions': average_emissions.values
})

plt.figure(figsize=(10, 6))
plt.plot(plot_data['Year'], plot_data['Average Emissions'], marker='o')
plt.title('Average Industrial Emissions by Year (2000-2016)')
plt.xlabel('Year')
plt.ylabel('Average Emissions (million metric tons of CO2)')
plt.grid(True)
plt.show()
