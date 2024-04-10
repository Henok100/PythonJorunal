"""
    Title: A simple script that reads, preprocess and send UAV locations to OMNeT++ from a CSV file

    By Henok Gashaw 

    2023, Bahir Dar Ethiopia
"""

# Importing Libraries
import Method
import Movment as M
import json
import time
import pandas as pd

CLIENT = Method.GetHostName()
FORMAT = 'utf-8'

#For UAVs
numUavs = 2   #Change the number as desired.
numRows = []
LocationList = []

PORT = Method.PortList(numUavs)
ADDR = Method.AddrList(CLIENT, PORT, numUavs) 

#For Protocol Message
PORT_Protocol = 9000
ADDR_Protocol = (CLIENT, PORT_Protocol)  


"""
    The path_test file(s) is(are) needed from Ardusim!
    We first assign these files to *csv_filename* list.

    must be the  same as the Method's *csv_filename*.
"""

# city_profile = "Valencia"
# city_profile = "Barcelona"
city_profile = "Madrid"

csv_filename = [f'City_Profiles/{city_profile}/20_m/20_m_{i}_path_test.csv' for i in range(numUavs)]
# csv_filename = [f'City_Profiles/{city_profile}/60_m/60_m_{i}_path_test.csv' for i in range(numUavs)]
# csv_filename = [f'City_Profiles/{city_profile}/120_m/120_m_{i}_path_test.csv' for i in range(numUavs)]


ClientSocket = Method.SocketCreator()

XYZ_Dataframe = Method.DataFrameListMaker(numUavs)

Time = Method.TimeExtractor(pd.read_csv(csv_filename[0]))
XYZ_NumPyArray= Method.NumPyArrayMaker(XYZ_Dataframe, numUavs)

for i in range(numUavs):
     numRows.append(Method.numRows(XYZ_NumPyArray[i])) 

NUMRows = min(numRows)  #for accuracy, since the rows of the csv file are not equal

#for Protocol message
def SendProtocolMessage():        
    for j in range(numUavs-1):
        message = {"senderID":0,"receiverID":j,"payload":"Hello"}
        ClientSocket.sendto(json.dumps(message).encode(FORMAT), ADDR_Protocol)

def Send():
    t = -1
    counter = 1
    for Rowindex in range(NUMRows):
        #if counter % 2 == 0: ## remove this conditional if your PC is high End.
        SendProtocolMessage()
        
        for UAVindex in range(numUavs):
            # Valencia
            # if UAVindex == 6:
            #     x = 176.8
            #     y = 152.6
            #     z = 0
            # elif UAVindex == 7:
            #     x = 76.8
            #     y = -147.4
            #     z = 0
            # elif UAVindex == 8:
            #     x = -323.2
            #     y = -147.4
            #     z = 0
            # elif UAVindex == 9:
            #     x = -323.2
            #     y = 52.6
            #     z = 0
            # elif UAVindex == 10:
            #     x = -323.2
            #     y = 252.6
            #     z = 0   

            # Barcelona
            # if UAVindex == 6:
            #     x = -116.8
            #     y = 372.6
            #     z = 0
            # elif UAVindex == 7:
            #     x = 196.8
            #     y = -107.4
            #     z = 0
            # elif UAVindex == 8:
            #     x = 423.2
            #     y = -247.4
            #     z = 0
            # elif UAVindex == 9:
            #     x = 423.2
            #     y = 152.6
            #     z = 0
            # elif UAVindex == 10:
            #     x = -233.2
            #     y = 102.6
            #     z = 0  

            #   Madrid
            # if UAVindex == 6:
            #     x = -576.8
            #     y = -650.6
            #     z = 0
            # elif UAVindex == 7:
            #     x = -956.8
            #     y = -552.6
            #     z = 0
            # elif UAVindex == 8:
            #     x = -956.8
            #     y = -852.6
            #     z = 0
            # elif UAVindex == 9:
            #     x = -586.8
            #     y = -950.6
            #     z = 0
            # elif UAVindex == 10:
            #     x = -856.8
            #     y = -752.6
            #     z = 0       
            # else: 
            temp = XYZ_NumPyArray[UAVindex]

            x = temp[Rowindex][0]
            y = temp[Rowindex][1]
            z = temp[Rowindex][2]
            toSend = f"{round(x, 1)},{round(y, 1)},{round(z, 1)}"
            print(toSend)
            ClientSocket.sendto(toSend.encode(FORMAT), ADDR[UAVindex])
        counter = counter + 1
        t = t + 1
        time.sleep(Time[t+1] - Time[t])    
Send()