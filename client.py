# Import necessary libraries
import os
from ftplib import FTP

# Connect to the FTP server
ftp = FTP("127.0.0.1")
ftp.connect(port=21)  # You can omit the port argument since 21 is the default FTP port

# Login to the FTP server with your credentials
ftp.login(user="admin", passwd="admin")  # Replace with your server username and password

# List the files in the remote FTP directory

files = ftp.nlst("upload")
print("Remote files are following:")
if len(files) == 0:
    print("No files found in the remote directory.")
else:
    for file in files:
        print(file)
print("---------------------------------")
# Main loop for user interaction
while True:
    # Display menu options
    print("Options:")
    print("1. Upload a file")
    print("2. Download a file")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Upload a file to the server
        local_filename = input("Enter the local file path to upload: ")
        remote_path = os.path.join("upload", os.path.basename(local_filename))

        # Open the local file and upload it to the remote FTP server
        with open(local_filename, "rb") as file:
            ftp.storbinary(f"STOR {remote_path}", file)
            print(f"File uploaded successfully to 'ftp/upload/{os.path.basename(local_filename)}'!")

    elif choice == "2":
        # Download a file from the server
        filename = input("Enter the remote file path to download: ")
        local_path = os.path.join("ftp/download", os.path.basename(filename))

        # Open a local file and download the remote file from the FTP server
        with open(local_path, "wb") as file:
            ftp.retrbinary(f"RETR {filename}", file.write)
            print(f"File downloaded successfully to 'ftp/download/{os.path.basename(filename)}'!")

    elif choice == "3":
        # Quit the FTP session and exit the loop
        ftp.quit()
        break
