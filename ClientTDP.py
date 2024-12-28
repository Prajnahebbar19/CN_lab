from socket import *

# Define server details
serverName = "127.0.0.1"
serverPort = 12000

# Create and connect the client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Get the file name from the user
sentence = input("Enter file name: ")

# Send the file name to the server
clientSocket.send(sentence.encode())

# Receive the server's response
filecontents = clientSocket.recv(1024).decode()

# Print the server's response
print("From Server:", filecontents)

# Close the client socket
clientSocket.close()
