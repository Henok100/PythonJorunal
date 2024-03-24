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
numUavs = 6   #Change the number as desired.
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

city_profile = "Valencia"

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
    ###  for LOS path (Mobile)
    # Mov4 = M.Mov4()
    # Mov6 = M.Mov6()
    # Mov8 = M.Mov8() 
    # Mov10 = M.Mov10()
    for Rowindex in range(NUMRows):
        if counter % 2 == 0: ## remove this conditional if your PC is high End.
            SendProtocolMessage()
        
        for UAVindex in range(numUavs):
            temp = XYZ_NumPyArray[UAVindex]
            # #For UAV to omnet GND (static)
            # if UAVindex == 1:
            #     x = 210
            #     y = -100
            #     z = 0
            # elif UAVindex == 3:
            #     x = 210
            #     y = -200
            #     z = 0
            # elif UAVindex == 5:
            #     x = 210
            #     y = 0
            #     z = 0
            # elif UAVindex == 7:
            #     x = 210
            #     y = 100
            #     z = 0
            # elif UAVindex == 9:
            #     x = 210
            #     y = 200
            #     z = 0
            # elif UAVindex == 2:
            #     x = Mov2[Rowindex][0]
            #     y = Mov2[Rowindex][1]
            #     z = Mov2[Rowindex][2]
            # elif UAVindex == 4:
            #     x = Mov4[Rowindex][0]
            #     y = Mov4[Rowindex][1]
            #     z = Mov4[Rowindex][2]
            # elif UAVindex == 6:
            #     x = Mov6[Rowindex][0]
            #     y = Mov6[Rowindex][1]
            #     z = Mov6[Rowindex][2]
            # elif UAVindex == 8:
            #     x = Mov8[Rowindex][0]
            #     y = Mov8[Rowindex][1]
            #     z = Mov8[Rowindex][2]    
            # elif UAVindex == 10:
            #     x = Mov10[Rowindex][0]
            #     y = Mov10[Rowindex][1]
            #     z = Mov10[Rowindex][2]         
            # elif UAVindex == 0:
            #     x = temp[Rowindex][0]
            #     y = temp[Rowindex][1]
            #     z = temp[Rowindex][2]               
             ## For UAV to UAV (uncomment the 3 lines below)
             ## Commnet line 97 - 101 and 109 - 152
            x = temp[Rowindex][0]
            y = temp[Rowindex][1]
            z = temp[Rowindex][2]
            toSend = f"{round(x, 1)},{round(y, 1)},{round(z, 1)}"

            print(toSend)
            print("UAV ", str(UAVindex))
            ClientSocket.sendto(toSend.encode(FORMAT), ADDR[UAVindex])
        counter = counter + 1
        t = t + 1
        time.sleep(Time[t+1] - Time[t])    
Send()