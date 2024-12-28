from socket import *

# Define server details
serverName = "127.0.0.1"
serverPort = 12000

# Create the UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get the file name from the user
sentence = input("Enter file name: ")

# Send the file name to the server
clientSocket.sendto(sentence.encode("utf-8"), (serverName, serverPort))

# Receive the server's response
filecontents, serverAddress = clientSocket.recvfrom(2048)

# Print the server's response
print("From Server:", filecontents.decode("utf-8"))

# Close the client socket
clientSocket.close()
