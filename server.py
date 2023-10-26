# Import necessary modules from pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Create an authorizer with user accounts
authorizer = DummyAuthorizer()  # Create a DummyAuthorizer for managing user accounts

# Add a user account with the username "admin" and password "admin"
# The user has permissions to read (e), list (l), retrieve (r), append (a), delete (d), store (f), and make directories (m).
# You can customize these permissions as needed.
authorizer.add_user("admin", "admin", "ftp", perm="elradfmw", msg_login="Login successful.", msg_quit="Goodbye.")

# Create an FTP handler
handler = FTPHandler
handler.authorizer = authorizer  # Assign the authorizer to the handler

# Create and start the FTP server
server = FTPServer(("0.0.0.0", 21), handler)  # Listen on all available network interfaces on port 21 (the default FTP port)
server.serve_forever()  # Start the server and serve client requests indefinitely