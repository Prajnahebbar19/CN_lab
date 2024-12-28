from socket import *

# Define server details
serverName = "127.0.0.1"
serverPort = 12000

# Create and configure the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    # Accept a client connection
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with {addr}")

    try:
        # Receive the file name from the client
        sentence = connectionSocket.recv(1024).decode()

        # Try to open and read the requested file
        with open(sentence, "r") as file:
            fileContents = file.read(1024)
            connectionSocket.send(fileContents.encode())
    except FileNotFoundError:
        # Handle case where file does not exist
        errorMessage = f"Error: File '{sentence}' not found"
        connectionSocket.send(errorMessage.encode())
    except Exception as e:
        # Handle other exceptions
        errorMessage = f"Error: {str(e)}"
        connectionSocket.send(errorMessage.encode())
    finally:
        # Close the client connection
        connectionSocket.close()
