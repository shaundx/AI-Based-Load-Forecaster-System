import pandas as pd
import matplotlib.pyplot as plt

# Dataset manually entered based on final version
data = {
    'Dataset': [1, 2, 3, 4, 5, 6],
    'Error (%)': [20.44, 18.68, 13.22, 10, 1.42, 0.38]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Dataset'], df['Error (%)'], marker='o', linestyle='-', linewidth=2, color='blue')
plt.title('Error Percentage Over Multiple Datasets')
plt.xlabel('Dataset Number')
plt.ylabel('Error (%)')
plt.grid(True)
plt.show()