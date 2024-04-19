import matplotlib.pyplot as plt
import pandas as pd

# Example data
uav_numbers = [2, 3, 4, 5, 6]
channel_models = ['Log Distance', 'Rician', 'Nakagami']
flight_altitudes = [20, 60, 120]

# Example data for total packets received (replace with your actual data)
total_packets_received = [
    [[162, 248, 486], [162, 242, 486], [160, 239, 479]],
    [[162, 247,	671], [159,	243,	669], [159,	246, 657]],
    [[201,	395,	1132], [198,	385,	1121], [200,	381,	1101]],
    [[352,	612,	1514], [352,	602,	1503], [344,	599,	1469]],
    [[422,	708,	1689], [422,	706,	1682], [411,	703,	1656]]
]

# Example data for PDR values (replace with your actual data)
pdr_values = [
    [[0.1300,	0.20,	0.39], [0.1300,	0.1942,	0.3900], [0.1284,	0.1918,	0.3844]],
    [[0.0867,	0.13,	0.36], [0.0851,	0.1300,	0.3579], [0.0851,	0.1316,	0.3515]],
    [[0.0807,	0.16,	0.45], [0.0795,	0.1545,	0.4498], [0.0803,	0.1529,	0.4418]],
    [[0.1130,	0.1965,	0.49], [0.1130,	0.1933,	0.4825], [0.1104,	0.1923,	0.4716]],
    [[0.1129,	0.1894,	0.45], [0.1129,	0.1889,	0.4500], [0.1100,	0.1881,	0.4430]]
]

# # Create a table using pandas DataFrame
# table_data = pd.DataFrame(index=uav_numbers, columns=pd.MultiIndex.from_product([channel_models, flight_altitudes]))
# for i, uav in enumerate(uav_numbers):
#     for j, channel_model in enumerate(channel_models):
#         for k, altitude in enumerate(flight_altitudes):
#             table_data.loc[uav, (channel_model, altitude)] = f"{total_packets_received[i][j][k]} ({pdr_values[i][j][k]:.2f})"
# #print(table_data)

# Create line graphs
plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green']
linestyles = ['-', '--', ':']
for j, channel_model in enumerate(channel_models):
    for k, altitude in enumerate(flight_altitudes):
        plt.plot(uav_numbers, [pdr_values[i][j][k] for i in range(len(uav_numbers))], marker='o',
                 color=colors[k], linestyle=linestyles[j],
                 label=f'{channel_model}, Altitude {altitude}m')
plt.xlabel('Number of UAVs')
plt.ylabel('Packet Delivery Ratio (PDR)')
plt.legend(title='Channel model and Flight Altitude')
plt.grid(True)
plt.show()