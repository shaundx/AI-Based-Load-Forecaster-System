import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load Dataset
file_path = r'insert file path here'
data = pd.read_excel(file_path)

# Ensure correct structure
if 'Date' not in data.columns or 'Load' not in data.columns:
    raise KeyError("The dataset must include 'Date' and 'Load' columns.")

# Convert and clean
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
data = data.sort_index()

# Plot actual data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Load'], color='red', marker='o', label='Monthly Consumption (kW)')
plt.title('Monthly Electricity Consumption (Sep 2023 - Jan 2024)')
plt.xlabel('Date')
plt.ylabel('Consumption (kW)')
plt.grid(True)
plt.legend()
plt.show()

# SARIMA Forecasting
model = SARIMAX(data['Load'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit(disp=False)

forecast = model_fit.forecast(steps=1)

print("\n--------------------------------------------")
print(f"Forecasted Electricity Consumption for February: {forecast[0]:.2f} kW")
print("--------------------------------------------")