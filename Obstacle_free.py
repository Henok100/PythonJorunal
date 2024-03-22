import matplotlib.pyplot as plt
import pandas as pd

# Read the first CSV file
data1 = pd.read_csv('with_obstacle_Artificial.csv')

# Extract x and y data from the first CSV columns
x1 = data1.iloc[:, 0]
y1 = data1.iloc[:, 1]
# Apply moving average smoothing
window_size = 5
y1_smooth = y1.rolling(window_size, min_periods=1).mean()

# Read the second CSV file
data2 = pd.read_csv('with_obstacle_Real.csv')

# Extract x and y data from the second CSV columns
x2 = data2.iloc[:, 0]
y2 = data2.iloc[:, 1]
# Apply moving average smoothing
y2_smooth = y2.rolling(window_size, min_periods=1).mean()

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot the first data on the first subplot
ax1.plot(x1, y1_smooth)
ax1.set_xlabel('UAV-UAV-Separation', fontsize=12)
ax1.set_ylabel('Packet Delivery Ratio', fontsize=12)
ax1.set_title('Artificial')

# Plot the second data on the second subplot
ax2.plot(x2, y2_smooth)
ax2.set_xlabel('UAV-UAV-Separation', fontsize=12)
ax2.set_ylabel('Packet Delivery Ratio', fontsize=12)
ax2.set_title('Real')

# Adjust the spacing between subplots
fig.tight_layout()

# Save the figure
plt.savefig('Separation_test.png', dpi=300)

# Display the figure
plt.show()