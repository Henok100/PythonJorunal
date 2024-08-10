import matplotlib.pyplot as plt
import pandas as pd
import random

# Read the artificial CSV file
artificial_data = pd.read_csv('with_obstacle_Artificial.csv')

# Read the real CSV file
real_data = pd.read_csv('with_obstacle_Real.csv')

# Extract the relevant data for plotting from the artificial data
x1 = artificial_data['Distance']
y1 = artificial_data['PDR']

# Extract the relevant data for plotting from the real data
x2 = real_data['Distance']
y2 = real_data['PDR']

# Create a new figure and axis
fig, ax = plt.subplots()

# Set a larger font size
plt.rcParams.update({'font.size': 18})

# Plot the artificial data
ax.plot(x1, y1, label='Artificial')

# Annotate the specified distances for the artificial data
distances_artificial = [100, 200, 300, 400, 600, 500]
for distance in distances_artificial:
    index = x1.tolist().index(distance)
    ax.annotate(f'PDR: {y1[index]}', xy=(distance, y1[index]), xytext=(10, 10),
                textcoords='offset points', arrowprops=dict(arrowstyle="->"), color='blue')

# Plot the real data
ax.plot(x2, y2, label='Real')

# Annotate the specified distances for the real data
distances_real = [100, 200, 300, 400, 600, 500]
for distance in distances_real:
    index = x2.tolist().index(distance)
    ax.annotate(f'PDR: {y2[index]}', xy=(distance, y2[index]), xytext=(10, 10),
                textcoords='offset points', arrowprops=dict(arrowstyle="->"), color='red')

# Add labels and a legend with larger font size
ax.set_xlabel('UAV-UAV Separation', fontsize=25)
ax.set_ylabel('Packet Delivery Ratio', fontsize=25)
ax.legend(fontsize=25)

# Display the plot
plt.show()