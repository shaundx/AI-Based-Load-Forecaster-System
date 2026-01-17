import pandas as pd  
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the dataset from the new Excel file
file_path = r'insert file path here'
data = pd.read_excel(file_path)

# Print the column names and first few rows to understand the structure                                                                                                                                                                                      
print("Column names:", data.columns)
print("Loaded Data Sample:")
print(data.head())

# Ensure the required columns exist
if 'Date' not in data.columns or 'Load' not in data.columns:
    raise KeyError("Expected columns 'Date' and 'Load' are not found in the dataset. Please verify the column names.")

# Convert 'Date' column to datetime and set it as the index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Filter the data from March to August 2024
data_filtered = data['2024-03-01':'2024-08-31']

# Sort the index
data_filtered = data_filtered.sort_index()

# Plot the filtered data for March to August 2024
plt.figure(figsize=(10, 6))
plt.plot(data_filtered.index, data_filtered['Load'], label='Monthly Consumption (kW)')
plt.title('Monthly Electricity Consumption (March - August 2024)')
plt.xlabel('Date')
plt.ylabel('Consumption (kW)')
plt.legend()
plt.grid(True)
plt.show()

# Fit a Seasonal ARIMA model to predict September's consumption
model = SARIMAX(data_filtered['Load'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit(disp=False)

# Forecast the next month (September)
forecast = model_fit.forecast(steps=1)

# Print the forecasted value for September
print(f"Forecasted Electricity Consumption for September: {forecast[0]:.2f} kW")