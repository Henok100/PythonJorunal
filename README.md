# **ArdusimMockup**

This repository contains two Python scripts: `Method_for_clientUDP.py` and `clientUDP.py`, which work together to read, preprocess, and send UAV locations to OMNeT++ over UDP from CSV files. These scripts are designed to aid in simulations of multiple UAVs by sending real-time location data to a network simulator such as OMNeT++.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Overview

The `Method_for_clientUDP.py` script provides helper methods to the main `clientUDP.py` script. Together, these scripts read UAV location data from CSV files, preprocess it, and send the data to a server using the UDP protocol. This is useful for simulations involving UAVs, particularly in cases where location data needs to be sent dynamically to OMNeT++.

### Features

- Reads and processes CSV files containing UAV path data.
- Sends UAV locations over UDP for simulation purposes.
- Supports different numbers of UAVs.
- Configurable city profiles for various simulation environments (e.g., Valencia, Barcelona, Madrid).

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Henok100/PythonJorunal.git
    ```

2. **Install required libraries:**

    ```bash
    pip install numpy pandas
    ```

3. **Ensure that OMNeT++ is installed and running:** Make sure that the number of UAVs in OMNeT++ matches the number specified in `clientUDP.py`.

4. **Prepare the CSV files:** Ensure the CSV files are placed in the correct city profile directory, such as `City_Profiles/Valencia/20_m/`.

## Usage

1. **Configure the simulation:**

    - Set the `city_profile` variable in both `Method_for_clientUDP.py` and `clientUDP.py` to the desired city (e.g., `Valencia`, `Barcelona`, `Madrid`).
    - Specify the number of UAVs (`numUAVs`) in `clientUDP.py`. Make sure this number matches the number of UAVs in OMNeT++.

2. **Run the main script:**

    ```bash
    python clientUDP.py
    ```

    This will read the location data from the CSV files and send it to OMNeT++ via UDP.

3. **Simulation Data:**

    - The data sent includes x, y, and z coordinates of the UAVs. It is rounded to one decimal place and sent as a formatted string.

## Project Structure

- **`Method_for_clientUDP.py`**: Contains helper methods for reading, processing, and sending data.
- **`clientUDP.py`**: The main script responsible for sending UAV location data to OMNeT++.
- **`City_Profiles/`**: Directory containing UAV path CSV files categorized by city and altitude.

### Helper Methods

- **`PortList(numUavs)`**: Generates a list of ports for the UAVs.
- **`AddrList(Client, Port, numUavs)`**: Creates a list of addresses for the UAVs.
- **`SocketCreator()`**: Creates and returns a UDP socket.
- **`DataFrameListMaker(numUavs)`**: Reads and processes CSV files into pandas DataFrames.
- **`PreProcessor(df, i)`**: Preprocesses UAV location data by adjusting for the city center.
- **`NumPyArrayMaker(XYZ_Dataframe, numUavs)`**: Converts processed DataFrames into NumPy arrays for easier handling of location data.

### Example CSV Filenames

Ensure that your CSV files are correctly named and placed in the appropriate directories. For instance, example filenames for Valencia (at 20 meters) would look like:

```bash
City_Profiles/Valencia/20_m/20_m_0_path_test.csv
City_Profiles/Valencia/20_m/20_m_1_path_test.csv
...
