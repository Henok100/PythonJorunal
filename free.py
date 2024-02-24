import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('obstacle_free.csv')

# Extract x and y data from the CSV columns
x = data.iloc[:, 0]
y = data.iloc[:, 1]
# Apply moving average smoothing
window_size = 5
y_smooth = y.rolling(window_size, min_periods=1).mean()

# Create a line plot with smoothed data
plt.plot(x, y_smooth)

# Add labels and title
plt.xlabel('UAV-UAV-Separation', fontsize=12)
plt.ylabel('Packet Delivery Ratio', fontsize=12)
plt.title('')

# Display the graph
plt.show()