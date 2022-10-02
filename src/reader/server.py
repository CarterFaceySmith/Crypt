# Imports
import socket, threading, enCrypt

# Program settings
bufferSize = 1024
title = "\n   ______                 __ \n  / ____/______  ______  / /_\n / /   / ___/ / / / __ \/ __/\n/ /___/ /  / /_/ / /_/ / /_  \n\____/_/   \__, / .___/\__/  \n          /____/_/           \n\n"
host = '127.0.0.1'
port = 8888

# Initialisation
print(title)
# host = input('Input host IP to set (default = 127.0.0.1):\n> ')
# print()
# # port = int(input('Input host port to set:\n> '))
# print()
# cipherTitle = input('Input name for cipher key files:\n> /)
# print("Beginning cipher generation.\n")
# enCrypt.makeKeyFiles(cipherTitle, bufferSize)
# serverPW = input('Input server access password to set:\n> ')

# Socket and server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("Server started successfully.")
print("Input \'end\' to shutdown the server at any point.")

# User params
clients = []
aliases = []

# FUNCTIONS
def uIn():
    userIn = input('')
    if userIn == "end":
        print()
        print("Shutting down server.")
        print("Thank you for using Crypt.\nGoodbye.")
        exit()

def broadcast(message):
    for client in clients:
        if client:
            client.send(message)

def handle(client):                                         
    while True:
        try:                                                            
            message = client.recv(bufferSize)
            broadcast(message)
        except:                                                         
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast('{} left.'.format(alias).encode('ascii'))
            aliases.remove(alias)
            break

def receive():                                                          
    while True:
        print("Server active at {} on port {}".format(host, port))
        client, address = server.accept()
        # Get next msg and authenticate password or deny access
        print("User connected with {}".format(str(address)))       
        client.send('NICKNAME'.encode('ascii'))
        alias = client.recv(bufferSize).decode('ascii')
        aliases.append(alias)
        clients.append(client)
        print("Alias is {}".format(alias))
        broadcast("{} joined.".format(alias).encode('ascii'))
        client.send('Connected to server.'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive_thread = threading.Thread(target=receive)               
receive_thread.start()
input_thread = threading.Thread(target=uIn)                   
input_thread.start()