import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

files = ['20_m/FSP.csv', '20_m/LOG.csv', '20_m/RF.csv', '20_m/NF.csv']

data = []
xlabel = ['FreeSpace','Log-Distance', 'RicianFading', 'NakagamiFading']
# xlabel = ['Dense[UPV]', 'Sparse[Madrid]']

# Read the CSV file into a pandas DataFrame
for i in range(4):
    data.append(pd.read_csv(files[i]))

# Create a figure and axis object
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(25, 25))

# Extract the header row as a list
headers = list(data[0].columns)


# Create a box plot of the data
for i, ax in enumerate(axs):
    ax.boxplot(data[i])
    ax.set_xticklabels(headers, fontsize = 20)

# Add space between subplots
fig.subplots_adjust(wspace=0.4)

# Set the y-axis tick formatter to display values as percent
for i, ax in enumerate(axs):
    ax.set_ylim(0, 1)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    ax.set_xlabel(xlabel[i], fontsize = 24).set_color('blue')
    ax.set_ylabel('Packet Delivery Ratio', fontsize = 24).set_color('blue')

# Super Title
plt.suptitle("UAV-to-UAV Performance", fontsize=24).set_color('blue')

# Display the plot
plt.show()