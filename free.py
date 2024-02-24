import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('data.csv')

# Extract x and y data from the CSV columns
x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Create a scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph from CSV')

# Display the graph
plt.show()