# FTP Server and Client

This repository contains Python scripts for creating a basic FTP server and client. The server allows file uploads and downloads, while the client can be used to interact with the server.

## Prerequisites

Before using the FTP server and client, follow these steps:

### 1. Set Up a Virtual Environment

It's recommended to create and activate a virtual environment to isolate the project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
``` 

### 2. Install Dependencies

Once your virtual environment is active, you can install the required dependencies from the requirements.txt file.

```bash     
pip install -r requirements.txt
```

## Usage

### Server (server.py)

To run the FTP server, use the following command:
    
```bash 
    python server.py
```

The server will listen on all available network interfaces on port 21.

### Client (client.py)

To run the FTP client, use the following command:

```bash 
    python client.py
```

The client will connect to the FTP server using the IP address "127.0.0.1" and port 21. You can replace these values with your server's IP address and port.


## When prompted for options, you can:

### Upload a File:

1. Enter "1" and provide the local file path to upload. For example, you can use "test.txt" as a sample file.
Download a File:

2. Enter "2" and provide the remote file path to download. For example, if you previously uploaded "test.txt," enter "test.txt" when prompted. The downloaded file will be saved in the client's local directory.

3. Enter "3" to exit the client.
Feel free to customize the code and add more functionality as needed.

## Author
#### Danish Irfan

### LinkedIn
https://www.linkedin.com/in/danish-irfan-149830202/