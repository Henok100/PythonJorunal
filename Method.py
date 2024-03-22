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

num_UAVs = 2

# Generate the list of CSV filenames
# csv_filename = [f'City_Profiles/{city_profile}/20_m/20_m_{i}_path_test.csv' for i in range(num_UAVs)]
# csv_filename = [f'City_Profiles/{city_profile}/60_m/60_m_{i}_path_test.csv' for i in range(num_UAVs)]
csv_filename = [f'City_Profiles/{city_profile}/120_m/120_m_{i}_path_test.csv' for i in range(num_UAVs)]


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
    # Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')
 
    # Valencia

    ###
    #For Separation Test
    # if i == 0:
    #     Location1['x(m)'] = Location1['x(m)'] - 729013.96
    #     Location1['y(m)'] = Location1['y(m)'] - 4371261.32
        
    # elif i == 1:
    #     Location1['x(m)'] = Location1['x(m)'] - 728643.96
    #     Location1['y(m)'] = Location1['y(m)'] - 4371261.32
    ###
    
    #For UAV-UAV
    # if i == 0:
    #     Location1['x(m)'] = Location1['x(m)'] - 727922.10
    #     Location1['y(m)'] = Location1['y(m)'] - 4372031.83

    # elif i == 0:
    #     Location1['x(m)'] = Location1['x(m)'] - 727922.10		
    #     Location1['y(m)'] = Location1['y(m)'] - 4372031.83
        
    # elif i == 1:
    #     Location1['x(m)'] = Location1['x(m)'] - 728402.94
    #     Location1['y(m)'] = Location1['y(m)'] - 4371914.10

   
    # elif i == 2:
    #     Location1['x(m)'] = Location1['x(m)'] - 728843.96
    #     Location1['y(m)'] = Location1['y(m)'] - 4371961.32   

    # elif i == 3:
    #     Location1['x(m)'] = Location1['x(m)'] - 727511.47
    #     Location1['y(m)'] = Location1['y(m)'] - 4372280.28


    # elif i == 4:
    #     Location1['x(m)'] = Location1['x(m)'] - 728825.40			
    #     Location1['y(m)'] = Location1['y(m)'] - 4371810.62
        
    # elif i == 5:
    #     Location1['x(m)'] = Location1['x(m)'] - 728043.88	
    #     Location1['y(m)'] = Location1['y(m)'] - 4371727.53

    # elif i == 6:
    #     Location1['x(m)'] = Location1['x(m)'] - 728256.43	
    #     Location1['y(m)'] = Location1['y(m)'] - 4372214.30
        
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