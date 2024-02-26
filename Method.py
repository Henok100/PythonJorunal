"""
    Title: A collection of various methods that aids the clinetUDP1 script.

    By Henok Gashaw 

    2023, Bahir Dar Ethiopia
"""
#importing Libraries

import numpy as np
import pandas as pd
import socket
df = []
XYZ_NumPyArray = []

"""
    The path_test file(s) is(are) needed from Ardusim!
    We first assign these files to *csv_filename* list.

    must be the same as the clientUDP1's *csv_filename*.
"""
city_profile = "Valencia"

num_UAVs = 7

# Generate the list of CSV filenames
csv_filename = [f'City_Profiles/{city_profile}/20_m/20_m_{i}_path_test.csv' for i in range(num_UAVs)]
# csv_filename = [f'City_Profiles/{city_profile}/60_m/60_m_{i}_path_test.csv' for i in range(num_UAVs)]
# csv_filename = [f'City_Profiles/{city_profile}/120_m/120_m_{i}_path_test.csv' for i in range(num_UAVs)]


# Returns a PORT list according to the number of UAVs
def PortList(numUavs):
    return [8000 + i for i in range(numUavs)]

# Returns an ADDR list
def AddrList(Client, Port, numUavs):
    return [(Client, Port[i]) for i in range(numUavs)]

# Get the host name
def GetHostName():
    return socket.gethostbyname(socket.gethostname())

# Create a UDP socket
def SocketCreator():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Drop unnecessary columns from the DataFrame
def ColumnDropper(Dataframe):
    return Dataframe.drop(['t(s)', 'zRelative(m)', 'heading(rad)', 's(m/s)', 'a(m/s²)', 'Δd(m)', 'd(m)'], axis=1)

# Create a list of DataFrames by reading and preprocessing the CSV files
def DataFrameListMaker(numUavs):
    return [ColumnDropper(pd.read_csv(csv_filename[i])) for i in range(numUavs)]

# Extract the time column from the DataFrame
def TimeExtractor(DataFrame):
    return DataFrame['t(s)']

# Preprocess the DataFrame by subtracting the center point of the path
def PreProcessor(df, i):
    Location1 = df.round(1)
    Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')
 
    # Valencia
    # Path 1
    if i == 0:
        Location1['x(m)'] = Location1['x(m)'] - 728813.96
        Location1['y(m)'] = Location1['y(m)'] - 4371921.32
        #print("path-1")

    # Path 2
    elif i == 1:
        Location1['x(m)'] = Location1['x(m)'] - 729098.96
        Location1['y(m)'] = Location1['y(m)'] - 4371921.32     
        #print("path-2")

    # Path 3
    elif i == 2:
        Location1['x(m)'] = Location1['x(m)'] - 727834.36
    #     # Location1['x(m)'] = Location1['x(m)'] - 727884.36  
    #     # Location1['x(m)'] = Location1['x(m)'] - 727934.36
    #     # Location1['x(m)'] = Location1['x(m)'] - 727984.36  
    #     # Location1['x(m)'] = Location1['x(m)'] - 728034.36
    #     # Location1['x(m)'] = Location1['x(m)'] - 728084.36
    #     # Location1['x(m)'] = Location1['x(m)'] - 728134.36
    #     # Location1['x(m)'] = Location1['x(m)'] - 728184.36    
    #     # Location1['x(m)'] = Location1['x(m)'] - 728234.36 
    #     # Location1['x(m)'] = Location1['x(m)'] - 728284.36 
    #     # Location1['x(m)'] = Location1['x(m)'] - 728334.36 
    #     # Location1['x(m)'] = Location1['x(m)'] - 728384.36 
    #     # Location1['x(m)'] = Location1['x(m)'] - 728434.36 
    #     # Location1['x(m)'] = Location1['x(m)'] - 728484.36 
        Location1['y(m)'] = Location1['y(m)'] - 4372110.67
        
    #     #print("path-3")

    # # Path 4
    elif i == 3:
        Location1['x(m)'] = Location1['x(m)'] - 726922.31	
    #     # Location1['x(m)'] = Location1['x(m)'] - 726972.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727022.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727072.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727122.31	
    #     # Location1['x(m)'] = Location1['x(m)'] - 727172.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727222.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727272.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727322.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727372.31		
    #     # Location1['x(m)'] = Location1['x(m)'] - 727422.31	
    #     # Location1['x(m)'] = Location1['x(m)'] - 727472.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727522.31
    #     # Location1['x(m)'] = Location1['x(m)'] - 727572.31					
        Location1['y(m)'] = Location1['y(m)'] - 4372285.43
        
    elif i == 4:
        Location1['x(m)'] = Location1['x(m)'] - 729549.62		
        Location1['y(m)'] = Location1['y(m)'] - 4371828.58


    # Path 6
    elif i == 5:
        Location1['x(m)'] = Location1['x(m)'] - 728009.36 	
        Location1['y(m)'] = Location1['y(m)'] - 4371814.94
        
        #print("path-6")

    elif i == 6:
        Location1['x(m)'] = Location1['x(m)'] - 728206.59 		
        Location1['y(m)'] = Location1['y(m)'] - 4372073.32
        
    Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')

    NumPyArray = Location1.to_numpy()

    return NumPyArray

# Create a list of NumPy arrays by preprocessing the DataFrames
def NumPyArrayMaker(XYZ_Dataframe, numUavs):
    return [PreProcessor(XYZ_Dataframe[i], i) for i in range(numUavs)]

# Get the number of rows in a NumPy array
def numRows(NumPyArray):
    return np.shape(NumPyArray)[0]

# Extract the location from a NumPy array
def LocationExtractor(NumPyArray, i):
    return [NumPyArray[i][0], NumPyArray[i][1], NumPyArray[i][2]]