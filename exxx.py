import matplotlib.pyplot as plt
import pandas as pd

# Example data
uav_numbers = [2, 3, 4, 5, 6]
channel_models = ['Log Distance', 'Rician', 'Nakagami']
flight_altitudes = [20, 60, 120]

# Example data for PDR values (replace with your actual data)
pdr_values = [
    [[0.1779,	0.2383,	0.4362], [0.1745,	0.2383,	0.4362], [0.1745,	0.2282,	0.4597]],
    [[0.1275,	0.1700,	0.3177], [0.1253,	0.1723,	0.3132], [0.1253,	0.1700,	0.3065]],
    [[0.1544,	0.2013,	0.3826], [0.1527,	0.1997,	0.3826], [0.1527,	0.1997,	0.3842]],
    [[0.1248,	0.1611,	0.3060], [0.1248,	0.1611,	0.3047], [0.1208,	0.1597,	0.3034]],
    [[0.1376,	0.1834,	0.3333], [0.1365,	0.1846,	0.3333], [0.1376,	0.1801,	0.3277]]
]

# Create line graphs
plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green']
linestyles = ['-', '--', ':']
for j, channel_model in enumerate(channel_models):
    for k, altitude in enumerate(flight_altitudes):
        plt.plot(uav_numbers, [pdr_values[i][j][k] for i in range(len(uav_numbers))], marker='o',
                 color=colors[k], linestyle=linestyles[j],
                 label=f'{channel_model}, Altitude {altitude}m')

plt.xlabel('Number of UAVs', fontsize=16)  # Increase x-axis label font size
plt.ylabel('Packet Delivery Ratio', fontsize=16)  # Increase y-axis label font size
plt.legend(title='Channel model and Flight Altitude', fontsize=16)  # Increase legend font size
plt.grid(True)
plt.xticks(uav_numbers, uav_numbers)
# plt.gca().xaxis.set_major_locator(plt.MaxNLocator(len(uav_numbers)))
plt.tick_params(axis='both', which='major', labelsize=16)  # Increase tick label font size
plt.show()