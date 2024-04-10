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

# Create a figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data
ax.plot(x, y_smooth)
ax.set_xlabel('UAV-UAV-Separation', fontsize=12)
ax.set_ylabel('Packet Delivery Ratio', fontsize=12)
ax.set_title('Obstacle_Free')

# Save the figure
plt.savefig('Obstacle_Free.png', dpi=300)

# Display the figure
plt.show()