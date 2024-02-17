import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

""" For Meduim_Urban """

""" files = ['Meduim_Urban/BAR_UAVtoVeh_NLOS/TRG.csv', \
         'Meduim_Urban/BAR_UAVtoVeh_NLOS/LNS.csv', \
         'Meduim_Urban/BAR_UAVtoVeh_NLOS/RF.csv', \
         'Meduim_Urban/BAR_UAVtoVeh_NLOS/NF.csv'] """

""" For High_Urban """

""" files = ['High_Urban/NY_UAVtoVeh_NLOS/TRG.csv', \
         'High_Urban/NY_UAVtoVeh_NLOS/LNS.csv', \
         'High_Urban/NY_UAVtoVeh_NLOS/RF.csv', \
         'High_Urban/NY_UAVtoVeh_NLOS/NF.csv'] """

"""For Comparision """
files = ['Comparision/UAV_TO_VEH_NLOS/_60m/TRG.csv', \
         'Comparision/UAV_TO_VEH_NLOS/_60m/LNS.csv', \
         'Comparision/UAV_TO_VEH_NLOS/_60m/RF.csv', \
         'Comparision/UAV_TO_VEH_NLOS/_60m/NF.csv']

files=['Dense/UPV.csv', 'Medium/Madrid.csv']

data = []
#xlabel = ['TwoRayGround','LogNormalShadowing', 'RicianFading', 'NakagamiFading']
xlabel = ['Dense[UPV]', 'Sparse[Madrid]']

# Read the CSV file into a pandas DataFrame
for i in range(2):
    data.append(pd.read_csv(files[i]))

# Create a figure and axis object
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(25, 25))

# Extract the header row as a list
headers = list(data[0].columns)


# Create a box plot of the data
for i, ax in enumerate(axs):
    ax.boxplot(data[i])
    ax.set_xticklabels(headers)

# Add space between subplots
fig.subplots_adjust(wspace=0.4)

# Set the y-axis tick formatter to display values as percent
for i, ax in enumerate(axs):
    ax.set_ylim(0, 1)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    ax.set_xlabel(xlabel[i], fontsize = 16).set_color('blue')
    ax.set_ylabel('Packet Delivery Ratio', fontsize = 16).set_color('blue')

# Super Title
plt.suptitle("UAV-to-UAV Performance Comaprision [Rician Fading Channel Model]", fontsize=24).set_color('blue')

# Display the plot
plt.show()