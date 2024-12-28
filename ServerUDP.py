from socket import *

# Define server details
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive")

while True:
    # Receive file name from the client
    sentence, clientAddress = serverSocket.recvfrom(2048)
    filename = sentence.decode("utf-8")  # Decode the file name
    try:
        # Try to open and read the requested file
        with open(filename, "r") as file:
            fileContents = file.read(2048)
            serverSocket.sendto(fileContents.encode("utf-8"), clientAddress)
        print(f"Sent back to client: {fileContents}")
    except FileNotFoundError:
        # Handle case where file does not exist
        errorMessage = f"Error: File '{filename}' not found"
        serverSocket.sendto(errorMessage.encode("utf-8"), clientAddress)
        print(errorMessage)
    except Exception as e:
        # Handle other exceptions
        errorMessage = f"Error: {str(e)}"
        serverSocket.sendto(errorMessage.encode("utf-8"), clientAddress)
        print(errorMessage)
